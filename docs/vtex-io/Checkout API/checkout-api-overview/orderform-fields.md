---
title: "orderForm"
slug: "orderform-fields"
hidden: false
createdAt: "2020-09-02T13:59:41.676Z"
updatedAt: "2020-11-11T22:16:29.648Z"
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
      "code": "{\n  \"allowManualPrice\": boolean,\n  \"canEditData\": boolean,\n  \"clientPreferencesData\": {},\n  \"clientProfileData\": {},\n  \"commercialConditionData\": {},\n  \"customData\": {},\n  \"giftRegistryData\": {},\n  \"hooksData\": {},\n  \"ignoreProfileData\": boolean,\n  \"isCheckedIn\": boolean,\n  \"itemMetadata\": {},\n  \"items\": {},\n  \"itemsOrdination\": {},\n  \"loggedIn\": boolean,\n  \"marketingData\": {},\n  \"messages\": [],\n  \"openTextField\": {},\n  \"orderFormId\": \"426effeba9210\",\n  \"paymentData\": {},\n  \"products\": {},\n  \"ratesAndBenefitsData\": {},\n  \"salesChannel\": \"1\",\n  \"selectableGifts\": {},\n  \"sellers\": {},\n  \"shippingData\": {},\n  \"storeId\": {},\n  \"storePreferencesData\": {},\n  \"totalizers\": {},\n  \"userProfileId\": {},\n  \"userType\": {},\n  \"value\": number\n}",
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
- [invoiceData](#invoicedata)
- [itemsOrdination](#itemsordination)
- [marketingData](#marketingdata)
- [messages](#messages)
- [openTextField](#opentextfield)
- [paymentData](#paymentdata)
- [products](#products)
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
| locale       | string       | Client's locale. Examples: "pt-BR" and "en-US". The method `sendLocale()`, from vtex.js, changes the value of this field.       |
| optinNewsLetter       | boolean       | `true` if the client opted to receive newsletters from the store.       |


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
|      email      |    string    |  Customer's email      |
|   firstName         |     string       |  Customer's first name     |
|    lastName        |   string         |   Customer's last name      |
|   document         |   string         |  Document number informed by the customer          |
|   documentType         |   string         |  Type of the document informed by the customer          |
|   phone         |     string       |   Customer's phone number    |
|    corporateName        |  string          |     If it's a legal entity, here goes the company name.       |
|  tradeName          |  string          |     If legal entity, here goes the trade name.       |
|  corporateDocument          |      string      |   If legal entity, here goes the corporate document.         |
|   stateInscription         |    string        |   If legal entity, here goes the state inscription.         |
|   corporatePhone         |    string        |   If legal entity, here goes the company phone.        |
|   isCorporate         |     boolean       |  It has the value `true` if it's a legal entity.         |


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
|    customApps |    array  |  Array que contém os apps criados pela loja      |
|    fields |    object  |  Objeto que contém os campos criados pela loja para cada app      |
|    id   |    string   |   App ID      |
|    major   |        |         |



## giftRegistryData
[block:callout]
{
  "type": "warning",
  "title": "Work in progress",
  "body": "This guide is currently being written and published as content becomes available."
}
[/block]
## hooksData
[block:callout]
{
  "type": "warning",
  "title": "Work in progress",
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
      "code": "[\n  {\n    \"id\": \"3106957\",\n    \"productId\": \"2214\",\n    \"name\": \"Mochila para material de natação Swimm II\",\n    \"skuName\": \"Mochila para material de natação Swimm II - vermelha\",\n    \"tax\": 0,\n    \"price\": 10490,\n    \"listPrice\": 10490,\n    \"manualPrice\": null,\n    \"priceValidUntil\": \"2019-03-06T12:53:40Z\",\n    \"modalType\": null,\n    \"sellingPrice\": 10490,\n    \"isGift\": false,\n    \"attachments\": [],\n    \"attachmentOfferings\": [],\n    \"additionalInfo\": {\n      \"brandName\": \"Royal Canin Cães\",\n      \"brandId\": \"37\",\n      \"offeringInfo\": null\n    },\n    \"preSaleDate\": null,\n    \"productCategories\": {\n      \"343\": \"Natação\",\n      \"515\": \"Mochilas\"\n    },\n    \"productCategoryIds\": \"/343/515/\",\n    \"defaultPicker\": null,\n    \"handlerSequence\": 0,\n    \"handling\": false,\n    \"quantity\": 2,\n    \"refId\": \"193\",\n    \"rewardValue\": 0,\n    \"seller\": \"1\",\n    \"sellerChain\": [\n      \"0\": \"1\"\n    ]\n    \"itemAttachment\": {\n      \"content\": {},\n      \"name\": null\n    },\n    \"imageUrl\": \"/arquivos/ids/188329-71-71/racao-club-performance-junior.jpg\",\n    \"detailUrl\": \"/racao-royal-canin-club-performance-junior/p\",\n    \"components\": [],\n    \"ean\": null,\n    \"bundleItems\": [],\n    \"offerings\": [{\n      \"id\": \"1033\",\n      \"name\": \"A Oferta Magnifica\",\n      \"price\": 100,\n      \"type\": \"idk\"\n    }],\n    \"priceTags\": [],\n    \"availability\": \"available\",\n    \"measurementUnit\": \"un\",\n    \"uniqueId\": \"58FFD07FEE47407EAD545F9A9A31E4A8\",\n    \"unitMultiplier\": 1\n  }\n]",
      "language": "json"
    }
  ]
}
[/block]
## itemsOrdination
[block:callout]
{
  "type": "warning",
  "body": "This guide is currently being written and published as content becomes available.",
  "title": "Work in progress"
}
[/block]
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
|    attachmentId  |    string |        |
|    coupon |    string |        |
|    marketingTags |    string |        |
|    utmCampaign  |    string |  Valor do parâmetro `utm_campaign` da URL que levou ao pedido      |
|    utmMedium  |    string |  Valor do parâmetro `utm_medium` da URL que levou ao pedido      |
|    utmSource  |    string |  Valor do parâmetro `utm_source` da URL que levou ao pedido      |
|    utmiCampaign  |    string |  Valor da UTM interna `utmi_cp`     |
|    utmiPart  |    string |  Valor da UTM interna `utmi_pc`      |
|    utmipage  |    string |  Vvalor da UTM interna `utmi_p`      |


## messages

This array contains an object for each message generated by our servers while processing the request. 

**Example:**
[block:code]
{
  "codes": [
    {
      "code": "[\n  {\n    \"code\": null,\n    \"status\": \"error\",\n    \"text\": \"O vale compra de código AAAA-BBBB-CCCC-DDDD não foi encontrado no sistema\"\n  }\n]",
      "language": "json"
    }
  ]
}
[/block]

## openTextField
[block:callout]
{
  "type": "warning",
  "title": "Work in progress",
  "body": "This guide is currently being written and published as content becomes available."
}
[/block]
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
|    giftCards  |    array  |        |
|    giftCardMessages |    array  |        |
|    availableAccounts |    array  |        |
|    availableTokens  |    array  |        |
|    installmentOptions  |    array  |        |
|    paymentSystems |    array  |        |
|    payments  |    array  |        |
[block:callout]
{
  "type": "warning",
  "title": "Work in progress",
  "body": "This guide is currently being written and published as content becomes available."
}
[/block]
## products
[block:callout]
{
  "type": "warning",
  "title": "Work in progress",
  "body": "This guide is currently being written and published as content becomes available."
}
[/block]
## ratesAndBenefitsData
[block:callout]
{
  "type": "warning",
  "title": "Work in progress",
  "body": "This guide is currently being written and published as content becomes available."
}
[/block]
## selectableGifts
[block:callout]
{
  "type": "warning",
  "title": "Work in progress",
  "body": "This guide is currently being written and published as content becomes available."
}
[/block]
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
|    id  |    string  |   ID of the seller     |
|    name |    string  |   Name of the seller     |
|    logo  |    string  |  URL pointing to where the image is hosted     |


## shippingData

This object contains shipping information for the order.

**Example:**
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"attachmentId\": \"shippingData\",\n  \"address\": {\n    \"addressType\": \"residential\",\n    \"receiverName\": \"Gui***rme\",\n    \"addressId\": \"-1368194386810\",\n    \"postalCode\": \"******000\",\n    \"city\": \"Rio ** *******\",\n    \"state\": \"RJ\",\n    \"country\": \"BRA\",\n    \"street\": \"Rua *** *****nte\",\n    \"number\": \"***\",\n    \"neighborhood\": \"Bot*****\",\n    \"complement\": \"*** ** *\",\n    \"reference\": null\n  },\n  \"availableAddresses\": [\n    {\n      \"addressType\": \"residential\",\n      \"receiverName\": \"Gui***rme\",\n      \"addressId\": \"-1368194386810\",\n      \"postalCode\": \"******000\",\n      \"city\": \"Rio ** *******\",\n      \"state\": \"RJ\",\n      \"country\": \"BRA\",\n      \"street\": \"Rua *** *****nte\",\n      \"number\": \"***\",\n      \"neighborhood\": \"Bot*****\",\n      \"complement\": \"*** ** *\",\n      \"reference\": null\n    }\n  ],\n  \"logisticsInfo\": [\n    {\n      \"itemIndex\": 0,\n      \"selectedSla\": \".Transportadora\",\n      \"slas\": [\n        {\n          \"id\": \".Transportadora\",\n          \"name\": \".Transportadora\",\n          \"deliveryIds\": [\n            {\n              \"courierId\": \"67\",\n              \"warehouseId\": \"1_1\",\n              \"dockId\": \"1_1_1\",\n              \"courierName\": \"Transportadora\",\n              \"quantity\": 1\n            }\n          ],\n          \"shippingEstimate\": \"3d\",\n          \"shippingEstimateDate\": null,\n          \"lockTTL\": null,\n          \"availableDeliveryWindows\": [],\n          \"deliveryWindow\": null,\n          \"price\": 956,\n          \"tax\": 0\n        }, {\n          \"id\": \"Agendada\",\n          \"name\": \"Agendada\",\n          \"deliveryIds\": [\n            {\n              \"courierId\": \"FA02F72F-FEBD-41A0-AF70-83A77E8C77A0\",\n              \"warehouseId\": \"1_1\",\n              \"dockId\": \"1_1_1\",\n              \"courierName\": \"Entrega agendada\",\n              \"quantity\": 1\n            }\n          ],\n          \"shippingEstimate\": \"90d\",\n          \"shippingEstimateDate\": null,\n          \"lockTTL\": null,\n          \"availableDeliveryWindows\": [\n            {\n              \"startDateUtc\": \"2014-04-21T09:00:00+00:00\",\n              \"endDateUtc\": \"2014-04-21T12:00:00+00:00\",\n              \"price\": 1000,\n              \"tax\": 0\n            }, {\n              \"startDateUtc\": \"2014-04-21T13:00:00+00:00\",\n              \"endDateUtc\": \"2014-04-21T17:00:00+00:00\",\n              \"price\": 1000,\n              \"tax\": 0\n            }\n          ],\n          \"deliveryWindow\": null,\n          \"price\": 1220,\n          \"tax\": 0\n        }\n      ]\n    }\n  ],\n  \"selectedAddresses\": []\n}",
      "language": "json"
    }
  ]
}
[/block]
| Field      | Type      | Description |
| ---------- | ---------- | ---------- |
|    attachmentId  |    string  |       |
|    address  |    object  |       |
|    availableAddresses  |    array  |       |
|    logisticsInfo  |    array  |       |
|    selectedAddresses  |    array  |       |


## storeId
[block:callout]
{
  "type": "warning",
  "body": "This guide is currently being written and published as content becomes available.",
  "title": "Work in progress"
}
[/block]
## storePreferencesData

This object contains data from the store's configuration (stored in VTEX's License Manager). 

**Example:**
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"countryCode\": \"BRA\",\n  \"checkToSavePersonDataByDefault\": true,\n  \"templateOptions\": {\n    \"toggleCorporate\": false\n  },\n  \"timeZone\": \"E. South America Standard Time\",\n  \"currencyCode\": \"BRL\",\n  \"currencyLocale\": 0,\n  \"currencySymbol\": \"R$\",\n  \"currencyFormatInfo\": {\n    \"currencyDecimalDigits\": 2,\n    \"currencyDecimalSeparator\": \",\",\n    \"currencyGroupSeparator\": \".\",\n    \"currencyGroupSize\": 3,\n    \"startsWithCurrencySymbol\": true\n  }\n}",
      "language": "json"
    }
  ]
}
[/block]

## totalizers

This array contains an object for each totalizer for the purchase. Totalizers contain the sum of values for a specific part of the order (e.g. Total item value, Total shipping value)

**Example:**
[block:code]
{
  "codes": [
    {
      "code": "[\n  {\n    \"id\": \"Items\"\n    \"name\": \"Total dos Itens\"\n    \"value\": 35620\n  }, {\n    \"id\": \"Shipping\"\n    \"name\": \"Total do Frete\"\n    \"value\": 399\n  }\n]",
      "language": "json"
    }
  ]
}
[/block]