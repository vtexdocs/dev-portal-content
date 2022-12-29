---
title: "Sending invoice and tracking code to the marketplace"
slug: "external-marketplace-integration-invoice-tracking"
hidden: false
createdAt: "2021-09-02T20:56:04.330Z"
updatedAt: "2022-06-09T21:59:50.349Z"
---

When integrating orders fulfilled by VTEX sellers, it is important to include tracking codes and invoice data. There are some requirements needed, before connectors can make sure that invoice and tracking code were sent to the marketplace:

- The tracking code and invoice information must be contained within the VTEX Order.
- Connectors should offer a secure endpoint to receive VTEX notification from our [Retrieve feed order status](https://developers.vtex.com/vtex-rest-api/reference/getfeedorderstatus1) endpoint updating tracking code and invoice data
- Tracking code and other data about the order’s delivery will only be made available to orders where the seller is in charge of delivery.

## Invoice notification from VTEX

The invoice sent by VTEX consists of a notification for the connector's URL, with the following structure:

`http://{{marketplaceServicesEndpoint}}/pub/orders/{{orderId}}/invoice`.

If the connector does not take that into account in their integration, they might receive an error 400 in VTEX's Send Invoice requests.

## Integrating tracking code and invoice data

The diagram below describes the notification flow, for integrating tracking code and invoice data:

Follow the steps below to integrate them, once receiving the notification. Make sure to review our [Recommendations](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-recommendations) page before you start.

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/external-marketplace-integration-invoice-tracking-0.jpg)

