---
title: "Formatting order invoicing time via API"
slug: "formatting-order-invoicing-time"
hidden: false
createdAt: "2022-08-30T21:58:00.958Z"
updatedAt: "2022-08-30T21:58:00.958Z"
---
When submitting invoice data to a marketplace via API, you can use the endpoint [Update order's partial invoice](https://developers.vtex.com/vtex-rest-api/reference/updatepartialinvoicesendtrackingnumber) to format the order invoicing time. The correct JSON format for the request is as the following example:
[block:code]
{
  "codes": [
    {
      "code": "{\n \"type\":\"Output\",\n \"issuanceDate\":\"2017-10-05T11:32:11\",\n \"invoiceNumber\":\"9999\",\n \"invoiceValue\":\"10000\",\n \"invoiceKey\": null,\n \"invoiceUrl\": null,\n \"courier\": null,\n \"trackingNumber\": null,\n \"trackingUrl\": null,\n \"items\": [\n   {\n     \"id\": \"1234\",\n     \"price\": 10000,\n     \"quantity\": 1\n    }\n  ]\n }",
      "language": "json"
    }
  ]
}
[/block]

The property responsible for informing the invoicing date and time is `issuanceDate`. This field follows the UTC 0 time zone. 

If you want to include a time with a specific time zone (for example: "UTC -3"), you must use a format like the example below:

`"issuanceDate": "2017-10-05T11:32:11-0300"`

**Attention:** Do not use any spaces on the date.

Note that integrations that fetch order data from the VTEX system should also be aware of the time zone and make the necessary adjustments.

For details on how the request should be formatted, see the API [Update order's partial invoice](https://developers.vtex.com/vtex-rest-api/reference/updatepartialinvoicesendtrackingnumber).