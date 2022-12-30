---
title: "Price Simulations API - Overview"
slug: "price-simulations-api-overview"
hidden: false
createdAt: "2020-09-04T15:58:43.493Z"
updatedAt: "2022-08-11T20:38:08.291Z"
---
[block:callout]
{
  "type": "info",
  "body": "Check the new [Pricing onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/pricing-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Pricing and is organized by focusing on the developer's journey.",
  "title": "Onboarding guide"
}
[/block]
The Price Simulations API allows you to configure custom price selectors for B2B stores, based on the context set by the [Orders Configuration app](https://vtex.io/docs/components/content-blocks/vtex.order-configuration/readme).


[block:api-header]
{
  "title": "Index"
}
[/block]
<span class="api pg-type type-get">get</span> [Get custom prices schema](ref:get_-v-custom-prices-session-schema)
<span class="api pg-type type-post">post</span> [Create or Update custom prices schema](ref:post_-v-custom-prices-session-schema)
<span class="api pg-type type-post">post</span> [Update Order Configuration](ref:post_sessions)
<span class="api pg-type type-get">get</span> [Get price association by ID](ref:get_-v-custom-prices-rules-priceassociationid)
<span class="api pg-type type-post">post</span> [Create price association](ref:post_-v-custom-prices-rules)
<span class="api pg-type type-put">put</span> [Update price association by ID](ref:put_-v-custom-prices-rules-priceassociationid)
<span class="api pg-type type-delete">delete</span> [Disassociate price association by ID](ref:delete_-v-custom-prices-rules-priceassociationid)

[block:api-header]
{
  "title": "Custom Prices"
}
[/block]
In this session, you can create a specific shopping scenario with the criteria you want. For explaining purpose, we used the `orderType` and `state` as default values, but it can be others too.
[block:api-header]
{
  "title": "Session Management"
}
[/block]
Every time you edit a configuration value set on the Custom Prices session, you must use this endpoint to update the Order Configuration.
[block:api-header]
{
  "title": "Price Association"
}
[/block]
Use these routes to associate a shopping scenario, created at the Custom Price session, to a specific price table.