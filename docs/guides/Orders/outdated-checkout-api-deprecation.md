---
title: "Outdated Checkout API deprecation"
slug: "unofficial-checkout-api-deprecation"
hidden: true
createdAt: "2022-12-08T22:14:43.582Z"
updatedAt: "2023-01-24T19:07:25.000"
---

Both the Outdated Checkout endpoint and the Order Management System (OMS) endpoints in the table below allow you to obtain order fulfillment information, order management data, seller identification and more.

Beginning June 25, 2023, the Outdated Checkout endpoint will be deprecated and all integrations that use this route will have to migrate to OMS endpoints, as indicated in the following table:

| **From Checkout endpoint** | **To OMS endpoints** |
|---|---|
|  Outdated Checkout endpoint GET - `api/checkout/pub/orders` | <ul><li><a href="https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/user/orders">Retrieve user's orders</a><br>GET - <code>https://{accountName}.{environment}.com.br/api/oms/user/orders</code></li><li><a href="https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/user/orders/-orderId-">Retrieve user order details</a><br>GET - <code>https://{accountName}.{environment}.com.br/api/oms/user/orders/{orderId}</code></li></ul>

> For integrations built with GraphQL that use the Outdated Checkout endpoint, instead of using the `orders` query provided by the `vtex.store-graphql` app, now they will have to use the `orders` query provided by the `vtex.orders-graphql` app. For more information about GraphQL APIs, see this [Overview](https://developers.vtex.com/docs/guides/graphql-ide). In the next sections, you will find a [GraphQL query example](#graphql-query-example).

## Why are we doing this

The Outdated Checkout endpoint is an old route that will be discontinued. Using the OMS endpoints ensure that your store is using the latest and most performant VTEX solution. Some of the benefits of migrating to the VTEX OMS endpoints are:

* Faster order retrieve
* Reduction in order integration errors
* Option to paginate orders data

Having a unified service across all VTEX stores also helps us accelerate the pace of new solutions and product releases to improve your business.

## What are the differences

The table below shows the Outdated Checkout endpoint fields that do not exist on OMS endpoints, and most of them will be permanently deprecated. Except for the fields in the table, all of the other Outdated Checkout endpoint fields can be found on VTEX OMS endpoints.

If you wish to see the Outdated Checkout endpoint’s payload, go to [Outdated Checkout endpoint response body](#outdated-checkout-endpoint-response-body).

| **Missing Field** | **Type** | **Description** | **Will be deprecated** |
|:---:|:---:|:---:|:---|
| storeId | string | ID of purchases made in the GoCommerce context. | Yes |
| productRefId | string | Product Ref ID. | Yes |
| modalType | string | Links an unusual type of product to a carrier specialized in delivering it. For more information see How the modal works and Setting up modal for carriers. | Yes |
| manualPriceAppliedBy | string | User ID or appKey used to make the change. This field must not be displayed to the shopper. | Yes |
| productCategoryIds | string | Item's category path composed of category IDs. In OMS endpoints this field corresponds to `productCategories`. | Yes |
| sellerChain | array | Sellers involved in the chain. The list should contain only one seller, unless it is a Multilevel Omnichannel Inventory order. | Yes |
| attachmentOfferings | array of objects | Object with the properties of the content declared in the field `attachments`. | No |
| name (items > attachmentOfferings > name) | string | Name of the attachment. | No |
| required (items > attachmentOfferings > required) | boolean | If the attachment is required or not. | No |
| schema (items > attachmentOfferings > schema) | object | Object with the schema of the content declared in the field `attachmentOfferings`. | No |
| availability | string | Availability to fulfill the order with the item. This field is being removed because it is related to the shopping cart. | Yes |
| manufacturerCode | string | Provided by the manufacturers to identify their product. This field should be completed if the item has a specific manufacturer’s code. | Yes |
| profileCompleteOnLoading | boolean | When set as `true`, the order was made by a recurrent customer, and when set as `false`, it was not. | Yes |
| profileErrorOnLoading | boolean | When set as `true`, this field indicates a profile error on loading, and when set as `false`, no errors were found. If there are errors, check the store's customer profiles in Master Data. This field doesn't have to be displayed to the shopper. | Yes |
| teaser | array | List with promotions and taxes teasers. | No |
| selectedDeliveryChannel | string | Delivery channel selected by the customer, like `delivery` or `pickup-in-point`. This field is being removed and the information it retrieves can be found in the `deliveryChannel`. | Yes |
| kitItemDetails | array of objects | Information about kits, if there are any. | No |
| availableDeliveryWindows | array | Available delivery window information, if it applies to the item.This field is being removed because it is related to the shopping cart. | Yes |
| pickupDistance | number | Distance in kilometers between the pickup point and the customer's address. The distance is measured as a straight line. | No |
| deliveryChannels | array of objects | Contains the delivery channels associated with the trade policy. Structure: `{id: delivery} and/or {id: pickup-in-point}`. | No |
| availableAddresses | array of objects | Information about available adresses.This field is being removed because it is related to the shopping cart. | Yes |
| pickupPoints | array of objects | Detailed information about pickup points in the shopping cart. This field is being removed because it is related to the shopping cart; the pickup point option of the order was already selected. | Yes |
| businessHours | array of objects | Information about the pickup point's business hours. | Yes |
| DayOfWeek | integer | Day of the week of the business hour, with `0`: corresponding to Sunday, `1` to Monday, `2` to Tuesday, and so on. | Yes |
| OpeningTime | string | Starting time of the business hour, with the format `hh:mm:ss`. | Yes |
| ClosingTime | string | Closing time of the business hour, with the format `hh:mm:ss`. | Yes |
| sharedTransaction | boolean | When set as `true`, this field indicates it was a shared transaction, and when set as `false`, it means it was not.This field does not reflect on the shopper experience since it is about the store's internal financial matters. | Yes |
| clientPreferencesData | object | Information about customer's preferences. | No |
| locale (clientPreferencesData > locale) | string | Customer's prefered language while accessing the store. | No |
| optinNewsLetter (clientPreferencesData >optinNewsLetter)  | boolean | When set as `true`, this field indicates the customer opted to receive the newsletters, and when set as `false`, it means they did not accept to receive the newsletters. This field isn't displayed to the shopper since it is about the store's internal matters. | Yes |
| saveUserData | boolean | When this field is set as `true`, it means the customers agree to have their data stored, and when set as `false`, the customer did not allow to store their data. This field isn't displayed to the shopper since it is about the store's internal matters. | Yes |
| hooksData | object | Information about a legacy hook.This field has been deactivated. | Yes |
| major | string | An internal system's code of VTEX's modules communication. | Yes |
| url | string | URL that used to be notified by the legacy look, which has been deactivated. | Yes |

### Outdated Checkout endpoint properties descriptions

| **Field** | **Type** | **Description** |
|:---:|:---:|:---|
| orderId | string | Order ID is a unique code that identifies an order. |
| orderGroup | string | Order's group ID. |
| state | string | Status of the order in the Order flow. |
| isCheckedIn | boolean | The field is set `true` when the order was made via inStore and `false` when it was not. |
| sellerOrderId | string | ID of the seller related to the order. It can be a VTEX seller or an external seller. |
| storeId | string | ID that identifies the store when the order was made using inStore. |
| checkedInPickupPointId | string | If the field `isCheckedIn` is set as `true`, the `checkedInPickupPointId` will retrieve the ID of the physical store where the order was made. |
| value | integer | The order's total amount, written as a sequence of numbers with no punctuation. |
| items | array of object | Information about the order items. |
| uniqueId | string | Unique ID is an alphanumeric sequence that identifies an SKU in a given order. |
| id | integer | Item's SKU ID, which is a unique numerical identifier. |
| productId | string | ID of the Product associated with the item. |
| productRefId | string | Product Ref ID. |
| refId | string | Product referencial code associated with the item. |
| ean | string | EAN of the SKU. |
| name | string | Name of the Product associated with the item. |
| skuName | string | Name of the SKU corresponding to the item. |
| modalType | string | Links an unusual type of product to a carrier specialized in delivering it. For more information see How the modal works and Setting up modal for carriers. |
| parentItemIndex | number | Parent item index. |
| parentAssemblyBinding | string | Parent assembly binding. |
| assemblies | array | Retrieves information about orders' customizations. |
| priceValidUntil | string | Computed price's validation date, due to pricing scheduling. |
| tax | integer | Item's tax. |
| price | integer | Item's price. |
| listPrice | integer | Item's list price. |
| manualPrice | integer | Item's manual price. |
| manualPriceAppliedBy | string | User ID or appKey used to make the change. |
| sellingPrice | integer | Item's selling price. |
| rewardValue | integer | Item's reward value. |
| isGift | boolean | This field is `true` when the item is a gift in order context and `false` when it is not.  |
| additionalInfo | object | Additional information about the item. |
| dimension | object | Item's dimensions in the measure unit configured in the catalog. |
| cubicweight | number | Item's cubic weight. |
| height | number | Item's height. |
| length | number | Item's length. |
| weight | number | Item's weight. |
| width | number | Item's width. |
| brandName | string | Item's brand name. |
| brandId | string | Item's brand ID. |
| offeringInfo | string | Offering information. |
| offeringType | string | Offering type. |
| offeringTypeId | string | Offering type ID. |
| preSaleDate | string | Item's pre sale date. |
| productCategoryIds | string | Item's category path composed of category IDs separated by `/`. For example: `/3/15/`. |
| productCategories | object | Object containing product categories. Structure: "{CategoryID}": "{CategoryName}". Both the key and the value are strings. |
| quantity | integer | Quantity of items. |
| seller | string | Seller ID that identifies the seller the item belongs to. |
| sellerChain | array of strings | Sellers involved in the chain. The list should contain only one seller, unless it is a Multilevel Omnichannel Inventory order. |
| imageUrl | string | Item's SKU Image URL. |
| detailUrl | string | URL slug of the Product associated with the item. |
| components | array | Item's components. |
| bundleItems | array | Information on services sold along with the item's SKU. For example: a gift package. |
| attachments | array of object | Array containing information on attachments. |
| name | string | Attachment's name. |
| content | object | Attachment's custom field for content. |
| attachmentOfferings | array of object | Object with the properties of the content declared in the field `attachments`. |
| name | string | Name of the attachment. |
| required | boolean | If the attachment is required or not. |
| schema | object | Object with the schema of the content declared in the field `attachmentOfferings`. |
| offerings | array | Item's offerings. |
| priceTags | array of object | Array containing objects with item's price modifiers.  |
| availability | string | Availability to fulfill the order with the item. |
| measurementUnit | string | Item's measurement unit. |
| unitMultiplier | integer | Item's unit multiplier. |
| manufacturerCode | string | Provided by the manufacturers to identify their product. This field should be completed if the item has a specific manufacturer’s code. |
| priceDefinitions | object | Item's price information. |
| calculatedSellingPrice | integer | Item's calculated unitary selling price in cents. |
| total | integer | Total value of all item's units in cents. |
| sellingPrices | array of object | Details on item's selling price. |
| value | integer | Total value of items in cents. |
| quantity | integer | Quantity of items. |
| sellers | array of object | Array containing information on all the sellers associated with the order.  |
| id | string | Seller ID that identifies the seller. |
| name | string | Seller's name. |
| logo | string | URL of the seller's logo. |
| totals | array of object | Array of object that includes the following fields, whenever they apply to the order: - Items - Discounts - Shipping - Tax - Change |
| id | string | Code that identifies if the information is about `Items`, `Discounts`, `Shipping`, `Tax` or `Change`.  |
| name | string |  Name of the `Items`, `Discounts`, `Shipping`, `Tax` or `Change`.  |
| value | integer |  Total value of the `Items`, `Discounts`, `Shipping`, `Tax` or `Change`.  |
| clientProfileData | object | Object with information on the client's profile. |
| email | string | Customer's email. |
| firstName | string | Customer's first name. |
| lastName | string | Customer's last name. |
| document | string | Document identification code informed by the customer. |
| documentType | string | Type of the document informed by the customer. |
| phone | string | Customers's phone number. |
| corporateName | string | If the customer is a legal entity, here goes the corporate name. |
| tradeName | string | If the customer is a legal entity, here goes the trade name. |
| corporateDocument | string | If the customer is a legal entity, here goes the corporate document. |
| stateInscription | string | If the custmer is a legal entity, here goes the state inscription. |
| corporatePhone | string | If the customer is a legal entity, here goes the corpany's phone number. |
| isCorporate | boolean | The value is `true` when the customer is a legal entity and `false` when not.  |
| profileCompleteOnLoading | boolean | When set as `true`, the order was made by a recurrent customer, and when set as `false`, it was not. |
| profileErrorOnLoading | boolean | When set as `true`, this field indicates a profile error on loading, and when set as `false`, no errors were found. If there are errors, check the store's customer profiles in Master Data. |
| customerClass | string | Identification of the class the customer belongs to. |
| ratesAndBenefitsData | object | Information on promotions and taxes that apply to the order. |
| rateAndBenefitsIdentifiers | array of object | Information about order's promotions and taxes identifiers. |
| id | string | ID of the rate or benefit. |
| name | string | Name of the rate or benefit. |
| featured | boolean | This field is set `true` when the promotions and taxes are cumulative and `false` when not. |
| description | string | Description of promotions and taxes. |
| matchedParameters | object | Informs the criteria and conditions fulfilled so the promotion became valid. |
| paymentMethodId | string | ID of the payment method. |
| additionalInfo | object | Object containing additional information about promotions and taxes, if it applies. For example { "Free shipping": "249,99"  }. |
| teaser | array of object | List with promotions and taxes teasers. |
| shippingData | object | Object containing shipping data. |
| address | object | Shipping address. |
| addressType | string | Type of address. For example, `Residential` or `Pickup`, among others. |
| receiverName | string | Name of the person who is going to receive the order. |
| addressId | string | Shipping address ID. |
| isDisposable | boolean | This field is set as `true` when after the order placement the user's profile is disposed, and `false` when profile data is saved for future checkouts. |
| postalCode | string | Postal code of the shipping address. |
| city | string | City of the shipping address. |
| state | string | State of the shipping address. |
| country | string | Three letters ISO code of the country of the shipping address (ISO 3166 ALPHA-3). |
| street | string | Street of the shipping address. |
| number | string | Number of the building, house or apartment in the shipping address. |
| neighborhood | string | Neighborhood of the shipping address. |
| complement | string | Complement to the shipping address when it applies. |
| reference | string | Complement to help locate the shipping address, in case of delivery. |
| geoCoordinates | array of numbers | Array with two numbers with geocoordinates, first latitude, then longitude. |
| logisticsInfo | array of object | Array of objects containing logistics information of each item. |
| itemIndex | integer | Index of the item starting from 0. |
| selectedSla | string | Selected shipping option. |
| selectedDeliveryChannel | string | Delivery channel selected by the customer, like `delivery` or `pickup-in-point`. |
| addressId | string | Adress ID. |
| slas | array of object | Information on Service Level Agreement (SLA), corresponding to shipping policies. |
| id | string | ID of the shipping method used in the shipping policy. |
| deliveryChannel | string | If the delivery channel is "delivery" or "pickup-in-point". |
| name | string | Name of the shipping policy. |
| deliveryIds | array of object | Information about delivery IDs.  |
| courierId | string | Carrier's ID. |
| warehouseId | string | ID of the warehouse. |
| dockId | string | ID of the loading dock. |
| courierName | string | Carrier's name. |
| quantity | integer | Quantity of items. |
| kitItemDetails | array of object | Information about kits, if there are any. |
| itemId | string | SKU ID of the kit's item. |
| warehouseId | string | ID of the warehouse related to the kit's item. |
| shippingEstimate | string | Total shipping estimate time in days. For instance, three business days is represented `3bd`. |
| shippingEstimateDate | string | Shipping estimate date. It is defined only after the confirmation of the order.  |
| lockTTL | string | Logistics reservation waiting time. |
| availableDeliveryWindows | array | Available delivery window information, if it applies to the item. |
| deliveryWindow | object | Scheduled delivery window information, if it applies to the item. |
| price | integer | Shipping price for the item in cents. Does not account for the whole order's shipping price. |
| listPrice | integer | SKU's optional price for a specific trade policy. |
| tax | integer | Tax in cents. |
| pickupStoreInfo | object | Detailed information about a pickup point. |
| isPickupStore | boolean | If this field is set `true`, it means the type of shipping is pickup, and if set as `false`, it is not. |
| friendlyName | string | Name of the pickup point displayed at checkout. |
| address | string | Pickup point's address. |
| additionalInfo | string | Additional information about the delivery or the pickup point. |
| dockId | string | ID of the loading dock related to the delivery or the pickup point |
| pickupPointId | string | Pickup point's ID. |
| pickupDistance | number | Distance in kilometers between the pickup point and the customer's address. The distance is measured as a straight line. |
| polygonName | string | Name of the polygon associated with the shipping policy. |
| transitTime | string | Duration in business days of the time the carrier takes in transit to fulfill the order. For example, three business days is represented `3bd`. |
| shipsTo | array of string | Three letters ISO code of the country of the shipping address (ISO 3166 ALPHA-3). |
| itemId | string | Item's SKU ID, which is a unique numerical identifier. |
| deliveryChannels | array of object | Contains the delivery channels associated with the trade policy. Structure: `{id: delivery} and/or {id: pickup-in-point}`.  |
| selectedAddresses | array of object | Information about selected adresses. |
| addressType | string | Selected adress's shipping type, which can be `pickup` or `residential`.  |
| receiverName | string | Name of the person who is going to receive the order in the selected address. |
| addressId | string | Selected address ID. |
| isDisposable | boolean | This field is set `true` when after the order placement the information is disposed, and `false` when data is saved for future checkouts. |
| postalCode | string | Postal code of the selected address. |
| city | string | City of the selected address. |
| state | string | State of the selected address. |
| country | string | Three letters ISO code of the country of the selected address (ISO 3166 ALPHA-3). |
| street | string | Street of the selected address. |
| number | string | Number of the building, house or apartment in the selected address. |
| neighborhood | string | Neighborhood of the selected address. |
| complement | string | Complement to the selected address if it applies. |
| reference | string | Complement to help locate the selected address. |
| geoCoordinates | array of numbers | Array with two numbers with the selected address's geocoordinates, first latitude, then longitude. |
| availableAddresses | array of objects | Information about available adresses. |
| addressType | string | Available address's shipping type, which can be `pickup` or `residential`. |
| receiverName | string | Name of the person who is going to receive the order in the available address. |
| addressId | string | Available address ID. |
| isDisposable | boolean | This field is set `true` when after the order placement the information is disposed, and `false` when data is saved for future checkouts. |
| postalCode | string | Postal code of the available address. |
| city | string | City of the available address. |
| state | string | State of the available address. |
| country | string | Three letters ISO code of the country of the available address (ISO 3166 ALPHA-3). |
| street | string | Street of the available address. |
| neighborhood | string | Neighborhood of the available address. |
| number | string | Number of the building, house or apartment in the available address. |
| complement | string | Complement to the available address, if it applies. |
| reference | string | Complement to help locate the available address. |
| geoCoordinates | array of numbers | Array with two numbers with the available address's geocoordinates, first latitude, then longitude. |
| pickupPoints | array of objects | Detailed information about pickup points, when that is the type of shipping. |
| friendlyName | string | Name of the pickup point displayed at checkout. |
| address | object | Pickup point's adress. |
| addressType | string | Pickup point's adress type. |
| receiverName | string | Name of the person who is going to receive the order. |
| addressId | string | Address ID. |
| isDisposable | boolean | This field is set `true` when after the order placement the information is disposed, and `false` when data is saved for future checkouts. |
| postalCode | string | Postal code of the pickup point. |
| city | string | City of the pickup point. |
| state | string | State of the pickup point. |
| country | string | Three letters ISO code of the country of the pickup point (ISO 3166 ALPHA-3). |
| street | string | Street of the pickup point. |
| neighborhood | string | Neighborhood of the pickup point. |
| number | string | Number of the building of the pickup point, if it applies. |
| complement | string | Complement to the pickup point address, when it applies. |
| reference | string | Complement to help locate the pickup point address. |
| geoCoordinates | array of number | Array with two numbers with geocoordinates, first latitude, then longitude. |
| additionalInfo | string | Additional information about the pickup point. |
| id | string | Pickup point's ID. |
| businessHours | array of objects | Information about the pickup point's business hours. |
| DayOfWeek | integer | Day of the week of the business hour, with `0`: corresponding to Sunday, `1` to Monday, `2` to Tuesday, and so on. |
| OpeningTime | string | Starting time of the business hour, with the format `hh:mm:ss`. |
| ClosingTime | string | Closing time of the business hour, with the format `hh:mm:ss`. |
| paymentData | object | Object with information about the payment. |
| giftCards | array | Array with information about gift cards. |
| redemptionCode | string | Code for the customer to use the Gift Card. |
| provider | string | Payment provider's name. |
| value | integer | Total amount of the Gift Card used by the customer. |
| balance | integer | Current amount of the Gift Card that can still be used by the customer. |
| name | string | Gift Card's name. |
| caption | string | Gift Card's caption. |
| id | string | Gift Card's ID. |
| inUse | boolean | When this field is set as `true`, it means the Gift Card is activated, and when set as `false`, it is deactivated. |
| isSpecialCard | boolean | When this field is set as `true`, the customer does not have to insert a code (`redemptionCode`) to make use of the Gift Card. For example, in a fidelity program in which the client has credits for another purchase. When the field is set as `false`, the customer must insert a code to make use of the Gift Card. |
| groupName | string | Name of the collection the Gift Card belongs to. |
| transactions | array of object | Information about financial transactions. |
| isActive | boolean | When this field is set as `true`, the payment is active, and when it is `false`, the payment is inactive. |
| transactionId | string | ID of the transaction. |
| merchantName | string | Name of the merchant that will receive the payment. |
| payments | array of object | Detailed information about payment. |
| id | string | VTEX payment ID that can be used as unique identifier.  |
| paymentSystem | string | Payment system's ID. |
| paymentSystemName | string | Payment system's name. |
| value | integer | Payment's final amount in cents. |
| installments | integer | Number of payment installments. |
| connectorResponses | object | Information about the connector responses. |
| Tid | string | Provider's unique identifier for the transaction. |
| ReturnCode | integer | Provider's operation/error code to be logged. |
| Message | string | Provider's operation/error message to be logged. |
| authId | string | Connector's authorization ID. |
| referenceValue | number | Payment's reference value in cents. |
| cardHolder | string | Name of the person who owns the card. |
| cardNumber | string | Numeric sequence of the card used in the transaction. |
| firstDigits | string | Fist digits of the card used in the transaction. |
| lastDigits | string | Last digits of the card used in the transaction. |
| cvv2 | string | Card Verification Value (CVV2) is a security code used by payment processors to reduce fraudulent credit and debit card transactions. |
| expireMonth | string | Expire month of the card used in the transaction (2-digits). |
| expireYear | string | Expire year of the card used in the transaction (4-digits). |
| url | string | Payment's URL. |
| koinUrl |  |  |
| tid | string | Provider's unique identifier for the transaction. |
| redemptionCode | string | Code for the customer to use the Gift Card. |
| giftCardId | string | Gift Card's ID. |
| giftCardProvider | string | Gift Card provider's ID. |
| giftCardAsDiscount | boolean | When this field is set as `true`, the Gift Card is a discount over the price, and when set as `false`, it is not a discount. |
| dueDate | string | Payment due date, with the format `yyyy-mm-dd`. |
| accountId | string | Payment's account ID.  |
| parentAccountId | string | This field retrieves the main account if the payment was made in a subaccount. |
| bankIssuedInvoiceIdentificationNumber | string | Numeric sequence that identifies the bank issued invoice. |
| bankIssuedInvoiceIdentificationNumberFormatted | string | Bank issued invoice ID formatted. |
| bankIssuedInvoiceBarCodeNumber | string | Number of the bank issued invoice bar code. |
| bankIssuedInvoiceBarCodeType | string | Type of the bank issued invoice bar code. |
| billingAddress | string | Billing address. |
| sharedTransaction | boolean | When set as `true`, this field indicates it was a shared transaction, and when set as `false`, it means it was not. |
| clientPreferencesData | object | Information about customer's preferences. |
| locale | string | Customer's prefered language while accessing the store. |
| optinNewsLetter | boolean | When set as `true`, this field indicates the customer opted to receive the newsletters, and when set as `false`, it means they did not accept to receive the newsletters. |
| commercialConditionData | object | Information about commercial conditions. |
| giftRegistryData | object | Information about gift list, when it applies. |
| giftRegistryId | string | Gift list item registry ID. |
| giftRegistryType | string | Gift list item's type. |
| giftRegistryTypeName | string | Gift list item's type name. |
| addressId | string | Address's ID for shipping the gift list item.  |
| description | string | Gift list item's description. |
| marketingData | object | Information about promotions and marketing. For example, coupon tracking information and internal or external UTMs. |
| attachmentId | string | Attachment's ID.  |
| coupon | string | Coupon's code information. |
| marketingTags | array | Marketing tags information. This field can be used to register campaign data or informative tags regarding promotions. |
| utmCampaign | string | Value of the `utm_campaign` parameter of the URL that led to the request. |
| utmMedium | string | Value of the `utm_medium` parameter of the URL that led to the request. |
| utmSource | string | Value of the `utm_source` parameter of the URL that led to the request. |
| utmiCampaign         | string | Internal UTM value `utmi_cp`. |
| utmiPart | string | Internal UTM value `utmi_pc`. |
| utmipage | string | Internal UTM value `utmi_p`. |
| storePreferencesData | object | Object with data from the store's configuration - stored in VTEX's License Manager. |
| countryCode | string | Three letters ISO code of the country (ISO 3166 ALPHA-3). |
| saveUserData | boolean | When this field is set as `true`, it means the customers agree to have their data stored, and when set as `false`, the customer did not allow to store their data. |
| timeZone | string | Time zone from where the order was made. |
| currencyCode | string | Currency code in ISO 4217. For example, `BRL`. |
| currencyLocale | integer | Currency Locale Code in LCID in decimal. |
| currencySymbol | string | Currency symbol. |
| currencyFormatInfo | object | Object with currency format details. |
| CurrencyDecimalDigits | integer | Quantity of currency decimal digits. |
| CurrencyDecimalSeparator | string | Defines what currency decimal separator will be applied. |
| CurrencyGroupSeparator | string | Defines what currency group separator will be applied. |
| CurrencyGroupSize | integer | Defines how many characters will be grouped. |
| StartsWithCurrencySymbol | boolean | Defines if all prices will be initiated with the currency symbol. |
| openTextField | object | Optional field with order's additional information. We recommend using regular text only, do not use data formats like `JSON` - not even escaped.  |
| value | string | Additional information about the order.  |
| invoiceData | object | Information used for order invoicing. |
| address | object | Address information. |
| postalCode | string | Postal code of the order's invoice address. |
| city | string | City of the order's invoice address. |
| state | string | State of the order's invoice address. |
| country | string | Country of the order's invoice address. The format is three letters code (ISO 3166 ALPHA-3). |
| street | string | Street of the order's invoice address. |
| number | string | Number of the building of the order's invoice address. |
| neighborhood | string | Neighborhood of the order's invoice address. |
| complement | string | Complement to the order's invoice address. |
| reference | string | Complement to help locate the order's invoice address. |
| settleInvoices | array of string | List of numbers of settled invoices. |
| itemMetadata | object | Metadata information about the order's items. |
| items | array of object | List of items with specific metadata about each one of them. |
| id | string | Item's SKU ID, which is a unique numerical identifier. |
| seller | string | Seller ID that identifies the seller the item belongs to. |
| name | string | Name of the item as displayed to customers in the storefront. |
| skuName | string | Name of the SKU corresponding to the item. |
| productId | string | ID of the Product associated with the item. |
| refId | string | Item's reference ID. |
| ean | string | EAN of the item. |
| imageUrl | string | Item's SKU image URL. |
| detailUrl | string | URL slug of the item. |
| assemblyOptions | array of object | Displays information about assembly options related to the item, if there are any.  |
| id | string | ID of the attachment related to the order.  |
| name | string | Name of the attachment related to the order.  |
| required | boolean | If this field is set as `true`, when the customer purchases the item sending the attachment is required, and when set as `false`, sending the attachment is optional.  |
| inputValues | object | Displays the attachment's content. |
| composition | object | Displays the attachment's composition. |
| taxData | object | Order's tax information. |
| customData | object | Custom information in the order. This field is useful for storing data not included in other fields, for example, a message for a gift or a name to be printed in a shirt. |
| customApps | array | Array containing the customer apps created by the store |
| id | string | Customer app's ID. |
| fields | object | Displays the fields created by the store for each customer app. |
| hooksData | object | Information about the hook.  |
| major | string | An internal system's code of VTEX's modules communication. |
| url | string | URL notified by the Hook to update order's data. |
| changeData | array of object | List with information about changes in the order. |
| reason | string | Text explaining why there was a change in the order. This information may be shown to the customer in the UI or transactional emails. |
| discountValue | integer | This field can be used to apply a discount to the total value of the order. Value in cents. |
| incrementValue | integer | This field can be used to increment the total value of the order. Value in cents. |
| itemsAdded | array of object | List of items added to the order. |
| id | string | SKU ID of the item added to the order. |
| name | string | Name of the item added to the order. |
| quantity | integer | Quantity of items added to the order. |
| price | integer | Total amount in cents of the item added to the order.  |
| unitMultiplier | integer | Unit multiplier of the item added to the order. |
| itemsRemoved | array of object | List of items removed from the order. |
| id | string | SKU ID of the item removed from the order |
| name | string | Name of the item removed from the order. |
| quantity | integer | Quantity of items removed from the order. |
| price | integer | Total amount in cents of the item removed from the order.  |
| unitMultiplier | integer | Unit multiplier of the item removed from the order. |
| receipt | object | Information about the receipt for changed orders. |
| date | string | The time the receipt was created. For example, 2022-06-29T17:42:08.3431198+00:00. |
| orderId | string | ID of the order. |
| receipt | string | Receipt's unique identifier code. |
| subscriptionData | object | Information about subscriptions. |
| subscriptionGroupId | string | ID of the subscription's group. If this field returns `null` and the `executionCount` is `0`, the order is the first one with subscriptions. |
| subscriptions | array of object | List with subscriptions and their details. |
| executionCount | integer | Position of the order in the subscription cycle. The first order will have the value `0`, the second will have the value `1`, and so on. |
| priceAtSubscriptionDate | integer | Price of the order when the customer signed up for subscriptions. Subscriptions created from Admin UI or APIs do not have an original order, so the field returns `0.0`.  This field was valid only for Subscriptions v2 and is deprecated in Subscriptions v3. |
| itemIndex | integer | Each item in the subscriptions' order is identified by an index. The position starts in`0`, followed by `1`, `2`, and so on. |
| plan | object | Information about the subscription's validility and frequency. |
| validility | object | Information about the period during which the subscription will be valid. |
| begin | string | Subscriptions' beginning date with the format `yyyy-mm-ddThh:mm:ss`. |
| end | string | Subscriptions' ending date with the format `yyyy-mm-ddThh:mm:ss`. |
| frequency | object | Information about subscriptions' recurrence. |
| periodicity | string | Defines the subscriptions recurrence period. The possible values are `DAILY`,`WEEKLY`, `MONTHLY` and `YEARLY`. |
| interval | number | Number of the time interval configured between subscription orders, which depends on the periodicity. For a `DAILY` periodicity, the field's value will correspond to days, for `MONTHLY` to months, and so on.  |
| merchantContextData | object | Information about the order's context provided by the merchant. |
| salesAssociateData | object | Information associated to the order.  |
| salesAssociateId | string | Identification code of the vendor related to the order. This field is registered by the merchant, with a maximum of 100 characters. |
| salesChannel | string | Sales channel, or trade policy, related to the order. |
| followUpEmail | string | Email of the store's employee responsible for managing the order. |
| creationDate | string | Order's creation date with the format `yyyy-mm-ddThh:mm:ss.{zone}Z`. |
| lastChange | string | Order's last change date with the format `yyyy-mm-ddThh:mm:ss.{zone}Z`. |
| timeZoneCreationDate | string | Time zone of when the order was created with the format `yyyy-mm-ddThh:mm:ss.{zone}Z`. |
| timeZoneLastChange | string | Time zone of when the order was last changed with the format `yyyy-mm-ddThh:mm:ss.{zone}Z`. |
| isCompleted | boolean | When set as `true`, the order's payment has been settled, and when set as `false`, it has not been settled yet. |
| hostName | string | Account Hostname registered in License Manager |
| merchantName | string | For a VTEX store, the merchant's name will be the same as the account name. An external seller can have a `merchantName`, and in this case the field will not correspond to an account name. |
| userType | string | Role of the user retrieving the order. |
| roundingError | integer | Rounding error total amount, if it applies. For example, in orders with a discount over non-integer multiplier items, the rounding price is performed per item, not after the sum of all items. That can cause a difference in the total discount amount, which is informed in this field.  |
| allowEdition | boolean | When set as `true`, the order can be edited, and when set as `false`, it is no longer possible to edit the order. |
| allowCancellation | boolean | When set as `true`, the order can be canceled, and when set as `false`, it is no longer possible to cancel the order. |
| isUserDataVisible | boolean | When set as `true`, the client's data is visible in the checkout, and when set as `false`, it is not. |
| allowChangeSeller | boolean | When set as `true`, it is possible to use the Change Seller feature in the order, and when set as `false`, it is not possible. |
| orderFormCreationDate | string | Date of when the orderForm was created with the format `yyyy-mm-ddThh:mm:ss.{zone}Z`. |

### Outdated Checkout endpoint response body

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"orderId\": \"1268540501456-01\",\n    \"orderGroup\": \"1268540501456\",\n    \"state\": \"payment-pending\",\n    \"isCheckedIn\": false,\n    \"sellerOrderId\": \"00-1268540501456-01\",\n    \"storeId\": \"store2485\",\n    \"checkedInPickupPointId\": \"storeNameExample_901\",\n    \"value\": 1500,\n    \"items\": [\n        {\n            \"uniqueId\": \"AB1D237A5D92460383B53305AA647BAD\",\n            \"id\": \"14\",\n            \"productId\": \"13\",\n            \"productRefId\": \"\",\n            \"refId\": \"356\",\n            \"ean\": \"dasdsadasdasda\",\n            \"name\": \"Xícara com Imagem Pequena Xicrinha Small\",\n            \"skuName\": \"Xicrinha Small\",\n            \"modalType\": \" \",\n            \"parentItemIndex\": 87,\n            \"parentAssemblyBinding\": \" \",\n            \"assemblies\": [],\n            \"priceValidUntil\": \"2023-10-13T13:48:11Z\",\n            \"tax\": 0,\n            \"price\": 1500,\n            \"listPrice\": 1500,\n            \"manualPrice\": 1400,\n            \"manualPriceAppliedBy\": \" \",\n            \"sellingPrice\": 1000,\n            \"rewardValue\": 0,\n            \"isGift\": false,\n            \"additionalInfo\": {\n                \"dimension\": null,\n                \"brandName\": \"Escola\",\n                \"brandId\": \"2000001\",\n                \"offeringInfo\": null,\n                \"offeringType\": null,\n                \"offeringTypeId\": null\n            },\n            \"preSaleDate\": null,\n            \"productCategoryIds\": \"/2/\",\n            \"productCategories\": {\n                \"2\": \"Uniforme\"\n            },\n            \"quantity\": 1,\n            \"seller\": \"1\",\n            \"sellerChain\": [\n                \"1\"\n            ],\n            \"imageUrl\": \"http://partnerintegrationbra.vteximg.com.br/arquivos/ids/155419-55-55/xicrinha_small.png?v=637885856236700000\",\n            \"detailUrl\": \"/xicara-pequena/p\",\n            \"components\": [],\n            \"bundleItems\": [],\n            \"attachments\": [],\n            \"attachmentOfferings\": [],\n            \"offerings\": [],\n            \"priceTags\": [\n                {\n                    \"name\": \"discount@price-2050d4d9-1116-42d4-8a06-5db9eb677dc8#851f4d9a-bb88-41d2-bca3-65d0f55716b6\",\n                    \"value\": -500,\n                    \"rawValue\": -5.0,\n                    \"isPercentual\": false,\n                    \"identifier\": \"2050d4d9-1116-42d4-8a06-5db9eb677dc8\",\n                    \"owner\": \"partnerintegrationbra\"\n                }\n            ],\n            \"availability\": \"available\",\n            \"measurementUnit\": \"un\",\n            \"unitMultiplier\": 1.0000,\n            \"manufacturerCode\": null,\n            \"priceDefinition\": {\n                \"calculatedSellingPrice\": 1000,\n                \"total\": 1000,\n                \"sellingPrices\": [\n                    {\n                        \"value\": 1000,\n                        \"quantity\": 1\n                    }\n                ]\n            }\n        }\n    ],\n    \"sellers\": [\n        {\n            \"id\": \"1\",\n            \"name\": \"VTEX\",\n            \"logo\": \"\"\n        }\n    ],\n    \"totals\": [\n        {\n            \"id\": \"Items\",\n            \"name\": \"Total dos Itens\",\n            \"value\": 1500\n        },\n        {\n            \"id\": \"Discounts\",\n            \"name\": \"Total dos Descontos\",\n            \"value\": -500\n        },\n        {\n            \"id\": \"Shipping\",\n            \"name\": \"Total do Frete\",\n            \"value\": 500\n        },\n        {\n            \"id\": \"Tax\",\n            \"name\": \"Total da Taxa\",\n            \"value\": 0\n        }\n    ],\n    \"clientProfileData\": {\n        \"email\": \"gabriel.barros@vtex.com.br\",\n        \"firstName\": \"sdfsd\",\n        \"lastName\": \"sdfsdf\",\n        \"document\": \"35234110095\",\n        \"documentType\": \"cpf\",\n        \"phone\": \"+5541998664959\",\n        \"corporateName\": null,\n        \"tradeName\": null,\n        \"corporateDocument\": null,\n        \"stateInscription\": null,\n        \"corporatePhone\": null,\n        \"isCorporate\": false,\n        \"profileCompleteOnLoading\": true,\n        \"profileErrorOnLoading\": false,\n        \"customerClass\": null\n    },\n    \"ratesAndBenefitsData\": {\n        \"rateAndBenefitsIdentifiers\": [\n            {\n                \"id\": \"2050d4d9-1116-42d4-8a06-5db9eb677dc8\",\n                \"name\": \"Promoção Afiliados\",\n                \"featured\": false,\n                \"description\": \"Test teste\",\n                \"matchedParameters\": {\n                    \"paymentMethodId\": \"201\"\n                },\n                \"additionalInfo\": null\n            }\n        ],\n        \"teaser\": []\n    },\n    \"shippingData\": {\n        \"address\": {\n            \"addressType\": \"residential\",\n            \"receiverName\": \"sdfsd sdfsdf\",\n            \"addressId\": \"4983586086510\",\n            \"isDisposable\": false,\n            \"postalCode\": \"80050-350\",\n            \"city\": \"Curitiba\",\n            \"state\": \"PR\",\n            \"country\": \"BRA\",\n            \"street\": \"Avenida São José\",\n            \"number\": \"656453\",\n            \"neighborhood\": \"Cristo Rei\",\n            \"complement\": null,\n            \"reference\": null,\n            \"geoCoordinates\": [\n                -49.243179321289063,\n                -25.435266494750977\n            ]\n        },\n        \"logisticsInfo\": [\n            {\n                \"itemIndex\": 0,\n                \"selectedSla\": \"jatinho\",\n                \"selectedDeliveryChannel\": \"delivery\",\n                \"addressId\": \"4983586086510\",\n                \"slas\": [\n                    {\n                        \"id\": \"jatinho\",\n                        \"deliveryChannel\": \"delivery\",\n                        \"name\": \"jatinho\",\n                        \"deliveryIds\": [\n                            {\n                                \"courierId\": \"jatinho\",\n                                \"warehouseId\": \"1_1\",\n                                \"dockId\": \"1\",\n                                \"courierName\": \"Jatinho\",\n                                \"quantity\": 1,\n                                \"kitItemDetails\": [\n                                    {\n                                        \"itemId\": \"1065\"\n                                    },\n                                    {\n                                        \"warehouseId\": \"517\"\n                                    }\n                                ]\n                            }\n                        ],\n                        \"shippingEstimate\": \"3d\",\n                        \"shippingEstimateDate\": null,\n                        \"lockTTL\": \"26d\",\n                        \"availableDeliveryWindows\": [],\n                        \"deliveryWindow\": null,\n                        \"price\": 500,\n                        \"listPrice\": 500,\n                        \"tax\": 0,\n                        \"pickupStoreInfo\": {\n                            \"isPickupStore\": false,\n                            \"friendlyName\": null,\n                            \"address\": null,\n                            \"additionalInfo\": null,\n                            \"dockId\": null\n                        },\n                        \"pickupPointId\": null,\n                        \"pickupDistance\": 0.0,\n                        \"polygonName\": \"\",\n                        \"transitTime\": \"3d\"\n                    },\n                    {\n                        \"id\": \"Split\",\n                        \"deliveryChannel\": \"delivery\",\n                        \"name\": \"Split\",\n                        \"deliveryIds\": [\n                            {\n                                \"courierId\": \"2\",\n                                \"warehouseId\": \"2_2_2\",\n                                \"dockId\": \"2_2\",\n                                \"courierName\": \"Split\",\n                                \"quantity\": 1,\n                                \"kitItemDetails\": []\n                            }\n                        ],\n                        \"shippingEstimate\": \"3d\",\n                        \"shippingEstimateDate\": null,\n                        \"lockTTL\": \"26d\",\n                        \"availableDeliveryWindows\": [\n                            {\n                                \"startDateUtc\": \"2022-10-17T08:00:00+00:00\",\n                                \"endDateUtc\": \"2022-10-17T12:00:59+00:00\",\n                                \"price\": 0,\n                                \"lisPrice\": 0,\n                                \"tax\": 0\n                            }\n                        ],\n                        \"deliveryWindow\": null,\n                        \"price\": 500,\n                        \"listPrice\": 500,\n                        \"tax\": 0,\n                        \"pickupStoreInfo\": {\n                            \"isPickupStore\": false,\n                            \"friendlyName\": null,\n                            \"address\": null,\n                            \"additionalInfo\": null,\n                            \"dockId\": null\n                        },\n                        \"pickupPointId\": null,\n                        \"pickupDistance\": 0.0,\n                        \"polygonName\": \"\",\n                        \"transitTime\": \"3d\"\n                    },\n                    {\n                        \"id\": \"Normal\",\n                        \"deliveryChannel\": \"delivery\",\n                        \"name\": \"Normal\",\n                        \"deliveryIds\": [\n                            {\n                                \"courierId\": \"1\",\n                                \"warehouseId\": \"1_1\",\n                                \"dockId\": \"1\",\n                                \"courierName\": \"Transportadora\",\n                                \"quantity\": 1,\n                                \"kitItemDetails\": []\n                            }\n                        ],\n                        \"shippingEstimate\": \"3d\",\n                        \"shippingEstimateDate\": null,\n                        \"lockTTL\": \"26d\",\n                        \"availableDeliveryWindows\": [\n                            {\n                                \"startDateUtc\": \"2022-10-17T08:00:00+00:00\",\n                                \"endDateUtc\": \"2022-10-17T12:00:59+00:00\",\n                                \"price\": 0,\n                                \"lisPrice\": 0,\n                                \"tax\": 0\n                            },\n                            {\n                                \"startDateUtc\": \"2022-10-17T12:00:00+00:00\",\n                                \"endDateUtc\": \"2022-10-17T16:00:59+00:00\",\n                                \"price\": 0,\n                                \"lisPrice\": 0,\n                                \"tax\": 0\n                            },\n                            {\n                                \"startDateUtc\": \"2022-10-18T08:00:00+00:00\",\n                                \"endDateUtc\": \"2022-10-18T12:00:59+00:00\",\n                                \"price\": 0,\n                                \"lisPrice\": 0,\n                                \"tax\": 0\n                            },\n                            {\n                                \"startDateUtc\": \"2022-10-18T12:00:00+00:00\",\n                                \"endDateUtc\": \"2022-10-18T16:00:59+00:00\",\n                                \"price\": 0,\n                                \"lisPrice\": 0,\n                                \"tax\": 0\n                            },\n                            {\n                                \"startDateUtc\": \"2022-10-19T08:00:00+00:00\",\n                                \"endDateUtc\": \"2022-10-19T12:00:59+00:00\",\n                                \"price\": 0,\n                                \"lisPrice\": 0,\n                                \"tax\": 0\n                            },\n                            {\n                                \"startDateUtc\": \"2022-10-19T12:00:00+00:00\",\n                                \"endDateUtc\": \"2022-10-19T16:00:59+00:00\",\n                                \"price\": 0,\n                                \"lisPrice\": 0,\n                                \"tax\": 0\n                            },\n                            {\n                                \"startDateUtc\": \"2022-10-20T08:00:00+00:00\",\n                                \"endDateUtc\": \"2022-10-20T12:00:59+00:00\",\n                                \"price\": 0,\n                                \"lisPrice\": 0,\n                                \"tax\": 0\n                            },\n                            {\n                                \"startDateUtc\": \"2022-10-20T12:00:00+00:00\",\n                                \"endDateUtc\": \"2022-10-20T16:00:59+00:00\",\n                                \"price\": 0,\n                                \"lisPrice\": 0,\n                                \"tax\": 0\n                            },\n                            {\n                                \"startDateUtc\": \"2022-10-21T08:00:00+00:00\",\n                                \"endDateUtc\": \"2022-10-21T12:00:59+00:00\",\n                                \"price\": 0,\n                                \"lisPrice\": 0,\n                                \"tax\": 0\n                            },\n                            {\n                                \"startDateUtc\": \"2022-10-21T12:00:00+00:00\",\n                                \"endDateUtc\": \"2022-10-21T16:00:59+00:00\",\n                                \"price\": 0,\n                                \"lisPrice\": 0,\n                                \"tax\": 0\n                            }\n                        ],\n                        \"deliveryWindow\": null,\n                        \"price\": 500,\n                        \"listPrice\": 500,\n                        \"tax\": 0,\n                        \"pickupStoreInfo\": {\n                            \"isPickupStore\": false,\n                            \"friendlyName\": null,\n                            \"address\": null,\n                            \"additionalInfo\": null,\n                            \"dockId\": null\n                        },\n                        \"pickupPointId\": null,\n                        \"pickupDistance\": 0.0,\n                        \"polygonName\": \"\",\n                        \"transitTime\": \"3d\"\n                    }\n                ],\n                \"shipsTo\": [\n                    \"BRA\"\n                ],\n                \"itemId\": \"14\",\n                \"deliveryChannels\": [\n                    {\n                        \"id\": \"delivery\"\n                    }\n                ]\n            }\n        ],\n        \"selectedAddresses\": [\n            {\n                \"addressType\": \"residential\",\n                \"receiverName\": \"sdfsd sdfsdf\",\n                \"addressId\": \"4983586086510\",\n                \"isDisposable\": false,\n                \"postalCode\": \"80050-350\",\n                \"city\": \"Curitiba\",\n                \"state\": \"PR\",\n                \"country\": \"BRA\",\n                \"street\": \"Avenida São José\",\n                \"number\": \"656453\",\n                \"neighborhood\": \"Cristo Rei\",\n                \"complement\": null,\n                \"reference\": null,\n                \"geoCoordinates\": [\n                    -49.243179321289063,\n                    -25.435266494750977\n                ]\n            }\n        ],\n        \"availableAddresses\": [\n            {\n                \"addressType\": \"residential\",\n                \"receiverName\": \"sdfsd sdfsdf\",\n                \"addressId\": \"4983586086510\",\n                \"isDisposable\": false,\n                \"postalCode\": \"80050-350\",\n                \"city\": \"Curitiba\",\n                \"state\": \"PR\",\n                \"country\": \"BRA\",\n                \"street\": \"Avenida São José\",\n                \"number\": \"656453\",\n                \"neighborhood\": \"Cristo Rei\",\n                \"complement\": null,\n                \"reference\": null,\n                \"geoCoordinates\": [\n                    -49.243179321289063,\n                    -25.435266494750977\n                ]\n            }\n        ],\n        \"pickupPoints\": []\n    },\n    \"paymentData\": {\n        \"giftCards\": [\n            {\n                \"redemptionCode\": \"HYUO-TEZZ-QFFT-HTFR\",\n                \"provider\": \"TesteFer\",\n                \"value\": 0,\n                \"balance\": 1000,\n                \"name\": null,\n                \"caption\": \"gift card by id\",\n                \"id\": \"123\",\n                \"inUse\": false,\n                \"isSpecialCard\": true,\n                \"groupName\": \"giftCardPaymentGroup\"\n            }\n        ],\n        \"transactions\": [\n            {\n                \"isActive\": true,\n                \"transactionId\": \"E7FE5D0AC86F49FCAEAFE74BD663E1E6\",\n                \"merchantName\": \"PARTNERINTEGRATIONBRA\",\n                \"payments\": [\n                    {\n                        \"id\": \"D73F65660C5C4CF38D2B241991C25314\",\n                        \"paymentSystem\": \"201\",\n                        \"paymentSystemName\": \"Promissoria\",\n                        \"value\": 1500,\n                        \"installments\": 1,\n                        \"connectorResponses\": {\n                            \"Tid\": \"\",\n                            \"ReturnCode\": 34,\n                            \"Message\": \"\",\n                            \"authId\": \"\"\n                        },\n                        \"referenceValue\": 1500,\n                        \"cardHolder\": null,\n                        \"cardNumber\": null,\n                        \"firstDigits\": null,\n                        \"lastDigits\": null,\n                        \"cvv2\": null,\n                        \"expireMonth\": null,\n                        \"expireYear\": null,\n                        \"url\": \"https://paymentMethod.com.br/apiboleto/nameMethod?token=AEDCBCtR3RCTH\",\n                        \"koinUrl\": null,\n                        \"tid\": \"151902\",\n                        \"redemptionCode\": \"HYUO-TEZZ-QFFT-HTFR\",\n                        \"giftCardId\": null,\n                        \"giftCardProvider\": null,\n                        \"giftCardAsDiscount\": null,\n                        \"group\": \"promissory\",\n                        \"dueDate\": null,\n                        \"accountId\": \"7EA64D20BEC47F55AG7F5BC12D4BF0D5\",\n                        \"parentAccountId\": \"f861a86274af4c678c936k93172fdeed\",\n                        \"bankIssuedInvoiceIdentificationNumber\": \"23797770100000019003099260100022107500729050\",\n                        \"bankIssuedInvoiceIdentificationNumberFormatted\": null,\n                        \"bankIssuedInvoiceBarCodeNumber\": null,\n                        \"bankIssuedInvoiceBarCodeType\": \"i25\",\n                        \"billingAddress\": null\n                    }\n                ],\n                \"sharedTransaction\": false\n            }\n        ]\n    },\n    \"clientPreferencesData\": {\n        \"locale\": \"pt-BR\",\n        \"optinNewsLetter\": false\n    },\n    \"commercialConditionData\": null,\n    \"giftRegistryData\": {\n        \"giftRegistryId\": \"154\",  \n        \"giftRegistryType\": \"9\",\n        \"giftRegistryTypeName\": \"Wedding list\",\n        \"addressId\": \"4352357942349\",\n        \"description\": \"Alanna & Hugo\"\n    },\n    \"marketingData\": {\n        \"attachmentId\": \"marketingData\",\n        \"coupon\": null,\n        \"marketingTags\": [],\n        \"utmCampaign\": \"christmas\",\n        \"utmMedium\": null,\n        \"utmSource\": \"fb\",\n        \"utmiCampaign\": \"\",\n        \"utmiPart\": \"\",\n        \"utmipage\": \"\"  \n      },\n    \"storePreferencesData\": {\n        \"countryCode\": \"BRA\",\n        \"saveUserData\": false,\n        \"timeZone\": \"E. South America Standard Time\",\n        \"currencyCode\": \"BRL\",\n        \"currencyLocale\": 1046,\n        \"currencySymbol\": \"R$\",\n        \"currencyFormatInfo\": {\n            \"currencyDecimalDigits\": 2,\n            \"currencyDecimalSeparator\": \",\",\n            \"currencyGroupSeparator\": \".\",\n            \"currencyGroupSize\": 3,\n            \"startsWithCurrencySymbol\": true\n        }\n    },\n    \"openTextField\": {\n        \"value\": \"{\\\"Phones\\\":[\\\"55555555\\\"]}\"\n    },\n    \"invoiceData\": {\n        \"address\": {\n        \"postalCode\": \"******000\",\n        \"city\": \"Rio ** *******\",\n        \"state\": \"RJ\",\n        \"country\": \"BRA\",\n        \"street\": \"Rua *** *****nte\",\n        \"number\": \"***\",\n        \"neighborhood\": \"Bot*****\",\n        \"complement\": \"*** ** *\",\n        \"reference\": null\n         },\n         \"settleInvoices\":[\n            \"24382\",\n            \"41252\"\n         ]  \n     },\n    \"itemMetadata\": {\n        \"items\": [\n            {\n                \"id\": \"14\",\n                \"seller\": \"1\",\n                \"name\": \"Xícara com Imagem Pequena Xicrinha Small\",\n                \"skuName\": \"Xicrinha Small\",\n                \"productId\": \"13\",\n                \"refId\": null,\n                \"ean\": \"dasdsadasdasda\",\n                \"imageUrl\": \"http://partnerintegrationbra.vteximg.com.br/arquivos/ids/155419-55-55/xicrinha_small.png?v=637885856236700000\",\n                \"detailUrl\": \"/xicara-pequena/p\",\n                \"assemblyOptions\": [\n                    {\n                    \"id\": \"\",\n                    \"name\": \"\",\n                    \"required\": false,\n                    \"inputValues\": {},\n                    \"composition\": {\n                        \"minQuantity\": \"\",\n                        \"maxQuantity\": \"\"\n                        }\n                    }\n                ]\n            }\n        ]\n    },\n    \"taxData\": null,\n    \"customData\":  {\n        \"customApps\": [\n            {\n                \"id\": \"profile\",\n                \"fields\": {\n                    \"age\": \"33\",\n                    \"gender\": \"M\"\n                }\n            }\n        ]\n    },\n    \"hooksData\": {\n        \"major\": \"1\",\n        \"url\": \"\"\n    },\n    \"changeData\": [\n        {\n            \"reason\": \"Aumento peso da Manga em 100grs\",\n            \"discountValue\": 0,\n            \"incrementValue\": 75,\n            \"itemsAdded\": [\n                {\n                    \"id\": \"5042\",\n                    \"name\": \"Manga Tommy 500g\",\n                    \"quantity\": 1,\n                    \"price\": 75,\n                    \"unitMultiplier\": 0.100\n                }\n            ],\n            \"itemsRemoved\": [\n                {\n                    \"id\": \"5030\",\n                    \"name\": \"Morango 300g\",\n                    \"quantity\": 1,\n                    \"price\": 75,\n                    \"unitMultiplier\": 0.100\n                }\n            ],\n            \"receipt\": {\n                \"date\": \"2022-06-29T17:42:08.3431198+00:00\",\n                \"orderId\": \"1243130560385-01\",\n                \"receipt\": \"cce77f10-59f0-4e57-89e8-78ed755505ff\"\n            }\n        }\n    ],\n    \"subscriptionData\": {\n        \"subscriptionGroupId\": \"32586VDS876BFD\",\n        \"subscriptions\": \n        [\n                {\n                        \"executionCount\": 3,\n                        \"priceAtSubscriptionDate\": 84444360.0,\n                        \"itemIndex\": 0,\n                        \"plan\": {\n                                \"validity\": {\n                                        \"begin\": \"2021-08-29T00:00:00\",\n                                        \"end\": \"2024-08-29T00:00:00\"\n                                },\n                                \"frequency\": {\n                                        \"periodicity\": \"DAILY\",\n                                        \"interval\": 15\n                                },\n                                \"type\": \"RECURRING_PAYMENT\"\n                        }\n                }\n        ]\n    },\n    \"merchantContextData\": {\n        \"salesAssociateData\": {\n          \"salesAssociateId\": \"Id72945\"\n        }\n    }        ,\n    \"salesChannel\": \"1\",\n    \"followUpEmail\": \"6eac6fa6521d4cc88f7e03585f1ae69c@ct.vtex.com.br\",\n    \"creationDate\": \"2022-10-13T13:48:36.1056593Z\",\n    \"lastChange\": \"2022-10-13T13:48:42.1418456Z\",\n    \"timeZoneCreationDate\": \"2022-10-13T10:48:36.1056593\",\n    \"timeZoneLastChange\": \"2022-10-13T10:48:42.1418456\",\n    \"isCompleted\": true,\n    \"hostName\": \"partnerintegrationbra\",\n    \"merchantName\": \"merchant123\",\n    \"userType\": \"callCenterOperator\",\n    \"roundingError\": 0,\n    \"allowEdition\": false,\n    \"allowCancellation\": true,\n    \"isUserDataVisible\": true,\n    \"allowChangeSeller\": true,\n    \"orderFormCreationDate\": \"2022-10-13T12:56:47.4031427Z\"\n}",
      "language": "json"
    }
  ]
}
[/block]

### GraphQL query example

```
query orders($options: OrdersOptionsInput!) {
  orders(options: $options) @context(provider: "vtex.orders-graphql") {
    list {
      orderId
      clientName
      clientEmail
      status
      origin
      creationDate
      totalItems
      totalValue
      currencyCode
    }
    total
    currencies {
      currencyCode
      quantity
      value
    }
  }
}
```
