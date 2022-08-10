---
title: "Update Feed Configuration"
slug: "feedconfiguration"
excerpt: "Configures the filter rule applied to Feed V3."
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2020-04-17T05:04:31.019Z"
---
Learn more about [Feed v3 in VTEX Help](https://help.vtex.com/pt/tutorial/feed-v3-de-gerenciamento-de-pedidos)



| Attribute    | Type        | Description |
| --------------- |:-------------:| ----------------------------------:|
| `filter`| object | Status Filter Array Details |
| `status`| array | The events status array to filter |
| `queue`| object | Array of string |
| `visibilityTimeoutInSeconds`| integer | Visibility Timeout in Seconds: 30 minimum and 86400 max value |
| `MessageRetentionPeriodInSeconds`| integer | Visibility Timeout in Seconds: 345600 minimum and 1209600 max value |



[block:callout]
{
  "type": "info",
  "title": "",
  "body": "If the `status` array is not configured in the API, all status updates are sent to the feed."
}
[/block]
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

Learn more about [Order Status in VTEX Help](https://help.vtex.com/en/faq/from-to-for-order-status)






## Response codes


200 - Success

403 - The credentials are not enabled to access the service

404 - Value not found

429 - Too many requests

The event will be removed if the message "send retry" is equal to, or greater than the maximum retention period.
[block:api-header]
{
  "title": "Request body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request POST 'https://accountname.vtexcommercestable.com/api/orders/feed/config' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--data-raw '{\n\t\"filter\": {\n\t\t\"status\": [\"order-completed\",\"start-handling\", \"handling\", \"ready-for-handling\", \"waiting-ffmt-authorization\", \"cancel\"]\n\t},\n\t\"queue\":{\n\t\t\n\t\t\"visibilityTimeoutInSeconds\": 250,\n\t\t\"MessageRetentionPeriodInSeconds\":345600\n\t}\n}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]