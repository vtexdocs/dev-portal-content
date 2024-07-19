---
title: "Changes in authentication requirements for external gift card providers"
slug: "2024-05-27-changes-in-authentication-requirements-for-external-gift-card-providers"
type: "info"
excerpt: "Authentication is required on requests to Gift Card Provider Protocol endpoints."
createdAt: "2024-05-27T00:00:00.000Z"
updatedAt: ""
---
Gift card providers will now be required to enforce authentication in their implementation of most [Gift Card Provider Protocol](https://developers.vtex.com/docs/api-reference/giftcard-provider-protocol) endpoints, using credentials they provide to merchants. From July 1, 2024 onwards, failure to enforce this requirement may result in the automatic cancellation of payment transactions associated with the non-compliant gift card provider.

## What is changing?

Gift Card Hub, our gateway that forwards all requests to integrated gift card providers using our protocol, will periodically verify if providers are actually enforcing authentication using the credentials provided in the `X-PROVIDER-API-AppKey` and `X-PROVIDER-API-AppToken` headers. This will be performed by sending verification requests with invalid credentials.

> ⚠️ If a verification request with invalid credentials receives a successful response from a gift card provider, transactions associated with that provider will be automatically canceled.

## What needs to be done?

By July 1, 2024 all gift card providers must ensure that:

1. They have provided valid credentials to all merchants using their integration
2. Merchants using their integration have stored valid credentials in their integration settings, using the [Create/Update GiftCard Provider by ID](https://developers.vtex.com/docs/api-reference/giftcard-hub-api#put-/api/giftcardproviders/-giftCardProviderId-) endpoint
3. Their implementation of [Gift Card Provider Protocol](https://developers.vtex.com/docs/api-reference/giftcard-provider-protocol) endpoints correctly enforces authentication through the appropriate headers

Note that "correctly enforcing authentication through the appropriate headers" means that requests received with missing or invalid credentials in the `X-PROVIDER-API-AppKey` and `X-PROVIDER-API-AppToken` headers should get an empty response with an HTTP status code that is either 401 or 403, depending on the scenario.
