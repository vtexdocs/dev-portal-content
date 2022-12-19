---
title: "List orders"
slug: "listorders"
excerpt: "Retrieves a list of orders according to the filters described below.\n\r\n\r> This should **not** be used for integrations. Use the [orders Feed or hook](https://developers.vtex.com/vtex-rest-api/docs/feed-v3-1) for this purpose.\n\r\n\rThis endpoint returns only orders that already have been indexed, which takes approximately four minutes. Because of this, the data retrieved may present inconsistencies. To get live up-to-date information and [build order integrations](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-set-up-order-integration) use the [orders Feed or hook](https://developers.vtex.com/vtex-rest-api/docs/feed-v3-1).\n\r\n> 📘 Onboarding guide \r\n>\r\n> Check the new [Orders onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/orders-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Orders and is organized by focusing on the developer's journey."
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2022-08-31T20:24:40.224Z"
---
[block:callout]
{
  "type": "danger",
  "body": "This endpoint returns only orders that already have been indexed, which takes aproximately four minutes. Because of this, the data retrieved may present inconsistencies or become unavailable in periods of peak order volume. \n\nIn other words, **order integrations built with the List orders endpoint are not reliable** and **will not be supported**. To get live up to date information and [build order integrations](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-set-up-order-integration) use the [orders Feed or hook](https://developers.vtex.com/vtex-rest-api/docs/feed-v3-1).",
  "title": "Do not use this request for integrations"
}
[/block]

[block:api-header]
{
  "title": "Throttling"
}
[/block]

> ℹ️ Throttling: Each account can make up to 5000 requests per minute.

[block:api-header]
{
  "title": "Request parameters allowed"
}
[/block]
| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `orderBy` | string | Order Field and Order Type concatenated `orderBy={{OrderField}},{{OrderType}}`  |
| `OrderField` | string | Order Field expected values: `creationDate`,`orderId`,`items`,`totalValue` and `origin` |
| `OrderType` | string | Order Type expected values: `asc` and `desc`  |

### Sorting Examples

CreationDate:

 /api/oms/pvt/orders?orderBy=creationDate,desc

OrderID:

 /api/oms/pvt/orders?orderBy=orderId,desc

Items:

 /api/oms/pvt/orders?orderBy=items,asc

TotalValue:

 /api/oms/pvt/orders?orderBy=totalValue,desc

Origin:

 /api/oms/pvt/orders?orderBy=origin,asc

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `page` | integer | Page Number  |

### Pagination Examples

 /api/oms/pvt/orders?page=3

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `per_page` | integer | Quantity orders per page  |

Quantity per Page Examples:

 /api/oms/pvt/orders?per_page=15

> ℹ️ Pagination Limit: The limit of pages that can be requested is 30.</div>

### Time zone query

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `utc` | integer | Time Zone. By including this parameter alone in your query, the call will not convert the UTC nor show the amount of orders set for that UTC. To filter orders with the desired UTC, you must also modify date and time in the `f_creationDate=creationDate:` parameter.  |

Time Zone Example:

 /api/oms/pvt/orders?utc=-0200

## Request filters

### Fulltext

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `q` | string | Fulltext accepts Order Ids, Client E-mail, Client Document and Client Name  |

> The "+" caracter isn't allowed in Fulltext Search

Fulltext filter Examples:

OrderID:
 
 /api/oms/pvt/orders?q=v212333lux-02

Email:
 
 /api/oms/pvt/orders?q=rodrigo.cunha@vtex.com

Document:
 
 /api/oms/pvt/orders?q=21133355524

ClientName:

 /api/oms/pvt/orders?q=Cunha

### Shipping Estimate

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `f_shippingEstimate` | string | Concatened value of quantity days and sufix `.days`  |

Shipping Estimate filter Examples:

Next 7 days:

 /api/oms/pvt/orders?f_shippingEstimate=7.days

Tomorrow:

 /api/oms/pvt/orders?f_shippingEstimate=1.days

Today:
 
 /api/oms/pvt/orders?f_shippingEstimate=0.days

Late:
 
 /api/oms/pvt/orders?f_shippingEstimate=-1.days

### Invoiced Date

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `f_invoicedDate` | string | Concatened value sufix `invoicedDate` and range date in Timestamp format  |

Invoiced Date filter Examples:

1 Day:

 /api/oms/pvt/orders?f_invoicedDate=invoicedDate:[2017-01-01T02:00:00.000Z TO 2017-01-02T01:59:59.999Z]

1 Month:
 
 /api/oms/pvt/orders?f_invoicedDate=invoicedDate:[2017-01-01T02:00:00.000Z TO 2017-02-01T01:59:59.999Z]

