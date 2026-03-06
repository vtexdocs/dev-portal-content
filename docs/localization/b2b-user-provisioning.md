---
title: "B2B user provisioning"
slug: "b2b-user-provisioning"
hidden: false
excerpt: "Learn how to migrate B2B users from external platforms to VTEX by registering users, creating organization units, and managing roles and permissions."
createdAt: "2026-02-20T00:00:00.000Z"
updatedAt: "2026-02-20T00:00:00.000Z"
---

>⚠️ This feature is in closed beta, meaning only specific customers can access it now. If you want to implement it in the future, please contact [our Support](https://support.vtex.com/hc/en-us/).

This guide explains how merchants can migrate their B2B user base from external platforms to VTEX in a secure way, including:

* Register new users in VTEX ID with unique login credentials.
* Create and manage organization units for buyer users.
* Link users to their respective organization units.
* Assign administrative roles and permissions to users.
* Register detailed user information in the Shopper entity.

## Before you begin

Before provisioning B2B users in VTEX, ensure that the necessary features are enabled and the appropriate permissions are configured:

* The [Storefront Permissions](https://developers.vtex.com/docs/guides/storefront-permissions) feature is enabled for your account. Requests to accounts without this feature enabled will receive a `403 Forbidden` response.
* Any user or [API key](https://developers.vtex.com/docs/guides/authentication-overview#api-keys) must have an admin [role](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) that contains the appropriate [License Manager resources](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3) to successfully run requests as listed in the table below. Otherwise, they will receive a `403` error.

| Product | Category | Resource | Associated endpoints |
| :---- | :---- | :---- | :---- |
| VTEX ID | User Management | Create User | `POST` [Create storefront user with username](https://developers.vtex.com/docs/api-reference/vtex-id-api#post-/api/authenticator/storefront/users) |
| Organization Units | Units | Edit Organization Unit | `POST` [Create organization unit](https://developers.vtex.com/docs/api-reference/buyer-organizations-api#post-/api/organization-units/v1) <br/><br/>`POST` [Assign user to organization unit](https://developers.vtex.com/docs/api-reference/vtex-id-api#post-/api/vtexid/organization-units/-organizationUnit-/users) |
| License Manager | Services access control | Edit Storefront User Permissions | `POST` [Assign storefront roles to user](https://developers.vtex.com/docs/api-reference/storefront-permissions-api#post-/api/license-manager/storefront/users) |
| Dynamic Storage | Dynamic storage generic resources | Insert or update document (not remove) | `POST` [Create new document](https://developers.vtex.com/docs/api-reference/masterdata-api#post-/api/dataentities/-acronym-/documents) |

### B2B shopper requirements

For effective authentication, every B2B shopper must comply with the following:

* The username needs to be unique within the tenant.
* The user needs to be linked to an organization unit.
* The user's organization unit needs to be linked with at least one valid contract.
* The user needs to be registered in the Shopper entity in Master Data v2.
* If the user is signing in with an email, they need to have a valid email address registered in the Shopper entity for receiving an access code when defining or recovering their password.

## How it works

The user provisioning process follows these main steps:

1. [Create storefront user with username](#step-1---create-storefront-user-with-username): Register new storefront users in VTEX ID with unique login credentials.
2. [Create organization unit](#step-2---create-organization-unit): Create organization units where storefront users will be assigned.
3. [Assign user to organization unit](#step-3---assign-user-to-organization-unit): Link storefront users to their respective organization units.
4. [Assign storefront roles to user](#step-4---assign-storefront-roles-to-user): Assign storefront roles and permissions to users.
5. [Save shopper data](#step-5---save-shopper-data): Register detailed user information in the Shopper entity.

The created user is still not linked to any organization unit, nor do they have a storefront permission.

## Step 1 - Create storefront user with username

Register a new user in VTEX ID. This user will be created with a mandatory `username`, which remains the primary login identifier for the storefront. The username is a case-insensitive field accepting 3 to 70 characters, including special characters (excluding whitespace).

Optionally, you may also register a login email for the user. When provided, this email can be used as an alternative login identifier, allowing the user to authenticate using either their `username` or their login email. This same login email will also be used for password recovery.

>⚠️ The login email defined in this step is different from the email collected in [Step 5](#step-5-save-shopper-data), which is used exclusively for transactional communications and does not affect authentication or password recovery.

The created user is not yet linked to any organization unit and does not have storefront permissions.

**Parameters:**

* `identifiers`: List of login keys, indicating their type and value.
* `isLegacyPassword`: Indicates whether the user should recover their password through an external service (`true`) or define a new password on first login (`false`, default).

>ℹ️ For more information, see `POST` [Create storefront user with username](https://developers.vtex.com/docs/api-reference/vtex-id-api#post-/api/authenticator/storefront/users).

>⚠️ Once a user is added, it cannot be edited or removed. If incorrect data is uploaded, create a new username.

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

>⚠️ This step is only required if the storefront user’s organization unit doesn’t exist yet. If it already exists, proceed to [Step 3 - Assign user to organization unit](#step-3--assign-user-to-organization-unit).

Organization units identify the organizations that buyer users are part of. All new units are created at the root level. To create child-level units, see the [Move organization unit](#move-organization-unit) section.

>ℹ️ For more information, see `POST` [Create organization unit](https://developers.vtex.com/docs/api-reference/buyer-organizations-api#post-/api/organization-units/v1).

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

Links a user to an organization unit, establishing their organizational membership.

>ℹ️ For more information, see `POST` [Assign user to organization unit](https://developers.vtex.com/docs/api-reference/vtex-id-api#post-/api/vtexid/organization-units/-organizationUnit-/users).

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

Storefront users can have roles in their organizations. This endpoint assigns the role(s) that the user will have within their buyer organization.

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

>ℹ️ For more information about available storefront roles and permissions, see [Storefront Permissions](https://developers.vtex.com/docs/guides/storefront-permissions). For the complete reference for this endpoint, see `POST` [Assign storefront roles to user](https://developers.vtex.com/docs/api-reference/storefront-permissions-api#post-/api/license-manager/storefront/users).

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

Shopper data is the source of truth for users' enriched profile information, including first and last name, document, telephone, email, and other details. This endpoint enables the registration of enriched user information.

In this context, the email stored in Shopper Data is used exclusively for operational and transactional account actions, such as transaction status updates and other communications related to order lifecycle and account activity.

This transactional email is distinct from the login email defined in [Step 1](#step-1-create-storefront-user-with-username), which is used for authentication and credential recovery.

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

For additional user and organization management operations, see the following API references:

* `GET` [Get user by identifier](https://developers.vtex.com/docs/api-reference/vtex-id-api#get-/api/vtexid/pvt/user/info)
* `GET` [Get organization units](https://developers.vtex.com/docs/api-reference/buyer-organizations-api#get-/api/organization-units/v1)
* `GET` [Get users from organization unit](https://developers.vtex.com/docs/api-reference/vtex-id-api#get-/api/vtexid/organization-units/-organizationUnit-/users)
* `GET` [Verify user roles](https://developers.vtex.com/docs/api-reference/storefront-permissions-api#get-/api/license-manager/storefront/users/-userId-/roles)
* `GET` [Get shopper data](https://developers.vtex.com/docs/api-reference/masterdata-api#get-/api/dataentities/-acronym-/search)
* `PATCH` [Edit organization unit](https://developers.vtex.com/docs/api-reference/buyer-organizations-api#patch-/api/organization-units/v1/-unitId-)
* `PUT` [Move organization unit](https://developers.vtex.com/docs/api-reference/buyer-organizations-api#put-/api/organization-units/v1/-unitId-/path)
* `DELETE` [Delete organization unit](https://developers.vtex.com/docs/api-reference/buyer-organizations-api#delete-/api/organization-units/v1/-unitId-)
* `DELETE` [Remove users from organization unit](https://developers.vtex.com/docs/api-reference/buyer-organizations-api#delete-/api/organization-units/v1/-unitId-/users)
