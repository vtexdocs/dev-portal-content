---
slug: "gift-card-support-multi-currencies"
title: "Gift card support multi-currencies"
createdAt: 2023-07-27T12:00:00.000Z
hidden: false
type: "added"
excerpt: "Configure your store gift cards in multiple currencies."
---
As of July 30, 2023, you will be able to create gift cards in currencies other than those added to your store. This new feature allows you to indicate in which currency the gift card should be created when adding a new gift card in the VTEX Admin.
 
Also, a new optional field (`currencyCode`) has been added to the endpoints below, enabling you to identify the currency applicable to each gift card.

**GiftCard API**
- [Create GiftCard](https://developers.vtex.com/docs/api-reference/giftcard-api#post-/giftcards)
- [Create GiftCard by ID](https://developers.vtex.com/docs/api-reference/giftcard-api#get-/giftcards/-giftCardID-)

**GiftCard Hub API**
- [Create GiftCard in GiftCard Provider](https://developers.vtex.com/docs/api-reference/giftcard-hub-api#post-/giftcardproviders/-giftCardProviderID-/giftcards)
- [Get GiftCard from GiftCard Provider by ID](https://developers.vtex.com/docs/api-reference/giftcard-hub-api#get-/giftcardproviders/-giftCardProviderID-/giftcards/-giftCardID-)

**GiftCard Provider Protocol API**
- [Create GiftCard](https://developers.vtex.com/docs/api-reference/giftcard-provider-protocol#post-/giftcards)
- [Get GiftCard by ID](https://developers.vtex.com/docs/api-reference/giftcard-provider-protocol#get-/giftcards/-giftCardID-)



>⚠️ Setting a specific currency for each gift card is optional. If you don't want to indicate in which currency it should be created, the behavior will remain the same as in a store using only one currency type, where discounts on the amount are applied without currency conversion.

To learn more about how to create gift cards, read the [Setting up Gift cards](https://help.vtex.com/en/tutorial/gift-card--tutorials_995) article.