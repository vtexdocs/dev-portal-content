---
title: "List orders"
slug: "listorderspiicompliant"
excerpt: "Retrieve a list of orders according to the filters described below.\n\r\n\r> This endpoint returns masked order data.\n\r\n\r> This should **not** be used for integrations. Use the [orders Feed or hook](https://developers.vtex.com/vtex-rest-api/docs/feed-v3-1) for this purpose.\n\r\n\rThis endpoint returns only orders that already have been indexed, which takes aproximately four minutes. Because of this, the data retrieved may present inconsistencies. To get live up to date information and [build order integrations](https://developers.vtex.com/docs/guides/erp-integration-set-up-order-integration ) use the [orders Feed or hook](https://developers.vtex.com/vtex-rest-api/docs/feed-v3-1)."
hidden: true
createdAt: "2022-04-26T15:47:38.589Z"
updatedAt: "2022-04-29T19:41:50.360Z"
---
## Throtling

<div class="alert alert-info">Throttling: Each account can make up to 5000 requests per minute.</div>

## Request parameters

| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `orderBy` | string | Order Field and Order Type concatenated `orderBy={{OrderField}},{{OrderType}}`  |
| `OrderField` | string | Order Field expected values: `creationDate`,`orderId`,`items`,`totalValue` and `origin` |
| `OrderType` | string | Order Type expected values: `asc` and `desc`  |

Sorting Examples

CreationDate:

 `/api/oms/pvt/orders?orderBy=creationDate,desc`

OrderID:

 `/api/oms/pvt/orders?orderBy=orderId,desc`

Items:

 `/api/oms/pvt/orders?orderBy=items,asc`

TotalValue:

 `/api/oms/pvt/orders?orderBy=totalValue,desc`

Origin:

 `/api/oms/pvt/orders?orderBy=origin,asc`

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `page` | integer | Page Number  |

Pagination Examples:

 /api/oms/pvt/orders?page=3

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `per_page` | integer | Quantity orders per page  |

Quantity per Page Examples:

 /api/oms/pvt/orders?per_page=15

<div class="alert alert-info">Pagination Limit: The limit of pages that can be requested is 30.</div>

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `utc` | integer | Time Zone  |

Time Zone Example:

 `/api/oms/pvt/orders?utc=-0200`

## Request filters

### Shipping Estimate

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `f_shippingEstimate` | string | Concatened value of quantity days and sufix `.days`  |

Shipping Estimate filter Examples:

Next 7 days:

 `/api/oms/pvt/orders?f_shippingEstimate=7.days`

Tomorrow:

 `/api/oms/pvt/orders?f_shippingEstimate=1.days`

Today:

 `/api/oms/pvt/orders?f_shippingEstimate=0.days`

Late:

 `/api/oms/pvt/orders?f_shippingEstimate=-1.days`

### Invoiced Date

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `f_invoicedDate` | string | Concatened value sufix `invoicedDate` and range date in Timestamp format  |

Invoiced Date filter Examples:

1 Day:

 `/api/oms/pvt/orders?f_invoicedDate=invoicedDate:[2017-01-01T02:00:00.000Z TO 2017-01-02T01:59:59.999Z]`

1 Month:

 `/api/oms/pvt/orders?f_invoicedDate=invoicedDate:[2017-01-01T02:00:00.000Z TO 2017-02-01T01:59:59.999Z]`

1 Year:

 `/api/oms/pvt/orders?f_invoicedDate=invoicedDate:[2016-01-01T02:00:00.000Z TO 2017-01-01T01:59:59.999Z]`

### Authorized Date

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `f_authorizedDate` | string | Concatened value sufix `authorizedDate` and range date in Timestamp format  |

Authorized Date filter Examples:

1 Day:

 `/api/oms/pvt/orders?f_authorizedDate=authorizedDate:[2017-01-01T02:00:00.000Z TO 2017-01-02T01:59:59.999Z]`

1 Month:

 `/api/oms/pvt/orders?f_authorizedDate=authorizedDate:[2017-01-01T02:00:00.000Z TO 2017-02-01T01:59:59.999Z]`

