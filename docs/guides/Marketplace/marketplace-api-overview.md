---
title: "Marketplace API overview"
slug: "marketplace-api-overview"
hidden: false
createdAt: "2020-10-27T14:57:55.698Z"
updatedAt: "2022-02-04T13:33:39.092Z"
---

The **Marketplace API** enables marketplaces and sellers hosted on VTEX to perform their collaborative operations.  

>⚠️ The marketplace must [create an appKey and appToken](https://developers.vtex.com/docs/guides/getting-started-authentication) for each non-VTEX seller that will use this API.

## Index

### Get Suggestions

Search and filter all suggestions using specific criteria.

`GET` [Get all SKU Suggestions](https://developers.vtex.com/vtex-rest-api/reference/getsuggestions)
`GET` [Get SKU Suggestion by ID](https://developers.vtex.com/vtex-rest-api/reference/getsuggestion)

### Manage Suggestions

Send or delete SKU suggestions from the seller to marketplace.
`PUT` [Send SKU Suggestion](https://developers.vtex.com/vtex-rest-api/reference/savesuggestion)
`DELETE` [Delete SKU Suggestion](https://developers.vtex.com/vtex-rest-api/reference/deletesuggestion)

### Get Versions

Search and filter all versions of suggestions, using specific criteria.
`GET` [Get all versions](https://developers.vtex.com/vtex-rest-api/reference/getversions)
`GET` [Get version by ID](https://developers.vtex.com/vtex-rest-api/reference/getsuggestionbyversion)

### Match Received SKUs

Match SKU suggestions received in the marketplace.
`PUT` [Match Received SKUs individually](https://developers.vtex.com/vtex-rest-api/reference/match)
`PUT` [Match Multiple Received SKUs](https://developers.vtex.com/vtex-rest-api/reference/matchmultiple)

### Notifications

Endpoints used by sellers to notify marketplaces that the price or inventory language has changed for one of their SKUs.

`POST` [Notify marketplace of price update](https://developers.vtex.com/vtex-rest-api/reference/pricenotification)
`POST` [Notify marketplace of inventory update](https://developers.vtex.com/vtex-rest-api/reference/inventorynotification)

### SKU Approval Settings

Allows marketplaces to configure rules for automatically and manually approving SKUs received from sellers.

`GET`[Get autoApprove Status in Account Settings](https://developers.vtex.com/vtex-rest-api/reference/getautoapprovevaluefromconfig)  
`PUT`[Activate autoApprove in Marketplace's Account](https://developers.vtex.com/vtex-rest-api/reference/saveautoapproveforaccount)  
`GET`[Get Account's Approval Settings](https://developers.vtex.com/vtex-rest-api/reference/getaccountconfig)  
`PUT`[Save Account's Approval Settings](https://developers.vtex.com/vtex-rest-api/reference/saveaccountconfig)
`GET`[Get Seller's Approval Settings](https://developers.vtex.com/vtex-rest-api/reference/getselleraccountconfig)
`PUT`[Save Seller's Approval Settings](https://developers.vtex.com/vtex-rest-api/reference/putselleraccountconfig)
`PUT`[Activate autoApprove Setting for a Seller](https://developers.vtex.com/vtex-rest-api/reference/saveautoapproveforaccountseller)  

### Review Received SKUs

Allows marketplace operators to request sellers to review the sent SKUs that were either refused or pending approval. Thus, marketplace operators can point out the exact fields that need sellers’ review.

`GET`[Get SKU’s review information](https://developers.vtex.com/vtex-rest-api/reference/getreview)  
`PUT`[Request SKU review from seller](https://developers.vtex.com/vtex-rest-api/reference/putreview)  

### Matched Offers

Offers are seller products and SKUs that were sent to the marketplace, and already have their price and inventory level configured.

`GET`[Get Matched Offers List](https://developers.vtex.com/vtex-rest-api/reference/getofferslist)
`GET`[Get Matched Offer's Data by SKU ID](https://developers.vtex.com/vtex-rest-api/reference/getskuoffers)  
`GET`[Get Matched Offer's Data by Product ID](https://developers.vtex.com/vtex-rest-api/reference/getproductoffers)