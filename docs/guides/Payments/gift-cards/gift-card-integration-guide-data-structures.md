---
title: "How do gift cards work?"
slug: "gift-card-integration-guide-data-structures"
hidden: true
createdAt: "2020-07-01T02:24:37.898Z"
updatedAt: "2020-10-16T02:29:18.408Z"
excerpt: "Understand the gift card provider data structures and behaviors expected by VTEX Gift Card Hub."
---

Before developing your gift card provider implementation, it's important to clearly understand the data structures and the behaviors expected by Gift Card Hub. In most cases, developers will need to map the data structures and behaviors exhibited by external gift card providers and create parsing routines in their middleware to switch back and forth between standards.

## Gift Card Provider

A gift card provider is an external system that manages gift cards and their transactions.

The minimum information needed to define a provider includes:

- `id`: the provider identifier in the context of Gift Card Hub API
- `caption`: the name seen by shoppers in the store checkout
- `serviceUrl`: the base URL that should be prepended to all provider endpoints

![The name seen by shoppers in the store checkout is set by the caption parameter (e.g. My Gift Card Provider)](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/gift-card-integration-guide-data-structures-0.png)

Below you will find an example of the gift card provider data structure and more details on the usage of each parameter. Parameters that were not mentioned in our short description above can usually be set to the values in the example.

```json
{
    "id": "GiftCardExample",
    "serviceUrl": "https://giftcard--cosmetics2.myvtex.com/my-provider",
    "caption": "My Gift Card Provider",
    "oauthProvider": "vtex",
    "preAuthEnabled": true,
    "cancelEnabled": true,
    "_self": {
        "href": "cosmetics2/giftcardproviders/GiftCardExample"
    }
}
```