1. VTEX Orders receive tracking and/or invoice data. This information can be inserted via [Place Fulfillment Order API](https://developers.vtex.com/vtex-rest-api/reference/place-fulfillment-order) or manually in VTEX Admin. 
After receiving invoice information, the order status is updated to `invoiced` in VTEX. In this case, it is not possible to cancel the order anymore. 
2. VTEX OMS notifies the connector through the URL informed in [Invoice notification from VTEX](#invoice-notification-from-vtex) by the connector through the property `marketplaceServicesEndpoint`, once the order is inserted in VTEX. 
3. Connector collects information sent through the notification.
a. To collect information about **invoice**, use the properties:
    - `invoiceNumer`: invoice’s ID code.
    - `invoiceUrl`: URL that leads to the invoice document.
    - `embeddedInvoice`: invoice document’s XML file. 
    - `invoiceValue`: value declared in the invoice.
    - `invoiceKey`: invoice’s key.
b. To collect information about **tracking code**, use the properties:
    - `courier`: carrier’s name.
    - `trackingNumber`: number used by the carrier to identify the delivery
    - `trackingUrl`: carrier’s URL used by clients to track the order’s delivery. 
4. Connector transforms the information to the expected format in the marketplace.
5. Connector sends the information to the marketplace.
6. Marketplace validates and records information, and responds with a success or failure status. 
7. Connector generates an [Order log](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-order-logs) for each situation.


Note that:


- An order can have more than one invoice with partial values
- The tracking code and/or invoice can be filled in at different moments. In this case it is important to understand the flow demanded by the marketplace for sending separate information.
- Not all fields listed are demanded by the marketplace. Keep in mind to check which ones are in fact mandatory and the correct moment to send them. 
[block:callout]
{
  "type": "info",
  "body": "Make sure that all steps are logged as either success or failure, to offer the operation's full traceability. Check out the [Order logs](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-order-logs) page to learn more",
  "title": "Order Logs"
}
[/block]
## API Reference

Use the endpoints described below to perform this step. It is important to note that when consuming this API, the connector must have a valid VTEX App Key and App Token.

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/external-marketplace-integration-invoice-tracking-1.jpg)
[block:callout]
{
  "type": "info",
  "body": "All parameters in the endpoints below must be declared in the request. In case one of the parameters does not have a value, you must still send it as `null`.",
  "title": "Request bodies for POST calls"
}
[/block]
### Shopping cart simulation

Use the request example below to perform the Shopping Cart Simulation. Check out our  [Shopping cart Simulation](https://developers.vtex.com/vtex-rest-api/reference/cartsimulation) API Reference to know more details.

[block:code]
{
  "codes": [
    {
      "code": "{\n\"items\":[\n{...}\n]\n\"ratesAndBenefitsData\":{\n\"rateAndBenefitsIdentifiers\":[]\n\"teaser\":[]\n}\n\"paymentData\":{\n\"installmentOptions\":[...]\n\"paymentSystems\":[...]\n\"payments\":[]\n\"giftCards\":[]\n\"giftCardMessages\":[]\n\"availableAccounts\":[]\n\"availableTokens\":[]\n}\n\"selectableGifts\":[]\n\"marketingData\":NULL\n\"postalCode\":NULL\n\"country\":\"BRA\"\n\"logisticsInfo\":[\n{...}\n]\n\"messages\":[]\n\"purchaseConditions\":{\n\"itemPurchaseConditions\":[...]\n}\n\"pickupPoints\":[]\n\"subscriptionData\":NULL\n\"totals\":[\n{...}\n]\n\"itemMetadata\":NULL\n}",
      "language": "text",
      "name": "Shopping Cart Simulation - Request Example"
    }
  ]
}
[/block]
### Place fulfillment order

Use the request example below to place fulfillment order. Check out our [Place fulfillment order](https://developers.vtex.com/vtex-rest-api/reference/place-fulfillment-order) API Reference to know more details.
[block:code]
{
  "codes": [
    {
      "code": "[\n  {\n    \"items\": [\n        {\n            \"id\": \"1\",\n            \"price\": 900,\n            \"quantity\": 1,\n            \"seller\": \"1\"\n        }\n    ],\n    \"isCreatedAsync\": true,\n    \"marketplaceOrderGroup\" : \"794901324\",\n    \"marketplaceOrderId\": \"2630580124\",\n    \"marketplacePaymentValue\": 1100,\n    \"marketplacePaymentReferenceValue\": 1100,\n    \"marketplaceServicesEndpoint\": \"http://skyhubintegration.vtexinternal.com/api/skyhubintegration/commercialcondition?an=grocery1\",\n    \"clientProfileData\": {\n        \"CorporateDocument\": null, //Cnpj\n        \"CorporateName\": null, //nome da empresa\n        \"CorporatePhone\": null, // ddd+telefone\n        \"Document\": \"14310315771\", //cpf\n        \"DocumentType\": null, //se pessoa fisica, colocar CPF, senão CNPJ\n        \"Email\": \"conta@dominio.com.br\",\n        \"FirstName\": \"Nome\",\n        \"IsCorporate\": false, //caso pessoa juridica o valor deve ser true\n        \"LastName\": \"Sobrenome\",\n        \"Phone\": \"41998718616\",\n        \"StateInscription\": null, //inscrição estadual\n        \"TradeName\": null,\n        \"UserProfileId\": null //utilizado somente com pedidos VTEX\n    },\n    \"shippingData\": {\n        \"address\": {\n            \"addressId\": \"Casa\",\n            \"addressType\": \"Residencial\",\n            \"receiverName\": \"Marcelo\",\n            \"city\": \"Curitiba\",\n            \"complement\": null,\n            \"country\": \"BRA\",\n            \"geoCoordinates\": [],\n            \"neighborhood\": \"Novo Mundo\",\n            \"number\": \"4000\",\n            \"postalCode\": \"81020230\",\n            \"reference\": null,\n            \"state\": \"PR\",\n            \"street\": \"Rua Eduardo Carlos Pereira\"\n        },\n        \"logisticsInfo\": [\n            {\n                    \"itemIndex\": 0,\n                    \"price\": 200,\n                    \"selectedDeliveryChannel\":\"delivery\",\n                    \"selectedSla\": null,\n                    \"lockTTL\": \"1d\", //tempo para reserva do estoque do pedido\n                    \"shippingEstimate\":\"1d\" //tempo de entrega do pedido\n            }\n        ],\n        \"selectedAddresses\":[\n          {\n            \"addressType\": \"Residencial\",\n            \"receiverName\": \"Henrique Vianna\",\n            \"addressId\": \"2\",\n            \"postalCode\": \"81020-235\",\n            \"city\": \"Curitiba\",\n            \"state\": \"PR\",\n            \"country\": \"BRA\",\n            \"street\": \"Rua Eduardo Carlos Pereira\",\n            \"number\": \"4125\",\n            \"neighborhood\": \"Portão\",\n            \"complement\": \"\",\n            \"reference\": null,\n            \"geoCoordinates\": [\n                -49.2892059,\n                -25.4826319\n            ]\n        }],\n        \"isFob\": false //se entrega feita pelo lojista coloque false, senão true\n    },\n    \"customData\": {\n\t\t\"customApps\": [{\n\t\t\t\"fields\": {\n\t\t\t\t\"orderIdMarketplace\": \"2630580148\",\n\t\t\t\t\"paymentIdMarketplace\": \"8191598627\"\n\t\t\t},\n\t\t\t\"id\": \"marketplace-integration\",\n\t\t\t\"major\": 1\n\t\t}]\n\t},\n    \"openTextField\": {\n         \"value\": \"{\\\"Phones\\\":[\\\"21998718616\\\"]}\"\n    }\n  }\n]",
      "language": "text",
      "name": "Place Fulfillment Order - Request Example"
    }
  ]
}
[/block]
### Authorize dispatch

Use the request example below to authorize dispatch. Check out our [Authorize Dispatch](https://developers.vtex.com/vtex-rest-api/reference/authorize-dispatch-for-fulfillment-order)
 API Reference to know more details.

[block:code]
{
  "codes": [
    {
      "code": "[\n  {\n    \"marketplaceOrderId\": \"956\"\n  }\n]",
      "language": "text",
      "name": "Authorize Dispatch - Request Example"
    }
  ]
}
[/block]
