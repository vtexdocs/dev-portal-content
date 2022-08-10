---
title: "Marketplace API overview"
slug: "marketplace-api-overview"
hidden: false
createdAt: "2020-10-27T14:57:55.698Z"
updatedAt: "2021-03-12T17:25:53.606Z"
---
# Marketplace API

We define as **marketplace **the store where a purchase is performed. It's the environment where the customer pays for an order.  A **seller **can be understood as the product owner. It owns the product, being responsible for its distribution logistics, inventory maintenance, handling and shipping throug the carriers.

Both sellers and marketplace operators use the Marketplace API to manage their offers, relying on VTEX's capabilities.
[block:callout]
{
  "type": "info",
  "body": "The [seller must be registered by the marketplace](https://help.vtex.com/tutorial/configurando-seller--tutorials_392) before products can be submitted.",
  "title": "Seller configuration"
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "The marketplace must [create an appKey and appToken](https://developers.vtex.com/docs/getting-started-authentication#section-creating-the-appkey-and-apptoken) for each non-VTEX seller that will use this API.",
  "title": "Authorization"
}
[/block]
# Index

## Notification

*Endpoints used by sellers to notify marketplaces that the price or inventory language has changed for one of their SKUs.*

<span class="api"><span class="pg-type type-post">post</span> [Notify marketplace of price update](https://developers.vtex.com/vtex-developer-docs/reference/notification#price-notification)
<span class="api"><span class="pg-type type-post">post</span> [Notify marketplace of inventory update](https://developers.vtex.com/vtex-developer-docs/reference/notification#inventory-notification)


## SKU Approval Settings

*Allow marketplaces to configure rules for automatically and manually approving SKUs received from sellers.*

<span class="api"><span class="pg-type type-get">get</span>[Get autoApprove Status in Account Settings](https://developers.vtex.com/vtex-developer-docs/reference/sku-approval-settings#get-autoapprove-value)
<span class="api"><span class="pg-type type-put">put</span>[Activate autoApprove in Marketplace's Account](https://developers.vtex.com/vtex-developer-docs/reference/sku-approval-settings#activate-autoapprove-for-account)
<span class="api"><span class="pg-type type-get">get</span>[Get Account's Approval Settings](https://developers.vtex.com/vtex-developer-docs/reference/sku-approval-settings#getaccountconfig)
<span class="api"><span class="pg-type type-put">put</span>[Save Account's Approval Settings](https://developers.vtex.com/vtex-developer-docs/reference/sku-approval-settings#saveaccountconfig)
<span class="api"><span class="pg-type type-get">get</span>[Get Seller's Approval Settings
](https://developers.vtex.com/vtex-developer-docs/reference/sku-approval-settings#getselleraccountconfig)
<span class="api"><span class="pg-type type-put">put</span>[Save Seller's Approval Settings
](https://developers.vtex.com/vtex-developer-docs/reference/sku-approval-settings#putselleraccountconfig)
<span class="api"><span class="pg-type type-put">put</span>[Activate autoApprove Setting for a Seller](https://developers.vtex.com/vtex-developer-docs/reference/sku-approval-settings#activate-autoapprove-for-seller)


## Get Suggestions

*Search and filter all suggestions using specific criteria.*
<span class="api"><span class="pg-type type-get">get</span> [Get all SKU Suggestions](https://developers.vtex.com/vtex-developer-docs/reference/get-suggestions-1#get-all-sku-suggestions)
<span class="api"><span class="pg-type type-get">get</span> [Get SKU Suggestion by ID]https://developers.vtex.com/vtex-developer-docs/reference/get-suggestions-1#get-sku-suggestions-by-id)


## Manage Suggestions

*Send or delete SKU suggestions from the seller to marketplace.*
<span class="api"><span class="pg-type type-put">put</span> [Send SKU Suggestion](https://developers.vtex.com/vtex-developer-docs/reference/manage-suggestions-1)
<span class="api"><span class="pg-type type-delete">delete</span> [Delete SKU Suggestion](https://developers.vtex.com/vtex-developer-docs/reference/manage-suggestions-1#delete-sku-suggestion)

## Get Versions

*Search and filter all versions of suggestions, using specific criteria.*
<span class="api"><span class="pg-type type-get">get</span> [Get all versions](https://developers.vtex.com/vtex-developer-docs/reference/get-versions-1#get-all-versions)
<span class="api"><span class="pg-type type-get">get</span> [Get version by ID](https://developers.vtex.com/vtex-developer-docs/reference/get-versions-1#get-version-by-id)

## Match Received SKUs

*Sellers select and send products to be sold in the marketplace. Those products sent by sellers become **received SKUs** that the marketplace operator reviews and approves.*
<span class="api"><span class="pg-type type-put">put</span> [Match Received SKUs individually](https://developers.vtex.com/vtex-developer-docs/reference/match-received-skus-1#match-received-skus-individually
<span class="api"><span class="pg-type type-put">put</span> [Match Multiple Received SKUs](https://developers.vtex.com/vtex-developer-docs/reference/match-received-skus-1#match-multiple-received-skus)


## Review Received SKUs
*The Review Received SKUs API allows marketplace operators to request sellers to review the sent SKUs that were either refused or pending approval. Thus, marketplace operators can point out the exact fields that need sellers’ review.*
<span class="api"><span class="pg-type type-get">get</span> [Get SKU’s review information](https://developers.vtex.com/vtex-developer-docs/reference/review-received-skus#get-sku-review-information)
<span class="api"><span class="pg-type type-put">put</span> [Request SKU review from seller](https://developers.vtex.com/vtex-developer-docs/reference/review-received-skus#request-sku-review)



## Matched Offers
*Offers are seller products and SKUs that were sent to the marketplace, and already have their price and inventory level configured.*
<span class="api"><span class="pg-type type-get">get</span> [Get Matched Offer's Data by SKU ID
](https://developers.vtex.com/vtex-developer-docs/reference/matched-offers#marketplace-api-get-matched-offers-skuid)
<span class="api"><span class="pg-type type-get">get</span> [Get Matched Offer's Data by Product ID
](https://developers.vtex.com/vtex-developer-docs/reference/matched-offers#marketplace-api-get-matched-offers-productid)