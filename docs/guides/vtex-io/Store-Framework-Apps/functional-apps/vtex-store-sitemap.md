---
title: "Store Sitemap"
slug: "vtex-store-sitemap"
hidden: false
createdAt: "2020-06-03T15:19:35.206Z"
updatedAt: "2022-08-12T20:16:11.281Z"
---
The Store Sitemap app is responsible for automatically generating a `sitemap.xml` file of your store website.

An important SEO feature for cross-border stores is having a sitemap capable of handling route internationalization. This guarantees that each route has its alternate link for the supported locale binding. Once the app is deployed and installed in your account, your store will benefit from having a sitemap, which can lead to increased visibility of your site in search tools, such as Google.

For more information about generating a sitemap, check the following sections.

## Before you begin

This app is available to stores using `vtex.edition-store@3.x` or a later version of the [Edition App](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app). To check which Edition App is installed on your account, run `vtex edition get`. If it is an older Edition, please [open a ticket](https://help-tickets.vtex.com/smartlink/sso/login/zendesk) to VTEX Support asking for the installation of the `vtex.edition-store@3.x` Edition App or a newer version.

Before generating your store's sitemap, you might want to adjust if products, navigation, app and/or custom routes will be included in it or not. If that is the case, check the [Advanced Configuration section](#advanced-configuration) for more information.

## Instructions

1. Using your terminal and the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference), log into your account.
2. Run `vtex use {workspaceName} --production` to use a production workspace or [create a production workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-production-workspace) from scratch.

> ⚠️ Remember to replace the values between the curly brackets according to your scenario.

3. Run `vtex install vtex.store-sitemap@2.x` to install the Sitemap app.

4. Run `vtex install vtex.admin-graphql-ide@3.x` to install the GraphQL admin IDE.
5. In your browser, access the account's administrative panel and select the **GraphQL IDE**.

![adminsidebarmenu](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-store-sitemap-0.png)

6. From the dropdown list, choose the `vtex.routes-bootstrap@0.x` app.
7. If this is **not the first time** you're generating your store's sitemap or if your store's routes **did not suffer any changes** since the last time you generated your store's sitemap, go to step 8. Otherwise, run the following query:

    ```graphql
    {
      bootstrap {
        brands
        categories
      }
    }
    ```

  The expected response is a `JSON` object in the following format:

    ```json
    {
      "data" : {
        "bootstrap" {
          "brands": true,
          "categories": true
        }
      }
    }
    ```

8. Now, from the GraphQL IDE dropdown list, choose the `vtex.store-sitemap@2.x` app.

9. Run the following query:

  ```
  {
    generateSitemap
  }
  ```

  The expected response body is

  ```
  {
    "data": {
      "generateSitemap": true
    }
  }
  ```

  This means your sitemap will be available in some minutes, after being processed and saved on our database.

  > ℹ️ Keep in mind that the time taken to generate a sitemap is proportional to the number of products. For example, the average time to generate a sitemap for a store with 60k products is 30 minutes. For 5k products, the duration should be about 5 minutes.

  > ⚠️ If you attempt to send a new request to the Sitemap API while your store's sitemap generation is already taking place, the following message will be displayed:
  > 
  > ```
  > Sitemap generation already in place
  > Next generation available: <End-date>
  > ```

  To make a force restart, add the `force` argument to the query, as in: `generateSitemap(force: true)`. But, be aware that this will cancel the previous process.

10. Check the sitemap generated for the current workspace you are working on by accessing `https://{workspace}--{account}.myvtex.com/sitemap.xml` on your browser. Notice that if your store is a cross-border one, you'll first see an index containing a website's sitemap for each locale.

  > ℹ️ Notice that different `.xml` files are generated according to their entity type (product, category, subcategory, user routes, brand and department) and that each `.xml` file supports a maximum of 5k routes.

11. If you're happy with the results, run `vtex promote` to promote your workspace and to have your sitemap in your master workspace.

  Once you promoted your workspace, no further actions are needed on your part: you are ready to check out your store's sitemap by accessing `https://{account}.myvtex.com/sitemap.xml` on your browser.

### Advanced configuration

#### Managing routes

You can manage if you want to include product, navigation and/or apps routes in your sitemap or not. To do that, check the following step by step.

1. In your browser, access the the account's Admin in which you are working using the Production workspace used in the **step 2** of the [Configuration section](#configuration) (`{workspaceName}--{accountName}.myvtex.com/admin`).
2. Go to **Account settings > Apps > My apps** and search for **Sitemap** app.
3. Enable or disable product, navigation, or app routes according to your scenario.

  ![sitemap-admin](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-store-sitemap-1.png)

#### Enabling custom routes

If you have [custom pages](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-new-custom-page) configured in a `routes.json` file and want them to be included in your store's sitemap, add `isSitemapEntry=true` as a prop of the routes you want to include in the sitemap. Take the following example:

```
{
    "store.custom#about-us": {
      "path": "/about-us",
      "isSitemapEntry": true
  }
}
```

Once everything is set up, go back to the **step 4** of the [Configuration section](#configuration).

#### Extending the sitemap

To add custom routes created by an app (for example, the ones created by the [`store-locator`](https://github.com/vtex-apps/store-locator)) to your store's sitemap, the app must respond to an XML file containing a list of the routes created by that app. Lastly, you must include the path to the XML file that your app responds to as an index of your store's sitemap.

For implementation details, check the following step by step.

1. Create or modify your app to respond to the following route `/sitemap/{index-name}.xml` and to return an XML file containing the data that you want the search engine (e.g., Google) to index. Remember to replace the values between the curly brackets according to your scenario.

  > ℹ️ We recommend that you use a pre-created XML file. Otherwise, for every request, the XML file will be built from scratch, consuming more time to complete the task.

2. [Publish](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app) and install your app in a production workspace.

3. Now, to make your index available in the sitemap root file (`/sitemap.xml`), access your account's admin, relative to the workspace you're working on, and select the GraphQL IDE.

4. From the dropdown list, choose the `vtex.store-sitemap@2.x` app and perform the following mutation, adapting it to your scenario:

  ```gql
  mutation {
    saveIndex(index: "{index-name}")
  }
  ```

  > ℹ️ **If your store is a cross-border one**, keep in mind that the `saveIndex` mutation also accepts the `binding` id as an argument. That means that, by specifying the `binding` id, you can add your new index to the sitemap of the desired binding. If the `binding` id is not specified, the mutation will consider the store's default binding.

5. Check the updated sitemap for the current workspace you are working on by accessing `https://{workspace}--{account}.myvtex.com/sitemap.xml` in your browser.

6. If you're happy with the results, run `vtex promote` to promote your workspace and to have your sitemap in your master workspace.

##### Removing a custom route

If it's ever desired to remove a custom route, you may execute the following mutation, which takes the same arguments as `saveIndex`:

  ```gql
  mutation {
    deleteIndex(index: "{index-name}")
  }
  ```
