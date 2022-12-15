---
title: "Get Seller by ID"
slug: "catalog-api-get-seller"
excerpt: "Retrieves the seller's details by its ID."
hidden: true
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2022-12-02T21:22:14.464Z"
---
[block:callout]
{
  "type": "warning",
  "body": "This is part of a legacy version of the Sellers' endpoints. Check out the updated version in our [Marketplace API documentation](https://developers.vtex.com/vtex-rest-api/reference/sellers). If you are doing this integration for the first time, we recommend that you follow the updated documentation instead.",
  "title": "New version of Sellers API"
}
[/block]
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