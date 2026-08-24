---
title: "B2B Organizations GraphQL: optional status on create mutations"
slug: "2026-08-27-b2b-organizations-graphql-optional-status-on-create-mutations"
hidden: false
type: "added"
createdAt: "2026-08-27T00:00:00.000Z"
excerpt: "The B2B Organizations GraphQL API now accepts an optional status when creating organizations, so integrations can start them as inactive or on-hold without a follow-up update call."
---

The [`vtex.b2b-organizations-graphql`](https://developers.vtex.com/docs/apps/vtex.b2b-organizations-graphql) `createOrganization` and `createOrganizationAndCostCentersWithId` mutations now accept an optional `status` argument.

## What has changed?

- `OrganizationInput` and `NormalizedOrganizationInput` now accept an optional `status: String` field, with the same canonical values as `updateOrganization`: `active`, `inactive`, and `on-hold`.
- Omitting `status` keeps the historical behavior: the organization is created as `active`.
- Creating an organization with a non-`active` status does not trigger the organization status-changed email. That email is sent only for status transitions made through `updateOrganization`.

## Why has this changed?

Previously, an organization could only be created as `active`. Setting any other status required an immediate follow-up `updateOrganization` call. This added latency and a failure risk to a common B2B onboarding flow for integrations that must start organizations in a non-active state.

## What needs to be done?

1. No action is required for existing integrations. This change is fully backward compatible.
2. To adopt it, pass `status` in the input of `createOrganization` or `createOrganizationAndCostCentersWithId`.
3. Verify the persisted status with `getOrganizationById`, not with the mutation response's `status` field, which reflects the operation result rather than the organization's lifecycle status.

## Learn more

- [Organization status on create](https://developers.vtex.com/docs/apps/vtex.b2b-organizations-graphql#organization-status-on-create)
- [B2B Organizations GraphQL API](https://developers.vtex.com/docs/guides/vtex-io-graphql-api-list)
