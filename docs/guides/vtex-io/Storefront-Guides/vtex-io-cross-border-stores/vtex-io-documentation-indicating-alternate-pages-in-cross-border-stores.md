---
title: "Indicating alternate versions of localized pages in cross border stores"
slug: "vtex-io-documentation-indicating-alternate-pages-in-cross-border-stores"
hidden: false
createdAt: "2020-11-23T14:49:49.171Z"
category: "Storefront Development"
updatedAt: "2022-12-13T20:17:44.702Z"
---

If you have different versions of a [landing page](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-new-custom-page) for each region your store is present, we recommend that you save them as `alternate` versions.

This way, search engines will be aware of the different versions of your page and able to provide the right content to the right audience.

> ℹ️ Notice that this is especially useful for improving your store's SEO.

Keep in mind that when indicating alternate versions of a page, you must do it in pairs. For example, if you point the USA version of a page to a Brazilian variant, then the Brazilian page must point to the USA version as well.

By doing that, search engines are capable of understanding the relationship between those two pages, avoiding issues such as indicating the incorrect title for a given page or wrong indexing.

![Frame 15](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-indicating-alternate-pages-in-cross-border-stores-0.png)

Hence, be aware that you'll need to perform the following step by step for each localized version of your landing page.

> ℹ️ It's important for search engines that each version of a page indicates itself as well as the other localized versions as `alternates`. However, **you don't need to worry about self-referencing** since we already do that for you.

## Instructions

1. [Install](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app) the `vtex.admin-graphql-ide@3.x` app using your terminal.
2. In your browser, access your account's admin and go to the GraphQL IDE section.
3. From the GraphQL IDE dropdown list, choose the `vtex.rewriter` app.
4. Run the following query to get the internal data related to the specified page `path`.

```graphql
{
  internal {
    get(path: "/{URL}") {
      from
      declarer
      type
      id
      binding
    }
  }
}
```

> ⚠️ Remember to replace the values between the curly brackets according to your scenario.

5. Save the returned data.
6. Erase the previous query and fill in the main text box with the following mutation command.

```graphql
mutation saveInternal($args: InternalInput!) {
  internal {
    save(route: $args) {
      id
    }
  }
}
```

7. Click on _Query Variables_ at the bottom of the page and, according to the following example and the following explanations, fill in the _Query Variables_ section.

```json
{
  "args": {
    "from": "/US/about-us",
    "declarer": "vtex.store@2.x",
    "type": "userRoute",
    "id": "vtex.store@2.x:store.custom::us-about-us",
    "binding": "748aafcf-3572-456d-5dec-6ddb3f26e43f",
    "alternates": [
      {
        "binding": "7cf37a3b-efc0-4e47-8201-d8b58kd4d3fd",
        "path": "/BR/sobre-nos"
      },
      {
        "binding": "8cf37a3b-edc0-4a47-8241-d8b58kfsd3fd",
        "path": "/UK/about-us"
      }
    ]
  }
}
```

- Replace the `from`, `declarer`, `type`, `id`, and `binding` values with the information obtained in step 4.
- Regarding the `alternates` field, fill in the `binding` and `path` values according to the alternate landing page's data.

> ⚠️ If you don't know the `binding` values of your stores, follow [this step by step on checking your account's `binding` ids](https://developers.vtex.com/docs/guides/checking-your-stores-binding-id).

Once you perform these changes, remember to repeat the process from step 4 as many times as the number of existing versions of that landing page, using each `alternate` page as the `path`.
