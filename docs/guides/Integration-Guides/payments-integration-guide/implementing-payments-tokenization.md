---
title: "Implementing payments tokenization"
slug: "implementing-payments-tokenization"
excerpt: "Learn how to implement payment tokenization in your VTEX store to enhance security and improve the customer experience."
hidden: false
createdAt: "2025-12-01T00:00:00.000Z"
updatedAt: "2026-09-08T00:00:00.000Z"
---

Payment tokenization is the VTEX solution that allows providers to process payment transactions using [tokens](https://help.vtex.com/docs/tutorials/dpan-and-fpan-understanding-security-in-the-online-tokenized-payment-flow) instead of real credit card data. This approach adds a layer of security to the process, reducing the exposure of sensitive information and the risk of fraud or attacks.

> ⚠️ This feature is currently in the testing phase (Closed Beta), which means that only select clients can access it. If you'd like to implement it in the future, [open a ticket](https://help.vtex.com/docs/tutorials/opening-tickets-to-vtex-support) with VTEX Technical Support.

## Benefits and features

Tokenization allows you to:

- **Integrate PCI and non-PCI systems**: Import or export tokenized cards between PCI-compliant environments (such as the VTEX gateway) and non-PCI customer systems, such as ERPs or corporate purchasing platforms (B2B).
- **Automatic token update**: Automatically assign new tokens when a credit card expires and is replaced, improving the customer experience, especially in specific recurring purchase scenarios like subscriptions.

> ℹ️ VTEX doesn't generate or request tokens from other services. It only stores tokens imported directly into the Card Token Vault (CTV) or returned by a payment provider in the authorization response.

> ⚠️ Payment tokenization is available only for stores with checkout in the [Headless](https://developers.vtex.com/docs/guides/store-architecture#headless) and [FastCheckout](https://help.vtex.com/en/announcements/2024-04-03-fastcheckout-boost-your-conversion-with-the-new-checkout) architecture. The feature supports proprietary tokens from payment providers and also allows using Network Tokens when the connector acts as a Token Requester and sends the token back to VTEX.

## Before you begin

Make sure you meet the following requirements:

| Requirement | Description |
| ----------- | ----------- |
| Closed Beta access | Request access to the feature by [opening a ticket](https://help.vtex.com/docs/tutorials/opening-tickets-to-vtex-support) with VTEX Technical Support. |
| Compatible checkout | Use a store with a [Headless](https://developers.vtex.com/docs/guides/store-architecture#headless) or FastCheckout architecture. Tokenization isn't available for other checkout architectures. |
| Payment provider integration | Have a payment connector integrated through the [Payment Provider Protocol (PPP)](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol) and approved by VTEX. |
| PPP version 2.0.0 | Declare PPP version `2.0.0` in the connector manifest. For more information about how versioning works, see [PPP versioning](https://developers.vtex.com/docs/guides/ppp-versioning). |
| Authentication credentials | Use an `X-VTEX-API-AppKey` and an `X-VTEX-API-AppToken` header to call the [Card Token Vault API](https://developers.vtex.com/docs/api-reference/card-token-vault-api). For more information, see [Authentication](https://developers.vtex.com/docs/guides/api-authentication-using-application-keys). |

## How the tokenization flow works

The following table describes how VTEX, the payment provider, and the Card Token Vault (CTV) interact when a shopper pays with a card that is tokenized for the first time:

| Step | Who acts | What happens | Key fields |
| ---- | -------- | ------------ | ---------- |
| 1 | Store | Sends the shopper's card data to VTEX through the [Send payments information](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/payments/transactions/-transactionId-/payments) endpoint, requesting that the card be saved. | `savePaymentData` |
| 2 | VTEX | Calls the payment provider's [Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) endpoint, indicating that the card must be tokenized. | `saveCreditCard`, `useCardToken` |
| 3 | Payment provider | Authorizes the transaction and returns the generated token in the authorization response. | `isNewTokenization`, `generatedCardToken` |
| 4 | VTEX | Stores the token in the CTV and links it to the shopper's profile. | `accountId` |
| 5 | Store | Reuses the stored token in later purchases, sending the account identifier instead of card data. | `accountId`, `useCardToken` |

## Steps for deployment

To make the tokenization feature available to your customers, you must:

1. [Update the connector manifest](#updating-the-connector-manifest)
2. [Configure the sending of tokenized information](#configuring-the-sending-of-tokenized-information)
3. [Integrate with the Card Token Vault (CTV)](#integrating-the-card-token-vault-ctv-system)
4. [Validate the tokenization implementation](#validating-the-deployment-of-payment-tokenization)

### Updating the connector manifest

Include the following fields in the connector manifest:

| **Field** | **Required** | **Type** | **Description** |
| --- | --- | --- | --- |
| `version` | Yes | string | Indicates the version of the [Payment Provider Protocol (PPP)](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol) to be used in requests. The default value is `1.0.0`. For card tokenization operations, use the value `2.0.0`. |
| `cardToken` | No | object | Groups the information required for card tokenization operations. This object and all its nested fields are required only when the `version` field is set to `2.0.0`. |
| `cardToken.canAcceptCardToken` | No | boolean | Indicates whether the payment provider can process tokenized cards. |
| `cardToken.cardTokenAcceptedTypes` | No | array | Indicates the types of tokens accepted by the payment provider. Possible values are: `FILE`, `TOKEN_CLIENT_ID`, and `TOKEN_VALUE`. |
| `cardToken.canGenerateCardToken` | No | boolean | Indicates whether the payment provider can generate a card token after processing a card with a [Primary Account Number (PAN)](https://en.wikipedia.org/wiki/Payment_card_number). |

Example of a manifest with tokenization enabled:

```json
{
    ...
    "version": "2.0.0",
    "cardToken": {
        "canAcceptCardToken": true,
        "cardTokenAcceptedTypes": ["TOKEN_VALUE"],
        "canGenerateCardToken": true
    }
    ...
}
```

> ⚠️ After reviewing the manifest, [open a ticket](https://help.vtex.com/docs/tutorials/opening-tickets-to-vtex-support) with VTEX Technical Support to request the connector update.

### Configuring the sending of tokenized information

In addition to updating the manifest, you must include specific fields in the [Payment Gateway](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/payments/transactions/-transactionId-/payments) and [Payment Provider Protocol](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) endpoints, according to the type of credit card used in the tokenized transaction.
Card types are classified as follows:

- **Cards with PAN:** Cards not yet tokenized in the Card Token Vault (CTV).
- **Tokenized cards saved on VTEX:** Cards already stored in CTV and reused in a payment transaction.
- **External tokenized cards:** Tokenized cards stored in external systems, which may or may not later be saved on VTEX.

The following sections show examples of requests and responses for each payment transaction scenario. The payloads are partial, and the ellipsis (`...`) indicates the other fields of the payload.

#### Scenario 1: Transaction using credit card with PAN

**Payment Gateway** ([Send payments information](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/payments/transactions/-transactionId-/payments))

- **Request body:** No specific fields for tokenization.
- **Response body:** Fields received for tokenization.

```json
[
    {
        ...
        "fields": [
            {
                "name": "accountId",
                "value": "string"
            }
        ]
        ...
    }
]
```

**Payment Provider Protocol** ([Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments))

- **Request body:** Fields sent for tokenization.

```json
{
    ...
    "saveCreditCard": true,
    "useCardToken": false
    ...
}
```

- **Response body:** Fields received for tokenization.

```json
{
    ...
    "isNewTokenization": true,
    "generatedCardToken": {
        "cardTokenType": "TOKEN_VALUE",
        "cardTokenHref": "string",
        "tokenExtraData": {
            "extraData1": "string",
            "extraData2": "string"
        },
        "useCvvForAuthorization": true
    }
    ...
}
```

> ℹ️ When the `saveCreditCard` field is sent with the value `false` in the request body of the [Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) endpoint, VTEX won't store the credit card and the response body won't return tokenization data.

#### Scenario 2: Transaction using tokenized credit card stored in VTEX

**Payment Gateway** ([Send payments information](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/payments/transactions/-transactionId-/payments))

- **Request body:** Fields sent for tokenization.

```json
[
    {
        ...
        "fields": {
            "accountId": "string"
        }
        ...
    }
]
```

- **Response body:** Fields received for tokenization.

```json
[
    {
        ...
        "fields": [
            {
                "name": "accountId",
                "value": "string"
            }
        ]
        ...
    }
]
```

**Payment Provider Protocol** ([Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments))

- **Request body:** Fields sent for tokenization.

```json
{
    ...
    "saveCreditCard": false,
    "useCardToken": true
    ...
}
```

- **Response body:** Fields received for tokenization.

```json
{
    ...
    "isNewTokenization": false,
    "generatedCardToken": {
        "cardTokenType": "TOKEN_VALUE",
        "cardTokenHref": "string",
        "tokenExtraData": {
            "extraData1": "string",
            "extraData2": "string"
        },
        "useCvvForAuthorization": true
    }
    ...
}
```

#### Scenario 3: Transaction using external tokenized credit card

This scenario covers cards tokenized in an external system. The payloads are the same whether or not the token is saved in VTEX afterward. Two fields control that behavior:

| Goal | `savePaymentData` (Payment Gateway) | `saveCreditCard` (Payment Provider Protocol) |
| ---- | ----------------------------------- | -------------------------------------------- |
| Use the external token only in the current transaction | `false` | `false` |
| Use the external token and save it in VTEX | `true` | `true` |

**Payment Gateway** ([Send payments information](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/payments/transactions/-transactionId-/payments))

- **Request body:** Fields sent for tokenization.

```json
[
    {
        ...
        "fields": {
            "isCardToken": "true",
            "savePaymentData": "false",
            "accountId": "account-guid",
            "cardTokenData": {
                "accountName": "cea",
                "providerId": "connector-id",
                "card": {
                    "firstDigits": "411111",
                    "lastDigits": "1111",
                    "holderName": "John Doe",
                    "paymentSystemId": 2,
                    "paymentSystemName": "Visa"
                },
                "cardTokenData": {
                    "cardLabel": "My card",
                    "type": "TOKEN_VALUE",
                    "value": "tok_xxx",
                    "expiration": "2032-04",
                    "useCvvForAuthorization": true
                },
                "tokenExtraData": {
                    "extraData1": "string",
                    "extraData2": "string"
                }
            }
        }
        ...
    }
]
```

- **Response body:** Fields received for tokenization.

```json
[
    {
        ...
        "fields": [
            {
                "name": "isCardToken",
                "value": "true"
            },
            {
                "name": "accountId",
                "value": "string"
            }
        ]
        ...
    }
]
```

**Payment Provider Protocol** ([Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments))

- **Request body:** Fields sent for tokenization.

```json
{
    ...
    "saveCreditCard": false,
    "useCardToken": true,
    "cardTokenData": {
        "cardTokenType": "TOKEN_VALUE",
        "cardTokenValue": "string",
        "tokenExtraData": {
            "extraData1": "string",
            "extraData2": "string"
        },
        "useCvvForAuthorization": true,
        "cardTokenCvv": "string"
    },
    "shopperInteraction": "ecommerce"
    ...
}
```

- **Response body:** Fields received for tokenization.

```json
{
    ...
    "isNewTokenization": true,
    "generatedCardToken": {
        "cardTokenType": "TOKEN_VALUE",
        "cardTokenHref": "string",
        "tokenExtraData": {
            "extraData1": "string",
            "extraData2": "string"
        },
        "useCvvForAuthorization": true
    }
    ...
}
```

> ℹ️ The `shopperInteraction` field indicates which system the shopper interacted with. Examples of values are `ecommerce`, `instore`, and `subscription`.

> ⚠️ For more information on the full payload of the requests, see the documentation for the [Send payments information](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/payments/transactions/-transactionId-/payments) and [Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) endpoints.

### Integrating the Card Token Vault (CTV) system

The **Card Token Vault (CTV)** is the VTEX system for storing and managing credit card token information. Its main features are:

- Full token CRUD (create, read, update, delete).
- Bulk import of tokens via XLSX file.
- Secure storage with [AES encryption](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard).
- Activity tracking with full audit support.

The CTV stores the following types of information for each token:

| **Field** | **Required** | **Type** | **Description** |
| --- | --- | --- | --- |
| `id` | Yes | string | Token ID in the system. |
| `accountName` | Yes | string | VTEX account name in License Manager (example: carrefourbr, cea). |
| `providerId` | Yes | string | Connector owner account name used to create the token (example: worldpay). |
| `profileId` | No | string | Profile ID in the Profile System. |
| `orderGroup` | No | string | Order identifier. |
| `email` | No | string | Used only if neither `profileId` nor `orderGroup` is provided (rare). |
| `shopperId` | No | string | Shopper identification, applicable only if a personal card is used. |
| `card.paymentSystemId` | No | string | Payment system ID in the Payment Gateway. |
| `card.paymentSystemName` | Yes | string | Card brand (example: Visa, Mastercard). |
| `card.firstDigits` | Yes | string | Card BIN (first six digits). |
| `card.lastDigits` | Yes | string | The last four digits of the card. |
| `card.address.addressType` | No | string | Address type (example: `Residential`). |
| `card.address.addressId` | No | string | Address identifier. |
| `card.address.postalCode` | No | string | Postal code (ZIP/CEP). |
| `card.address.street` | No | string | Street name. |
| `card.address.neighborhood` | No | string | Neighborhood name. |
| `card.address.city` | No | string | City name. |
| `card.address.state` | No | string | State or province. |
| `card.address.country` | No | string | Country code of the billing address, in ISO 3166 alpha-3 format (example: `BRA`). |
| `card.address.number` | No | string | Street number. |
| `card.address.complement` | No | string | Address complement (example: apartment, building). |
| `card.holderName` | No | string | Name of the cardholder as printed on the card. |
| `cardTokenData.type` | Yes | string | Type of token. Possible values are: `FILE`, `TOKEN_CLIENT_ID`, and `TOKEN_VALUE`. |
| `cardTokenData.value` | Conditional | string | Token value used in transactions. Required when `cardTokenData.type` is `TOKEN_VALUE`. |
| `cardTokenData.expiration` | Yes | string | Token expiration date in `YYYY-MM` format. |
| `cardTokenData.label` | No | string | Token alias (used instead of `lastDigits` in the UI). |
| `cardTokenData.providerCardTokenId` | Conditional | string | Client ID used to retrieve the token from the provider. Required when `cardTokenData.type` is `TOKEN_CLIENT_ID`. |
| `cardTokenData.useCvvForAuthorization` | No | boolean | Flag indicating if CVV is required (default: true). |
| `cardTokenData.href` | Conditional | string | URL of the token file stored by the provider. Required when `cardTokenData.type` is `FILE`. |
| `extraData` | No | object | Dictionary `<string, string>` for additional data. |

The value of `cardTokenData.type` determines which field must carry the token, as described in the following table:

| Token type | Required field |
| ---------- | -------------- |
| `TOKEN_VALUE` | `cardTokenData.value` |
| `TOKEN_CLIENT_ID` | `cardTokenData.providerCardTokenId` |
| `FILE` | `cardTokenData.href` |

Integrate with CTV using the [Card Token Vault API](https://developers.vtex.com/docs/api-reference/card-token-vault-api), available in the Developer Portal.

See the [Managing tokenized cards](https://developers.vtex.com/docs/guides/managing-tokenized-cards) guide for details on token management.

### Handling errors

The [Card Token Vault API](https://developers.vtex.com/docs/api-reference/card-token-vault-api) returns the following status codes when a token operation fails:

| Status code | Meaning | How to handle it |
| ----------- | ------- | ---------------- |
| `400` | Bad Request. The request data failed validation. | Check the required fields for the declared `cardTokenData.type` and the format of `cardTokenData.expiration`. |
| `401` | Unauthorized. The authentication headers are invalid or unauthorized. | Confirm that the `X-VTEX-API-AppKey` and `X-VTEX-API-AppToken` values are correct and still valid. |
| `403` | Forbidden. The authentication headers are missing. | Send both authentication headers in the request. |
| `404` | Not Found. The token isn't registered. | Confirm the token ID before retrying the request. |
| `409` | Conflict. The token already exists. | Update the existing token instead of creating a new one. |
| `500` | Internal Server Error. | Retry after a short delay. If the problem persists, [open a ticket](https://help.vtex.com/docs/tutorials/opening-tickets-to-vtex-support) with VTEX Technical Support. |

In your implementation of the [Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) endpoint, return `400` when the tokenization fields fail validation and `500` when an unexpected error prevents you from processing the request.

> ⚠️ A successful call to the [Send payments information](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/payments/transactions/-transactionId-/payments) endpoint returns the `201` status code. Any other status code means the payment data wasn't accepted, so the tokenization flow doesn't start.

### Validating the deployment of payment tokenization

Before you begin validation on the provider side, make sure you have an account set up for headless purchases (without using the VTEX Admin). Then perform purchase tests as described in the guide [Creating a regular order with the Checkout API](https://developers.vtex.com/docs/guides/creating-a-regular-order-with-the-checkout-api).

After testing headless purchases, complete the following actions to validate tokenization:

1. [Set up the account](#setting-up-the-account)
2. [Simulate a credit card purchase](#simulating-a-credit-card-purchase)
3. [Confirm data tokenization](#confirming-data-tokenization)

#### Setting up the account

To enable tokenization on the headless account, follow these instructions:

1. [Open a ticket](https://help.vtex.com/docs/tutorials/opening-tickets-to-vtex-support) with VTEX Technical Support to request that the VTEX Payments team enable the tokenization feature. In the ticket, include the account name and the name of the payment connector.
2. Install the payment connector that will support tokenization operations on the account.

    > ℹ️ If you want, you can use a VTEX test connector to simulate tokenization operations. To do this, install the connector using the command `vtex install vtex.fake-pay-io-connector@3.0.3` in the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-usage).

3. In the VTEX Admin, go to **Store Settings > Payments > Providers**, or type **Providers** in the search bar at the top of the page.
4. On the providers page, click the `New provider` button.
5. In the search bar, type the name of the installed connector.
6. Click the connector.
7. Complete the information requested on the configuration screen.
8. Click `Save`.
9. [Set up a payment condition](https://help.vtex.com/docs/tutorials/how-to-configure-payment-conditions) with a credit card.

#### Simulating a credit card purchase

To make a purchase using your credit card, follow these instructions:

1. Follow the purchase steps up to the **Placing the order** section in the guide [Creating a regular order with the Checkout API](https://developers.vtex.com/docs/guides/creating-a-regular-order-with-the-checkout-api).
2. Send the payment data via the [Send payments information](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/payments/transactions/-transactionId-/payments) endpoint (as described in the **Resolving the order payment** section of the guide), including the `savePaymentData` field in the request.

    ```json
    [
        {
            ...
            "fields": {
                "savePaymentData": true,
                "holderName": "John Doe",
                ...
            }
            ...
        }
    ]
    ```

#### Confirming data tokenization

To confirm the card data was tokenized and saved correctly, follow these instructions:

1. In the VTEX Admin, go to **Orders > Transactions**, or type **Transactions** in the search bar at the top of the page.
2. Click the payment transaction for the purchase made in the previous section.
3. On the **Transaction events** page, find the connector authorization response event and confirm that the `generatedCardToken` dataset is present. The event starts with `Authorization response received: [200 OK]`, followed by the payload, as shown in the following example:

    ```json
    {
        "status": "approved",
        "authorizationId": "AC97443800154CA8950FA49DB8271EB4",
        "nsu": null,
        "tid": "40b73bc2-ed66-4118-a6b6-1726c16332a6",
        "acquirer": null,
        "delayToAutoSettle": 3600,
        "isNewTokenization": true,
        "generatedCardToken": {
            "cardTokenType": "TOKEN_VALUE",
            "cardTokenValue": "******",
            "cardTokenExpiryMonth": "08",
            "cardTokenExpiryYear": "2037",
            "cardTokenHref": null,
            "cardTokenClientId": null,
            "tokenExtraData": null,
            "useCvvForAuthorization": false,
            "cardTokenCvv": null
        },
        "paymentId": "DA4B34B82A76497D86F69F2951F6C306",
        "code": null,
        "message": "Card token payment has been approved"
    }
    ```

4. Access the [Get client profile by email](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/profiles) endpoint and confirm that the `accountId` field is returned correctly, as shown in the following example:

    ```json
    {
        ...
        "availableAccounts": [
            {
                "accountId": "ADA70C8D7321403510535172A6EFC3C5",
                "paymentSystem": "4",
                "paymentSystemName": "Mastercard",
                "cardNumber": "************1111",
                "bin": "111111",
                ...
            }
        ],
        "availableAddresses": {}
    }
    ```

> ℹ️ The presence of the `generatedCardToken` dataset and the `accountId` field confirms that the connector has processed the tokenization correctly and the token has been assigned to the buyer's profile.

## Learn more

- [Managing tokenized cards](https://developers.vtex.com/docs/guides/managing-tokenized-cards)
- [Card Token Vault API](https://developers.vtex.com/docs/api-reference/card-token-vault-api)
- [Payment Provider Protocol](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol)
- [PPP versioning](https://developers.vtex.com/docs/guides/ppp-versioning)
- [DPAN and FPAN: understanding security in the online tokenized payment flow](https://help.vtex.com/docs/tutorials/dpan-and-fpan-understanding-security-in-the-online-tokenized-payment-flow)
