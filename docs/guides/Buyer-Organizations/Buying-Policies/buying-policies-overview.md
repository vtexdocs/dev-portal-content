---
title: "Buying Policies overview"
slug: "buying-policies-overview"
hidden: false
createdAt: "2026-01-12t17:53:09.698z"
updatedAt: "2026-01-12t17:53:09.698z"
excerpt: "With Buying Policies, merchants can configure dynamic rules and custom expressions for flexible authorization processes in B2B organizations."

---

>⚠️ The Buying Policies feature is only available for B2B Buyer Portal. Authorization from the Commerce Engineer of the account is required for usage.

The [Buying Policies](https://developers.vtex.com/docs/api-reference/buying-policies-api) system supports dynamic rules that merchants can configure to suit their specific authorization processes. It provides a mechanism for users to register custom rule expressions, offering greater flexibility and extensibility.

The approval process is hierarchical and uses a priority-based evaluation system.

## Organization unit evaluation (dimension priority)

The following are the main characteristics of organization unit evaluation:

- Each organization unit has one dimension, a container that groups its buying policies.
- Dimensions are checked in ascending priority order (lower numbers first).
- To enforce policies from lowest to highest hierarchy levels, assign descending priorities by hierarchy:
  - Top-level unit = 9999 (evaluated last)
  - Child units = 9998 (evaluated second)
  - Grandchild units = 9997 (evaluated first)
- Sibling units share the same priority.

## Policy type evaluation (rule priority)

Within each organization unit's dimension, rules are evaluated in ascending priority order with fixed assignments:

- Priority `1` = bypass (`effectType: 0`) - checked first, approves and stops evaluation.
- Priority `2` = deny (`effectType: 1`) - checked second, denies and stops evaluation.
- Priority `3` = sequential workflow (`effectType: 2`) - checked last, requires approval.

>❗ The dimension must have `requireAllRulesAcceptance: false` so the first matching rule executes and stops further evaluation, enabling bypass functionality.

## Authorization dynamics and score fields

The following sections explain the flow of rule evaluation and the score system.

### Rule evaluation flow

When an order is submitted, authorization rules are evaluated in two stages.

#### Stage 1: Rule triggering

- Rules are evaluated in priority order (bypass → deny → sequential workflow).
- The rule's expression is evaluated against the order data.
- If the expression is `true`, the rule is triggered and executes immediately, stopping further evaluation.
- The `effectType` determines what happens:
  - `0` (bypass) → Automatic approval, order proceeds.
  - `1` (deny) → Automatic denial, order is blocked.
  - `2` (sequential workflow) → Pending, requires manual authorization.
- If no rules trigger, the system moves to the next org unit's dimension (if any).

#### Stage 2: Manual authorization for pending rules

Rules with `effectType: 2` require manual approval/denial via the [Accept or deny rule](https://developers.vtex.com/docs/api-reference/buying-policies-api#post-/commercial-authorizations/-orderAuthId-/callback) endpoint.

### Score system

The `scoreInterval` object defines decision thresholds:

```json
{
  "scoreInterval": {
    "accept": 10,
    "deny": 5
  }
}
```

When calling the approval and denial endpoints, you provide a score value that determines the outcome:

| Score Value | Condition | Outcome |
| :--- | :--- | :--- |
| score ≥ `scoreInterval.accept` | score ≥ 10 | Accepted |
| score ≤ `scoreInterval.deny` | score ≤ 5 | Denied |
| Between thresholds | 5 < score < 10 | Bypassed |

>⚠️ The score is not the result of the rule's expression. It's a separate value you send when manually authorizing/denying a pending rule.

**Example:** With `accept: 10` and `deny: 5`:

- Sending `score: 100` → Rule accepted.
- Sending `score: 0` → Rule denied.
- Sending `score: 8` → Rule bypassed (authorization continues to the next rule or dimension).

## Permissions

Any user or [API key](https://developers.vtex.com/docs/guides/authentication-overview#api-keys) must have at least one of the appropriate [License Manager resources](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3) to be able to successfully use the [Buying Policies API](https://developers.vtex.com/docs/api-reference/buying-policies-api), otherwise they will receive a status code 403 error.

Each endpoint will require a different resource, which will be one of the following:

| Product | Category | Resource |
| :--- | :--- | :--- |
| Manage Buying Policies | OMS | ManageBuyingPolicies |
| View Buying Policies | OMS | ViewBuyingPolicies |
| Approve Orders | My Account / OMS | ApproveOrders |
