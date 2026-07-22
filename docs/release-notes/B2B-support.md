---
title: B2B support
excerpt: 'VTEX IO now requires authentication to access product commercial information, providing a greater support to stores with closed sales channel.'
createdAt: '2019-12-12T18:27:49.833Z'
type: 'info'
---
VTEX IO now requires authentication to access product commercial information, providing a greater support to stores with closed sales channel.

## What has changed

A closed sales channel means that an authentication is always required to access a product commercial information. Therefore, B2B environments are usually blocked, in whole or in part, for anonymous users in VTEX.

Although VTEX’s APIs, such as Search and Checkout, already support user authentication in closed sales channels using the `VtexIdClientAutCookie`, this token was not used in VTEX IO.

Previously, the Search API in VTEX IO could not require user authentication because the API was accessed only by the segment route. By forcing all queries to be requested on the private route, the cookies now can pass to the IO backend, not performing cache.

With this release, `VtexIdClientAuthCookie` is now available to `vtex.store-graphql` and the Search API.

## Key advantage

As the API now requires user authentication, all product information in a closed sales channel are protected with more security layers.

## What you need to do

To enable this feature, follow the steps below:

1. In the admin v2, access **Account Settings** and click on **Apps**
2. Select **VTEX Store**
3. Check the **Enables B2B Behavior** checkbox.

![image](https://user-images.githubusercontent.com/52087100/60180024-7eb3b900-97f5-11e9-932a-e705107affeb.png)

## Side Effects

The feature set up removes any cache from the store when enabled.
