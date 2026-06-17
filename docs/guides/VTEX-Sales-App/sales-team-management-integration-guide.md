---
title: "Sales Team Management integration guide"
slug: "sales-team-management-integration-guide"
excerpt: "Learn how to configure Sales Team Management via API."
hidden: false
createdAt: "2026-06-17T10:00:00.000Z"
updatedAt: "2026-06-17T10:00:00.000Z"
---

Sales Team Management lets you organize your sales force into a hierarchical structure using [Organization Units (OUs)](https://help.vtex.com/en/docs/tutorials/organizational-units). Each unit can contain users and B2B contracts, allowing you to control which commercial conditions are available to each team.

This guide covers the API operations needed to configure and operate Sales Team Management programmatically: creating the unit hierarchy, assigning users, and linking B2B contracts.

> ℹ️ All requests require a `VtexIdclientAutCookie` authentication header. See [Authentication](https://developers.vtex.com/docs/guides/authentication) for details.

## Data model overview

Sales Team Management is built around three core entities:

- **Organization Unit (OU)** — A node in the sales team hierarchy. Every unit must have the `type` field set to `Sales Team`. Units without a `parentId` are root-level units.
- **User** — A VTEX account user assigned to an organization unit. Users inherit the contracts linked to their unit.
- **Contract** — A B2B contract (stored in Master Data) linked to an organization unit via the `contractIds` scope. All users in the unit gain access to the contracts linked to it.

## Setup flow

Follow this sequence when setting up Sales Team Management for the first time:

1. [Create root organization units](#organization-unit-management) using the endpoint [Create organization unit](https://developers.vtex.com/docs/api-reference/organization-units-api#post-/api/organization-units/v1). Don't include the `parentId` parameter.
2. Create child units, passing the root unit's ID as the `parentId` parameter.
3. [Add users](#user-management) to each unit.
4. [Link B2B contracts](#contract-management) to the appropriate units.
5. Verify the hierarchy using the endpoints [Get all children organization units](https://developers.vtex.com/docs/api-reference/organization-units-api#get-/api/organization-units/v1/-organizationUnitId-/children) and [Get root organization units](https://developers.vtex.com/docs/api-reference/organization-units-api#get-/api/organization-units/v1/roots).
6. Verify linked contracts using the endpoint [Get organization unit scopes](https://developers.vtex.com/docs/api-reference/organization-units-api#get-/api/organization-units/v1/-organizationUnitId-/scopes).
7. Verify users and their accessible scopes using the endpoints [List users from organization unit](https://developers.vtex.com/docs/api-reference/organization-units-api#get-/api//vtexid/organization-units/-organizationUnitId-/users) and [Get user scopes](https://developers.vtex.com/docs/api-reference/organization-units-api#get-/api/organization-units/v1/users/-userId-/scopes).

## Organization unit management

Use the [Organization Units API](https://developers.vtex.com/docs/api-reference/organization-units-api) to create and manage the sales team hierarchy:

| Endpoint | Description |
| :--- | :--- |
| [Get root organization units](https://developers.vtex.com/docs/api-reference/organization-units-api#get-/api/organization-units/v1/roots) | Returns all top-level units (no parent). |
| [Search organization units](https://developers.vtex.com/docs/api-reference/organization-units-api#get-/api/organization-units/v1) | Lists all units with pagination. Always set `type=Sales Team`. |
| [Get organization unit](https://developers.vtex.com/docs/api-reference/organization-units-api#get-/api/organization-units/v1/-organizationUnitId-) | Returns the full details of a unit by ID. |
| [Create organization unit](https://developers.vtex.com/docs/api-reference/organization-units-api#post-/api/organization-units/v1) | Creates a unit. The `type` field must be `Sales Team`. Omit `parentId` to create a root unit. |
| [Rename organization unit](https://developers.vtex.com/docs/api-reference/organization-units-api#patch-/api/organization-units/v1/-organizationUnitId-) | Updates the unit name without changing its position in the hierarchy. |
| [Move organization unit](https://developers.vtex.com/docs/api-reference/organization-units-api#put-/api/organization-units/v1/-organizationUnitId-/path) | Moves a unit to a new parent. All child units move with it. Send `parentId: null` to promote to root level. |
| [Delete organization unit](https://developers.vtex.com/docs/api-reference/organization-units-api#delete-/api/organization-units/v1/-organizationUnitId-) | Permanently removes a unit. Irreversible — verify the unit has no linked users or children first. |

## User management

Use the [Organization Units API](https://developers.vtex.com/docs/api-reference/organization-units-api) to assign users to units and check their access:

| Endpoint | Description |
| :--- | :--- |
| [List users from organization unit](https://developers.vtex.com/docs/api-reference/organization-units-api#get-/api//vtexid/organization-units/-organizationUnitId-/users) | Returns all users in a unit, including IDs, emails, and roles. |
| [Add user to organization unit](https://developers.vtex.com/docs/api-reference/organization-units-api#post-/api//vtexid/organization-units/-organizationUnitId-/users) | Adds one or more users to a unit. Users must already exist in the VTEX account. |
| [Remove users from organization unit](https://developers.vtex.com/docs/api-reference/organization-units-api#delete-/api//vtexid/organization-units/-organizationUnitId-/users) | Removes users from a unit without deleting them from the account. Requires a request body with `userIds`. |
| [Get user's organization unit](https://developers.vtex.com/docs/api-reference/organization-units-api#get-/api/organization-units/v1/-userId-/unit) | Returns which unit a user belongs to. |
| [Get user scopes](https://developers.vtex.com/docs/api-reference/organization-units-api#get-/api/organization-units/v1/users/-userId-/scopes) | Returns all scopes (contracts and resources) accessible to a user through their unit. Scopes can be inherited from parent units. |

To retrieve user details and roles, use the [License Manager API](https://developers.vtex.com/docs/api-reference/license-manager-api):

- [Get user](https://developers.vtex.com/docs/api-reference/license-manager-api#get-/api/license-manager/users/-userId-) — Returns user data by ID.
- [Get user roles](https://developers.vtex.com/docs/api-reference/license-manager-api#get-/api/license-manager/users/-userId-/roles) — Returns user data and associated roles.

## Contract management

B2B contracts are stored in Master Data and linked to organization units via the `contractIds` scope. All users in a unit gain access to the contracts linked to it.

Use the [Organization Units API](https://developers.vtex.com/docs/api-reference/organization-units-api) to manage contract associations:

| Endpoint | Description |
| :--- | :--- |
| [Get organization unit scopes](https://developers.vtex.com/docs/api-reference/organization-units-api#get-/api/organization-units/v1/-organizationUnitId-/scopes) | Returns all scopes linked to a unit. Contracts are identified by `"scope": "contractIds"`. |
| [Create organization unit scope](https://developers.vtex.com/docs/api-reference/organization-units-api#post-/api/organization-units/v1/-organizationUnitId-/scopes/-scope-) | Links one or more contracts to a unit. Use `contractIds` as the `scope` parameter. Accepts multiple IDs in a single request. |
| [Delete organization unit scope](https://developers.vtex.com/docs/api-reference/organization-units-api#delete-/api/organization-units/v1/-organizationUnitId-/scopes/-scope-) | Removes one or more contracts from a unit. Users in the unit lose access to those contracts. |

To retrieve full contract details, use the [Master Data API v2](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/documents/-id-) with `dataEntityName=CL`.

## Organizational structure

Use [Get all children organization units](https://developers.vtex.com/docs/api-reference/organization-units-api#get-/api/organization-units/v1/-organizationUnitId-/children) to traverse the hierarchy below a given unit. The `shallowSearch` parameter controls the depth:

- `shallowSearch=true` — Returns direct children only.
- `shallowSearch=false` (default) — Returns the full subtree recursively. May be slower for large hierarchies.
