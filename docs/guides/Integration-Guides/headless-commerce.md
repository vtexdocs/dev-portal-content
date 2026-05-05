---
title: "Headless commerce"
slug: "headless-commerce"
hidden: false
createdAt: "2021-03-31T21:12:21.094Z"
updatedAt: "2023-05-29T21:21:53.940Z"
---

VTEX technology allows for flexibility, enabling our clients to build commerce experiences that address their needs and potentialize their strengths.

This guide can help you leverage VTEX APIs to build a headless shopping experience considering that you:

- Will use VTEX core commerce features via REST APIs.
- Will use the native VTEX ID page to [authenticate shoppers](#authentication).
- Can build your storefront using a third-party Content Management System (CMS), instead of VTEX storefront solutions, except for the authentication page.
- Can use VTEX IO to host core commerce microservices and any developed applications to extend functionality.

![headless integration](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Integration-Guides/headless-commerce/headless-integration.jpg)

>ℹ️ This document outlines the basic features required to deliver any shopping experience and does not limit the VTEX capabilities you can use. You are free to use any VTEX features that benefit your store, even if they are not mentioned above.

## Authentication

When it comes to authentication, a headless store must consider two aspects:

- [Authenticating shopper identity](#authenticating-shopper-identity)
- [Authenticating requests to VTEX APIs](#authenticating-requests-to-vtex-apis)

>ℹ️ We recommend you also learn more about:

    - [VTEX authentication for developers](https://developers.vtex.com/vtex-rest-api/docs/getting-started-authentication).
    - [VTEX native login](https://help.vtex.com/en/tutorial/authentication-page--21CkKHLKP1o41lUpGhuRUs)
    - [VTEX native login settings](https://help.vtex.com/en/subcategory/authentications-settings--cgsivNN3J6M6gKAYoeIww)

### Authenticating shopper identity

Currently, VTEX does not support any form of headless shopper authentication. Because of this, we recommend that you direct shoppers to the native VTEX login page so they can log in to your store.

Whenever a shopper requires authentication in your store, your interface must:

1. Direct the shopper to this URL on an internet browser:
  ```bash
  {yourStoreUrl}/login
  ```
2. Once the shopper has successfully logged in, VTEX will set a [user token](https://developers.vtex.com/vtex-rest-api/docs/getting-started-authentication#user-token) in a cookie named `VtexIdclientAutCookie`.
3. Store this user token. You must use it to authenticate API requests.

### Authenticating requests to VTEX APIs

There are different [machine authentication methods](https://developers.vtex.com/vtex-rest-api/docs/getting-started-authentication#machine-authentication) available for you to authenticate your integration's requests to VTEX APIs.

For the purpose of headless stores, we recommend using [user tokens](https://developers.vtex.com/vtex-rest-api/docs/getting-started-authentication#user-token) whenever possible. You can obtain this token as indicated in the section [Authenticating shoppers' identity](#authenticating-shopper-identity).

You can also use [application keys](https://developers.vtex.com/vtex-rest-api/docs/getting-started-authentication#api-keys) in contexts where shoppers authentication is not necessary, such as product search.

## Shopping experience

You can think of a customer's journey in your headless store as divided into three main parts, which connect to different VTEX APIs and features. See the guides below to learn how to implement each of these parts:

- [Viewing catalog information](https://developers.vtex.com/docs/guides/headless-catalog)
- [Placing orders](https://developers.vtex.com/docs/guides/headless-cart-and-checkout)
- [Viewing account information](https://developers.vtex.com/docs/guides/headless-profile-management-and-order-history)
