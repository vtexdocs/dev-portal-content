---
title: "Managing VTEX gift cards"
slug: "managing-vtex-gift-cards"
hidden: false
createdAt: "2023-10-26T00:00:00.000Z"
updatedAt: "2026-09-08T00:00:00.000Z"
excerpt: "Learn how to manage VTEX native gift cards using the GiftCard API."
---
This guide describes how to manage VTEX native gift cards from the VTEX gift card provider through the [GiftCard API](https://developers.vtex.com/docs/api-reference/giftcard-api#overview). With this API, you can perform the following actions:

- [Create a VTEX gift card](#creating-a-vtex-gift-card)
- [Check VTEX gift card details](#checking-vtex-gift-card-details)
- [Create VTEX gift card transactions](#creating-vtex-gift-card-transactions)
- [Check VTEX gift card transactions](#checking-vtex-gift-card-transactions)
- [Cancel a VTEX gift card transaction](#canceling-a-vtex-gift-card-transaction)

> ⚠️ You can also manage VTEX gift cards using the VTEX Admin. For more information, see [Setting up Gift Cards](https://help.vtex.com/en/tutorial/gift-card--tutorials_995).

## Before you begin

Make sure you meet the following requirements:

| Requirement | Description |
| ----------- | ----------- |
| Authentication credentials | All GiftCard API requests require an `X-VTEX-API-AppKey` and an `X-VTEX-API-AppToken` header. For more information, see [Authentication](https://developers.vtex.com/docs/guides/api-authentication-using-application-keys). |
| Permissions | The application key must be associated with a role that includes the **Gift card full access** [License Manager resource](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3). Without it, requests return a `403` status code. |
| Customer profile ID | Every gift card is issued to a customer. To create one, you need the customer's `profileId`. You can use the customer's registered email or the `userId` value stored in [Master Data](https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw). |
| API client | You can use any HTTP client, such as cURL or Postman, to send the requests in this guide. |

> ℹ️ The examples in this guide use the account name `cosmetics2` in response payloads. Replace `accountName` and `environment` in request URLs with your own store values.

## Creating a VTEX gift card

To create a VTEX gift card, you can use the [Create GiftCard](https://developers.vtex.com/docs/api-reference/giftcard-api#post-/giftcards) endpoint. In this request, you must send the information of the gift card you want to create.

**POST**

`https://{accountName}.{environment}.com.br/api/giftcards`

The request body accepts the following fields:

| Field | Required | Description |
| ----- | -------- | ----------- |
| `relationName` | Yes | Identifies the relationship between the customer and the store. This value must be different for each gift card. |
| `expiringDate` | Yes | Sets the gift card expiration date in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format (`YYYY-MM-DDThh:mm:ss.fff`). |
| `caption` | Yes | Describes the gift card and identifies the loyalty program associated with it. |
| `profileId` | Yes | Identifies the customer, as registered in Master Data. |
| `currencyCode` | No | Sets the gift card currency in [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) format. If you omit this field, the gift card behaves as in a store with a single currency. |
| `restrictedToOwner` | No | Defines whether the gift card can be used only by the customer identified in `profileId` (`true`) or not (`false`). |
| `multipleCredits` | No | Defines whether the gift card balance can be changed (`true`) or not (`false`). Set this field to `true` to allow the credit and debit transactions described in [Creating VTEX gift card transactions](#creating-vtex-gift-card-transactions). |
| `multipleRedemptions` | No | Defines whether the gift card can be used in multiple purchases until its balance is completely used (`true`) or not (`false`). |

Request body

```json
{
  "relationName": "loyalty-program-test",
  "expiringDate": "2027-01-01T00:00:00",
  "caption": "VTEX Loyalty Test",
  "profileId": "92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff",
  "restrictedToOwner": false,
  "currencyCode": "USD",
  "multipleCredits": true,
  "multipleRedemptions": false
}
```

The endpoint returns some of the previously sent details and new information about the created gift card, such as:

- `"id"`: Gift card identification, composed of the customer's `profileId` and a sequential number, separated by an underscore.
- `"redemptionCode"`: Code the shopper enters at checkout to activate the gift card. It has a minimum of 6 characters.
- `"redemptionToken"`: Optional token used to validate the gift card. Using it requires customizing your checkout to accept the token as user input.
- `"balance"`: Gift card balance.
- `"emissionDate"`: Gift card issue date.
- `"transactions"`: URL of the gift card transactions resource.

> ℹ️ Store the `redemptionCode` and `redemptionToken` values returned in this response. The [Create GiftCard Transaction](https://developers.vtex.com/docs/api-reference/giftcard-api#post-/giftcards/-giftCardID-/transactions) endpoint requires both of them in the request body.

Response body

```json
{
    "id": "92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74",
    "redemptionToken": "b2dac6f2-f365-48cd-82a9-0b376a55557a",
    "redemptionCode": "COCW-OZYZ-BEXN-TIMU",
    "balance": 0.0000,
    "relationName": "loyalty-program-test",
    "emissionDate": "2026-09-08T16:20:01.047Z",
    "expiringDate": "2027-01-01T00:00:00",
    "caption": "VTEX Loyalty Test",
    "currencyCode": "USD",
    "discount": false,
    "transactions": {
        "href": "/cosmetics2/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions"
    }
}
```

You can also access the VTEX Admin (**Promotions > Gift Cards**) to confirm that the new gift card was created.

![VTEX Admin Gift Cards page listing the newly created gift card](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Payments/gift-cards/managing-vtex-gift-cards_1.png)

> ⚠️ All gift cards created via API have no balance (value 0). You can add balance amounts to new gift cards through the [Create GiftCard Transaction](https://developers.vtex.com/docs/api-reference/giftcard-api#post-/giftcards/-giftCardID-/transactions) endpoint or the VTEX Admin.

## Checking VTEX gift card details

When you want to check details about a specific gift card, you can use the [Get GiftCard by ID](https://developers.vtex.com/docs/api-reference/giftcard-api#get-/giftcards/-giftCardID-) endpoint. In this request, you must send the gift card identification (`giftCardId`) as a path parameter.

The following example uses gift card `92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74`:

**GET**

`https://{accountName}.{environment}.com.br/api/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74`

Response body

```json
{
    "id": "92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74",
    "redemptionToken": "b2dac6f2-f365-48cd-82a9-0b376a55557a",
    "redemptionCode": "COCW-OZYZ-BEXN-TIMU",
    "balance": 0.0000,
    "relationName": "loyalty-program-test",
    "emissionDate": "2026-09-08T16:20:01.047Z",
    "expiringDate": "2027-01-01T00:00:00",
    "caption": "VTEX Loyalty Test",
    "currencyCode": "USD",
    "discount": false,
    "transactions": {
        "href": "/cosmetics2/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions"
    }
}
```

> ⚠️ You can also check the information of a VTEX gift card using the VTEX Admin. For more information, go to **Promotions > Gift Cards > Search or Filter Results**.

## Creating VTEX gift card transactions

A gift card transaction is a record of an operation that changes the gift card balance, such as a purchase or a refund. To change balance values, you can use the [Create GiftCard Transaction](https://developers.vtex.com/docs/api-reference/giftcard-api#post-/giftcards/-giftCardID-/transactions) endpoint.

The following sections simulate these changes to the balance of gift card `92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74`:

- Add 500 USD
- Remove 120 USD

### Adding balance to a gift card

You can use the [Create GiftCard Transaction](https://developers.vtex.com/docs/api-reference/giftcard-api#post-/giftcards/-giftCardID-/transactions) endpoint to add balance to a gift card. In this request, you must send the gift card identification (`giftCardId`) as a path parameter.

**POST**

`https://{accountName}.{environment}.com.br/api/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions`

To add 500 USD to the balance, send `Credit` in the `operation` field and `500` in the `value` field.

Request body

```json
{
  "operation": "Credit",
  "value": 500,
  "description": "Opening balance",
  "redemptionToken": "b2dac6f2-f365-48cd-82a9-0b376a55557a",
  "redemptionCode": "COCW-OZYZ-BEXN-TIMU",
  "requestId": "1"
}
```

Response body

```json
{
    "cardId": "92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74",
    "id": "465f2d7370f349879f4c194ac81d8e98",
    "_self": {
        "href": "/cosmetics2/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions/465f2d7370f349879f4c194ac81d8e98"
    }
}
```

The `id` field returns the transaction identification, which you need to check or cancel that transaction later.

To confirm the new gift card balance, use the [Get GiftCard by ID](https://developers.vtex.com/docs/api-reference/giftcard-api#get-/giftcards/-giftCardID-) endpoint or the VTEX Admin.

Response body

```json
{
    "id": "92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74",
    "redemptionToken": "b2dac6f2-f365-48cd-82a9-0b376a55557a",
    "redemptionCode": "COCW-OZYZ-BEXN-TIMU",
    "balance": 500.0000,
    "relationName": "loyalty-program-test",
    "emissionDate": "2026-09-08T16:20:01.047Z",
    "expiringDate": "2027-01-01T00:00:00",
    "caption": "VTEX Loyalty Test",
    "currencyCode": "USD",
    "discount": false,
    "transactions": {
        "href": "/cosmetics2/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions"
    }
}
```

In the VTEX Admin, the gift card shows the updated balance:

![VTEX Admin gift card details showing a balance of 500 after the credit transaction](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Payments/gift-cards/managing-vtex-gift-cards_2.png)

### Removing balance from a gift card

To remove balance from a gift card, you must also use the [Create GiftCard Transaction](https://developers.vtex.com/docs/api-reference/giftcard-api#post-/giftcards/-giftCardID-/transactions) endpoint and send the gift card identification (`giftCardId`) as a path parameter.

**POST**

`https://{accountName}.{environment}.com.br/api/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions`

To remove 120 USD from the balance, send `Debit` in the `operation` field and `120` in the `value` field.

Request body

```json
{
  "operation": "Debit",
  "value": 120,
  "description": "Payment of order 5555",
  "redemptionToken": "b2dac6f2-f365-48cd-82a9-0b376a55557a",
  "redemptionCode": "COCW-OZYZ-BEXN-TIMU",
  "requestId": "2"
}
```

Response body

```json
{
    "cardId": "92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74",
    "id": "c2b69a5990404a11b26888964bed3868",
    "_self": {
        "href": "/cosmetics2/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions/c2b69a5990404a11b26888964bed3868"
    }
}
```

> ⚠️ Whenever you create a new transaction, you must send a `requestId` different from the ones previously used for that gift card. Transactions that have a `requestId` value previously used on the same gift card aren't completed. For example: after creating the first credit transaction, in which you used the value `1` for `requestId`, you create a debit transaction with `requestId` equal to `2`. Any other transaction for this gift card must be created with values different from `1` and `2` in the `requestId`.

To confirm the new gift card balance, use the [Get GiftCard by ID](https://developers.vtex.com/docs/api-reference/giftcard-api#get-/giftcards/-giftCardID-) endpoint or the VTEX Admin.

Response body

```json
{
    "id": "92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74",
    "redemptionToken": "b2dac6f2-f365-48cd-82a9-0b376a55557a",
    "redemptionCode": "COCW-OZYZ-BEXN-TIMU",
    "balance": 380.0000,
    "relationName": "loyalty-program-test",
    "emissionDate": "2026-09-08T16:20:01.047Z",
    "expiringDate": "2027-01-01T00:00:00",
    "caption": "VTEX Loyalty Test",
    "currencyCode": "USD",
    "discount": false,
    "transactions": {
        "href": "/cosmetics2/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions"
    }
}
```

In the VTEX Admin, the gift card shows the balance after the debit transaction:

![VTEX Admin gift card details showing a balance of 380 after the debit transaction](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Payments/gift-cards/managing-vtex-gift-cards_3.png)

## Checking VTEX gift card transactions

You can use the [List All GiftCard Transactions](https://developers.vtex.com/docs/api-reference/giftcard-api#get-/giftcards/-giftCardID-/transactions) endpoint to check all transactions performed on a gift card. In this request, you must send the gift card identification (`giftCardId`) as a path parameter.

**GET**

`https://{accountName}.{environment}.com.br/api/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions`

The following response body shows information from the two transactions created in the previous sections:

```json
[
    {
        "cardId": "92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74",
        "id": "c2b69a5990404a11b26888964bed3868",
        "_self": {
            "href": "/cosmetics2/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions/c2b69a5990404a11b26888964bed3868"
        }
    },
    {
        "cardId": "92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74",
        "id": "465f2d7370f349879f4c194ac81d8e98",
        "_self": {
            "href": "/cosmetics2/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions/465f2d7370f349879f4c194ac81d8e98"
        }
    }
]
```

> ⚠️ If you use this endpoint to request details for a new gift card that doesn't contain transactions yet, the response body is empty.

### Accessing information from a gift card transaction

To get information about a specific gift card transaction, you can use the [Get GiftCard Transaction by ID](https://developers.vtex.com/docs/api-reference/giftcard-api#get-/giftcards/-giftCardID-/transactions/-transactionID-) endpoint. In this request, you must send the gift card identification (`giftCardId`) and the transaction identification (`transactionId`) as path parameters.

> ⚠️ The `transactionId` value used in this request is the same `id` value obtained from the response body of the [List All GiftCard Transactions](https://developers.vtex.com/docs/api-reference/giftcard-api#get-/giftcards/-giftCardID-/transactions) endpoint. For more information, see the [Checking VTEX gift card transactions](#checking-vtex-gift-card-transactions) section.

The following example uses gift card `92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74` and the credit transaction `465f2d7370f349879f4c194ac81d8e98`.

**GET**

`https://{accountName}.{environment}.com.br/api/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions/465f2d7370f349879f4c194ac81d8e98`

Response body

```json
{
    "value": 500.0,
    "description": "Opening balance",
    "date": "2026-09-08T16:25:12.331Z",
    "requestId": "1",
    "settlement": {
        "href": "/cosmetics2/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions/465f2d7370f349879f4c194ac81d8e98/settlements"
    },
    "cancellation": {
        "href": "/cosmetics2/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions/465f2d7370f349879f4c194ac81d8e98/cancellations"
    },
    "authorization": {
        "href": "/cosmetics2/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions/465f2d7370f349879f4c194ac81d8e98/authorization"
    },
    "operation": "Credit"
}
```

The `settlement`, `cancellation`, and `authorization` objects return the URLs of the resources related to that transaction:

| Object | Description |
| ------ | ----------- |
| `settlement` | Points to the settlements of the transaction. Use [Settle GiftCard Transaction](https://developers.vtex.com/docs/api-reference/giftcard-api#post-/giftcards/-giftCardID-/transactions/-transactionID-/settlements) to create a settlement, or [List All GiftCard Transaction Settlements](https://developers.vtex.com/docs/api-reference/giftcard-api#get-/giftcards/-giftCardID-/transactions/-transactionID-/settlements) to retrieve them. |
| `cancellation` | Points to the cancellations of the transaction. Use [Cancel GiftCard Transaction](https://developers.vtex.com/docs/api-reference/giftcard-api#post-/giftcards/-giftCardID-/transactions/-transactionID-/cancellations) to cancel the transaction, cancel an item reservation, or create a refund. |
| `authorization` | Points to the authorization data of the transaction. Use [Get GiftCard Transaction Authorization](https://developers.vtex.com/docs/api-reference/giftcard-api#get-/giftcards/-giftCardID-/transactions/-transactionID-/authorization) to retrieve it. |

## Canceling a VTEX gift card transaction

To partially or completely cancel a value assigned in a transaction (credit or debit), you can use the [Cancel GiftCard Transaction](https://developers.vtex.com/docs/api-reference/giftcard-api#post-/giftcards/-giftCardID-/transactions/-transactionID-/cancellations) endpoint. In this request, you must send the gift card identification (`giftCardId`) and the transaction identification (`transactionId`) as path parameters.

> ⚠️ The `transactionId` value used in this request is the same `id` value obtained from the response body of the [List All GiftCard Transactions](https://developers.vtex.com/docs/api-reference/giftcard-api#get-/giftcards/-giftCardID-/transactions) endpoint. For more information, see the [Checking VTEX gift card transactions](#checking-vtex-gift-card-transactions) section.

The following example partially cancels the debit transaction `c2b69a5990404a11b26888964bed3868`. The transaction value is 120 USD and the canceled amount is 20 USD. The gift card used is `92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74`, with a current balance of 380 USD.

**POST**

`https://{accountName}.{environment}.com.br/api/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions/c2b69a5990404a11b26888964bed3868/cancellations`

To cancel the amount of 20 USD in the debit transaction, send `20` in the `value` field.

Request body

```json
{
  "value": 20,
  "requestId": "3"
}
```

Response body

```json
{
    "oid": "a1e7edfb72d74bfa960cdbc2eb9471ce",
    "value": 20.0,
    "date": "2026-09-08T17:28:39.721Z"
}
```

To confirm the new gift card balance, use the [Get GiftCard by ID](https://developers.vtex.com/docs/api-reference/giftcard-api#get-/giftcards/-giftCardID-) endpoint or the VTEX Admin.

Response body

```json
{
    "id": "92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74",
    "redemptionToken": "b2dac6f2-f365-48cd-82a9-0b376a55557a",
    "redemptionCode": "COCW-OZYZ-BEXN-TIMU",
    "balance": 400.0000,
    "relationName": "loyalty-program-test",
    "emissionDate": "2026-09-08T16:20:01.047Z",
    "expiringDate": "2027-01-01T00:00:00",
    "caption": "VTEX Loyalty Test",
    "currencyCode": "USD",
    "discount": false,
    "transactions": {
        "href": "/cosmetics2/giftcards/92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff_74/transactions"
    }
}
```

In the VTEX Admin, the gift card shows the balance after the partial cancellation:

![VTEX Admin gift card details showing a balance of 400 after the partial cancellation](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Payments/gift-cards/managing-vtex-gift-cards_4.png)

> ⚠️ When a debit transaction is canceled, the canceled amount is credited to the total gift card balance. Likewise, when a credit transaction is canceled, the canceled amount is debited from the total gift card balance.

## Learn more

- [Gift card integration guide](https://developers.vtex.com/docs/guides/gift-card-integration-guide)
- [Gift Card system architecture](https://developers.vtex.com/docs/guides/gift-card-integration-guide-system-architecture)
- [Configuring an external gift card provider](https://developers.vtex.com/docs/guides/configuring-an-external-gift-card-provider)
- [GiftCard API](https://developers.vtex.com/docs/api-reference/giftcard-api#overview)
- [Setting up Gift Cards](https://help.vtex.com/en/tutorial/gift-card--tutorials_995)
