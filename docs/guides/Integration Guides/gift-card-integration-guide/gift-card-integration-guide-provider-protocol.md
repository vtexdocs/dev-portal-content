---
title: "Integrating a new gift card provider"
slug: "gift-card-integration-guide-provider-protocol"
hidden: true
createdAt: "2020-07-01T02:25:50.803Z"
updatedAt: "2020-09-29T23:09:46.033Z"
---
## Linking the boilerplate code

Download from github
Create a workspace (giftcard in the example)
Link the code

All mock routes will be available in /my-provider

## Setting up for development

[List All GiftCard Providers](https://developers.vtex.com/reference/provider#listallgiftcardproviders) from Gift Card Hub should have only native Gift Card
[block:code]
{
  "codes": [
    {
      "code": "[\n    {\n        \"id\": \"VtexGiftCard\",\n        \"serviceUrl\": \"http://api.vtex.com/cosmetics2\",\n        \"oauthProvider\": \"vtex\",\n        \"preAuthEnabled\": true,\n        \"cancelEnabled\": true,\n        \"_self\": {\n            \"href\": \"cosmetics2/giftcardproviders/VtexGiftCard\"\n        }\n    }\n]",
      "language": "json",
      "name": "Response Body"
    }
  ]
}
[/block]
[Create/Update GiftCard Provider by ID](https://developers.vtex.com/reference/provider#createupdategiftcardproviderbyid) from Gift Card Hub should let you add your own
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"serviceUrl\": \"https://giftcard--cosmetics2.myvtex.com/my-provider\",\n    \"oauthProvider\": \"vtex\",\n    \"preAuthEnabled\": true,\n    \"cancelEnabled\": true\n}",
      "language": "json",
      "name": "Request Body"
    },
    {
      "code": "{\n    \"id\": \"GiftCardExample\",\n    \"serviceUrl\": \"https://giftcard--cosmetics2.myvtex.com/my-provider\",\n    \"oauthProvider\": \"vtex\",\n    \"preAuthEnabled\": true,\n    \"cancelEnabled\": true,\n    \"_self\": {\n        \"href\": \"cosmetics2/giftcardproviders/GiftCardExample\"\n    }\n}",
      "language": "json",
      "name": "Response Body"
    }
  ]
}
[/block]
Once it's there, your store's Checkout will use the serviceUrl to make requests. You should do this in a test account so it doesn't break anyone

## Testing the mock provider

Buy some product, you should see the mock gift card there

## Where each route is called


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2052a81-GiftCard.png",
        "GiftCard.png",
        1682,
        1400,
        "#fbf7f9"
      ]
    }
  ]
}
[/block]
This is what is needed to make Gift Card available in checkout:

### List cards
When a customer reaches the payment step, checkout will make a request to [List All GiftCards](https://developers.vtex.com/reference/gift-cards#listallgiftcards) in order to display a list of options for the customer.

### Use card
When a customer selects a gift card, checkout will make a request to [Get GiftCard by ID](https://developers.vtex.com/reference/gift-cards#getgiftcardbyid-1)

### Order Placed
Once the order is placed, checkout will make a request to [Create GiftCard Transaction](https://developers.vtex.com/reference/transactions#creategiftcardtransaction-2) to create a transaction

This is what is needed to make Gift Card fully integrated with orders:

## Cancel
https://developers.vtex.com/reference/transactions#getgiftcardtransactionbyid-2
## Invoice



This is expected, but not required by any existing process:

[Create GiftCard](https://developers.vtex.com/reference/gift-cards#creategiftcard-2)
[List All GiftCard Transactions](https://developers.vtex.com/reference/transactions#listallgiftcardtransactions-1)