---
title: "Get current or create a new cart"
slug: "create-a-new-cart"
hidden: false
createdAt: "2022-10-10T19:19:27.723Z"
updatedAt: "2022-11-17T12:27:20.530Z"
---
The shopping cart is where the information on the products chosen by the customer while browsing a store is gathered. This data may include item prices, shipping value, payment, and delivery methods, among others.

This guide will describe how to get the information of your current shopping cart (`orderFormId`) or to create a new cart with the API.

## Accessing current shopping cart information

To access your current shopping cart information, you must use the [Get current or create a new cart](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/orderForm) endpoint. In this request, it is not required to send any additional information (path params, query, or body). See this URL example:

`https://{accountName}.{environment}.com.br/api/checkout/pub/orderForm`

After sending the request, the endpoint will return the response body containing the information of your current shopping cart, as shown in the example below:

```json
{
    "orderFormId": "11c257869e444e7185e61cab475f91bd",
    "salesChannel": "1",
    "loggedIn": false,
    "isCheckedIn": false,
    "storeId": null,
    "checkedInPickupPointId": null,
    "allowManualPrice": false,
    "canEditData": true,
    "userProfileId": null,
    "userType": null,
    "ignoreProfileData": false,
    "value": 0,
    "messages": [],
   "items": [
        {
            "uniqueId": "D1E0949706A3441DA0386929FAB6E7E8",
            "id": "2005",
            "productId": "3",
            "productRefId": "",
            "refId": null,
            "ean": "978020137962",
            "name": "Weightless Waves Mild Lather Cleanser 50 ml",
            "skuName": "50 ml",
            "modalType": null,
            "parentItemIndex": null,
            "parentAssemblyBinding": null,
            "assemblies": [],
            "priceValidUntil": "2023-11-07T22:14:44Z",
            "tax": 0,
            "price": 3190,
            "listPrice": 3190,
            "manualPrice": null,
            "manualPriceAppliedBy": null,
            "sellingPrice": 3107,
            "rewardValue": 0,
            "isGift": false,
            "additionalInfo": {
                "dimension": null,
                "brandName": "VALDIE&CO",
                "brandId": "2000000",
                "offeringInfo": null,
                "offeringType": null,
                "offeringTypeId": null
            },
            "preSaleDate": null,
            "productCategoryIds": "/2/",
            "productCategories": {
                "2": "Computers"
            },
            "quantity": 3,
            "seller": "cosmetics1",
            "sellerChain": [
                "cosmetics1"
            ],
            "imageUrl": "http://cosmetics2.vteximg.com.br/arquivos/ids/155401-55-55/ID-001-MAIN.jpg?v=637109313796670000",
            "detailUrl": "/weightless-waves-mild-lather-cleanser/p",
            "components": [],
            "bundleItems": [],
            "attachments": [],
            "attachmentOfferings": [],
            "offerings": [],
            "priceTags": [
                {
                    "name": "discount@price-0e45a4e3-6084-4bf9-bff7-0fe8403699fc#ac2d3d37-5845-45a6-9254-191449d6f100",
                    "value": -416,
                    "rawValue": -4.160,
                    "isPercentual": false,
                    "identifier": "0e45a4e3-6084-4bf9-bff7-0fe8403699fc",
                    "owner": "cosmetics2"
                }
            ],
            "availability": "available",
            "measurementUnit": "un",
            "unitMultiplier": 1.0000,
            "manufacturerCode": null,
            "priceDefinition": {
                "calculatedSellingPrice": 3107,
                "total": 15534,
                "sellingPrices": [
                    {
                        "value": 3107,
                        "quantity": 4
                    },
                    {
                        "value": 3106,
                        "quantity": 1
                    }
                ]
            }
        },
...
```

> ℹ️️ If you want access to a specific shopping cart (other than your current one) and you already know its `orderFormId`, you can find it through the [Get cart information by ID](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/orderForm/-orderFormId-) endpoint. See more information at [Get cart information by ID](https://developers.vtex.com/docs/guides/get-cart-information-by-id#accessing-shopping-cart-information) guide.


## Creating the new shopping cart

To create a new shopping cart, in the same way that to obtain the information of the current cart, you must use the [Get current or create a new cart](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/orderForm) endpoint. However, in this request, you must also send the query parameter `forceNewCart = true`, as shown in this URL example:

`https://{accountName}.{environment}.com.br/api/checkout/pub/orderForm?forceNewCart=true`

After sending the request, the endpoint will return the response body containing the information about the new shopping cart created, as shown in the example below:

```json
{
    "orderFormId": "ede846222cd44046ba6c638442c3505a",
    "salesChannel": "1",
    "loggedIn": false,
    "isCheckedIn": false,
    "storeId": null,
    "checkedInPickupPointId": null,
    "allowManualPrice": false,
    "canEditData": true,
    "userProfileId": null,
    "userType": null,
    "ignoreProfileData": false,
    "value": 0,
    "messages": [],
    "items": [],
    "selectableGifts": [],
    "totalizers": [],
    "shippingData": null,
    "clientProfileData": {
        "email": null,
        "firstName": null,
        "lastName": null,
        "document": null,
        "documentType": null,
        "phone": null,
        "corporateName": null,
        "tradeName": null,
        "corporateDocument": null,
        "stateInscription": null,
        "corporatePhone": null,
        "isCorporate": false,
        "profileCompleteOnLoading": null,
        "profileErrorOnLoading": null,
        "customerClass": null
    },
...
```

> ℹ️️ For more information about the meaning of each of the fields available in the shopping cart, access the [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) overview.


## Error codes

The following error may appear as a message in the response body.

### 404 - Not Found

- `Message error example: "The requested URL was not found on the server"`: check that the URL data is correct.

```html
<body>
	<h1>404 Not Found</h1>
	<p>The requested URL was not found on this server.</p>
</body>
```
