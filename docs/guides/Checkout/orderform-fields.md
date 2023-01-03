---
title: "orderForm"
slug: "orderform-fields"
hidden: false
createdAt: "2020-09-02T13:59:41.676Z"
updatedAt: "2022-10-27T19:51:49.586Z"
---
The `orderForm` is the main object processed by VTEX checkout, and one of the most important data structures in the architecture of every VTEX store.

It stores a lot of contextual information about the order which is important to the processing of the order: order items, client's personal data, delivery address, freight information, etc. 

Using VTEX APIs this information can be accessed, processed, and even changed on certain occasions. 

VTEX's Checkout API is one of the main interfaces interacting with the `orderForm` object. Most of its operations will return the `orderForm` or part of it.

The object's basic structure is:
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"allowManualPrice\": boolean,\n  \"canEditData\": boolean,\n  \"clientPreferencesData\": {},\n  \"clientProfileData\": {},\n  \"commercialConditionData\": {},\n  \"customData\": {},\n  \"giftRegistryData\": {},\n  \"hooksData\": {},\n  \"ignoreProfileData\": boolean,\n  \"isCheckedIn\": boolean,\n  \"itemMetadata\": {},\n  \"items\": {},\n  \"itemsOrdination\": {},\n  \"loggedIn\": boolean,\n  \"marketingData\": {},\n  \"messages\": [],\n  \"openTextField\": {},\n  \"orderFormId\": \"426effeba9210\",\n  \"paymentData\": {},  \n  \"ratesAndBenefitsData\": {},\n  \"salesChannel\": \"1\",\n  \"selectableGifts\": {},\n  \"sellers\": {},\n  \"shippingData\": {},\n  \"storeId\": {},\n  \"storePreferencesData\": {},\n  \"totalizers\": {},\n  \"userProfileId\": {},\n  \"userType\": {},\n  \"value\": number\n}",
      "language": "json"
    }
  ]
}
[/block]
This structure is made of many __sections__.
[block:callout]
{
  "type": "warning",
  "body": "Any properties representing monetary values will have **cents** as their units. (e.g. `10390` means **R$103,90** in Brazilian stores)"
}
[/block]
In the following menu, you can find details regarding these sections. 

# `OrderForm` Sections

