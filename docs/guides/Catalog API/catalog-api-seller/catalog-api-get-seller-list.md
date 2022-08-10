---
title: "Get Seller List"
slug: "catalog-api-get-seller-list"
excerpt: "Retrieves the seller's details by its ID."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2022-04-19T00:02:08.041Z"
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
| `ArchiveId` | integer | Define what Currency Decimal Separator will be apply|




## Authentication

This is a private API which requires credentials with viewer access.


> Learn more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)