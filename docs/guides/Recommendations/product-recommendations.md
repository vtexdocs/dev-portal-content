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
  - "/docs/guides/vtex-recommendation-shelf"
hidePaginationPrevious: false
hidePaginationNext: false
---

> ℹ️ Product Recommendations is in **closed beta** and available only to selected clients. If you are a VTEX client and want to adopt it, contact [Commercial Support](https://help.vtex.com/docs/tracks/commercial-support). Additional fees may apply. For a product-focused introduction, see the Help Center tutorial [Product Recommendations (beta)](https://help.vtex.com/en/docs/tutorials/product-recommendations-beta).

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

Request activation and the strategies you want enabled through [Commercial Support](https://help.vtex.com/docs/tracks/commercial-support). After approval, VTEX typically prepares your account by creating a recommendations workspace, syncing the catalog with the recommendation service, issuing API access where needed, and providing any integration script used for tracking.

### Prerequisites for collecting data and training models

Recommendation quality depends on **catalog quality**, **tracked shopper behavior**, and, for some strategies, **order volume**. Before models are trained and campaigns go live, your integration should:

* Run the integration script on the pages where you want recommendations or behavioral signals, as provided during onboarding.
* Persist the shopper identifier used for recommendations (including `_snrs_uuid` in the order form where applicable) so purchases can be tied to browsing behavior. Details are in the implementation guides below.
* Send the **events** expected for your channel (for example, product views on channels that do not auto-track them), so the service can learn from real traffic.

For **FastStore** specifically, [Intelligent Search](https://help.vtex.com/docs/tracks/installing-intelligent-search) must be installed and integrated with the catalog before you implement recommendations, as described in [Integrating product recommendations in headless or FastStore web stores](https://developers.vtex.com/docs/guides/integrating-product-recommendations-in-headless-or-faststore-web-stores).

Some strategies need **minimum purchase history** so joint purchase patterns can be learned. Until those thresholds are met, VTEX may not train that strategy to full quality; see [Recommendation strategies](#recommendation-strategies) and [FAQ](#faq).

## Recommendation strategies

The exact set enabled for your account is agreed during onboarding. The sections below describe how each strategy behaves, what usually drives results, typical **page placement** (merchandising), and **training or data** notes. Some types need enough sales or behavior history before models perform well; until then, tune shelves with your VTEX contact or rely on strategies that do not depend on those signals.

### How each strategy works

| Strategy | What shoppers see | How it works (summary) |
| -------- | ----------------- | ---------------------- |
| **Most popular** | Widely viewed products in the store | Surfaces items with strong **view** activity so new or anonymous sessions still get relevant trending products. |
| **Recommended for you** | Items tuned to this shopper | Uses **individual behavior** (clicks, views, purchases). When the user is new or the model is not ready yet, behavior may fall back to a **general “top picks”** style result until personalization is available—confirm fallback with your VTEX contact (see [FAQ](#faq)). |
| **Similar products** | Alternatives like the reference product | Matches using **catalog attributes** (for example name, description, **category**, **brand**, and specifications) for the product in context (often PDP). |
| **Frequently bought together (cross-sell)** | Complements in the same journey | Highlights items that appear together in **transactions** or carts with the reference product (classic **cross-sell**). Quality depends on enough multi-item **purchase** history. |
| **Best sellers** | Store-wide top performers by sales | Emphasizes **best-selling** or high-momentum products across the catalog (store-wide popularity by **sales**, not only views). |
| **Recently viewed** | The shopper’s last-seen items | Driven by **this shopper’s recent views** (and, where tracked, cart adds). Requires reliable **view and interaction events** in your channel. |
| **Recent interactions** | Likely next picks from behavior | Uses **recent interaction** signals (views, cart, and similar) to surface products the shopper is **more likely to engage with next**—useful for continuing the session across pages. |
| **Visually similar products** | Look-alikes from product imagery | Uses **image** features (color, shape, pattern) rather than text attributes alone; needs **quality images** and the strategy enabled for your account. |
| **Manual collection** | A fixed set you define | **Merchant-defined**: products from a **collection** or rules you maintain—does not depend on model training. |

### Signal mix (what each type leans on)

This table is a shorthand for implementation and catalog work. It is not an exhaustive API matrix.

| Strategy | Shopper behavior (views, clicks, orders) | Catalog attributes (category, specs, brand, …) | Co-purchase / multi-item carts | Broad popularity (views or sales) | You define the assortment |
| -------- | :----------------------------------------: | :----------------------------------------------: | :------------------------------: | :-------------------------------: | :-------------------------: |
| **Most popular** | ✓ | | | ✓ (views) | |
| **Recommended for you** | ✓ | ✓ | ✓ | ✓ | |
| **Similar products** | | ✓ | | | |
| **Frequently bought together (cross-sell)** | | | ✓ | | |
| **Best sellers** | | | | ✓ (sales) | |
| **Recently viewed** | ✓ | | | | |
| **Recent interactions** | ✓ | | | | |
| **Visually similar products** | | ✓ (via images) | | | |
| **Manual collection** | | | | | ✓ |

### Typical placement by store page

Use this when deciding where to render each shelf. Your final placement is agreed with VTEX and may vary by theme.

| Strategy | Home | Category / brand | Search | Product (PDP) | Cart | Checkout | Post-purchase¹ |
| -------- | :--: | :--------------: | :----: | :-----------: | :--: | :------: | :------------: |
| **Most popular** | ✓ | ✓ | ✓ | | | | |
| **Recommended for you** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Similar products** | | | | ✓ | | | |
| **Frequently bought together (cross-sell)** | | | | ✓ | ✓ | | |
| **Best sellers** | ✓ | ✓ | ✓ | | | | |
| **Recently viewed** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Recent interactions** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Visually similar products** | | | | ✓ | | | |
| **Manual collection** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

¹ **Post-purchase** means pages such as **order confirmation** or **thank you**, where you still have a session or order context.

### Training and data quality

| Strategy | Notes for training and quality |
| -------- | ------------------------------ |
| **Most popular** | Less dependent on large **co-purchase** datasets than collaborative strategies; still needs reliable **view** tracking. |
| **Recommended for you** | Typically needs a meaningful volume of **purchases that include more than one line item** (often on the order of **1,000** such orders) so joint patterns can be learned. |
| **Similar products** | Quality follows **catalog** consistency—categories, attributes, and specs should be complete and uniform. |
| **Frequently bought together (cross-sell)** | Similar data appetite to collaborative models—enough **multi-item carts and purchases** (commonly on the order of **1,000** qualifying purchases). |
| **Best sellers** | Depends on **sales** signals visible to the recommendation service. |
| **Recently viewed** | Needs **view** (and optional cart) **events** on every channel where the shelf appears. |
| **Recent interactions** | Needs **ongoing interaction** data and correct **user/session** linkage. |
| **Visually similar products** | Depends on **images** and the visual model being enabled for your account. |
| **Manual collection** | No model training loop—quality is entirely your **collection** curation. |

Campaign identifiers and API usage (including BFF campaign types such as `rec-persona-v2`, `rec-cross-v2`, and others) are documented in [Integrating product recommendations in headless or FastStore web stores](https://developers.vtex.com/docs/guides/integrating-product-recommendations-in-headless-or-faststore-web-stores) and the [Recommendations BFF API](https://developers.vtex.com/docs/api-reference/recommendations-bff-api) reference.

## Implementation by storefront

Choose the guide that matches how your storefront is built:

| Storefront | Developer guide |
| ---------- | ----------------- |
| **Store Framework** | [Product Recommendation shelf (`vtex.recommendation-shelf`)](https://developers.vtex.com/docs/guides/vtex-recommendation-shelf): blocks, props, and Biggy pixel prerequisites for tracking. |
| **FastStore / Headless** | [Integrating product recommendations in headless or FastStore web stores](https://developers.vtex.com/docs/guides/integrating-product-recommendations-in-headless-or-faststore-web-stores): session management, fetching recommendations, event tracking, and Activity Flow setup. |
| **Mobile** | [Integrating product recommendations in mobile stores](https://developers.vtex.com/docs/guides/integrating-product-recommendations-in-mobile-stores): session management, fetching recommendations, and manual event tracking via API. |

All API-based flows rely on the **[Recommendations BFF API](https://developers.vtex.com/docs/api-reference/recommendations-bff-api)**.

## FAQ

### What happens to “Recommended for you” when there is not enough data to train yet?

**Recommended for you** depends on a personalization model trained from real shopper and purchase behavior. Until there is enough history for VTEX to train and enable that model for your account, that **campaign does not behave as fully personalized** yet. What shoppers see in the meantime is **configured as part of onboarding** (for example, emphasizing other strategies such as **Most popular** or **Best sellers**, hiding the shelf, or using a transitional setup). Confirm the exact behavior with your VTEX contact so your UI matches expectations.

### How long does it take before models are ready?

It varies by traffic, catalog size, and which strategies you enabled. Implementation guides describe training as happening **after enough browsing and order data** has been collected; your support or onboarding team gives concrete timelines for your store.

### Do I need Intelligent Search for every storefront?

**FastStore** implementations require Intelligent Search and catalog integration, as documented in [Integrating product recommendations in headless or FastStore web stores](https://developers.vtex.com/docs/guides/integrating-product-recommendations-in-headless-or-faststore-web-stores). Requirements for Store Framework or mobile may differ; follow the guide for your stack and what onboarding specifies.

### What is the difference between “Similar products” and “Frequently bought together”?

**Similar products** is mainly about **catalog similarity** (category and attributes). **Frequently bought together** is about **co-purchase patterns** in orders. They answer different merchandising goals and have different data needs.

### Does the Store Framework shelf call the same APIs as FastStore and headless?

Conceptually the **same recommendation service** backs these experiences, but Store Framework uses the **app and pixel** integration model, while FastStore and headless guides focus on **scripts plus Recommendations BFF**. Use the guide for your architecture.

### What data is collected for training?

Typically includes **navigation and product interaction** events used to learn views, affinity, and personalization signals, plus **order** data when identifiers link a session to a completed purchase. Your integration guide lists the events you should send explicitly.

### Can I implement only one strategy?

Yes. You request the strategies you want during activation; VTEX enables and trains what is agreed for your account.

### Where do I get campaign IDs (VRNs) for API calls?

Campaign identifiers are part of onboarding. The FastStore guide explains the **VRN** pattern and example **campaign types**; your VTEX contact supplies the **campaign IDs** applicable to your store.

### Who do I contact if recommendations are empty or look wrong?

Open a ticket with **[VTEX Support](https://help.vtex.com/en/support)** with examples (page, strategy, time). Wrong or sparse results are often tied to **catalog structure**, **missing events**, or a strategy that is **still gathering training data**.

## Next steps

* [Integrating product recommendations in headless or FastStore web stores](https://developers.vtex.com/docs/guides/integrating-product-recommendations-in-headless-or-faststore-web-stores)
* [Integrating product recommendations in mobile stores](https://developers.vtex.com/docs/guides/integrating-product-recommendations-in-mobile-stores)
* [Product Recommendation shelf (Store Framework)](https://developers.vtex.com/docs/guides/vtex-recommendation-shelf)
* [Recommendations BFF API](https://developers.vtex.com/docs/api-reference/recommendations-bff-api)
