---
title: "Indicating alternate versions of localized pages in cross-border stores"
slug: "vtex-io-documentation-indicating-alternate-pages-in-cross-border-stores"
hidden: false
excerpt: "Learn how to indicate alternate versions of localized pages."
createdAt: "2020-11-23T14:49:49.171Z"
updatedAt: "2025-10-30T16:07:14.409Z"
---

In this guide, you'll learn how to indicate alternative versions of localized landing pages in cross-border stores to improve SEO and ensure search engines display the correct content for each region.

If your store operates in multiple regions and you have different versions of a [landing page](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-new-custom-page) for each, you should link them as alternate versions. This practice helps search engines understand the relationship between your localized pages, ensuring they serve the right content to the right audience and improving your store's SEO.

When you indicate alternate versions, you must do so in pairs. For example, if you point the US version of a page to a Brazilian one, the Brazilian page must also point back to the US version. This reciprocal linking enables search engines to accurately map the relationship between them, thereby preventing indexing errors.

![Frame 15](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-indicating-alternate-pages-in-cross-border-stores-0.png)

Follow the steps below for each localized version of your landing page.

## Instructions

### Step 1 - Getting the route information

1. In your terminal, [install](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app) the `vtex.admin-graphql-ide@3.x` app.
2. In the Admin, go to **Store Settings > Store > GraphQL IDE**.
3. From the GraphQL IDE dropdown list, choose the `vtex.rewriter` app.
4. Run the following query to get the internal data for the page path you want to update:

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

⚠️ Replace the values between the curly brackets according to your scenario.

5. Save the returned data.

### Step 2 - Updating the route

1. Erase the previous query and use the following mutation command

  ```graphql
  mutation saveInternal($args: InternalInput!) {
    internal {
      save(route: $args) {
        id
      }
    }
  }
  ```

2. At the bottom of the page, click Query Variables.
3. Fill in the Query Variables section with the data from the [previous step](#getting-the-route-information) and the information for your alternate pages. See the example below:

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

- For the `from`, `declarer`, `type`, `id`, and `binding` fields, use the information you obtained in the [previous section](#getting-the-route-information).
- In the `alternates` field, provide the `binding` and `path` for each alternate landing page.

  >⚠️ If you don't know the `binding` values of your stores, follow [this step-by-step on checking your account's `binding` ids](https://developers.vtex.com/docs/guides/checking-your-stores-binding-id).

4. Click `Run` to apply the changes.

Repeat this entire process for each alternate version of the landing page, updating the path in the initial query each time.
