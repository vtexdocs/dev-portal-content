---
title: "Managing B2B prospects"
slug: "b2b-prospect-management"
hidden: false
createdAt: "2026-09-23T00:00:00.000Z"
updatedAt: "2026-09-23T00:00:00.000Z"
excerpt: "Learn how to register a B2B buyer organization as a prospect using core VTEX platform APIs, then review it and move it through approval or rejection."
---

> ⚠️ This feature is only available for stores using **[B2B Buyer Portal](https://help.vtex.com/en/docs/tutorials/b2b-buyer-portal)**, which is currently available to selected accounts.

A **prospect** is a buyer organization that has registered but is not yet cleared to buy. It is a contract held inactive while its review runs.

Prospect registration is integrator-driven. VTEX exposes no prospect-registration endpoint, so you assemble the prospect yourself by calling core platform APIs directly. Use the [B2B Contracts API](https://developers.vtex.com/docs/api-reference/b2b-contracts-api) for the `CL` contract document, the [B2B Addresses API](https://developers.vtex.com/docs/api-reference/b2b-addresses) for the `AD` address, and the [Organization Units API](https://developers.vtex.com/docs/api-reference/organization-units-api) for the unit that scopes the contract. The storefront user comes from **[Authenticator](https://developers.vtex.com/docs/api-reference/authenticator-api)**, **[License Manager](https://developers.vtex.com/docs/api-reference/license-manager-api)**, and the `shopper` entity, the **Master Data** entity that holds the storefront user's profile data.

A prospect is a `CL` document carrying three values: `prospectWorkflow` set to `PENDING`, `approved` set to `false`, and `isActive` set to `false`. Everything else on the document is a normal contract.

> ⚠️ If you omit `prospectWorkflow` when you create the `CL` document, the field stays `null` and the record is an ordinary contract, not a prospect. It will not be returned when you search for prospects by state.

This guide covers what must exist for a prospect to be reviewable, how to confirm it, and how to move the prospect between review states.

## Before you begin

- The store must have **[B2B Buyer Portal](https://help.vtex.com/en/docs/tutorials/b2b-buyer-portal)** enabled.
- Requests must be authenticated with an App Key and App Token pair or with a valid `VtexIdclientAutCookie` header. Learn more about [API authentication](https://developers.vtex.com/docs/guides/authentication-overview).
- The user or API key must hold the **[License Manager** resources](https://help.vtex.com/docs/tutorials/license-manager-resources) listed in the **Permissions** section of each endpoint you call. Writing `CL` and `AD` documents requires **Dynamic Storage** resources, the **License Manager** resource family that covers **Master Data** document operations. Reading organization units requires **Organization Units** resource.

## 1. Create the prospect contract

A prospect starts as a `CL` document. Three fields define it as a prospect rather than as an ordinary contract:

| Field              | Value at creation | Description                                                                                                                                                                                                                               |
| ------------------ | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `prospectWorkflow` | `PENDING`         | Review state of the prospect. The three values are `PENDING` (under review), `APPROVED` (review accepted the prospect), and `REJECTED` (review refused it). Stored values are uppercase. `null` means the record is an ordinary contract. |
| `approved`         | `false`           | Indicates whether the contract is approved to operate.                                                                                                                                                                                    |
| `isActive`         | `false`           | Keeps the contract inactive while its review runs.                                                                                                                                                                                        |

### Request example

```bash
curl -X POST "https://{{accountName}}.vtexcommercestable.com.br/api/dataentities/CL/documents" \
  -H "VtexIdclientAutCookie: {{VtexIdclientAutCookie}}" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{
    "email": "purchasing@acme.com",
    "firstName": "Acme",
    "lastName": "Industries",
    "corporateName": "Acme Industries Ltd",
    "tradeName": "Acme Industries",
    "document": "00000000000000",
    "documentType": "CNPJ",
    "isCorporate": true,
    "prospectWorkflow": "PENDING",
    "approved": false,
    "isActive": false
  }'
```

The response returns `documentId`, which is the contract ID. The remaining steps use it.

> ℹ️ For the complete field list and the field descriptions, see `POST` [Create contract](https://developers.vtex.com/docs/api-reference/b2b-contracts-api#post-/api/dataentities/CL/documents).

## 2. Prospect graph requirements

The contract alone is not reviewable. A prospect is a graph of records spread across several platform APIs, and the following table lists only what the prospect flow requires of each piece. For the entity-relationship context, the full field inventory, and the linking fields between these entities, see [B2B Buyer Portal Master Data architecture](https://developers.vtex.com/docs/guides/b2b-buyer-portal-master-data-architecture).

| Piece             | Owning API                                                                                                                                                                                                                                                                      | What the prospect flow requires                                                                                                                                                                                                                                       | Required before approval |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| Contract (`CL`)   | [B2B Contracts API](https://developers.vtex.com/docs/api-reference/b2b-contracts-api)                                                                                                                                                                                           | `prospectWorkflow` set to `PENDING`, `approved` set to `false`, and `isActive` set to `false`.                                                                                                                                                                        | Yes                      |
| Organization unit | [Organization Units API](https://developers.vtex.com/docs/api-reference/organization-units-api)                                                                                                                                                                                 | One unit in **Organization Units** whose `contractIds` scope contains the contract ID.                                                                                                                                                                                | Yes                      |
| Address (`AD`)    | [B2B Addresses API](https://developers.vtex.com/docs/api-reference/b2b-addresses)                                                                                                                                                                                               | At least one address whose `userId` is the contract ID and whose `isActive` is `true`.                                                                                                                                                                                | Yes                      |
| Storefront user   | [Authenticator API](https://developers.vtex.com/docs/api-reference/authenticator-api), [Storefront Roles API](https://developers.vtex.com/docs/api-reference/storefront-roles-api), and [B2B Buyer Data API](https://developers.vtex.com/docs/api-reference/b2b-buyer-data-api) | An **Authenticator** user assigned to the organization unit, storefront roles assigned in **License Manager**, and a `shopper` document holding the buyer's profile data. See [B2B user provisioning](https://developers.vtex.com/docs/guides/b2b-user-provisioning). | No                       |

> ℹ️ The storefront user is what lets the buyer sign in to their **Organization Account**. It is not part of the eligibility conditions, so a prospect can be reviewed before it has one.

## 3. Review the prospect

### 3.1 List prospects by state

To list prospects, you can use the **Master Data** search operation on the `CL` data entity and filter by `prospectWorkflow`. Values in `_where` are uppercase.

```bash
curl -X GET "https://{{accountName}}.vtexcommercestable.com.br/api/dataentities/CL/search?_where=prospectWorkflow=PENDING&_fields=id,email,corporateName,prospectWorkflow,approved,isActive" \
  -H "VtexIdclientAutCookie: {{VtexIdclientAutCookie}}" \
  -H "REST-Range: resources=0-99" \
  -H "Accept: application/json"
```

To list the contracts that never went through prospect review, filter by `_where=prospectWorkflow is null`.

> ℹ️ The `REST-Range` header is required, and a single query returns at most 100 documents. For the query syntax, pagination headers, and response shape, see `GET` [Search documents](https://developers.vtex.com/docs/api-reference/masterdata-api#get-/api/dataentities/-acronym-/search).

### 3.2 Confirm eligibility

Two conditions must hold before you approve a prospect, and both are yours to check. Run them against the contract ID returned in [Step 1](#1-create-the-prospect-contract).

First, confirm that an organization unit's `contractIds` scope contains the contract ID. The request must return at least one unit. A `204 No Content` or a `404 Not Found` response means no unit references the contract.

```bash
curl -X GET "https://{{accountName}}.vtexcommercestable.com.br/api/organization-units/v1/scope/contractIds/value/{{contractId}}" \
  -H "VtexIdclientAutCookie: {{VtexIdclientAutCookie}}" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

Second, confirm that at least one active address references the contract ID in `userId`.

```bash
curl -X GET "https://{{accountName}}.vtexcommercestable.com.br/api/dataentities/AD/search?_where=userId={{contractId}}%20AND%20isActive=true&_fields=id,userId,isActive" \
  -H "VtexIdclientAutCookie: {{VtexIdclientAutCookie}}" \
  -H "REST-Range: resources=0-10" \
  -H "Accept: application/json"
```

> ℹ️ For the full operation details, see `GET` [Find all organization units with scope value](https://developers.vtex.com/docs/api-reference/organization-units-api#get-/api/organization-units/v1/scope/-scope-/value/-scopeValue-) and `GET` [Search B2B addresses](https://developers.vtex.com/docs/api-reference/b2b-addresses#get-/api/dataentities/AD/search).

### 3.3 Approve or reject the prospect

You move a prospect between review states by updating `prospectWorkflow` on its `CL` document.

To approve a prospect, send `prospectWorkflow` as `APPROVED` together with `approved` as `true`. On a direct write to the `CL` document, you set `approved` yourself and you run the eligibility checks yourself.

> ⚠️ A direct write does not refuse an ineligible approval. Confirm first that a prospect is eligible by following the eligibility confirmation steps mentioned above.

A prospect approved through a direct write is equivalent to one approved in the prospect review interface, which runs the same checks and will not approve while those entities are missing.

To reject a prospect, send `prospectWorkflow` as `REJECTED` and keep `approved` as `false`.

Approval provisions nothing. It creates no organization unit, no address, and no storefront user, which is why those records must already exist.

```bash
curl -X PATCH "https://{{accountName}}.vtexcommercestable.com.br/api/dataentities/CL/documents/{{contractId}}" \
  -H "VtexIdclientAutCookie: {{VtexIdclientAutCookie}}" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{
    "prospectWorkflow": "APPROVED",
    "approved": true
  }'
```

`CL` documents are stored in **Master Data v1**, where a `PATCH` request updates the fields you send and leaves the other fields of the document unchanged, so a transition request carries only the fields the transition changes.

> ℹ️ For the full field list and the field descriptions, see `PATCH` [Update contract by ID](https://developers.vtex.com/docs/api-reference/b2b-contracts-api#patch-/api/dataentities/CL/documents/-contractId-). For the partial update behavior, see `PATCH` [Update partial document](https://developers.vtex.com/docs/api-reference/masterdata-api#patch-/api/dataentities/-acronym-/documents/-id-).

## After approval

An approved prospect is a contract approved to operate: `approved` carries `true`, and `prospectWorkflow` stays as `APPROVED`, keeping a record of the review on the document.

Contracts created before the prospect workflow existed carry `prospectWorkflow` as `null` and are unaffected by it.

## Next steps

Give the buyer organization its users and permissions. See [B2B user provisioning](https://developers.vtex.com/docs/guides/b2b-user-provisioning).

## Related resources

- [B2B Contracts API](https://developers.vtex.com/docs/api-reference/b2b-contracts-api)
- [Organization Units API](https://developers.vtex.com/docs/api-reference/organization-units-api)
- [Master Data API - v1](https://developers.vtex.com/docs/api-reference/masterdata-api)
- [B2B Addresses API](https://developers.vtex.com/docs/api-reference/b2b-addresses)
- [B2B user provisioning](https://developers.vtex.com/docs/guides/b2b-user-provisioning)
- [B2B Buyer Portal Master Data architecture](https://developers.vtex.com/docs/guides/b2b-buyer-portal-master-data-architecture)
- [B2B Buyer Portal integration overview](https://developers.vtex.com/docs/guides/b2b-buyer-portal-integration-overview)

