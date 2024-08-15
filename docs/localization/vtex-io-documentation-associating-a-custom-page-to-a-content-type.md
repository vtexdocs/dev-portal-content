---
title: "Best practices for associating a custom page with a content type"
slug: "vtex-io-documentation-best-practices-for-associating-a-custom-page-with-a-content-type"
hidden: false
createdAt: "2024-07-25T19:50:31.469Z"
updatedAt: "2024-08-15T15:34:39.964Z"
excerpt: "Configure URLs effectively when associating custom pages with content types."
---

[Custom landing pages](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-new-custom-page) are usually associated with specific store URLs. However, in some situations, it is helpful to associate a page template with a **content type** instead. Content types indicate the purpose of a page, such as Product Listing Pages (PLPs) and Product Detail Pages (PDPs).

Creating your own content types can simplify website content management. For example, you can create a content type named "Store Finder" for the web pages that display the cities where your store is located. To associate the assets of these pages with the Store Finder content type, you need to set up an id value for Store Finder and use it as a variable in your route paths.

Follow the guidelines below to manage your website content more efficiently and ensure that your assets remain correctly associated with them, even when URLs change.

## Before you begin

Ensure you have created a new page according to the [Creating a new custom page](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-new-custom-page) guide.

## URLs guidelines

To associate a custom landing page with a content type, note the following when creating your page's URL.

### Setting up content type parameter

- Any URL parameter named `{entity}_id` is recognized as a content type. For example, `finder_id` creates the `${finder}` content type.

  >⚠️ For the URL definition, adding the identifier of the content type is not enough. You must also attach `_id` in the sequence. For example, if you create a URL such as `/foo/:bar`, the content will be tied to that URL, since there is no parameter capable of being interpreted as a content type. Thus, if you access *Storefront > Site Editor* and update the content for `/foo/skywalker`, the content related to any page matching `/foo/:bar` will be updated as well.

- The page URL can have only one parameter that designates a content type.
- The page URL can have only one parameter ending with `_id`.
- Any additional variable parameters in the URL are ignored when matching content. For example, if you create the route `/foo/:bar/:{entity}_id`, the same content will be delivered for `/foo/skywalker/1` and `/foo/palpatine/1` as they both relate to the `{$entity}` content type.

### Handling URL changes

If you change your URL, the assets will remain associated with the content type, not the specific URL.

For example, if you create a page with the URL `/store/:store_id`, where `store_id` represents the `${store}` content type, and later change it to`/store-finder/:store_id`, the assets will still be accessible at the new URL, as they both relate to the `${store}` content type.

### Dos and Don’ts

|✅ Do | Explanation |
| - | - |
| `/foo/:{entity}_id` | The URL uses a content type parameter (ending with `_id`) that allows the system to recognize the content type. For example, if `{entity}` is finder, this URL would link to the `${finder}` content type. |

| ❌ Don’ts | Explanation |
| - | - |
| `/foo/:{entity}`|The URL is incorrect because it lacks the required `_id` suffix. Without `_id`, the system cannot recognize it as a content type, which means no assets will be associated with this URL. |
| `/foo/:bar/:{entity}_id`|While this URL includes a valid content type parameter, any additional variable parameters (like `:bar`) are ignored when determining content association. This can lead to unexpected content being delivered. |
| `/foo/:{entity}_id/{entity2}_id`|The URL is not allowed because it has two parameters ending with `_id`. To maintain clarity in the content association, a URL can only have one content type parameter ending with `_id`. |
