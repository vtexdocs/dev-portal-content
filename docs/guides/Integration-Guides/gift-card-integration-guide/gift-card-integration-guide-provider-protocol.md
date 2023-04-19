---
title: "Integrating a new gift card provider"
slug: "gift-card-integration-guide-provider-protocol"
hidden: true
createdAt: "2020-07-01T02:25:50.803Z"
updatedAt: "2020-09-29T23:09:46.033Z"
---

## Linking the boilerplate code

1.Download from github.
2.Create a workspace (giftcard in the example).
3.Link the code.

All mock routes will be available in _/my-provider_.

## Setting up for development

[List All GiftCard Providers](https://developers.vtex.com/docs/api-reference/giftcard-hub-api#get-/giftcardproviders) from Gift Card Hub should have only native Gift Card.

```json
[
    {
        "id": "VtexGiftCard",
        "serviceUrl": "http://api.vtex.com/cosmetics2",
        "oauthProvider": "vtex",
        "preAuthEnabled": true,
        "cancelEnabled": true,
        "_self": {
            "href": "cosmetics2/giftcardproviders/VtexGiftCard"
        }
    }
]
```
[Create/Update GiftCard Provider by ID](https://developers.vtex.com/docs/api-reference/giftcard-hub-api#put-/giftcardproviders/-giftCardProviderID-) from Gift Card Hub should let you add your own.

```json
{
    "serviceUrl": "https://giftcard--cosmetics2.myvtex.com/my-provider",
    "oauthProvider": "vtex",
    "preAuthEnabled": true,
    "cancelEnabled": true
}
```

Once it is there, your store's Checkout will use the `serviceUrl` to make requests. You should do this in a test account so it does not break anyone.

## Testing the mock provider

Buy some product, you should see the mock gift card there.

## Where each route is called

![GiftCard](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/gift-card-integration-guide-provider-protocol-0.png)
This is what is needed to make Gift Card available in checkout:

### List cards

When a customer reaches the payment step, checkout will make a request to [List All GiftCards](https://developers.vtex.com/docs/api-reference/giftcard-provider-protocol#post-/giftcards/_search) in order to display a list of options for the customer.

### Use card

When a customer selects a gift card, checkout will make a request to [Get GiftCard by ID](https://developers.vtex.com/docs/api-reference/giftcard-provider-protocol#get-/giftcards/-giftCardID-).

### Order Placed

Once the order is placed, checkout will make a request to [Create GiftCard Transaction](https://developers.vtex.com/docs/api-reference/giftcard-provider-protocol#post-/giftcards/-giftCardID-/transactions) to create a transaction.

This is what is needed to make Gift Card fully integrated with orders:

## Cancel

[Create GiftCard Transaction Cancellation](https://developers.vtex.com/docs/api-reference/giftcard-provider-protocol#post-/giftcards/-giftCardID-/transactions/-transactionID-/cancellations)

## Invoice

This is expected, but not required by any existing process:

[Create GiftCard](https://developers.vtex.com/docs/api-reference/giftcard-provider-protocol#post-/giftcards)

[List All GiftCard Transactions](https://developers.vtex.com/docs/api-reference/giftcard-provider-protocol#get-/giftcards/-giftCardID-/transactions)
