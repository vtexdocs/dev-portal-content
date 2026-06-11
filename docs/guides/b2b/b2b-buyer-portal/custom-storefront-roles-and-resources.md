---
title: "Custom storefront roles and resources"
slug: "custom-storefront-roles-and-resources"
hidden: false
excerpt: "Learn how to create and manage custom storefront roles and resources to extend the B2B Buyer Portal permission model for your account's specific needs."
createdAt: "2026-06-09T00:00:00.000Z"
updatedAt: "2026-06-09T00:00:00.000Z"
seeAlso:
 - "/docs/guides/storefront-roles"
---

> ⚠️ This feature is available only for stores using [B2B Buyer Portal](https://help.vtex.com/docs/tutorials/b2b-buyer-portal), currently available for selected accounts.

The B2B Buyer Portal permission model is built on [predefined storefront roles and resources](https://developers.vtex.com/docs/guides/storefront-roles) provided by VTEX. When the native set does not cover all the permission scenarios your business requires, you can extend it by creating custom storefront roles and resources scoped to your account.

Custom storefront roles and resources follow the same model as native ones, but are fully owned and managed by your account via the [Storefront Roles API](https://developers.vtex.com/docs/api-reference/storefront-roles-api#overview).

## Key concepts

- **Custom storefront resource**: An account-defined permission key representing a specific capability not covered by the native VTEX storefront resources. Once created, a resource key is immutable.
- **Custom storefront role**: An account-defined grouping of storefront resources. Custom roles can include both native VTEX storefront resources and custom resources belonging to your account.

## Constraints

Before working with custom roles and resources, keep the following limits and rules in mind:

- An account can have a maximum of 10 custom storefront resources.
- Custom resource keys must be 5–80 characters, unique within the account, and must not match any native VTEX resource key. Keys are treated as case-insensitive and can't be changed after creation. See the [Storefront Roles](https://developers.vtex.com/docs/guides/storefront-roles) guide for the list of native resource keys to avoid conflicts.
- Custom role names must be 1–100 characters, unique within the account, and must not match any native VTEX role name. See the [Storefront Roles](https://developers.vtex.com/docs/guides/storefront-roles) guide for the list of native role names.
- A custom role must be unassigned from all users before it can be deleted.
- Native roles and resources can't be modified or deleted through the custom role and resource endpoints.

## Before you begin

All endpoints require the Storefront Roles feature to be enabled on your account. Requests sent to accounts without this feature return a `403 Forbidden` error.

Any user or [API key](https://developers.vtex.com/docs/guides/authentication-overview#api-keys) must have the appropriate [License Manager resources](https://help.vtex.com/docs/tutorials/license-manager-resources) as described in the table below. Otherwise, they will receive a status code `403` error.

| Product | Category | Resource | Associated endpoints |
| :---- | :---- | :---- | :---- |
| License Manager | Services access control | View Storefront User Permissions | `GET` [List storefront roles](https://developers.vtex.com/docs/api-reference/storefront-roles-api#get-/api/license-manager/storefront/role) <br/> `GET` [Get storefront role](https://developers.vtex.com/docs/api-reference/storefront-roles-api#get-/api/license-manager/storefront/role/-roleId-) <br/> `GET` [List storefront resources](https://developers.vtex.com/docs/api-reference/storefront-roles-api#get-/api/license-manager/storefront/resource) |
| License Manager | Services access control | Edit Storefront User Permissions | `POST` [Create custom storefront role](https://developers.vtex.com/docs/api-reference/storefront-roles-api#post-/api/license-manager/storefront/role) <br/> `PUT` [Update custom storefront role](https://developers.vtex.com/docs/api-reference/storefront-roles-api#put-/api/license-manager/storefront/role/-roleId-) <br/> `DELETE` [Delete custom storefront role](https://developers.vtex.com/docs/api-reference/storefront-roles-api#delete-/api/license-manager/storefront/role/-roleId-) <br/> `POST` [Create custom storefront resource](https://developers.vtex.com/docs/api-reference/storefront-roles-api#post-/api/license-manager/storefront/resource) <br/> `DELETE` [Delete custom storefront resource](https://developers.vtex.com/docs/api-reference/storefront-roles-api#delete-/api/license-manager/storefront/resource/-id-) |

To learn more about machine authentication at VTEX, see [Authentication overview](https://developers.vtex.com/docs/guides/authentication-overview#machine-authentication).

## Managing custom storefront resources

Custom storefront resources define new permission keys that your account can use when building custom roles.

### Creating a custom storefront resource

Use `POST` [Create custom storefront resource](https://developers.vtex.com/docs/api-reference/storefront-roles-api#post-/api/license-manager/storefront/resource) to create a new resource key for your account.

> ℹ️ Use `GET` [List storefront resources](https://developers.vtex.com/docs/api-reference/storefront-roles-api#get-/api/license-manager/storefront/resource) before creating a resource to verify that your intended key does not conflict with any existing native or custom resource key.

**Example request body:**

```json
{
  "Key": "report_viewer",
  "Name": "Report Viewer",
  "Description": "Allows access to reporting"
}
```

**Example response — `201 Created`:**

```json
{
  "Id": 42,
  "Key": "report_viewer",
  "Name": "Report Viewer",
  "Description": "Allows access to reporting"
}
```

### Listing storefront resources

Use `GET` [List storefront resources](https://developers.vtex.com/docs/api-reference/storefront-roles-api#get-/api/license-manager/storefront/resource) to retrieve all storefront resources visible to the account, including native VTEX resources and your account's own custom resources. An empty array is a valid response.

**Example response — `200 OK`:**

```json
[
  {
    "Id": 1,
    "Key": "ViewUsers",
    "Name": "View Users",
    "Description": null,
    "IsCustom": false
  },
  {
    "Id": 42,
    "Key": "report_viewer",
    "Name": "Report Viewer",
    "Description": "Allows access to reporting",
    "IsCustom": true
  }
]
```

### Deleting a custom storefront resource

Use `DELETE` [Delete custom storefront resource](https://developers.vtex.com/docs/api-reference/storefront-roles-api#delete-/api/license-manager/storefront/resource/-id-) to permanently remove a custom resource from the account.

> ⚠️ A resource can't be deleted while it is assigned to any custom role. Remove the resource from all roles that reference it before attempting to delete it. Native VTEX resources can't be deleted.

## Managing custom storefront roles

Custom storefront roles group resources into named permission sets that can then be assigned to storefront users.

### Creating a custom storefront role

Use `POST` [Create custom storefront role](https://developers.vtex.com/docs/api-reference/storefront-roles-api#post-/api/license-manager/storefront/role) to create a new role and assign resources to it.

**Example request body:**

```json
{
  "Name": "Report Viewer",
  "Resources": [1, 7]
}
```

**Example response — `201 Created`:**

```json
{
  "Id": 42,
  "Name": "Report Viewer",
  "Resources": [
    {
      "Id": 1,
      "Key": "ManageOrganizationAndContract",
      "IsCustom": false
    },
    {
      "Id": 7,
      "Key": "MyResource",
      "IsCustom": true
    }
  ]
}
```

### Listing storefront roles

Use `GET` [List storefront roles](https://developers.vtex.com/docs/api-reference/storefront-roles-api#get-/api/license-manager/storefront/role) to retrieve all storefront roles visible to the account, including native VTEX roles and your account's own custom roles. An empty array is a valid response.

**Example response — `200 OK`:**

```json
[
  {
    "Id": 1,
    "Name": "Organizational Unit Admin",
    "IsCustom": false,
    "Resources": [
      {
        "Id": 1,
        "Key": "ManageOrganizationAndContract",
        "IsCustom": false
      }
    ]
  },
  {
    "Id": 42,
    "Name": "Report Viewer",
    "IsCustom": true,
    "Resources": [
      {
        "Id": 1,
        "Key": "ManageOrganizationAndContract",
        "IsCustom": false
      },
      {
        "Id": 7,
        "Key": "MyResource",
        "IsCustom": true
      }
    ]
  }
]
```

### Getting a storefront role

Use `GET` [Get storefront role](https://developers.vtex.com/docs/api-reference/storefront-roles-api#get-/api/license-manager/storefront/role/-roleId-) to retrieve the details of a specific role by its numeric ID, including its name, whether it is custom or native, and its associated resources.

**Example response — `200 OK`:**

```json
{
  "Id": 42,
  "Name": "Report Viewer",
  "IsCustom": true,
  "Resources": [
    {
      "Id": 1,
      "Key": "ManageOrganizationAndContract",
      "IsCustom": false
    }
  ]
}
```

### Updating a custom storefront role

Use `PUT` [Update custom storefront role](https://developers.vtex.com/docs/api-reference/storefront-roles-api#put-/api/license-manager/storefront/role/-roleId-) to update a custom role's name or resource assignments.

> ℹ️ The `Resources` array in the request body replaces the role's current resource list entirely. Include all resource IDs the role should have after the update, not just the ones being added or removed. Native VTEX roles can't be updated through this endpoint.

**Example request body:**

```json
{
  "Resources": [1, 9]
}
```

**Example response — `200 OK`:**

```json
{
  "Id": 42,
  "Name": "Report Viewer",
  "Resources": [
    {
      "Id": 1,
      "Key": "ManageOrganizationAndContract",
      "IsCustom": false
    },
    {
      "Id": 9,
      "Key": "AnotherResource",
      "IsCustom": true
    }
  ]
}
```

### Deleting a custom storefront role

Use `DELETE` [Delete custom storefront role](https://developers.vtex.com/docs/api-reference/storefront-roles-api#delete-/api/license-manager/storefront/role/-roleId-) to permanently remove a custom role from the account.

> ⚠️ The role must be unassigned from all storefront users before it can be deleted. Native VTEX roles can't be deleted.

## Assigning custom roles to users

Once a custom role is created, you can assign it to storefront users using the existing role assignment endpoints, the same way you would assign any predefined role. See [Storefront Roles](https://developers.vtex.com/docs/guides/storefront-roles) for details on the assignment endpoints and the required permissions.
