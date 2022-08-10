---
title: "How do gift cards work?"
slug: "gift-card-integration-guide-data-structures"
hidden: true
createdAt: "2020-07-01T02:24:37.898Z"
updatedAt: "2020-10-16T02:29:18.408Z"
---
Before developing your gift card provider implementation, it's important to clearly understand the data structures and the behaviors expected by Gift Card Hub. In most cases, developers will need to map the data structures and behaviors exhibited by external gift card providers and create parsing routines in their middleware to switch back and forth between standards.

## Gift Card Provider

A gift card provider is an external system that manages gift cards and their transactions. 

The minimum information needed to define a provider includes:

- `id`: the provider identifier in the context of Gift Card Hub API
- `caption`: the name seen by shoppers in the store checkout
- `serviceUrl`: the base URL that should be prepended to all provider endpoints
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9a4bd43-Screen_Shot_2020-10-13_at_21.59.31.png",
        "Screen Shot 2020-10-13 at 21.59.31.png",
        658,
        286,
        "#f1f3f4"
      ],
      "caption": "The name seen by shoppers in the store checkout is set by the `caption` parameter\n\n(e.g. My Gift Card Provider)"
    }
  ]
}
[/block]
Below you will find an example of the gift card provider data structure and more details on the usage of each parameter. Parameters that were not mentioned in our short description above can usually be set to the values in the example.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"id\": \"GiftCardExample\",\n    \"serviceUrl\": \"https://giftcard--cosmetics2.myvtex.com/my-provider\",\n    \"caption\": \"My Gift Card Provider\",\n    \"oauthProvider\": \"vtex\",\n    \"preAuthEnabled\": true,\n    \"cancelEnabled\": true,\n    \"_self\": {\n        \"href\": \"cosmetics2/giftcardproviders/GiftCardExample\"\n    }\n}",
      "language": "json",
      "name": "Gift Card Provider - Example"
    }
  ]
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Name",
    "h-1": "Type",
    "h-2": "Description",
    "h-3": "Required?",
    "1-0": "`serviceUrl`",
    "1-1": "string",
    "1-2": "Base URL for all gift card provider middleware endpoints",
    "1-3": "",
    "2-0": "`caption`",
    "2-3": "",
    "2-1": "string",
    "2-2": "Gift card provider identifier in the store checkout",
    "0-0": "`id`",
    "0-2": "Gift card provider identifier for API requests",
    "0-1": "string",
    "3-0": "`oauthProvider`",
    "3-1": "string",
    "3-2": "[Webstore login provider](https://developers.vtex.com/docs/login-integration-guide-webstore-oauth2) identifier in VTEX ID, used to identify users in loyalty programs",
    "4-0": "`preAuthEnabled`",
    "4-1": "bool",
    "5-0": "`cancelEnabled`",
    "5-1": "bool",
    "4-2": "Indicates whether purchases using this gift card provider should be pre-authorized",
    "3-3": "'vtex'",
    "4-3": "true",
    "5-3": "true",
    "5-2": "Indicates whether purchases using this gift card provider can be cancelled",
    "6-0": "`_self`",
    "6-1": "object",
    "6-2": "Indicates the relative path where this data structure can be found in Gift Card Hub, by appending the `href` parameter to `https://api.vtex.com`"
  },
  "cols": 3,
  "rows": 7
}
[/block]

[block:callout]
{
  "type": "danger",
  "title": "Invalid oauthProvider",
  "body": "Failing to define a valid `oauthProvider` will generate an error in your store's checkout. Most implementations should set this parameter to `'vtex'`"
}
[/block]
## Gift card

A gift card can work as either a redeemable gift voucher or a loyalty program. Although the data structure is the same, the required fields for each behavior are slightly different. 

The minimum information needed to define a gift card includes:

- `id`: the gift card identifier in the context of Gift Card Hub API
- `balance`: the amount of credit available in the gift card
- `emissionDate`: the date when the gift card starts being valid
- `expiringDate`: the date when the gift card stops being valid

### Loyalty program

When used as a redeemable gift voucher, you should also set:

- `caption`: the gift card identifier in checkout

Below you will find an example of the gift card data structure for a loyalty program card. The `provider` and `transaction` fields are added by Gift Card Hub.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"id\": \"1\",\n    \"balance\": 100.0,\n    \"emissionDate\": \"2020-07-30T00:00:00Z\",\n    \"expiringDate\": \"2030-07-30T00:00:00Z\",\n    \"caption\": \"My Awesome Card 1\",\n    \"provider\": \"GiftCardExample\",\n    \"transaction\": {\n        \"href\": \"cosmetics2/giftcardproviders/GiftCardExample/giftcards/1/transactions\"\n    }\n}",
      "language": "json",
      "name": "Gift Card - Loyalty Program Example"
    }
  ]
}
[/block]
### Redeemable voucher

When used as a redeemable gift voucher, you should also set:

- `redemptionCode`: the gift card code in checkout