- [clientPreferencesData](#clientpreferencesdata)
- [clientProfileData](#clientprofiledata)
- [commercialConditionData](#commercialconditiondata)
- [customData](#customdata)
- [giftRegistryData](#giftregistrydata)
- [hooksData](#hooksdata)
- [items](#items)
    - [items[].priceDefinition](#itemspricedefinition)
- [invoiceData](#invoicedata)
- [itemsOrdination](#itemsordination)
- [marketingData](#marketingdata)
- [messages](#messages)
- [openTextField](#opentextfield)
- [paymentData](#paymentdata)
- [ratesAndBenefitsData](#ratesandbenefitsdata)
- [selectableGifts](#selectablegifts)
- [sellers](#sellers)
- [shippingData](#shippingdata)
- [storeId](#storeid)
- [storePreferencesData](#storepreferencesdata)
- [subscriptionData](#subscriptiondata)
- [totalizers](#totalizers)

## clientPreferencesData

Object containing preferences from the client who placed the order.

**Example:**
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"locale\": \"pt-BR\",\n  \"optinNewsLetter\": true\n}",
      "language": "json"
    }
  ]
}
[/block]
| Field     | Type     | Description     |
| ---------- | ---------- | ---------- |
| locale       | String       | Client's locale. Examples: "pt-BR" and "en-US". The method `sendLocale()`, from vtex.js, changes the value of this field.       |
| optinNewsLetter       | Boolean       | `true` if the client opted to receive newsletters from the store.       |


## clientProfileData

Object containing the data of the customer who placed the order.

If the customer has not yet informed her or his e-mail, much of the data may be empty (`null`).

If the customer's e-mail has not yet been confirmed, several personal data will be censored, that is, some of its parts will be hidden by asterisks to avoid identification.

**Example:** 
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"email\": \"customer@mailprovider.com\",\n  \"firstName\": \"Bre******\",\n  \"lastName\": \"Bar******\",\n  \"document\": \"*1*2*5*5*3*\",\n  \"documentType\": \"cpf\",\n  \"phone\": \"******0879\",\n  \"corporateName\": null,\n  \"tradeName\": null,\n  \"corporateDocument\": null,\n  \"stateInscription\": null,\n  \"corporatePhone\": null,\n  \"isCorporate\": false\n}",
      "language": "json"
    }
  ]
}
[/block]
| Field      | Type      | Description |
| ---------- | ---------- | ---------- |
|      email      |    String    |  Customer's email.      |
|   firstName         |     String       |  Customer's first name.     |
|    lastName        |   String         |   Customer's last name.      |
|   document         |   String         |  Document number informed by the customer.          |
|   documentType         |   String         |  Type of the document informed by the customer.          |
|   phone         |     String       |   Customer's phone number.    |
|    corporateName        |  String          |     If it's a legal entity, here goes the company name.       |
|  tradeName          |  String          |     If legal entity, here goes the trade name.       |
|  corporateDocument          |      String      |   If legal entity, here goes the corporate document.         |
|   stateInscription         |    String        |   If legal entity, here goes the state inscription.         |
|   corporatePhone         |    String        |   If legal entity, here goes the company phone.        |
|   isCorporate         |     Boolean       |  It has the value `true` if it's a legal entity.         |


## commercialConditionData
[block:callout]
{
  "type": "warning",
  "title": "Work in progress",
  "body": "This guide is currently being written and published as content becomes available."
}
[/block]
## customData

During the checkout process, some stores need to include data gathered from the client that is not part of our standard `orderForm` format (e.g. gender, cell phone number, age). 

To do that you will need to create extra fields in the `orderForm` and those will be located inside the `customData` parameter

**Example:** 
[block:code]
{
  "codes": [
    {
      "code": "\"customData\": {\n\t\"attachmentId\": \"customData\",\n\t\"customApps\": [\n\t\t{\n\t\t\t\"fields\": {\n\t\t\t\t\"number\": \"78550693\",\n\t\t\t\t\"street\": \"Rua Voluntários da Pátria\",\n\t\t\t\t\"complement\": \"Em frente à Torre Citi\",\n\t\t\t\t\"name\": \"101 - Delco Autopista,\n\t\t\t\t\"neighborhood\": \"Botafogo\",\n\t\t\t\t\"city\": \"Rio de Janeiro\",\n\t\t\t\t\"state\": \"RJ\"\n\t\t\t},\n\t\t\t\"id\": \"pickupinfo\",\n\t\t\t\"major\": 1\n\t\t},\n\t\t{\n\t\t\t\"fields\": {\n\t\t\t\t\"deliveryEstimate\": \"30\"\n\t\t\t},\n\t\t\t\"id\": \"deliveryinfo\",\n\t\t\t\"major\": 1\n\t\t}\n\t]\n}",
      "language": "json"
    }
  ]
}
[/block]
| Field      | Type      | Description |
| ---------- | ---------- | ---------- |
|    customApps |    Array  |  Array containing the apps created by the store.      |
|    fields |    Object  |  Object that contains the fields created by the store for each app.      |
|    id   |    String   |   App ID.      |
|    major   |        |         |



## giftRegistryData

Object containing the gift registration list data.

**Example:** 
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"giftRegistryId\": \"22222\",  \n  \"giftRegistryType\": null,\n  \"giftRegistryTypeName\": null,\n  \"addressId\": null,\n  \"description\": \"gift1\"    \n}",
      "language": "json"
    }
  ]
}
[/block]
| Field      | Type      | Description |
| ---------- | ---------- | ---------- |
|    giftRegistryId |    String  |  Gift registry ID.      |
|    giftRegistryType |    String  |  Gift registry type.      |
|    giftRegistryTypeName   |    String   |   Gift registration typen name.       |
|    addressId   |    String   |   Address ID.      |
|    description   |    String   |   Gift registry description.      |


## hooksData
[block:callout]
{
  "type": "warning",
  "body": "This guide is currently being written and published as content becomes available."
}
[/block]
## items

it is an array containing an object describing every item in the buyer's cart.

**Example:** 
[block:code]
{
  "codes": [
    {
      "code": "\"items\": [\n        {\n            \"uniqueId\": \"3B31329E5DDA4A1A81449DD7466D9575\",\n            \"id\": \"4\",\n            \"productId\": \"3\",\n            \"productRefId\": \"\",\n            \"refId\": null,\n            \"ean\": \"978073487962\",\n            \"name\": \"Mild Hair Cleanser 50 ml\",\n            \"skuName\": \"50 ml\",\n            \"modalType\": null,\n            \"parentItemIndex\": null,\n            \"parentAssemblyBinding\": null,\n            \"priceValidUntil\": \"2022-04-07T18:31:11Z\",\n            \"tax\": 0,\n            \"price\": 3190,\n            \"listPrice\": 3190,\n            \"manualPrice\": 1700,\n            \"manualPriceAppliedBy\": \"in542e51-5863-4c34-8i86-ed8fcf597a09\",\n            \"sellingPrice\": 1700,\n            \"rewardValue\": 0,\n            \"isGift\": false,\n            \"additionalInfo\": {\n                \"dimension\": null,\n                \"brandName\": \"VALCOSMETICS\",\n                \"brandId\": \"2000000\",\n                \"offeringInfo\": null,\n                \"offeringType\": null,\n                \"offeringTypeId\": null\n            },\n            \"preSaleDate\": null,\n            \"productCategoryIds\": \"/2/\",\n            \"productCategories\": {\n                \"2\": \"Computers\"\n            },\n            \"quantity\": 3,\n            \"seller\": \"seller1\",\n            \"sellerChain\": [\n                \"seller1\"\n            ],\n            \"imageUrl\": \"http://cosmeticsstore.vteximg.com.br/arquivos/ids/155401-55-55/ID-001-MAIN.jpg?v=637109313796670000\",\n            \"detailUrl\": \"/mild-hair-cleanser/p\",\n            \"bundleItems\": [],\n            \"attachments\": [],\n            \"attachmentOfferings\": [],\n            \"offerings\": [],\n            \"priceTags\": [\n                {\n                    \"name\": \"DISCOUNT@MANUALPRICE\",\n                    \"value\": -4470,\n                    \"rawValue\": -44.7,\n                    \"isPercentual\": false,\n                    \"identifier\": null\n                }\n            ],\n            \"availability\": \"available\",\n            \"measurementUnit\": \"un\",\n            \"unitMultiplier\": 1.0000,\n            \"manufacturerCode\": null,\n            \"priceDefinition\": {\n                “sellingPrice”: [\n                    {\n                        “quantity”: 1,\n                        “value”: 1700\n                    }\n                ],\n                “total”: 5100\n            }\n        }\n    ]",
      "language": "json"
    }
  ]
}
[/block]
| Field      | Type      | Description |
| ---------- | ---------- | ---------- |
|    uniqueId |    String  |  This string is the unique identifier for each occurrence of a SKU in an order. Two same SKUs in an order will have different uniqueIds. Obsolete field.     |
|    id |    String  |  ID of the item.     |
|    productId   |    String   |   Product ID.       |
|    productRefId   |    String   |   Product Ref ID.      |
|    refId   |    String   |   Ref ID.    |
|    ean |    String  |  EAN (codebar) field from [SKU registry](https://help.vtex.com/pt/tutorial/cadastrar-o-codigo-de-barra-dos-skus-para-o-instore--2jkOdRB4XSMG2ke0uUQIKS#cadastrar-o-campo-ean).      |
|    name |    String  |  Product name.     |
|    skuName |    String  |  SKU name.    |
|    modalType   |    String   |   Modal type.     |
|    parentItemIndex   |    Integer   |   Parent item index.     |
|    parentAssemblyBinding   |    String   |   Parent assembly binding.   |
|    priceValidUntil |    String  |  Price expiration date and time.    |
|    tax |    Integer |  Tax value in cents.    |
|    price   |    Integer   |   Price in cents.    |
|    listPrice   |    Integer  |   List price in cents.    |
|    manualPrice   |    Integer  |   Manual price in cents.   |
|    manualPriceAppliedBy |    String  |  User that applied the manual price, if that is the case.    |
|    sellingPrice |    Integer |  Selling price in cents. Note that this field may be subject to rounding discrepancies. We recommend retrieving data from the `priceDefinition` data structure instead.   |
|    rewardValue   |    Integer   |   Reward value in cents.   |
|    isGift   |    Boolean  |   Indicates whether item is a gift.   |
|    additionalInfo   |    Object  |   Additional information. |
|    dimension |    String  |  Dimension.    |
|    brandName |    String |  Brand name.   |
|    brandId |    String |  Brand ID.   |
|    offeringInfo  |    String  |   Offering information.  |
|    offeringType  |    String|   Offering type.   |
|    offeringTypeId  |    String  |   Offering type ID. |
|    preSaleDate |    String  |  Presale date.   |
|    productCategoryIds |    String |  Product category IDs.  |
|    productCategories  |    Object  |   Object, where each field is an ID from `productCategoryIds`.  |
|    {ID}  |    String|   Product category corresponding to the ID in the field key.   |
|    quantity  |    Integer  |   Quantity. |
|    seller |    String  |  Seller information.   |
|    sellerChain |    Array of strings |  Sellers involved in the chain. The list should contain only one seller, unless it is a [Multilevel Omnichannel Inventory](https://help.vtex.com/en/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4) order.   |
|    imageUrl  |    String  |   Image URL.  |
|    detailUrl  |    String|   Detail URL.   |
|    bundleItems |    Array of objects |   Information on services sold along with the SKU. Example: a gift package. |
|    type |    String  |  Service type.  |
|    id |    Integer |  Service identifier. |
|   name  |    String |   Service name.  |
|    price  |     Integer |   Service price in cents.  |
|    attachments |    Array of strings |   Array containing information on attachments. |
|    priceTags |    Array of objects  |  Array of price tags, each of which, modifies the price in some way, like discounts or rates that apply to the item in the context of the order.  |
|    name  |     String |   Price tag name. |
|    value |    Integer  |  Price tag value.  |
|    rawValue |    Integer |   Price tag raw value. |
|   isPercentual  |    Boolean |   Indicates whether price tag value is applied through a percentage.  |
|    identifier |    String |  Price tag identifier. |
|    owner |    String |  Identification of the responsible for the price tag. |
|    availability |    String |  SKU availability. The values are: `available`, `withoutStock`and `cannotBeDelivered`. Only SKUs with  `available` value can be sold and delivered. |
|   measurementUnit  |    String |   Measurement unit.  |
|    unitMultiplier  |     String |   Unit multiplier. |
|    manufacturerCode |    String |   Manufacturer code. |
|    priceDefinition |    Object  |  Price information for all units of a specific item. |
|    calculatedSellingPrice |    Integer |  Item's calculated unitary selling price in cents. |
|   total  |     Integer |   Total value for all units of the item in cents. |
|    sellingPrices  |     Array of objects |   Array of objects, each containing value (in cents) and quantity for the different rounding instances that can be combined to form the correctly rounded total. |
|    value |    Integer |   Value in cents for that specific rounding. |
|    quantity |    Integer |   Rounding quantity, meaning how many items are rounded to this value. |
[block:callout]
{
  "type": "warning",
  "body": "If you use integrations that consume price data, such as checkout or order integrations, note that the field `sellingPrice` may be subject to rounding discrepancies. We recommend retrieving data from the `priceDefinition` data structure instead."
}
[/block]

### items[].priceDefinition

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

| **Atribute**                                   | **Type** | **Description**                                                                                                                                                      |
|------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| items[].priceDefinition                        | Object   | Price information for all units of a specific item.                                                                                                                  |
| items[].priceDefinition.total                  | Integer  | Total value for all units of the item in cents.                                                                                                                      |
| items[].priceDefinition.calculatedSellingPrice | Integer  | Item's calculated unitary selling price in cents.                                                                                                                    |
| items[].priceDefinition.sellingPrices          | Array    | Array of objects, each containing `value` (in cents) and `quantity` for the different rounding instances that can be combined to form the correctly rounded `total`. |

## invoiceData

This is an object containing information pertinent to the order's invoice.
[block:code]
{
  "codes": [
    {
      "code": "{\n   \"address\": {\n   \"postalCode\": \"******000\",\n   \"city\": \"Rio ** *******\",\n   \"state\": \"RJ\",\n   \"country\": \"BRA\",\n   \"street\": \"Rua *** *****nte\",\n   \"number\": \"***\",\n   \"neighborhood\": \"Bot*****\",\n   \"complement\": \"*** ** *\",\n   \"reference\": null\n  \t},\n    \"settleInvoices\":[]  \n}     ",
      "language": "json"
    }
  ]
}
[/block]
| Field      | Type      | Description |
| ---------- | ---------- | ---------- |
|    address |    Object  |  Address information.      |
|    settleInvoices |    String  |  List of strings corresponding to invoice numbers.      |

## itemsOrdination

This is an object containing information about the ordering of items within the orderForm.

**Example:** 
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"criteria\": \"NAME\",  \n  \"ascending\": true  \n}",
      "language": "json"
    }
  ]
}
[/block]
| Field      | Type      | Description |
| ---------- | ---------- | ---------- |
|    criteria  |    String |  Criteria adopted to order the items in the list. The values are: `NAME`, `ADD_TIME` (date information), and `GIFT` (non-gift items are mentioned before gift items).              |
|    ascending |    String |  Indicates whether the ordering is ascending.              |


## marketingData

This object contains promotion data such as coupon tracking information and internal or external UTMs. 

**Example:** 
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"attachmentId\": \"marketingData\",\n  \"coupon\": null,\n  \"marketingTags\": [],\n  \"utmCampaign\": \"christmas\",\n  \"utmMedium\": null,\n  \"utmSource\": \"fb\",\n  \"utmiCampaign\": \"\",\n  \"utmiPart\": \"\",\n  \"utmipage\": \"\"  \n}",
      "language": "json"
    }
  ]
}
[/block]
| Field      | Type      | Description |
| ---------- | ---------- | ---------- |
|    attachmentId  |    String |   Attachment ID.     |
|    coupon |    String |   Coupon code information.     |
|    marketingTags |    Array |   Marketing tags information. This field can be used to register campaign data or informative tags regarding promotions.    |
|    utmCampaign  |    String |  Value of the `utm_campaign` parameter of the URL that led to the request.      |
|    utmMedium  |    String |  Value of the `utm_medium` parameter of the URL that led to the request.      |
|    utmSource  |    String |  Value of the `utm_source` parameter of the URL that led to the request.      |
|    utmiCampaign  |    String |  Internal UTM value `utmi_cp`.     |
|    utmiPart  |    String |  Internal UTM value `utmi_pc`.      |
|    utmipage  |    String |  Internal UTM value `utmi_p`.      |


## messages

This array contains an object for each message generated by our servers while processing the request. 

**Example:**
[block:code]
{
  "codes": [
    {
      "code": "[\n  {\n    \"code\": null,\n    \"status\": \"error\",\n    \"text\": \"Voucher code AAAA-BBBB-CCCC-DDDD was not found in the system\"\n  }\n]",
      "language": "json"
    }
  ]
}
[/block]

## openTextField

Optional field meant to hold additional information about the order. We recommend using this field for text, not data formats such as `JSON` even if escaped. For that purpose, see [How to add and handle custom information in the order](https://developers.vtex.com/vtex-rest-api/docs/how-to-add-and-handle-custom-information-in-the-order).
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"value\": \"{\\\"Phones\\\":[\\\"55555555\\\"]}\"\n  }",
      "language": "json"
    }
  ]
}
[/block]
| Field      | Type      | Description |
| ---------- | ---------- | ---------- |
|    value |    String |  Additional information about the order.               |


## paymentData

This object contains all payment information inserted for this purchase. 

**Example:**
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"giftCards\": [\n    {\n      \"redemptionCode\": \"HYUO-TEZZ-QFFT-HTFR\",\n      \"value\": 500,\n      \"balance\": 500,\n      \"name\": null,\n      \"id\": \"-1390324156495k195pmab4rall3di\",\n      \"inUse\": true,\n      \"isSpecialCard\": false\n    }, {\n      \"redemptionCode\": \"MTHU-WNTD-VXJW-TIDC\",\n      \"value\": 0,\n      \"balance\": 700000,\n      \"name\": \"loyalty-program\",\n      \"id\": \"122\",\n      \"inUse\": false,\n      \"isSpecialCard\": true\n    }\n  ],\n  \"giftCardMessages\": [],\n  \"availableAccounts\": [\n    {\n      \"accountId\": \"71F2775D46BF44B1BF217F828F4E6131\",\n      \"paymentSystem\": \"2\",\n      \"paymentSystemName\": \"Visa\",\n      \"cardNumber\": \"************1111\",\n      \"availableAddresses\": [\"-1363804954758\", \"-1366200971560\"]\n    }\n  ],\n  \"availableTokens\": [],\n  \"installmentOptions\": [\n    {\n      \"paymentSystem\": \"2\",\n      \"value\": 16175,\n      \"installments\": [\n        {\n          \"count\": 1,\n          \"hasInterestRate\": false,\n          \"interestRate\": 0,\n          \"value\": 16175,\n          \"total\": 16175\n        }, {\n          \"count\": 2,\n          \"hasInterestRate\": false,\n          \"interestRate\": 132,\n          \"value\": 4178,\n          \"total\": 16712\n        }\n      ]\n    }\n  ],\n  \"paymentSystems\": [\n    {\n      \"id\": 2,\n      \"name\": \"Visa\",\n      \"groupName\": \"creditCardPaymentGroup\",\n      \"validator\": {\n        \"regex\": \"^4\",\n        \"mask\": \"9999 9999 9999 9999\",\n        \"cardCodeRegex\": \"[^0-9]\",\n        \"cardCodeMask\": \"999\",\n        \"weights\": [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]\n      },\n      \"stringId\": null,\n      \"template\": \"creditCardPaymentGroup-template\",\n      \"requiresDocument\": false,\n      \"selected\": false,\n      \"isCustom\": false,\n      \"description\": null\n    }\n  ],\n  \"payments\": [\n    {\n      \"accountId\": null,\n      \"bin\": null,\n      \"installments\": 2,\n      \"paymentSystem\": \"12\",\n      \"referenceValue\": 16175,\n      \"value\": 16175\n    }\n  ]\n}",
      "language": "json"
    }
  ]
}
[/block]
| Field      | Type      | Description |
| ---------- | ---------- | ---------- |
|    giftCards  |    Array  |    Gift cards information.    |
|    giftCardMessages |    Array  |    Gift cards message information.    |
|    availableAccounts |    Array  |    Available accounts information.    |
|    availableTokens  |    Array  |    Available tokes information.    |
|    installmentOptions  |    Array  | For accurate information on installment options and values, we recommend using the [Cart installment endpoint](https://developers.vtex.com/vtex-rest-api/reference/shopping-cart#getcartinstallments), instead of this field's data. |
|    paymentSystems |    Array  |    Payment systems information.    |
|    payments  |    Array  |    Payments information.    |
|    updateStatus    |    String    |    Checkout can not be concluded if value is `"outdated"`.    |
[block:callout]
{
  "type": "warning",
  "title": "Work in progress",
  "body": "This guide is currently being written and published as content becomes available."
}
[/block]
## ratesAndBenefitsData

Information on rates and benefits that apply to the order.

**Example:** 
[block:code]
{
  "codes": [
    {
      "code": "{\n\t\"rateAndBenefitsIdentifiers\": [\n    {\n\t\t\t\"items\": {}\n    }\n  ],\n\t\"teaser\":[\n    {\n\t\t\t\"items\": {}\n    }\n\t]\n}\n",
      "language": "json"
    }
  ]
}
[/block]
| Field      | Type      | Description |
| ---------- | ---------- | ---------- |
|    rateAndBenefitsIdentifiers    |    Array    |    List with rates and benefits identifiers.    |
|    items    |   Object    |    Object that contains identifiers information.    |
|    teaser    |    Array   |    List with rates and benefits teasers.    |
|    items    |    Object   |    Object that contains teasers information.  |


## selectableGifts

Array containing the data of the item selected as a gift.
[block:code]
{
  "codes": [
    {
      "code": "[\n  {\n    \"id\": null,\n    \"availableQuantity\": \"3\",\n    \"availableGifts\": {\n      \"items\": [\n\t\t\t\t\t\t\t\t{},\n        \t\t\t   \"isSelected\": true\n\t\t\t\t\t\t\t ]\n  }\n]",
      "language": "json"
    }
  ]
}
[/block]
| Field      | Type      | Description |
| ---------- | ---------- | ---------- |
|    id    |    String    |    Identification of the selectable gifts list.    |
|    availableQuantity    |    Integer   |    Number of items available.    |
|    items   |    Integer   |    Array containing an object describing each item that can be selected as a gift.    |
|    isSelected    |    Boolean   |    Indication if the item was selected as a gift.    |


## sellers

An array containing an object for each seller being used in the order.

**Example:**
[block:code]
{
  "codes": [
    {
      "code": "[\n  {\n    \"id\": \"1\",\n    \"name\": \"meuamigopet\",\n    \"logo\": \"http://portal.vtexcommerce.com.br/arquivos/logo.jpg\"\n  }\n]",
      "language": "json"
    }
  ]
}
[/block]
| Field      | Type      | Description |
| ---------- | ---------- | ---------- |
|    id  |    String  |   ID of the seller.     |
|    name |    String  |   Name of the seller.     |
|    logo  |    String  |  URL pointing to where the image is hosted.     |


## shippingData

This object contains shipping information for the order.

**Example:**
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"attachmentId\": \"shippingData\",\n  \"address\": {\n    \"addressType\": \"residential\",\n    \"receiverName\": \"Gui***rme\",\n    \"addressId\": \"-1368194386810\",\n    \"postalCode\": \"******000\",\n    \"city\": \"Rio ** *******\",\n    \"state\": \"RJ\",\n    \"country\": \"BRA\",\n    \"street\": \"Rua *** *****nte\",\n    \"number\": \"***\",\n    \"neighborhood\": \"Bot*****\",\n    \"complement\": \"*** ** *\",\n    \"reference\": null\n  },\n  \"availableAddresses\": [\n    {\n      \"addressType\": \"residential\",\n      \"receiverName\": \"Gui***rme\",\n      \"addressId\": \"-1368194386810\",\n      \"postalCode\": \"******000\",\n      \"city\": \"Rio ** *******\",\n      \"state\": \"RJ\",\n      \"country\": \"BRA\",\n      \"street\": \"Rua *** *****nte\",\n      \"number\": \"***\",\n      \"neighborhood\": \"Bot*****\",\n      \"complement\": \"*** ** *\",\n      \"reference\": null\n    }\n  ],\n  \"logisticsInfo\": [\n    {\n      \"itemIndex\": 0,\n      \"selectedSla\": \".Transportadora\",\n      \"selectedDeliveryChannel\": \"delivery\",\n      \"addressId\": \"teste\",\n      \"slas\": [\n        {\n          \"id\": \".Transportadora\",\n          \"deliveryChannel\": \"delivery\",\n          \"name\": \".Transportadora\",\n          \"deliveryIds\": [\n            {\n              \"courierId\": \"67\",\n              \"warehouseId\": \"1_1\",\n              \"dockId\": \"1_1_1\",\n              \"courierName\": \"Transportadora\",\n              \"quantity\": 1\n            }\n          ],\n          \"shippingEstimate\": \"3d\",\n          \"shippingEstimateDate\": null,\n          \"lockTTL\": null,\n          \"availableDeliveryWindows\": [],\n          \"deliveryWindow\": null,\n          \"price\": 956,\n          \"tax\": 0\n        }, {\n          \"id\": \"Agendada\",\n          \"name\": \"Agendada\",\n          \"deliveryIds\": [\n            {\n              \"courierId\": \"FA02F72F-FEBD-41A0-AF70-83A77E8C77A0\",\n              \"warehouseId\": \"1_1\",\n              \"dockId\": \"1_1_1\",\n              \"courierName\": \"Entrega agendada\",\n              \"quantity\": 1\n            }\n          ],\n          \"shippingEstimate\": \"90d\",\n          \"shippingEstimateDate\": null,\n          \"lockTTL\": null,\n          \"availableDeliveryWindows\": [\n            {\n              \"startDateUtc\": \"2014-04-21T09:00:00+00:00\",\n              \"endDateUtc\": \"2014-04-21T12:00:00+00:00\",\n              \"listprice\": 1000,\n              \"tax\": 0\n            }, {\n              \"startDateUtc\": \"2014-04-21T13:00:00+00:00\",\n              \"endDateUtc\": \"2014-04-21T17:00:00+00:00\",\n              \"listprice\": 1000,\n              \"tax\": 0\n            }\n          ],\n          \"deliveryWindow \": [\n            {\n              \"startDateUtc\": \"2014-04-21T09:00:00+00:00\",\n              \"endDateUtc\": \"2014-04-21T12:00:00+00:00\",\n              \"listprice\": 1000,\n              \"tax\": 0\n            }, {\n              \"startDateUtc\": \"2014-04-21T13:00:00+00:00\",\n              \"endDateUtc\": \"2014-04-21T17:00:00+00:00\",\n              \"listprice\": 1000,\n              \"tax\": 0\n            }\n          ],          \n          \"price\": 1220,\n          \"tax\": 0,\n          \"pickupStoreInfo\": {\n              \"isPickupStore\": false,\n              \"friendlyName\": null,\n              \"address\": null,\n              \"additionalInfo\": null,\n              \"dockId\": null\n            },\n            \"pickupPointId\": null,\n            \"pickupDistance\": 0,\n            \"polygonName\": null,\n            \"transitTime\": \"3bd\"\n          }\n        ],\n         \"shipsTo\": [\n           \"BRA\",\n           \"COL\",\n           \"USA\"\n        ],\n         \"itemId\": \"2\",\n         \"deliveryChannels\": [\n           {\n             \"id\": \"delivery\"\n           },\n           {\n             \"id\": \"pickup-in-point\"\n           }\n         ]\n       }\n      ],\n  \"selectedAddresses\": []\n}",
      "language": "json"
    }
  ]
}
[/block]
| Field      | Type      | Description |
| ---------- | ---------- | ---------- |
|    attachmentId  |    String  |   Attachment ID.     |
|    address  |    Object  |   Address information.     |
|    availableAddresses  |    Array  |   Information about available shipping addresses.    |
|    logisticsInfo  |    Array  |   Logistics information.     |
|    itemIndex  |    Integer  |   Index corresponding to the position of the object in the `items` array.     |
|    selectedSla  |    String  |   SLA selected by the customer.     |
|    selectedDeliveryChannel  |    String  |   Delivery channel selected by the customer.     |
|    addressId  |    String  |   Address ID.    |
|    slas |    Array  |   Information on available SLAs.     |
|    id |    String  |   SLA ID.    |
|    deliveryChannel |    String  |   Delivery channel.    |
|    name |    String  |   SLA name.    |
|    deliveryIds |    Array  |   Information on each delivery ID.    |
|    courierId |    String  |   Courier ID.    |
|    warehouseId |    String  |   Warehouse ID.    |
|    dockId |    String  |   Dock ID.    |
|    courierName |    String  |   Courier name.   |
|    quantity |    Integer  |   Quantity.   |
|    shippingEstimate |    String  |   Shipping estimate. For instance, Three business days will be represented `3bd`.   |
|    shippingEstimateDate |     String  |   Shipping estimate date.  |
|    lockTTL |     String  |   Estimate date of delivery.  |
|    availableDeliveryWindows |     String  |   Available shipping date.  | 
|    startDateUtc |     String  |   Available delivery window start date in UTC.  |
|    endDateUtc |     String  |   Available delivery window end date in UTC.  |
|    deliveryWindow |     Object  |   Scheduled delivery window information, in case it applies to the item.  | 
|    startDateUtc |     String  |   Scheduled delivery window start date in UTC.  |
|    endDateUtc |     String  |   Scheduled delivery window end date in UTC.  |
|    listPrice |     Integer  |   Scheduled delivery window list price.  |
|    price |     Integer  |   Price in cents.  |
|    tax |     Integer  |   Tax in cents.  |
|    pickupStoreInfo |     Object  |   Information on the pickup store.  |
|    isPickupStore |     Boolean  |   Indicates whether it is the pickup store.  |
|    friendlyName |     String  |   Friendly name.  |
|    address |     Object  |   Address information.  |
|    additionalInfo |     String  |   Additional information.  |
|    dockId |     String  |   Corresponding dock ID.  |
|    pickupPointId |     String  |   Pickup point ID.  |
|    pickupDistance |     Integer  |   Pickup point distance.  |
|    polygonName |     String  |   Polygon name.  |
|    transitTime |     String  |   Transit time. For instance, "three business days" is represented `3bd`.  |
|    shipsTo |     Array  |   List of countries that the item may be shipped to.  |
|    itemId |     String  |   Item ID.  |
|    deliveryChannels |     String  |   List of available delivery channels.  |
|    id |     String  |   elivery channel ID.  |
|    selectedAddresses  |    Array  |   Selected addresses information.     |


## storeId

It is a string containing the store ID.

**Example:** 
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"storeId\": \"2\"\n  }",
      "language": "json"
    }
  ]
}
[/block]
| Field      | Type      | Description |
| ---------- | ---------- | ---------- |
|    storeId  |    integer  |   Identification of the store.    |

