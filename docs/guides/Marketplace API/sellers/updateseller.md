---
title: "Update Seller by Seller ID"
slug: "updateseller"
excerpt: "This endpoint allows marketplace operators to update the information of sellers connected to their account. You can replace a path's value with another value in order to update that single information. There is no need to fill all the body params available, only the one you wish to update."
hidden: false
createdAt: "2021-11-09T18:52:06.572Z"
updatedAt: "2022-04-08T17:30:06.513Z"
---
## Request body can have one of the following properties:

[block:parameters]
{
  "data": {
    "0-0": "`id`",
    "0-1": "string",
    "0-2": "Seller ID assigned by the marketplace.",
    "1-0": "`name`",
    "1-1": "string",
    "1-2": "Name of the seller's store, configured in the seller's environment.",
    "2-0": "`isActive`",
    "2-1": "boolean",
    "2-2": "Whether the seller is active on the marketplace or not.",
    "3-0": "`fulfillmentEndpoint`",
    "3-1": "string",
    "3-2": "URL of the endpoint for fulfillment of seller's orders, which the marketplace will use to communicate with the seller.",
    "4-0": "`allowHybridPayments`",
    "4-1": "boolean",
    "4-2": "Flag that allows customers to use gift cards from the seller to buy their products on the marketplace. It identifies purchases made with a gift card so that only the final price (with discounts applied) is paid to the seller.",
    "5-0": "`taxCode`",
    "5-1": "string",
    "5-2": "This code is the Identity Number for the legal entity and is linked to information in its base country.",
    "6-0": "`email`",
    "6-1": "string",
    "6-2": "Email of the admin responsible for the seller.",
    "7-0": "`description`",
    "7-1": "string",
    "7-2": "String describing the seller.",
    "8-0": "`isBetterScope`",
    "8-1": "boolean",
    "8-2": "Flag used by the VTEX Checkout to simmulate shopping carts, products and shipping only in sellers with the boolean set as `true`, avoiding performance issues.",
    "9-0": "`sellerType`",
    "9-1": "int32",
    "9-2": "Type of seller, including:\n\n1: regular seller\n\n2: whitelabel seller",
    "10-0": "`availableSalesChannels`",
    "10-1": "array of objects",
    "10-2": "Sales channel (or trade policy) available.",
    "11-0": "`CSCIdentification`",
    "11-1": "string",
    "11-2": "SKU Seller Identification.",
    "12-0": "`account`",
    "12-1": "string",
    "12-2": "Seller's account name.",
    "13-0": "`channel`",
    "13-1": "string",
    "13-2": "Channel's name.",
    "14-0": "`salesChannel`",
    "14-1": "string",
    "14-2": "Sales channel (or trade policy) associated to the seller account created.",
    "15-0": "`isVtex`",
    "15-1": "boolean",
    "15-2": "Flag determining whether the seller configured is a VTEX store or not.",
    "16-0": "`exchangeReturnPolicy`",
    "16-2": "Text describing the exchange and return policy previously agreed between the marketplace and the seller.",
    "16-1": "string",
    "17-0": "`deliveryPolicy`",
    "17-1": "string",
    "17-2": "Text describing the delivery policy previously agreed between the marketplace and the seller.",
    "18-0": "`securityPrivacyPolicy`",
    "18-1": "string",
    "18-2": "Text describing the security policy previously agreed between the marketplace and the seller.",
    "19-0": "`fulfillmentSellerId`",
    "19-1": "string",
    "19-2": "Identification code of the seller responsible for fulfilling the order. This is an optional field used when a seller sells SKUs from another seller. If the seller sells their own SKUs, it must be nulled.",
    "20-0": "`groups`",
    "20-1": "array of objects",
    "20-2": "Array of groups attached to the seller. Groups are defined by key-words that group sellers into categories defined by the marketplace when adding a new seller through the Configure Seller Account endpoint.",
    "21-0": "`user`",
    "21-1": "string",
    "21-2": "Username, if you are using a hub to integrate with the external seller.",
    "22-2": "User password, if you are using a hub to integrate with the external seller.",
    "22-0": "`password`",
    "22-1": "string",
    "23-0": "`catalogSystemEndpoint`",
    "23-1": "string",
    "23-2": "URL of the endpoint of the seller's catalog. This field will only be displayed if the seller type is VTEX Store. The field format will be as follows: `https://{sellerName}.vtexcommercestable.com.br/api/catalog_system/`.",
    "24-2": "The marketplace must first allow VTEX to share clients’ email addresses with the seller. To do so, it is necessary to set 'AllowEmailSharing' as the value for the TrustPolicy field.",
    "24-0": "`trustPolicy`",
    "24-1": "string",
    "25-0": "`integration`",
    "25-1": "string",
    "25-2": "If the integration is made by VTEX (internal-default), or an external hub.",
    "26-0": "`score`",
    "26-1": "number",
    "26-2": "Score attributed to this seller.",
    "27-0": "`offers`",
    "27-1": "object",
    "27-2": "Offers sent by external sellers that are still waiting the marketplace's approval through the Match Received SKUs endpoint.",
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Description"
  },
  "cols": 3,
  "rows": 28
}
[/block]
## Request body examples:
[block:code]
{
  "codes": [
    {
      "code": "[\n    {\n        \"operation\": \"replace\",\n        \"path\": \"/isBetterScope\",\n        \"value\": true\n    }\n]",
      "language": "json"
    },
    {
      "code": "[\n    {\n        \"operation\": \"replace\",\n        \"path\": \"/availableSalesChannels\",\n        \"value\": [\n            {\n                \"id\": 1\n            },\n            {\n                \"id\": 2\n            }\n        ]\n    }\n]",
      "language": "json"
    }
  ]
}
[/block]