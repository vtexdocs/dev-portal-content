---
title: "VTEX Shipping Network Labels Integration"
slug: "vtex-shipping-network-labels-integration"
hidden: false
createdAt: "2023-03-01T16:44:01.460Z"
updatedAt: "2023-09-11T16:44:01.460Z"
---

> This feature is in beta, which means that we are working to improve it. If you have any questions, please contact our [Support](https://help.vtex.com/support).

[VTEX Shipping Network](https://help.vtex.com/pt/tutorial/vtex-shipping-network-correios-ativacao--57opHihFbRAwrjQjCTymTa) is the solution that uses order tracking data directly from [carriers](https://help.vtex.com/en/tutorial/carries-on-vtex--7u9duMD5UQa2QQwukAWMcE) to keep merchants and shoppers up to date with the status of each delivery.

## Overview

The VTEX Shipping Network module is responsible for integrating your store with carriers via a defined protocol. The integration is divided into three workflows:

1. Notification
2. Tracking
3. Shipping label creation

 A Package created in the VTEX Shipping Network module (SPN) has the following lifecycle, including these workflows:

1. The cycle begins when an order is invoiced in the OMS module, which results in SPN creating all of its packages. The new packages will have an `Invoiced` [status](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196).
2. The Carrier App will then receive a notification request for all packages, and their status will move to `carrier_notified`.
3. All packages can now have their associated Shipping Label created. Once each label is successfully created, its associated package status moves to `label_issued`.
4. Tagged by its Shipping Label, the package can now be delivered, and while it is in transit, the SPN module requests the Carrier App for tracking updates until the package is tagged as `Delivered`.

The Package lifecycle ends when it is delivered.

![vtex_shipping_network_label_diagram](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Fulfillment/vtex-shipping-network/vtex_shipping_network_label_diagram.png)

## Integration

The endpoint described in this document is responsible for creating the Shipping Labels of all the packages associated with an order. Given an `orderId`, it will provide a URL that when accessed downloads a pdf file containing the Shipping Labels.

>❗ The URL returned by the API is valid for 5 days from the moment it was requested, and expires after that period. If the file is required after the link has expired, only a new request with the same `orderId` will provide a new valid URL.

Be aware that VTEX Shipping Network only keeps track of Fulfillment orders, therefore, the `orderId` used on the endpoint must have their [origin as Fulfillment](https://help.vtex.com/en/tutorial/orders-list--tutorials_200#origin). All Fulfillment Orders contain a prefix, for example:

- **Order with prefix:** 00-1307463503290-01
- **Order without prefix:** 1307463503290-01

The order origin can be found using the [Orders API documentation](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders/-orderId-). If the order has other origins rather than Fulfillment, the Order.sellerOrderId field should be used, as it references the Fulfillment Order.

### Endpoint

Order with Fulfillment origin:

**POST** - `https://api.vtex.com/api/transportation/deliverylabels/{orderId}`

Order with another origin:

**POST** - `https://api.vtex.com/api/transportation/deliverylabels/{sellerOrderId}`

The [authentication](https://developers.vtex.com/docs/guides/authentication-overview#api-keys) headers must be used to call this endpoint:

- X-VTEX-API-AppKey
- X-VTEX-API-AppToken

> To use the endpoint, the appKey and appToken must have `TransportationViewer` or `TransportationAdmin` [License Manager resources](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3) and [roles](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) associated with them.

### Example cURL request

```sh
curl --location --request POST 'https://api.vtex.com/api/transportation/deliverylabels/{{orderId}}?an={{accountName}}' \
--header 'X-VTEX-API-AppToken: {{token}}' \
--header 'X-VTEX-API-AppKey: {{appKey}}'
```

### Responses

The successful response has the following format:

- Status code: 200 (OK)
- Response body:

```json
{
    "url" : "www.labelexampledownload.com"
}
```

This endpoint can return other status codes in the following scenarios:

| **Code** | **Message** | **Description** |
| ---------- | ---------- | ---------- |
| 400 | `Package {packageId} has an invalid state!` | One or more packages associated with the `orderId` have an invalid status. This might happen if the carrier app has not been notified about the package yet. Retry the operation in a few minutes. |
| 401 | `Unauthorized` | [Authentication](https://developers.vtex.com/docs/guides/authentication-overview#api-keys) credentials are missing. Make sure to include the headers `X-VTEX-API-AppToken` and `X-VTEX-API-AppKey`. |
| 403 | `reason: User does not have access to the resources [TransportationAdmin]` | Forbidden response status code indicates that the request has not been completed because it lacks valid authentication credentials for the requested resource. In this case, the header values `X-VTEX-API-AppToken` or `X-VTEX-API-AppKey` are invalid. |
| 404 | `Not Found` | The `orderId` provided does not belong to any existing order. This might happen if the `orderId` does not contain the correct prefix. |
| 500 | `Internal Server Error` | Unexpected error. |

## Configuring shipping labels printing format

In the VTEX Admin, you can configure the shipping labels printing format as a **A4** (297x210mm) or a **ZPL** (Zebra Programming Language) extension. You will find the instructions in our Help Center article [Pronto para envio](https://help.vtex.com/pt/tutorial/pronto-para-envio--5YOZV7Aotv3pap0fGNESDs).
