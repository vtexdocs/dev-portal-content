---
title: "Cart information: maximum storage time reduced from six to three months"
slug: "cart-information-maximum-storage-time-reduced-from-six-to-three-months"
type: "improved"
createdAt: "2022-07-05T11:52:18.269Z"
hidden: false
---
The <code>orderFormId</code> is the parameter that allows identifying a cart and verifying what information is present in it (items, payment method, delivery channel, etc.).

Previously, you could access a cart's information for up to six months after it was created.

From now on, the cart information, as well as the items chosen by the customer, will no longer be accessible after three months of creating the cart. After this period, the <code>orderFormId</code> can be automatically reassigned to any new cart created.

**Important**: This change does not affect the information used to send abandoned cart e-mails (which can be accessed at any time), as they come from the user profile (Master Data) and represents only the items from the last cart.

Learn more at [Shared Cart](https://help.vtex.com/en/tutorial/o-que-e-o-carrinho-compartilhado--3oKJZfoAoUm8g0ukCIGsUu#) and [Abandoned Cart](https://help.vtex.com/en/tutorial/acesse-o-carrinho-abandonado-dos-clientes--4bbXy1TlzJaiCr41xKDN4e#).