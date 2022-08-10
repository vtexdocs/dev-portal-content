---
title: "Retrieve User's orders"
slug: "userorderslist"
excerpt: "Lists all orders from a given client, filtering by their email."
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2020-04-20T14:22:04.494Z"
---
[block:api-header]
{
  "title": "Request object has the following properties:"
}
[/block]
| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `email` | string | Client e-mail |
| `pageNumber` | string | Page number for result pagination |
| `pageSize` | string | Page quantity for result pagination |



[block:api-header]
{
  "title": "Response object has the following properties:"
}
[/block]
| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `list` | object | Order List Object|
| `orderId` | string |  Order ID |
| `creationDate` | string | Order Creation Date |
| `clientName` | string | Order Client Name|
| `items` | object | Obsolete Field  |
| `totalValue` | integer | Total Value Amount |
| `paymentNames` | string | Payment System Name |
| `status` | string | Order Status |
| `statusDescription` | string | Status Description |
| `marketplaceOrderId` | string | Marketplace Order Id |
| `sequence` | string | Order Sequence ID |
| `salesChannel` | string | Order Sales Channel Id |
| `affiliateId` | string | Seller Name who was responsible for the order |
| `origin` | string | Order Origin: "Marketplace" or "Fulfillment" |
| `workflowInErrorState` | boolean | If is a Work Flow Error |
| `workflowInRetry` | boolean | If is in a Work Flow Retry |
| `lastMessageUnread` | string | Last sent transactional message  |
| `shippingEstimateDate` | string | Estimate Shipping Date |
| `ShippingEstimatedDateMax` | string | ??? |
| `ShippingEstimatedDateMin` | string | ??? |
| `orderIsComplete` | boolean | If is a Order Completed |
| `listId` | string | Releated Gift List Id |
| `listType` | string | Releated Gift List Type |
| `authorizedDate` | string | Authorized Order Date |
| `callCenterOperatorData` | string | Call Center Operator responsible for the order |
| `totalItems` | integer | Total Order Items |
| `currencyCode` | string | Currency Code in ISO 4217  |

