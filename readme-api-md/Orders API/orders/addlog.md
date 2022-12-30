---
title: "Add log in orders"
slug: "addlog"
excerpt: "Add a Log in Interactions Order Array."
hidden: true
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2021-05-18T21:41:42.331Z"
---
> Learn more about [Changing completed orders in VTEX Help](https://help.vtex.com/en/tutorial/change-making-changes-to-an-order)



| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `orderId` | string | Order ID |
| `source` | string | Log Source |
| `message` | integer | Log Message |






## Response codes


204 - Success

429 - Too many requests

403 - The credentials are not enabled to access the service

404 - Value not found 
[block:api-header]
{
  "title": "Request body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request POST 'https://{{accountName}}.{{environment}}.com.br/api/oms/pvt/orders/{{orderId}}/interactions' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--data-raw '{\n     \"source\":\"Postman\",                    \n     \"message\":\"Teste add interactions\"\n}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]