Below you will find an example of the gift card data structure for a redeemable gift voucher. The `provider` and `transaction` fields are added by Gift Card Hub.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"id\": \"2\",\n    \"balance\": 50.0,\n    \"emissionDate\": \"2020-07-30T00:00:00Z\",\n    \"expiringDate\": \"2030-07-30T00:00:00Z\",\n    \"caption\": \"My Awesome Card 2\",\n    \"redemptionCode\": \"123456\",\n    \"provider\": \"GiftCardExample\",\n    \"transaction\": {\n        \"href\": \"cosmetics2/giftcardproviders/GiftCardExample/giftcards/2/transactions\"\n    }\n}",
      "language": "json",
      "name": "Gift Card - Redeemable Gift Voucher Example"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "warning",
  "title": "Customization needed to display caption",
  "body": "Our default display for redeemable vouchers is simply the redemption code. \n\nIf you would like to present the caption as well, you will need to customize your checkout to display it by fetching that information from the [paymentData](https://github.com/vtex/vtex.js/blob/master/docs/checkout/order-form.md#paymentData) available in the [vtex.js](https://github.com/vtex/vtex.js) orderForm object."
}
[/block]
All the parameters that can be set when creating gift cards are listed in the table below.
[block:parameters]
{
  "data": {
    "h-0": "Name",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "`id`",
    "3-0": "`expiringDate`",
    "1-0": "`balance`",
    "2-0": "`emissionDate`",
    "4-0": "`caption`",
    "5-0": "`relationName`",
    "6-0": "`redemptionCode`",
    "8-0": "`provider`",
    "9-0": "`transaction`",
    "9-2": "Indicates the relative path where the transactions for this gift card can be found in Gift Card Hub, by appending the `href` parameter to `https://api.vtex.com`",
    "8-2": "Gift card provider identifier for API requests",
    "0-2": "Gift card identifier for API requests",
    "1-2": "Credit available in gift card",
    "2-2": "Date when the gift card starts being valid (ISO 8601 format)",
    "3-2": "Date when the gift card stops being valid (ISO 8601 format)",
    "4-2": "Gift card identifier in the store checkout that is displayed for loyalty programs",
    "6-2": "Code used in the store checkout to activate redeemable vouchers",
    "5-2": "Relationship between the customer and the store",
    "0-1": "string",
    "1-1": "number",
    "2-1": "string",
    "3-1": "string",
    "4-1": "string",
    "5-1": "string",
    "6-1": "string",
    "8-1": "string",
    "9-1": "object",
    "7-0": "`redemptionToken`",
    "7-1": "string",
    "7-2": "Optional code that can be used to validate redeemable vouchers (checkout customization required for user input)"
  },
  "cols": 3,
  "rows": 10
}
[/block]
Some fields are shown in the order details page when gift cards are used to pay for an order:

- Code: `redemptionCode`
- Name: `relationName`
- Caption: `caption`
- Gift Card Issuer: `provider`

The image below illustrates how these might be presented in a specific order.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/543d003-Screen_Shot_2020-10-14_at_18.47.59.png",
        "Screen Shot 2020-10-14 at 18.47.59.png",
        256,
        545,
        "#f0f2f3"
      ],
      "caption": "Gift card fields seen in the order details page: \n`redemptionCode`, `relationName`, `caption`, `provider`"
    }
  ]
}
[/block]
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
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"value\": 254.98,\n    \"description\": \"Recarga de Gift Card\",\n    \"redemptionMode\": \"6392472000000066891\",\n    \"date\": \"2020-09-30T16:20:57\",\n    \"settlement\": {\n        \"href\": \"rihappy/giftcardproviders/safe/giftcards/6392472000000066891/transactions/112172/settlements\"\n    },\n    \"cancellation\": {\n        \"href\": \"rihappy/giftcardproviders/safe/giftcards/6392472000000066891/transactions/112172/cancellations\"\n    },\n    \"authorization\": {\n        \"href\": \"rihappy/giftcardproviders/safe/giftcards/6392472000000066891/transactions/112172/authorization\"\n    },\n    \"operation\": \"Credit\"\n}",
      "language": "json",
      "name": "Transaction by ID example (recharge)"
    },
    {
      "code": "{\n    \"value\": 254.98,\n    \"description\": \"Utilização de Gift Card\",\n    \"redemptionMode\": \"6392472000000066891\",\n    \"date\": \"2020-09-30T16:24:40\",\n    \"settlement\": {\n        \"href\": \"rihappy/giftcardproviders/safe/giftcards/6392472000000066891/transactions/112173/settlements\"\n    },\n    \"cancellation\": {\n        \"href\": \"rihappy/giftcardproviders/safe/giftcards/6392472000000066891/transactions/112173/cancellations\"\n    },\n    \"authorization\": {\n        \"href\": \"rihappy/giftcardproviders/safe/giftcards/6392472000000066891/transactions/112173/authorization\"\n    },\n    \"operation\": \"Credit\"\n}",
      "language": "json",
      "name": "Transaction by ID example (use)"
    }
  ]
}
[/block]
When gift card transactions are listed for a specific gift card, Gift Card expects a minimal list including only the transaction IDs and references paths where full details can be found for each gift card. This allows for better performance.
[block:code]
{
  "codes": [
    {
      "code": "[\n    {\n        \"id\": \"112172\",\n        \"_self\": {\n            \"href\": \"rihappy/giftcardproviders/safe/giftcards/6392472000000066891/transactions/112172\"\n        }\n    },\n    {\n        \"id\": \"112173\",\n        \"_self\": {\n            \"href\": \"rihappy/giftcardproviders/safe/giftcards/6392472000000066891/transactions/112173\"\n        }\n    }\n]",
      "language": "json",
      "name": "Get transactions response"
    }
  ]
}
[/block]
If your gift cards need code or not, it's all about how you implement your search endpoint. Our native provider requires redemption code and sometimes document (if restricted)

Loyalty program: list is fine

Gift Voucher: redemption code must return only one gift card

Checkout validates data between search and get by id
[block:parameters]
{
  "data": {
    "h-0": "Name",
    "h-1": "Type",
    "h-2": "Description",
    "h-3": "Required?",
    "0-3": "Yes",
    "0-0": "`id`",
    "1-0": "`providerId`"
  },
  "cols": 4,
  "rows": 11
}
[/block]