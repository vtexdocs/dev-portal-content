---
title: "Start handling order"
slug: "starthandling"
excerpt: "Change the status of an order to indicate that is is in `handling`.\n\r\n\r> Expect a `status 204` response with no content in case of a successful request. The store must validate this response to retry the call if the responses differs from the 204 code, making this flow the store's responsibility. This endpoint can also respond with `status 500`. \n\r\n\r> The `Change order workflow status` resource is needed to use this API request. This is included in `OMS - Full access` and `IntegrationProfile - Fulfillment Oms`, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#)."
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2022-06-27T20:21:47.649Z"
---
[block:api-header]
{
  "title": "Attributes"
}
[/block]
| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `orderId` | string | Order ID |

[block:api-header]
{
  "title": "Request body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request POST 'https://{{accountName}}.{{environment}}.com.br/api/oms/pvt/orders/{{orderId}}/start-handling' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
      "language": "json",
      "name": "CURL"
    }
  ]
}
[/block]
## Response codes


204 - [No content](https://httpstatuses.com/204)

429 - [Too many requests](https://httpstatuses.com/429)

403 - [The credentials are not enabled to access the service](https://httpstatuses.com/403)

404 - [Not found](https://httpstatuses.com/404)