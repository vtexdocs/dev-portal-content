---
title: "Fulfillment simulation"
slug: "fulfillment-simulation"
excerpt: "This endpoint may be called upon by VTEX for fulfillment simulation in the external seller different contexts. See examples below.\n\nWhen a [Notification request](https://developers.vtex.com/vtex-rest-api/reference/notification) returns a response with status `200 OK`, it means that the SKU already exists in the marketplace. Whenever this happens, the marketplace will call the seller to get two updated information about the SKU: Price and Inventory.\n\nThe seller needs to have an endpoint implemented in order to receive this call and send a response containing the requested information to the marketplace. We call it the Fulfillment Simulation endpoint.\n\nIf the seller wishes to include other parameters in this call (like account name, or [sales channel](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV) ID), this should be done within their {fulfillmentEndpoint}. This path is then inserted in the marketplace's VTEX admin when [configuring a seller](https://help.vtex.com/en/tutorial/configurando-seller--tutorials_392). \n\nThe marketplace will send an object containing an array of items. The seller must use this list to get the updated information about the referred SKUs and send them back to the marketplace, following the response format explained in the API Reference. \n\nThis call is also applied in the Storefront simulation scenario, in which case the request from VTEX does not send the paramenters `country` and `postalCode`."
hidden: false
createdAt: "2020-09-01T13:10:10.114Z"
updatedAt: "2022-06-23T19:30:16.184Z"
---
The call's payload can be adapted into two scenarios: 

- **Displaying items in the storefront**: the address information can be nulled in the request, since they are not mandatory data for this context.   
- **Making a shopping cart simulation during checkout**: address information must be sent, since this data is needed to calculate freight values. If the address information (including `postalCode` and `country`) is not sent through the call, VTEX interprets the stock balance as zero. Without a valid stock balance, the seller will not be shown as an option during checkout. 


## Request body example - Indexing simulation
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"items\": [\n    {\n      \"id\": \"7908010136043\",\n      \"quantity\": 1,\n      \"seller\": \"1\",\n    }\n  ],\n  \"isCheckedIn\": false,\n}",
      "language": "json"
    }
  ]
}
[/block]
## Request body example - Checkout simulation
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"items\": [\n    {\n      \"id\": \"7908010136043\",\n      \"quantity\": 1,\n      \"seller\": \"1\",\n    }\n  ],\n  \"postalCode\": \"22270-030\",\n  \"country\": \"BRA\",\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body fields to be sent by the seller

