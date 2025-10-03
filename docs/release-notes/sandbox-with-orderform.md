---
title: Sandbox with OrderForm
excerpt: "The user's cart data can now be used in Sandbox components in a fast and simple way."
createdAt: "2019-09-26T14:47:00.000Z"
type: 'info'
---
The [Sandbox component](https://vtex.io/docs/components/all/vtex.sandbox/) is now able to receive OrderForm context.

## What has changed

Previously, the Sandbox component did not support information that depended on items added in the cart, being only capable of displaying data from the page's context.

Now, it also is able to receive OrderForm data!

## Main advantages

With the OrderForm, **Sandbox is able to make cart item data available**, allowing new functionalities that depend on such data to be developed by the store.

For example: suppose that a store wants to run a free shipping campaign for orders above U$ 150. With this improvement, a component that calculates how much is missing to reach the free shipping range can be developed, based on user cart data from the OrderForm. 

## What you need to do 

Lucky you! It's easy: just make sure your store has the [Sandbox component](https://vtex.io/docs/components/all/vtex.sandbox/) installed at least on version **0.3.0**.
