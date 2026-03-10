---
title: "B2B user provisioning"
slug: "b2b-user-provisioning"
hidden: false
excerpt: "Learn how to migrate B2B users from external platforms to VTEX by registering users, creating organization units, and managing roles and permissions."
createdAt: "2026-02-20T00:00:00.000Z"
updatedAt: "2026-02-20T00:00:00.000Z"
---

>⚠️ This feature is in closed beta, which means that only specific clients can access it now. If you want to implement it in the future, contact [VTEX Support](https://support.vtex.com/hc/en-us/).

This guide explains how merchants can migrate their B2B user base from external platforms to VTEX in a secure way, including how to:

* Register new users in VTEX ID with unique login credentials.
* Create and manage organizational units for buyer users.
* Link users to their respective organizational units.
* Assign administrative roles and permissions to users.
* Save detailed user information in the Shopper entity.

## Before you begin

Before provisioning B2B users in VTEX, make sure the required features are enabled and the appropriate permissions are configured:

* The [Storefront Permissions](https://developers.vtex.com/docs/guides/storefront-permissions) feature is enabled for your account. Requests to accounts without this feature enabled will receive a `403 Forbidden` response.
* Any user or [API key](https://developers.vtex.com/docs/guides/authentication-overview#api-keys) must have an admin [role](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) containing the appropriate [License Manager resources](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3) to successfully run requests listed in the table below. Otherwise, the requests will return a `403` error.

| Product | Category | Resource | Associated endpoints |
| :---- | :---- | :---- | :---- |
| VTEX ID | User Management | Create User | `POST` [Create storefront user with username](https://developers.vtex.com/docs/api-reference/vtex-id-api#post-/api/authenticator/storefront/users) |
| Organization Units | Units | Edit Organization Unit | `POST` [Create organizational unit](https://developers.vtex.com/docs/api-reference/organization-units-api#post-/api/organization-units/v1) <br/><br/>`POST` [Assign user to organizational unit](https://developers.vtex.com/docs/api-reference/vtex-id-api#post-/api/vtexid/organization-units/-organizationUnit-/users) |
| License Manager | Services access control | Edit Storefront User Permissions | `POST` [Assign storefront roles to user](https://developers.vtex.com/docs/api-reference/storefront-permissions-api#post-/api/license-manager/storefront/users) |
| Dynamic Storage | Dynamic storage generic resources | Insert or update document (not remove) | `POST` [Create new document](https://developers.vtex.com/docs/api-reference/masterdata-api#post-/api/dataentities/-acronym-/documents) |

### B2B shopper requirements

For effective authentication, every B2B shopper must comply with the following:

* The username must be unique within the tenant.
* The user must be linked to an organizational unit.
* The user's organizational unit must be linked with at least one valid contract.
* The user must be registered in the Shopper entity in Master Data v2.
* If the user signs in with an email, they must have a valid email address registered in the Shopper entity to receive an access code when defining or recovering their password.

## How it works

The user provisioning process follows these main steps:

1. [Create storefront user with username](#step-1---create-storefront-user-with-username): Register new storefront users in VTEX ID with unique login credentials.
2. [Create organizational unit](#step-2---create-organizational-unit): Create organizational units where storefront users will be assigned.
3. [Assign user to organizational unit](#step-3---assign-user-to-organizational-unit): Link storefront users to their respective organizational units.
4. [Assign storefront roles to user](#step-4---assign-storefront-roles-to-user): Assign storefront roles and permissions to users.
5. [Save shopper data](#step-5---save-shopper-data): Register detailed user information in the Shopper entity.

At this stage, the created user is not yet linked to an organizational unit, nor do they have storefront permissions.

## Step 1 - Create storefront user with username

Register a new user in VTEX ID. You must create this user with a required `username`, which remains the primary login identifier for the storefront. The username is a case-insensitive field that accepts 3 to 70 characters, including special characters (except whitespace).

Optionally, you may also register a login email for the user. When provided, the user can use this email address as an alternative login identifier to authenticate using either their `username` or their login email address. This same login email will also be used for password recovery.

>⚠️ The login email address defined in this step is different from the email address collected in [Step 5](#step-5-save-shopper-data), which is used exclusively for transactional communications and does not affect authentication or password recovery.

At this stage, the created user is not yet linked to an organizational unit, nor do they have storefront permissions.

**Parameters:**

* `identifiers`: List of login keys, indicating their type and value.
* `isLegacyPassword`: Indicates whether the user should recover their password through an external service (`true`) or define a new password on their first login (`false`, default).

>ℹ️ For more information, see `POST` [Create storefront user with username](https://developers.vtex.com/docs/api-reference/vtex-id-api#post-/api/authenticator/storefront/users).

>⚠️ Once you create a user, you can’t edit or remove it. If you upload incorrect data, create a new user with a new username.

### Request example

```shell
curl -X POST "https://{{accountname}}.vtexcommercestable.com.br/api/authenticator/storefront/users?isLegacyPassword=false" \
  -H "X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}" \
  -H "X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}" \
  -H "Content-Type: application/json" \
  -d '{
  "identifiers": [
    {
        "type": "username", 
        "value": "beneson_test_21"
    }, 
    {
        "type": "email", 
        "value": "beneson2010@gmail.com+4"
    }, 
    {
        "type": "phoneNumber", 
        "value": "415‑602‑8838"
    }
  ]
}'
```

### Response example

```json
{
  "userId": "f0a15a42-f7fc-4b09-a9ab-fabc76d9f332",
  "identifier": "beneson_test_21"
}
```

## Step 2 - Create organization unit

>⚠️ This step is required only if the storefront user's organizational unit does not exist yet. If it already exists, proceed to [Step 3 - Assign user to organizational unit](#step-3--assign-user-to-organizational-unit).

Organizational units identify the organizations that buyer users are part of. All new units are created at the root level. To create child-level units, see the [Move organizational unit](#move-organizational-unit) section.

>ℹ️ For more information, see `POST` [Create organization unit](https://developers.vtex.com/docs/api-reference/organization-units-api#post-/api/organization-units/v1).

### Request example

```shell
curl -X POST "https://{{accountName}}.vtexcommercestable.com.br/api/organization-units/v1" \
  -H "X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}" \
  -H "X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}" \
  -H "Content-Type: application/json" \
  -d '{
   "name": "marketing-department"
}'
```

### Response example

```json

{
  "createdAt": "2025-03-19T21:28:13.103978Z",
  "updatedAt": "2025-03-19T21:28:13.103978Z",
  "name": "marketing-department",
  "path": {
    "ids": "qastore/b13531bb-8242-43fd-80f5-3263dd4e9cdd/92264b68-74da-4fc4-b51a-9ddcb8baf29a"
  },
  "id": "92264b68-74da-4fc4-b51a-9ddcb8baf29a",
  "customerGroup": {
    "customerIds": []
  }
}

```

## Step 3 - Assign user to organization unit

Links a user to an organizational unit, establishing their organizational membership.

>ℹ️ For more information, see `POST` [Assign user to organizational unit](https://developers.vtex.com/docs/api-reference/vtex-id-api#post-/api/vtexid/organization-units/-organizationUnit-/users).

### Request example

```shell
curl -X POST "https://{{accountName}}.vtexcommercestable.com.br/api/vtexid/organization-units/{{organizationUnit}}/users" \
  -H "X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}" \
  -H "X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}" \
  -H "Content-Type: application/json" \
  -d '{
    "userIds": [ "468cc9c0-e8bd-4826-b7a6-13dce147dc26" ]
  }'
```

### Response example

```json

{
  "organizationUnitId": "b13531bb-8242-43fd-80f5-3263dd4e9cdd",
  "addedUserIds": [
    "468cc9c0-e8bd-4826-b7a6-13dce147dc26"
  ],
  "failedUserIds": []
}

```

## Step 4 - Assign storefront roles to user

Storefront users can have roles in their organizations. This endpoint assigns the role(s) the user will have within their buyer organization.

Each storefront role has a unique `roleId` (integer). The available roles and their permissions are:

| Role ID | Storefront role | Associated resources |
| :---- | :---- | :---- |
| 1 | Organizational Unit Admin | ManageOrganizationAndContract |
| 2 | Order Approver | ApproveOrders |
| 3 | Order Modifier | ModifyOrders |
| 4 | Buyer | PlaceOrders |
| 5 | Personal Cards User | UseAdHocCard, SavePrivateCard |
| 6 | Contract Manager | ViewMyContractOrders |
| 7 | Buyer Organization Manager | ViewMyOrgUnitOrders |
| 8 | Contract Viewer | ViewProfile, ViewMyCards, ViewAddresses |
| 9 | Address Manager | ManageAddresses |

>ℹ️ For more information about available storefront roles and permissions, see [Storefront Permissions](https://developers.vtex.com/docs/guides/storefront-permissions). For the complete endpoint reference, see `POST` [Assign storefront roles to user](https://developers.vtex.com/docs/api-reference/storefront-permissions-api#post-/api/license-manager/storefront/users).

### Request example

```shell
curl -X POST "https://{{accountName}}.vtexcommercestable.com.br/api/license-manager/storefront/user/roles" \
  -H "X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}" \
  -H "X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "f0a15a42-f7fc-4b09-a9ab-fabc76d9f332",
    "roleIds": [1, 4, 5]
  }'
```

### Response example

```json
{
  "id": "f0a15a42-f7fc-4b09-a9ab-fabc76d9f332",
  "roles": [
    {
      "id": 1,
      "name": "Organizational Unit Admin"
    },
    {
      "id": 4,
      "name": "Buyer"
    },
    {
      "id": 5,
      "name": "Personal Cards User"
    }
  ]
}
```

## Step 5 - Save shopper data

Shopper data is the source of truth for enriched profile information, such as first and last name, document, phone number, email, and other details. This endpoint allows you to save enriched user information.

In this context, the email address saved in Shopper Data is used exclusively for operational and transactional account actions, such as account activity, transaction status updates, and other order-lifecycle messages.

This transactional email is different from the login email defined in [Step 1](#step-1-create-storefront-user-with-username), which is used for authentication and password recovery.

>ℹ️ For more information, see `POST` [Create new document](https://developers.vtex.com/docs/api-reference/master-data-api-v2#post-/api/dataentities/-dataEntityName-/documents).

### Request example

```shell
curl -X POST "https://{{accountName}}.vtexcommercestable.com.br/api/dataentities/shopper/documents?_schema=v1" \
  -H "X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}" \
  -H "X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{
    "userId": "{{userId}}",
    "firstName": "User First Name",
    "lastName": "User Last Name",
    "document": "111.444.000-00",
    "email": "user@vtex.com",
    "phone": "5583987499600",
    "documentType": "cpf",
    "cards": []
  }'
```

### Response example

```json
{
  "Id": "shopper-cbfc4f67-6ea3-11ee-83ab-0a8d18f9f827",
  "Href": "http://{{accountName}}.vtexcommercestable.com.br/api/dataentities/shopper/documents/cbfc4f67-6ea3-11ee-83ab-0a8d18f9f827",
  "DocumentId": "cbfc4f67-6ea3-11ee-83ab-0a8d18f9f827"
}
```

## Additional operations

For additional user and organizational management operations, see the following API references:

* `GET` [Get user by identifier](https://developers.vtex.com/docs/api-reference/vtex-id-api#get-/api/vtexid/pvt/user/info)
* `GET` [Get organizational units](https://developers.vtex.com/docs/api-reference/organization-units-api#get-/api/organization-units/v1)
* `GET` [Get users from organizational unit](https://developers.vtex.com/docs/api-reference/vtex-id-api#get-/api/vtexid/organization-units/-organizationUnit-/users)
* `GET` [Verify user roles](https://developers.vtex.com/docs/api-reference/storefront-permissions-api#get-/api/license-manager/storefront/users/-userId-/roles)
* `GET` [Get shopper data](https://developers.vtex.com/docs/api-reference/masterdata-api#get-/api/dataentities/-acronym-/search)
* `PATCH` [Edit organizational unit](https://developers.vtex.com/docs/api-reference/organization-units-api#patch-/api/organization-units/v1/-unitId-)
* `PUT` [Move organizational unit](https://developers.vtex.com/docs/api-reference/organization-units-api#put-/api/organization-units/v1/-unitId-/path)
* `DELETE` [Delete organizational unit](https://developers.vtex.com/docs/api-reference/organization-units-api#delete-/api/organization-units/v1/-unitId-)
* `DELETE` [Remove users from organizational unit](https://developers.vtex.com/docs/api-reference/organization-units-api#delete-/api/organization-units/v1/-unitId-/users)
