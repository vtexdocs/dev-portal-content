---
title: "Contextual price per shopper"
slug: "contextual-price-per-shopper"
hidden: false
createdAt: "2025-02-13T13:00:00.152Z"
updatedAt: "2025-05-19T13:00:00.152Z"
---
Contextual price allows you to define different prices for a product based on the sale context. These contexts can include criteria such as the marketplace, the seller offering the product, the buyer's geolocation, or active promotions.

This feature is ideal for scenarios where multiple sellers sell the same SKU on a marketplace but want to apply specific pricing strategies for customers or regions. Thus, the final price of the SKU can vary depending on the seller and the context of the sale.

## Configuring custom prices in B2B marketplaces

To apply contextual pricing per seller in a B2B marketplace scenario, it is necessary to use the Audience Manager and Price Table Mapper APIs. These APIs enable sellers to configure custom price tables for each customer, using email addresses as a reference.

### Marketplace configuration

Follow the steps below to ensure that all the prerequisites are met:

1. **Activate Audience Manager:** Contact [VTEX support](https://help.vtex.com/support?/cultureInfo=pt-br) and request the activation of the Audience Manager feature toggle for the Checkout module in the marketplace and sellers accounts.

2. **Allow email sharing:**  Set the `TrustPolicy` field to the value `AllowEmailSharing` when creating or updating a seller using the [POST Create Seller](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog_system/pvt/seller) or [PUT Update Seller endpoints](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog_system/pvt/seller). This allows the marketplace to share customers' email addresses with the sellers.

### Seller configuration

Sellers must configure price lists associated with customer email addresses using the [Fetch audience](https://developers.vtex.com/docs/api-reference/audience-api#post-/api/audience-manager/pvt/audience?endpoint=post-/api/audience-manager/pvt/audience) endpoint of the **Audience Manager** API. This API generates a unique `audienceId` (UUID) based on the content of a JSON payload, which can be used to save price tables via the **Price Table Mapper** API.

This operation requires the buyer email as an input parameter. See the example below:

#### POST - Fetch audience

`https://{accountName}.{environment}.com.br/api/audience-manager/pvt/audience`

Request body

```json
{
  "email": "email-do-comprador@email.com"
}
```

If the request is successful (**status 200 OK**), the endpoint will return an array with the ID of one or more audiences associated with the provided email, which will be used in the following steps to configure the pricing table.

Response body

```json
[
    "f8cb4d62-b43a-599c-89cc-027fadaa4b18"
]
```

> ℹ️ Any change to the payload will generate a new UUID, representing an audience created based on the updated content of the payload.

## Configuring price tables

With the audience ID obtained, configure the price table using the [Set price table mapping](https://developers.vtex.com/docs/api-reference/audience-api#put-/api/price-table-mapper/pvt/mapping/-audienceId-) endpoint of the **Price Table Mapper** API, where you can associate price table IDs with customer group IDs (audiences).

See the example below:

### PUT - Set price table mapping

`https://{accountName}.{environment}.com.br/api/price-table-mapper/pvt/mapping/{audienceId}`

Request body

```json
[
    "gold-price-table"
]
```

In `{audienceId}`, use the desired audience ID. The endpoint will associate the `gold-price-table` with the `{audienceId}` and return the **status 204 No Content** indicating that the operation was successfully completed.

>⚠️ If there are no price tables configured for a specific customer (audienceId), the system will automatically apply the base price. Besides, the pricing strategy defined for the account, such as "Lowest price," "Highest price," or "First price list," will influence the final price applied.

## Removing a price table configuration

To remove the configuration of a price table for a specific audience, use the endpoint [Delete price table mapping](https://developers.vtex.com/docs/api-reference/audience-api#delete-/api/price-table-mapper/pvt/mapping/-audienceId-).

### DELETE - Delete price table mapping

`https://{accountName}.{environment}.com.br/api/price-table-mapper/pvt/mapping/{audienceId}`

Replace `{audienceId}` with the ID of the audience from which you want to remove the price table. After the call, the endpoint will return the **status 204 No Content**, confirming that the price table has been removed from the audience.

## Recovering the price table mapping

To query the price table mapping of a specific audience, use the [GET price table mapping endpoint](https://developers.vtex.com/docs/api-reference/audience-api#get-/api/price-table-mapper/pvt/mapping/-audienceId-?endpoint=get-/api/price-table-mapper/pvt/mapping/-audienceId-).

### GET - Get price table mapping

`https://{accountName}.{environment}.com.br/api/price-table-mapper/pvt/mapping/{audienceId}`

Replace `{audienceId}' with the ID of the audience you want to query. If the request is successful, the API will return an array containing the name of the pricing table associated with the audience ID. See the example below:

Response body

```json
[
    "gold-price-table"
]
```