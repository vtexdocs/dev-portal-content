---
title: "Setting up white label seller as pickup point"
slug: "setting-up-white-label-seller-as-pickup-point"
hidden: false
createdAt: "2023-07-25T20:30:14.043Z"
updatedAt: "2023-07-25T20:30:14.127Z"
---

Every [franchise account](https://help.vtex.com/en/tutorial/what-is-a-franchise-account--kWQC6RkFSCUFGgY5gSjdl) created in VTEX is also automatically a [white label seller](https://help.vtex.com/en/tutorial/white-label-seller--5orlGHyDHGAYciQ64oEgKa) of the main account. So any [pickup points](https://help.vtex.com/en/tutorial/pickup-points--2fljn6wLjn8M4lJHA6HP3R) configured in the franchise account will be available options for shoppers who place orders in the main account.

>❗ Items will only be displayed at Checkout for shoppers with the pickup point option if the SKU is available in the inventory of the main account and also in the inventory of the franchise account.

## Initial setup

To set up a white label seller as a pickup point, you have to make the following configurations:

- [Pickup point](https://help.vtex.com/en/tutorial/creating-pickup-points--2R5ClQiwe4KoSQgsuiOw4E): create the pickup point with the franchise account address. You can use the [Create/Update Pickup Point](https://developers.vtex.com/docs/api-reference/logistics-api#put-/api/logistics/pvt/configuration/pickuppoints/-pickupPointId-) endpoint.
- [Shipping policy](https://help.vtex.com/en/tutorial/shipping-policy--tutorials_140): set up a shipping policy and link it to a registered pickup point. You can use the [Create shipping policy](https://developers.vtex.com/docs/api-reference/logistics-api#post-/api/logistics/pvt/shipping-policies) endpoint.
- [Loading dock](https://help.vtex.com/en/tutorial/managing-loading-docks--7K3FultD8I2cuuA6iyGEiW): configure a loading dock and link it to the shipping policy associated with the pickup point. You can use the [Create/update dock](https://developers.vtex.com/docs/api-reference/logistics-api#post-/api/logistics/pvt/configuration/docks) endpoint.
- [Warehouse](https://help.vtex.com/en/tutorial/managing-warehouses--tutorials_137): you must configure a warehouse and link it to the shipping policy associated with the pickup point. You can use the [Create/update warehouse](https://developers.vtex.com/docs/api-reference/logistics-api#post-/api/logistics/pvt/configuration/warehouses) endpoint.

## Fill in inventory quantity

After setting the pickup point, the shipping policy, the loading dock, and the warehouse, fill in the quantity of the items in inventory. You can also use the [Update inventory by SKU and warehouse](https://developers.vtex.com/docs/api-reference/logistics-api#put-/api/logistics/pvt/inventory/skus/-skuId-/warehouses/-warehouseId-) endpoint.

The franchise account does not have its own catalogue, it inherits products and SKU information from the main account, so it is necessary to update quantity through the [import and export of the inventory spreadsheet](https://help.vtex.com/en/tutorial/importing-and-exporting-an-inventory-spreadsheet--tutorials_2034).

## Validate configuration

When you made the pickup point configurations correctly in the franchise account, SKUs with inventory and price can be sold on the main account. The franchise account will work as white label seller and the main account will work as marketplace.

>❗ Make sure your white label seller is active. In your VTEX Admin, go to __Marketplace > Sellers > Management__, and in the seller row in column _Status_, click `Active`.

### White label seller and franchise account

To check if the white label seller, which is the franchise account, is delivering a SKU through the registered pickup point, use the [Cart simulation endpoint](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForms/simulation).

__POST__ - `https://{accountName}.{environment}.com.br/api/checkout/pub/orderForms/simulation`

#### Request body example

```json
{
  "items": [
    {
      "id": "1",
      "quantity": 1,
      "seller": "1"
    }
  ],
  "country": "BRA",
  "postalCode": "12345-000",
  "geoCoordinates": [
    -47.924747467041016
  ]
}
```

#### Response body example

```json
{
  "items": [
    {
      "id": "1",
      "requestIndex": 0,
      "quantity": 1,
      "seller": "1",
      "sellerChain": [
        "1"
      ],
      "tax": 0,
      "priceValidUntil": "2023-07-12T11:49:01Z",
      "price": 9999,
      "listPrice": 9999,
      "rewardValue": 0,
      "sellingPrice": 2999700,
      "offerings": [],
      "priceTags": [
        {
          "name": "DISCOUNT@MANUALPRICE",
          "value": -5000,
          "rawValue": -50,
          "isPercentual": false,
          "identifier": "1234abc-5678b-1234c"
        }
      ],
      "measurementUnit": "un",
      "unitMultiplier": 300,
      "parentItemIndex": null,
      "parentAssemblyBinding": null,
      "availability": "available",
      "priceDefinition": {
        "calculatedSellingPrice": 2999700,
        "total": 2999700,
        "sellingPrices": [
          {
            "value": 2999700,
            "quantity": 1
          }
        ]
      }
    }
  ],
  "ratesAndBenefitsData": {
    "rateAndBenefitsIdentifiers": [],
    "teaser": []
  },
  "paymentData": {
    "installmentOptions": [
      {
        "paymentSystem": "2",
        "bin": null,
        "paymentName": "Visa",
        "paymentGroupName": "creditCardPaymentGroup",
        "value": 2999700,
        "installments": [
          {
            "count": 1,
            "hasInterestRate": false,
            "interestRate": 0,
            "value": 2999700,
            "total": 2999700,
            "sellerMerchantInstallments": [
              {
                "id": "brenoStore",
                "count": 1,
                "hasInterestRate": false,
                "interestRate": 0,
                "value": 2999700,
                "total": 2999700
              }
            ]
          }
        ]
      }
    ],
    "paymentSystems": [
      {
        "id": 2,
        "name": "Visa",
        "groupName": "creditCardPaymentGroup",
        "validator": null,
        "stringId": "2",
        "template": "creditCardPaymentGroup-template",
        "requiresDocument": false,
        "displayDocument": false,
        "isCustom": false,
        "description": "",
        "requiresAuthentication": false,
        "dueDate": "2022-07-19T11:39:36.37197Z",
        "availablePayments": null
      }
    ],
    "payments": [],
    "giftCards": [],
    "giftCardMessages": [],
    "availableAccounts": [],
    "availableTokens": [],
    "availableAssociations": {}
  },
  "selectableGifts": [],
  "marketingData": {
    "utmSource": "app",
    "utmMedium": "CPC",
    "utmCampaign": "Black friday",
    "utmipage": "true",
    "utmiPart": "true",
    "utmiCampaign": "true",
    "coupon": null,
    "marketingTags": [
      "tag1",
      "tag2"
    ]
  },
  "country": "BRA",
  "postalCode": "12345-000",
  "geoCoordinates": [
    -47.924747467041016,
    -15.832582473754883
  ],
  "logisticsInfo": [
    {
      "itemIndex": 0,
      "addressId": null,
      "selectedSla": null,
      "selectedDeliveryChannel": null,
      "quantity": 1,
      "shipsTo": [
        "BRA"
      ],
      "slas": [],
      "deliveryChannels": [
        {
          "id": "pickup-in-point"
        }
      ]
    }
  ],
  "messages": [],
  "purchaseConditions": {
    "itemPurchaseConditions": [
      {
        "id": "1",
        "seller": "1",
        "sellerChain": [
          "1"
        ],
        "slas": [
          {
            "id": "Normal",
            "deliveryChannel": "delivery",
            "name": "Normal",
            "deliveryIds": [
              {
                "courierId": "1",
                "warehouseId": "1_1",
                "dockId": "1",
                "courierName": "Transportadora",
                "quantity": 1,
                "kitItemDetails": []
              }
            ],
            "shippingEstimate": "3bd",
            "shippingEstimateDate": null,
            "lockTTL": "10d",
            "availableDeliveryWindows": {
              "startDateUtc": "2017-03-27T00:00:00+00:00",
              "endDateUtc": "2017-03-27T00:00:00+00:00",
              "price": 0,
              "lisPrice": 0,
              "tax": 0
            },
            "deliveryWindow": {
              "startDateUtc": "2014-04-21T09:00:00+00:00",
              "endDateUtc": "2014-04-21T12:00:00+00:00",
              "price": 0,
              "listprice": 1000,
              "tax": 0
            },
            "price": 1500,
            "listPrice": 1500,
            "tax": 0,
            "pickupStoreInfo": {
              "isPickupStore": false,
              "friendlyName": null,
              "address": null,
              "additionalInfo": null,
              "dockId": null
            },
            "pickupPointId": null,
            "pickupDistance": 0,
            "polygonName": null,
            "transitTime": "3bd"
          }
        ],
        "price": 9999,
        "listPrice": 9999
      }
    ]
  },
  "pickupPoints": [
    {
            "friendlyName": "Locker Arizona",
            "address": {
                "addressType": "pickup",
                "receiverName": null,
                "addressId": "1cc6116",
                "postalCode": "85004",
                "city": "Phoenix",
                "state": "AZ",
                "country": "USA",
                "street": "North 3rd Street",
                "number": "752",
                "neighborhood": "Downtown",
                "complement": "",
                "reference": null,
                "geoCoordinates": [
                    3345.231544494628906,
                    -11206.918148040771484
                ]
            },
            "additionalInfo": "Bring your ID",
            "id": "1cc6116",
            "businessHours": []
        }
  ],
  "subscriptionData": null,
  "totals": [
    {
      "id": "Items",
      "name": "Total dos Itens",
      "value": 2999700
    }
  ],
  "itemMetadata": {
    "items": []
  }
```

When the configuration was made correctly, the call will return the shipping information of a given SKU. That is enough to check if the shipping is occurring by the registered pickup point.

### Marketplace and main account

To check if the main account, which is the marketplace, is including the SKU of the white label seller in the shopping cart, use the same [Cart simulation](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForms/simulation) endpoint mentioned in the previous section.

Fill in the `id` field of the [request body](#request-body-example) with the SKU ID sold by the white label seller and make sure to use a shipping address covered by your logistic operation. The [response body](#response-body-example) you will get should display valid shopping cart information, which shows that the SKU is been sold by the main account as well.