[block:api-header]
{
  "title": "Request body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET 'https://{{accountName}}.{{environment}}.com.br/api/oms/user/orders/?clientEmail={{email}}&page={{pageNumber}}&per_page={{pageSize}}' \\\n--header 'Accept: application/json'",
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
      "code": "{\n  \"list\": [\n    {\n      \"orderId\": \"v502556llux-01\",\n      \"creationDate\": \"2019-01-28T20:09:43.0000000+00:00\",\n      \"clientName\": \"Cunha VTEX\",\n      \"items\": null,\n      \"totalValue\": 1160,\n      \"paymentNames\": \"Boleto Bancário\",\n      \"status\": \"handling\",\n      \"statusDescription\": \"Preparando Entrega\",\n      \"marketPlaceOrderId\": null,\n      \"sequence\": \"502556\",\n      \"salesChannel\": \"1\",\n      \"affiliateId\": \"\",\n      \"origin\": \"Marketplace\",\n      \"workflowInErrorState\": false,\n      \"workflowInRetry\": false,\n      \"lastMessageUnread\": \" Lux Store Seu pedido foi alterado! Pedido realizado em: 28/01/2019 Olá, Rodrigo. Seu pedido foi alterado. Seguem informações abaixo: \",\n      \"ShippingEstimatedDate\": \"2019-02-04T20:33:46.0000000+00:00\",\n      \"ShippingEstimatedDateMax\": null,\n      \"ShippingEstimatedDateMin\": null,\n      \"orderIsComplete\": true,\n      \"listId\": null,\n      \"listType\": null,\n      \"authorizedDate\": \"2019-01-28T20:33:04.0000000+00:00\",\n      \"callCenterOperatorName\": null,\n      \"totalItems\": 1,\n      \"currencyCode\": \"BRL\"\n    },\n    {\n      \"orderId\": \"v502449llux-02\",\n      \"creationDate\": \"2018-08-28T17:42:40.0000000+00:00\",\n      \"clientName\": \"Cunha VTEX\",\n      \"items\": null,\n      \"totalValue\": 118588,\n      \"paymentNames\": \"Promissory\",\n      \"status\": \"canceled\",\n      \"statusDescription\": \"Cancelado\",\n      \"marketPlaceOrderId\": null,\n      \"sequence\": \"502452\",\n      \"salesChannel\": \"1\",\n      \"affiliateId\": \"\",\n      \"origin\": \"Marketplace\",\n      \"workflowInErrorState\": false,\n      \"workflowInRetry\": false,\n      \"lastMessageUnread\": \" Lux Store 96 Seu pedido foi cancelado. Referente ao Pedido #v502449llux-02 Resumo Itens R$ 1.178,98 Entrega R$ 6,90 Total R$ 1.185,88\",\n      \"ShippingEstimatedDate\": null,\n      \"ShippingEstimatedDateMax\": null,\n      \"ShippingEstimatedDateMin\": null,\n      \"orderIsComplete\": true,\n      \"listId\": null,\n      \"listType\": null,\n      \"authorizedDate\": null,\n      \"callCenterOperatorName\": null,\n      \"totalItems\": 12,\n      \"currencyCode\": \"BRL\"\n    },\n    {\n      \"orderId\": \"v502449llux-01\",\n      \"creationDate\": \"2018-08-28T17:42:28.9171556+00:00\",\n      \"clientName\": \"Cunha VTEX\",\n      \"items\": [\n        {\n          \"seller\": \"1\",\n          \"quantity\": 1,\n          \"description\": \"Mangueira Reservatório Ao Cavalete\",\n          \"ean\": null,\n          \"refId\": \"TE3121110\",\n          \"id\": \"195\",\n          \"productId\": \"134\",\n          \"sellingPrice\": 7390,\n          \"price\": 7390\n        },\n        {\n          \"seller\": \"1\",\n          \"quantity\": 1,\n          \"description\": \"Mangueira Filtro\",\n          \"ean\": null,\n          \"refId\": \"XC459N610CA\",\n          \"id\": \"238\",\n          \"productId\": \"162\",\n          \"sellingPrice\": 5190,\n          \"price\": 5190\n        }\n      ],\n      \"totalValue\": 21526180,\n      \"paymentNames\": null,\n      \"status\": \"canceled\",\n      \"statusDescription\": \"Cancelado\",\n      \"marketPlaceOrderId\": \"\",\n      \"sequence\": \"502449\",\n      \"salesChannel\": \"1\",\n      \"affiliateId\": \"\",\n      \"origin\": \"Marketplace\",\n      \"workflowInErrorState\": false,\n      \"workflowInRetry\": false,\n      \"lastMessageUnread\": null,\n      \"ShippingEstimatedDate\": null,\n      \"ShippingEstimatedDateMax\": null,\n      \"ShippingEstimatedDateMin\": null,\n      \"orderIsComplete\": true,\n      \"listId\": null,\n      \"listType\": null,\n      \"authorizedDate\": null,\n      \"callCenterOperatorName\": null,\n      \"totalItems\": 0,\n      \"currencyCode\": null\n    },\n    {\n      \"orderId\": \"v502058llux-01\",\n      \"creationDate\": \"2017-07-25T23:17:36.7963248+00:00\",\n      \"clientName\": \"Cunha VTEX\",\n      \"items\": [\n        {\n          \"seller\": \"1\",\n          \"quantity\": 1,\n          \"description\": \"Aquecedor Britania 1500 Branco\",\n          \"ean\": \"1235567890143\",\n          \"refId\": \"branquinho\",\n          \"id\": \"1234568212\",\n          \"productId\": \"1000200\",\n          \"sellingPrice\": 35599,\n          \"price\": 35599\n        }\n      ],\n      \"totalValue\": 35599,\n      \"paymentNames\": null,\n      \"status\": \"invoiced\",\n      \"statusDescription\": \"Faturado\",\n      \"marketPlaceOrderId\": \"\",\n      \"sequence\": \"502058\",\n      \"salesChannel\": \"1\",\n      \"affiliateId\": \"\",\n      \"origin\": \"Marketplace\",\n      \"workflowInErrorState\": false,\n      \"workflowInRetry\": false,\n      \"lastMessageUnread\": null,\n      \"ShippingEstimatedDate\": \"2017-07-29T19:24:20.7444363+00:00\",\n      \"ShippingEstimatedDateMax\": null,\n      \"ShippingEstimatedDateMin\": null,\n      \"orderIsComplete\": true,\n      \"listId\": null,\n      \"listType\": null,\n      \"authorizedDate\": null,\n      \"callCenterOperatorName\": null,\n      \"totalItems\": 0,\n      \"currencyCode\": null\n    },\n    {\n      \"orderId\": \"v501538llux-01\",\n      \"creationDate\": \"2017-06-26T16:57:58.9986524+00:00\",\n      \"clientName\": \"Cunha VTEX\",\n      \"items\": [\n        {\n          \"seller\": \"1\",\n          \"quantity\": 1,\n          \"description\": \"Boneco do Mário\",\n          \"ean\": \"bonecomario\",\n          \"refId\": \"bonecomario\",\n          \"id\": \"1234568183\",\n          \"productId\": \"1000257\",\n          \"sellingPrice\": 150363,\n          \"price\": 150363\n        },\n        {\n          \"seller\": \"1\",\n          \"quantity\": 1,\n          \"description\": \"Camiseta GG\",\n          \"ean\": null,\n          \"refId\": \"abc1234\",\n          \"id\": \"1234567894\",\n          \"productId\": \"1000187\",\n          \"sellingPrice\": 899,\n          \"price\": 899\n        }\n      ],\n      \"totalValue\": 151262,\n      \"paymentNames\": null,\n      \"status\": \"invoiced\",\n      \"statusDescription\": \"Faturado\",\n      \"marketPlaceOrderId\": \"\",\n      \"sequence\": \"501538\",\n      \"salesChannel\": \"1\",\n      \"affiliateId\": \"\",\n      \"origin\": \"Marketplace\",\n      \"workflowInErrorState\": false,\n      \"workflowInRetry\": false,\n      \"lastMessageUnread\": null,\n      \"ShippingEstimatedDate\": \"2017-06-27T13:59:49.7705236+00:00\",\n      \"ShippingEstimatedDateMax\": null,\n      \"ShippingEstimatedDateMin\": null,\n      \"orderIsComplete\": true,\n      \"listId\": null,\n      \"listType\": null,\n      \"authorizedDate\": null,\n      \"callCenterOperatorName\": null,\n      \"totalItems\": 0,\n      \"currencyCode\": null\n    },\n    {\n      \"orderId\": \"v501020llux-01\",\n      \"creationDate\": \"2016-11-21T19:57:54.0415289+00:00\",\n      \"clientName\": \"Cunha VTEX\",\n      \"items\": [\n        {\n          \"seller\": \"1\",\n          \"quantity\": 2,\n          \"description\": \"Camiseta GG\",\n          \"ean\": null,\n          \"refId\": \"abc1234\",\n          \"id\": \"1234567894\",\n          \"productId\": \"1000187\",\n          \"sellingPrice\": 899,\n          \"price\": 899\n        }\n      ],\n      \"totalValue\": 3190,\n      \"paymentNames\": null,\n      \"status\": \"canceled\",\n      \"statusDescription\": \"Cancelado\",\n      \"marketPlaceOrderId\": \"\",\n      \"sequence\": \"501020\",\n      \"salesChannel\": \"1\",\n      \"affiliateId\": \"\",\n      \"origin\": \"Marketplace\",\n      \"workflowInErrorState\": false,\n      \"workflowInRetry\": false,\n      \"lastMessageUnread\": null,\n      \"ShippingEstimatedDate\": \"2016-12-02T08:00:00.0000000+00:00\",\n      \"ShippingEstimatedDateMax\": null,\n      \"ShippingEstimatedDateMin\": null,\n      \"orderIsComplete\": true,\n      \"listId\": null,\n      \"listType\": null,\n      \"authorizedDate\": null,\n      \"callCenterOperatorName\": null,\n      \"totalItems\": 0,\n      \"currencyCode\": null\n    },\n    {\n      \"orderId\": \"v500973llux-01\",\n      \"creationDate\": \"2016-10-10T17:19:30.8562035+00:00\",\n      \"clientName\": \"Cunha VTEX\",\n      \"items\": [\n        {\n          \"seller\": \"1\",\n          \"quantity\": 1,\n          \"description\": \"SMARTPHONE SAMSUNG GALAXY S7 FLAT SM-G930FZDLZTO 32GB DOURADO TELA 5.1\\\" 4G CÂMERA 12 MP\",\n          \"ean\": null,\n          \"refId\": \"testefnac\",\n          \"id\": \"1234568028\",\n          \"productId\": \"1000203\",\n          \"sellingPrice\": 299000,\n          \"price\": 299000\n        }\n      ],\n      \"totalValue\": 299900,\n      \"paymentNames\": null,\n      \"status\": \"handling\",\n      \"statusDescription\": \"Preparando Entrega\",\n      \"marketPlaceOrderId\": \"\",\n      \"sequence\": \"500973\",\n      \"salesChannel\": \"1\",\n      \"affiliateId\": \"\",\n      \"origin\": \"Marketplace\",\n      \"workflowInErrorState\": false,\n      \"workflowInRetry\": false,\n      \"lastMessageUnread\": null,\n      \"ShippingEstimatedDate\": \"2016-10-10T14:23:17.1897068+00:00\",\n      \"ShippingEstimatedDateMax\": null,\n      \"ShippingEstimatedDateMin\": null,\n      \"orderIsComplete\": true,\n      \"listId\": null,\n      \"listType\": null,\n      \"authorizedDate\": null,\n      \"callCenterOperatorName\": null,\n      \"totalItems\": 0,\n      \"currencyCode\": null\n    },\n    {\n      \"orderId\": \"v500970llux-01\",\n      \"creationDate\": \"2016-10-10T17:07:59.0889392+00:00\",\n      \"clientName\": \"Cunha VTEX\",\n      \"items\": [\n        {\n          \"seller\": \"1\",\n          \"quantity\": 1,\n          \"description\": \"Camiseta GG\",\n          \"ean\": null,\n          \"refId\": \"abc1234\",\n          \"id\": \"1234567894\",\n          \"productId\": \"1000187\",\n          \"sellingPrice\": 899,\n          \"price\": 899\n        }\n      ],\n      \"totalValue\": 1799,\n      \"paymentNames\": null,\n      \"status\": \"invoiced\",\n      \"statusDescription\": \"Faturado\",\n      \"marketPlaceOrderId\": \"\",\n      \"sequence\": \"500970\",\n      \"salesChannel\": \"1\",\n      \"affiliateId\": \"\",\n      \"origin\": \"Marketplace\",\n      \"workflowInErrorState\": false,\n      \"workflowInRetry\": false,\n      \"lastMessageUnread\": null,\n      \"ShippingEstimatedDate\": \"2016-10-10T14:13:34.4927265+00:00\",\n      \"ShippingEstimatedDateMax\": null,\n      \"ShippingEstimatedDateMin\": null,\n      \"orderIsComplete\": true,\n      \"listId\": null,\n      \"listType\": null,\n      \"authorizedDate\": null,\n      \"callCenterOperatorName\": null,\n      \"totalItems\": 0,\n      \"currencyCode\": null\n    },\n    {\n      \"orderId\": \"v500890llux-01\",\n      \"creationDate\": \"2016-08-17T18:35:04.8659804+00:00\",\n      \"clientName\": \"Cunha VTEX\",\n      \"items\": [\n        {\n          \"seller\": \"1\",\n          \"quantity\": 1,\n          \"description\": \"Botin Futbol Adidas 11Questra Fg Cesped Hombre Absolut - M\",\n          \"ean\": \"absolutm\",\n          \"refId\": null,\n          \"id\": \"549\",\n          \"productId\": \"9\",\n          \"sellingPrice\": 1000,\n          \"price\": 1000\n        }\n      ],\n      \"totalValue\": 1000,\n      \"paymentNames\": null,\n      \"status\": \"canceled\",\n      \"statusDescription\": \"Cancelado\",\n      \"marketPlaceOrderId\": \"\",\n      \"sequence\": \"500890\",\n      \"salesChannel\": \"1\",\n      \"affiliateId\": \"\",\n      \"origin\": \"Marketplace\",\n      \"workflowInErrorState\": false,\n      \"workflowInRetry\": false,\n      \"lastMessageUnread\": null,\n      \"ShippingEstimatedDate\": null,\n      \"ShippingEstimatedDateMax\": null,\n      \"ShippingEstimatedDateMin\": null,\n      \"orderIsComplete\": true,\n      \"listId\": null,\n      \"listType\": null,\n      \"authorizedDate\": null,\n      \"callCenterOperatorName\": null,\n      \"totalItems\": 0,\n      \"currencyCode\": null\n    },\n    {\n      \"orderId\": \"v500838llux-01\",\n      \"creationDate\": \"2016-07-29T00:20:47.7736718+00:00\",\n      \"clientName\": \"Cunha VTEX\",\n      \"items\": [\n        {\n          \"seller\": \"1\",\n          \"quantity\": 1,\n          \"description\": \"Rooibos Lavanda - Pouch - 50gr\",\n          \"ean\": \"198\",\n          \"refId\": \"10098\",\n          \"id\": \"98\",\n          \"productId\": \"1000025\",\n          \"sellingPrice\": 5200,\n          \"price\": 5200\n        }\n      ],\n      \"totalValue\": 6200,\n      \"paymentNames\": null,\n      \"status\": \"canceled\",\n      \"statusDescription\": \"Cancelado\",\n      \"marketPlaceOrderId\": \"\",\n      \"sequence\": \"500838\",\n      \"salesChannel\": \"1\",\n      \"affiliateId\": \"\",\n      \"origin\": \"Marketplace\",\n      \"workflowInErrorState\": false,\n      \"workflowInRetry\": false,\n      \"lastMessageUnread\": null,\n      \"ShippingEstimatedDate\": null,\n      \"ShippingEstimatedDateMax\": null,\n      \"ShippingEstimatedDateMin\": null,\n      \"orderIsComplete\": true,\n      \"listId\": null,\n      \"listType\": null,\n      \"authorizedDate\": null,\n      \"callCenterOperatorName\": null,\n      \"totalItems\": 0,\n      \"currencyCode\": null\n    }\n  ],\n  \"facets\": [],\n  \"paging\": {\n    \"total\": 19,\n    \"pages\": 10,\n    \"currentPage\": 1,\n    \"perPage\": 2\n  },\n  \"stats\": {\n    \"stats\": {\n      \"totalValue\": {\n        \"Count\": 19,\n        \"Max\": 0,\n        \"Mean\": 0,\n        \"Min\": 0,\n        \"Missing\": 0,\n        \"StdDev\": 0,\n        \"Sum\": 0,\n        \"SumOfSquares\": 0,\n        \"Facets\": {}\n      },\n      \"totalItems\": {\n        \"Count\": 19,\n        \"Max\": 0,\n        \"Mean\": 0,\n        \"Min\": 0,\n        \"Missing\": 0,\n        \"StdDev\": 0,\n        \"Sum\": 0,\n        \"SumOfSquares\": 0,\n        \"Facets\": {}\n      }\n    }\n  }\n}",
      "language": "text"
    }
  ]
}
[/block]