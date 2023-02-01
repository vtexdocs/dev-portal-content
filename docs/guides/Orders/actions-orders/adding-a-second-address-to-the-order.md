---
title: "Adding a second address for invoicing an order"
slug: "adding-a-second-address-to-the-order"
hidden: false
createdAt: "2022-08-30T22:57:21.319Z"
updatedAt: "2022-08-30T23:20:03.471Z"
---
For B2B businesses, it is common to add to the invoice an address that is different from the one registered for delivery, since the location where the product will be received is often different from the billing address.

VTEX Admin allows you to add a second address only in the case of [Pickup Points](https://help.vtex.com/en/tutorial/pickup-points--2fljn6wLjn8M4lJHA6HP3R) because there will be only one address for the invoice. For other cases, adding a second address must be done via API, using the [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) object. 

The `orderForm` is the main object processed by VTEX Checkout, and one of the most important data structures in VTEX stores' architecture. 

There are two ways to manipulate data from the `orderForm` to enter a second address:

- Using the vtex.js library
- Through API REST

<br>

[block:callout]
{
  "type": "warning",
  "body": "Although it is possible to create a custom interface superimposed on that of VTEX containing the second address field, we do not recommend it, because it increases the chances of errors in order management."
}
[/block]
<br> 

## vtex.js

The vtex.js is a library of JavaScript functions that will do the API requests. The function used for this is the `sendAttachment`. Fore more information, see the [specific library documentation](https://github.com/vtex/vtex.js/tree/master/docs/checkout#sendattachmentattachmentid-attachment-expectedorderformsections).

## API REST

To add a second address to an order via API, make a POST request to the endpoint below: 

`/api/checkout/pub/orderForm/{{orderFormId}}/attachments/invoiceData`

The `{{orderFormId}}` value must be replaced by the ID of the orderForm that you want to manipulate.

In the `orderForm` object there is the object` invoiceData`, which contains information about the order's invoice and contains the field `address`. This field must be set with the second address you wish to add. The request body looks like the example below:

<br>
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"address\": {\n        \"postalCode\": \"22250-040\",\n        \"city\": \"Rio de Janeiro\",\n        \"state\": \"RJ\",\n        \"country\": \"BRA\",\n        \"street\": \"Praia Botafogo\",\n        \"number\": \"300\",\n        \"neighborhood\": \"Botafogo\",\n        \"complement\": null,\n        \"reference\": null,\n        \"geoCoordinates\": [\n            -43.18218231201172,\n            -22.94549560546875\n        ]\n    }\n}",
      "language": "json"
    }
  ]
}
[/block]