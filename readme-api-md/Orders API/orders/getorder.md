---
title: "Get order"
slug: "getorder"
excerpt: "Retrieves order details by searching a specific order ID or sequence number.\n\r\n\r> The `View order` resource is needed to use this API request. This is included in `OMS - Full access` and `IntegrationProfile - Fulfillment Oms`, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#).\r\n\r\n> 📘 Onboarding guide \r\n>\r\n> Check the new [Orders onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/orders-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Orders and is organized by focusing on the developer's journey."
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2022-11-30T17:22:54.197Z"
---
[block:api-header]
{
  "title": "Throttling"
}
[/block]

[block:html]
{
  "html": "<div class=\"alert alert-info\">Throttling: Each account can make up to 5000 requests per minute.\n</div>"
}
[/block]

[block:api-header]
{
  "title": "Request body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET 'https://{{accountName}}.{{environment}}.com.br/api/oms/pvt/orders/v5195004lux-01' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
      "language": "json",
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
      "code": "{\n  \"emailTracked\": \"a27499cad31f42b7a771ae34f57c8358@ct.vtex.com.br\",\n  \"approvedBy\": null,\n  \"cancelledBy\": null,\n  \"cancelReason\": null,\n  \"orderId\": \"v5195004lux-01\",\n  \"sequence\": \"502556\",\n  \"marketplaceOrderId\": \"\",\n  \"marketplaceServicesEndpoint\": \"http://oms.vtexinternal.com.br/api/oms?an=luxstore\",\n  \"sellerOrderId\": \"00-v5195004lux-01\",\n  \"origin\": \"Marketplace\",\n  \"affiliateId\": \"\",\n  \"salesChannel\": \"1\",\n  \"merchantName\": null,\n  \"status\": \"handling\",\n  \"statusDescription\": \"Preparando Entrega\",\n  \"value\": 1160,\n  \"creationDate\": \"2019-01-28T20:09:43.8999580+00:00\",\n  \"lastChange\": \"2019-02-06T20:46:11.7010747+00:00\",\n  \"orderGroup\": null,\n  \"totals\": [\n    {\n      \"id\": \"Items\",\n      \"name\": \"Total dos Itens\",\n      \"value\": 3290\n    },\n    {\n      \"id\": \"Discounts\",\n      \"name\": \"Total dos Descontos\",\n      \"value\": 0\n    },\n    {\n      \"id\": \"Shipping\",\n      \"name\": \"Total do Frete\",\n      \"value\": 1160\n    },\n    {\n      \"id\": \"Tax\",\n      \"name\": \"Total da Taxa\",\n      \"value\": 0\n    },\n    {\n      \"id\": \"Change\",\n      \"name\": \"Total das mudanças\",\n      \"value\": -3290\n    }\n  ],\n  \"items\": [\n    {\n      \"uniqueId\": \"87F0945396994B349158C7D9C9941442\",\n      \"id\": \"1234568358\",\n      \"productId\": \"9429485\",\n      \"ean\": null,\n      \"lockId\": \"00-v5195004lux-01\",\n      \"itemAttachment\": {\n        \"content\": {},\n        \"name\": null\n      },\n      \"attachments\": [],\n      \"quantity\": 1,\n      \"seller\": \"1\",\n      \"name\": \"Bay Max L\",\n      \"refId\": \"BIGHEROBML\",\n      \"price\": 3290,\n      \"listPrice\": 3290,\n      \"manualPrice\": null,\n      \"priceTags\": [],\n      \"imageUrl\": \"http://luxstore.vteximg.com.br/arquivos/ids/159263-55-55/image-cc1aed75cbfa424a85a94900be3eacec.jpg?v=636795432619830000\",\n      \"detailUrl\": \"/bay-max-9429485/p\",\n      \"components\": [],\n      \"bundleItems\": [],\n      \"params\": [],\n      \"offerings\": [],\n      \"sellerSku\": \"1234568358\",\n      \"priceValidUntil\": null,\n      \"commission\": 0,\n      \"tax\": 0,\n      \"preSaleDate\": null,\n      \"additionalInfo\": {\n        \"brandName\": \"VTEX\",\n        \"brandId\": \"2000023\",\n        \"categoriesIds\": \"/1/\",\n        \"productClusterId\": \"135,142\",\n        \"commercialConditionId\": \"5\",\n        \"dimension\": {\n          \"cubicweight\": 0.7031,\n          \"height\": 15,\n          \"length\": 15,\n          \"weight\": 15,\n          \"width\": 15\n        },\n        \"offeringInfo\": null,\n        \"offeringType\": null,\n        \"offeringTypeId\": null\n      },\n      \"measurementUnit\": \"un\",\n      \"unitMultiplier\": 1,\n      \"sellingPrice\": 3290,\n      \"isGift\": false,\n      \"shippingPrice\": null,\n      \"rewardValue\": 0,\n      \"freightCommission\": 0,\n      \"priceDefinition\": {\n        \"sellingPrice\": [\n          {\n             \"quantity\": 1,\n             \"value\": 3290,\n          }\n        ],\n        \"total\": 3290     \n      },\n      \"taxCode\": null,\n      \"parentItemIndex\": null,\n      \"parentAssemblyBinding\": null\n    }\n  ],\n  \"marketplaceItems\": [],\n  \"clientProfileData\": {\n    \"id\": \"clientProfileData\",\n    \"email\": \"rodrigo.cunha@vtex.com.br\",\n    \"firstName\": \"Rodrigo\",\n    \"lastName\": \"VTEX\",\n    \"documentType\": \"cpf\",\n    \"document\": \"11047867702\",\n    \"phone\": \"+5521972321094\",\n    \"corporateName\": null,\n    \"tradeName\": null,\n    \"corporateDocument\": null,\n    \"stateInscription\": null,\n    \"corporatePhone\": null,\n    \"isCorporate\": false,\n    \"userProfileId\": \"5a3692de-358a-4bea-8885-044bce33bb93\",\n    \"customerClass\": null\n  },\n  \"giftRegistryData\": null,\n  \"marketingData\": null,\n  \"ratesAndBenefitsData\": {\n    \"id\": \"ratesAndBenefitsData\",\n    \"rateAndBenefitsIdentifiers\": []\n  },\n  \"shippingData\": {\n    \"id\": \"shippingData\",\n    \"address\": {\n      \"addressType\": \"residential\",\n      \"receiverName\": \"Rodrigo Cunha\",\n      \"addressId\": \"-1425945657910\",\n      \"postalCode\": \"22250-040\",\n      \"city\": \"Rio de Janeiro\",\n      \"state\": \"RJ\",\n      \"country\": \"BRA\",\n      \"street\": \"Praia de Botafogo\",\n      \"number\": \"300\",\n      \"neighborhood\": \"Botafogo\",\n      \"complement\": \"3\",\n      \"reference\": null,\n      \"geoCoordinates\": []\n    },\n    \"logisticsInfo\": [\n      {\n        \"itemIndex\": 0,\n        \"selectedSla\": \"Normal\",\n        \"lockTTL\": \"10d\",\n        \"price\": 1160,\n        \"listPrice\": 1160,\n        \"sellingPrice\": 1160,\n        \"deliveryWindow\": null,\n        \"deliveryCompany\": \"Todos os CEPS\",\n        \"shippingEstimate\": \"5bd\",\n        \"shippingEstimateDate\": \"2019-02-04T20:33:46.4595004+00:00\",\n        \"slas\": [\n          {\n            \"id\": \"Normal\",\n            \"name\": \"Normal\",\n            \"shippingEstimate\": \"5bd\",\n            \"deliveryWindow\": null,\n            \"price\": 1160,\n            \"deliveryChannel\": \"delivery\",\n            \"pickupStoreInfo\": {\n              \"additionalInfo\": null,\n              \"address\": null,\n              \"dockId\": null,\n              \"friendlyName\": null,\n              \"isPickupStore\": false\n            },\n            \"polygonName\": null\n          },\n          {\n            \"id\": \"Expressa\",\n            \"name\": \"Expressa\",\n            \"shippingEstimate\": \"5bd\",\n            \"deliveryWindow\": null,\n            \"price\": 1160,\n            \"deliveryChannel\": \"delivery\",\n            \"pickupStoreInfo\": {\n              \"additionalInfo\": null,\n              \"address\": null,\n              \"dockId\": null,\n              \"friendlyName\": null,\n              \"isPickupStore\": false\n            },\n            \"polygonName\": null\n          },\n          {\n            \"id\": \"Quebra Kit\",\n            \"name\": \"Quebra Kit\",\n            \"shippingEstimate\": \"2bd\",\n            \"deliveryWindow\": null,\n            \"price\": 1392,\n            \"deliveryChannel\": \"delivery\",\n            \"pickupStoreInfo\": {\n              \"additionalInfo\": null,\n              \"address\": null,\n              \"dockId\": null,\n              \"friendlyName\": null,\n              \"isPickupStore\": false\n            },\n            \"polygonName\": null\n          },\n          {\n            \"id\": \"Sob Encomenda\",\n            \"name\": \"Sob Encomenda\",\n            \"shippingEstimate\": \"32bd\",\n            \"deliveryWindow\": null,\n            \"price\": 1392,\n            \"deliveryChannel\": \"delivery\",\n            \"pickupStoreInfo\": {\n              \"additionalInfo\": null,\n              \"address\": null,\n              \"dockId\": null,\n              \"friendlyName\": null,\n              \"isPickupStore\": false\n            },\n            \"polygonName\": null\n          }\n        ],\n        \"shipsTo\": [\n          \"BRA\"\n        ],\n        \"deliveryIds\": [\n          {\n            \"courierId\": \"197a56f\",\n            \"courierName\": \"Todos os CEPS\",\n            \"dockId\": \"1\",\n            \"quantity\": 1,\n            \"warehouseId\": \"1_1\"\n          }\n        ],\n        \"deliveryChannel\": \"delivery\",\n        \"pickupStoreInfo\": {\n          \"additionalInfo\": null,\n          \"address\": null,\n          \"dockId\": null,\n          \"friendlyName\": null,\n          \"isPickupStore\": false\n        },\n        \"addressId\": \"-1425945657910\",\n        \"polygonName\": null\n      }\n    ],\n    \"trackingHints\": null,\n    \"selectedAddresses\": [\n      {\n        \"addressId\": \"-1425945657910\",\n        \"addressType\": \"residential\",\n        \"receiverName\": \"Rodrigo Cunha\",\n        \"street\": \"Praia de Botafogo\",\n        \"number\": \"518\",\n        \"complement\": \"10\",\n        \"neighborhood\": \"Botafogo\",\n        \"postalCode\": \"22250-040\",\n        \"city\": \"Rio de Janeiro\",\n        \"state\": \"RJ\",\n        \"country\": \"BRA\",\n        \"reference\": null,\n        \"geoCoordinates\": []\n      }\n    ]\n  },\n  \"paymentData\": {\n    \"transactions\": [\n      {\n        \"isActive\": true,\n        \"transactionId\": \"418213DE29634837A63DD693A937A696\",\n        \"merchantName\": \"luxstore\",\n        \"payments\": [\n          {\n            \"id\": \"D3DEECAB3C6C4B9EAF8EF4C1FE062FF3\",\n            \"paymentSystem\": \"6\",\n            \"paymentSystemName\": \"Boleto Bancário\",\n            \"value\": 4450,\n            \"installments\": 1,\n            \"referenceValue\": 4450,\n            \"cardHolder\": null,\n            \"firstDigits\": null,\n            \"lastDigits\": null,\n            \"url\": \"https://luxstore.vtexpayments.com.br:443/BankIssuedInvoice/Transaction/418213DE29634837A63DD693A937A696/Payment/D3DEECAB3C6C4B9EAF8EF4C1FE062FF3/Installment/{Installment}\",\n            \"giftCardId\": null,\n            \"giftCardName\": null,\n            \"giftCardCaption\": null,\n            \"redemptionCode\": null,\n            \"group\": \"bankInvoice\",\n            \"tid\": null,\n            \"dueDate\": \"2019-02-02\",\n            \"connectorResponses\": {},\n            \"billingAddress\": {\n                  \"postalCode\": \"00000-000\",\n                  \"city\": \"Rio de Janeiro\",\n                  \"state\": \"RJ\",\n                  \"country\": \"BRA\",\n                  \"street\": \"Avenida Vice-Presidente José Alencar\",\n                  \"number\": \"0000\",\n                  \"neighborhood\": \"Jacarepaguá\",\n                  \"complement\": null,\n                  \"reference\": null,\n                  \"geoCoordinates\": [\n                       -43.386474609375,\n                       -22.965709686279297\n                  ]\n             }\n          }\n        ]\n      }\n    ]\n  },\n  \"packageAttachment\": {\n    \"packages\": []\n  },\n  \"sellers\": [\n    {\n      \"id\": \"1\",\n      \"name\": \"Loja do Suporte\",\n      \"logo\": \"\"\n    }\n  ],\n  \"callCenterOperatorData\": null,\n  \"followUpEmail\": \"7bf3a59bbc56402c810bda9521ba449e@ct.vtex.com.br\",\n  \"lastMessage\": null,\n  \"hostname\": \"luxstore\",\n  \"invoiceData\": null,\n  \"changesAttachment\": {\n    \"id\": \"changeAttachment\",\n    \"changesData\": [\n      {\n        \"reason\": \"Blah\",\n        \"discountValue\": 3290,\n        \"incrementValue\": 0,\n        \"itemsAdded\": [],\n        \"itemsRemoved\": [\n          {\n            \"id\": \"1234568358\",\n            \"name\": \"Bay Max L\",\n            \"quantity\": 1,\n            \"price\": 3290,\n            \"unitMultiplier\": null\n          }\n        ],\n        \"receipt\": {\n          \"date\": \"2019-02-06T20:46:04.4003606+00:00\",\n          \"orderId\": \"v5195004lux-01\",\n          \"receipt\": \"029f9ab8-751a-4b1e-bf81-7dd25d14b49b\"\n        }\n      }\n    ]\n  },\n  \"openTextField\": null,\n  \"roundingError\": 0,\n  \"orderFormId\": \"caae7471333e403f959fa5fd66951340\",\n  \"commercialConditionData\": null,\n  \"isCompleted\": true,\n  \"customData\": null,\n  \"storePreferencesData\": {\n    \"countryCode\": \"BRA\",\n    \"currencyCode\": \"BRL\",\n    \"currencyFormatInfo\": {\n      \"CurrencyDecimalDigits\": 2,\n      \"CurrencyDecimalSeparator\": \",\",\n      \"CurrencyGroupSeparator\": \".\",\n      \"CurrencyGroupSize\": 3,\n      \"StartsWithCurrencySymbol\": true\n    },\n    \"currencyLocale\": 1046,\n    \"currencySymbol\": \"R$\",\n    \"timeZone\": \"E. South America Standard Time\"\n  },\n  \"allowCancellation\": false,\n  \"allowEdition\": false,\n  \"isCheckedIn\": false,\n  \"marketplace\": {\n    \"baseURL\": \"http://oms.vtexinternal.com.br/api/oms?an=luxstore\",\n    \"isCertified\": null,\n    \"name\": \"luxstore\"\n  },\n  \"authorizedDate\": \"2019-01-28T20:33:04.0000000+00:00\",\n  \"invoicedDate\": null\n}",
      "language": "json",
      "name": "200 - OK"
    }
  ]
}
[/block]
## Request object has the following properties:

| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `orderId` | string | Order Id |


## Response object has the following properties:


| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `affiliateId` | string | Seller Name who was responsible for the order |
| `allowCancellation` | boolean | If Cancellation is allowed |
| `allowEdition` | boolean | If Order Edition is allowed |
| `approvedBy` | string | User who approved the order |
| `authorizedDate` | string | Authorized Order Date |
| `callCenterOperatorData` | string | Call Center Operator responsible for the order |
| `cancelReason` | string | Cancel Reason |
| `cancelledBy` | string | User who Cancelled the order |
| `changesAttachment` | object | Change details object |
| `changesData` | object | Array with each change |
| `discountValue` | integer | Change Discount Value |
| `incrementValue` | integer | Change Increment Value |
| `itemsAdded` | object | Added items details |
| `itemsRemoved` | object | Removed items details |
| `id` | integer | Changed SKU ID |
| `name` | string | Changed SKU Name |
| `price` | integer | Changed SKU Price |
| `quantity` | integer | Changed SKU Quantity |
| `unitMultiplier` | integer | Changed SKU Unit Multiplier |
| `reason` | string | Change Reason |
| `receipt` | object | Change receipt details object |
| `date` | string | Change receipt date |
| `orderId` | string | Change receipt order Id |
| `receipt` | object | Change receipt ID |
| `id` | string | Object Id, expect value "changeAttachment" |
| `clientProfileData` | object | Object with all Cliente Profile Data |
| `corporateDocument` | string | Client Corporate Document |
| `corporateName` | string | Client Corporate Name |
| `corporatePhone` | string | Cliente Corporate Telephone |
| `customerClass` | string | Customer class |
| `document` | string | Client Document |
| `documentType` | string | Client Document Type |
| `email` | string | Client e-mail |
| `firstName` | string | Client First Name |
| `id` | string | Object ID, expected value "clientProfileData" |
| `isCorporate` | string | If the Client is a Corporate Client |
| `lastName` | string | Client Last Name|
| `phone` | string | Client Telephone |
| `stateInscription` | string | Client Corporate Inscription |
| `tradeName` | string | Client Corporate Trade Name |
| `userProfileId` | string | Client User Profile ID |
| `commercialConditionData` | object | Commercial condition information, including `"Id"`, `"parentOrderId"`, and `"reason"` |
| `creationDate` | string | Order Creation Date |
| `customData` | object | Custom Data Object |
| `customApps` | object | Custom apps details object |
| `fields` | object | Custom app fields |
| `id` | string | Custom App ID |
| `major` | integer | Major |
| `emailTracked` | string | Client Conversation Tracker email  |
| `followUpEmail` | string | Responsible store e-mail |
| `giftRegistryData` | object | Gift registry list information, including `"addressId"` (object), `"description"` (string), and `"giftRegistryId"` (string) |
| `hostname` | string | Account hostname registered in License Manager |
| `invoiceData` | object | Information pertinent to the order's invoice |
| `invoicedDate` | string | Invoice Date |
| `isCheckedIn` | boolean | True if order is from inStore |
| `isCompleted` | boolean | True if the order is completed |
| `items` | object | Order items object |
| `additionalInfo` | string | Order item additional info |
| `brandId` | string | Brand ID |
| `brandName` | string | Brand name |
| `categoriesIds` | string | Item category ID |
| `commercialConditionId` | string | Invoice date |
| `dimension` | object | Item dimension object |
| `cubicweight` | number | Item cubic weight |
| `height` | number | Item height |
| `length` | number | Item length |
| `weight` | number | Item weight |
| `width` | number | Item width |
| `offeringInfo` | string | Extra information on offering |
| `offeringType` | string | Offering type |
| `offeringTypeId` | string | ID of offering type |
| `productClusterId` | string | All releated product clusters |
| `attachments` | object | Attachents Array |
| `content` | object | Attachment Content Custom Field |
| `name` | string | Attachment Name |
| `bundleItems` | object | Invoice date |
| `commission` | string | Comission value registered to Seller |
| `components` | object | If item is a kit, contains components information |
| `detailUrl` | string | Product Slug URL |
| `ean` | string | SKU EAN |
| `freightCommission` | integer | Comission value registered to seller |
| `id` | string | SKU Id |
| `imageUrl` | string | SKU Image URL |
| `isGift` | string | If this item is a gift in order context |
| `itemAttachment` | object | Attachment Object |
| `content` | object | Attachment Content Array |
| `name` | string | Attachment Name |
| `listPrice` | integer | Item List Price |
| `lockId` | string | Reservation ID |
| `manualPrice` | string | Manually inserted price, if there is one. |
| `measurementUnit` | string | Item measurement unit |
| `name` | string | Item name |
| `offerings` | object | Offerings information |
| `params` | object | "ContextParameter" hashset with `"name"` and `"value"` |
| `preSaleDate` | string | Item pre sale date |
| `price` | integer | Item Price |
| `items[].priceDefinition`                        | Object   | Price information for all units of a specific item.                                                                                                                  |
| `items[].priceDefinition.total`                  | Integer  | Total value for all units of the item in cents.                                                                                                                      |
| `items[].priceDefinition.calculatedSellingPrice` | Integer  | Item's calculated unitary selling price in cents.                                                                                                                    |
| `items[].priceDefinition.sellingPrices`          | Array    | Array of objects, each containing `value` (in cents) and `quantity` for the different rounding instances that can be combined to form the correctly rounded `total`. |
| `priceTags` | object | Object with all price modifiers |
| `identifier` | string | Price Tag ID |
| `isPercentual` | boolean | Indicates whether the price tag is a percentual modifier |
| `name` | string | Price tag name |
| `rawValue` | string | Price tag raw value |
| `value` | string | Price tag value |
| `priceValidUntil` | string | Price expiration date |
| `productId` | string | Item product ID |
| `quantity` | integer | Item quantity |
| `refId` | string | Item reference ID |
| `rewardValue` | integer | Item reward value |
| `seller` | string | Item seller |
| `sellerSku` | string | Invoice Date |
| `sellingPrice` | integer | Item selling price. For more accurate information, see the `priceDefinition` field |
| `shippingPrice` | string | Item Shipping Price |
| `tax` | integer | Item Tax |
| `taxCode` | string | Item Tax Code |
| `uniqueId` | string | Item Order Unique ID |
| `unitMultiplier` | integer | Item Unit Multipler |
| `lastChange` | string | Order Last Change Date |
| `lastMessage` | string | initial excerpt from last message sent to the customer |
| `marketingData` | string | Marketing Data Object |
| `coupon` | string | Order Disccount Coupon |
| `id` | string |  Object ID, expected value "marketingData" |
| `marketingTags` | object | Marketing Tags Array |
| `utmCampaign` | string | UTM Campaign Parameters |
| `utmMedium` | string | UTM Medium Parameters |
| `utmPartner` | string | UTM Source Parameters |
| `utmSource` | string | UTM Source Parameters|
| `utmiCampaign` | string | UTMI Campaign Internal Parameters |
| `utmiPart` | string | UTMI Part Internal Parameters |
| `utmipage` | string | UTMI Page Internal Parameters |
| `marketplace` | object | Marketplace Details Object |
| `baseURL` | string | Marketplace Base URL |
| `isCertified` | string | If is a Certified Marketplace |
| `name` | string | Marketplace Name |
| `marketplaceItems` | object | Marketplace Details Object |
| `marketplaceOrderId` | string | Marketplace Order Id |
| `marketplaceServicesEndpoint` | string | Marketplace Services Endpoint |
| `merchantName` | string | Merchant Name |
| `openTextField` | object | Open Text Field Object |
| `value` | string | Open Text Field Value |
| `orderFormId` | string | Order Form Id |
| `orderGroup` | string | Order Group Id |
| `orderId` | string | Order Id |
| `origin` | string | Order Origin: "Marketplace", "Fulfillment", or "Chain" (for the third level in a [Multilevel Omnichannel Inventory](https://help.vtex.com/en/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4?&utm_source=autocomplete#) purchase). |
| `packageAttachment` | object | Package Object |
| `packages` | object | Packages Details Object, populated after order invoiced |
| `cfop` | string | Fiscal code for operations and installments |
| `courier` | string | Package selected Courier |
| `courierStatus` | string | Package Tracking Status |
| `data` | object | Package Tracking Timeline |
| `finished` | string | If the delivery are finished |
| `status` | string | Courier Status |
| `embeddedInvoice` | string | XML of the invoice |
| `invoiceKey` | string | Invoice Credencial Key |
| `invoiceNumber` | string | Package Invoice Number |
| `invoiceUrl` | string | Package Invoice URL |
| `invoiceValue` | string | Package Invoice Value |
| `issuanceDate` | string | Package Issuance Date |
| `items` | string | Items Package Array |
| `description` | string | Item Desciprtion |
| `itemIndex` | string | Item Index |
| `price` | string | Item Price |
| `quantity` | string | Item Quantity |
| `unitMultiplier` | string | Unit Multiplier |
| `trackingNumber` | string | Package Tracking Number |
| `trackingUrl` | string | Tracking Order URL |
| `type` | string | Invoice Type, expected values "Output" and "Input" |
| `paymentData` | object | Payment Object |
| `transactions` | object | Transactions Object |
| `isActive` | boolean | If the payment is Active |
| `merchantName` | string | Merchant Name|
| `payments` | object | Payment Object |
| `cardHolder` | string | Payment Card Holder |
| `connectorResponses` | object | Connector Responses Object |
| `billingAddress` | object | Billing Address information |
| `Message` | string | Connector Responses Message |
| `ReturnCode` | string | Connector Return Code |
| `Tid` | string | Connector Transaction ID |
| `acquirer` | string | Connector acquirer |
| `authId` | string | Connector authorization ID |
| `dueDate` | string | Payment due date |
| `firstDigits` | string | Payment card first digits |
| `giftCardCaption` | string | Gift card caption |
| `giftCardId` | string | Gift card ID |
| `giftCardName` | string | Gift card name |
| `group` | string | Payment group |
| `id` | string | Payment ID |
| `installments` | string | Payment installments quantity |
| `lastDigits` | string | Payment card last digits |
| `paymentSystem` | string | Payment system type ID |
| `paymentSystemName` | string | Payment system name |
| `redemptionCode` | string | Gift card redemption code |
| `referenceValue` | string | Payment reference value |
| `tid` | string | Payment transaction ID |
| `url` | string | Payment URL |
| `value` | string | Payment value with interest if it applies |
| `transactionId` | string | Transaction Id |
| `ratesAndBenefitsData` | string | Rates and Benefits Data Object |
| `id` | string |  Object ID, expected value "ratesAndBenefitsData" |
| `rateAndBenefitsIdentifiers` | object | Rates and Benefits Details Object |
| `additionalInfo` | string |  Rates and Benefits Additional Info |
| `description` | string | Rates and Benefits Description |
| `featured` | string |  If is allowed to acumulate the Rates and Benefits |
| `matchedParameters` | object | March Parameters Array |
| `name` | string |  Rates and Benefits Name |
| `roundingError` | integer | Rounding Error Total Amount  |
| `salesChannel` | string | Order Sales Channel Id |
| `sellerOrderId` | string | Order Seller Id |
| `sellers` | object | Sellers Array |
| `id` | string | Seller Id |
| `logo` | string | URL Seller Logo |
| `name` | string | Seller Name |
| `sequence` | string | Order Sequence ID |
| `shippingData` | object | Shipping Data Object |
| `address` | object | Shipping Address |
| `addressId` | string | Shipping Address Id |
| `addressType` | string | Shipping Address Type |
| `city` | string | Shipping City |
| `complement` | string | Shipping Complement |
| `country` | string | Shipping Country in ISO 3166 ALPHA-3 abbreviation  |
| `geoCoordinates` | object | Shipping Geo Coordinates Array |
| `neighborhood` | string | Shipping Neighborhood |
| `number` | string | Shipping Number |
| `postalCode` | string | Shipping Postal Code |
| `receiverName` | string | Shipping Receiver Name |
| `reference` | string | Shipping Reference |
| `state` | string | Shipping State |
| `street` | string | Shipping Street |
| `id` | string | Object ID, expected value "shippingData"|
| `logisticsInfo` | object | Logistics Info Object |
| `addressId` | string | Adress Id |
| `deliveryChannel` | string | Delivery Channel, allowed values "delivery" or "pickup-in-point" |
| `deliveryCompany` | string | Courier Company Name |
| `deliveryIds` | object | Delivery Ids Object |
| `courierId` | string | Courier Id |
| `courierName` | string | Courier Name |
| `dockId` | string | Releated Dock Id |
| `quantity` | integer | Items Quantity |
| `warehouseId` | string | Releated Warehouse Id |
| `deliveryWindow` | object | Delivery Window Object |
| `endDateUtc` | string | Delivery Date End in UTC  |
| `price` | string | Delivery Window Cost |
| `startDateUtc` | string | Delivery Date Starts in UTC |
| `itemIndex` | integer | Logistic Info Item Index |
| `listPrice` | integer | Logistic Info Item List Price |
| `lockTTL` | string | Stock reservation waiting period |
| `pickupStoreInfo` | object | Pickup Store Info Object |
| `additionalInfo` | string | Pickup Store Additional Info |
| `address` | string | Pickup Store Address |
| `dockId` | string | Pickup Store Releated Dock Id |
| `friendlyName` | string | Pickup Store Friendly Name |
| `isPickupStore` | boolean | If is a Pickup Store |
| `polygonName` | string | Releated Polygom Name |
| `price` | integer | Logistic Info Item Price |
| `selectedSla` | string | Selected SLA |
| `sellingPrice` | integer | Logistic Info Item Selling Price |
| `shippingEstimate` | string | Estimate Shipping Duration |
| `shippingEstimateDate` | string | Estimate Shipping Date |
| `shipsTo` | object | Shipping Country in ISO 3166 ALPHA-3 abbreviation |
| `slas` | object | SLAs Object |
| `deliveryChannel` | string | Delivery Channel, allowed values "delivery" or "pickup-in-point" |
| `deliveryWindow` | object | Delivery Window Object |
| `endDateUtc` | string | Delivery Date End in UTC  |
| `price` | string | Delivery Window Cost |
| `startDateUtc` | string | Delivery Date Starts in UTC |
| `id` | string | SLA Id |
| `pickupStoreInfo` | object | Pickup Store Details Object |
| `additionalInfo` | string | Pickup Store Additional Info |
| `address` | string | Pickup Store Address |
| `dockId` | string | Pickup Store releated Dock Id  |
| `friendlyName` | string | Pickup Store Friendly Name |
| `isPickupStore` | boolean | If is a Pickup Store |
| `polygonName` | string | Releated Polygon Name |
| `price` | integer | SLA Price |
| `shippingEstimate` | string | SLA Shipping Estimate |
| `selectedAddresses` | object | Selected Address Details Object |
| `addressId` | string | Shipping Address Id |
| `addressType` | string | Shipping Address Type |
| `city` | string | Shipping City |
| `complement` | string | Shipping Complement |
| `country` | string | Shipping Country in ISO 3166 ALPHA-3 abbreviation  |
| `geoCoordinates` | object | Shipping Geo Coordinates Array |
| `neighborhood` | string | Shipping Neighborhood |
| `number` | string | Shipping Number |
| `postalCode` | string | Shipping Postal Code |
| `receiverName` | string | Shipping Receiver Name |
| `reference` | string | Shipping Reference |
| `state` | string | Shipping State |
| `street` | string | Shipping Street |
| `trackingHints` | array | Array of tracking hint objects, containing `"courierName"`, `"trackingId"`, `"trackingLabel"`, and `"trackingUrl"` |
| `status` | string | Order Status |
| `statusDescription` | string | Status Description |
| `storePreferencesData` | object | Store Preferences Data Object |
| `countryCode` | string | Country Code in ISO 3166 ALPHA-3 abbreviation |
| `currencyCode` | string | Currency Code in ISO 4217  |
| `currencyFormatInfo` | object | Currency Format Info Object |
| `CurrencyDecimalDigits` | integer | Currency Decimal Digits |
| `CurrencyDecimalSeparator` | string | Currency Decimal Separator |
| `CurrencyGroupSeparator` | string | Currency Group Separator |
| `CurrencyGroupSize` | integer | Currency Group Size |
| `StartsWithCurrencySymbol` | boolean | If Starts With Currency Symbol |
| `currencyLocale` | integer | LCID Decimal |
| `currencySymbol` | string | Currency Symbol |
| `timeZone` | string | Order Time Zone |
| `totals` | object | Totals Object |
| `id` | string | Totals Ids, expected values: "Items", "Discounts", "Shipping" and "Tax" |
| `name` | string | Totals ID Description |
| `value` | integer | Totals Value |
| `value` | integer | Order Value |

[block:callout]
{
  "type": "warning",
  "body": "If you use integrations that consume price data, such as checkout or order integrations, note that the field `sellingPrice` may be subject to rounding discrepancies. We recommend retrieving data from the `priceDefinition` data structure instead."
}
[/block]