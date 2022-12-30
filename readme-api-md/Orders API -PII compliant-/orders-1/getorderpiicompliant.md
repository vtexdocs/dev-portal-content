---
title: "Get order"
slug: "getorderpiicompliant"
excerpt: "Retrieve order details by searching a specific order ID.\n\r\n\r>If you wish to retrieve unmasked data, use the `reason` parameter.\n\r\n\r> The `View order` resource is needed to use this API request. This is included in `OMS - Full access` and `IntegrationProfile - Fulfillment Oms`, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#)."
hidden: true
createdAt: "2022-04-26T15:47:38.588Z"
updatedAt: "2022-04-26T19:48:36.927Z"
---
## Throtling
[block:html]
{
  "html": "<div class=\"alert alert-info\">Throttling: Each account can make up to 5000 requests per minute.\n</div>"
}
[/block]

## Request body example

```json
curl --location --request GET 'https://{{accountName}}.{{environment}}.com.br/api/oms/pvt/orders/v5195004lux-01' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \
--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'
```

## Response body example

```json
{
  "emailTracked": "a27499cad31f42b7a771ae34f57c8358@ct.vtex.com.br",
  "approvedBy": null,
  "cancelledBy": null,
  "cancelReason": null,
  "orderId": "v5195004lux-01",
  "sequence": "502556",
  "marketplaceOrderId": "",
  "marketplaceServicesEndpoint": "http://oms.vtexinternal.com.br/api/oms?an=luxstore",
  "sellerOrderId": "00-v5195004lux-01",
  "origin": "Marketplace",
  "affiliateId": "",
  "salesChannel": "1",
  "merchantName": null,
  "status": "handling",
  "statusDescription": "Preparando Entrega",
  "value": 1160,
  "creationDate": "2019-01-28T20:09:43.8999580+00:00",
  "lastChange": "2019-02-06T20:46:11.7010747+00:00",
  "orderGroup": null,
  "totals": [
    {
      "id": "Items",
      "name": "Total dos Itens",
      "value": 3290
    },
    {
      "id": "Discounts",
      "name": "Total dos Descontos",
      "value": 0
    },
    {
      "id": "Shipping",
      "name": "Total do Frete",
      "value": 1160
    },
    {
      "id": "Tax",
      "name": "Total da Taxa",
      "value": 0
    },
    {
      "id": "Change",
      "name": "Total das mudanças",
      "value": -3290
    }
  ],
  "items": [
    {
      "uniqueId": "87F0945396994B349158C7D9C9941442",
      "id": "1234568358",
      "productId": "9429485",
      "ean": null,
      "lockId": "00-v5195004lux-01",
      "itemAttachment": {
        "content": {},
        "name": null
      },
      "attachments": [],
      "quantity": 1,
      "seller": "1",
      "name": "Bay Max L",
      "refId": "BIGHEROBML",
      "price": 3290,
      "listPrice": 3290,
      "manualPrice": null,
      "priceTags": [],
      "imageUrl": "http://luxstore.vteximg.com.br/arquivos/ids/159263-55-55/image-cc1aed75cbfa424a85a94900be3eacec.jpg?v=636795432619830000",
      "detailUrl": "/bay-max-9429485/p",
      "components": [],
      "bundleItems": [],
      "params": [],
      "offerings": [],
      "sellerSku": "1234568358",
      "priceValidUntil": null,
      "commission": 0,
      "tax": 0,
      "preSaleDate": null,
      "additionalInfo": {
        "brandName": "VTEX",
        "brandId": "2000023",
        "categoriesIds": "/1/",
        "productClusterId": "135,142",
        "commercialConditionId": "5",
        "dimension": {
          "cubicweight": 0.7031,
          "height": 15,
          "length": 15,
          "weight": 15,
          "width": 15
        },
        "offeringInfo": null,
        "offeringType": null,
        "offeringTypeId": null
      },
      "measurementUnit": "un",
      "unitMultiplier": 1,
      "sellingPrice": 3290,
      "isGift": false,
      "shippingPrice": null,
      "rewardValue": 0,
      "freightCommission": 0,
      "priceDefinition": {
        "sellingPrice": [
          {
             "quantity": 1,
             "value": 3290,
          }
        ],
        "total": 3290     
      },
      "taxCode": null,
      "parentItemIndex": null,
      "parentAssemblyBinding": null
    }
  ],
  "marketplaceItems": [],
  "clientProfileData": {
    "id": "clientProfileData",
    "email": "rodrigo.cunha@vtex.com.br",
    "firstName": "Rodrigo",
    "lastName": "VTEX",
    "documentType": "cpf",
    "document": "11047867702",
    "phone": "+5521972321094",
    "corporateName": null,
    "tradeName": null,
    "corporateDocument": null,
    "stateInscription": null,
    "corporatePhone": null,
    "isCorporate": false,
    "userProfileId": "5a3692de-358a-4bea-8885-044bce33bb93",
    "customerClass": null
  },
  "giftRegistryData": null,
  "marketingData": null,
  "ratesAndBenefitsData": {
    "id": "ratesAndBenefitsData",
    "rateAndBenefitsIdentifiers": []
  },
  "shippingData": {
    "id": "shippingData",
    "address": {
      "addressType": "residential",
      "receiverName": "Rodrigo Cunha",
      "addressId": "-1425945657910",
      "postalCode": "22250-040",
      "city": "Rio de Janeiro",
      "state": "RJ",
      "country": "BRA",
      "street": "Praia de Botafogo",
      "number": "300",
      "neighborhood": "Botafogo",
      "complement": "3",
      "reference": null,
      "geoCoordinates": []
    },
    "logisticsInfo": [
      {
        "itemIndex": 0,
        "selectedSla": "Normal",
        "lockTTL": "10d",
        "price": 1160,
        "listPrice": 1160,
        "sellingPrice": 1160,
        "deliveryWindow": null,
        "deliveryCompany": "Todos os CEPS",
        "shippingEstimate": "5bd",
        "shippingEstimateDate": "2019-02-04T20:33:46.4595004+00:00",
        "slas": [
          {
            "id": "Normal",
            "name": "Normal",
            "shippingEstimate": "5bd",
            "deliveryWindow": null,
            "price": 1160,
            "deliveryChannel": "delivery",
            "pickupStoreInfo": {
              "additionalInfo": null,
              "address": null,
              "dockId": null,
              "friendlyName": null,
              "isPickupStore": false
            },
            "polygonName": null
          },
          {
            "id": "Expressa",
            "name": "Expressa",
            "shippingEstimate": "5bd",
            "deliveryWindow": null,
            "price": 1160,
            "deliveryChannel": "delivery",
            "pickupStoreInfo": {
              "additionalInfo": null,
              "address": null,
              "dockId": null,
              "friendlyName": null,
              "isPickupStore": false
            },
            "polygonName": null
          },
          {
            "id": "Quebra Kit",
            "name": "Quebra Kit",
            "shippingEstimate": "2bd",
            "deliveryWindow": null,
            "price": 1392,
            "deliveryChannel": "delivery",
            "pickupStoreInfo": {
              "additionalInfo": null,
              "address": null,
              "dockId": null,
              "friendlyName": null,
              "isPickupStore": false
            },
            "polygonName": null
          },
          {
            "id": "Sob Encomenda",
            "name": "Sob Encomenda",
            "shippingEstimate": "32bd",
            "deliveryWindow": null,
            "price": 1392,
            "deliveryChannel": "delivery",
            "pickupStoreInfo": {
              "additionalInfo": null,
              "address": null,
              "dockId": null,
              "friendlyName": null,
              "isPickupStore": false
            },
            "polygonName": null
          }
        ],
        "shipsTo": [
          "BRA"
        ],
        "deliveryIds": [
          {
            "courierId": "197a56f",
            "courierName": "Todos os CEPS",
            "dockId": "1",
            "quantity": 1,
            "warehouseId": "1_1"
          }
        ],
        "deliveryChannel": "delivery",
        "pickupStoreInfo": {
          "additionalInfo": null,
          "address": null,
          "dockId": null,
          "friendlyName": null,
          "isPickupStore": false
        },
        "addressId": "-1425945657910",
        "polygonName": null
      }
    ],
    "trackingHints": null,
    "selectedAddresses": [
      {
        "addressId": "-1425945657910",
        "addressType": "residential",
        "receiverName": "Rodrigo Cunha",
        "street": "Praia de Botafogo",
        "number": "518",
        "complement": "10",
        "neighborhood": "Botafogo",
        "postalCode": "22250-040",
        "city": "Rio de Janeiro",
        "state": "RJ",
        "country": "BRA",
        "reference": null,
        "geoCoordinates": []
      }
    ]
  },
  "paymentData": {
    "transactions": [
      {
        "isActive": true,
        "transactionId": "418213DE29634837A63DD693A937A696",
        "merchantName": "luxstore",
        "payments": [
          {
            "id": "D3DEECAB3C6C4B9EAF8EF4C1FE062FF3",
            "paymentSystem": "6",
            "paymentSystemName": "Boleto Bancário",
            "value": 4450,
            "installments": 1,
            "referenceValue": 4450,
            "cardHolder": null,
            "firstDigits": null,
            "lastDigits": null,
            "url": "https://luxstore.vtexpayments.com.br:443/BankIssuedInvoice/Transaction/418213DE29634837A63DD693A937A696/Payment/D3DEECAB3C6C4B9EAF8EF4C1FE062FF3/Installment/{Installment}",
            "giftCardId": null,
            "giftCardName": null,
            "giftCardCaption": null,
            "redemptionCode": null,
            "group": "bankInvoice",
            "tid": null,
            "dueDate": "2019-02-02",
            "connectorResponses": {},
            "billingAddress": {
                  "postalCode": "00000-000",
                  "city": "Rio de Janeiro",
                  "state": "RJ",
                  "country": "BRA",
                  "street": "Avenida Vice-Presidente José Alencar",
                  "number": "0000",
                  "neighborhood": "Jacarepaguá",
                  "complement": null,
                  "reference": null,
                  "geoCoordinates": [
                       -43.386474609375,
                       -22.965709686279297
                  ]
             }
          }
        ]
      }
    ]
  },
  "packageAttachment": {
    "packages": []
  },
  "sellers": [
    {
      "id": "1",
      "name": "Loja do Suporte",
      "logo": ""
    }
  ],
  "callCenterOperatorData": null,
  "followUpEmail": "7bf3a59bbc56402c810bda9521ba449e@ct.vtex.com.br",
  "lastMessage": null,
  "hostname": "luxstore",
  "invoiceData": null,
  "changesAttachment": {
    "id": "changeAttachment",
    "changesData": [
      {
        "reason": "Blah",
        "discountValue": 3290,
        "incrementValue": 0,
        "itemsAdded": [],
        "itemsRemoved": [
          {
            "id": "1234568358",
            "name": "Bay Max L",
            "quantity": 1,
            "price": 3290,
            "unitMultiplier": null
          }
        ],
        "receipt": {
          "date": "2019-02-06T20:46:04.4003606+00:00",
          "orderId": "v5195004lux-01",
          "receipt": "029f9ab8-751a-4b1e-bf81-7dd25d14b49b"
        }
      }
    ]
  },
  "openTextField": null,
  "roundingError": 0,
  "orderFormId": "caae7471333e403f959fa5fd66951340",
  "commercialConditionData": null,
  "isCompleted": true,
  "customData": null,
  "storePreferencesData": {
    "countryCode": "BRA",
    "currencyCode": "BRL",
    "currencyFormatInfo": {
      "CurrencyDecimalDigits": 2,
      "CurrencyDecimalSeparator": ",",
      "CurrencyGroupSeparator": ".",
      "CurrencyGroupSize": 3,
      "StartsWithCurrencySymbol": true
    },
    "currencyLocale": 1046,
    "currencySymbol": "R$",
    "timeZone": "E. South America Standard Time"
  },
  "allowCancellation": false,
  "allowEdition": false,
  "isCheckedIn": false,
  "marketplace": {
    "baseURL": "http://oms.vtexinternal.com.br/api/oms?an=luxstore",
    "isCertified": null,
    "name": "luxstore"
  },
  "authorizedDate": "2019-01-28T20:33:04.0000000+00:00",
  "invoicedDate": null
}
```

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
| `dimension` | string | Item dimension object |
| `cubicweight` | string | Item cubic weight |
| `height` | string | Item height |
| `length` | string | Item length |
| `weight` | string | Item weight |
| `width` | string | Item width |
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