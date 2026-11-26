---
title: "VTEX Ads Single Sign On (SSO)"
slug: "vtex-ads-single-sign-on-sso"
excerpt: "Enable seamless user authentication across environments with VTEX Ads SSO integration."
hidden: false
createdAt: "2026-06-19T00:00:00.000Z"
updatedAt: "2026-06-19T00:00:00.000Z"
---
Single Sign On (SSO) allows users to switch between environments without having to log in again. Once a user is connected to the marketplace platform, they can reuse that session to access the VTEX Ads platform.

> ℹ️ Requests to the VTEX Ads API are authenticated with the `X-Api-Key` and `X-App-Id` headers. For details, see the [VTEX Ads API overview](https://developers.vtex.com/docs/api-reference/vtex-ads-api).

## 1. Request the redirect URL

Send a `POST` request to the `/sso/marketplace` endpoint with the seller and user information. For the full request specification, including required headers and body parameters, see [Generate seller single sign-on URL](https://developers.vtex.com/docs/api-reference/vtex-ads-api#post-/sso/marketplace) in the VTEX Ads API reference.

Request example:

```bash
curl --location --request POST 'https://api-retail-media.newtail.com.br/sso/marketplace' \
--header 'X-Api-Key: XXX' \
--header 'X-App-Id: YYY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "sso_token": "sso-token-12345",
  "email": "seller@example.com",
  "user_id": "seller123",
  "name": "Seller Name",
  "marketplace_name": "My Marketplace"
}'
```

Response example:

```json
{
  "redirect_url": "https://app.ads.vtex.com/sso/auth?token=GENERATED_TOKEN"
}
```

## 2. Redirect the user to the redirect URL

Once you have the redirect URL, redirect the user to it. The user is then logged in to the platform without requiring any additional login integration.

## Login URL (user disconnection)

Optionally, you can redirect the user to a previously provided URL that is used when the user is disconnected.
