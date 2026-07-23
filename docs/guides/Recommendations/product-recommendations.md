---
title: "Product recommendations"
slug: "product-recommendations"
hidden: false
excerpt: "VTEX Product Recommendations (beta): strategies, data prerequisites for model training, implementation paths by storefront, and frequently asked questions."
createdAt: "2026-05-12T12:00:00.000Z"
updatedAt: "2026-05-12T18:00:00.000Z"
seeAlso:
  - "/docs/guides/integrating-product-recommendations-in-headless-or-faststore-web-stores"
  - "/docs/guides/integrating-product-recommendations-in-mobile-stores"
  - "/docs/apps/vtex.recommendation-shelf"
hidePaginationPrevious: false
hidePaginationNext: false
---

> ℹ️ Product Recommendations is in closed beta and available only to selected clients. If you are a VTEX client and want to adopt it, contact [Commercial Support](https://help.vtex.com/docs/tracks/commercial-support). Additional fees may apply. For a product-focused introduction, see the Help Center tutorial [Product Recommendations (beta)](https://help.vtex.com/en/docs/tutorials/product-recommendations-beta).

Product Recommendations let your store surface relevant products through multiple strategies (for example, similar items, cross-sell, or personalized shelves). They can improve discovery, conversion, and average order value.

This page is the entry point for developers: it summarizes prerequisites to train models, lists strategies, points to implementation guides by storefront model, and includes frequently asked questions.

## Prerequisites

### Store architecture

You need a storefront implemented with one of the following:

* [Store Framework](https://developers.vtex.com/docs/guides/store-framework)
* [FastStore](https://developers.vtex.com/docs/guides/faststore)
* A [headless](https://developers.vtex.com/docs/guides/headless-commerce) storefront that can load scripts and call VTEX APIs
* A mobile app capable of making authenticated HTTPS requests

### Activation and onboarding

Request activation and the strategies you want enabled through [Commercial Support](https://help.vtex.com/docs/tracks/commercial-support). After approval, VTEX typically prepares your account by creating a recommendations workspace, syncing the catalog with the recommendation service, and issuing API access where needed.

### Collecting data and training models

Recommendation quality depends on catalog quality, tracked shopper behavior, and, for some strategies, order volume. Before models are trained and campaigns go live, your integration should:

* All storefronts must have cart and order event capture configured. Store Framework handles click/view events through the `vtex.recommendation-shelf` app. For other events in Store Framework, or all events in FastStore, headless, and mobile, configure [Activity Flow](https://developers.vtex.com/docs/guides/activity-flow) as described in the implementation guides.
* FastStore, headless, and mobile must also call the [Start session](https://developers.vtex.com/docs/api-reference/recommendations-bff-api#post-/api/recommend-bff/v2/users/start-session) endpoint to link browsing behavior to completed purchases.
* All channels should send the product view events expected by the recommendation service so models can learn from real traffic.

Some strategies need minimum purchase history and product views so joint purchase patterns can be learned. Until those thresholds are met, VTEX may not train that strategy to full quality. See [Recommendation strategies](#recommendation-strategies) and [FAQ](#faq).

## Recommendation strategies

The exact set of strategies enabled for your account is agreed during onboarding. Some strategies require enough sales or behavioral history before models perform well. Until then, rely on strategies that do not depend on those signals or tune shelves with your VTEX contact.

| Strategy | How it works | Data requirements | Typical placement |
| :---- | :---- | :---- | :---- |
| Best sellers | Highlights top-performing products by sales volume | None | Home, category, search |
| Recommended for you | Personalizes picks based on individual browsing and purchase history. For shoppers with no item page visit events or completed transactions, recommendations are generated based on the first items clicked in the last 90 days by other first-time visitors (see [FAQ](#faq)) | At least 1,000 unique profiles who visited a product page more than once. At least 10,000 of one of the following: product.view events or transaction.charge events. | Home, category, search, PDP, cart, checkout, post-purchase |
| Similar products | Matches items by catalog attributes such as category, brand, and specifications | Complete and consistent catalog attributes | PDP |
| Frequently bought together | Surfaces items commonly purchased alongside the reference product | At least 1,000 transactions with more than one item in the cart | PDP, cart |
| Recently viewed | Shows the shopper's last-seen items based on view and interaction events | View and interaction event tracking | Home, category, search, PDP, cart, checkout, post-purchase |
| Visually similar products | Matches items by visual similarity using image recognition | Visual model enabled for the account | PDP |
| Manual collection | Displays a merchant-defined set of products from a collection or rules | None | Any |

For FastStore, headless, and mobile implementations, campaign identifiers and API usage (including BFF campaign types such as `rec-persona-v2`, `rec-cross-v2`, and others) are documented in [Integrating product recommendations in headless or FastStore web stores](https://developers.vtex.com/docs/guides/integrating-product-recommendations-in-headless-or-faststore-web-stores) and the [Recommendations BFF API](https://developers.vtex.com/docs/api-reference/recommendations-bff-api) reference. Store Framework uses the app and block model described in the `vtex.recommendation-shelf` guide.

## Implementation by storefront

Choose the guide that matches how your storefront is built:

| Storefront | Developer guide |
| :---- | :---- |
| Store Framework | [Product Recommendation shelf (`vtex.recommendation-shelf`)](https://developers.vtex.com/docs/apps/vtex.recommendation-shelf): blocks, props, and Intelligent Search pixel prerequisites for tracking. |
| FastStore / Headless | [Integrating product recommendations in headless or FastStore web stores](https://developers.vtex.com/docs/guides/integrating-product-recommendations-in-headless-or-faststore-web-stores): session management, fetching recommendations, event tracking, and Activity Flow setup. |
| Mobile | [Integrating product recommendations in mobile stores](https://developers.vtex.com/docs/guides/integrating-product-recommendations-in-mobile-stores): session management, fetching recommendations, and manual event tracking via API. |

FastStore, headless, and mobile implementations all use the [Recommendations BFF API](https://developers.vtex.com/docs/api-reference/recommendations-bff-api). Store Framework uses the app and block model and does not call the BFF API directly.

## FAQ

### Can I implement only one strategy?

Yes. You request the strategies you want during activation. VTEX enables and trains what is agreed for your account.

### How long does it take before models are ready?

It depends on the strategy. Strategies that do not rely on model training, such as Best sellers, Recently viewed, and Manual collection, are available as soon as the integration is configured. Strategies that require training become available once the minimum data thresholds are met: Recommended for you requires at least 1,000 unique profiles with repeat product page visits and at least 10,000 product view or purchase events, and Frequently bought together requires at least 1,000 transactions with more than one item in the cart. Beyond those thresholds, time to readiness also depends on catalog size and overall traffic volume. Your onboarding team can give more accurate timelines for your store.

### What data is collected for training?

Typically includes navigation and product interaction events used to learn views, affinity, and personalization signals, plus order data when identifiers link a session to a completed purchase. Your integration guide lists the events you should send explicitly.

### What happens to co-purchase strategies when the store does not have enough order volume?

Strategies that rely on co-purchase patterns, such as Frequently bought together, require a minimum of 1,000 transactions with more than one item in the cart. Until that threshold is reached, the strategy remains inactive. Once the volume is met, VTEX trains the model and activates the strategy. Until then, consider relying on strategies that do not depend on co-purchase data, such as Best sellers or Similar products.

### What happens to "Recommended for you" when there is not enough data?

Recommended for you depends on a personalization model trained from real shopper and purchase behavior. When a shopper has no item page visit events or completed transactions, recommendations are generated based on the first items clicked in the last 90 days by other first-time visitors in the store. As the shopper builds a history, recommendations gradually shift to reflect their individual behavior.

Until there is enough account-level history for VTEX to train and enable the model, the campaign does not behave as fully personalized. What shoppers see in the meantime is configured as part of onboarding (for example, emphasizing other strategies such as Best sellers, hiding the shelf, or using a transitional setup). Confirm the exact behavior with your VTEX contact so your UI matches expectations.

### Where do I get campaign IDs (VRNs) for API calls?

Campaign VRNs follow the format `vrn:recommendations:{store-name}:{campaignType}:{campaignId}`. You can retrieve the full VRN from the store Admin under **Storefront > Recommendations**: in the shelf list, click the three dots next to the shelf and select **Copy ID**. You can also request it through [VTEX Support](https://help.vtex.com/en/support). For the list of available campaign types, see [Integrating product recommendations in headless or FastStore web stores](https://developers.vtex.com/docs/guides/integrating-product-recommendations-in-headless-or-faststore-web-stores) or [Integrating product recommendations in mobile stores](https://developers.vtex.com/docs/guides/integrating-product-recommendations-in-mobile-stores).

### Who do I contact if recommendations are empty or look wrong?

Open a ticket with [VTEX Support](https://help.vtex.com/en/support) with examples (page, strategy, time). Wrong or sparse results are often tied to catalog structure, missing events, or a strategy that is still gathering training data.
