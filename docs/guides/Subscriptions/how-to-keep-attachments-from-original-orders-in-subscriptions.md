---
title: "How to keep attachments from original orders in subscriptions"
slug: "how-to-keep-attachments-from-original-orders-in-subscriptions"
hidden: false
createdAt: "2024-09-10T15:00:00.958Z"
updatedAt: "2024-09-10T15:00:00.958Z"
---

[Subscriptions](https://help.vtex.com/en/tutorial/how-subscriptions-work--frequentlyAskedQuestions_4453) is the VTEX solution for customers who want to make recurring purchases at the store on a regular schedule. When customers subscribe, they define what products they want to acquire regularly and at the frequency they want these automatic orders to be created.

When a new subscription is created from an order containing SKUs with [attachments](https://help.vtex.com/en/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm), the platform default behavior is to discard the attachments in future subscription orders. However, you can configure the store to incorporate SKU attachments from the original order into recurring orders.

## Configuring the store to keep attachments from original orders

To allow a VTEX store to keep SKU attachments for subscription orders, use the [Edit subscriptions settings](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3#post-/api/rns/settings) endpoint. Within the request body, in the `attachmentPreferences` object, set the `enableAttachments` field as `true`, as shown below:

```json
"attachmentPreferences": {
        "enableAttachments": true
    }
```

>ℹ️ Whether an order contains the [same SKU with or without attachments](#original-orders-containing-the-same-skus-with-different-attachments), keep in mind that the platform's default behavior is to group these SKUs. You can configure the platform to [split the same SKUs with attachments](#configuring-to-split-the-same-skus-with-different-attachments) instead.

## Original orders containing the same SKUs with different attachments

The platform’s default behavior when keeping attachments from original orders is to group the same SKUs, regardless of whether they have attachments.

The table below shows how the SKU grouping works:

| **Original order** | **Subscription order grouping different attachments for the same SKU** | **Behavior** |
| :--- | :--- | :--- |
| <p>Total: 8 items<ul><li>[1] SKU X - Attachment A: Type I<ul><li>Quantity: 2</li></ul></li><li>[2] SKU X - Attachment A: Type II<ul><li>Quantity: 3</li></ul></li><li>[3] SKU X - No attachment<ul><li>Quantity: 1</li></ul></li><li>[4] SKU X - No attachment<ul><li>Quantity: 1</li></ul></li><li>[5] SKU Y - No attachment<ul><li>Quantity: 1</li></ul></li></ul></p> | <p>Total: 8 items<ul><li>[1] SKU X - Attachment A: Type I + SKU X - Attachment A: Type II + SKU X - No attachment<ul><li>Quantity: 7</li></ul></li><li>[2] SKU Y - No attachment<ul><li>Quantity: 1</li></ul></li></ul></p> | When the original order has the same SKUs, with and without attachments, the subscription order groups them together. |

You can change this behavior so that subscription orders created from original orders containing the same SKUs with different attachments are not grouped together but kept separate.

The table below shows how that works:

| **Original order** | **Subscription orders splitting the same SKUs with different attachments** | **Behavior** |
| :--- | :--- | :--- |
| <p>Total: 8 items<ul><li>[1] SKU X - Attachment A: Type I<ul><li>Quantity: 2</li></ul></li><li>[2] SKU X - Attachment A: Type II<ul><li>Quantity: 3</li></ul></li><li>[3] SKU X - No attachment<ul><li>Quantity: 1</li></ul></li><li>[4] SKU X - No attachment<ul><li>Quantity: 1</li></ul></li><li>[5] SKU Y<ul><li>Quantity: 1</li></ul></li></ul></p> | <p>Total: 8 items<ul><li>[1] SKU X - Attachment A: Type I<ul><li>Quantity: 2</li></ul></li><li>[2] SKU X - Attachment A: Type II<ul><li>Quantity: 3</li></ul></li><li>[3] SKU X - No attachment<ul><li>Quantity: 2</li></ul></li><li>[4] SKU Y - No attachment<ul><li>Quantity: 1</li></ul></li></ul></p> | The organization from the original order is kept for subscription orders, and the same SKUs with attachments are no longer grouped, not even if they have the same type of attachment. Only SKUs that do not have attachments will be grouped. |

## Configuring to split the same SKUs with different attachments

To allow a VTEX store to keep SKU attachments for new subscriptions, use the [Edit subscriptions settings](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3#post-/api/rns/settings) endpoint. In the request body, inside the property `attachmentPreferences`, set the `enableAttachments` field to `true`, as shown below:

```json
"attachmentPreferences": {
        "enableAttachments": true,
        "splitSameSkuWithDifferentAttachments": true
    }
```

>❗ The `splitSameSkuWithDifferentAttachments` field can only be set to `true` if the `enableAttachments` field is also set to `true`.
