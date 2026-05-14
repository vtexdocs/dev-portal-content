---
title: "Intelligent Search: Negative filters (NOT operator)"
slug: "2026-04-22-intelligent-search-negative-filters-not-operator"
hidden: false
type: "added"
createdAt: "2026-04-22T20:30:00.000Z"
excerpt: "VTEX Intelligent Search now supports negative filters in the facets path using the not: prefix so that you can exclude facet values from results."
---

[VTEX Intelligent Search](https://developers.vtex.com/docs/api-reference/intelligent-search-api) now supports **negative filters** in the `facets` path: you can exclude a specific facet value by prefixing it with `not:` in the value segment of the URL.

## What has changed?

When building the `facets` segment (for example, on [`GET /product_search/{facets}`](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/product_search/-facets-)), you can exclude a value using the pattern `/{facetKey}/not:{facetValue}/`. For example, `color/blue/size/not:42` keeps products that match `color/blue` and removes those that match size `42`.

Existing behavior for combining filters remains unchanged: multiple values of the same facet type are combined with **OR**, and values of different facet types are combined with **AND**. The NOT operator applies to that model to exclude a given facet value.

## Why did we make this change?

Negative filters enable richer merchandising and navigation scenarios, for example, showing products in one collection while excluding another.

## What needs to be done?

No change is required for existing integrations. URLs that don't use `not:` behave as before.

To adopt negative filters, include `not:` in the appropriate facet value when constructing the `facets` path. See the `facets` parameter description in the [Intelligent Search API reference](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/product_search/-facets-) for syntax details and examples.
