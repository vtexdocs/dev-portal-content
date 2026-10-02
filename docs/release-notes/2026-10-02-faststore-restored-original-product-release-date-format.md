---
title: "FastStore: Restored the original product release date format"
slug: "2026-10-02-faststore-restored-original-product-release-date-format"
type: "fixed"
excerpt: "FastStore now returns the original product release date to storefront customizations while keeping PDP structured data compatible with Schema.org."
createdAt: "2026-10-02T00:00:00.000Z"
tags:
  - FastStore
---

FastStore now returns `StoreProduct.releaseDate` in the original format provided by [Intelligent Search](https://help.vtex.com/en/docs/tutorials/intelligent-search-overview). This restores compatibility with storefront customizations that consume the field directly while keeping product structured data valid for search engines.

## What has changed?

In FastStore versions `v4.7.0` through `v4.8.x`, the API resolver converted `StoreProduct.releaseDate` to an ISO 8601 calendar date. This conversion was introduced to make the product detail page (PDP) JSON-LD compatible with Schema.org, but it also changed the value returned to every GraphQL consumer. As a result, customizations that expected the original epoch value could stop working.

Now, `StoreProduct.releaseDate` is returned without modification, as provided by Intelligent Search. ISO 8601 normalization is applied only when FastStore builds the product JSON-LD on PDPs. Therefore:

- Storefront customizations receive the original catalog value.
- Release dates in PDP JSON-LD structured data are normalized to ISO 8601 for Schema.org compatibility.
- Missing release dates continue to return an empty string.

## Why did we make this change?

Only the PDP structured data requires an ISO 8601 date. Applying the conversion in the API resolver changed the field for all consumers, including custom storefront code that relied on its original format.

Moving the conversion to the JSON-LD generation keeps product metadata compatible with search engines without changing the value consumed by storefront customizations.

## What needs to be done?

Follow the instructions in [Updating the CLI package version](https://developers.vtex.com/docs/guides/faststore/developer-tools-updating-the-cli-package-version) to upgrade to FastStore `v4.9.1`.

If you changed a customization in `v4.7.0` or `v4.8.x` to expect an ISO 8601 date, update it to parse and validate the original value returned by the catalog. Do not assume a specific format, because the field may contain an epoch timestamp, another string format, or an empty string.

No additional configuration is required for stores that don't consume `StoreProduct.releaseDate` directly.
