---
title: "Promotion Provider Middleware"
slug: "vtex-promotion-provider-middleware"
excerpt: "vtex.promotion-provider-middleware@0.24.3"
hidden: true
createdAt: "2022-07-19T21:54:46.416Z"
updatedAt: "2022-07-21T21:41:29.276Z"
---
This app allows external providers to apply promotions to any SKUs in the shopping cart during an end-user checkout experience.

## Getting Started

You can install it through the command-line interface:

```
vtex install vtex.promotion-provider-middleware@0.x
```

Right after installation, the external endpoint needs to be set. To make this configuration, go to the page `https://{{accountName}}.myvtex.com/admin/apps` , search for `Promotion Provider Middleware`, click on the Settings button, set the External Endpoint and save your configurations.

Upon saving the settings, this application will set the whole environment to comply with its necessities, meaning that the following actions will be done automatically by the app:

* `allowManualPrice` will be set to `true` in the [orderForm Configurations](https://developers.vtex.com/vtex-rest-api/reference/configuration#getorderformconfiguration);
* Create a new object in the `apps` array at [orderForm Configurations](https://developers.vtex.com/vtex-rest-api/reference/configuration#getorderformconfiguration), this allows your promotions data to be stored in the customData object (inside orderForm) for every order.

Upon installing, the public routes will become instantly available to use.

It's worth mentioning that Order Authorization configurations could interfere with key functional aspects of this application. If the account has any Manual Discount rules configured, make sure to verify if the promotions applied by the external provider comply with the range set in Manual Discount rules. The reason for the impact is that this application makes use of [Update cart items](https://developers.vtex.com/vtex-rest-api/reference/cart-update#itemsupdate) to apply discounts.

## Syntax and Supported Routes

### Notification:
`POST /_v/promotion-provider/notification`

This route is responsible for consulting the external provider and applying the discounts afterwards.

All this route needs to be initiated is the cookie `checkout.vtex.com` containing the orderformId in the format `__ofid={{orderFormId}}`. After receiving this cookie in the headers, the middleware will go through the following steps:

* Fetch the orderForm through the orderFormId sent inside the cookie;
* Clean all manual prices currently active in the orderForm;
* Parse the orderForm according to the protocol (more details later on);
* Send the payload to the external provider.

> 🔎 It is worth mentioning that there's a 12.5 seconds timeout attributed to the external provider with 0 retries. Meaning that the external provider has this exact time to deliver a response to our application.
The object sent to the external provider looks like the following:
> Observation: The objects customData, shippingData, clientProfileData, paymentData are exactly the same as seen in the orderForm.
```typescript
interface ExternalPromotionsRequestProtocol {
  items: {
    id: string
    productId: string
    refId?: any
    ean: string
    name: string
    skuName: string
    modalType?: any
    productCategoryIds: string
    productCategories: ProductCategories
    availability: string
    measurementUnit: string
    variations: {
      index: number
      assemblies: any[]
      tax: number
      price: number
      listPrice: number
      manualPrice?: any
      sellingPrice: number
      isGift: boolean
      quantity: number
      attachments: Attachment[]
      attachmentOfferings: AttachmentOffering[]
      offerings: any[]
      priceTags: PriceTag[]
      unitMultiplier: number
      seller: string
      sellerChain: string[]
    }[]
  }[]
  customData: CustomData
  shippingData: ShippingData
  clientProfileData: ClientProfileData
  marketingData?: MarketingData
  paymentData: PaymentData
  totalizers: {
    id: string
    name: string
    value: number
  }[]
}
```

When it comes to the external provider response, we expect the following objects (example at the end of this documentation):

```typescript
interface ExternalPromotionsResponseProtocol {
  items: {
    id: number
    variations: {
      requestIndex: number
      quantity: number
      externalPromotions: {
        matchedParameters: {[key: string]: string}
        identifier: string
        isPercentual: boolean
        value: number
      }[]
    }[]
  }[]
}
```

It's important to notice that in cases where `isPercentual` is `true`, the `value` property should contain numbers between `0` and `1`, for example: `0.35`. If `isPercentual` is `false`, the `value` property should have negative values such as `-100` or `-2500` for a nominal discount of $1,00 and $25,00 respectively.

The `requestIndex` field (present in the external provider response) should match the index from the payload sent while also respecting it's variations. If the payload sent has 3 SKU's, but 1 SKU has 2 variations (due to split index), then your request index could vary from 0 to 4. If this is not respected, the middleware will throw an error and not apply any discount.

> 🚨 Warning: The `items` array (present in the external provider response) should <strong>only</strong> contain the items that will be affected by any promotion. If no items should be impacted, then the `items` array should be sent empty.

Another important observation is that the discount will be applied over the summed `price` of the skuId based on its quantity. Also worth mentioning that percentual discounts will be applied first and nominal discounts afterwards.

> ❗ Reminder: We are talking about the `price` property as found in the orderForm, we are <strong>not</strong> talking about `sellingPrice` nor `listPrice`.

The `matchedParameters` property should have `key` and `value` as strings with a maximum of 50 characters.

After the external provider response, if it all went well, the middleware will use the API [Update cart items](https://developers.vtex.com/vtex-rest-api/reference/cart-update#itemsupdate) to update the prices in the cart respecting the discounts sent.

An important reminder, every promotion configured in the promotions module is equipped with a flag called `Allows accumulate with manual prices`, if this flag is checked, first the external promotion will be applied, and only then the other promotions will apply. If this flag remains unchecked, when the external promotion gets applied, the respective promotion will not be applied.

### Simulation:
`POST /_v/promotion-provider/simulation`

This route is only responsible for consulting the external provider, and <strong>does not</strong> apply discounts.

In order to put this route in use, all you need to do is send a request body containing the `items` array, which for this route is exactly the same as it is in the orderForm.

Besides the `items` array, you could also send `customData`, `shippingData`, `clientProfileData`, `marketingData`, `paymentData`.

> Observation: The only field required in this request is the `id` property inside each object present in the `items` array.

## External Provider Response Example (Response Body):

```json
{
    "items": [
        {
            "id": 33, //required
            "variations": [
                {
                    "requestIndex": 0, //required
                    "quantity": 1, //required
                    "externalPromotions": [
                        {
                            "matchedParameters": {
                                "slaIds": "transportadora genérica"
                            },
                            "identifier": "anyName",
                            "isPercentual": false, //required
                            "value": -200 //required
                        },
                        {
                            "matchedParameters": {
                                "skuId": "33"
                            },
                            "identifier": "10off",
                            "isPercentual": true, //required
                            "value": 0.10 //required
                        }
                    ]
                },
                {
                    "requestIndex": 1, //required
                    "quantity": 1, //required
                    "externalPromotions": [
                        {
                            "isPercentual": true, //required
                            "value": 0.50 //required
                        }
                    ]
                }
            ]
        }
    ]
}
```