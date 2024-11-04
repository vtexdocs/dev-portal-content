---
title: "Integrating external orders via API to be used with VTEX Tracking"
slug: "integrate-external-orders-vtex-tracking"
hidden: false
createdAt: "2021-07-21T20:48:44.673Z"
updatedAt: "2024-11-04T19:34:41.464Z"
---
The [VTEX Tracking app](https://help.vtex.com/en/tutorial/vtex-tracking-overview--1uDRquVudbPuoK05MtbZGh) automatically gets invoiced orders’ information from VTEX’s Order Management System (OMS) so as to create delivery routes. However, it is possible to import external orders by using our APIs.

Since the actual fulfillment and tracking only happen for invoiced orders, external order integrations must accomplish four steps in order to create and move the imported orders along the [OMS’s workflow](https://help.vtex.com/en/tutorial/fluxo-de-pedido--tutorials_196#) to the `invoiced` status. The steps are:

1. Place order
2. Authorize dispatch
3. Start handling
4. Send invoice

>ℹ️ Because this type of integration assumes payment is already taken care of when orders are imported, we can use the fulfillment order workflow. This is the same workflow used by sellers integrating with marketplaces, for example.

>ℹ️ Make sure you have [API authentication credentials](https://developers.vtex.com/docs/guides/getting-started-authentication) in order to use the APIs listed below.

## 1. Place order

This step actually creates the order in the [OMS](https://help.vtex.com/en/tutorial/lista-de-pedidos--tutorials_200#).

To do this, use the [Place fulfillment order API request](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-orders#post-/api/fulfillment/pvt/orders).

>❗ In order to successfully place an order on the platform, you must have products already registered in your VTEX [catalog](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ#) and make sure they are available in the platform's [inventory](https://help.vtex.com/en/tutorial/inventory-management--tutorials_139). For this purpose, it may be a good idea to [set unlimited inventory](https://help.vtex.com/en/tutorial/inventory-management--tutorials_139).

>⚠️ The field `marketplaceServicesEndpoint` is required, but not necessarily applicable in the context of integrating orders to VTEX Tracking. Because of this, you may send it with a mock value not corresponding with a real working endpoint, such as `https://exampleseller.marketplaceservices.com`.

### Affiliate ID

Because we are using endpoints typically used by sellers connecting to external marketplaces, steps 1 and 2 will require you to send the `affiliateId` field.

This field is meant to be a three-letter code identifying the marketplace that made the sale to be fulfilled. In the case of importing external orders to VTEX Tracking, you may send any arbitrary three-letter code and the requests should work as expected.

>⚠️ For a given order you should use the same `affiliateId`, `orderId` and `marketplaceOrderId` in steps 2, 3 and 4, as used in this first step when required in the API requests. The `orderId` will be in the response of the [Place fulfillment order request](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-orders#post-/api/fulfillment/pvt/orders) and it is composed of the `affiliateId` and `marketplaceOrderId` joined by a “-`.

>⚠️ Do not use an affiliate that is configured to use the seller's payment methods, or else this request will return a `status 500`. In this case, create a new affiliate without this configuration or use an arbitrary `affiliateId`.

## 2. Authorize dispatch

To move the created order to the next status, use the [Authorize dispatch for fulfillment orders request](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-orders#post-/api/fulfillment/pvt/orders/-orderId-/fulfill).

## 3. Start handling

After dispatch is authorized, the order goes automatically into the grace period also known as the cancellation window. This is a period of time in which the store waits to see if the customer wants to cancel the purchase before it actually starts handling the order. This window is set to 30 minutes by default, but can be changed in the Order Management settings. Learn how to [set the grace period for order cancelation](https://help.vtex.com/en/tutorial/setting-the-grace-period-for-order-cancellation--jYFdnPDtNm4WCEkYWqqC#).

After the grace period, the order status will be `ready-for-handling`. To move it to the next status, use the [Start handling order API request](https://developers.vtex.com/vtex-rest-api/reference/starthandling).

## 4. Send invoice

Use the [Order invoice notification request](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/invoice) to send invoice information to VTEX.

>ℹ️ Note that this step can occur in parallel to steps 2 and 3. Once an order has been created, the platform can receive its invoice information.

You can use the [Order invoice notification request](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/invoice) to send all invoice information at once, or you can send part of the information and update the invoice with the rest of the information later by using the [Update order's partial invoice request](https://developers.vtex.com/docs/api-reference/orders-api#patch-/api/oms/pvt/orders/-orderId-/invoice/-invoiceNumber-).

An example of the latter is when you need to include a tracking number to an invoice that is already registered to the platform.

>ℹ️ This request can be used to send the link to the XML of the invoice, which can be relevant to some VTEX Tracking integrations. Find if that is your case and learn more in this article on [how to install and configure the VTEX Tracking app](https://help.vtex.com/pt/tutorial/how-to-install-and-setup-the-vtex-tracking-app-on-your-vtex-admin--3ejuFsJ1m0r08cT6afpIPf#).

## Checking an integrated order's information

During integration or after you are done integrating a given order with these steps, you can check the order's information and progress in the [Order Management](https://help.vtex.com/en/category/orders-management--2663q96EyQuYc20y0yYAEE#) section in VTEX Admin or with the [Orders API](https://developers.vtex.com/vtex-rest-api/reference/orders).

For order information related to VTEX Tracking, see the [VTEX Tracking API documentation](https://developers.vtex.com/docs/api-reference/tracking).