<table>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>country</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>ISO 3-digit code of the country where the delivery address is located. If you don’t want to send it, use the value null.</td>
    </tr>
    <tr>
        <td><code>items</code></td>
        <td>array</td>
        <td>Yes</td>
        <td>Contains the data about each SKU in the cart.</td>
    </tr>
    <tr>
        <td><code>&#x21B3; requestIndex</code></td>
        <td>integer</td>
        <td>Yes</td>
        <td>Posição desse item no array original (request)</td>
    </tr>
    <tr>
        <td><code>&#x21B3; attachmentOfferings</code></td>
        <td>array</td>
        <td>No</td>
        <td>Contains the attachments that are available for the SKU customization. If this array is sent, the following fields are mandatory. If you don’t have any attachment to send, this array should be empty.</b></td>
    </tr>
    <tr>
        <td><code>&nbsp;&#x21B3; name</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Attachment name.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&#x21B3; required</code></td>
        <td>boolean</td>
        <td></td>
        <td>Sets the attachment as mandatory (value = <code>true</code>) or not (value = <code>false</code>).</td>
    </tr>
    <tr>
        <td><code>&nbsp;&#x21B3; schema</code></td>
        <td>object</td>
        <td>Yes</td>
        <td>Schema for customization.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&nbsp;&#x21B3; maximumNumberOfCharacters</code></td>
        <td>integer</td>
        <td>Yes</td>
        <td>Maximum number of characters for the attachment.</td>
    </tr>
    <tr>
        <td><code>&#x21B3; id</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>SKU ID.</td>
    </tr>
    <tr>
        <td><code>&#x21B3; listPrice</code></td>
        <td>integer</td>
        <td>Yes</td>
        <td>List price. It’s the amount presented to the customer as a “previous” price that has been lowered due to a discount. Don’t separate  the decimal places. The last two digits are the cents.</td>
    </tr>
    <tr>
        <td><code>&#x21B3; measurementUnit</code></td>
        <td>string</td>
        <td>No</td>
        <td>SKU’s measurement unit.</td>
    </tr>
    <tr>
        <td><code>&#x21B3; merchantName</code></td>
        <td>string</td>
        <td>No</td>
        <td>Name of the marketplace, used to guide  payments. This field should be nulled if the marketplace is responsible for processing payments. Check out our [Split Payment](https://help.vtex.com/en/tutorial/split-de-pagamento--6k5JidhYRUxileNolY2VLx) article to know more.</td>
    </tr>
    <tr>
        <td><code>&#x21B3; offerings</code></td>
        <td>array</td>
        <td>No</td>
        <td>Services that may be offered for this SKU. Examples are the assembly of a piece of furniture or warranty. In case these information are sent, the following fields are mandatory. If you don’t want to send it, use an empty array.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&#x21B3; type</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Type of the service.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&#x21B3; id</code></td>
        <td>string</td>
        <td>No</td>
        <td>Service ID.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&#x21B3; name</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Service name.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&#x21B3; price</code></td>
        <td>integer</td>
        <td>Yes</td>
        <td>Service price. The last two digits are the cents.</td>
    </tr>
    <tr>
        <td><code>&#x21B3; price</code></td>
        <td>integer</td>
        <td>Yes</td>
        <td>Actual selling price of the SKU. Don’t separate  the decimal places. The last two digits are the cents.</td>
    </tr>
    <tr>
        <td><code>&#x21B3; priceTags</code></td>
        <td>array</td>
        <td>No</td>
        <td>List with the promotions applied to the SKU.</td>
    </tr>
    <tr>
        <td><code>&#x21B3; priceValidUntil</code></td>
        <td>string</td>
        <td>No</td>
        <td>Expiration date of the SKU price. Example: "2014-03-01T22:58:28.143". In case you don’t want to send it, use the value null.</td>
    </tr>
    <tr>
        <td><code>&#x21B3; quantity</code></td>
        <td>integer</td>
        <td>Yes</td>
        <td>Quantity of the item. The seller should send the quantity that was indicated in the request, or the maximum quantity possible.</td>
    </tr>
    <tr>
        <td><code>&#x21B3; seller</code></td>
        <td>integer</td>
        <td>Yes</td>
        <td>ID of the seller as registered in VTEX. You should send the same value that came in the request.</td>
    </tr>
    <tr>
        <td><code>&#x21B3; unitMultiplier</code></td>
        <td>integer</td>
        <td>No</td>
        <td>SKU unit multiplier. The default value is 1.</td>
    </tr>
   <tr>
        <td><code>logisticsInfo</code></td>
        <td>array</td>
        <td>Yes</td>
        <td>Array that contains the data regarding the delivery methods and stock for each item. If all products are unavailable, this field should return empty.</td>
    </tr>
    <tr>
        <td><code>&#x21B3; itemIndex</code></td>
        <td>integer</td>
        <td>Yes</td>
        <td>Position of this item in the original array, i.e., in the array that came with the request. This index is what identifies which SKU you are referring to for each object inside the logisticsInfo.</td>
    </tr>
    <tr>
        <td><code>&#x21B3; quantity</code></td>
        <td>integer</td>
        <td>Yes</td>
        <td>Quantity of the item. The seller should send the quantity that was indicated in the request, or the maximum quantity possible.</td>
    </tr>
    <tr>
        <td><code>&#x21B3; shipsTo</code></td>
        <td>array</td>
        <td>Yes</td>
        <td>ISO 3-digit code of the countries to where the SKU is delivered.</td>
    </tr>
    <tr>
        <td><code>&#x21B3; slas</code></td>
        <td>array</td>
        <td>Yes</td>
        <td>Contains the available delivery methods.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&#x21B3; id</code></td>
        <td>integer</td>
        <td>Yes</td>
        <td>Identifier of the delivery method.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&#x21B3; deliveryChannel</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Type of sales channel. The values that are possible are: <code>pickup-in-point</code> for pickup point and <code>delivery</code> for regular delivery.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&#x21B3; name</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Name of the delivery method.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&#x21B3; shippingEstimate</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Time estimated for the delivery. Possible suffixes are <code>bd</code> for “business day” , <code>h</code> for “hours”, and <code>m</code> for “minutes”.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&#x21B3; price</code></td>
        <td>integer</td>
        <td>Yes</td>
        <td>Delivery price. The two last digits are the cents.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&#x21B3; availableDeliveryWindows </code></td>
        <td>array</td>
        <td>No</td>
        <td>Contains the delivery windows available for the SLA. Below fields with * are required if delivery windows are sent.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&nbsp;&#x21B3; startDateUtc</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Start date of the delivery window.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&nbsp;&#x21B3; endDateUtc</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>End date of the delivery window.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&nbsp;&#x21B3; price</code></td>
        <td>integer</td>
        <td>Yes</td>
        <td>Extra price for scheduled delivery. The last two digits are the cents.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&#x21B3; pickupStoreInfo</code></td>
        <td>object</td>
        <td>Yes</td>
        <td>Contains the data about the pickup point. If you don’t want to send this, use the value null.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&nbsp;&#x21B3; isPickupStore</code></td>
        <td>boolean</td>
        <td>Yes</td>
        <td><code>true</code> if it is a pickup point.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&nbsp;&#x21B3; friendlyName</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Friendly name of the pickup point.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&nbsp;&#x21B3; address</code></td>
        <td>array</td>
        <td>Yes</td>
        <td>Address data of the pickup point.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&nbsp;&nbsp;&#x21B3; addressType</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>The possible value is pickup.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&nbsp;&nbsp;&#x21B3; receiverName</code></td>
        <td>array</td>
        <td>No</td>
        <td>Name of the person who will receive the product. May be sent as null.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&nbsp;&nbsp;&#x21B3; addressId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Identifies the pickup point.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&nbsp;&nbsp;&#x21B3; postalCode</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Postal code of the pickup point. This field is mandatory, for shopping carts simulations, where both Country and Postal Code are required. This field should be sent as `null` for storefront simulations, where the information is not necessary.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&nbsp;&nbsp;&#x21B3; city</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>City of the pickup point.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&nbsp;&nbsp;&#x21B3; state</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>State of the pickup point.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&nbsp;&nbsp;&#x21B3; country</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>3-digit ISO code of the country where the pickup point is located.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&nbsp;&nbsp;&#x21B3; street</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Street where the pickup point is located.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&nbsp;&nbsp;&#x21B3; number</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Address number of the pickup point.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&nbsp;&nbsp;&#x21B3; neighborhood</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Neighborhood where the pickup point is located.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&nbsp;&nbsp;&#x21B3; complement</code></td>
        <td>string</td>
        <td>No</td>
        <td>Complement of the pickup point address.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&nbsp;&nbsp;&#x21B3; reference</code></td>
        <td>string</td>
        <td>No</td>
        <td>A reference for the pickup point address.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&nbsp;&nbsp;&#x21B3; geoCoordinates</code></td>
        <td>array</td>
        <td>Yes</td>
        <td>Contains the geographic coordinates of the pickup point.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&nbsp;&#x21B3; additionalInfo</code></td>
        <td>string</td>
        <td>No</td>
        <td>Description or extra information about the pickup point.</td>
    </tr>
    <tr>
        <td><code>&#x21B3; stockBalance</code></td>
        <td>integer</td>
        <td>Yes</td>
        <td>Stock balance of the SKU.</td>
    </tr>
    <tr>
        <td><code>&#x21B3; deliveryChannels</code></td>
        <td>array</td>
        <td>Yes</td>
        <td>Contains the stock balance for each channel.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&#x21B3; id</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Identifies the channel type whose stock balance will be informed in the next field. Possible values are: pickup-in-point for pickup point and delivery for regular delivery.</td>
    </tr>
    <tr>
        <td><code>&nbsp;&#x21B3; stockBalance</code></td>
        <td>integer</td>
        <td>Yes</td>
        <td>Stock balance for the channel type selected in the previous field.</td>
    </tr>
    <tr>
        <td><code>geoCoordinates</code></td>
        <td>array</td>
        <td>No</td>
        <td>Geographic coordinates of the delivery address. If it’s not sent, use an empty array here.</td>
    </tr>
    <tr>
        <td><code>postalCode</code></td>
        <td>string</td>
        <td>No</td>
        <td>Postal code of the delivery address. This field is mandatory, for shopping carts simulations, where both Country and Postal Code are required. This field should be sent as `null` for storefront simulations, where the information is not necessary.</td>
    </tr>
</table>

## Response body example
[block:code]
{
  "codes": [
    {
      "code": "{\n   \"country\": \"BRA\",\n   \"items\": [\n         {\n         \"id\": \"2000037\",\n         \"listPrice\": 67203,\n         \"measurementUnit\": \"un\",\n         \"merchantName\": \"mySeller1\",\n         \"offerings\":[\n           {\n              \"type\": \"Warranty\",\n              \"id\": \"5\",\n              \"name\": \"1 year warranty\",\n              \"price\": 10000\n           }\n        ],\n         \"price\": 67203,\n         \"priceTags\": [],\n         \"priceValidUntil\": null,\n         \"quantity\": 1,\n         \"requestIndex\": 0,\n         \"seller\": \"1\",\n         \"unitMultiplier\": 1\n      }\n   ],\n   \"logisticsInfo\": [\n      {\n         \"itemIndex\": 0,\n         \"quantity\": 1,\n         \"shipsTo\": [\n            \"BRA\"\n         ],\n         \"slas\": [\n            {\n               \"id\": \"Regular\",\n               \"deliveryChannel\": \"delivery\",\n               \"name\": \"Regular Delivery\",\n               \"price\": 846,\n               \"shippingEstimate\": \"19bd\"\n            },\n            {\n               \"id\": \"Curbside pickup\",\n               \"deliveryChannel\": \"pickup-in-point\",\n               \"name\": \"Curbside pickup\",\n               \"shippingEstimate\": \"0bd\",\n               \"price\": 0,\n               \"availableDeliveryWindows\": [\n                {\n                   \"startDateUtc\": \"2013-02-04T08:00:00+00:00\",\n                   \"endDateUtc\": \"2013-02-04T13:00:00+00:00\",\n                   \"price\": 0\n                }\n              ],\n               \"pickupStoreInfo\": {\n                  \"isPickupStore\": true,\n                  \"friendlyName\": \"Santa Felicidade\",\n                  \"address\": {\n                     \"addressType\": \"pickup\",\n                     \"receiverName\": null,\n                     \"addressId\": \"548304ed-dd40-4416-b12b-4b32bfa7b1e0\",\n                     \"postalCode\": \"82320-040\",\n                     \"city\": \"Curitiba\",\n                     \"state\": \"PR\",\n                     \"country\": \"BRA\",\n                     \"street\": \"Rua Domingos Strapasson\",\n                     \"number\": \"100\",\n                     \"neighborhood\": \"Santa Felicidade\",\n                     \"complement\": \"Loja 10\",\n                     \"reference\": null,\n                     \"geoCoordinates\": [\n                        -49.334934,\n                        -25.401705\n                     ]\n                  },\n                  \"additionalInfo\": \"\"\n               }\n            }\n         ],\n         \"stockBalance\": 199,\n         \"deliveryChannels\": [\n            {\n               \"id\": \"delivery\",\n               \"stockBalance\": 179\n            },\n            {\n               \"id\": \"pickup-in-point\",\n               \"stockBalance\": 20\n            }\n         ]\n      }\n   ],\n   \"postalCode\": \"80250000\"\n}",
      "language": "json"
    }
  ]
}
[/block]