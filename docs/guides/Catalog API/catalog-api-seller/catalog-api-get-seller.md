---
title: "Get Seller by ID"
slug: "catalog-api-get-seller"
excerpt: "Retrieves the seller's details by its ID."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2022-04-19T00:02:26.517Z"
---
[block:callout]
{
  "type": "warning",
  "body": "Check out the updated version of the Sellers' endpoints in our [Marketplace API documentation](https://developers.vtex.com/vtex-rest-api/reference/sellers). If you are doing this integration for the first time, we recommend that you follow the updated documentation.",
  "title": "New version of Sellers API"
}
[/block]
## Response object has the following properties: 


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `SellerId` | integer | Seller ID |
| `Name` | string |  Seller Name |
| `Email` | string | E-mail from Seller Administrator |
| `Description` | string | Seller Description  |
| `ExchangeReturnPolicy` | string | Details about Seller Exchange Return Policy | 
| `DeliveryPolicy` | string | Details about Seller Delivery Policy |  
| `UseHybridPaymentOptions` | boolean | If will uses Hybrid Payment between Seller and Marketplace |
| `UserName` | string | UserName in case the integration isn't between VTEX stores  |
| `Password` | string | Password in case the integration isn't between VTEX stores |
| `SecutityPrivacyPolicy` | string | Details about Seller Security Privacy Policy |
| `CNPJ` | string | Seller Company Register Document  |
| `CSCIdentification` | string | Seller Identification |
| `ArchiveId` | integer | Image ID |
| `UrlLogo` | string | Seller URL logo |
| `Category` | string | Product Category |
| `ProductCommissionPercentage` | decimal | Product Comission Percentage  |
| `FreightCommissionPercentage` | decimal | Freight Comission Percentage  |
| `CategoryCommissionPercentage` | decimal |  Category Comission Percentage   |
| `FulfillmentEndpoint` | string| URL of the endpoint for fulfillment of seller's orders, which the marketplace will use to communicate with the seller  |
| `CatalogSystemEndpoint` | decimal | URL of the endpoint of the seller's catalog. This field will only be displayed if the seller type is `VTEX Store` |
| `IsActive` | boolean | Condition if the seller is active or not |
| `MerchantName` | string |   |
| `FulfillmentSellerId` | string | Identification code of the seller responsible for fulfilling the order   |
| `SellerType` | integer | Seller type. Add `1` to a normal seller or `2` to a seller whitelabel  |
| `IsBetterScope` | boolean | Field used by the Checkout to simulate items. Only sellers white label can have this field as `true` |


## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"SellerId\": \"externalseller\",\n    \"Name\": \"External Seller\",\n    \"Email\": \"seller@email.com\",\n    \"Description\": \"\",\n    \"ExchangeReturnPolicy\": \"\",\n    \"DeliveryPolicy\": \"\",\n    \"UseHybridPaymentOptions\": false,\n    \"UserName\": \"\",\n    \"Password\": \"\",\n    \"SecutityPrivacyPolicy\": \"\",\n    \"CNPJ\": \"\",\n    \"CSCIdentification\": \"\",\n    \"ArchiveId\": null,\n    \"UrlLogo\": \"\",\n    \"ProductCommissionPercentage\": 30.00,\n    \"FreightCommissionPercentage\": 10.00,\n    \"CategoryCommissionPercentage\": null,\n    \"FulfillmentEndpoint\": \"https://sellerendpoint.com/\",\n    \"CatalogSystemEndpoint\": null,\n    \"IsActive\": true,\n    \"MerchantName\": \"\",\n    \"FulfillmentSellerId\": \"\",\n    \"SellerType\": 1,\n    \"IsBetterScope\": false\n}",
      "language": "json"
    }
  ]
}
[/block]