1 Year:

 /api/oms/pvt/orders?f_invoicedDate=invoicedDate:[2016-01-01T02:00:00.000Z TO 2017-01-01T01:59:59.999Z]

### Order Date

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `f_creationDate` | string | Concatened value sufix `creationDate` and range date in Timestamp format  |

Order Date filter Examples:

1 Day:

 /api/oms/pvt/orders?f_creationDate=creationDate:[2017-01-01T02:00:00.000Z TO 2017-01-02T01:59:59.999Z]

1 Month:

 /api/oms/pvt/orders?f_creationDate=creationDate:[2017-01-01T02:00:00.000Z TO 2017-02-01T01:59:59.999Z]

1 Year:

 /api/oms/pvt/orders?f_creationDate=creationDate:[2016-01-01T02:00:00.000Z TO 2017-01-01T01:59:59.999Z]

### Authorized Date

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `f_authorizedDate` | string | Concatened value sufix `authorizedDate` and range date in Timestamp format  |

Authorized Date filter Examples:

1 Day:

 /api/oms/pvt/orders?f_authorizedDate=authorizedDate:[2017-01-01T02:00:00.000Z TO 2017-01-02T01:59:59.999Z]

1 Month:

 /api/oms/pvt/orders?f_authorizedDate=authorizedDate:[2017-01-01T02:00:00.000Z TO 2017-02-01T01:59:59.999Z]

1 Year:

 /api/oms/pvt/orders?f_authorizedDate=authorizedDate:[2016-01-01T02:00:00.000Z TO 2017-01-01T01:59:59.999Z]

### UTMs

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `f_UtmSource` | string | UTM Source value  |

Channels filter Examples:

 /api/oms/pvt/orders?f_UtmSource=buscape_campaign

### Seller

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `f_sellerNames` | string | Seller Name value  |

Seller filter Examples:

 /api/oms/pvt/orders?f_sellerNames=Fast+Shop

### Call Center Operator

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `f_callCenterOperatorName` | string | Call Center Operator Value  |

Call Center Operator filter Examples:

 /api/oms/pvt/orders?f_callCenterOperatorName=Operator%20Name

### Sales Channel Name

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `f_salesChannel` | string | Sales Channel Name Value  |

Sales Channel Name filter Examples:

 /api/oms/pvt/orders?f_salesChannel=Main

### Sales Channel ID

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `salesChannelId` | string | Sales Channel ID Value  |

Sales Channel ID filter Examples:

 /api/oms/pvt/orders?salesChannelId=1

### Affiliate ID

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `f_affiliateId` | string | Affiliate ID Value  |

Affiliate ID filter Examples:

 /api/oms/pvt/orders?f_affiliateId=WLM

### Order Status

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `f_status` | string | Order Status Value  |

| Order Status avaible to filter    |
| --------------------- |
| `waiting-for-sellers-confirmation` |
| `payment-pending` |
| `payment-approved` |
| `ready-for-handling` |
| `handling` |
| `invoiced` |
| `canceled` |

Order Status filter Examples:

 /api/oms/pvt/orders?f_status=ready-for-handling

### Order Status Description

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `f_statusDescription` | string | Order Status Description Value  |

| Order Status Description avaible to filter |
| --------------------- |
| `Aguardando+autorização+para+despachar` |
| `Pagamento+Pendente` |
| `Pagamento+Aprovado` |
| `Pronto+para+o+manuseio` |
| `Preparando+Entrega` |
| `Faturado` |
| `Cancelado` |

Order Status Description filter Examples:

 /api/oms/pvt/orders?f_statusDescription=Pronto+para+o+manuseio

### Order Situation

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `incompleteOrders` | boolean | If is a Incomplete Order  |

