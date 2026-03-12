---
title: "Storefront Roles"
slug: "storefront-roles"
hidden: false
excerpt: "Learn how to manage user access and roles within the storefront using the Storefront Permissions API for B2B scenarios."
createdAt: "2025-10-09T00:00:00.000Z"
updatedAt: "2026-03-10T00:00:00.000Z"
---

> ⚠️ This feature is available only for stores using B2B Buyer Portal, currently available for selected accounts.

The [Storefront Roles API](https://developers.vtex.com/docs/api-reference/storefront-roles-api#overview) provides a structured way to manage user access and roles within the storefront. It enables organizations to define and enforce authorization policies by controlling which actions users can perform.

The Storefront Roles API allows you to:

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

The Storefront Roles API supports a wide range of business scenarios by enabling control over user access, such as:

* Granting buyers permission to place orders while restricting order approvals to designated approvers.
* Allowing managers to oversee all orders within their organizational unit.
* Enabling administrators to configure organizational structures, contracts, and user access.

## Before you begin

* All endpoints require the Storefront Roles feature to be enabled on your account. Requests sent to accounts without this feature enabled return a “Feature not enabled for this account” error.

* Any user or [API key](https://developers.vtex.com/docs/guides/authentication-overview#api-keys) must have the appropriate [License Manager resources](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3) to be able to successfully run requests to the License Manager API as listed in the table below. Otherwise, they will receive a status code 403 error.

| Product | Category | Resource | Associated endpoints |
| :---- | :---- | :---- | :---- |
| License Manager | Services access control | View Storefront User Permissions | `GET` [Check storefront user resource access](https://developers.vtex.com/docs/api-reference/storefront-roles-api#get-/api/license-manager/storefront/users/-userId-/resources/-resourceKey-/granted) <br/> `GET` [Get storefront user roles](https://developers.vtex.com/docs/api-reference/storefront-roles-api#get-/api/license-manager/storefront/users/-userId-/roles) <br/>  `GET` [Fetch storefront user roles by email](https://developers.vtex.com/docs/api-reference/storefront-roles-api#get-/api/license-manager/storefront/users/-email-/roles) <br/> `GET` [Fetch storefront user details](https://developers.vtex.com/docs/api-reference/storefront-roles-api#get-/api/license-manager/storefront/users/-userId-) |
| License Manager | Services access control | Edit Storefront User Permissions | `POST` [Assign storefront roles](https://developers.vtex.com/docs/api-reference/storefront-roles-api#post-/api/license-manager/storefront/user/roles) <br/> `POST` [Assign one storefront role](https://developers.vtex.com/docs/api-reference/storefront-roles-api#post-/api/license-manager/storefront/roles/assign) <br/> `DELETE` [Revoke storefront roles](https://developers.vtex.com/docs/api-reference/storefront-roles-api#delete-/api/license-manager/storefront/user/roles) <br/> `DELETE` [Remove storefront user](https://developers.vtex.com/docs/api-reference/storefront-roles-api#delete-/api/license-manager/storefront/remove/users/-userId-) |

To learn more about machine authentication at VTEX, see [Authentication overview](https://developers.vtex.com/docs/guides/authentication-overview#machine-authentication).

## Available storefront resources

The following resource keys are available in the system:

| Resource Key | Description |
| :---- | :---- |
| ManageOrganizationAndContract | Allows management of the organization's structure, contracts, and related settings. |
| ManageOrganizationHierarchy | Allows the user to bypass organizational unit boundaries and manage entities at the root organization level, including access and administration across all organizational units. |
| ManageUsers | Allows creation, modification, and deletion of users. |
| ManageBuyingPolicies | Allows creation, modification, and deletion of buying policies and approval workflows. |
| ViewBuyingPolicies | Grants permission to view configured buying policies, including approval rules and spending restrictions. |
| ManageBudgets | Allows full control over budget creation, editing, allocation, and deletion. |
| ViewBudget | Grants read-only access to view budget details, including allocations, limits, and spending history. |
| ManageAccountingFields | Allows creation, modification, and deletion of accounting fields. |
| ManageQuotes | Allows creation, modification, and deletion of quotes. |
| PlaceOrders | Grants the ability to create and submit orders within the system. |
| ViewMyContractOrders | Enables users to see orders placed under their assigned contract. |
| ViewMyOrgUnitOrders | Allows users to view all orders within their organizational unit. |
| ModifyOrders | Provides permission to use the change order feature for all orders that the user has access to. |
| ApproveOrders | Grants the ability to approve or reject orders based on predefined workflows. |
| ManageAddresses | Allows adding a new address during checkout and saving it for the contract or organization unit. It also allows users to change address information at checkout. |
| UseAdHocCard | Grants permission to use a new credit card at checkout. |
| SavePrivateCard | Grants permission to save a new card for the user's personal use only. |
| ViewProfile | Allows access to view profile information. |
| ManageAuthentication | Provides access to authentication settings. |
| ViewMyCards | Enables users to view their saved payment cards. |
| ViewAddresses | Allows users to view and update their saved addresses. |

## Predefined storefront roles

The system comes with these predefined storefront roles, each with specific permissions:

| Predefined storefront role | Storefront role ID | Description | Associated resources | Availability |
| :---- | :---- | :---- | :---- | :---- |
| Organizational Unit Admin | 1 | Manages the organization's structure, contracts, and related settings. | ManageOrganizationAndContract, ManageUsers, ManageBuyingPolicies, ViewBuyingPolicies, ManageBudgets, ViewBudget, ManageAccountingFields, ManageQuotes, ManageOrganizationHierarchy | UI and API |
| Order Approver | 2 | Can approve or reject orders based on predefined workflows. | ApproveOrders | UI and API |
| Order Modifier | 3 | Can use the change order feature for all orders they have access to. | ModifyOrders | UI and API |
| Buyer | 4 | Can create and submit orders within the system. | PlaceOrders | UI and API |
| Personal Cards User | 5 | Can use a new credit card at checkout and save cards for personal use only. | UseAdHocCard, SavePrivateCard | UI and API |
| Contract Manager | 6 | Can view orders placed under their assigned contract. | ViewMyContractOrders | UI and API |
| Buyer Organization Manager | 7 | Can view all orders within their organizational unit. | ViewMyOrgUnitOrders | UI and API |
| Contract Viewer | 8 | Can view profiles, payment cards, and addresses. | ViewMyCards, ViewAddresses | UI and API |
| Address Manager | 9 | Can add and manage addresses during checkout. | ManageAddresses, ViewAddresses | UI and API |
| User Manager | 10 | Can create, edit, and remove users within the buyer organization. | ManageUsers | API only |
| Buying Policy Manager | 11 | Can create, edit, and delete buying policies and approval workflows, and view buying policies. | ManageBuyingPolicies, ViewBuyingPolicies | API only |
| Budget Manager | 12 | Can create, edit, allocate, and delete budgets, and view budget details, allocations, limits, and spending history. | ManageBudgets, ViewBudget | API only |
| Accounting Field Manager | 13 | Can create, edit, and delete accounting fields. | ManageAccountingFields | API only |
| Quote Manager | 14 | Can create, edit, and delete quotes. | ManageQuotes | API only |
| Super Buyer Admin | 16 | Has full administrative control over the buyer organization's structure, including management of Organizational Units and hierarchical configuration. | ManageOrganizationHierarchy | UI and API |

> ℹ️ Roles marked as "API only" can only be assigned to users via the `POST` [Assign storefront roles](https://developers.vtex.com/docs/api-reference/storefront-roles-api#post-/api/license-manager/storefront/user/roles) or `POST` [Assign one storefront role](https://developers.vtex.com/docs/api-reference/storefront-roles-api#post-/api/license-manager/storefront/roles/assign) endpoints.
