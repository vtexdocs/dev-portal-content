---
title: "Marketplace API overview"
slug: "marketplace-api-overview"
hidden: false
createdAt: "2020-10-27T14:57:55.698Z"
updatedAt: "2022-02-04T13:33:39.092Z"
---
The **Marketplace API** enables marketplaces and sellers hosted on VTEX to perform their collaborative operations.  
[block:callout]
{
  "type": "warning",
  "body": "The marketplace must [create an appKey and appToken](https://developers.vtex.com/docs/getting-started-authentication#section-creating-the-appkey-and-apptoken) for each non-VTEX seller that will use this API.",
  "title": "Authorization"
}
[/block]

## Index

### Get Suggestions

*Search and filter all suggestions using specific criteria.*
<span class="api pg-type type-get">get</span> [Get all SKU Suggestions](https://developers.vtex.com/vtex-rest-api/reference/getsuggestions)
<span class="api pg-type type-get">get</span> [Get SKU Suggestion by ID](https://developers.vtex.com/vtex-rest-api/reference/getsuggestion)

### Manage Suggestions

*Send or delete SKU suggestions from the seller to marketplace.*
<span class="api pg-type type-put">put</span> [Send SKU Suggestion](https://developers.vtex.com/vtex-rest-api/reference/savesuggestion)
<span class="api pg-type type-delete">delete</span> [Delete SKU Suggestion](https://developers.vtex.com/vtex-rest-api/reference/deletesuggestion)

### Get Versions

*Search and filter all versions of suggestions, using specific criteria.*
<span class="api pg-type type-get">get</span> [Get all versions](https://developers.vtex.com/vtex-rest-api/reference/getversions)
<span class="api pg-type type-get">get</span> [Get version by ID](https://developers.vtex.com/vtex-rest-api/reference/getsuggestionbyversion)

### Match Received SKUs

*Match SKU suggestions received in the marketplace.*
<span class="api pg-type type-put">put</span> [Match Received SKUs individually](https://developers.vtex.com/vtex-rest-api/reference/match)
<span class="api pg-type type-put">put</span> [Match Multiple Received SKUs](https://developers.vtex.com/vtex-rest-api/reference/matchmultiple)

### Notifications

*Endpoints used by sellers to notify marketplaces that the price or inventory language has changed for one of their SKUs.*

<span class="api pg-type type-post">post</span> [Notify marketplace of price update](https://developers.vtex.com/vtex-rest-api/reference/pricenotification)
<span class="api pg-type type-post">post</span> [Notify marketplace of inventory update](https://developers.vtex.com/vtex-rest-api/reference/inventorynotification)

### SKU Approval Settings

*Allows marketplaces to configure rules for automatically and manually approving SKUs received from sellers.*

<span class="api pg-type type-get">get</span>[Get autoApprove Status in Account Settings](https://developers.vtex.com/vtex-rest-api/reference/getautoapprovevaluefromconfig)  
<span class="api pg-type type-put">put</span>[Activate autoApprove in Marketplace's Account](https://developers.vtex.com/vtex-rest-api/reference/saveautoapproveforaccount)  
<span class="api pg-type type-get">get</span>[Get Account's Approval Settings](https://developers.vtex.com/vtex-rest-api/reference/getaccountconfig)  
<span class="api pg-type type-put">put</span>[Save Account's Approval Settings](https://developers.vtex.com/vtex-rest-api/reference/saveaccountconfig)
<span class="api pg-type type-get">get</span>[Get Seller's Approval Settings](https://developers.vtex.com/vtex-rest-api/reference/getselleraccountconfig)
<span class="api pg-type type-put">put</span>[Save Seller's Approval Settings](https://developers.vtex.com/vtex-rest-api/reference/putselleraccountconfig)
<span class="api pg-type type-put">put</span>[Activate autoApprove Setting for a Seller](https://developers.vtex.com/vtex-rest-api/reference/saveautoapproveforaccountseller)  

### Review Received SKUs

*Allows marketplace operators to request sellers to review the sent SKUs that were either refused or pending approval. Thus, marketplace operators can point out the exact fields that need sellers’ review.*
<span class="api pg-type type-get">get</span>[Get SKU’s review information](https://developers.vtex.com/vtex-rest-api/reference/getreview)  
<span class="api pg-type type-put">put</span>[Request SKU review from seller](https://developers.vtex.com/vtex-rest-api/reference/putreview)  

### Matched Offers

 *Offers are seller products and SKUs that were sent to the marketplace, and already have their price and inventory level configured.*
<span class="api pg-type type-get">get</span>[Get Matched Offers List](https://developers.vtex.com/vtex-rest-api/reference/getofferslist)
<span class="api pg-type type-get">get</span>[Get Matched Offer's Data by SKU ID](https://developers.vtex.com/vtex-rest-api/reference/getskuoffers)  
<span class="api pg-type type-get">get</span>[Get Matched Offer's Data by Product ID](https://developers.vtex.com/vtex-rest-api/reference/getproductoffers)
