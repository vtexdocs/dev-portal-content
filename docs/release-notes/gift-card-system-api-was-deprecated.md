---
slug: "gift-card-system-api-was-deprecated"
title: "Gift Card System API was deprecated"
createdAt: 2020-04-27T23:54:26.252Z
hidden: true
type: ""
---

![Commerce APIs](https://img.shields.io/badge/-Commerce%20APIs-brightgreen)

The **Gift Card System API** was used in VTEX to provide a built-in solution for stores who wanted to use gift cards in their business, but there were opportunities to improve the mechanics of how it worked. So our developers created the new  [Gift Card API](https://developers.vtex.com/reference/giftcard-api-overview) as a replacement.

Now that most of its functionality is available in Gift Card API, we decided it was time to say goodbye to Gift Card System API. While integrations built on top of the older Gift Card System will keep working, we will no longer dedicate efforts to improve it. *New integrations should be created using the new API.*
[block:callout]
{
  "type": "warning",
  "title": "Gift Card expiration date can no longer be changed",
  "body": "There is no corresponding endpoint to this action in the new Gift Card API. To achieve the same result, you must create a new Gift Card with the correct expiration date."
}
[/block]
The table below lists the endpoints in both APIs and their correspondence.
[block:parameters]
{
  "data": {
    "h-0": "Gift Card System API",
    "h-1": "Gift Card API",
    "0-0": "**` [GET] List Giftcard`**\n\nThis endpoint returned all the Gift Cards related to a single customer.",
    "1-0": "**` [POST] Add/Remove Credit to Gift Card`**\n\nThis endpoint was used to change the Gift Card balance.",
    "1-1": "**[`[POST] Create GiftCard Transaction`](https://developers.vtex.com/reference/miscellaneous-3#creategiftcardtransaction-1)**\n\nThis endpoint is used to change the Gift Card balance and associate this change to a transaction.\n\nTo change the Gift Card balance, you should use the body parameters `operation` and `value`.",
    "2-0": "**`[POST] Create Gift Card`**\n\nThis endpoint was used to create a new Gift Card associated with a client `profileId`.",
    "2-1": "**[`[POST] Create Gift Card`](https://developers.vtex.com/reference/miscellaneous-3#creategiftcard-1)**\n\nThis endpoint is used to create a new Gift Card, optionally associating it with a client `profileId`.\n\nIf no `profileId` is indicated in the request body, the new Gift Card will be associated to the AppToken informed in the header.",
    "0-1": "**[`[POST] Get Giftcard using JSON`](https://developers.vtex.com/reference/miscellaneous-3#getgiftcardusingjson)**\n\nThis endpoint returns all Gift Cards related to a single customer *given the purchase context*.\n\nThis allows the Checkout to only display options that can be used for the combination of items in cart and other conditions that might be applied.",
    "3-0": "**`[PATCH] Update Expiration Date`**\n\nThis endpoint was used to update the expiration date of a Gift Card.",
    "3-1": "There is no corresponding endpoint to this action in the new Gift Card API. To achieve the same result, you must create a new Gift Card with the correct expiration date."
  },
  "cols": 2,
  "rows": 4
}
[/block]