> know more about [Incomplete Orders in VTEX Help](https://help.vtex.com/en/tutorial/understanding-incomplete-orders)

Order Situation filter Examples:

 /api/oms/pvt/orders?incompleteOrders=true

### Error Situation

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `incompleteOrders` | boolean | Error Situation Type  |

| Error Situation Values avaible to filter |
| ------- |
| `all` |
| `perm` |
| `temp` |  

Error Situation filter Examples:

 /api/oms/pvt/orders?filterError=all

### Payment Type Name

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `f_paymentNames` | string | Payment Type Value  |

Payment Type Name filter Examples:

 /api/oms/pvt/orders?f_paymentNames=Visa

### Rates and Benefits Name

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `f_RnB` | string | Rates and Benefits Name  |

Rates and Benefits filter Examples:

 /api/oms/pvt/orders?f_RnB="Free+Shipping"

### Search Field

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `searchField` | string | Affiliate ID Value  |
| `sku_Ids&sku_Ids` | integer | SKU ID  |
| `listId&listId` | integer | Gift List ID  |
| `tid&tid` | integer | Transaction ID (TID)  |
| `pci_tid&pci_tid` | integer | PCI Connector's Transaction ID (TID)  |
| `paymentId&paymentId` | integer | Payment ID (PID)  |
| `nsu&nsu` | integer | Connector's NSU  |

Search Field filter Examples:

SKU ID:
 
 /api/oms/pvt/orders?searchField=sku_Ids&sku_Ids=11223

Gift List ID:
 
 /api/oms/pvt/orders?searchField=listId&listId=11223

Transaction ID (TID):
 
 /api/oms/pvt/orders?searchField=tid&tid=54546300238810034995829230012

PCI Connector's Transaction ID (TID):

 /api/oms/pvt/orders?searchField=pci_tid&pci_tid=7032909234899834298423209

Payment ID (PID):
 
 /api/oms/pvt/orders?searchField=paymentId&paymentId=2

Connector's NSU:
 
 /api/oms/pvt/orders?searchField=nsu&nsu=2437281

<div class="alert alert-warning">As of October 3, 2018, this API will not return the <strong>"items"</strong> property.</div>

[block:api-header]
{
  "title": "Response objects"
}
[/block]
**Response object has the following properties:**

| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `list` | object | Order List Object |
| `shippingEstimateDate` | string | Estimate Shipping Date |
| `affiliateId` | string | Seller Name who was responsible for the order |
| `authorizedDate` | string | Authorized Order Date |
| `callCenterOperatorData` | string | Call Center Operator responsible for the order |
| `name` | string | Client Name|
| `creationDate` | string | Order Creation Date |
| `currencyCode` | string | Currency Code in ISO 4217  |
| `items` | object | Obsolete Field  |
| `lastMessageUnread` | string | Last sent transactional message  |
| `listId` | string | Releated Gift List Id |
| `listType` | string | Releated Gift List Type |
| `marketplaceOrderId` | string | Marketplace Order Id |
| `orderId` | string | Change receipt order Id |
| `orderIsComplete` | boolean | If is a Order Completed |
| `origin` | string | Order Origin: "Marketplace" or "Fulfillment" |
| `paymentNames` | string | Payment System Name |
| `salesChannel` | string | Order Sales Channel Id |
| `sequence` | string | Order Sequence ID |
| `status` | string | Order Status |
| `statusDescription` | string | Status Description |
| `totalItems` | integer | Total Order Items |
| `totalValue` | integer | Total Value Amount |
| `workflowInErrorState` | boolean | If is a Work Flow Error |
| `workflowInRetry` | boolean | If is in a Work Flow Retry |
| `paging` | object | Paging Details Object |
| `pages` | integer | Paging Total Pages |
| `perPage` | integer | Paging total per Page |
| `total` | integer | Total Result |
| `stats` | object | Results segmented by `totalItems` and `totalValue` |
| `totalItems` | integer | Total Order Items segmeted by `currencyCode` and `origin`|
| `totalValue` | integer | Total Value Amount segmeted by `currencyCode` and `origin`|
| `currencyCode` | string | Currency Code in ISO 4217  |
| `origin` | string | Order Origin: "Marketplace" or "Fulfillment" |
| `Count` | integer | Orders Count |
| `Facets` | object | Grouping Object |
| `Max` | object | Paging Details Object |
| `Mean` | object | Paging Details Object |
| `Min` | object | Paging Details Object |
| `Missing` | object | Paging Details Object |
| `StdDev` | object | Paging Details Object |
| `Sum` | object | Paging Details Object |
| `SumOfSquares` | object | Paging Details Object |
[block:api-header]
{
  "title": "Request body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET 'https://luxstore.{{environment}}.com.br/api/oms/pvt/orders?_stats=1&f_creationDate=creationDate:%5B2018-08-08T03:00:00.000Z+TO+2019-02-09T01:59:59.999Z%5D&orderBy=creationDate,desc&page=1&utc=-0200' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
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
      "code": "{\n  \"list\": [\n    {\n      \"orderId\": \"v502559llux-01\",\n      \"creationDate\": \"2019-02-04T10:29:11.0000000+00:00\",\n      \"clientName\": \"J C\",\n      \"items\": null,\n      \"totalValue\": 7453,\n      \"paymentNames\": \"Boleto Bancário\",\n      \"status\": \"invoiced\",\n      \"statusDescription\": \"Faturado\",\n      \"marketPlaceOrderId\": null,\n      \"sequence\": \"502559\",\n      \"salesChannel\": \"1\",\n      \"affiliateId\": \"\",\n      \"origin\": \"Marketplace\",\n      \"workflowInErrorState\": false,\n      \"workflowInRetry\": false,\n      \"lastMessageUnread\": \" Lux Store 96 Sua Nota Fiscal foi emitida. Referente ao Pedido #v502559llux-01 Olá, J. Estamos empacotando seu produto para providenci\",\n      \"ShippingEstimatedDate\": null,\n      \"ShippingEstimatedDateMax\": null,\n      \"ShippingEstimatedDateMin\": null,\n      \"orderIsComplete\": true,\n      \"listId\": null,\n      \"listType\": null,\n      \"authorizedDate\": \"2019-02-07T21:29:54.0000000+00:00\",\n      \"callCenterOperatorName\": null,\n      \"totalItems\": 1,\n      \"currencyCode\": \"BRL\"\n    },\n    {\n      \"orderId\": \"v502556llux-01\",\n      \"creationDate\": \"2019-01-28T20:09:43.0000000+00:00\",\n      \"clientName\": \"Rodrigo VTEX\",\n      \"items\": null,\n      \"totalValue\": 1160,\n      \"paymentNames\": \"Boleto Bancário\",\n      \"status\": \"handling\",\n      \"statusDescription\": \"Preparando Entrega\",\n      \"marketPlaceOrderId\": null,\n      \"sequence\": \"502556\",\n      \"salesChannel\": \"1\",\n      \"affiliateId\": \"\",\n      \"origin\": \"Marketplace\",\n      \"workflowInErrorState\": false,\n      \"workflowInRetry\": false,\n      \"lastMessageUnread\": \" Lux Store Seu pedido foi alterado! Pedido realizado em: 28/01/2019 Olá, Rodrigo. Seu pedido foi alterado. Seguem informações abaixo: \",\n      \"ShippingEstimatedDate\": \"2019-02-04T20:33:46.0000000+00:00\",\n      \"ShippingEstimatedDateMax\": null,\n      \"ShippingEstimatedDateMin\": null,\n      \"orderIsComplete\": true,\n      \"listId\": null,\n      \"listType\": null,\n      \"authorizedDate\": \"2019-01-28T20:33:04.0000000+00:00\",\n      \"callCenterOperatorName\": null,\n      \"totalItems\": 1,\n      \"currencyCode\": \"BRL\"\n    },\n    {\n      \"orderId\": \"v502553llux-01\",\n      \"creationDate\": \"2019-01-24T12:35:19.0000000+00:00\",\n      \"clientName\": \"test test\",\n      \"items\": null,\n      \"totalValue\": 10150,\n      \"paymentNames\": \"Mastercard\",\n      \"status\": \"ready-for-handling\",\n      \"statusDescription\": \"Pronto para o manuseio\",\n      \"marketPlaceOrderId\": null,\n      \"sequence\": \"502554\",\n      \"salesChannel\": \"1\",\n      \"affiliateId\": \"\",\n      \"origin\": \"Marketplace\",\n      \"workflowInErrorState\": false,\n      \"workflowInRetry\": false,\n      \"lastMessageUnread\": \" Lux Store 96 Sua Nota Fiscal foi emitida. Referente ao Pedido #v502553llux-01 Olá, test. Estamos empacotando seu produto para provide\",\n      \"ShippingEstimatedDate\": \"2019-01-31T12:36:30.0000000+00:00\",\n      \"ShippingEstimatedDateMax\": null,\n      \"ShippingEstimatedDateMin\": null,\n      \"orderIsComplete\": true,\n      \"listId\": null,\n      \"listType\": null,\n      \"authorizedDate\": \"2019-01-24T12:36:01.0000000+00:00\",\n      \"callCenterOperatorName\": null,\n      \"totalItems\": 1,\n      \"currencyCode\": \"BRL\"\n    },\n    {\n      \"orderId\": \"v502550llux-01\",\n      \"creationDate\": \"2019-01-23T16:39:45.0000000+00:00\",\n      \"clientName\": \"test test\",\n      \"items\": null,\n      \"totalValue\": 10150,\n      \"paymentNames\": \"Mastercard\",\n      \"status\": \"ready-for-handling\",\n      \"statusDescription\": \"Pronto para o manuseio\",\n      \"marketPlaceOrderId\": null,\n      \"sequence\": \"502551\",\n      \"salesChannel\": \"1\",\n      \"affiliateId\": \"\",\n      \"origin\": \"Marketplace\",\n      \"workflowInErrorState\": false,\n      \"workflowInRetry\": false,\n      \"lastMessageUnread\": \" Lux Store 96 Seu pagamento foi aprovado. Referente ao Pedido #v502550llux-01 Olá, test. Estamos providenciando a emissão da Nota Fisc\",\n      \"ShippingEstimatedDate\": \"2019-01-30T16:40:55.0000000+00:00\",\n      \"ShippingEstimatedDateMax\": null,\n      \"ShippingEstimatedDateMin\": null,\n      \"orderIsComplete\": true,\n      \"listId\": null,\n      \"listType\": null,\n      \"authorizedDate\": \"2019-01-23T16:40:27.0000000+00:00\",\n      \"callCenterOperatorName\": null,\n      \"totalItems\": 1,\n      \"currencyCode\": \"BRL\"\n    },\n    {\n      \"orderId\": \"v502547llux-01\",\n      \"creationDate\": \"2019-01-23T16:34:20.0000000+00:00\",\n      \"clientName\": \"test test\",\n      \"items\": null,\n      \"totalValue\": 10150,\n      \"paymentNames\": \"Mastercard\",\n      \"status\": \"ready-for-handling\",\n      \"statusDescription\": \"Pronto para o manuseio\",\n      \"marketPlaceOrderId\": null,\n      \"sequence\": \"502548\",\n      \"salesChannel\": \"1\",\n      \"affiliateId\": \"\",\n      \"origin\": \"Marketplace\",\n      \"workflowInErrorState\": false,\n      \"workflowInRetry\": false,\n      \"lastMessageUnread\": \" Lux Store 96 Seu pagamento foi aprovado. Referente ao Pedido #v502547llux-01 Olá, test. Estamos providenciando a emissão da Nota Fisc\",\n      \"ShippingEstimatedDate\": \"2019-01-30T16:35:30.0000000+00:00\",\n      \"ShippingEstimatedDateMax\": null,\n      \"ShippingEstimatedDateMin\": null,\n      \"orderIsComplete\": true,\n      \"listId\": null,\n      \"listType\": null,\n      \"authorizedDate\": \"2019-01-23T16:35:04.0000000+00:00\",\n      \"callCenterOperatorName\": null,\n      \"totalItems\": 1,\n      \"currencyCode\": \"BRL\"\n    },\n    {\n      \"orderId\": \"v502544llux-01\",\n      \"creationDate\": \"2018-12-28T18:15:28.0000000+00:00\",\n      \"clientName\": \"test test\",\n      \"items\": null,\n      \"totalValue\": 8990,\n      \"paymentNames\": \"Boleto Bancário\",\n      \"status\": \"canceled\",\n      \"statusDescription\": \"Cancelado\",\n      \"marketPlaceOrderId\": null,\n      \"sequence\": \"502544\",\n      \"salesChannel\": \"1\",\n      \"affiliateId\": \"\",\n      \"origin\": \"Marketplace\",\n      \"workflowInErrorState\": false,\n      \"workflowInRetry\": false,\n      \"lastMessageUnread\": \" Lux Store 96 Seu pedido foi cancelado. Referente ao Pedido #v502544llux-01 Resumo Itens R$ 89,90 Total R$ 89,90 Produto Alavanca De M\",\n      \"ShippingEstimatedDate\": null,\n      \"ShippingEstimatedDateMax\": null,\n      \"ShippingEstimatedDateMin\": null,\n      \"orderIsComplete\": true,\n      \"listId\": null,\n      \"listType\": null,\n      \"authorizedDate\": null,\n      \"callCenterOperatorName\": null,\n      \"totalItems\": 1,\n      \"currencyCode\": \"BRL\"\n    },\n    {\n      \"orderId\": \"v502541llux-01\",\n      \"creationDate\": \"2018-12-18T18:48:17.0000000+00:00\",\n      \"clientName\": \"Douglas Rodrigues\",\n      \"items\": null,\n      \"totalValue\": 3290,\n      \"paymentNames\": \"Boleto Bancário\",\n      \"status\": \"canceled\",\n      \"statusDescription\": \"Cancelado\",\n      \"marketPlaceOrderId\": null,\n      \"sequence\": \"502541\",\n      \"salesChannel\": \"1\",\n      \"affiliateId\": \"\",\n      \"origin\": \"Marketplace\",\n      \"workflowInErrorState\": false,\n      \"workflowInRetry\": false,\n      \"lastMessageUnread\": \" Lux Store 96 Seu pedido foi cancelado. Referente ao Pedido #v502541llux-01 Resumo Itens R$ 32,90 Total R$ 32,90 Produto Bay Max L 1 u\",\n      \"ShippingEstimatedDate\": null,\n      \"ShippingEstimatedDateMax\": null,\n      \"ShippingEstimatedDateMin\": null,\n      \"orderIsComplete\": true,\n      \"listId\": null,\n      \"listType\": null,\n      \"authorizedDate\": null,\n      \"callCenterOperatorName\": null,\n      \"totalItems\": 1,\n      \"currencyCode\": \"BRL\"\n    },\n    {\n      \"orderId\": \"v502538llux-01\",\n      \"creationDate\": \"2018-12-12T18:21:47.0000000+00:00\",\n      \"clientName\": \"test test\",\n      \"items\": null,\n      \"totalValue\": 8990,\n      \"paymentNames\": \"Mastercard\",\n      \"status\": \"ready-for-handling\",\n      \"statusDescription\": \"Pronto para o manuseio\",\n      \"marketPlaceOrderId\": null,\n      \"sequence\": \"502538\",\n      \"salesChannel\": \"1\",\n      \"affiliateId\": \"\",\n      \"origin\": \"Marketplace\",\n      \"workflowInErrorState\": false,\n      \"workflowInRetry\": false,\n      \"lastMessageUnread\": \" Lux Store 96 Seu pagamento foi aprovado. Referente ao Pedido #v502538llux-01 Olá, test. Estamos providenciando a emissão da Nota Fisc\",\n      \"ShippingEstimatedDate\": \"2018-12-19T18:22:26.0000000+00:00\",\n      \"ShippingEstimatedDateMax\": null,\n      \"ShippingEstimatedDateMin\": null,\n      \"orderIsComplete\": true,\n      \"listId\": null,\n      \"listType\": null,\n      \"authorizedDate\": \"2018-12-12T18:22:22.0000000+00:00\",\n      \"callCenterOperatorName\": null,\n      \"totalItems\": 1,\n      \"currencyCode\": \"BRL\"\n    },\n    {\n      \"orderId\": \"SCP-880102018018-01\",\n      \"creationDate\": \"2018-11-30T17:34:01.0000000+00:00\",\n      \"clientName\": \"roberta grecco\",\n      \"items\": null,\n      \"totalValue\": 1250,\n      \"paymentNames\": \"\",\n      \"status\": \"canceled\",\n      \"statusDescription\": \"Cancelado\",\n      \"marketPlaceOrderId\": \"880102018018-01\",\n      \"sequence\": \"502537\",\n      \"salesChannel\": \"1\",\n      \"affiliateId\": \"SCP\",\n      \"origin\": \"Fulfillment\",\n      \"workflowInErrorState\": false,\n      \"workflowInRetry\": false,\n      \"lastMessageUnread\": \"cancelamento teste shp \",\n      \"ShippingEstimatedDate\": null,\n      \"ShippingEstimatedDateMax\": null,\n      \"ShippingEstimatedDateMin\": null,\n      \"orderIsComplete\": true,\n      \"listId\": null,\n      \"listType\": null,\n      \"authorizedDate\": \"2018-11-30T17:34:42.0000000+00:00\",\n      \"callCenterOperatorName\": null,\n      \"totalItems\": 1,\n      \"currencyCode\": \"BRL\"\n    },\n    {\n      \"orderId\": \"SCP-880091692043-01\",\n      \"creationDate\": \"2018-11-30T17:28:35.0000000+00:00\",\n      \"clientName\": \"roberta grecco\",\n      \"items\": null,\n      \"totalValue\": 1250,\n      \"paymentNames\": \"\",\n      \"status\": \"invoiced\",\n      \"statusDescription\": \"Faturado\",\n      \"marketPlaceOrderId\": \"880091692043-01\",\n      \"sequence\": \"502536\",\n      \"salesChannel\": \"1\",\n      \"affiliateId\": \"SCP\",\n      \"origin\": \"Fulfillment\",\n      \"workflowInErrorState\": false,\n      \"workflowInRetry\": false,\n      \"lastMessageUnread\": null,\n      \"ShippingEstimatedDate\": null,\n      \"ShippingEstimatedDateMax\": null,\n      \"ShippingEstimatedDateMin\": null,\n      \"orderIsComplete\": true,\n      \"listId\": null,\n      \"listType\": null,\n      \"authorizedDate\": \"2018-11-30T17:29:22.0000000+00:00\",\n      \"callCenterOperatorName\": null,\n      \"totalItems\": 1,\n      \"currencyCode\": \"BRL\"\n    },\n    {\n      \"orderId\": \"SCP-880091058221-01\",\n      \"creationDate\": \"2018-11-30T17:18:00.0000000+00:00\",\n      \"clientName\": \"roberta grecco\",\n      \"items\": null,\n      \"totalValue\": 1250,\n      \"paymentNames\": \"\",\n      \"status\": \"canceled\",\n      \"statusDescription\": \"Cancelado\",\n      \"marketPlaceOrderId\": \"880091058221-01\",\n      \"sequence\": \"502535\",\n      \"salesChannel\": \"1\",\n      \"affiliateId\": \"SCP\",\n      \"origin\": \"Fulfillment\",\n      \"workflowInErrorState\": false,\n      \"workflowInRetry\": false,\n      \"lastMessageUnread\": \"Teste de cancelamento do ShopFácil \",\n      \"ShippingEstimatedDate\": null,\n      \"ShippingEstimatedDateMax\": null,\n      \"ShippingEstimatedDateMin\": null,\n      \"orderIsComplete\": true,\n      \"listId\": null,\n      \"listType\": null,\n      \"authorizedDate\": \"2018-11-30T17:18:44.0000000+00:00\",\n      \"callCenterOperatorName\": null,\n      \"totalItems\": 1,\n      \"currencyCode\": \"BRL\"\n    },\n    {\n      \"orderId\": \"SCP-880090643370-01\",\n      \"creationDate\": \"2018-11-30T17:10:59.0000000+00:00\",\n      \"clientName\": \"roberta grecco\",\n      \"items\": null,\n      \"totalValue\": 1250,\n      \"paymentNames\": \"\",\n      \"status\": \"ready-for-handling\",\n      \"statusDescription\": \"Pronto para o manuseio\",\n      \"marketPlaceOrderId\": \"880090643370-01\",\n      \"sequence\": \"502534\",\n      \"salesChannel\": \"1\",\n      \"affiliateId\": \"SCP\",\n      \"origin\": \"Fulfillment\",\n      \"workflowInErrorState\": false,\n      \"workflowInRetry\": false,\n      \"lastMessageUnread\": null,\n      \"ShippingEstimatedDate\": \"2018-12-07T17:11:39.0000000+00:00\",\n      \"ShippingEstimatedDateMax\": null,\n      \"ShippingEstimatedDateMin\": null,\n      \"orderIsComplete\": true,\n      \"listId\": null,\n      \"listType\": null,\n      \"authorizedDate\": \"2018-11-30T17:11:42.0000000+00:00\",\n      \"callCenterOperatorName\": null,\n      \"totalItems\": 1,\n      \"currencyCode\": \"BRL\"\n    },\n    {\n      \"orderId\": \"SCP-880090622238-01\",\n      \"creationDate\": \"2018-11-30T17:10:45.0000000+00:00\",\n      \"clientName\": \"roberta grecco\",\n      \"items\": null,\n      \"totalValue\": 1250,\n      \"paymentNames\": \"\",\n      \"status\": \"canceled\",\n      \"statusDescription\": \"Cancelado\",\n      \"marketPlaceOrderId\": \"880090622238-01\",\n      \"sequence\": \"502533\",\n      \"salesChannel\": \"1\",\n      \"affiliateId\": \"SCP\",\n      \"origin\": \"Fulfillment\",\n      \"workflowInErrorState\": false,\n      \"workflowInRetry\": false,\n      \"lastMessageUnread\": null,\n      \"ShippingEstimatedDate\": null,\n      \"ShippingEstimatedDateMax\": null,\n      \"ShippingEstimatedDateMin\": null,\n      \"orderIsComplete\": true,\n      \"listId\": null,\n      \"listType\": null,\n      \"authorizedDate\": null,\n      \"callCenterOperatorName\": null,\n      \"totalItems\": 1,\n      \"currencyCode\": \"BRL\"\n    },\n    {\n      \"orderId\": \"MNC-877730530419-01\",\n      \"creationDate\": \"2018-11-20T21:09:01.0000000+00:00\",\n      \"clientName\": \"Carlos VTEX\",\n      \"items\": null,\n      \"totalValue\": 11150,\n      \"paymentNames\": \"\",\n      \"status\": \"canceled\",\n      \"statusDescription\": \"Cancelado\",\n      \"marketPlaceOrderId\": \"877730530419-01\",\n      \"sequence\": \"502532\",\n      \"salesChannel\": \"1\",\n      \"affiliateId\": \"MNC\",\n      \"origin\": \"Fulfillment\",\n      \"workflowInErrorState\": false,\n      \"workflowInRetry\": false,\n      \"lastMessageUnread\": null,\n      \"ShippingEstimatedDate\": null,\n      \"ShippingEstimatedDateMax\": null,\n      \"ShippingEstimatedDateMin\": null,\n      \"orderIsComplete\": true,\n      \"listId\": null,\n      \"listType\": null,\n      \"authorizedDate\": \"2018-11-20T21:13:06.0000000+00:00\",\n      \"callCenterOperatorName\": null,\n      \"totalItems\": 1,\n      \"currencyCode\": \"BRL\"\n    },\n    {\n      \"orderId\": \"SCP-876733475998-01\",\n      \"creationDate\": \"2018-11-16T16:58:18.0000000+00:00\",\n      \"clientName\": \"roberta grecco\",\n      \"items\": null,\n      \"totalValue\": 1250,\n      \"paymentNames\": \"\",\n      \"status\": \"ready-for-handling\",\n      \"statusDescription\": \"Pronto para o manuseio\",\n      \"marketPlaceOrderId\": \"876733475998-01\",\n      \"sequence\": \"502531\",\n      \"salesChannel\": \"1\",\n      \"affiliateId\": \"SCP\",\n      \"origin\": \"Fulfillment\",\n      \"workflowInErrorState\": false,\n      \"workflowInRetry\": false,\n      \"lastMessageUnread\": null,\n      \"ShippingEstimatedDate\": \"2018-11-23T16:58:48.0000000+00:00\",\n      \"ShippingEstimatedDateMax\": null,\n      \"ShippingEstimatedDateMin\": null,\n      \"orderIsComplete\": true,\n      \"listId\": null,\n      \"listType\": null,\n      \"authorizedDate\": \"2018-11-16T16:58:53.0000000+00:00\",\n      \"callCenterOperatorName\": null,\n      \"totalItems\": 1,\n      \"currencyCode\": \"BRL\"\n    }\n  ],\n  \"facets\": [],\n  \"paging\": {\n    \"total\": 84,\n    \"pages\": 6,\n    \"currentPage\": 1,\n    \"perPage\": 15\n  },\n  \"stats\": {\n    \"stats\": {\n      \"totalValue\": {\n        \"Count\": 84,\n        \"Max\": 21526180,\n        \"Mean\": 262672.75,\n        \"Min\": 1160,\n        \"Missing\": 0,\n        \"StdDev\": 2348087.3869179883,\n        \"Sum\": 22064511,\n        \"SumOfSquares\": 463417439039853,\n        \"Facets\": {\n          \"origin\": {\n            \"Fulfillment\": {\n              \"Count\": 68,\n              \"Max\": 11150,\n              \"Mean\": 1395.5882352941176,\n              \"Min\": 1250,\n              \"Missing\": 0,\n              \"StdDev\": 1200.5513439298484,\n              \"Sum\": 94900,\n              \"SumOfSquares\": 229010000,\n              \"Facets\": null\n            },\n            \"Marketplace\": {\n              \"Count\": 16,\n              \"Max\": 21526180,\n              \"Mean\": 1373100.6875,\n              \"Min\": 1160,\n              \"Missing\": 0,\n              \"StdDev\": 5374326.141087491,\n              \"Sum\": 21969611,\n              \"SumOfSquares\": 463417210029853,\n              \"Facets\": null\n            }\n          },\n          \"currencyCode\": {\n            \"BRL\": {\n              \"Count\": 84,\n              \"Max\": 21526180,\n              \"Mean\": 262672.75,\n              \"Min\": 1160,\n              \"Missing\": 0,\n              \"StdDev\": 2348087.3869179883,\n              \"Sum\": 22064511,\n              \"SumOfSquares\": 463417439039853,\n              \"Facets\": null\n            }\n          }\n        }\n      },\n      \"totalItems\": {\n        \"Count\": 84,\n        \"Max\": 89,\n        \"Mean\": 2.2261904761904763,\n        \"Min\": 1,\n        \"Missing\": 0,\n        \"StdDev\": 9.660940100525016,\n        \"Sum\": 187,\n        \"SumOfSquares\": 8163,\n        \"Facets\": {\n          \"origin\": {\n            \"Fulfillment\": {\n              \"Count\": 68,\n              \"Max\": 1,\n              \"Mean\": 1,\n              \"Min\": 1,\n              \"Missing\": 0,\n              \"StdDev\": 0,\n              \"Sum\": 68,\n              \"SumOfSquares\": 68,\n              \"Facets\": null\n            },\n            \"Marketplace\": {\n              \"Count\": 16,\n              \"Max\": 89,\n              \"Mean\": 7.4375,\n              \"Min\": 1,\n              \"Missing\": 0,\n              \"StdDev\": 21.92401651157926,\n              \"Sum\": 119,\n              \"SumOfSquares\": 8095,\n              \"Facets\": null\n            }\n          },\n          \"currencyCode\": {\n            \"BRL\": {\n              \"Count\": 84,\n              \"Max\": 89,\n              \"Mean\": 2.2261904761904763,\n              \"Min\": 1,\n              \"Missing\": 0,\n              \"StdDev\": 9.660940100525016,\n              \"Sum\": 187,\n              \"SumOfSquares\": 8163,\n              \"Facets\": null\n            }\n          }\n        }\n      }\n    }\n  }\n}",
      "language": "text",
      "name": "200 - OK"
    }
  ]
}
[/block]
