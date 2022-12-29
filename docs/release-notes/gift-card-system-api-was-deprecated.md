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

> ⚠️ There is no corresponding endpoint to this action in the new Gift Card API. To achieve the same result, you must create a new Gift Card with the correct expiration date.

The table below lists the endpoints in both APIs and their correspondence.

| Gift Card System API|Gift Card API|
| -------------------|--------------|
|**`[GET] List Giftcard`** This endpoint returned all the Gift Cards related to a single customer.|**[`[POST] Get Giftcard using JSON`](https://developers.vtex.com/reference/miscellaneous-3#getgiftcardusingjson)** This endpoint returns all Gift Cards related to a single customer *given the purchase context*. This allows the Checkout to only display options that can be used for the combination of items in cart and other conditions that might be applied.|
|**`[POST] Add/Remove Credit to Gift Card`** This endpoint was used to change the Gift Card balance.|**[`[POST] Create GiftCard Transaction`](https://developers.vtex.com/reference/miscellaneous-3#creategiftcardtransaction-1)** This endpoint is used to change the Gift Card balance and associate this change to a transaction. To change the Gift Card balance, you should use the body parameters `operation` and `value`.|
|**`[POST] Create Gift Card`** This endpoint was used to create a new Gift Card associated with a client `profileId`.|**[`[POST] Create Gift Card`](https://developers.vtex.com/reference/miscellaneous-3#creategiftcard-1)** This endpoint is used to create a new Gift Card, optionally associating it with a client `profileId`. If no `profileId` is indicated in the request body, the new Gift Card will be associated to the AppToken informed in the header.|
|**`[PATCH] Update Expiration Date`** This endpoint was used to update the expiration date of a Gift Card|There is no corresponding endpoint to this action in the new Gift Card API. To achieve the same result, you must create a new Gift Card with the correct expiration date.|
