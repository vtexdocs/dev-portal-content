---
title: "Marketplace"
slug: "marketplace-overview"
hidden: false
createdAt: "{Creation date as 2022-10-20T17:08:52.219Z}"
updatedAt: "{Update dates as 2022-10-21T14:33:45.242Z}"
excerpt: "{Insert a synopsis of your article here}"
hidePaginationPrevious: false
hidePaginationNext: false
---
# Marketplace

>ℹ️ Help us improve our documentation! Tell us about your experience with this article by filling out [this form](https://forms.gle/fQoELRA1yfKDqmAb8).

We define marketplace as the environment where sellers expose their products and also where consumers make purchases and pay for an order. Sellers in turn are commonly the owners of the products and responsible for delivery the products to consumers. VTEX promotes digital collaboration in different settings. In addition to selling their products in other marketplaces, sellers can become marketplaces themselves. Learn more about partners and growth opportunities in [Marketplace Strategies at VTEX](https://help.vtex.com/en/tutorial/estrategias-de-marketplace-na-vtex--tutorials_402).

## Understanding the marketplace architecture

The architecture of a VTEX store allows them to become marketplaces or sellers in other VTEX stores without the need for any additional development, that is, every VTEX store is a seller in its own marketplace environment and can also be a seller in other environments from marketplaces, VTEX (native marketplaces) or external (certified marketplaces or partners).

![VTEX<>VTEX Integration](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Getting-Started/quick-start-guide-marketplace-integracao-vtex-vtex.jpg)

- **VTEX Marketplace:** Store environment hosted on the VTEX platform responsible for product sales, checkout, and payment.
- **External Marketplace:** Showcase store hosted on platforms external to VTEX and responsible for product sales, checkout, and payment.
- **VTEX Seller**: Is a store hosted on the VTEX platform that owns the products and is usually responsible for delivery to the consumer.
- **External Seller:** Is a store hosted on another platform, or that is not yet hosted on any platform, and which owns the products and is usually responsible for delivery to the consumer. A VTEX marketplace is interested in integrating with this external store, in order to offer its products in its showcase.

## Configuring VTEX Marketplace

To operate as a marketplace, it is necessary to configure your store according to the steps described in [Configuring VTEX Marketplace](https://help.vtex.com/en/tutorial/configuring-vtex-marketplace--7splyp5MqIyt2Iyz5jsNzb).

The actions that can be performed via API are the following:

- [Adding seller](#Adding-Sellers)
- [Configuring seller selection at checkout](https://developers.vtex.com/docs/guides/checkout-overview)
- [Configure storefront](https://developers.vtex.com/docs/guides/getting-started-3)
- [Configure payments](https://developers.vtex.com/docs/guides/payments-integration-guide)

## Integrating External Marketplaces or External Sellers

The Marketplace Protocol is a set of API requests and definitions to help you integrate external sellers into a VTEX marketplace, as well as external marketplaces into VTEX sellers.

- **External seller protocol:** If you are a VTEX marketplace and want to integrate offers from an external seller into your catalog, see our [External Seller Integration Guide](https://developers.vtex.com/docs/guides/external-seller-integration-guide).
- **External marketplace protocol:** If you are an external marketplace that wants to integrate with a VTEX seller, see [External Marketplace Integration Guide](https://developers.vtex.com/docs/guides/external-marketplace-integration-guide) to learn how to develop a custom connector to integrate with the architecture and catalog of VTEX sellers.

## <a name="Adding-Sellers"></a>1. Marketplace: Adding Sellers

VTEX marketplaces that want to make products from sellers available in their store, it will be necessary to perform some processes. The first step is to find out if the seller you want to connect to is a VTEX seller or an external seller. For external sellers, verify the [External Seller Integration Guide](https://developers.vtex.com/docs/guides/external-seller-integration-guide) and for VTEX sellers, follow the steps below.

### Adding a seller for the Seller Portal

The [Seller Portal](https://help.vtex.com/en/tutorial/seller-portal-primeiros-passos-para-o-marketplace--6ccErY3mCcfoW0qGXf167) is an edition of the VTEX platform with essential functionalities available, so that external or VTEX sellers can quickly integrate into VTEX marketplaces. The Seller Portal has default version developed by VTEX and if the marketplace wants its own customized version, it can develop from the VTEX version following the [Seller Portal Edition App](https://developers.vtex.com/docs/guides/seller-portal-edition-app) guide.

To integrate a partner's products to your marketplace using the Seller Portal as a solution, there is a flow of actions to be performed by marketplace and seller, see the image below.

![Seller_Portal_Steps_Integration](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Getting-Started/quick-start-guide-marketplace-seller-portal-steps.png)

The marketplace is responsible for onboarding new sellers. In other words, it is the role of the marketplace to support the seller's experience in the Seller Portal. For information about seller actions, see [Seller Portal: First Steps for the Seller](https://help.vtex.com/en/tutorial/seller-portal-primeiros-passos--6w1vBdRH2uuBGmUqgNQjwK).

To perform the actions of invite seller and activate seller, the marketplace must follow the endpoints listed below in the order represented (1,2 and 3), for the action of approving offers, see the section [Cataloging offers](#Cataloging-offers).

   1. POST - [Invite Seller Lead](https://developers.vtex.com/docs/api-reference/marketplace-apis#post-/seller-register/pvt/seller-leads)  
   2. PUT - [Accept Seller Lead](https://developers.vtex.com/docs/api-reference/marketplace-apis#put-/seller-register/pvt/seller-leads/-sellerLeadId-)  
   3. PUT - [Create Seller from Lead](https://developers.vtex.com/docs/api-reference/marketplace-apis/#put-/seller-register/pvt/seller-leads/-sellerLeadId-/seller)  

In the same category of Seller invite, you will also find the endpoints:

- GET - [List Seller Leads](https://developers.vtex.com/docs/api-reference/marketplace-apis#get-/seller-register/pvt/seller-leads): Returns a list of all sellers that have been invited by the marketplace.
- GET - [Get Seller Lead's Data by Id](https://developers.vtex.com/docs/api-reference/marketplace-apis#get-/seller-register/pvt/seller-leads/-sellerLeadId-): Marketplace gets a list of the sellers invitated to its own environment.
- PUT - [Resend Seller Lead Invite](https://developers.vtex.com/docs/api-reference/marketplace-apis#put-/seller-register/pvt/seller-leads/-sellerLeadId-/status): Marketplace resends the invitation to the desired seller.
- DELETE - [Delete Seller Lead](https://developers.vtex.com/docs/api-reference/marketplace-apis#delete-/seller-register/pvt/seller-leads/-sellerLeadId-): Allows the marketplace to delete a seller previously invited to its environment, if the seller has not yet accepted the invitation.

### Adding and configuring a seller's account to VTEX Commerce

To add and configure a registered seller account and update accounts that are not hosted on the Seller Portal, the marketplace will use the following endpoints.

- POST - [Configure Seller Account](https://developers.vtex.com/docs/api-reference/marketplace-apis#post-/seller-register/pvt/sellers): Configure a specific seller's account.
- PATCH - [Update Seller by Seller ID](https://developers.vtex.com/docs/api-reference/marketplace-apis#patch-/seller-register/pvt/sellers/-sellerId-) for when the marketplace needs to make updates to the settings of a specific seller.
- PUT - [Upsert Sales Channel Mapping](https://developers.vtex.com/docs/api-reference/marketplace-apis/#put-/seller-register/pvt/sellers/-sellerId-/sales-channel/mapping) when the seller has two affiliates pointing to the same marketplace, the account settings will be done through this endpoint.

After configuring the account, the marketplace will be able to verify the settings made.

- GET - [List Sellers](https://developers.vtex.com/docs/api-reference/marketplace-apis#get-/seller-register/pvt/sellers): Retrieve a list of sellers registered in the marketplace, and this list can be filtered by the configured [trade policy](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV#master-data).
- GET - [Get Seller data by ID](https://developers.vtex.com/docs/api-reference/marketplace-apis#get-/seller-register/pvt/sellers/-sellerId-): Retrieve information on a specific seller, it is also possible to filter by commercial policy.
- GET - [Get Sales Channel Mapping Data](https://developers.vtex.com/docs/api-reference/marketplace-apis/#get-/seller-register/pvt/sellers/-sellerId-/sales-channel/mapping): Retrieve information about mapping between your sales channels and a specific seller.

### Configuring seller's commission

The marketplace will configure the seller's commissions after the initial configurations. To perform this action, one of the following endpoints can be used.

- PUT - [Upsert Seller Commissions in Bulk](https://developers.vtex.com/docs/api-reference/marketplace-apis#put-/seller-register/pvt/sellers/-sellerId-/commissions/categories): To apply the same commission rule to all categories of a seller already registered in the marketplace.
- PUT - [Upsert Seller Commissions by Category ID](https://developers.vtex.com/docs/api-reference/marketplace-apis#put-/seller-register/pvt/sellers/-sellerId-/commissions/-categoryId-): To apply a commission rule to only one category of the respective seller.

The query and management of applied commission rules will be performed through the following endpoints.

- GET - [List Seller Commissions by seller ID](https://developers.vtex.com/docs/api-reference/marketplace-apis/#get-/seller-register/pvt/sellers/-sellerId-/commissions): Retrieve the list of commissions defined for a seller.
- GET- [Get Seller Commissions by Category ID](https://developers.vtex.com/docs/api-reference/marketplace-apis/#get-/seller-register/pvt/sellers/-sellerId-/commissions/-categoryId-): Retrieve the commission list defined for a specific category of a specific seller.
- DELETE - [Remove Seller Commission by Category ID](https://developers.vtex.com/docs/api-reference/marketplace-apis#delete-/seller-register/pvt/sellers/-sellerId-/commissions/-categoryId-): Removes a previously defined commission for a category of a seller.

When completing the steps listed above, the marketplace will have completed the integration of a seller into its store.

## 2. Suggestions

When the seller is integrated into a store, he will begin to suggest products from his catalog to the marketplace. The APIs mentioned in this section refer to the Received SKUs page of Admin VTEX.

### Sellers: Sending Suggestions

When the seller wants to suggest that one of their SKUs be sold on the marketplace, we say that the seller is sending a suggestion.  
Before sending suggestions, the seller can check if the SKU already exists in the marketplace. If it does not exist, the **Get SKU bindings by SKU ID** call should be made after sending the suggestion to notify the marketplace that the SKU in question is a new suggestion.

- GET - [Get SKU Bindings by SKU ID](https://developers.vtex.com/docs/api-reference/sku-bindings-api#get-/catalog/pvt/skusellers/-skuId-)
- PUT - [Send SKU Suggestion](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#put-/suggestions/-sellerId-/-sellerSkuId-)

### Marketplace: Deleting Suggestions

If the marketplace wants to remove a submitted suggestion, they should use this call to delete the suggestion of a specific SKU.

- DELETE - [Delete SKU Suggestion](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#delete-/suggestions/-sellerId-/-sellerSkuId-)

## <a name="Cataloging-offers"></a>3. Cataloging offers

When the seller sends a product suggestion to the marketplace with configured price and inventory information, after approval by the marketplace, this suggestion becomes an offer. However, before approving a seller's suggestion, it is important to ensure that the product information sent corresponds to the business strategy of the marketplace. When cataloging offers, consider the quality of information sent by the seller, such as price, product description and image.

Cataloging can be performed [manually](https://help.vtex.com/pt/tutorial/sugerindo-e-aprovando-skus--tutorials_396#opcoes-de-catalogacao) or automatically by [VTEX matcher](https://help.vtex.com/en/tutorial/entendendo-a-pontuacao-do-vtex-matcher) and/or by external matchers. VTEX matcher is a tool used by marketplaces to analyze offers submitted by sellers and accelerate their cataloging process.

### Marketplace: Matching

When matching received SKUs, the marketplace can perform this action either in bulk or individually.

- PUT - [Match Received SKUs individually](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#put-/suggestions/-sellerId-/-sellerskuid-/versions/-version-/matches/-matchid-)
- PUT - [Match Multiple Received SKUs](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#put-/suggestions/matches/action/-actionName-)

### Marketplace: Auto Approve

Received SKUs will be approved automatically independently [Matcher score](https://help.vtex.com/en/tutorial/entendendo-a-pontuacao-do-vtex-matcher--tutorials_424).

- PUT - [Active autoApprove in the Marketplace's Account](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions/#put-/suggestions/configuration/autoapproval/toggle): Will be used by the marketplace to activate the VTEX Matcher with the default parameters for all received SKU modules, so that all sent SKUs are automatically approved.
- GET - [Get Account's Approval Settings](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#get-/suggestions/configuration): After activating the matcher, the marketplace can use this endpoint to check the current settings of automatic approval scoring in its store.
- PUT - [Save Account's Approval Settings](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#put-/suggestions/configuration):Will be used to update the matcher's approval parameters in the received SKU module.
- GET - [Get autoApprove Status in Account Settings](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#get-/suggestions/configuration/autoapproval/toggle): Can be used to check the matcher status for a specific seller.
- PUT - [Activate autoApprove Settings](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#put-/suggestions/configuration/autoapproval/toggle/seller/-sellerId-): The marketplace will use this to activate the matcher with the default parameters for a specific seller identified by sellerId.
- GET - [Get Seller's Approval Settings](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#get-/suggestions/configuration/seller/-sellerId-): To check the current automatic approval configuration for a specific seller identified by sellerId.
- PUT - [Save Seller's Approval Settings](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#put-/suggestions/configuration/seller/-sellerId-): Will be used to update the matcher's approval parameters for a specific seller identified by sellerId.

## 4. Managing Products

There are several actions that a marketplace or a VTEX seller can perform in product management. In the following sections, you will find the main actions for a marketplace and a seller.

### For Marketplaces

The following endpoints will be used by the marketplace to query information about sellers in a store.

**Suggestion**

- GET - [Get all SKU Suggestions](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#get-/suggestions): Retrieves information about all suggestions sent by a seller.
- GET - [Get SKU Suggestion by ID](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions/#get-/suggestions/-sellerId-/-sellerSkuId-): Retrieves the matcher status and score information of a specific suggestion.

**Version**

- GET - [Get all Versions](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions/#get-/suggestions/-sellerId-/-sellerskuid-/versions): Retrieves information about the versions of a suggestion sent by the seller.
- GET - [Get Version by ID](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions/#get-/suggestions/-sellerId-/-sellerskuid-/versions/-version-): Retrieves information about a specific version of the suggestion.
- GET - [Get Matched Offers List](https://developers.vtex.com/docs/api-reference/marketplace-apis/#get-/offer-manager/pvt/offers): Retrieves the available offers in the marketplace.
- GET - [Get Matched Offer's Data by SKU ID](https://developers.vtex.com/docs/api-reference/marketplace-apis/#get-/offer-manager/pvt/product/-productId-/sku/-skuId-): Retrieves the list of offers available for a specific SKU ID in the marketplace catalog.
- GET - [Get Matched Offer's Data by Product ID](https://developers.vtex.com/docs/api-reference/marketplace-apis/#get-/offer-manager/pvt/product/-productId-): Retrieves a list of all offers available for a specific product ID in the marketplace catalog.

### For Sellers

The endpoints presented will be used by sellers already connected to a marketplace to notify external marketplaces or VTEX whenever there is an update to their SKUs.

- POST - [Notify Marketplace of Price Update](https://developers.vtex.com/docs/api-reference/marketplace-apis/#post-/notificator/-sellerId-/changenotification/-skuId-/price)
- POST - [Notify Marketplace of Inventory Update](https://developers.vtex.com/docs/api-reference/marketplace-apis/#post-/notificator/-sellerId-/changenotification/-skuId-/inventory)

## 5. Sellers: Offer Management

[Offer Management](https://help.vtex.com/en/tutorial/offer-management--7MRb9S78aBdZjFGpbuffpE?&utm_source=autocomplete) is the VTEX feature that provides sellers with more visibility into the process of sending a product to external channels, such as marketplaces. Offer Management helps sellers identify updates and resolve errors in their offers during the sending process, ensuring that they can be sent to the marketplace and synchronized correctly.

Check our[ Offer Management Integration Guide](https://developers.vtex.com/docs/guides/sent-offers-integration-guide-connectors) for more details.
