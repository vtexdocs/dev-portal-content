---
slug: "new-price-simulations-api"
title: "New Price Simulations API"
createdAt: 2020-09-03T23:21:09.762Z
hidden: false
type: "added"
---

<span class="badge" id="price-simulations-api">Price Simulations API</span>

The Price Simulations API allows you to configure custom price selectors for B2B stores, based on the context set by the [Orders Configuration app](https://vtex.io/docs/components/content-blocks/vtex.order-configuration/readme/). It contains the following endpoints:

<span class="api pg-type type-get">get</span> [Get custom prices schema](ref:get_-v-custom-prices-session-schema)
<span class="api pg-type type-post">post</span> [Create or Update custom prices schema](ref:post_-v-custom-prices-session-schema)
<span class="api pg-type type-post">post</span> [Update Order Configuration](ref:post_sessions)
<span class="api pg-type type-get">get</span> [Get price association by ID](ref:get_-v-custom-prices-rules-priceassociationid)
<span class="api pg-type type-post">post</span> [Create price association](ref:post_-v-custom-prices-rules)
<span class="api pg-type type-put">put</span> [Update price association by ID](ref:put_-v-custom-prices-rules-priceassociationid)
<span class="api pg-type type-delete">delete</span> [Disassociate price association by ID](ref:delete_-v-custom-prices-rules-priceassociationid)
