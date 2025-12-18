---
title: "Implementing payments tokenization"
slug: "implementing-payments-tokenization"
hidden: false
createdAt: "2025-12-01T00:00:00.00Z"
---

Payment tokenization is the VTEX solution that allows providers to process payment transactions using [tokens](https://help.vtex.com/docs/tutorials/dpan-and-fpan-understanding-security-in-the-online-tokenized-payment-flow) instead of real credit card data. This approach adds a layer of security to the process, reducing the exposure of sensitive information and the risk of fraud or attacks.

> ⚠️ This feature is currently in the testing phase (Closed Beta), which means that only select clients can access it. If you'd like to implement it in the future, contact our [Support](https://support.vtex.com/hc/en-us/).

## Benefits and features

Tokenization allows you to:

- **Integrate PCI and non-PCI systems**: Import or export tokenized cards between PCI-compliant environments (such as the VTEX gateway) and non-PCI customer systems, such as ERPs or corporate purchasing platforms (B2B).
- **Automatic token update**: Automatically assign new tokens when a credit card expires and is replaced, improving the customer experience, especially in specific recurring purchase scenarios like subscriptions.

> ℹ️ VTEX doesn't generate or request tokens from other services. It only stores tokens imported directly into the Card Token Vault (CTV) or returned by a payment provider in the authorization response.

> ⚠️ Payment tokenization is available only for stores with checkout in the [Headless](https://developers.vtex.com/docs/guides/store-architecture#headless) and [FastCheckout](https://newhelp.vtex.com/en/announcements/2024-04-03-fastcheckout-boost-your-conversion-with-the-new-checkout) architecture. The feature supports proprietary tokens from payment providers and also allows using Network Tokens when the connector acts as a Token Requester and sends the token back to VTEX.

## Steps for deployment

To make the tokenization feature available to your customers, the payment provider must:

1. [Update the connector manifest](#updating-the-connector-manifest)
2. [Configure the sending of tokenized information](#configuring-the-sending-of-tokenized-information)
3. [Integrate with the Card Token Vault (CTV)](#integrating-the-card-token-vault-ctv-system)
4. [Validate the tokenization implementation](#validating-the-deployment-of-payment-tokenization)

### Updating the connector manifest

The payment provider must include the following fields in the connector manifest:

| **Field** | **Required** | **Type** | **Description** |
| --- | --- | --- | --- |
| `version` | Yes | string | Indicates the version of the [Payment Provider Protocol (PPP)](https://help.vtex.com/en/docs/tutorials/payment-provider-protocol) to be used in requests. The default value is `1.0.0`. For card tokenization operations, use the value `2.0.0`. |
| `cardToken` | No | object | Object containing information required for card tokenization operations. This object and all its nested fields are required only when the `version` field is set to `2.0.0`. |
| `canAcceptCardToken` | No | boolean | Indicates whether the payment provider can process tokenized cards. |
| `cardTokenAcceptedTypes` | No | array | Indicates the types of tokens accepted by the payment provider. Possible values are: `TOKEN_FILE`, `TOKEN_CLIENT_ID`, and `TOKEN_VALUE`. |
| `cardGenerateCardToken` | No | boolean | Indicates whether the payment provider can generate a new card after processing a PAN card. |

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

- **Cards with PAN ([Primary Account Number](https://en.wikipedia.org/wiki/Payment_card_number)):** Cards not yet tokenized in the Card Token Vault (CTV).
- **Tokenized cards saved on VTEX:** Cards already stored in CTV and reused in a payment transaction.
- **External tokenized cards:** Tokenized cards stored in external systems, which may or may not later be saved on VTEX.

Below are examples of requests and responses for each payment transaction scenario:

#### Scenario 1: Transaction using credit card with PAN

**Payment Gateway** ([Send payments information](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/payments/transactions/-transactionId-/payments))

- **Request body:** Doesn't send specific fields for tokenization.
- **Response body:** Received fields about tokenization.

```json
[
    ...
    "fields": [
        {
            "name": "accountId",
            "value": "string"
        }
    ]
    ...
]
```

**Payment Provider Protocol** ([Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments))

- **Request body:** Fields sent for tokenization.

```json
{
    ...
    "saveCreditCard": true,
    "useCardToken": true
    ...
}
```

- **Response body:** Received fields about tokenization.

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
    ...
    "fields": {
        "accountId": "string"
    }
    ...
]
```

- **Response body:** Received fields about tokenization.

```json
[
    ...
    "fields": [
        {
            "name": "accountId",
            "value": "string"
        }
    ]
    ...
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

- **Response body:** Received fields about tokenization.

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

#### Scenario 3: Transaction using external tokenized credit card (not to be saved in VTEX)

**Payment Gateway** ([Send payments information](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/payments/transactions/-transactionId-/payments))

- **Request body:** Fields sent for tokenization.

```json
[
    ...
    "fields": [
        {
            "accountId": "null",
            "cardTokenData": {
                "cardTokenType": "TOKEN_FILE",
                "cardTokenHref": "https://linktothetokenfile.com",
                "tokenExtraData": {
                    "extraData1": "string",
                    "extraData2": "string"
                },
                "useCvvForAuthorization": "boolean",
                "cardTokenCvv": "string"
            }
        }
    ]
    ...
]
```

- **Response body:** Received fields about tokenization.

```json
[
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
    "shopperInteration": "string"
    ...
}
```

- **Response body:** Received fields about tokenization.

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

#### Scenario 4: Transaction with external tokenized credit card (to be saved in VTEX)

**Payment Gateway** ([Send payments information](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/payments/transactions/-transactionId-/payments))

- **Request body:** Fields sent for tokenization.

```json
[
    ...
    "fields": {
        "accountId": "null",
        "savePaymentData": true,
        "cardData": {
            "cardLabel": "string",
            "paymentName": "enum",
            "bin": "string",
            "lastDigits": "string"
        },
        "cardTokenData": {
            "cardTokenType": "TOKEN_FILE",
            "cardTokenHref": "https://linktothetokenfile.com",
            "tokenExtraData": {
                "extraData1": "string",
                "extraData2": "string"
            },
            "useCvvForAuthorization": "boolean",
            "cardTokenCvv": "string"
        }
    }
    ...
]
```

- **Response body:** Received fields about tokenization.

```json
[
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
]
```

**Payment Provider Protocol** ([Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments))

- **Request body:** Fields sent for tokenization.

```json
{
    ...
    "saveCreditCard": true,
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
    "shopperInteration": "string"
    ...
}
```

- **Response body:** Received fields about tokenization.

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

> ⚠️ For more information on the full payload of the requests, see the documentation for the [Send payments information](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/payments/transactions/-transactionId-/payments) and [Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) endpoints.

### Integrating the Card Token Vault (CTV) system

The **Card Token Vault (CTV)** is the VTEX system for storing and managing credit card token information. Its main features are:

- Full token CRUD (create, read, update, delete).
- Bulk import of tokens via .XLSX file.
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
| `shopperId` | No | string | Used only if none of `profileId`, `orderGroup`, or email is provided. |
| `card.paymentSystemId` | No | string | Payment system ID in the Payment Gateway. |
| `card.paymentSystemName` | Yes | string | Card brand (example: Visa, Mastercard). |
| `card.firstDigits` | Yes | string | Card BIN (first six digits). |
| `card.lastDigits` | Yes | string | The last four digits of the card. |
| `card.address.addressType` | No | string | Address type (example: residential or pickup point). |
| `card.address.addressId` | No | string | Address identifier. |
| `card.address.postalCode` | No | string | Postal code (ZIP/CEP). |
| `card.address.street` | No | string | Street name. |
| `card.address.neighborhood` | No | string | Neighborhood name. |
| `card.address.city` | No | string | City name. |
| `card.address.state` | No | string | State name. |
| `card.address.country` | No | string | Country name. |
| `card.address.number` | No | string | Street number. |
| `card.address.complement` | No | string | Address complement (example: apartment, building). |
| `card.holderName` | No | string | Name of the cardholder as printed on the card. |
| `cardTokenData.type` | Yes | string | Type of token (example: `FILE`, `TOKEN_CLIENT_ID`, `TOKEN_VALUE`). |
| `cardTokenData.value` | No | string | Token value used in transactions. |
| `cardTokenData.expiration` | Yes | string | Token expiration date in YYYY-MM format. |
| `cardTokenData.label` | No | string | Token alias (used instead of lastDigits in the UI). |
| `cardTokenData.providerCardTokenId` | No | string | Client ID used to retrieve the token from the provider. |
| `cardTokenData.useCvvForAuthorization` | No | boolean | Flag indicating if CVV is required (default: true). |
| `cardTokenData.href` | No | string | URL of the token file stored by the provider. |
| `extraData` | No | object | Dictionary <string, string> for additional data. |

Integrate with CTV using the [Card Token Vault API](https://developers.vtex.com/docs/api-reference/card-token-vault-api), available in the Developer Portal.

See the [Managing tokenized cards](https://developers.vtex.com/docs/guides/managing-tokenized-cards) guide for details on token management.

### Validating the deployment of payment tokenization


Before you start validation on the provider side, make sure you have an account set up for headless purchases (without using the VTEX Admin). Then perform purchase tests as described in the guide [Creating a regular order with the Checkout API](https://developers.vtex.com/docs/guides/creating-a-regular-order-with-the-checkout-api).


After testing headless purchases, complete the following actions to validate tokenization:

1. [Set up the account](#setting-up-the-account)
2. [Simulate a credit card purchase](#simulating-a-credit-card-purchase)
3. [Confirm data tokenization](#confirming-data-tonkenization)

#### Setting up the account

Enable tokenization on the headless account following the steps below:

1. Ask the VTEX Payments team to enable the tokenization feature.
2. Install the payment connector that will support tokenization operations on the account.

> ℹ️ If you want, you can use a VTEX test connector to simulate tokenization operations. To do this, install the connector using the command `vtex install vtex.fake-pay-io-connector@3.0.3` in the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-usage).

3. In the VTEX Admin, go to **Store Settings > Payments > Providers**, or type **Providers** in the search bar at the top of the page.
4. On the providers page, click the `New provider` button.
5. In the search bar, type the name of the installed connector and click it.
6. Complete the information requested on the configuration screen and click `Save`.
7. [Set up a payment condition](https://help.vtex.com/docs/tutorials/how-to-configure-payment-conditions) with a credit card.

#### Simulating a credit card purchase

Make a purchase using your credit card as described below:

1. Follow the purchase steps up to the **Placing the order** in the guide [Creating a regular order with the Checkout API](https://developers.vtex.com/docs/guides/creating-a-regular-order-with-the-checkout-api).
2. Send the payment information via the [Send Payments](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/payments/transactions/-transactionId-/payments) endpoint (as described in the **Resolving the order payment** section), including the `savePaymentData` field in the request.

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


To confirm the card data was tokenized and saved correctly, follow the steps below:

1. In the VTEX Admin, go to **Orders > Transactions**, or type **Providers** in the search bar at the top of the page.
2. Click the payment transaction for the purchase made in the previous section.
3. On the **Transaction events** page, find the connector authorization response event and confirm that the `generatedCardToken` dataset is present, as shown in the following example:

```
Authorization response received: [200 OK] {"status":"approved","authorizationId":"AC97443800154CA8950FA49DB8271EB4","nsu":null,"tid":"40b73bc2-ed66-4118-a6b6-1726c16332a6","acquirer":null,"delayToAutoSettle":3600,"isNewTokenization":true,"generatedCardToken":{"cardTokenType":"TOKEN_VALUE","cardTokenValue":"******","cardTokenExpiryMonth":"08","cardTokenExpiryYear":"2037","cardTokenHref":null,"cardTokenClientId":null,"tokenExtraData":null,"useCvvForAuthorization":false,"cardTokenCvv":null},"paymentId":"DA4B34B82A76497D86F69F2951F6C306","code":null,"message":"Card token payment has been approved"}
```

4. Access the [Get client profile by email](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/profiles) endpoint and confirm if the `accountId` field is being returned correctly, as shown in the example below:

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

> ℹ️ The presence of the `generatedCardToken` dataset and the `accountId` field confirms the connector processed tokenization correctly and the token has been assigned to the buyer's profile.
