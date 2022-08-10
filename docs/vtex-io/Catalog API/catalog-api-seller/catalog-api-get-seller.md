---
title: "Get Seller by Id"
slug: "catalog-api-get-seller"
excerpt: "Retrieves the seller's details by its ID."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2021-05-27T18:39:59.843Z"
---
Retrieves the Seller details by its ID



| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `SellerId` | integer | Seller ID |



For example, in case you need get details from sellerId  `myseller`.

You will have to replace de variable `sellerId` for `myseller` :

```
https://{{accountName}}.{{environment}}.com.br/api/catalog_system/pvt/seller/myseller
```





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
| `Category` | string | Product Category |
| `ProductCommissionPercentage` | decimal | Product Comission Percentage  |
| `FreightCommissionPercentage` | decimal | Freight Comission Percentage  |
| `ArchiveId` | integer | Image ID |
| `UrlLogo` | string | Seller URL logo |




## Authentication

This is a private API and need credentials with viewer access


> know more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)