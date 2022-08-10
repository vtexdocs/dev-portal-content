---
title: "Create or Update Hook Configuration"
slug: "hookconfiguration"
excerpt: "Configure filter rules to Order Hook"
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2020-02-28T14:18:16.876Z"
---
Learn more about [Feed v3 in VTEX Help.](https://help.vtex.com/pt/tutorial/feed-v3-de-gerenciamento-de-pedidos)




| Attribute    | Type        | Description |
| --------------- |:-------------:| ----------------------------------:|
| `filter`| object | Status Filter Array |
| `status`| object | The events status to filter |
|`hook`| object | Object of EndPoint infos|
| `url`| integer | End Point URL |
| `headers`| object | Credentials Array |
| `key`|string | Endpoint key |


| Status avaible to filter    |
| --------------------------- |
|order-created order-completed|
|on-order-completed|
|payment-pending| 
|waiting-for-order-authorization|
|approve-payment|
|payment-approved|
|payment-denied|
|request-cancel|
|waiting-for-seller-decision|
|authorize-fulfillment|
|order-create-error|
|order-creation-error|
|window-to-cancel|
|ready-for-handling|
|start-handling|
|handling|
|invoice-after-cancellation-deny|
|order-accepted|
|invoice|
|invoiced|
|replaced|
|cancellation-requested|
|cancel|
|canceled|


Learn more about [Order Status in VTEX Help.](https://help.vtex.com/en/faq/from-to-for-order-status)




## Response codes


200 - Success

400 - Bad Request  - "Unable to check address" / "Only https scheme is accepted"

403 - The credentials are not enabled to access the service

404 - Value not found 

429 - Too many requests

The status event will be removed, if it can't deliver a message more than 100 times, 4 days progressively.



[block:api-header]
{
  "title": "Request body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request POST 'https://{{accountName}}.vtexcommercestable.com/api/orders/hook/config' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--data-raw '{\n    \"filter\": {\n        \"status\": [\"order-completed\", \"handling\", \"ready-for-handling\", \"waiting-ffmt-authorization\", \"cancel\"]\n    },\n    \"hook\": {\n        \"url\": \"https://endpoint.example/path\",\n        \"headers\": {\n            \"key\": \"value\"\n        }\n    }\n}'",
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
      "code": "{\n  \"Domain\": \"Fulfillment\",\n  \"OrderId\": \"v52277740atmc-01\",\n  \"State\": \"ready-for-handling\",\n  \"LastState\": \"window-to-cancel\",\n  \"LastChange\": \"2019-08-14T17:11:39.2550122Z\",\n  \"CurrentChange\": \"2019-08-14T17:12:48.0965893Z\",\n  \"Origin\": {\n    \"Account\": \"automacaoqa\",\n    \"Key\": \"vtexappkey-appvtex\"\n  }\n}",
      "language": "text",
      "name": "200 - OK"
    }
  ]
}
[/block]