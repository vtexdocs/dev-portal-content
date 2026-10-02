---
title: "orderForm fields reference"
slug: "orderform-fields"
hidden: false
createdAt: "2020-09-02T13:59:41.676Z"
updatedAt: "2026-10-02T00:00:00.000Z"
excerpt: "Reference of all orderForm fields returned by the Checkout API, organized by section, with descriptions, types, and examples."
---

The `orderForm` is the main object processed by VTEX Checkout and one of the most important data structures in every VTEX architecture's store. It represents a shopping cart and stores all the contextual information needed to turn that cart into an order: the items, the customer's profile, delivery and pickup options, payment options, promotions, and custom information.

The [Checkout API](https://developers.vtex.com/docs/api-reference/checkout-api) is the main interface for reading and changing the `orderForm`. Most of its endpoints return the complete `orderForm` in the response body.

This guide describes every field of the `orderForm`, grouped by section. Each section includes a description of its purpose, a JSON example, and a table with the type, description, and an example value of each field.

## Conventions used in this guide

- **Monetary values:** All fields that represent monetary values are integers in **cents**, without a decimal separator. For example, `10390` represents R$ 103.90 in a Brazilian store, and `2499` represents $24.99 in a US store.
- **Nested fields:** Field names in the tables use dot notation relative to the section. `[]` indicates that the field belongs to each object of an array. For example, `logisticsInfo[].slas[].price` is the `price` field of each SLA, inside each element of the `logisticsInfo` array.
- **Nullable fields:** When a field can return `null`, the type column says so (for example, `String or null`). Fields related to the customer, such as addresses and profile data, are often `null` until the customer identifies themselves.
- **Masked data:** When the customer hasn't been authenticated, personal data, such as names, documents, phone numbers, and addresses, is returned partially masked with asterisks (for example, `"Cla** ***t"`) to protect the shopper's privacy.

## orderForm structure

The `orderForm` is composed of root fields, which describe the cart as a whole, and **sections**, which are objects or arrays that group related information.

```json
{
  "orderFormId": "9ceee0fde6db489fbc682a0e2ab13a86",
  "salesChannel": "1",
  "loggedIn": false,
  "isCheckedIn": false,
  "storeId": null,
  "allowManualPrice": false,
  "canEditData": true,
  "userProfileId": null,
  "profileProvider": "Vtex",
  "availableAccounts": [],
  "availableAddresses": [],
  "userType": null,
  "ignoreProfileData": false,
  "value": 16500,
  "messages": [],
  "items": [],
  "selectableGifts": [],
  "totalizers": [],
  "shippingData": {},
  "clientProfileData": {},
  "paymentData": {},
  "marketingData": {},
  "sellers": [],
  "clientPreferencesData": {},
  "commercialConditionData": null,
  "storePreferencesData": {},
  "giftRegistryData": null,
  "openTextField": null,
  "invoiceData": null,
  "customData": null,
  "itemMetadata": {},
  "hooksData": null,
  "ratesAndBenefitsData": {},
  "subscriptionData": null,
  "itemsOrdination": null
}
```

The sections are organized in this guide by subject:

| Subject | Sections |
| - | - |
| [Cart and items](#cart-and-items) | [items](#items), [itemMetadata](#itemmetadata), [itemsOrdination](#itemsordination), [selectableGifts](#selectablegifts), [sellers](#sellers), [totalizers](#totalizers) |
| [Customer](#customer) | [clientProfileData](#clientprofiledata), [clientPreferencesData](#clientpreferencesdata), [giftRegistryData](#giftregistrydata) |
| [Shipping](#shipping) | [shippingData](#shippingdata) |
| [Payment and invoice](#payment-and-invoice) | [paymentData](#paymentdata), [invoiceData](#invoicedata) |
| [Promotions and marketing](#promotions-and-marketing) | [marketingData](#marketingdata), [ratesAndBenefitsData](#ratesandbenefitsdata) |
| [Custom information](#custom-information) | [customData](#customdata), [openTextField](#opentextfield), [hooksData](#hooksdata) |
| [Store and commercial context](#store-and-commercial-context) | [storePreferencesData](#storepreferencesdata), [commercialConditionData](#commercialconditiondata), [subscriptionData](#subscriptiondata) |
| [Server messages](#server-messages) | [messages](#messages) |

## Root fields

Root fields are located directly in the `orderForm` object and describe the cart as a whole: its identification, the sales channel, the shopper's session state, and the total order value.

| Field | Type | Description | Example |
| - | - | - | - |
| `orderFormId` | String | ID of the `orderForm` corresponding to a specific cart. Use this ID in the path of the Checkout API endpoints to read or change the cart. | `"9ceee0fde6db489fbc682a0e2ab13a86"` |
| `salesChannel` | String | ID of the [sales channel (trade policy)](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV) associated with the cart, as configured in the store. It defines the prices, promotions, and catalog available to the shopper. | `"1"` |
| `loggedIn` | Boolean | Indicates whether the user is logged into the store. | `false` |
| `isCheckedIn` | Boolean | Indicates whether the cart is checked in to a physical store, which is used in in-store sales scenarios. | `false` |
| `storeId` | String or null | ID of the physical store where the cart is checked in, when `isCheckedIn` is `true`. | `"1"` |
| `allowManualPrice` | Boolean | Indicates whether the user has permission to change item prices manually in this cart. | `false` |
| `canEditData` | Boolean | Indicates whether the customer's data in the cart can be edited. | `true` |
| `userProfileId` | String or null | Unique ID associated with the customer profile. | `"fb542e51-5488-4c34-8d17-ed8fcf597a94"` |
| `profileProvider` | String | Provider of the customer profile. | `"VTEX"` |
| `availableAccounts` | Array of strings | Available accounts. | `[]` |
| `availableAddresses` | Array of objects | Addresses available for the customer. Each object has the same fields as the [address object](#address-object). | See [shippingData](#shippingdata). |
| `userType` | String or null | User type. Example: `"callCenterOperator"` when the cart is being handled by a call center operator on behalf of a customer. | `"callCenterOperator"` |
| `ignoreProfileData` | Boolean | Indicates whether the customer profile data should be ignored in this cart. | `false` |
| `value` | Integer | Total value of the order in cents. For example, $24.99 is represented as `2499`. | `16500` |
| `messages` | Array of objects | Messages generated by the server while processing the request. See [messages](#messages). | `[]` |
| `items` | Array of objects | Information on each item in the cart. See [items](#items). | `[]` |
| `selectableGifts` | Array | Gifts that the customer can select. See [selectableGifts](#selectablegifts). | `[]` |
| `totalizers` | Array of objects | Totals of the order by category. See [totalizers](#totalizers). | `[]` |
| `shippingData` | Object or null | Shipping information. See [shippingData](#shippingdata). | `{}` |
| `clientProfileData` | Object or null | Customer profile information. See [clientProfileData](#clientprofiledata). | `{}` |
| `paymentData` | Object | Payment information. See [paymentData](#paymentdata). | `{}` |
| `marketingData` | Object or null | Promotion and campaign tracking data. See [marketingData](#marketingdata). | `{}` |
| `sellers` | Array of objects | Sellers of the items in the cart. See [sellers](#sellers). | `[]` |
| `clientPreferencesData` | Object | Customer preferences. See [clientPreferencesData](#clientpreferencesdata). | `{}` |
| `commercialConditionData` | Object or null | Commercial condition information. See [commercialConditionData](#commercialconditiondata). | `null` |
| `storePreferencesData` | Object | Store configuration data. See [storePreferencesData](#storepreferencesdata). | `{}` |
| `giftRegistryData` | Object or null | Gift registry (gift list) information. See [giftRegistryData](#giftregistrydata). | `null` |
| `openTextField` | Object or null | Free text information about the order. See [openTextField](#opentextfield). | `null` |
| `invoiceData` | Object or null | Invoice data, including the billing address. See [invoiceData](#invoicedata). | `null` |
| `customData` | Object or null | Custom information added by the store. See [customData](#customdata). | `null` |
| `itemMetadata` | Object | Metadata of the items in the cart. See [itemMetadata](#itemmetadata). | `{}` |
| `hooksData` | Object or null | Hooks information. See [hooksData](#hooksdata). | `null` |
| `ratesAndBenefitsData` | Object | Promotions and taxes that apply to the order. See [ratesAndBenefitsData](#ratesandbenefitsdata). | `{}` |
| `subscriptionData` | Object or null | Subscription information. See [subscriptionData](#subscriptiondata). | `null` |
| `itemsOrdination` | Object or null | Sorting criteria of the items in the cart. See [itemsOrdination](#itemsordination). | `null` |

## Cart and items

The sections in this group describe what is in the cart: the items and their prices, the sellers that fulfill them, the gifts available, and the order totals.

### items

Array containing one object for each item (SKU) in the cart, with identification, catalog, price, quantity, and seller information. Items are identified in other sections, such as `shippingData.logisticsInfo`, by their position in this array (`itemIndex`), starting at `0`.

>⚠️ If you use integrations that consume price data, such as checkout or order integrations, the `sellingPrice` field may be subject to rounding discrepancies. We recommend retrieving price data from the [`priceDefinition`](#itemspricedefinition) object instead.

**Example:**

```json
"items": [
  {
    "uniqueId": "E0F2B7AF5CD74D668F1E27537206912C",
    "id": "1",
    "productId": "1",
    "productRefId": "1",
    "refId": "0001",
    "ean": "123456789",
    "name": "Royal Canin Feline Urinary 500g",
    "skuName": "Royal Canin Feline Urinary 500g",
    "modalType": null,
    "parentItemIndex": null,
    "parentAssemblyBinding": null,
    "priceValidUntil": "2026-11-02T14:59:00Z",
    "tax": 0,
    "taxCode": "54WC8ZN6K8",
    "price": 15000,
    "listPrice": 30000,
    "manualPrice": null,
    "manualPriceAppliedBy": null,
    "sellingPrice": 15000,
    "rewardValue": 0,
    "isGift": false,
    "additionalInfo": {
      "dimension": null,
      "brandName": "Royal Canin",
      "brandId": "2000000",
      "offeringInfo": null,
      "offeringType": null,
      "offeringTypeId": null
    },
    "preSaleDate": null,
    "productCategoryIds": "/1/10/",
    "productCategories": {
      "1": "Food",
      "10": "Dry food"
    },
    "quantity": 1,
    "seller": "1",
    "sellerChain": ["1"],
    "imageUrl": "http://mystore.vteximg.com.br/arquivos/ids/155450-55-55/Royal-Canin-Feline-Urinary.jpg?v=637139444438700000",
    "detailUrl": "/royal-canin-feline-urinary/p",
    "bundleItems": [],
    "attachments": [],
    "offerings": [],
    "priceTags": [],
    "availability": "available",
    "measurementUnit": "un",
    "unitMultiplier": 1.0,
    "manufacturerCode": null,
    "priceDefinition": {
      "calculatedSellingPrice": 15000,
      "total": 15000,
      "sellingPrices": [
        {
          "value": 15000,
          "quantity": 1
        }
      ]
    }
  }
]
```

| Field | Type | Description | Example |
| - | - | - | - |
| `uniqueId` | String | Unique identifier of the item in the cart. Two lines of the same SKU in the cart, for example, with different attachments, have different `uniqueId` values. | `"E0F2B7AF5CD74D668F1E27537206912C"` |
| `id` | String | SKU ID. | `"1"` |
| `productId` | String | ID of the product to which the SKU belongs. | `"1"` |
| `productRefId` | String | Product reference ID. | `"1"` |
| `refId` | String or null | SKU reference ID. | `"0001"` |
| `ean` | String or null | European Article Number (EAN), the SKU barcode, as registered in the [SKU registration](https://help.vtex.com/en/tutorial/sku-registration-fields--21DDItuEQc6mseiW8EakcY). | `"123456789"` |
| `name` | String | Product name. | `"Royal Canin Feline Urinary 500g"` |
| `skuName` | String | SKU name. | `"Royal Canin Feline Urinary 500g"` |
| `modalType` | String or null | Modal type of the SKU, used to define specific carriers for products that require special transportation, such as furniture or chemicals. | `"FURNITURE"` |
| `parentItemIndex` | Integer or null | Index of the parent item in the `items` array, when this item is part of an [assembly](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH) (for example, an engraving added to a product). | `0` |
| `parentAssemblyBinding` | String or null | ID of the assembly option that binds this item to its parent item. | `"vtex.subscription.weekly"` |
| `priceValidUntil` | String | Date and time until which the item price is valid, in UTC ISO 8601 format. | `"2026-11-02T14:59:00Z"` |
| `tax` | Integer | Tax value in cents. | `0` |
| `taxCode` | String | Unique identifier code assigned to a tax within the VTEX Admin. | `"54WC8ZN6K8"` |
| `price` | Integer | Unit price of the SKU in cents, before promotions are applied. | `15000` |
| `listPrice` | Integer | Unit list price ("from" price) in cents. | `30000` |
| `manualPrice` | Integer or null | Unit price manually set for the item in cents, when it applies. See [Change price](https://developers.vtex.com/docs/api-reference/checkout-api#put-/api/checkout/pub/orderForm/-orderFormId-/items/-itemIndex-/price). | `10000` |
| `manualPriceAppliedBy` | String or null | ID of the user who applied the manual price, when it applies. | `"fb542e51-5863-4c34-8d17-ed8fcf597a09"` |
| `sellingPrice` | Integer | Unit selling price in cents, with promotions applied. This field may be subject to rounding discrepancies. We recommend using `priceDefinition` instead. | `15000` |
| `rewardValue` | Integer | Reward value in cents. | `0` |
| `isGift` | Boolean | Indicates whether the item is a gift. | `false` |
| `additionalInfo` | Object | Additional information about the item. | See the following rows. |
| `additionalInfo.dimension` | String or null | Dimension. | `null` |
| `additionalInfo.brandName` | String | Brand name. | `"Royal Canin"` |
| `additionalInfo.brandId` | String | Brand ID. | `"2000000"` |
| `additionalInfo.offeringInfo` | String or null | Offering information. | `null` |
| `additionalInfo.offeringType` | String or null | Offering type. | `null` |
| `additionalInfo.offeringTypeId` | String or null | Offering type ID. | `null` |
| `preSaleDate` | String or null | Presale date, when the item is sold in presale. | `"2026-12-01T00:00:00Z"` |
| `productCategoryIds` | String | Path of category IDs of the product, from the department to the deepest category, separated by `/`. | `"/1/10/"` |
| `productCategories` | Object | Object in which each key is a category ID from `productCategoryIds`. | `{"1": "Food", "10": "Dry food"}` |
| `productCategories.{ID}` | String | Name of the category corresponding to the ID in the key. | `"Dry food"` |
| `quantity` | Integer | Quantity of units of the item in the cart. | `1` |
| `seller` | String | ID of the seller that sells the item. | `"1"` |
| `sellerChain` | Array of strings | Sellers involved in the chain. The list should contain only one seller, unless it is a [Multilevel Omnichannel Inventory](https://help.vtex.com/en/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4) order. | `["1"]` |
| `imageUrl` | String | URL of the SKU image. | `"http://mystore.vteximg.com.br/arquivos/ids/155450-55-55/Royal-Canin-Feline-Urinary.jpg"` |
| `detailUrl` | String | Relative URL of the product page. | `"/royal-canin-feline-urinary/p"` |
| `bundleItems` | Array of objects | Services sold along with the SKU, such as a gift wrap. | See the following rows. |
| `bundleItems[].type` | String | Service type. | `"Gift wrap"` |
| `bundleItems[].id` | Integer | Service ID. | `5` |
| `bundleItems[].name` | String | Service name. | `"Gift wrap"` |
| `bundleItems[].price` | Integer | Service price in cents. | `500` |
| `attachments` | Array of objects | [Attachments](https://help.vtex.com/en/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm) added to the item, such as a customization or a subscription. | See the following rows. |
| `attachments[].name` | String | Attachment name. | `"vtex.subscription.weekly"` |
| `attachments[].content` | Object | Attachment content as key-value pairs. | `{"vtex.subscription.key.frequency": "1 week"}` |
| `offerings` | Array of objects | Services available for the SKU, which the customer can add to the item, such as a gift wrap or a warranty. | See the following rows. |
| `offerings[].type` | String | Service type. | `"Warranty"` |
| `offerings[].id` | String | Service type ID. | `"5"` |
| `offerings[].name` | String | Name of the service type. | `"Extended warranty"` |
| `offerings[].allowGiftMessage` | Boolean | Indicates whether the service type can be displayed on the gift card. | `false` |
| `offerings[].price` | Integer | Service type price in cents. | `1500` |
| `offerings[].attachmentOfferings` | Array of objects | Attachments available for the service. | See the following rows. |
| `offerings[].attachmentOfferings[].name` | String | Name of the attachment. | `"message"` |
| `offerings[].attachmentOfferings[].required` | Boolean | Indicates whether the attachment is required (`true`) or not (`false`). | `false` |
| `offerings[].attachmentOfferings[].schema` | Object | Custom values [created into the attachment](https://help.vtex.com/en/tutorial/adding-an-attachment--7zHMUpuoQE4cAskqEUWScU). | `{"text": {"maximumNumberOfCharacters": 100, "domain": []}}` |
| `priceTags` | Array of objects | Price tags, each of which modifies the item price, such as discounts or taxes that apply to the item in the context of the order. | See the following rows. |
| `priceTags[].name` | String | Price tag name in the format `{type}@{where}-{identifier}#{calculationId}`, where:<ul><li>`type`: indicates whether the tag refers to a discount or tax.</li><li>`where`: specifies the context, either price or shipping.</li><li>`identifier`: promotion ID.</li><li>`calculationId`: hash that may vary with each price calculation.</li></ul> | `"DISCOUNT@MANUALPRICE"` |
| `priceTags[].value` | Integer | Price tag value in cents. Negative values represent a promotion (value decrease) and positive values represent a tax (value increase). | `-5000` |
| `priceTags[].rawValue` | Number | Raw price tag value with up to five decimals, sourced from the promotion configuration. This value is informational only and is not used in checkout calculations. | `-50.0` |
| `priceTags[].isPercentual` | Boolean | Indicates whether `value` and `rawValue` represent a percentage to be applied during checkout calculation. The default value is `false`. | `false` |
| `priceTags[].identifier` | String or null | Promotion unique identifier. | `"1234abc-5678b-1234c"` |
| `availability` | String | SKU availability. Possible values are `available`, `withoutStock`, and `cannotBeDelivered`. Only SKUs with the `available` value can be sold and delivered. | `"available"` |
| `measurementUnit` | String | Measurement unit of the SKU. | `"un"` |
| `unitMultiplier` | Number | Unit multiplier of the SKU. The quantity added to the cart is multiplied by this value. For example, a product sold by kilogram with `unitMultiplier` of `0.3` is sold in 300 g units. | `1.0` |
| `manufacturerCode` | String or null | Manufacturer code of the SKU. | `"MC-12345"` |
| `priceDefinition` | Object | Price information for all units of the item. See [items[].priceDefinition](#itemspricedefinition). | See the following rows. |
| `priceDefinition.calculatedSellingPrice` | Integer | Calculated unit selling price of the item in cents. | `15000` |
| `priceDefinition.total` | Integer | Total value for all units of the item in cents. | `15000` |
| `priceDefinition.sellingPrices` | Array of objects | Objects, each containing `value` and `quantity`, for the different rounding instances that can be combined to form the correctly rounded `total`. | See the following rows. |
| `priceDefinition.sellingPrices[].value` | Integer | Value in cents for that specific rounding. | `15000` |
| `priceDefinition.sellingPrices[].quantity` | Integer | Rounding quantity, meaning how many units are rounded to this value. | `1` |

#### items[].priceDefinition

The `priceDefinition` object provides the correctly rounded prices of an item. When the unit selling price can't be divided evenly among all units, for example because of a percentage discount or a unit multiplier, `sellingPrices` lists each rounding instance so that the sum of `value × quantity` matches `total`.

In the following example, an item sold by weight (`unitMultiplier` of `0.3` kg) has a unit price of `199` per kg and a quantity of `3`. The total of `179` is reached by charging `60` for two units and `59` for one unit:

```json
{
  "items": [
    {
      "id": "1001669",
      "price": 199,
      "quantity": 3,
      "unitMultiplier": 0.3,
      "measurementUnit": "kg",
      "sellingPrice": 59,
      "priceDefinition": {
        "calculatedSellingPrice": 59,
        "total": 179,
        "sellingPrices": [
          {
            "value": 60,
            "quantity": 2
          },
          {
            "value": 59,
            "quantity": 1
          }
        ]
      }
    }
  ]
}
```

### itemMetadata

Object containing catalog metadata of each item in the cart, such as name, image, and product page URL. It is used to display items consistently, including items that aren't part of `items`, such as gifts and assembly options.

**Example:**

```json
"itemMetadata": {
  "items": [
    {
      "id": "1",
      "seller": "1",
      "name": "Royal Canin Feline Urinary 500g",
      "skuName": "Royal Canin Feline Urinary 500g",
      "productId": "1",
      "refId": "0001",
      "ean": "123456789",
      "imageUrl": "http://mystore.vteximg.com.br/arquivos/ids/155450-55-55/Royal-Canin-Feline-Urinary.jpg?v=637139444438700000",
      "detailUrl": "/royal-canin-feline-urinary/p"
    }
  ]
}
```

| Field | Type | Description | Example |
| - | - | - | - |
| `items` | Array of objects | Metadata of each item in the order. | See the following rows. |
| `items[].id` | String | SKU ID. | `"1"` |
| `items[].seller` | String | Seller ID. | `"1"` |
| `items[].name` | String | Product name. | `"Royal Canin Feline Urinary 500g"` |
| `items[].skuName` | String | SKU name. | `"Royal Canin Feline Urinary 500g"` |
| `items[].productId` | String | Product ID. | `"1"` |
| `items[].refId` | String or null | SKU reference ID. | `"0001"` |
| `items[].ean` | String or null | European Article Number (EAN) of the SKU. | `"123456789"` |
| `items[].imageUrl` | String | URL of the SKU image. | `"http://mystore.vteximg.com.br/arquivos/ids/155450-55-55/Royal-Canin-Feline-Urinary.jpg"` |
| `items[].detailUrl` | String | Relative URL of the product page. | `"/royal-canin-feline-urinary/p"` |

### itemsOrdination

Object containing the criteria used to sort the items in the `items` array. Returns `null` when no sorting is applied.

**Example:**

```json
"itemsOrdination": {
  "criteria": "NAME",
  "ascending": true
}
```

| Field | Type | Description | Example |
| - | - | - | - |
| `criteria` | String | Criteria adopted to sort the items. Possible values are:<ul><li>`NAME`: item name.</li><li>`ADD_TIME`: time when the item was added to the cart.</li><li>`GIFT`: non-gift items are listed before gift items.</li></ul> | `"NAME"` |
| `ascending` | Boolean | Indicates whether the sorting is ascending (`true`) or descending (`false`). | `true` |

### selectableGifts

Array containing the gifts that the customer can choose from, based on [Buy One Get One](https://help.vtex.com/en/docs/tutorials/buy-one-get-one) promotions that offer a gift. Each object represents a list of gift options.

**Example:**

```json
"selectableGifts": [
  {
    "id": "a1b2c3d4-1234-5678-9abc-def012345678",
    "availableQuantity": 1,
    "availableGifts": [
      {
        "id": "15",
        "name": "Cat toy",
        "isSelected": true
      }
    ]
  }
]
```

| Field | Type | Description | Example |
| - | - | - | - |
| `id` | String | ID of the selectable gifts list. | `"a1b2c3d4-1234-5678-9abc-def012345678"` |
| `availableQuantity` | Integer | Number of gifts the customer can select from this list. | `1` |
| `availableGifts` | Array of objects | Items that can be selected as gifts. Each object has the same fields as the [items](#items) array, in addition to `isSelected`. | See the following row. |
| `availableGifts[].isSelected` | Boolean | Indicates whether the item was selected as a gift. | `true` |

### sellers

Array containing one object for each seller responsible for items in the cart.

**Example:**

```json
"sellers": [
  {
    "id": "1",
    "name": "mystore",
    "logo": "https://mystore.vteximg.com.br/arquivos/logo.jpg",
    "minimumOrderValue": 0
  }
]
```

| Field | Type | Description | Example |
| - | - | - | - |
| `id` | String | Seller ID. | `"1"` |
| `name` | String | Seller name. | `"mystore"` |
| `logo` | String or null | URL of the seller logo. | `"https://mystore.vteximg.com.br/arquivos/logo.jpg"` |
| `minimumOrderValue` | Integer or null | Minimum order value configured for the seller in cents. | `5000` |

### totalizers

Array containing one object for each totalizer of the order. Totalizers contain the sum of values for a specific part of the order, such as the total value of the items, discounts, shipping, and taxes.

**Example:**

```json
"totalizers": [
  {
    "id": "Items",
    "name": "Items Total",
    "value": 15000
  },
  {
    "id": "Discounts",
    "name": "Discounts Total",
    "value": -5000
  },
  {
    "id": "Shipping",
    "name": "Shipping Total",
    "value": 1500
  }
]
```

| Field | Type | Description | Example |
| - | - | - | - |
| `id` | String | Totalizer ID. Common values are `Items`, `Discounts`, `Shipping`, `Tax`, and `CustomTax`. | `"Items"` |
| `name` | String | Totalizer name, according to the cart locale. | `"Items Total"` |
| `value` | Integer | Totalizer value in cents. Discounts are represented as negative values. | `15000` |

## Customer

The sections in this group describe who is placing the order and their preferences.

### clientProfileData

Object containing the profile data of the customer who is placing the order. Returns `null` until the customer informs their email.

If the customer's identity hasn't been confirmed, some personal data is masked with asterisks to protect the shopper's privacy.

**Example:**

```json
"clientProfileData": {
  "email": "clark.kent@examplemail.com",
  "firstName": "Clark",
  "lastName": "Kent",
  "documentType": "cpf",
  "document": "12345678900",
  "phone": "+5521999999999",
  "corporateName": null,
  "tradeName": null,
  "corporateDocument": null,
  "stateInscription": null,
  "corporatePhone": null,
  "isCorporate": false,
  "profileCompleteOnLoading": false,
  "profileErrorOnLoading": false,
  "customerClass": null
}
```

| Field | Type | Description | Example |
| - | - | - | - |
| `email` | String or null | Customer's email address. | `"clark.kent@examplemail.com"` |
| `firstName` | String or null | Customer's first name. | `"Clark"` |
| `lastName` | String | Customer's last name. | `"Kent"` |
| `documentType` | String | Type of the document informed by the customer. | `"cpf"` |
| `document` | String | Document number informed by the customer. | `"12345678900"` |
| `phone` | String | Customer's phone number. | `"+5521999999999"` |
| `corporateName` | String or null | Company name, if the customer is a legal entity. | `"Daily Planet Ltd."` |
| `tradeName` | String or null | Trade name, if the customer is a legal entity. | `"Daily Planet"` |
| `corporateDocument` | String or null | Corporate document, if the customer is a legal entity. | `"12345678000100"` |
| `stateInscription` | String or null | State inscription, if the customer is a legal entity. | `"12345678"` |
| `corporatePhone` | String or null | Corporate phone number, if the customer is a legal entity. | `"+551100988887777"` |
| `isCorporate` | Boolean | Indicates whether the customer is a legal entity. | `false` |
| `profileCompleteOnLoading` | Boolean | Indicates whether the customer profile was complete when it was loaded into the cart. | `false` |
| `profileErrorOnLoading` | Boolean or null | Indicates whether an error occurred when loading the customer profile into the cart. | `false` |
| `customerClass` | String or null | Customer class, used to segment customers in promotions and B2B scenarios. | `"gold"` |

### clientPreferencesData

Object containing the preferences of the customer who is placing the order.

**Example:**

```json
"clientPreferencesData": {
  "locale": "pt-BR",
  "optinNewsLetter": true
}
```

| Field | Type | Description | Example |
| - | - | - | - |
| `locale` | String | Customer's locale. The `sendLocale()` method from [vtex.js](https://developers.vtex.com/docs/guides/vtexjs-for-checkout) changes the value of this field. | `"pt-BR"` |
| `optinNewsLetter` | Boolean or null | Indicates whether the customer opted to receive newsletters from the store. | `true` |

### giftRegistryData

Object containing information about the gift list associated with the cart, when the customer is buying items from a gift list. Returns `null` when the cart isn't associated with a gift list.

**Example:**

```json
"giftRegistryData": {
  "giftRegistryId": "22222",
  "giftRegistryType": "1",
  "giftRegistryTypeName": "Wedding",
  "addressId": "-1617303424547",
  "description": "Lois and Clark's wedding"
}
```

| Field | Type | Description | Example |
| - | - | - | - |
| `giftRegistryId` | String | Gift list ID. | `"22222"` |
| `giftRegistryType` | String or null | Gift list type ID. | `"1"` |
| `giftRegistryTypeName` | String or null | Gift list type name. | `"Wedding"` |
| `addressId` | String or null | ID of the delivery address of the gift list. | `"-1617303424547"` |
| `description` | String | Gift list description. | `"Lois and Clark's wedding"` |

## Shipping

### shippingData

Object containing the shipping information of the order: the delivery address, the addresses available to the customer, and the logistics information of each item, including the available shipping options (SLAs) and the option selected by the customer. Returns `null` until shipping information is available.

**Example:**

```json
"shippingData": {
  "address": {
    "addressType": "residential",
    "receiverName": "Clark Kent",
    "addressId": "666c2e830bd9474ab6f6cc53fb6dd2d2",
    "isDisposable": true,
    "postalCode": "22250040",
    "city": "Rio de Janeiro",
    "state": "RJ",
    "country": "BRA",
    "street": "Praia de Botafogo",
    "number": "300",
    "neighborhood": "Botafogo",
    "complement": "3rd floor",
    "reference": null,
    "geoCoordinates": [-43.18218231201172, -22.94549560546875]
  },
  "logisticsInfo": [
    {
      "itemIndex": 0,
      "selectedSla": "Normal",
      "selectedDeliveryChannel": "delivery",
      "addressId": "666c2e830bd9474ab6f6cc53fb6dd2d2",
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
              "courierName": "Carrier",
              "quantity": 1
            }
          ],
          "shippingEstimate": "3bd",
          "shippingEstimateDate": null,
          "lockTTL": "10d",
          "availableDeliveryWindows": [],
          "deliveryWindow": null,
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
      "shipsTo": ["BRA"],
      "itemId": "1",
      "deliveryChannels": [
        { "id": "delivery" },
        { "id": "pickup-in-point" }
      ]
    }
  ],
  "selectedAddresses": [
    {
      "addressType": "residential",
      "receiverName": "Clark Kent",
      "addressId": "666c2e830bd9474ab6f6cc53fb6dd2d2",
      "isDisposable": true,
      "postalCode": "22250040",
      "city": "Rio de Janeiro",
      "state": "RJ",
      "country": "BRA",
      "street": "Praia de Botafogo",
      "number": "300",
      "neighborhood": "Botafogo",
      "complement": "3rd floor",
      "reference": null,
      "geoCoordinates": [-43.18218231201172, -22.94549560546875]
    }
  ],
  "availableAddresses": [
    {
      "addressType": "residential",
      "receiverName": "Clark Kent",
      "addressId": "666c2e830bd9474ab6f6cc53fb6dd2d2",
      "isDisposable": true,
      "postalCode": "22250040",
      "city": "Rio de Janeiro",
      "state": "RJ",
      "country": "BRA",
      "street": "Praia de Botafogo",
      "number": "300",
      "neighborhood": "Botafogo",
      "complement": "3rd floor",
      "reference": null,
      "geoCoordinates": [-43.18218231201172, -22.94549560546875]
    }
  ]
}
```

| Field | Type | Description | Example |
| - | - | - | - |
| `address` | Object or null | Main delivery address of the order. See [Address object](#address-object). | See the example above. |
| `logisticsInfo` | Array of objects | Logistics information. Each object corresponds to an object in the `items` array, based on the respective `itemIndex`. | See the following rows. |
| `logisticsInfo[].itemIndex` | Integer | Index of the corresponding item in the `items` array, starting at `0`. | `0` |
| `logisticsInfo[].selectedSla` | String or null | ID of the SLA (shipping option) selected by the customer. If the store uses the [Delivery Options](https://help.vtex.com/en/docs/tutorials/delivery-options-beta) feature, this field returns the delivery option ID selected for this SLA. | `"Normal"` |
| `logisticsInfo[].selectedDeliveryChannel` | String or null | Delivery channel selected by the customer. Possible values are `delivery` and `pickup-in-point`. | `"delivery"` |
| `logisticsInfo[].addressId` | String or null | ID of the address to which the item will be delivered. | `"666c2e830bd9474ab6f6cc53fb6dd2d2"` |
| `logisticsInfo[].slas` | Array of objects | SLAs (shipping options) available for the item. | See the following rows. |
| `logisticsInfo[].slas[].id` | String | SLA ID. If the store uses the [Delivery Options](https://help.vtex.com/en/docs/tutorials/delivery-options-beta) feature, this field returns the delivery option ID, as in `1223d5b4-52a4-442f-ab23-01345b60be48`. | `"Normal"` |
| `logisticsInfo[].slas[].deliveryChannel` | String | Delivery channel of the SLA. Possible values are `delivery` and `pickup-in-point`. | `"delivery"` |
| `logisticsInfo[].slas[].name` | String | SLA name. If the store uses the [Delivery Options](https://help.vtex.com/en/docs/tutorials/delivery-options-beta) feature, this field shows the delivery option name, as in `Delivery \| BRA \| Up to 30 hours`. | `"Normal"` |
| `logisticsInfo[].slas[].deliveryIds` | Array of objects | Information on each delivery that composes the SLA. | See the following rows. |
| `logisticsInfo[].slas[].deliveryIds[].courierId` | String | Carrier ID. | `"1"` |
| `logisticsInfo[].slas[].deliveryIds[].warehouseId` | String | Warehouse ID. | `"1_1"` |
| `logisticsInfo[].slas[].deliveryIds[].dockId` | String | Loading dock ID. | `"1"` |
| `logisticsInfo[].slas[].deliveryIds[].courierName` | String | Carrier name. | `"Carrier"` |
| `logisticsInfo[].slas[].deliveryIds[].quantity` | Integer | Quantity of units of the item delivered by this carrier. | `1` |
| `logisticsInfo[].slas[].attachmentOfferings` | Array of objects or null | Attachments available for the SLA. | See the following rows. |
| `logisticsInfo[].slas[].attachmentOfferings[].name` | String or null | Name of the attachment. | `"delivery-instructions"` |
| `logisticsInfo[].slas[].attachmentOfferings[].required` | Boolean or null | Indicates whether the attachment is required (`true`) or not (`false`). | `false` |
| `logisticsInfo[].slas[].attachmentOfferings[].schema` | Object or null | Custom values [created into the attachment](https://help.vtex.com/en/tutorial/adding-an-attachment--7zHMUpuoQE4cAskqEUWScU). | `{"note": {"maximumNumberOfCharacters": 100, "domain": []}}` |
| `logisticsInfo[].slas[].shippingEstimate` | String | Total shipping estimate time, represented by a number followed by a time unit. The unit can be `bd` (business days), `d` (days), `h` (hours), or `m` (minutes). For example, three business days is represented as `3bd`. | `"3bd"` |
| `logisticsInfo[].slas[].shippingEstimateDate` | String or null | Estimated shipping date. Contains a value only when the query parameter `individualShippingEstimates=true` is used. Otherwise, it's `null`. | `"2026-10-07T17:35:00-03:00"` |
| `logisticsInfo[].slas[].useIndividualShippingEstimates` | Boolean | Indicates whether the product's individual estimated shipping date is displayed in the `shippingEstimate` field. | `false` |
| `logisticsInfo[].slas[].lockTTL` | String or null | Time during which the item inventory is reserved after the order is placed, using the same format as `shippingEstimate`. | `"10d"` |
| `logisticsInfo[].slas[].availableDeliveryWindows` | Array of objects | [Scheduled delivery](https://help.vtex.com/en/tutorial/scheduled-delivery--22g3HAVCGLFiU7xugShOBi) windows available for the SLA. | See the following rows. |
| `logisticsInfo[].slas[].availableDeliveryWindows[].startDateUtc` | String | Delivery window start date and time in UTC. | `"2026-10-05T09:00:00+00:00"` |
| `logisticsInfo[].slas[].availableDeliveryWindows[].endDateUtc` | String | Delivery window end date and time in UTC. | `"2026-10-05T12:00:00+00:00"` |
| `logisticsInfo[].slas[].availableDeliveryWindows[].price` | Integer | Delivery window price in cents. | `1000` |
| `logisticsInfo[].slas[].availableDeliveryWindows[].lisPrice` | Integer | Delivery window list price in cents. The field name is `lisPrice` in the API response. | `1000` |
| `logisticsInfo[].slas[].availableDeliveryWindows[].tax` | Integer | Delivery window tax in cents. | `0` |
| `logisticsInfo[].slas[].deliveryWindow` | Object or null | Delivery window selected by the customer, in case of scheduled delivery. It has the same fields as the objects in `availableDeliveryWindows`. | `{"startDateUtc": "2026-10-05T09:00:00+00:00", "endDateUtc": "2026-10-05T12:00:00+00:00", "price": 1000, "lisPrice": 1000, "tax": 0}` |
| `logisticsInfo[].slas[].price` | Integer | SLA price in cents. | `1500` |
| `logisticsInfo[].slas[].listPrice` | Integer | SLA list price in cents. | `1500` |
| `logisticsInfo[].slas[].tax` | Integer | SLA tax in cents. | `0` |
| `logisticsInfo[].slas[].pickupStoreInfo` | Object | Information on the pickup point, when the SLA is a pickup option. | See the following rows. |
| `logisticsInfo[].slas[].pickupStoreInfo.isPickupStore` | Boolean | Indicates whether the SLA is a pickup point. | `true` |
| `logisticsInfo[].slas[].pickupStoreInfo.friendlyName` | String or null | Name of the pickup point displayed to customers. | `"VTEX SP"` |
| `logisticsInfo[].slas[].pickupStoreInfo.address` | Object or null | Pickup point address. See [Address object](#address-object). | `{"addressType": "pickup", "postalCode": "04538-132", "city": "São Paulo", ...}` |
| `logisticsInfo[].slas[].pickupStoreInfo.additionalInfo` | String or null | Additional information about the pickup point, such as opening hours. | `"Open from 9 a.m. to 6 p.m."` |
| `logisticsInfo[].slas[].pickupStoreInfo.dockId` | String or null | ID of the loading dock associated with the pickup point. | `"1"` |
| `logisticsInfo[].slas[].pickupPointId` | String or null | Pickup point ID. | `"1_VTEXSP"` |
| `logisticsInfo[].slas[].pickupDistance` | Number | Distance between the customer's address and the pickup point, in kilometers. | `2.5` |
| `logisticsInfo[].slas[].polygonName` | String or null | Name of the [geolocation polygon](https://help.vtex.com/en/tutorial/registering-geolocation/) that matched the delivery address. | `"rio-south-zone"` |
| `logisticsInfo[].slas[].transitTime` | String | Transit time of the carrier, using the same format as `shippingEstimate`. | `"3bd"` |
| `logisticsInfo[].shipsTo` | Array of strings | Three-letter ISO codes of the countries to which the item can be shipped. | `["BRA"]` |
| `logisticsInfo[].itemId` | String | SKU ID of the item. | `"1"` |
| `logisticsInfo[].deliveryChannels` | Array of objects | Delivery channels available for the item. | See the following row. |
| `logisticsInfo[].deliveryChannels[].id` | String | Delivery channel ID. Possible values are `delivery` and `pickup-in-point`. | `"pickup-in-point"` |
| `selectedAddresses` | Array of objects | Addresses selected for the order. See [Address object](#address-object). | See the example above. |
| `availableAddresses` | Array of objects | Addresses available for the order. See [Address object](#address-object). | See the example above. |

#### Address object

The address object is used in `shippingData.address`, `shippingData.selectedAddresses`, `shippingData.availableAddresses`, `shippingData.logisticsInfo[].slas[].pickupStoreInfo.address`, and in the root `availableAddresses` field.

| Field | Type | Description | Example |
| - | - | - | - |
| `addressType` | String | Type of address. Possible values are `residential`, `commercial`, `pickup`, `inStore`, `giftRegistry`, `search`, and `invoice`. | `"residential"` |
| `receiverName` | String or null | Name of the person who will receive the order. | `"Clark Kent"` |
| `addressId` | String or null | Address ID. | `"666c2e830bd9474ab6f6cc53fb6dd2d2"` |
| `isDisposable` | Boolean | Indicates whether the address is disposable. Addresses with `isDisposable` set to `true` aren't saved to the shopper's profile when the order is completed, while addresses with `isDisposable` set to `false` belong to the shopper. See [Disposable addresses](#disposable-addresses). | `true` |
| `postalCode` | String | Postal code. | `"22250040"` |
| `city` | String | City. | `"Rio de Janeiro"` |
| `state` | String | State. | `"RJ"` |
| `country` | String | Three-letter ISO code of the country. | `"BRA"` |
| `street` | String | Street name. | `"Praia de Botafogo"` |
| `number` | String | Number of the building, house, or apartment. | `"300"` |
| `neighborhood` | String | Neighborhood. | `"Botafogo"` |
| `complement` | String or null | Complement to the address, when it applies. | `"3rd floor"` |
| `reference` | String or null | Reference that helps locate the address more precisely for delivery. | `"Next to the subway station"` |
| `geoCoordinates` | Array of numbers | Geographic coordinates of the address: longitude first, then latitude. | `[-43.18218231201172, -22.94549560546875]` |

#### Disposable addresses

The `isDisposable` behavior depends on the address type:

- `giftRegistry`, `pickup`, `search`, and `inStore`: always disposable, as they don't belong to the shopper navigating the cart.
- `residential`: may be disposable. Addresses from a complete shopper profile, or entered by an authenticated shopper with a complete profile, aren't disposable. All other residential addresses are disposable, including those from first-time purchases, since no complete profile exists yet.
- `commercial`: corresponds to company addresses used in B2B contexts and follows the same logic as residential addresses.
- `invoice`: doesn't have the `isDisposable` flag. In practice, only authenticated shoppers can add invoice data to the cart, so these addresses are never treated as disposable.

When a residential address is marked as disposable and the profile is complete, authentication is required to complete the order. Additionally, when a disposable residential address is used to complete a purchase, saved cards can't be used.

## Payment and invoice

### paymentData

Object containing the payment information of the order: the payment methods available, the installment options, the payments selected by the customer, gift cards, and transactions.

>ℹ️ For accurate information on installment options and values, we recommend using the [Cart installments](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/orderForm/-orderFormId-/installments) endpoint instead of the `installmentOptions` field.

**Example:**

```json
"paymentData": {
  "updateStatus": "updated",
  "installmentOptions": [
    {
      "paymentSystem": 2,
      "bin": null,
      "paymentName": null,
      "paymentGroupName": null,
      "value": 16500,
      "installments": [
        {
          "count": 1,
          "hasInterestRate": false,
          "interestRate": 0,
          "value": 16500,
          "total": 16500,
          "sellerMerchantInstallments": [
            {
              "id": "MYSTORE",
              "count": 1,
              "hasInterestRate": false,
              "interestRate": 0,
              "value": 16500,
              "total": 16500
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
      "validator": {
        "regex": "^4",
        "mask": "9999 9999 9999 9999",
        "cardCodeRegex": "^[0-9]{3}$",
        "cardCodeMask": "999",
        "weights": [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]
      },
      "stringId": "2",
      "template": "creditCardPaymentGroup-template",
      "requiresDocument": false,
      "displayDocument": false,
      "isCustom": false,
      "description": null,
      "requiresAuthentication": false,
      "dueDate": "2026-10-09T14:59:00Z",
      "availablePayments": null,
      "selected": false
    }
  ],
  "payments": [
    {
      "paymentSystem": 2,
      "paymentSystemName": "Visa",
      "group": "creditCardPaymentGroup",
      "bin": null,
      "accountId": null,
      "installments": 1,
      "installmentsInterestRate": 0,
      "installmentsValue": 16500,
      "value": 16500,
      "referenceValue": 16500,
      "hasDefaultBillingAddress": true
    }
  ],
  "giftCards": [
    {
      "redemptionCode": "HYUO-TEZZ-QFFT-HTFR",
      "value": 500,
      "balance": 500,
      "name": null,
      "id": "-1390324156495k195pmab4rall3di",
      "inUse": true,
      "isSpecialCard": false
    }
  ],
  "giftCardMessages": [],
  "availableAccounts": [],
  "availableTokens": [],
  "availableAssociations": {},
  "transactions": [
    {
      "isActive": true,
      "transactionId": "296D6D245C17437E823EB77E403FC88D",
      "merchantName": "MYSTORE",
      "payments": [
        {
          "paymentSystem": "2",
          "bin": null,
          "accountId": null,
          "installments": 1,
          "value": 16500,
          "referenceValue": 16500
        }
      ],
      "sharedTransaction": false
    }
  ]
}
```

| Field | Type | Description | Example |
| - | - | - | - |
| `updateStatus` | String | Indicates whether the payment information is up to date according to the order's items. The order can't be placed if the value is `outdated`. | `"updated"` |
| `installmentOptions` | Array of objects | Installment options available for each payment system. | See the following rows. |
| `installmentOptions[].paymentSystem` | Integer | Payment system ID. | `2` |
| `installmentOptions[].bin` | String or null | Card BIN (first digits of the card number). | `"411111"` |
| `installmentOptions[].paymentName` | String or null | Payment name. | `"Visa"` |
| `installmentOptions[].paymentGroupName` | String or null | Payment group name. | `"creditCardPaymentGroup"` |
| `installmentOptions[].value` | Integer | Total value assigned to this payment in cents. | `16500` |
| `installmentOptions[].installments` | Array of objects | Available installment options. | See the following rows. |
| `installmentOptions[].installments[].count` | Integer | Number of installments. | `2` |
| `installmentOptions[].installments[].hasInterestRate` | Boolean | Indicates whether the installment option has interest. | `false` |
| `installmentOptions[].installments[].interestRate` | Integer | Interest rate. | `0` |
| `installmentOptions[].installments[].value` | Integer | Value of each installment in cents. | `8250` |
| `installmentOptions[].installments[].total` | Integer | Total value of all installments in cents, including interest. | `16500` |
| `installmentOptions[].installments[].sellerMerchantInstallments` | Array of objects | Installment information for each seller merchant. Each object has the fields `id` (merchant ID), `count`, `hasInterestRate`, `interestRate`, `value`, and `total`. | `[{"id": "MYSTORE", "count": 2, "hasInterestRate": false, "interestRate": 0, "value": 8250, "total": 16500}]` |
| `paymentSystems` | Array of objects | Payment systems available for the order. | See the following rows. |
| `paymentSystems[].id` | Integer | Payment system ID. | `2` |
| `paymentSystems[].name` | String | Payment system name. | `"Visa"` |
| `paymentSystems[].groupName` | String | Payment group name. | `"creditCardPaymentGroup"` |
| `paymentSystems[].validator` | Object | Rules used to validate the card data of the payment system. | See the following rows. |
| `paymentSystems[].validator.regex` | String | Regular expression used to validate the card number. | `"^4"` |
| `paymentSystems[].validator.mask` | String | Card number mask. | `"9999 9999 9999 9999"` |
| `paymentSystems[].validator.cardCodeRegex` | String | Regular expression used to validate the card security code. | `"^[0-9]{3}$"` |
| `paymentSystems[].validator.cardCodeMask` | String | Card security code mask. | `"999"` |
| `paymentSystems[].validator.weights` | Array of integers | Weights used to validate the card number check digit. | `[2, 1, 2, 1]` |
| `paymentSystems[].stringId` | String | Payment system ID as a string. | `"2"` |
| `paymentSystems[].template` | String | Name of the template used to render the payment system at checkout. | `"creditCardPaymentGroup-template"` |
| `paymentSystems[].requiresDocument` | Boolean | Indicates whether a document is required. | `false` |
| `paymentSystems[].displayDocument` | Boolean | Indicates whether a document is displayed. | `false` |
| `paymentSystems[].isCustom` | Boolean | Indicates whether it's a custom payment system. | `false` |
| `paymentSystems[].description` | String or null | Payment system description. | `"Pay with your Visa card"` |
| `paymentSystems[].requiresAuthentication` | Boolean | Indicates whether authentication is required. | `false` |
| `paymentSystems[].dueDate` | String | Payment due date. | `"2026-10-09T14:59:00Z"` |
| `paymentSystems[].availablePayments` | String or null | Availability of payment. | `null` |
| `paymentSystems[].selected` | Boolean | Indicates whether this payment system has been selected. | `false` |
| `payments` | Array of objects | Payments chosen by the customer. | See the following rows. |
| `payments[].paymentSystem` | Integer | Payment system ID. | `2` |
| `payments[].paymentSystemName` | String | Payment system name. | `"Visa"` |
| `payments[].group` | String | Payment system group. | `"creditCardPaymentGroup"` |
| `payments[].bin` | String or null | Card BIN. | `null` |
| `payments[].accountId` | String or null | ID of the saved card account used in the payment. | `"71F2775D46BF44B1BF217F828F4E6131"` |
| `payments[].installments` | Integer | Selected number of installments. | `1` |
| `payments[].installmentsInterestRate` | Number | Interest rate of the installments. | `0` |
| `payments[].installmentsValue` | Integer | Value of each installment in cents. | `16500` |
| `payments[].value` | Integer | Total value assigned to this payment in cents, including interest. | `16500` |
| `payments[].referenceValue` | Integer | Reference value in cents used to calculate the total order value with interest. | `16500` |
| `payments[].hasDefaultBillingAddress` | Boolean | Indicates whether the billing address for this payment is the default address. | `true` |
| `giftCards` | Array of objects | Gift cards applied to or available for the order. | See the following rows. |
| `giftCards[].redemptionCode` | String | Gift card redemption code. | `"HYUO-TEZZ-QFFT-HTFR"` |
| `giftCards[].value` | Integer | Value of the gift card used in the order, in cents. | `500` |
| `giftCards[].balance` | Integer | Gift card balance in cents. | `500` |
| `giftCards[].name` | String | Gift card name. | `"loyalty-program"` |
| `giftCards[].id` | String | Gift card ID. | `"-1390324156495k195pmab4rall3di"` |
| `giftCards[].inUse` | Boolean | Indicates whether the gift card is being used in the order. | `true` |
| `giftCards[].isSpecialCard` | Boolean | Indicates whether the gift card is special, such as a loyalty program card. | `false` |
| `giftCardMessages` | Array of strings | Messages related to the gift cards. | `[]` |
| `availableAccounts` | Array | Saved cards available for the customer. | `[]` |
| `availableTokens` | Array | Payment tokens available for the customer. | `[]` |
| `availableAssociations` | Object | Available associations. | `{}` |
| `transactions` | Array of objects | Transactions related to the order. | See the following rows. |
| `transactions[].isActive` | Boolean | Indicates whether the transaction is active. | `true` |
| `transactions[].transactionId` | String | Transaction ID. | `"296D6D245C17437E823EB77E403FC88D"` |
| `transactions[].merchantName` | String | Merchant name. | `"MYSTORE"` |
| `transactions[].payments` | Array of objects | Payments of the transaction. | See the following rows. |
| `transactions[].payments[].accountId` | String | Account ID. | `"12"` |
| `transactions[].payments[].bin` | String or null | Card BIN. | `null` |
| `transactions[].payments[].installments` | Integer | Number of installments. | `1` |
| `transactions[].payments[].paymentSystem` | String | Payment system ID. | `"2"` |
| `transactions[].payments[].referenceValue` | Integer | Reference value in cents used to calculate interest, when it applies. | `16500` |
| `transactions[].payments[].value` | Integer | Payment value in cents, including interest, when it applies. | `16500` |
| `transactions[].sharedTransaction` | Boolean | Indicates whether the transaction is shared. | `false` |

### invoiceData

Object containing information about the order invoice, including the billing address. Returns `null` when no invoice data was added to the cart. Use the [Add invoice data](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/attachments/invoiceData) endpoint to add this information.

**Example:**

```json
"invoiceData": {
  "address": {
    "postalCode": "10019",
    "city": "New York",
    "state": "NY",
    "country": "USA",
    "street": "North 110th Street",
    "number": "52",
    "neighborhood": "Manhattan",
    "complement": "101",
    "reference": "Between the Upper West Side and Upper East Side",
    "geoCoordinates": [-73.9534529, 40.7986877]
  }
}
```

| Field | Type | Description | Example |
| - | - | - | - |
| `address` | Object | Billing address. | See the following rows. |
| `address.postalCode` | String | Postal code. | `"10019"` |
| `address.city` | String | City. | `"New York"` |
| `address.state` | String | State. | `"NY"` |
| `address.country` | String | Three-letter ISO code of the country. | `"USA"` |
| `address.street` | String | Street name. | `"North 110th Street"` |
| `address.number` | String | Street number. | `"52"` |
| `address.neighborhood` | String | Neighborhood. | `"Manhattan"` |
| `address.complement` | String | Address complement. | `"101"` |
| `address.reference` | String | Reference that helps locate the address. | `"Between the Upper West Side and Upper East Side"` |
| `address.geoCoordinates` | Array of numbers | Geographic coordinates of the address: longitude first, then latitude. | `[-73.9534529, 40.7986877]` |

## Promotions and marketing

### marketingData

Object containing promotion and campaign data, such as the coupon applied to the cart and the external and internal [UTM](https://help.vtex.com/en/tutorial/what-are-utm-source-utm-campaign-and-utm-medium--2wTz7QJ8KUG6skGAoAQuii) parameters. Returns `null` when no marketing data was added. Use the [Add marketing data](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/attachments/marketingData) endpoint to add this information.

**Example:**

```json
"marketingData": {
  "coupon": "free-shipping",
  "marketingTags": ["black-friday", "newsletter"],
  "utmSource": "app",
  "utmMedium": "CPC",
  "utmCampaign": "Black friday",
  "utmiPage": "home",
  "utmiPart": "banner-top",
  "utmiCampaign": "black-friday-banner"
}
```

| Field | Type | Description | Example |
| - | - | - | - |
| `coupon` | String | Coupon code applied to the cart. Sending an existing coupon code in this field returns the corresponding discount in the purchase. Use the [cart simulation](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForms/simulation) request to check which coupons might apply before placing the order. | `"free-shipping"` |
| `marketingTags` | Array of strings | Marketing tags, used to register campaign data or informative tags regarding promotions. Limited to a maximum of 50 items. | `["black-friday", "newsletter"]` |
| `utmSource` | String | Value of the `utm_source` parameter of the URL that led to the store. | `"app"` |
| `utmMedium` | String | Value of the `utm_medium` parameter of the URL that led to the store. | `"CPC"` |
| `utmCampaign` | String | Value of the `utm_campaign` parameter of the URL that led to the store. | `"Black friday"` |
| `utmiPage` | String or null | Value of the internal UTM `utmi_p` (page). | `"home"` |
| `utmiPart` | String or null | Value of the internal UTM `utmi_pc` (part). | `"banner-top"` |
| `utmiCampaign` | String or null | Value of the internal UTM `utmi_cp` (campaign). | `"black-friday-banner"` |

### ratesAndBenefitsData

Object containing the promotions (benefits) and taxes (rates) that apply to the order, and the teasers of promotions the customer can still qualify for.

**Example:**

```json
"ratesAndBenefitsData": {
  "rateAndBenefitsIdentifiers": [
    {
      "id": "d3b6a5f3-1e2c-4b5a-9c8d-7e6f5a4b3c2d",
      "name": "10% off on pet food",
      "featured": false,
      "description": "Get 10% off on all dry food",
      "matchedParameters": {},
      "additionalInfo": null
    }
  ],
  "teaser": []
}
```

| Field | Type | Description | Example |
| - | - | - | - |
| `rateAndBenefitsIdentifiers` | Array | Identifiers of the promotions and taxes applied to the order. | See the example above. |
| `teaser` | Array | Teasers of promotions and taxes that may apply to the order. | `[]` |

## Custom information

The sections in this group store information that isn't part of the standard `orderForm` structure.

### customData

Object containing custom information added to the cart by the store. Returns `null` when no custom data was added.

It supports two structures:

- `customApps`: custom fields grouped by app. See [Add and handle custom information in the order](https://developers.vtex.com/docs/guides/add-and-handle-custom-information-in-the-order) and the [Set multiple custom field values](https://developers.vtex.com/docs/api-reference/checkout-api#put-/api/checkout/pub/orderForm/-orderFormId-/customData/-appId-) endpoint.
- `customFields`: custom fields linked to the order, to an item, or to an address. See [Customizable fields with Checkout API](https://developers.vtex.com/docs/guides/customizable-fields-with-checkout-api).

**Example:**

```json
"customData": {
  "customApps": [
    {
      "id": "deliveryinfo",
      "major": 1,
      "fields": {
        "deliveryEstimate": "30",
        "deliveryInstructions": "Leave at the front door"
      }
    }
  ],
  "customFields": [
    {
      "linkedEntity": {
        "type": "address",
        "id": "7dfd4580-6340-437d-a8c8-c6c1f690c4fd"
      },
      "fields": [
        {
          "name": "desktop",
          "value": "DK1",
          "refId": "DK1"
        }
      ]
    }
  ]
}
```

| Field | Type | Description | Example |
| - | - | - | - |
| `customApps` | Array of objects or null | Custom apps created by the store. | See the following rows. |
| `customApps[].id` | String | App ID. | `"deliveryinfo"` |
| `customApps[].major` | Integer | App major version. | `1` |
| `customApps[].fields` | Object | Fields created by the store for the app, as key-value pairs. | `{"deliveryEstimate": "30"}` |
| `customFields` | Array of objects or null | Customizable fields created by the store. | See the following rows. |
| `customFields[].linkedEntity` | Object | Entity to which the custom fields are linked. | See the following rows. |
| `customFields[].linkedEntity.type` | String | Type of the linked entity. Possible values are `order`, `item`, and `address`. | `"address"` |
| `customFields[].linkedEntity.id` | String | ID of the linked entity. For `item`, it's the item `uniqueId`; for `address`, it's the `addressId`. Not used for `order`. | `"7dfd4580-6340-437d-a8c8-c6c1f690c4fd"` |
| `customFields[].fields` | Array of objects | Custom fields. | See the following rows. |
| `customFields[].fields[].name` | String | Custom field name. | `"desktop"` |
| `customFields[].fields[].value` | String | Custom field value. | `"DK1"` |
| `customFields[].fields[].refId` | String | Custom field reference ID. | `"DK1"` |

### openTextField

Optional field meant to hold free text information about the order, such as delivery notes. Returns `null` when empty.

We recommend using this field for text, not data formats such as `JSON`, even if escaped. To store structured data, see [Add and handle custom information in the order](https://developers.vtex.com/docs/guides/add-and-handle-custom-information-in-the-order).

**Example:**

```json
"openTextField": {
  "value": "Please ring the bell twice."
}
```

| Field | Type | Description | Example |
| - | - | - | - |
| `value` | String | Additional information about the order. | `"Please ring the bell twice."` |

### hooksData

Object containing hooks information of the cart. Returns `null` when no hook applies.

**Example:**

```json
"hooksData": null
```

## Store and commercial context

### storePreferencesData

Object containing data from the store configuration, stored in VTEX License Manager, such as country, currency, and time zone.

**Example:**

```json
"storePreferencesData": {
  "countryCode": "BRA",
  "saveUserData": true,
  "timeZone": "E. South America Standard Time",
  "currencyCode": "BRL",
  "currencyLocale": 1046,
  "currencySymbol": "R$",
  "currencyFormatInfo": {
    "currencyDecimalDigits": 2,
    "currencyDecimalSeparator": ",",
    "currencyGroupSeparator": ".",
    "currencyGroupSize": 3,
    "startsWithCurrencySymbol": true
  }
}
```

| Field | Type | Description | Example |
| - | - | - | - |
| `countryCode` | String | Three-letter ISO code of the store country. | `"BRA"` |
| `saveUserData` | Boolean | Indicates whether the store saves the customer data. | `true` |
| `timeZone` | String | Store time zone. | `"E. South America Standard Time"` |
| `currencyCode` | String | ISO 4217 code of the store currency. | `"BRL"` |
| `currencyLocale` | Integer | Locale ID (LCID) of the currency. | `1046` |
| `currencySymbol` | String | Currency symbol. | `"R$"` |
| `currencyFormatInfo` | Object | Currency formatting information. | See the following rows. |
| `currencyFormatInfo.currencyDecimalDigits` | Integer | Number of decimal digits. | `2` |
| `currencyFormatInfo.currencyDecimalSeparator` | String | Decimal separator. | `","` |
| `currencyFormatInfo.currencyGroupSeparator` | String | Thousands separator. | `"."` |
| `currencyFormatInfo.currencyGroupSize` | Integer | Number of digits in each group of thousands. | `3` |
| `currencyFormatInfo.startsWithCurrencySymbol` | Boolean | Indicates whether the currency symbol is displayed before the value. | `true` |

### commercialConditionData

Object containing information about the [commercial conditions](https://help.vtex.com/en/tutorial/registering-a-commercial-condition--tutorials_445) that apply to the order. Returns `null` when no commercial condition applies.

**Example:**

```json
"commercialConditionData": null
```

### subscriptionData

Object containing the [subscription](https://help.vtex.com/en/tutorial/how-subscriptions-work--frequentlyAskedQuestions_4453) information of the items in the cart. Returns `null` when the cart has no subscriptions. Use the [Add subscription data](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/attachments/subscriptionData) endpoint to add this information.

**Example:**

```json
"subscriptionData": {
  "subscriptions": [
    {
      "itemIndex": 0,
      "plan": {
        "type": "RECURRING_PAYMENT",
        "frequency": {
          "periodicity": "MONTH",
          "interval": 1
        },
        "validity": {
          "begin": "2026-10-02",
          "end": "2027-10-02"
        }
      }
    }
  ]
}
```

| Field | Type | Description | Example |
| - | - | - | - |
| `subscriptions` | Array of objects | Subscriptions of the cart items. | See the following rows. |
| `subscriptions[].itemIndex` | Integer | Index of the cart item the subscription refers to, starting at `0`. | `0` |
| `subscriptions[].plan` | Object | Subscription plan information. | See the following rows. |
| `subscriptions[].plan.type` | String | Type of the subscription plan. | `"RECURRING_PAYMENT"` |
| `subscriptions[].plan.frequency` | Object | Frequency in which the subscription order will be placed. | See the following rows. |
| `subscriptions[].plan.frequency.periodicity` | String | Time unit of the subscription frequency. Possible values are `DAY`, `WEEK`, `MONTH`, and `YEAR`. | `"MONTH"` |
| `subscriptions[].plan.frequency.interval` | Integer | Number of `periodicity` units between each subscription order. | `1` |
| `subscriptions[].plan.validity` | Object | Period in which the subscription is valid. | See the following rows. |
| `subscriptions[].plan.validity.begin` | String | Date when the subscription becomes valid, in the `YYYY-MM-DD` format. | `"2026-10-02"` |
| `subscriptions[].plan.validity.end` | String | Date when the subscription expires, in the `YYYY-MM-DD` format. | `"2027-10-02"` |

## Server messages

### messages

Array containing one object for each message generated by the server while processing the request, such as errors, warnings, and information about changes in the cart (for example, a price change or an unavailable item). Use the [Clear orderForm messages](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/messages/clear) endpoint to remove them. See the possible messages in [Checkout error codes](https://developers.vtex.com/docs/guides/checkout-error-codes).

**Example:**

```json
"messages": [
  {
    "code": null,
    "status": "error",
    "text": "Voucher code AAAA-BBBB-CCCC-DDDD was not found in the system"
  }
]
```

| Field | Type | Description | Example |
| - | - | - | - |
| `code` | String or null | Message code. | `null` |
| `status` | String | Message severity. Possible values are `error`, `warning`, and `info`. | `"error"` |
| `text` | String | Message text, according to the cart locale. | `"Voucher code AAAA-BBBB-CCCC-DDDD was not found in the system"` |
