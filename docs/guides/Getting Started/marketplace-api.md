---
title: "Marketplace API"
slug: "marketplace-api"
hidden: true
createdAt: "2021-04-12T18:20:19.152Z"
updatedAt: "2021-04-12T18:20:19.152Z"
---
The **Marketplace API** enables marketplaces and sellers hosted on VTEX to perform their collaborative operations.  
[block:callout]
{
  "type": "warning",
  "body": "The marketplace must [create an appKey and appToken](https://developers.vtex.com/docs/getting-started-authentication#section-creating-the-appkey-and-apptoken) for each non-VTEX seller that will use this API.",
  "title": "Authorization"
}
[/block]
# Index

## Get Suggestions

*Search and filter all suggestions using specific criteria.*
<span class="api"><span class="pg-type type-get">get</span> [Get all SKU Suggestions](https://developers.vtex.com/vtex-rest-api/reference/get-suggestions-1#get-all-sku-suggestions)
<span class="api"><span class="pg-type type-get">get</span> [Get SKU Suggestion by ID](https://developers.vtex.com/vtex-rest-api/reference/get-suggestions-1#get-sku-suggestions-by-id)


## Manage Suggestions

*Send or delete SKU suggestions from the seller to marketplace.*
<span class="api"><span class="pg-type type-put">put</span> [Send SKU Suggestion](https://developers.vtex.com/vtex-rest-api/reference/manage-suggestions-1#send-sku-suggestion)
<span class="api"><span class="pg-type type-delete">delete</span> [Delete SKU Suggestion](https://developers.vtex.com/vtex-rest-api/reference/manage-suggestions-1#delete-sku-suggestion)

## Get Versions

*Search and filter all versions of suggestions, using specific criteria.*
<span class="api"><span class="pg-type type-get">get</span> [Get all versions](https://developers.vtex.com/vtex-rest-api/reference/get-versions-1#get-all-versions)
<span class="api"><span class="pg-type type-get">get</span> [Get version by ID](https://developers.vtex.com/vtex-rest-api/reference/get-versions-1#get-version-by-id)

## Match Received SKUs

*Match SKU suggestions received in the marketplace.*
<span class="api"><span class="pg-type type-put">put</span> [Match Received SKUs individually](https://developers.vtex.com/vtex-rest-api/reference/match-received-skus-1#match-received-skus-individually)
<span class="api"><span class="pg-type type-put">put</span> [Match Multiple Received SKUs](https://developers.vtex.com/vtex-rest-api/reference/match-received-skus-1#match-multiple-received-skus)


## Notifications

*Endpoints used by sellers to notify marketplaces that the price or inventory language has changed for one of their SKUs.*

<span class="api"><span class="pg-type type-post">post</span> [Notify marketplace of price update](https://developers.vtex.com/vtex-rest-api/reference/notification#price-notification)
<span class="api"><span class="pg-type type-post">post</span> [Notify marketplace of inventory update](https://developers.vtex.com/vtex-rest-api/reference/notification#inventory-notification)


## SKU Approval Settings

*Allows marketplaces to configure rules for automatically and manually approving SKUs received from sellers.*

<span class="api"><span class="pg-type type-get">get</span>[Get autoApprove Status in Account Settings](https://developers.vtex.com/vtex-rest-api/reference/sku-approval-settings#get-autoapprove-value)  
<span class="api"><span class="pg-type type-put">put</span>[Activate autoApprove in Marketplace's Account](https://developers.vtex.com/vtex-rest-api/reference/sku-approval-settings#activate-autoapprove-for-account)  
<span class="api"><span class="pg-type type-get">get</span>[Get Account's Approval Settings](https://developers.vtex.com/vtex-rest-api/reference/sku-approval-settings#getaccountconfig)  
<span class="api"><span class="pg-type type-put">put</span>[Save Account's Approval Settings](https://developers.vtex.com/vtex-rest-api/reference/sku-approval-settings#saveaccountconfig)    
<span class="api"><span class="pg-type type-get">get</span>[Get Seller's Approval Settings](https://developers.vtex.com/vtex-rest-api/reference/sku-approval-settings#getselleraccountconfig)
<span class="api"><span class="pg-type type-put">put</span>[Save Seller's Approval Settings](https://developers.vtex.com/vtex-rest-api/reference/sku-approval-settings#putselleraccountconfig)    
<span class="api"><span class="pg-type type-put">put</span>[Activate autoApprove Setting for a Seller](https://developers.vtex.com/vtex-rest-api/reference/sku-approval-settings#activate-autoapprove-for-seller)  


## Review Received SKUs
*Allows marketplace operators to request sellers to review the sent SKUs that were either refused or pending approval. Thus, marketplace operators can point out the exact fields that need sellers’ review.*
<span class="api"><span class="pg-type type-get">get</span>[Get SKU’s review information](https://developers.vtex.com/vtex-rest-api/reference/review-received-skus#get-sku-review-information)  
<span class="api"><span class="pg-type type-put">put</span>[Request SKU review from seller](https://developers.vtex.com/vtex-rest-api/reference/review-received-skus#request-sku-review)  


## Matched Offers
 *Offers are seller products and SKUs that were sent to the marketplace, and already have their price and inventory level configured.*
<span class="api"><span class="pg-type type-get">get</span>[Get Matched Offer's Data by SKU ID](https://developers.vtex.com/vtex-rest-api/reference/matched-offers)  
<span class="api"><span class="pg-type type-get">get</span>[Get Matched Offer's Data by Product ID](https://developers.vtex.com/vtex-rest-api/reference/matched-offers#marketplace-api-get-matched-offers-productid)