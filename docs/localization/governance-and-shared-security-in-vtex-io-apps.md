---
title: "Governance and shared security in VTEX IO apps"
slug: "governance-and-shared-security-in-vtex-io-apps"
excerpt: "Understand the responsibilities of VTEX, developers, and clients about IO apps"
hidden: false
createdAt: "2025-08-28T16:30:00.000Z"
updatedAt: "2025-08-28T16:30:00.000Z"
---

In VTEX IO, each [app](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-a-vtex-app) is a resource on the platform. This means it can interact with other systems on its behalf. These interactions must be duly authorized by the [Sponsor user](https://help.vtex.com/en/tutorial/what-is-the-sponsor-user--3oPr7YuIkEYqUGmEqIMSEy) or an [account administrator](https://help.vtex.com/en/tutorial/predefined-roles--jGDurZKJHvHJS13LnO7Dy#user-administrator-restricted).

Security and governance in this environment follow a shared responsibility model:

- VTEX provides and maintains the core security infrastructure.
- Clients manage tokens and access at the account level.
- App developers declare the necessary permissions their apps require.

The sections below outline these responsibilities in detail.

## VTEX responsibilities

- Generate the [available tokens](https://developers.vtex.com/docs/guides/app-authentication-using-auth-tokens) in the context of VTEX IO.
- Maintenance of the access control infrastructure and license verification via [License Manager](https://help.vtex.com/en/tutorial/license-manager-resources).
- Protecting the token lifecycle.
- Monitoring and responding to incidents in the ecosystem.

## Client responsibilities

- Create the necessary tokens for apps that integrate with external (third-party) services.
- Monitor how tokens are used.
- Revoke or rotate tokens periodically to minimize security risks.

## App developer responsibilities

- Declare the necessary permissions and roles to access any API the app uses in the [`manifest.json` file](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest).
- Choose how permissions are handled when creating an app:
  1. **User-level permission:** The app only allows actions that match the permissions of the user's assigned token.
  2. **App-level permission:** The app operates using its own token, granting users the permissions defined for the app itself. This may expand the user’s access beyond what their individual token would normally allow.

Therefore, when creating an app, carefully evaluate the level of permission to be granted for each available token. Assigning unnecessary or excessive permissions can expose the account to security risks.

See also:

- [App authentication using auth tokens](https://developers.vtex.com/docs/guides/app-authentication-using-auth-tokens)
- [Discovering VTEX Commerce APIs and authentication](https://developers.vtex.com/docs/guides/calling-commerce-apis-2-discovering-vtex-commerce-apis-and-authentication)
- [GraphQL authorization in IO apps](https://developers.vtex.com/docs/guides/graphql-authorization-in-io-apps)
- [Security Shared Responsibility Model](https://compliance.vtex.com/?itemUid=b80a34d3-b6a1-47ca-b274-d6ab7de4749c)
