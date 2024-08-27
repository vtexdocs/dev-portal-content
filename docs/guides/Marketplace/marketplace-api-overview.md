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

### Notification

Endpoints used by sellers to notify marketplaces that the price or inventory language has changed for one of their SKUs.

`POST` [Notify marketplace of price update](https://developers.vtex.com/docs/api-reference/marketplace-apis#post-/notificator/-sellerId-/changenotification/-skuId-/price)

`POST` [Notify marketplace of inventory update](https://developers.vtex.com/docs/api-reference/marketplace-apis#post-/notificator/-sellerId-/changenotification/-skuId-/inventory)

### Suggestions

#### Get Suggestions

Search and filter all suggestions using specific criteria.

`GET` [Get all SKU Suggestions](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#get-/suggestions)

`GET` [Get SKU Suggestion by ID](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#get-/suggestions/-sellerId-/-sellerSkuId-)

#### Manage Suggestions

Send or delete SKU suggestions from the seller to marketplace.

`PUT` [Send SKU Suggestion](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#put-/suggestions/-sellerId-/-sellerSkuId-)

`DELETE` [Delete SKU Suggestion](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#delete-/suggestions/-sellerId-/-sellerSkuId-)

#### Get Versions

Search and filter all versions of suggestions, using specific criteria.

`GET` [Get all versions](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#get-/suggestions/-sellerId-/-sellerskuid-/versions)

`GET` [Get version by ID](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#get-/suggestions/-sellerId-/-sellerskuid-/versions/-version-)

#### Match Received SKUs

Match SKU suggestions received in the marketplace.

`PUT` [Match Received SKUs individually](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#put-/suggestions/-sellerId-/-sellerskuid-/versions/-version-/matches/-matchid-)

`PUT` [Match Multiple Received SKUs](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#put-/suggestions/matches/action/-actionName-)

#### SKU Approval Settings

Allows marketplaces to configure rules for automatically and manually approving SKUs received from sellers.

`GET` [Get autoApprove Status in Account Settings](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#get-/suggestions/configuration/autoapproval/toggle)

`PUT` [Activate autoApprove in Marketplace's Account](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#put-/suggestions/configuration/autoapproval/toggle)

`GET` [Get Account's Approval Settings](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#get-/suggestions/configuration)

`PUT` [Save Account's Approval Settings](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#put-/suggestions/configuration)

`GET` [Get Seller's Approval Settings](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#get-/suggestions/configuration/seller/-sellerId-)

`PUT` [Save Seller's Approval Settings](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#put-/suggestions/configuration/seller/-sellerId-)

`PUT` [Activate autoApprove Setting for a Seller](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#put-/suggestions/configuration/autoapproval/toggle/seller/-sellerId-)

### Matched Offers

Offers are seller products and SKUs that were sent to the marketplace, and already have their price and inventory level configured.

`GET` [Get Matched Offers List](https://developers.vtex.com/docs/api-reference/marketplace-apis#get-/offer-manager/pvt/offers)

`GET` [Get Matched Offer's Data by SKU ID](https://developers.vtex.com/docs/api-reference/marketplace-apis#get-/offer-manager/pvt/product/-productId-/sku/-skuId-)

`GET` [Get Matched Offer's Data by Product ID](https://developers.vtex.com/docs/api-reference/marketplace-apis#get-/offer-manager/pvt/product/-productId-)

### Seller Invite

Invite sellers to join their marketplace.

`POST` [Invite Seller Lead](https://developers.vtex.com/docs/api-reference/marketplace-apis/#post-/seller-register/pvt/seller-leads)

`GET` [List Seller Lead](https://developers.vtex.com/docs/api-reference/marketplace-apis/#get-/seller-register/pvt/seller-leads)

`PUT` [Accept Seller Lead](https://developers.vtex.com/docs/api-reference/marketplace-apis/#put-/seller-register/pvt/seller-leads/-sellerLeadId-)

`GET` [Get Seller Lead's Data by Id](https://developers.vtex.com/docs/api-reference/marketplace-apis/#get-/seller-register/pvt/seller-leads/-sellerLeadId-)

`DELETE` [Delete Seller Lead](https://developers.vtex.com/docs/api-reference/marketplace-apis/#get-/seller-register/pvt/seller-leads/-sellerLeadId-)

`PUT` [Create Seller From Lead](https://developers.vtex.com/docs/api-reference/marketplace-apis/#put-/seller-register/pvt/seller-leads/-sellerLeadId-/seller)

`PUT` [Resend Seller Lead Invite](https://developers.vtex.com/docs/api-reference/marketplace-apis/#put-/seller-register/pvt/seller-leads/-sellerLeadId-/status)

### Seller Commissions

Set commissions for different categories of sellers their marketplace.

`PUT` [Upsert Seller Commissions in Bulk](https://developers.vtex.com/docs/api-reference/marketplace-apis/#put-/seller-register/pvt/sellers/-sellerId-/commissions/categories)

`GET` [List Seller Commissions by Seller ID](https://developers.vtex.com/docs/api-reference/marketplace-apis/#get-/seller-register/pvt/sellers/-sellerId-/commissions)

`PUT` [Upsert Seller Commissions by Category ID](https://developers.vtex.com/docs/api-reference/marketplace-apis/#put-/seller-register/pvt/sellers/-sellerId-/commissions/-categoryId-)

`DELETE` [Remove Seller Commissions by Category ID](https://developers.vtex.com/docs/api-reference/marketplace-apis/#delete-/seller-register/pvt/sellers/-sellerId-/commissions/-categoryId-)

`GET` [Get Seller Commissions by Category ID](https://developers.vtex.com/docs/api-reference/marketplace-apis/#get-/seller-register/pvt/sellers/-sellerId-/commissions/-categoryId-)

### Sellers

Configure the accounts of sellers who have already accepted the invitation to join their marketplace.

`POST` [Configure Seller Account](https://developers.vtex.com/docs/api-reference/marketplace-apis/#post-/seller-register/pvt/sellers)

`GET` [List Sellers](https://developers.vtex.com/docs/api-reference/marketplace-apis/#get-/seller-register/pvt/sellers)

`PATCH` [Update Seller by Seller ID](https://developers.vtex.com/docs/api-reference/marketplace-apis/#patch-/seller-register/pvt/sellers/-sellerId-)

`GET` [Get Seller data by ID](https://developers.vtex.com/docs/api-reference/marketplace-apis/#get-/seller-register/pvt/sellers/-sellerId-)

### Sales Channel Mapping  

Map your sales channels with a seller affiliate.  

`POST` [Upsert Sales Channel Mapping](https://developers.vtex.com/docs/api-reference/marketplace-apis/#put-/seller-register/pvt/sellers/-sellerId-/sales-channel/mapping)

`GET` [Get Sales Channel Mapping](https://developers.vtex.com/docs/api-reference/marketplace-apis/#get-/seller-register/pvt/sellers/-sellerId-/sales-channel/mapping)
