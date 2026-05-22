---
title: "Managing VTEX gift cards"
slug: "managing-vtex-gift-cards"
hidden: false
createdAt: "2023-10-26T00:00:00.000Z"
updatedAt: ""
---
This guide describes how to manage VTEX native gift cards from the VTEX gift card provider through the [GiftCard API](https://developers.vtex.com/docs/api-reference/giftcard-api#overview). With this API, you can perform the following actions:

- [Create a VTEX gift card](#creating-a-vtex-gift-card)
- [Check VTEX gift card details](#checking-vtex-gift-card-details)
- [Create VTEX gift card transactions](#creating-vtex-gift-card-transactions)
- [Check VTEX gift card transactions](#checking-vtex-gift-card-transactions)
- [Cancel a VTEX gift card transaction](#cancelling-a-vtex-gift-card-transaction)

> ⚠️ You can also manage VTEX gift cards using your store Admin. For more information, see [Setting up Gift Cards](https://help.vtex.com/en/tutorial/gift-card--tutorials_995).

## Creating a VTEX gift card

To create a VTEX gift card, you can use the [Create GiftCard](https://developers.vtex.com/docs/api-reference/giftcard-api#post-/giftcards) endpoint. In this request, you must send the information of the gift card you want to create.

**POST**

`https://{accountName}.{environment}.com.br/api/giftcards`

Request body

```json
{
  "relationName": "loyalty-program-test",
  "expiringDate": "2024-01-01T00:00:00",
  "caption": "Vtex Loyalty Test",
  "profileId": "92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff",
  "restrictedToOwner": false,
  "currencyCode": "BRL",
  "multipleCredits": true,
  "multipleRedemptions": false
}
```

The endpoint will return some of the previously sent detailsand new information about the created gift card, such as:

- `"id"`: gift card identification.
- `"redemptionToken"`: gift card redemption token.
- `"redemptionCode"`: gift card redemption code.
- `"balance"`: gift card balance.
- `"emissionDate"`: gift card issue date.
- `"transaction"`: transaction code for the create gift card operation.

Response body

```json
{
    "id": "92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74",
    "redemptionToken": "COCW-OZYZ-BEXN-TIMU",
    "redemptionCode": "COCW-OZYZ-BEXN-TIMU",
    "balance": 0.0,
    "relationName": "loyalty-program-test",
    "emissionDate": "2023-08-23T16:20:01.0479856Z",
    "expiringDate": "2024-01-01T00:00:00",
    "caption": "Vtex Loyal Test",
    "currencyCode": "BRL",
    "discount": false,
    "transaction": {
        "href": "/cosmetics2/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions"
    }
}
```

You can also access your store Admin (**Promotions > Gift Cards**) to confirm that the new gift card was created.

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Integration-Guides/gift-card-integration-guide/managing-vtex-gift-cards_1.png)

> ⚠️ All gift cards created via API have no balance (value 0). You can add balance amounts to new gift cards through the [Create GiftCard Transaction](https://developers.vtex.com/docs/api-reference/giftcard-api#post-/giftcards/-giftCardID-/transactions) endpoint or the VTEX Admin.

## Checking VTEX gift card details

When you want to check details about a specific gift card, you can use the [Get GiftCard by ID](https://developers.vtex.com/docs/api-reference/giftcard-api#get-/giftcards/-giftCardID-) endpoint. In this request, you must send the gift card identification (`giftCardId`) as a path parameter.

See an example below using gift card `92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74`:

**GET**

`https://{accountName}.{environment}.com.br/api/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74`

Response body

```json
{
    "id": "92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74",
    "redemptionToken": "COCW-OZYZ-BEXN-TIMU",
    "redemptionCode": "COCW-OZYZ-BEXN-TIMU",
    "balance": 0.0,
    "relationName": "loyalty-program-test",
    "emissionDate": "2023-08-23T16:20:01.047",
    "expiringDate": "2024-01-01T00:00:00",
    "caption": "Vtex Loyal Test",
    "currencyCode": "BRL",
    "discount": false,
    "transaction": {
        "href": "/cosmetics2/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions"
    }
}
```

> ⚠️ You can also check the information of a VTEX gift card using the VTEX Admin. For more information, go to **Promotions > Gift Cards > Search or Filter Results**.

## Creating VTEX gift card transactions

A gift card transaction is a record of an operation that changes the gift card balance, such as a purchase or a refund. To change balance values, you can use the [Create GiftCard Transaction](https://developers.vtex.com/docs/api-reference/giftcard-api#post-/giftcards/-giftCardID-/transactions) endpoint.

The sections below show a simulation of how to make the following changes to a gift card balance:

- Add 500 USD
- Spend 120 USD

### Adding balance to a gift card

You can use the [Create GiftCard Transaction](https://developers.vtex.com/docs/api-reference/giftcard-api#post-/giftcards/-giftCardID-/transactions) endpoint to add balance to a gift card. In this request, you must send the gift card identification (`giftCardId`) as a path parameter.

See an example below using gift card `92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74`.

**POST**

`https://{accountName}.{environment}.com.br/api/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions`

To indicate that you wish to add 500 USD to your balance, send "Credit" in the "operation" field and 500 in the "value" field.

Request body

```json
{
  "operation": "Credit",
  "value": 500,
  "description": "Opening balance",
  "redemptionToken": "COCW-OZYZ-BEXN-TIMU",
  "redemptionCode": "COCW-OZYZ-BEXN-TIMU",
  "requestId": "1"
}
```

Response body

```json
{
    "cardId": "74",
    "id": "465f2d7370f349879f4c194ac81d8e98",
    "_self": {
        "href": "cosmetics2/giftcards/74/transactions/465f2d7370f349879f4c194ac81d8e98"
    }
}
```

To confirm the new gift card balance, use the [Get GiftCard by ID](https://developers.vtex.com/docs/api-reference/giftcard-api#get-/giftcards/-giftCardID-) endpoint or the Admin dashboard.

Response body

```json
{
    "id": "92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74",
    "redemptionToken": "COCW-OZYZ-BEXN-TIMU",
    "redemptionCode": "COCW-OZYZ-BEXN-TIMU",
    "balance": 500.0000,
    "relationName": "loyalty-program-test",
    "emissionDate": "2023-08-23T16:20:01.047",
    "expiringDate": "2024-01-01T00:00:00",
    "caption": "Vtex Loyal Test",
    "currencyCode": "BRL",
    "discount": false,
    "transaction": {
        "href": "/cosmetics2/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions"
    }
}
```

Admin

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Integration-Guides/gift-card-integration-guide/managing-vtex-gift-cards_2.png)

### Removing balance from a gift card

To remove balance from a gift card, you must also use the [Create GiftCard Transaction](https://developers.vtex.com/docs/api-reference/giftcard-api#post-/giftcards/-giftCardID-/transactions) endpoint and send the gift card identification (`giftCardId`) as a path parameter.

See an example below using gift card `92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74`.

**POST**

`https://{accountName}.{environment}.com.br/api/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions`

To indicate that you wish to remove 120 USD from your balance, send the information "Debit" in the "operation" field and 120 in the "value" field.

Request body

```json
{
  "operation": "Debit",
  "value": 120,
  "description": "Payment of order 5555",
  "redemptionToken": "COCW-OZYZ-BEXN-TIMU",
  "redemptionCode": "COCW-OZYZ-BEXN-TIMU",
  "requestId": "2"
}
```

Response body

```json
{
    "cardId": "74",
    "id": "c2b69a5990404a11b26888964bed3868",
    "_self": {
        "href": "cosmetics2/giftcards/74/transactions/c2b69a5990404a11b26888964bed3868"
    }
}
```

> ⚠️ Whenever you create a new transaction, you must send a `requestId` different from the ones previously used for that gift card. Transactions that have a `requestId` value previously used on the same gift card will not be completed. Example: After creating the first credit transaction, in which you used the value "1" for `requestId`, you create a debit transaction with `requestId` equal to "2". Any other transaction for this gift card must be created with values different from "1" and "2" in the `requestId`.

To confirm the new gift card balance, use the Get GiftCard by ID endpoint or Admin dashboard.

Response body

```json
{
    "id": "92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74",
    "redemptionToken": "COCW-OZYZ-BEXN-TIMU",
    "redemptionCode": "COCW-OZYZ-BEXN-TIMU",
    "balance": 380.0000,
    "relationName": "loyalty-program-test",
    "emissionDate": "2023-08-23T16:20:01.047",
    "expiringDate": "2024-01-01T00:00:00",
    "caption": "Vtex Loyal Test",
    "currencyCode": "BRL",
    "discount": false,
    "transaction": {
        "href": "/cosmetics2/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions"
    }
}
```

Admin

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Integration-Guides/gift-card-integration-guide/managing-vtex-gift-cards_3.png)

## Checking VTEX gift card transactions

You can use the [List All GiftCard Transactions](https://developers.vtex.com/docs/api-reference/giftcard-api#get-/giftcards/-giftCardID-/transactions) endpoint to check all transactions performed on a gift card. In this request, you must send the gift card identification (`giftCardId`) as a path parameter.

See an example below using gift card `92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74`.

**GET**

`https://{accountName}.{environment}.com.br/api/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions`

Response body showing information from two transactions:

```json
[
    {
        "cardId": "92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74",
        "id": "c2b69a5990404a11b26888964bed3868",
        "_self": {
            "href": "cosmetics2/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions/c2b69a5990404a11b26888964bed3868"
        }
    },
    {
        "cardId": "92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74",
        "id": "465f2d7370f349879f4c194ac81d8e98",
        "_self": {
            "href": "cosmetics2/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions/465f2d7370f349879f4c194ac81d8e98"
        }
    }
]
```

> ⚠️ If you use this endpoint to request details for a new gift card (which does not yet contain transactions), the response body will be empty.

### Accessing information from a gift card transaction

To get information about a specific gift card transaction, you can use the [Get GiftCard Transaction by ID](https://developers.vtex.com/docs/api-reference/giftcard-api#get-/giftcards/-giftCardID-/transactions/-transactionID-) endpoint. In this request, you must send the gift card identification (`giftCardId`) and transaction operation (`transactionId`) identification as path parameters.

> ⚠️ The `transactionID` value used in this request is the same id value obtained from the response body of the [List All GiftCard Transactions](https://developers.vtex.com/docs/api-reference/giftcard-api#get-/giftcards/-giftCardID-/transactions) endpoint. For more information, see the [Checking VTEX gift card transactions](#checking-vtex-gift-card-transactions) section.

See an example below using gift card `92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74` and transaction operation `18f71495d720497cb77dfc521f75087`.

**GET**

`https://{accountName}.{environment}.com.br/api/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_73/transactions/18f71495d720497cb77dfc521f750877`

Response body

```json
{
    "value": 58.0,
    "description": "Add 58 BRL",
    "date": "2023-08-22T22:16:23.2974622Z",
    "requestId": "10",
    "settlement": {
        "href": "/cosmetics2/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_73/transactions/18f71495d720497cb77dfc521f750877/settlements"
    },
    "cancellation": {
        "href": "/cosmetics2/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_73/transactions/18f71495d720497cb77dfc521f750877/cancellations"
    },
    "authorization": {
        "href": "/cosmetics2/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_73/transactions/18f71495d720497cb77dfc521f750877/authorization"
    },
    "operation": "Credit"
}
```

## Cancelling a VTEX gift card transaction

To partially or completely cancel a value assigned in a transaction (credit or debit), you can use the [Cancel GiftCard Transaction](https://developers.vtex.com/docs/api-reference/giftcard-api#post-/giftcards/-giftCardID-/transactions/-transactionID-/cancellations) endpoint. In this request, you must send the gift card identification (`giftCardId`) and transaction operation (`transactionId`) identification as path parameters.

> ⚠️ The transactionId value used in this request is the same id value obtained from the response body of the List All GiftCard Transactions endpoint. For more information, see the Checking VTEX gift card transactions section.

The example below shows how to partially cancel a debit transaction (`c2b69a5990404a11b26888964bed3868`). The transaction value is 120 USD and the canceled amount will be 20 USD. The gift card used is `92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74` (current balance of 380 USD).

**POST**

`https://{accountName}.{environment}.com.br/api/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions/c2b69a5990404a11b26888964bed3868/cancellations`

To indicate that you want to cancel the amount of 20 USD in the debit transaction, send 20 in the "value" field.

Request body

```json
{
  "value": 20,
  "requestId": "4"
}
```

Response body

```json
{
    "oid": "a1e7edfb72d74bfa960cdbc2eb9471ce",
    "value": 20.0,
    "date": "2023-08-23T17:28:39.7212872Z"
}
```

To confirm the new gift card balance, use the [Get GiftCard by ID](https://developers.vtex.com/docs/api-reference/giftcard-api#get-/giftcards/-giftCardID-) endpoint or the Admin dashboard.

Response body

```json
{
    "id": "92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74",
    "redemptionToken": "COCW-OZYZ-BEXN-TIMU",
    "redemptionCode": "COCW-OZYZ-BEXN-TIMU",
    "balance": 400.0000,
    "relationName": "loyalty-program-test",
    "emissionDate": "2023-08-23T16:20:01.047",
    "expiringDate": "2024-01-01T00:00:00",
    "caption": "Vtex Loyal Test",
    "currencyCode": "BRL",
    "discount": false,
    "transaction": {
        "href": "/cosmetics2/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions"
    }
}
```

Admin

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Integration-Guides/gift-card-integration-guide/managing-vtex-gift-cards_4.png)

> ⚠️ When a debit transaction is canceled, the canceled amount is credited to the total gift card balance. Likewise, when a credit transaction is canceled, the canceled amount is debited from the total gift card balance.
