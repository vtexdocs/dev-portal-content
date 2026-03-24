---
title: "B2B Buyer Portal integration overview"
slug: "b2b-buyer-portal-integration-overview"
hidden: false
createdAt: "2026-03-13T00:00:00.000Z"
updatedAt: "2026-03-13T00:00:00.000Z"
excerpt: "Explore the integration capabilities of B2B Buyer Portal, including contracts, organization management, payment cards, addresses, Budgets, Buying policies, Accounting fields, and Punchout."
---

> ⚠️ B2B Buyer Portal is currently available to select accounts.

B2B Buyer Portal is a set of features that enables merchants to offer B2B ecommerce experiences on top of their existing B2C store setup. It provides buyer organizations with the [Organization Account](https://help.vtex.com/docs/tutorials/organization-account), a self-service admin panel. In this panel they can manage users, organizational structure, budgets, purchasing rules, and checkout configurations.

This guide provides an overview of the integration capabilities available in B2B Buyer Portal and the APIs that support them. Each section introduces a feature area, explains its purpose, and links to the detailed integration guide or API reference.

## Table of contents

- [Architecture overview](#architecture-overview)
- [Contracts](#contracts)
- [Organization management](#organization-management)
  - [Organizational Units and scopes](#organizational-units-and-scopes)
  - [User provisioning](#user-provisioning)
  - [Storefront roles and permissions](#storefront-roles-and-permissions)
  - [Buyer data](#buyer-data)
- [Payment cards](#payment-cards)
- [Addresses](#addresses)
- [Budgets and allocations](#budgets-and-allocations)
- [Buying policies](#buying-policies)
- [Accounting fields](#accounting-fields)
  - [Default values](#default-values)
- [Punchout](#punchout)
- [Permissions](#permissions)

## Architecture overview

B2B Buyer Portal integrations are built around the following core concepts:

- **Contracts** sit at the **root** of the buyer organization. They define the commercial conditions that apply to the whole organization, such as product assortment, prices, and payment methods.
- [Organizational Units](https://help.vtex.com/en/docs/tutorials/organization-units) represent the hierarchical structure under that root, such as departments, divisions, or subsidiaries. They are the central entity for scoping many buyer portal features.
- **Storefront users** are members of the buyer organization who interact with the store, each assigned specific roles and permissions.
- **Storefront roles** control what actions each user can perform, from placing orders to managing budgets.

## Contracts

**Contracts** establish the commercial conditions between a B2B customer and your store. They centralize purchase agreement management by defining the products buyers can access, the prices that apply to them, and the payment methods they can use.

| Capability | Description |
| :--- | :--- |
| Agreement alignment | Define organization-wide conditions: assortment, pricing, and payment rules—that organizational units inherit. |
| Contract lifecycle | Create, update, and manage buyer contracts and keep commercial conditions aligned with negotiated agreements. |

Use the [B2B Contracts API](https://developers.vtex.com/docs/api-reference/b2b-contracts-api) to 
create, update, and manage contracts and their corresponding commercial conditions.

## Organization management

Organization management covers the structure, identity, and access control of a buyer organization. It includes creating and managing organizational units, provisioning users, assigning roles, and storing enriched buyer data.

These capabilities form the foundation of every B2B Buyer Portal integration since most other features (Budgets, Buying policies, accounting fields) operate within the context of organizational units and depend on users having the right storefront roles.

### Organizational units and scopes

Organizational units represent the hierarchical structure of a buyer organization. A unit can be a department, division, regional office, or any other grouping that reflects how the company organizes its purchasing operations.

Each organizational unit also supports **scopes**, which allow administrators to restrict which attributes, such as contracts, payment methods, addresses, credit cards, collections, and [accounting fields](https://help.vtex.com/en/docs/tutorials/accounting-fields), are visible and available to users within that unit.

> ℹ️ For more information about scopes, see [Scopes overview](https://help.vtex.com/en/docs/tutorials/scopes-overview).

| Capability | Description |
| :--- | :--- |
| Create and manage units | Create, list, move, edit, and delete organizational units that represent the buyer's company structure. |
| Hierarchical organization | Organize units into parent-child relationships to model the company's hierarchy. |
| Scope configuration | Restrict which contracts, payment methods, addresses, and other attributes are available per unit. |
| User assignment | Link storefront users to their respective organizational units. |

Use the [Organization Units API](https://developers.vtex.com/docs/api-reference/organization-units-api) to create, list, move, edit, and delete organizational units and to manage scopes.

### User provisioning

User provisioning covers the process of creating B2B users in VTEX and linking them to organizational units. This integration is essential when onboarding buyer organizations from external platforms or ERPs and when automating user lifecycle management.

The provisioning flow includes registering storefront credentials in VTEX ID, assigning users to organizational units, granting storefront roles, and saving enriched buyer data in the Shopper entity.

| Capability | Description |
| :--- | :--- |
| Create storefront users | Register users in VTEX ID with unique usernames and optional login emails. |
| Assign users to units | Link storefront users to their respective organizational units. |
| Assign storefront roles | Grant role-based permissions that control what each user can do. |


The key APIs related to user provisioning are:

- [VTEX ID API](https://developers.vtex.com/docs/api-reference/vtex-id-api) — Create storefront users and manage authentication identifiers.
- [Organization Units API](https://developers.vtex.com/docs/api-reference/organization-units-api) — Allocate users to organizational units.

> ℹ️ For the full step-by-step integration, see [B2B user provisioning](https://developers.vtex.com/docs/guides/b2b-user-provisioning).

### Storefront roles and permissions

Storefront roles provide a structured authorization model for B2B stores. They control which actions each user can perform, from placing orders and approving purchases to managing organizational settings and budgets.

The system ships with predefined roles (such as Buyer, Order Approver, and Organizational Unit Admin) and fine-grained resource keys that can be combined as needed.

| Capability | Description |
| :--- | :--- |
| Role assignment | Assign one or more predefined roles to storefront users via API. |
| Permission verification | Check whether a user has access to a specific storefront resource. |
| Role revocation | Remove roles from users when their responsibilities change. |

Use the [Storefront Roles API](https://developers.vtex.com/docs/api-reference/storefront-roles-api) to assign, revoke, and query storefront roles and resource permissions.

> ℹ️ For the full list of available roles, resources, and required permissions, see [Storefront Roles](https://developers.vtex.com/docs/guides/storefront-roles).

### Buyer data

VTEX provides a dedicated API for managing enriched buyer profile data associated with B2B storefront users. Use it when you need to store, query, or update buyer-specific attributes beyond what is captured during user provisioning.

| Capability | Description |
| :--- | :--- |
| Enriched profiles | Persist and maintain buyer attributes (such as name, document, and email) beyond minimal provisioning data. |
| Read and update | Query and change buyer profile records as your integration or back office requires. |

Use the [B2B Buyer Data API](https://developers.vtex.com/docs/api-reference/b2b-buyer-data-api) to manage enriched buyer profile data.

## Payment cards

Saved payment cards are first-class data in B2B Buyer Portal: they can be tied to a **contract** (shared payment methods for the organization or unit) or to a **shopper** (personal cards for individual buyers), similar to how other entities such as budgets or users are scoped. Tokenized card data is managed through the Card Token Vault API.

| Capability | Description |
| :--- | :--- |
| Tokenized storage | Store and reference payment cards securely without handling raw card data in your integration. |
| Lifecycle management | Add, update, list, or retire saved cards according to your checkout and Organization Account flows. |

Use the [Card Token Vault API](https://developers.vtex.com/docs/api-reference/card-token-vault-api) to store and manage tokenized payment card data for contract- or shopper-scoped cards.

## Addresses

Shipping destinations, internal delivery points, and contacts support checkout and fulfillment for buyer organizations.

| Capability | Description |
| :--- | :--- |
| Physical addresses | Create, search, update, and manage shipping and billing addresses for buyer organizations. |
| Checkout and account usage | Supply address data consumed in checkout, default values, and the Organization Account. |
| Delivery locations | Register internal delivery points (docks, departments, areas). |
| Contact information | Manage people who can be selected as shipment recipients at organization level. |

**Addresses** represent shipping and billing destinations. Integrations typically use the Addresses endpoints in the [Master Data API v1](https://developers.vtex.com/docs/api-reference/masterdata-api) to create, search, update, and manage addresses used in checkout and the Organization Account.

A **location** is a specific delivery point within a site, such as a dock, department, or internal area. For example, freight may be consigned to the company’s street address while the actual delivery is to **Dock 3456**. Locations are managed through the [Custom Fields API](https://developers.vtex.com/docs/api-reference/custom-fields-api). See [Custom Fields integration](https://developers.vtex.com/docs/guides/custom-fields-integration) to learn more.

**Contacts** are the people who can be chosen as **order recipients**, who will receive the shipment. At checkout, the buyer selects the recipient for the order. That person may be different from the user placing the order. Contact records are maintained at the **organization** level and can be **associated with addresses**, so choosing a shipping address can narrow which recipients are offered. Use the [B2B Contact Information API](https://developers.vtex.com/docs/api-reference/b2b-contact-information-api) to manage contacts in B2B scenarios.

## Budgets and allocations

Budgets allow buyer organizations to define spending envelopes and distribute them across allocations tied to specific entities such as accounting fields, users, or addresses. During checkout, the system queries applicable allocations so that orders can be funded according to the organization's financial rules.

| Capability | Description |
| :--- | :--- |
| Budget provisioning | Create and manage budgets with total amounts, validity periods, auto-reset, and carry-over settings. |
| Allocation management | Subdivide budgets into allocations linked to specific entities (accounting fields, users, addresses). |
| Checkout lookup | Query applicable allocations at checkout to determine how an order should be funded. |
| Balance tracking | Track remaining balances and spending history through transactions and statements. |

Use the [Budgets API](https://developers.vtex.com/docs/api-reference/budgets-api) to create, update, query, and delete budgets and allocations.

> ℹ️ For the complete integration flow, see [Budgets and allocations](https://developers.vtex.com/docs/guides/budgets-and-allocations).

## Buying policies

Buying policies enable buyer organizations to define dynamic authorization rules that control whether orders are automatically approved, denied, or sent for manual review. The system evaluates rules hierarchically across organizational units, using a priority-based mechanism.

| Capability | Description |
| :--- | :--- |
| Rule configuration | Register custom rule expressions with bypass, deny, or sequential workflow behaviors. |
| Hierarchical evaluation | Evaluate rules across organizational unit dimensions in priority order. |
| Manual authorization | Support approval or denial workflows through score-based callbacks. |

Use the [Buying Policies API](https://developers.vtex.com/docs/api-reference/buying-policies-api) to create and manage authorization rules and process order approval callbacks.

> ℹ️ For details on rule evaluation, score thresholds, and required permissions, see [Buying Policies](https://developers.vtex.com/docs/guides/buying-policies).

## Accounting fields

**Accounting fields** is the B2B Buyer Portal feature that allows stores to capture additional business-specific information during checkout, such as Cost Center or PO Number. Fields can be applied at the order, item, or address level and support predefined option lists or free-form input.

| Capability | Description |
| :--- | :--- |
| Field configuration | Define field structure, type, level, and requirements per contract. |
| Value management | Create predefined values for option-type fields. |
| OrderForm application | Apply field values to shopping carts during checkout, individually or in batch. |
| Integration with budgets and policies | Use field value IDs as matching criteria in budget allocations and buying policy expressions. |

The key APIs for managing accounting fields are:

- [Custom Fields API](https://developers.vtex.com/docs/api-reference/custom-fields-api) — Field configuration, value management, and orderForm application.
- [Default Values API](https://developers.vtex.com/docs/api-reference/default-values-api) — Pre-configured checkout defaults.

> ℹ️ For the full integration flow, see [Custom Fields integration](https://developers.vtex.com/docs/guides/custom-fields-integration).

### Default values

Default values allow buyer organization administrators to pre-configure checkout preferences for each organizational unit, such as the default shipping address, billing address, credit card, and accounting field selections. When a buyer logs in, the system automatically loads these defaults, reducing manual input at checkout.

| Capability | Description |
| :--- | :--- |
| Default configuration | Define default addresses, credit cards, and accounting fields per organizational unit. |
| Automatic application | Defaults are resolved and applied to the shopper session at login. |

Use the [Default Values API](https://developers.vtex.com/docs/api-reference/default-values-api) to create, update, retrieve, and delete default value configurations.

> ℹ️ For the complete integration flow, see [Default Values integration](https://developers.vtex.com/docs/guides/default-values-integration).

## Punchout

Punchout enables integration between external eprocurement systems and the VTEX store, allowing procurement users to authenticate and browse the supplier's catalog directly from their procurement platform. The integration supports two authentication flows: one for users who already exist in VTEX and one for pre-authenticated users managed by the integrator.

| Capability | Description |
| :--- | :--- |
| Seamless login | Authenticate procurement users into the store via one-time tokens, without manual credential input. |
| Pre-authenticated flow | Support delegated login for users who don't exist in VTEX, trusting the integrator for authorization. |
| Cart transfer | Customize the Punchout cart screen so buyers can transfer their cart back to the eprocurement system for approval, with optional per-item extensions. |

Use the [Punchout API](https://developers.vtex.com/docs/api-reference/punchout-api) to start and finish punchout login flows using one-time tokens.

> ℹ️ For the full login integration, see [Punchout login integration](https://developers.vtex.com/docs/guides/punchout-login-integration). For cart transfer customization, see [Punchout cart integration](https://developers.vtex.com/docs/guides/punchout-cart-integration). For a conceptual overview, see [Punchout](https://developers.vtex.com/docs/guides/punchout).

