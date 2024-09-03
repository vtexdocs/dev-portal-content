---
title: "Best practices for associating a custom page with a content type"
slug: "vtex-io-documentation-best-practices-for-associating-a-custom-page-with-a-content-type"
hidden: false
createdAt: "2024-07-25T19:50:31.469Z"
updatedAt: "2024-08-30T17:48:35.094Z"
excerpt: "Configure URLs effectively when associating custom pages with content types."
---

[Custom landing pages](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-new-custom-page) are usually associated with specific store URLs. However, in some situations, it is helpful to associate a page template with a **content type** instead. Content types indicate the purpose of a page, such as Product Listing Pages (PLPs) and Product Detail Pages (PDPs).

Creating your own content types can simplify website content management. For example, you can create a content type named "Store Finder" for the web pages that display the cities where your store is located. To associate the assets of these pages with the Store Finder content type, you must set an ID value for Store Finder and use it as a variable in your route paths.

Follow the guidelines below to manage your website content more efficiently and ensure that your assets remain correctly associated with them, even when URLs change.

## Before you begin

Ensure you have created a new page following the guide [Creating a new custom page](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-new-custom-page).

## URL guidelines

To associate a custom landing page with a content type, note the following when creating your URL:

### Setting up content type parameters

- Any URL parameter named `{entity}_id` is identified as a content type. For example, `finder_id` creates the `${finder}` content type.

  > ⚠️ For the URL definition, adding the content type identifier is not enough. You must also attach `_id` next to it. For example, if you create a URL like `/store/:category`, the content will be tied to that URL since there is no parameter that can be interpreted as a content type. Thus, if you access _Storefront > Site Editor_ and update the content for `/store/bakery`, the content related to any page matching `/store/:category` will also be updated.

- The page URL can have only one parameter to indicate a content type.
- The page URL can have only one parameter ending with `_id`.
- Any additional variable parameters in the URL are ignored when matching content. For example, if you create the route `/store/:category/:{entity}_id`, the same content will be delivered for `/store/bakery/1` and `/store/beverages/1` as they both relate to the `{$entity}` content type.

### Handling URL changes

If you change your URL, the assets will remain associated with the content type, not the specific URL.

For example, if you create a page with the URL `/store/:store_id`, where `store_id` represents the `${store}` content type, and later change it to `/store-finder/:store_id`, the assets will still be accessible at the new URL, as both URLs relate to the `${store}` content type.

### Dos and Don'ts

| ✅ Do |  Explanation |
| - | - |
| `/store/:{entity}_id` | The URL uses a content type parameter (ending with `_id`), allowing the system to identify the content type. For example: If `{entity}` is a finder, this URL would link to the `${finder}` content type. |

| ❌ Don'ts | Explanation |
| - | - |
| `/store/:{entity}`| The URL is wrong because it lacks the required `_id` suffix. Without `_id`, the system cannot identify it as a content type, which means no assets will be associated with this URL. |
| `/store/:category/:{entity}_id`| While this URL includes a valid content type parameter, additional variable parameters (like `:category`) are ignored when determining content association. This can lead to unexpected content being delivered. |
| `/store/:{entity}_id/{entity2}_id`| The URL is not allowed because it has two parameters ending with `_id`. To maintain clarity in the content association, a URL can only have one content type parameter ending with `_id`. |