1 Year:

 `/api/oms/pvt/orders?f_authorizedDate=authorizedDate:[2016-01-01T02:00:00.000Z TO 2017-01-01T01:59:59.999Z]`

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

 `/api/oms/pvt/orders?f_callCenterOperatorName=Operator%20Name`

### Sales Channel Name

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `f_salesChannel` | string | Sales Channel Name Value  |

Sales Channel Name filter Examples:

 `/api/oms/pvt/orders?f_salesChannel=Main`

### Sales Channel ID

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `salesChannelId` | string | Sales Channel ID Value  |

Sales Channel ID filter Examples:

 `/api/oms/pvt/orders?salesChannelId=1`

### Affiliate ID

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `f_affiliateId` | string | Affiliate ID Value  |

Affiliate ID filter Examples:

 `/api/oms/pvt/orders?f_affiliateId=WLM`

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

 `/api/oms/pvt/orders?f_status=ready-for-handling`

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

 `/api/oms/pvt/orders?f_statusDescription=Pronto+para+o+manuseio`

### Order Situation

| Attribute    | Type      | Description |
| ------------ |:---------:| -----------:|
| `incompleteOrders` | boolean | If is a Incomplete Order  |

> know more about [Incomplete Orders in VTEX Help](https://help.vtex.com/en/tutorial/understanding-incomplete-orders)

Order Situation filter Examples:

 `/api/oms/pvt/orders?incompleteOrders=true`

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

 `/api/oms/pvt/orders?filterError=all`

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

>⚠️ As of October 3, 2018, this API will not return the **"items"** property.

## Response objects

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

## Request body example

```
curl --location --request GET 'https://luxstore.{{environment}}.com.br/api/oms/pvt/orders?_stats=1&f_creationDate=creationDate:%5B2018-08-08T03:00:00.000Z+TO+2019-02-09T01:59:59.999Z%5D&orderBy=creationDate,desc&page=1&utc=-0200' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \
--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'
```

## Response body example

```json
{
  "list": [
    {
      "orderId": "v502559llux-01",
      "creationDate": "2019-02-04T10:29:11.0000000+00:00",
      "clientName": "J C",
      "items": null,
      "totalValue": 7453,
      "paymentNames": "Boleto Bancário",
      "status": "invoiced",
      "statusDescription": "Faturado",
      "marketPlaceOrderId": null,
      "sequence": "502559",
      "salesChannel": "1",
      "affiliateId": "",
      "origin": "Marketplace",
      "workflowInErrorState": false,
      "workflowInRetry": false,
      "lastMessageUnread": " Lux Store 96 Sua Nota Fiscal foi emitida. Referente ao Pedido #v502559llux-01 Olá, J. Estamos empacotando seu produto para providenci",
      "ShippingEstimatedDate": null,
      "ShippingEstimatedDateMax": null,
      "ShippingEstimatedDateMin": null,
      "orderIsComplete": true,
      "listId": null,
      "listType": null,
      "authorizedDate": "2019-02-07T21:29:54.0000000+00:00",
      "callCenterOperatorName": null,
      "totalItems": 1,
      "currencyCode": "BRL"
    },
    {
      "orderId": "v502556llux-01",
      "creationDate": "2019-01-28T20:09:43.0000000+00:00",
      "clientName": "Rodrigo VTEX",
      "items": null,
      "totalValue": 1160,
      "paymentNames": "Boleto Bancário",
      "status": "handling",
      "statusDescription": "Preparando Entrega",
      "marketPlaceOrderId": null,
      "sequence": "502556",
      "salesChannel": "1",
      "affiliateId": "",
      "origin": "Marketplace",
      "workflowInErrorState": false,
      "workflowInRetry": false,
      "lastMessageUnread": " Lux Store Seu pedido foi alterado! Pedido realizado em: 28/01/2019 Olá, Rodrigo. Seu pedido foi alterado. Seguem informações abaixo: ",
      "ShippingEstimatedDate": "2019-02-04T20:33:46.0000000+00:00",
      "ShippingEstimatedDateMax": null,
      "ShippingEstimatedDateMin": null,
      "orderIsComplete": true,
      "listId": null,
      "listType": null,
      "authorizedDate": "2019-01-28T20:33:04.0000000+00:00",
      "callCenterOperatorName": null,
      "totalItems": 1,
      "currencyCode": "BRL"
    },
    {
      "orderId": "v502553llux-01",
      "creationDate": "2019-01-24T12:35:19.0000000+00:00",
      "clientName": "test test",
      "items": null,
      "totalValue": 10150,
      "paymentNames": "Mastercard",
      "status": "ready-for-handling",
      "statusDescription": "Pronto para o manuseio",
      "marketPlaceOrderId": null,
      "sequence": "502554",
      "salesChannel": "1",
      "affiliateId": "",
      "origin": "Marketplace",
      "workflowInErrorState": false,
      "workflowInRetry": false,
      "lastMessageUnread": " Lux Store 96 Sua Nota Fiscal foi emitida. Referente ao Pedido #v502553llux-01 Olá, test. Estamos empacotando seu produto para provide",
      "ShippingEstimatedDate": "2019-01-31T12:36:30.0000000+00:00",
      "ShippingEstimatedDateMax": null,
      "ShippingEstimatedDateMin": null,
      "orderIsComplete": true,
      "listId": null,
      "listType": null,
      "authorizedDate": "2019-01-24T12:36:01.0000000+00:00",
      "callCenterOperatorName": null,
      "totalItems": 1,
      "currencyCode": "BRL"
    },
    {
      "orderId": "v502550llux-01",
      "creationDate": "2019-01-23T16:39:45.0000000+00:00",
      "clientName": "test test",
      "items": null,
      "totalValue": 10150,
      "paymentNames": "Mastercard",
      "status": "ready-for-handling",
      "statusDescription": "Pronto para o manuseio",
      "marketPlaceOrderId": null,
      "sequence": "502551",
      "salesChannel": "1",
      "affiliateId": "",
      "origin": "Marketplace",
      "workflowInErrorState": false,
      "workflowInRetry": false,
      "lastMessageUnread": " Lux Store 96 Seu pagamento foi aprovado. Referente ao Pedido #v502550llux-01 Olá, test. Estamos providenciando a emissão da Nota Fisc",
      "ShippingEstimatedDate": "2019-01-30T16:40:55.0000000+00:00",
      "ShippingEstimatedDateMax": null,
      "ShippingEstimatedDateMin": null,
      "orderIsComplete": true,
      "listId": null,
      "listType": null,
      "authorizedDate": "2019-01-23T16:40:27.0000000+00:00",
      "callCenterOperatorName": null,
      "totalItems": 1,
      "currencyCode": "BRL"
    },
    {
      "orderId": "v502547llux-01",
      "creationDate": "2019-01-23T16:34:20.0000000+00:00",
      "clientName": "test test",
      "items": null,
      "totalValue": 10150,
      "paymentNames": "Mastercard",
      "status": "ready-for-handling",
      "statusDescription": "Pronto para o manuseio",
      "marketPlaceOrderId": null,
      "sequence": "502548",
      "salesChannel": "1",
      "affiliateId": "",
      "origin": "Marketplace",
      "workflowInErrorState": false,
      "workflowInRetry": false,
      "lastMessageUnread": " Lux Store 96 Seu pagamento foi aprovado. Referente ao Pedido #v502547llux-01 Olá, test. Estamos providenciando a emissão da Nota Fisc",
      "ShippingEstimatedDate": "2019-01-30T16:35:30.0000000+00:00",
      "ShippingEstimatedDateMax": null,
      "ShippingEstimatedDateMin": null,
      "orderIsComplete": true,
      "listId": null,
      "listType": null,
      "authorizedDate": "2019-01-23T16:35:04.0000000+00:00",
      "callCenterOperatorName": null,
      "totalItems": 1,
      "currencyCode": "BRL"
    },
    {
      "orderId": "v502544llux-01",
      "creationDate": "2018-12-28T18:15:28.0000000+00:00",
      "clientName": "test test",
      "items": null,
      "totalValue": 8990,
      "paymentNames": "Boleto Bancário",
      "status": "canceled",
      "statusDescription": "Cancelado",
      "marketPlaceOrderId": null,
      "sequence": "502544",
      "salesChannel": "1",
      "affiliateId": "",
      "origin": "Marketplace",
      "workflowInErrorState": false,
      "workflowInRetry": false,
      "lastMessageUnread": " Lux Store 96 Seu pedido foi cancelado. Referente ao Pedido #v502544llux-01 Resumo Itens R$ 89,90 Total R$ 89,90 Produto Alavanca De M",
      "ShippingEstimatedDate": null,
      "ShippingEstimatedDateMax": null,
      "ShippingEstimatedDateMin": null,
      "orderIsComplete": true,
      "listId": null,
      "listType": null,
      "authorizedDate": null,
      "callCenterOperatorName": null,
      "totalItems": 1,
      "currencyCode": "BRL"
    },
    {
      "orderId": "v502541llux-01",
      "creationDate": "2018-12-18T18:48:17.0000000+00:00",
      "clientName": "Douglas Rodrigues",
      "items": null,
      "totalValue": 3290,
      "paymentNames": "Boleto Bancário",
      "status": "canceled",
      "statusDescription": "Cancelado",
      "marketPlaceOrderId": null,
      "sequence": "502541",
      "salesChannel": "1",
      "affiliateId": "",
      "origin": "Marketplace",
      "workflowInErrorState": false,
      "workflowInRetry": false,
      "lastMessageUnread": " Lux Store 96 Seu pedido foi cancelado. Referente ao Pedido #v502541llux-01 Resumo Itens R$ 32,90 Total R$ 32,90 Produto Bay Max L 1 u",
      "ShippingEstimatedDate": null,
      "ShippingEstimatedDateMax": null,
      "ShippingEstimatedDateMin": null,
      "orderIsComplete": true,
      "listId": null,
      "listType": null,
      "authorizedDate": null,
      "callCenterOperatorName": null,
      "totalItems": 1,
      "currencyCode": "BRL"
    },
    {
      "orderId": "v502538llux-01",
      "creationDate": "2018-12-12T18:21:47.0000000+00:00",
      "clientName": "test test",
      "items": null,
      "totalValue": 8990,
      "paymentNames": "Mastercard",
      "status": "ready-for-handling",
      "statusDescription": "Pronto para o manuseio",
      "marketPlaceOrderId": null,
      "sequence": "502538",
      "salesChannel": "1",
      "affiliateId": "",
      "origin": "Marketplace",
      "workflowInErrorState": false,
      "workflowInRetry": false,
      "lastMessageUnread": " Lux Store 96 Seu pagamento foi aprovado. Referente ao Pedido #v502538llux-01 Olá, test. Estamos providenciando a emissão da Nota Fisc",
      "ShippingEstimatedDate": "2018-12-19T18:22:26.0000000+00:00",
      "ShippingEstimatedDateMax": null,
      "ShippingEstimatedDateMin": null,
      "orderIsComplete": true,
      "listId": null,
      "listType": null,
      "authorizedDate": "2018-12-12T18:22:22.0000000+00:00",
      "callCenterOperatorName": null,
      "totalItems": 1,
      "currencyCode": "BRL"
    },
    {
      "orderId": "SCP-880102018018-01",
      "creationDate": "2018-11-30T17:34:01.0000000+00:00",
      "clientName": "roberta grecco",
      "items": null,
      "totalValue": 1250,
      "paymentNames": "",
      "status": "canceled",
      "statusDescription": "Cancelado",
      "marketPlaceOrderId": "880102018018-01",
      "sequence": "502537",
      "salesChannel": "1",
      "affiliateId": "SCP",
      "origin": "Fulfillment",
      "workflowInErrorState": false,
      "workflowInRetry": false,
      "lastMessageUnread": "cancelamento teste shp ",
      "ShippingEstimatedDate": null,
      "ShippingEstimatedDateMax": null,
      "ShippingEstimatedDateMin": null,
      "orderIsComplete": true,
      "listId": null,
      "listType": null,
      "authorizedDate": "2018-11-30T17:34:42.0000000+00:00",
      "callCenterOperatorName": null,
      "totalItems": 1,
      "currencyCode": "BRL"
    },
    {
      "orderId": "SCP-880091692043-01",
      "creationDate": "2018-11-30T17:28:35.0000000+00:00",
      "clientName": "roberta grecco",
      "items": null,
      "totalValue": 1250,
      "paymentNames": "",
      "status": "invoiced",
      "statusDescription": "Faturado",
      "marketPlaceOrderId": "880091692043-01",
      "sequence": "502536",
      "salesChannel": "1",
      "affiliateId": "SCP",
      "origin": "Fulfillment",
      "workflowInErrorState": false,
      "workflowInRetry": false,
      "lastMessageUnread": null,
      "ShippingEstimatedDate": null,
      "ShippingEstimatedDateMax": null,
      "ShippingEstimatedDateMin": null,
      "orderIsComplete": true,
      "listId": null,
      "listType": null,
      "authorizedDate": "2018-11-30T17:29:22.0000000+00:00",
      "callCenterOperatorName": null,
      "totalItems": 1,
      "currencyCode": "BRL"
    },
    {
      "orderId": "SCP-880091058221-01",
      "creationDate": "2018-11-30T17:18:00.0000000+00:00",
      "clientName": "roberta grecco",
      "items": null,
      "totalValue": 1250,
      "paymentNames": "",
      "status": "canceled",
      "statusDescription": "Cancelado",
      "marketPlaceOrderId": "880091058221-01",
      "sequence": "502535",
      "salesChannel": "1",
      "affiliateId": "SCP",
      "origin": "Fulfillment",
      "workflowInErrorState": false,
      "workflowInRetry": false,
      "lastMessageUnread": "Teste de cancelamento do ShopFácil ",
      "ShippingEstimatedDate": null,
      "ShippingEstimatedDateMax": null,
      "ShippingEstimatedDateMin": null,
      "orderIsComplete": true,
      "listId": null,
      "listType": null,
      "authorizedDate": "2018-11-30T17:18:44.0000000+00:00",
      "callCenterOperatorName": null,
      "totalItems": 1,
      "currencyCode": "BRL"
    },
    {
      "orderId": "SCP-880090643370-01",
      "creationDate": "2018-11-30T17:10:59.0000000+00:00",
      "clientName": "roberta grecco",
      "items": null,
      "totalValue": 1250,
      "paymentNames": "",
      "status": "ready-for-handling",
      "statusDescription": "Pronto para o manuseio",
      "marketPlaceOrderId": "880090643370-01",
      "sequence": "502534",
      "salesChannel": "1",
      "affiliateId": "SCP",
      "origin": "Fulfillment",
      "workflowInErrorState": false,
      "workflowInRetry": false,
      "lastMessageUnread": null,
      "ShippingEstimatedDate": "2018-12-07T17:11:39.0000000+00:00",
      "ShippingEstimatedDateMax": null,
      "ShippingEstimatedDateMin": null,
      "orderIsComplete": true,
      "listId": null,
      "listType": null,
      "authorizedDate": "2018-11-30T17:11:42.0000000+00:00",
      "callCenterOperatorName": null,
      "totalItems": 1,
      "currencyCode": "BRL"
    },
    {
      "orderId": "SCP-880090622238-01",
      "creationDate": "2018-11-30T17:10:45.0000000+00:00",
      "clientName": "roberta grecco",
      "items": null,
      "totalValue": 1250,
      "paymentNames": "",
      "status": "canceled",
      "statusDescription": "Cancelado",
      "marketPlaceOrderId": "880090622238-01",
      "sequence": "502533",
      "salesChannel": "1",
      "affiliateId": "SCP",
      "origin": "Fulfillment",
      "workflowInErrorState": false,
      "workflowInRetry": false,
      "lastMessageUnread": null,
      "ShippingEstimatedDate": null,
      "ShippingEstimatedDateMax": null,
      "ShippingEstimatedDateMin": null,
      "orderIsComplete": true,
      "listId": null,
      "listType": null,
      "authorizedDate": null,
      "callCenterOperatorName": null,
      "totalItems": 1,
      "currencyCode": "BRL"
    },
    {
      "orderId": "MNC-877730530419-01",
      "creationDate": "2018-11-20T21:09:01.0000000+00:00",
      "clientName": "Carlos VTEX",
      "items": null,
      "totalValue": 11150,
      "paymentNames": "",
      "status": "canceled",
      "statusDescription": "Cancelado",
      "marketPlaceOrderId": "877730530419-01",
      "sequence": "502532",
      "salesChannel": "1",
      "affiliateId": "MNC",
      "origin": "Fulfillment",
      "workflowInErrorState": false,
      "workflowInRetry": false,
      "lastMessageUnread": null,
      "ShippingEstimatedDate": null,
      "ShippingEstimatedDateMax": null,
      "ShippingEstimatedDateMin": null,
      "orderIsComplete": true,
      "listId": null,
      "listType": null,
      "authorizedDate": "2018-11-20T21:13:06.0000000+00:00",
      "callCenterOperatorName": null,
      "totalItems": 1,
      "currencyCode": "BRL"
    },
    {
      "orderId": "SCP-876733475998-01",
      "creationDate": "2018-11-16T16:58:18.0000000+00:00",
      "clientName": "roberta grecco",
      "items": null,
      "totalValue": 1250,
      "paymentNames": "",
      "status": "ready-for-handling",
      "statusDescription": "Pronto para o manuseio",
      "marketPlaceOrderId": "876733475998-01",
      "sequence": "502531",
      "salesChannel": "1",
      "affiliateId": "SCP",
      "origin": "Fulfillment",
      "workflowInErrorState": false,
      "workflowInRetry": false,
      "lastMessageUnread": null,
      "ShippingEstimatedDate": "2018-11-23T16:58:48.0000000+00:00",
      "ShippingEstimatedDateMax": null,
      "ShippingEstimatedDateMin": null,
      "orderIsComplete": true,
      "listId": null,
      "listType": null,
      "authorizedDate": "2018-11-16T16:58:53.0000000+00:00",
      "callCenterOperatorName": null,
      "totalItems": 1,
      "currencyCode": "BRL"
    }
  ],
  "facets": [],
  "paging": {
    "total": 84,
    "pages": 6,
    "currentPage": 1,
    "perPage": 15
  },
  "stats": {
    "stats": {
      "totalValue": {
        "Count": 84,
        "Max": 21526180,
        "Mean": 262672.75,
        "Min": 1160,
        "Missing": 0,
        "StdDev": 2348087.3869179883,
        "Sum": 22064511,
        "SumOfSquares": 463417439039853,
        "Facets": {
          "origin": {
            "Fulfillment": {
              "Count": 68,
              "Max": 11150,
              "Mean": 1395.5882352941176,
              "Min": 1250,
              "Missing": 0,
              "StdDev": 1200.5513439298484,
              "Sum": 94900,
              "SumOfSquares": 229010000,
              "Facets": null
            },
            "Marketplace": {
              "Count": 16,
              "Max": 21526180,
              "Mean": 1373100.6875,
              "Min": 1160,
              "Missing": 0,
              "StdDev": 5374326.141087491,
              "Sum": 21969611,
              "SumOfSquares": 463417210029853,
              "Facets": null
            }
          },
          "currencyCode": {
            "BRL": {
              "Count": 84,
              "Max": 21526180,
              "Mean": 262672.75,
              "Min": 1160,
              "Missing": 0,
              "StdDev": 2348087.3869179883,
              "Sum": 22064511,
              "SumOfSquares": 463417439039853,
              "Facets": null
            }
          }
        }
      },
      "totalItems": {
        "Count": 84,
        "Max": 89,
        "Mean": 2.2261904761904763,
        "Min": 1,
        "Missing": 0,
        "StdDev": 9.660940100525016,
        "Sum": 187,
        "SumOfSquares": 8163,
        "Facets": {
          "origin": {
            "Fulfillment": {
              "Count": 68,
              "Max": 1,
              "Mean": 1,
              "Min": 1,
              "Missing": 0,
              "StdDev": 0,
              "Sum": 68,
              "SumOfSquares": 68,
              "Facets": null
            },
            "Marketplace": {
              "Count": 16,
              "Max": 89,
              "Mean": 7.4375,
              "Min": 1,
              "Missing": 0,
              "StdDev": 21.92401651157926,
              "Sum": 119,
              "SumOfSquares": 8095,
              "Facets": null
            }
          },
          "currencyCode": {
            "BRL": {
              "Count": 84,
              "Max": 89,
              "Mean": 2.2261904761904763,
              "Min": 1,
              "Missing": 0,
              "StdDev": 9.660940100525016,
              "Sum": 187,
              "SumOfSquares": 8163,
              "Facets": null
            }
          }
        }
      }
    }
  }
}
```
