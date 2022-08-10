---
title: "Update order tracking status"
slug: "updatetrackingstatus"
excerpt: "Sends a tracking event to an order that already has a tracking number registered to its invoice.\n\r\n\rThis endpoint is not meant to send tracking number and URL to the invoice. If you wish to send tracking number and URL to an order, use the [Update order's partial invoice API request](https://developers.vtex.com/vtex-rest-api/reference/invoice#updatepartialinvoicesendtrackingnumber). You can also learn more about [Partial invoice](https://help.vtex.com/en/tracks/pedidos--2xkTisx4SXOWXQel8Jg8sa/q9GPspTb9cHlMeAZfdEUe) scenarios. \n\r\n\r> The `Notify invoice` resource is needed to use this API request. This is included in `OMS - Full access` and `IntegrationProfile - Fulfillment Oms`, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#)."
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2022-06-27T20:21:48.234Z"
---
[block:callout]
{
  "type": "danger",
  "body": "Do not use this request with orders that do not have a tracking number already added to their invoice. If you wish to send tracking number and URL to an order, use the [Update order's partial invoice API request](https://developers.vtex.com/vtex-rest-api/reference/invoice#updatepartialinvoicesendtrackingnumber)"
}
[/block]
> Learn more about [Transaction Details in VTEX Help](https://help.vtex.com/en/tutorial/how-to-view-the-orders-details)

Important: the **package** is generated when an invoice is added to the order.
**The last tracking's date is not the same as the delivery date.**


## Request object has the following properties:

| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `orderId` | string | Order Id |
| `invoiceNumber` | string | Order Invoice ID |
| `isDelivered` | boolean | If the order package is delivered |
| `deliveredDate` | string | the date when the **package** was delivered. It is not the same as the tracking date parameter. |
| `events` | object | Events Details Object |
| `city` | string | Event Tracking City |
| `state` | string | Event Tracking State |
| `description` | Event Tracking Description | This field is limited to 5000 characters |
| `date` | string | Event Tracking Date in international format `yyyy-mm-dd` |

> If `isDelivered` is true, the field `finished`  changes to *true*. The `courierStatus` field of `status` remains as **unknown**. This field can be found in the Order details of the. 

## Response object has the following properties:

| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `date` | string | Tracking Update Date|
| `orderId` | string | Order ID Update |
| `receipt` | string | Tracking Update Receipt |
[block:api-header]
{
  "title": "Request body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request PUT 'https://lojadosuporte.vtexcommercestable.com.br/api/oms/pvt/orders/v501245lspt-01/invoice/0102030405/tracking' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--data-raw '{\n  \"isDelivered\": true,\n  \"events\": [\n    {\n      \"city\": \"Rio de Janeiro\",\n      \"state\": \"RJ\",\n      \"description\": \"Coletado pela transportadora\",\n      \"date\": \"2015-06-23\"\n    },\n    {\n      \"city\": \"Sao Paulo\",\n      \"state\": \"SP\",\n      \"description\": \"A caminho de Curitiba\",\n      \"date\": \"2015-06-24\"\n    }\n  ]\n}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Response body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"date\": \"2017-03-29T18:04:31.0521233+00:00\",\n  \"orderId\": \"v501245lspt-01\",\n  \"receipt\": \"f67d33a8029c42ce9a8f07fc17f54449\"\n}",
      "language": "text",
      "name": "200 - OK"
    }
  ]
}
[/block]