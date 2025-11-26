---
title: "Policies"
slug: "vtex-io-documentation-policies"
hidden: false
excerpt: "Learn about policies in VTEX IO and what they are used for."
createdAt: "2020-07-16T20:35:02.107Z"
updatedAt: "2025-11-04T20:12:00.000Z"
seeAlso:
  - "https://developers.vtex.com/docs/guides/accessing-external-resources-within-a-vtex-io-app"
  - "https://developers.vtex.com/docs/guides/controlling-access-to-app-resources"
---
Policies are a set of permissions granted to a resource ([VRN](https://developers.vtex.com/docs/guides/vtex-io-documentation-vrn)) or a [role](https://developers.vtex.com/docs/guides/vtex-io-documentation-roles) that allows or forbids them to execute a given set of actions in an account, such as making a request to the platform.

In VTEX IO, apps interact with policies in two ways:

- Apps that want [access to an **external resource**](https://developers.vtex.com/docs/guides/accessing-external-resources-within-a-vtex-io-app), such as an endpoint from another VTEX IO app.
- Apps that [securely expose their own resources and define how to access them](https://developers.vtex.com/docs/guides/controlling-access-to-app-resources).

## Types of policies

There are two kinds of policies: role-based and resource-based. Both are based on [AWS's IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).

> Understanding the difference between role-based and resource-based policies is especially important when exposing a new policy, since the type determines where the policy must be declared and how it will be evaluated by the platform.

As the name suggests, **role-based policies** are associated with a role in the platform, for example, a role assumed by an app. In this case, these policies must be declared in the `policies.json` file in the app's root folder.

**Resource-based policies**, in turn, are policies assigned to a resource in the platform, such as an API endpoint. In this case, the resource itself must declare which apps, users, and services it trusts, and provide information about the context in which those roles should be trusted. Since an app declares its routes in a `service.json` file, this is also the file in which the resource-based policies must be declared.
