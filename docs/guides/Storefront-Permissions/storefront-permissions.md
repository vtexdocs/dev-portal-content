---
title: "Storefront Permissions"
slug: "storefront-permissions"
hidden: false
excerpt: "Learn how to manage user access and roles within the storefront using the Storefront Permissions API for B2B scenarios."
createdAt: "2025-10-09T00:00:00.000Z"
updatedAt: "2025-10-09T00:00:00.000Z"
---

The [Storefront Permissions API](https://developers.vtex.com/docs/api-reference/storefront-permissions-api#overview) provides a structured way to manage user access and roles within the storefront. It enables organizations to define and enforce authorization policies by controlling which actions users can perform.

The Storefront Permissions API allows you to:

* Assign and revoke roles for storefront users.
* Validate access by checking whether a user has permission to perform a specific action.
* Retrieve details about user roles and permissions.
* Manage access to resources such as orders, addresses, authentication settings, and payment methods.

## Key concepts

* **Storefront resources**: Fine-grained permissions that define a specific capability in the storefront (for example, `PlaceOrders`, `ApproveOrders`, `ManageAddresses`).
* **Storefront roles**: Logical groupings of resources that represent common permission sets (for example, `Buyer`, `Order Approver`, `Organizational Unit Admin`).
* **Storefront users**: Storefront identities (customers or organization members) to whom roles and resources are assigned.

## Use cases

This functionality is particularly relevant in B2B contexts, where multiple users within the same organization may require different access levels based on their role in the purchasing process.

The Storefront Permissions API supports a wide range of business scenarios by enabling control over user access, such as:

* Granting buyers permission to place orders while restricting order approvals to designated approvers.
* Allowing managers to oversee all orders within their organizational unit.
* Enabling administrators to configure organizational structures, contracts, and user access.

## Before you begin

* All endpoints require the Storefront Permissions feature to be enabled on your account. Requests sent to accounts without this feature enabled return a “Feature not enabled for this account” error.

* Any user or [API key](https://developers.vtex.com/docs/guides/authentication-overview#api-keys) must have the appropriate [License Manager resources](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3) to be able to successfully run requests to the License Manager API as listed in the table below. Otherwise, they will receive a status code 403 error.

| Product | Category | Resource | Associated endpoints |
| :---- | :---- | :---- | :---- |
| License Manager | Services access control | View Storefront User Permissions | `GET` [Check storefront user resource access](https://developers.vtex.com/docs/api-reference/storefront-permissions-api#get-/api/license-manager/storefront/users/-userId-/resources/-resourceKey-/granted) <br/> `GET` [Fetch storefront user roles by ID](https://developers.vtex.com/docs/api-reference/storefront-permissions-api#get-/api/license-manager/storefront/users/-userId-/roles) <br/>  `GET` [Fetch storefront user roles by email](https://developers.vtex.com/docs/api-reference/storefront-permissions-api#get-/api/license-manager/storefront/users/-email-/roles) <br/> `GET` [Fetch storefront user details](https://developers.vtex.com/docs/api-reference/storefront-permissions-api#get-/api/license-manager/storefront/users/-userId-) |
| License Manager | Services access control | Edit Storefront User Permissions | `POST` [Create storefront user](https://developers.vtex.com/docs/api-reference/storefront-permissions-api#post-/api/license-manager/storefront/users/) <br/> `POST` [Assign storefront role to user](https://developers.vtex.com/docs/api-reference/storefront-permissions-api#post-/api/license-manager/storefront/roles/assign) <br/> `DELETE` [Revoke storefront role from user](https://developers.vtex.com/docs/api-reference/storefront-permissions-api#delete-/api/license-manager/storefront/roles/revoke) <br/> `DELETE` [Remove storefront user](https://developers.vtex.com/docs/api-reference/storefront-permissions-api#delete-/api/license-manager/storefront/remove/users/-userId-) |

To learn more about machine authentication at VTEX, see [Authentication overview](https://developers.vtex.com/docs/guides/authentication-overview#machine-authentication).

## Available storefront resources

The following resource keys are available in the system:

| Resource Key | Description |
| :---- | :---- |
| ManageOrganizationAndContract | Allows management of the organization's structure, contracts, and related settings. |
| PlaceOrders | Grants the ability to create and submit orders within the system. |
| ViewMyContractOrders | Enables users to see orders placed under their assigned contract. |
| ViewMyOrgUnitOrders | Allows users to view all orders within their organizational unit. |
| ModifyOrders | Provides permission to use the change order feature for all orders that the user has access to. |
| ApproveOrders | Grants the ability to approve or reject orders based on predefined workflows. |
| ManageAddresses | Add the address during checkout and save it for that contract/organization unit. |
| UseAdHocCard | Grants permission to use a new credit card at checkout. |
| SavePrivateCard | Grants permission to save a new card for the user's use only. |
| ViewProfile | Allows access to view the profile information. |
| ManageAuthentication | Provides access to authentication settings. |
| ViewMyCards | Enables users to view their payment cards. |
| ViewAddresses | Allows users to manage and update their saved addresses. |

## Predefined storefront roles

The system comes with these predefined storefront roles, each with specific permissions:

| Predefined storefront role | Storefront role ID | Description | Associated resources |
| :---- | :---- | :---- | :---- |
| Organizational Unit Admin | 1 | Manages the organization's structure, contracts, and related settings. | ManageOrganizationAndContract |
| Order Approver | 2 | Can approve or reject orders based on predefined workflows. | ApproveOrders |
| Order Modifier | 3 | Can use the change order feature for all orders they have access to. | ModifyOrders |
| Buyer | 4 | Can create and submit orders within the system. | PlaceOrders |
| Personal Cards User | 5 | Can use a new credit card at checkout and save cards for personal use only. | UseAdHocCard, SavePrivateCard |
| Contract Manager | 6 | Can view orders placed under their assigned contract. | ViewMyContractOrders |
| Buyer Organization Manager | 7 | Can view all orders within their organizational unit. | ViewMyOrgUnitOrders |
| Contract Viewer | 8 | Can view profiles, payment cards, and addresses. | ViewProfile, ViewMyCards, ViewAddresses |
| Address Manager | 9 | Can add and manage addresses during checkout. | ManageAddresses |
