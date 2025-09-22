---
title: "Seller Opt-in Promotions"
slug: "seller-opt-in-promotions"
hidden: false
createdAt: "2025-06-11T11:03:41.334Z"
updatedAt: "2025-09-22T13:51:02.316Z"
---

The Seller opt-in promotions feature allows sellers to choose whether they want to participate in promotions on the marketplace.

>⚠️ Adding or removing sellers is not available through the Admin interface. These actions must be performed exclusively via the [Promotions & Taxes API](https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api).

## Creating promotions

You can create promotions manually in the VTEX Admin or via API.

### Via Admin

1. In the VTEX Admin, go to Promotions.
2. Click `Create Promotion` in the top right corner of the page.
3. Choose the desired type of promotion.
4. Complete the promotion details and, in the Sellers field, select the Participanting option.
5. Click `Create`.

After creating the promotion, you must configure seller participation using the API.

### Via API

Use the [Create or Update Promotion or Tax](https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api#post-/api/rnb/pvt/calculatorconfiguration) endpoint to configure promotions with opt-in.

> ℹ️ To avoid conflicts with the previous seller association model, make sure to set `idSeller` and `idSellerIsInclusive` to `null`.

Example request body with defined sellers:

```json
{
  "idSeller": null,
  "idSellerIsInclusive": null,
  "optIn": {
    "sellers": [
      "seller-id-1",
      "seller-id-2"
    ]
  },

  "name": "MY PROMOTION",
  "idCalculatorConfiguration": "",
  "type": "combo",
  "origin": "Marketplace",
  "isActive": true,
  "beginDateUtc": "2025-05-29T00:00:00.000Z",
  "endDateUtc": "2025-05-29T00:30:00.000Z",
  "newOffset": -3,
  "isFeatured": false,
  "listSku1BuyTogether": [ { "id": "1", "name": "t-shirt size P" } ],
  "listSku2BuyTogether": [ { "id": "8", "name": "t-shirt size M" } ],
  "percentualDiscountValueList1": 10,
  "percentualDiscountValueList2": 10,
  "minimumQuantityBuyTogether": 1,
  "maxUsage": 0,
  "maxUsagePerClient": 0,
  "cumulative": false,
  "accumulateWithManualPrice": false,
  "idSeller": null,
  "idSellerIsInclusive": null,
  "idsSalesChannel": [],
  "areSalesChannelIdsExclusive": true
}
```

Example request body without initially defined sellers:

```json
{
  "idSeller": null,
  "idSellerIsInclusive": null,
  "optIn": {
    "sellers": []
  },

  "name": "MY PROMOTION",
  "idCalculatorConfiguration": "",
  "type": "combo",
  "origin": "Marketplace",
  "isActive": true,
  "beginDateUtc": "2025-05-29T00:00:00.000Z",
  "endDateUtc": "2025-05-29T00:30:00.000Z",
  "newOffset": -3,
  "isFeatured": false,
  "listSku1BuyTogether": [ { "id": "1", "name": "t-shirt size P" } ],
  "listSku2BuyTogether": [ { "id": "8", "name": "t-shirt size M" } ],
  "percentualDiscountValueList1": 10,
  "percentualDiscountValueList2": 10,
  "minimumQuantityBuyTogether": 1,
  "maxUsage": 0,
  "maxUsagePerClient": 0,
  "cumulative": false,
  "accumulateWithManualPrice": false,
  "idSeller": null,
  "idSellerIsInclusive": null,
  "idsSalesChannel": [],
  "areSalesChannelIdsExclusive": true
}
```

> ℹ️ If you send invalid IDs, the promotion will still be created, but it won’t take effect, as it will be associated with non-existent participating sellers.

## Querying participating sellers

You can query participating sellers manually in the VTEX Admin or via API.

### Via Admin

1. In the VTEX Admin, go to Promotions.
2. Click the name of the promotion you created.
3. In the Sellers field, view the list of participating sellers.

![Seller-opt-in](https://images.ctfassets.net/alneenqid6w5/1YlZUUvrgcYERRM3IeJ8T2/2b2d3df08f40e071f57585c4e3af2e2b/sellers-participantes-en.png)

### Via API

Use the [Get promotion or tax by ID](https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api#get-/api/rnb/pvt/calculatorconfiguration/-idCalculatorConfiguration-) endpoint to query promotion details, including the opt-in configuration.

GET
`https://{accountName}.{environment}.com/api/rnb/pvt/calculatorconfiguration/{idCalculatorConfiguration}`

Example response for a promotion without opt-in:

```json
{
  "optIn": null
}
```

Example response for a promotion with opt-in and defined sellers:

```json
{
  "optIn": {
    "sellers": ["seller-id-1", "seller-id-2"]
  }
}
```

Example response for a promotion with opt-in and no defined sellers:

```json
{
  "optIn": {
    "sellers": []
  }
}
```

## Adding or removing participating sellers via API

To add or remove sellers in an opt-in promotion, use the Seller opt-in or opt-out endpoint.

POST

```json
'/api/rnb/pvt/calculatorConfiguration/{promotionId}/seller-opt?an={accountName}'
--header 'if-Match: {lastUpdate}'
--data '{
  "sellerIds": [{sellerIds}],
  "operation": "{operation}"
}'
```

| Field | Required | Type | Description |
| :---- | :---- | :---- | :---- |
| promotionId | true | string | ID of the promotion |
| accountName | true | string | Account that owns the promotion |
| sellerIds | true | string\[\] | List of seller IDs |
| lastUpdate | true | DateTime | Date and time of the promotion's last modification. Must match current value, otherwise, the request will fail. |
| operation | true | OptOperation \- OptIn \- OptOut | Operation to be performed. |

To add participating sellers, include their IDs in the request body.

Example request body:

```json
{
  "sellerIds": [
    "seller-id-1",
    "seller-id-2"
  ],
  "operation": "OptIn"
}
```

To remove a participating seller, send a new request with the ID of the seller you want to remove.

Example request body:

```json
{
  "sellerIds": [
    "seller-id-2"
  ],
  "operation": "OptOut"
}
```

Example response body:

```json
{
  "lastModified": "2025-01-28T17:50:13+00:00"
}
```

Response codes:

| Code | Description |
| :---- | :---- |
| 200 | Opt-in executed successfully. |
| 400 | Returned if the IdSellerIsInclusive field of the promotion is set to false. |
| 401 | Returned if the user doesn’t have the "Manage External Seller Promotions" permission. |
| 412 | Returned if the if-Match header value doesn’t match the promotion’s lastModified field, causing the request to fail. |
| 404 | Returned if no non-archived promotion with the specified ID is found. |
