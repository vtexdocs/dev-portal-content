---
title: "Start handling order"
slug: "starthandlingpiicompliant"
excerpt: "Change the status of an order to indicate that is is in `handling`.\n\r\n\r> Expect a `status 204` response with no content in case of a successful request.\n\r\n\r> The `Change order workflow status` resource is needed to use this API request. This is included in `OMS - Full access` and `IntegrationProfile - Fulfillment Oms`, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#)."
hidden: true
createdAt: "2022-04-26T15:47:38.590Z"
updatedAt: "2022-04-26T19:49:53.529Z"
---
## Atributes

| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `orderId` | string | Order ID |

## Request body example

```json
curl --location --request POST 'https://{{accountName}}.{{environment}}.com.br/api/oms/pvt/orders/{{orderId}}/start-handling' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \
--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'
```

## Response codes


204 - [No content](https://httpstatuses.com/204)

429 - [Too many requests](https://httpstatuses.com/429)

403 - [The credentials are not enabled to access the service](https://httpstatuses.com/403)

404 - [Not found](https://httpstatuses.com/404)