| Name | Type | Description | Required? |
|---|---|---|---|
| `id` | string | Gift card provider identifier for API requests | |
| `serviceUrl` | string | Base URL for all gift card provider middleware endpoints | |
| `caption` | string | Gift card provider identifier in the store checkout | |
| `oauthProvider` | string | [Webstore login provider](https://developers.vtex.com/docs/guides/login-integration-guide-webstore-oauth2) identifier in VTEX ID, used to identify users in loyalty programs | 'vtex' |
| `preAuthEnabled` | bool | Indicates whether purchases using this gift card provider should be pre-authorized | true |
| `cancelEnabled` | bool | Indicates whether purchases using this gift card provider can be cancelled | true |
| `_self` | object | Indicates the relative path where this data structure can be found in Gift Card Hub, by appending the `href` parameter to `https://api.vtex.com` | |

> ❗ **Invalid oauthProvider**
>
> Failing to define a valid `oauthProvider` will generate an error in your store's checkout. Most implementations should set this parameter to `'vtex'`

## Gift card

A gift card can work as either a redeemable gift voucher or a loyalty program. Although the data structure is the same, the required fields for each behavior are slightly different.

The minimum information needed to define a gift card includes:

- `id`: the gift card identifier in the context of Gift Card Hub API
- `balance`: the amount of credit available in the gift card
- `emissionDate`: the date when the gift card starts being valid
- `expiringDate`: the date when the gift card stops being valid

### Loyalty program

When used as a loyalty program, you should also set:

- `caption`: the gift card identifier in checkout

Below you will find an example of the gift card data structure for a loyalty program card. The `provider` and `transaction` fields are added by Gift Card Hub.

```json
{
    "id": "1",
    "balance": 100.0,
    "emissionDate": "2020-07-30T00:00:00Z",
    "expiringDate": "2030-07-30T00:00:00Z",
    "caption": "My Awesome Card 1",
    "provider": "GiftCardExample",
    "transaction": {
        "href": "cosmetics2/giftcardproviders/GiftCardExample/giftcards/1/transactions"
    }
}
```

### Redeemable voucher

When used as a redeemable gift voucher, you should also set:

- `redemptionCode`: the gift card code in checkout

Below you will find an example of the gift card data structure for a redeemable gift voucher. The `provider` and `transaction` fields are added by Gift Card Hub.

```json
{
    "id": "2",
    "balance": 50.0,
    "emissionDate": "2020-07-30T00:00:00Z",
    "expiringDate": "2030-07-30T00:00:00Z",
    "caption": "My Awesome Card 2",
    "redemptionCode": "123456",
    "provider": "GiftCardExample",
    "transaction": {
        "href": "cosmetics2/giftcardproviders/GiftCardExample/giftcards/2/transactions"
    }
}
```

> ⚠️ **Customization needed to display caption**
>
> Our default display for redeemable vouchers is simply the redemption code.
>
> If you would like to present the caption as well, you will need to customize your checkout to display it by fetching that information from the [paymentData](https://github.com/vtex/vtex.js/blob/master/docs/checkout/order-form.md#paymentData) available in the [vtex.js](https://github.com/vtex/vtex.js) orderForm object.

All the parameters that can be set when creating gift cards are listed in the table below.

| Name | Type | Description |
|---|---|---|
| `id` | string | Gift card identifier for API requests |
| `balance` | number | Credit available in gift card |
| `emissionDate` | string | Date when the gift card starts being valid (ISO 8601 format) |
| `expiringDate` | string | Date when the gift card stops being valid (ISO 8601 format) |
| `caption` | string | Gift card identifier in the store checkout that is displayed for loyalty programs |
| `relationName` | string | Relationship between the customer and the store |
| `redemptionCode` | string | Code used in the store checkout to activate redeemable vouchers |
| `redemptionToken` | string | Optional code that can be used to validate redeemable vouchers (checkout customization required for user input) |
| `provider` | string | Gift card provider identifier for API requests |
| `transaction` | object | Indicates the relative path where the transactions for this gift card can be found in Gift Card Hub, by appending the `href` parameter to `https://api.vtex.com` |

Some fields are shown in the order details page when gift cards are used to pay for an order:

- Code: `redemptionCode`
- Name: `relationName`
- Caption: `caption`
- Gift Card Issuer: `provider`

The image below illustrates how these might be presented in a specific order.

![Gift card fields seen in the order details page: redemptionCode, relationName, caption, provider](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/gift-card-integration-guide-data-structures-1.png)

## Transactions

A gift card transaction is a record of an operation that changes the gift card balance as a side-effect, such as a purchase or a refund. Our protocol expects gift cards to store their transactions for bookkeeping throughout the different stages of the purchase process.

The minimum information needed to define a transaction includes:

- `operation`: indicates whether credit should be added (`Credit`) or redeemed (`Debit`)
- `value`: the amount of credit that should be added or redeemed
- `date`: the date when the transaction occurred

Once a transaction is created, the gift card provider should allow our payments gateway to interact with the typical operations seen in the [transaction flow](https://help.vtex.com/en/tutorial/fluxo-da-transacao-no-pagamentos--Er2oWmqPIWWyeIy4IoEoQ):

- Authorization: provider verifies payment details and reserves the funds for capture
- Settlement: provider captures the funds for an authorized payment
- Cancellation: provider rejects the payment and reserved funds are released

Below you will find an example of the gift card transaction data structure and more details on the usage of each parameter. Parameters that were not mentioned in our short description above can usually be set to the values in the example.

**Transaction by ID example (recharge)**

```json
{
    "value": 254.98,
    "description": "Recarga de Gift Card",
    "redemptionMode": "6392472000000066891",
    "date": "2020-09-30T16:20:57",
    "settlement": {
        "href": "rihappy/giftcardproviders/safe/giftcards/6392472000000066891/transactions/112172/settlements"
    },
    "cancellation": {
        "href": "rihappy/giftcardproviders/safe/giftcards/6392472000000066891/transactions/112172/cancellations"
    },
    "authorization": {
        "href": "rihappy/giftcardproviders/safe/giftcards/6392472000000066891/transactions/112172/authorization"
    },
    "operation": "Credit"
}
```

**Transaction by ID example (use)**

```json
{
    "value": 254.98,
    "description": "Utilização de Gift Card",
    "redemptionMode": "6392472000000066891",
    "date": "2020-09-30T16:24:40",
    "settlement": {
        "href": "rihappy/giftcardproviders/safe/giftcards/6392472000000066891/transactions/112173/settlements"
    },
    "cancellation": {
        "href": "rihappy/giftcardproviders/safe/giftcards/6392472000000066891/transactions/112173/cancellations"
    },
    "authorization": {
        "href": "rihappy/giftcardproviders/safe/giftcards/6392472000000066891/transactions/112173/authorization"
    },
    "operation": "Debit"
}
```

When gift card transactions are listed for a specific gift card, Gift Card expects a minimal list including only the transaction IDs and references paths where full details can be found for each gift card. This allows for better performance.

```json
[
    {
        "id": "112172",
        "_self": {
            "href": "rihappy/giftcardproviders/safe/giftcards/6392472000000066891/transactions/112172"
        }
    },
    {
        "id": "112173",
        "_self": {
            "href": "rihappy/giftcardproviders/safe/giftcards/6392472000000066891/transactions/112173"
        }
    }
]
```

If your gift cards need code or not, it's all about how you implement your search endpoint. Our native provider requires redemption code and sometimes document (if restricted).

- Loyalty program: list is fine
- Gift Voucher: redemption code must return only one gift card
- Checkout validates data between search and get by id

| Name | Type | Description | Required? |
|---|---|---|---|
| `id` | | | Yes |
| `providerId` | | | |
