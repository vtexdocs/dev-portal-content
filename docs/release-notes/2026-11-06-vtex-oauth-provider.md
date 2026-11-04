---
title: "VTEX OAuth provider"
slug: "2026-11-06-vtex-oauth-provider"
hidden: false
type: "added"
createdAt: "2026-11-06T14:00:00.000Z"
excerpt: "VTEX now has a standard OAuth provider that AI agents, MCP clients, and partner apps can use to act on behalf of a VTEX user."
---

VTEX now offers a standard [OAuth provider](https://developers.vtex.com/docs/guides/vtex-oauth-provider). AI agents, MCP clients, and partner apps can ask a VTEX user for permission and get access in the standard way, using the OAuth libraries they already know.

## What has changed?

Previously, every external client that needed to act on behalf of a VTEX user required its own custom integration. Now, clients can use the VTEX OAuth provider, which follows the OAuth 2.1 authorization code flow with PKCE. With it, you can:

- **Register clients automatically**, with [dynamic client registration](https://developers.vtex.com/docs/api-reference/vtex-id-api#post-/api/vtexid/v1/oauth/register) and no manual setup per client.
- **Keep access without asking the user to sign in again**, using [refresh tokens](https://developers.vtex.com/docs/guides/vtex-oauth-provider#refreshing-the-access-token).
- **Discover how the provider works** through the standard [authorization server metadata](https://developers.vtex.com/docs/api-reference/vtex-id-api#get-/.well-known/oauth-authorization-server/-tenant-) and [OpenID Connect discovery](https://developers.vtex.com/docs/api-reference/vtex-id-api#get-/.well-known/openid-configuration) documents, and verify tokens on your own with the [JWKS endpoint](https://developers.vtex.com/docs/api-reference/vtex-id-api#get-/.well-known/jwks.json) or [token introspection](https://developers.vtex.com/docs/api-reference/vtex-id-api#post-/api/vtexid/v1/oauth/introspect).

The endpoints are available in the [VTEX ID API](https://developers.vtex.com/docs/api-reference/vtex-id-api), under the **OAuth provider** tag.

## Why did we make this change?

VTEX didn't have a standard OAuth provider, so each client that needed to act on behalf of a VTEX user had to build a custom integration. This release is the first step toward fixing that.

## What needs to be done?

No action is required. Existing authentication methods keep working.

To use the VTEX OAuth provider in your client, follow the [VTEX OAuth provider](https://developers.vtex.com/docs/guides/vtex-oauth-provider) guide.
