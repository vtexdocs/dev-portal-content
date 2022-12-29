---
title: "Gift List app: allow shoppers to create lists of store items and receive them as gifts"
slug: "gift-list-app-allow-shoppers-to-create-lists-of-store-items-and-receive-them-as-gifts"
type: "added"
createdAt: "2022-09-16T13:36:04.922Z"
hidden: false
excerpt: "The [Gift List app](https://developers.vtex.com/vtex-developer-docs/docs/vtex-gift-list) offers a new environment in the store where shoppers can create, manage and share gift lists."
---

![VTEX IO App](https://img.shields.io/badge/-VTEX%20IO%20App-orange)

The [Gift List app](https://developers.vtex.com/vtex-developer-docs/docs/vtex-gift-list) offers a new environment in the store where shoppers can create, manage and share gift lists.

A gift list is a list of products that a shopper creates and sends to guests (other shoppers) asking them to buy the products. This can be useful for events like birthdays, weddings, and baby showers. When a guest buys one or more products from the list, virtual credit is generated that can be converted into a [gift card](https://developers.vtex.com/vtex-rest-api/docs/gift-card-integration-guide). The list’s creator has a wallet with information about the generated credit and the gift card. Then, the creator of the list can use the gift card to purchase the desired items.

In a gift list, the creator of the list can:

- Define the list name. This can be useful to relate to an event related to the list (i.e.: Jhon’s birthday).
- Define an event date.
- Assign one or two names for the person(s) that will be gifted.
- Choose whether it is public or private.
- Add items from the store to the list and choose the amount of each item.
- Edit the items on the list (change amounts, remove items, etc.).
- Share the list with guests.
- Receive the credits with a value equivalent to the gifted items.
- Spend the credits for purchases in the store.

And the guests can:

- View the list.
- Buy the products available on the list. The amount of each purchase is converted to credits in the list wallet.
- Insert a message or a comment on the purchase.
[block:callout]
{
  "type": "info",
  "body": "The app will be free to trial until December 31. After this period, it will have a fixed cost billed monthly."
}
[/block]
You can install the app from the [App Store](https://apps.vtex.com/vtex-list/p). To learn more about the app and implement it in your store, please refer to its [technical documentation](https://developers.vtex.com/vtex-developer-docs/docs/vtex-gift-list).

You can see below some images of the Gift List environment in a store:
![Gift List environment](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/release-notes/5e2dd04-image5_40.png)

![Section with the created lists and button to create a new list](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/release-notes/e546825-image2_42.png)

![Section with the wallet (gift card)](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/release-notes/d65232e-image3_44.png)

![Window to create a new list](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/release-notes/eb7b37e-image1_46.png)

![Page to manage the items on the list](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/release-notes/8346a07-image4_48.png)

![Shared gift list where a guest can choose to gift items](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/release-notes/4172bf6-image6_50.png)

![Summary of the checkout with the message](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/release-notes/fb8839c-image7_52.png)