## storePreferencesData

This object contains data from the store's configuration (stored in VTEX's License Manager). 

**Example:**
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"countryCode\": \"BRA\",\n  \"saveUserData\": true,\n  \"templateOptions\": {\n    \"toggleCorporate\": false\n  },\n  \"timeZone\": \"E. South America Standard Time\",\n  \"currencyCode\": \"BRL\",\n  \"currencyLocale\": 0,\n  \"currencySymbol\": \"R$\",\n  \"currencyFormatInfo\": {\n    \"currencyDecimalDigits\": 2,\n    \"currencyDecimalSeparator\": \",\",\n    \"currencyGroupSeparator\": \".\",\n    \"currencyGroupSize\": 3,\n    \"startsWithCurrencySymbol\": true\n  }\n}",
      "language": "json"
    }
  ]
}
[/block]

## totalizers

This array contains an object for each totalizer for the purchase. Totalizers contain the sum of values for a specific part of the order (e.g. Total item value, Total shipping value).

**Example:**
[block:code]
{
  "codes": [
    {
      "code": "[\n  {\n    \"id\": \"Items\"\n    \"name\": \"Total items\"\n    \"value\": 35620\n  }, {\n    \"id\": \"Shipping\"\n    \"name\": \"Total freight\"\n    \"value\": 399\n  }\n]",
      "language": "json"
    }
  ]
}
[/block]