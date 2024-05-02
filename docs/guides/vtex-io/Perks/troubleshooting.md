---
title: "Troubleshooting"
slug: "troubleshooting"
excerpt: "Troubleshoot common issues in development and production environments with this guide."
hidden: false
createdAt: "2020-12-17T18:31:03.581Z"
updatedAt: "2022-02-16T15:20:43.154Z"
---

## Development

### I don't see my changes

Once you [link your app](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app), you should see all your changes live at `https://{workspace}--{accountName}.myvtex.com`. If your theme changes are not reflecting on your store workspace, check the following workarounds to fix your scenario.

<details>
<summary>My workspace does not reflect changes in Typescript types</summary>

The `vtex link` command does not automatically detect changes in Typescript types. To address this issue, follow these steps:

1. Stop the link process with `vtex unlink`.
2. Update the Typescript types.
3. Run `vtex link` to link the app again.

</details>

<details>
<summary>My endpoint is returning outdated values</summary>

If your endpoint is returning outdated values, consider disabling caching temporarily by setting the `no-cache` option on your endpoint's response, as in the following example:

```ts
ctx.set('Cache-Control', 'no-cache')
```

Please note that caching is enabled by default to enhance performance. Only use this option during development if a real-time response is necessary. Ensure not to disable caching for production stores.

</details>

<details>
<summary>My theme changes are not reflecting on my store</summary>

To see your changes in action, the version of the Store Theme you are working must be in the same major as the one from the Store Theme app installed on your account.

1. Log in to your VTEX account.
2. List the apps installed on your account by running `vtex ls`.
3. Check if the major of the Store Theme app installed is different from the one you are developing.
4. Check if there is another `Store Theme` app installed on your VTEX account. If positive, uninstall it.

</details>

### I can't install an app

<details>
<summary>I can't install an app with a major other than `0.x`</summary>

![major](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/development-0.png)

Run `vtex ls` to check which apps are included on the [Edition App](https://vtex.io/docs/concepts/edition-app/) installed on your account. If you see the app you are trying to install with another major, you might have an issue with the Edition App installed on your account.

In this case, consider [opening a support ticket](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app) to request a change to the Edition App installed on your account. First, go to the [Edition App](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app) article to learn more about the available Edition Apps.

</details>

### I can't create a new workspace

<details>
<summary>Render fail when sender is `vtex.menu`, Request failed with status code 400</summary>

###### Checking if the Search Integration process started

1. Access the Admin and go to **Store Settings > Intelligent Search > Integrations**.
2. Check if the search has been activated in the store.
3. Click the `Start integration` button to start integration.

The indexing process will start and you will see a link to the Indexing Status screen.

> ℹ️ The [Integration settings](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/6wKQgKmu2FT6084BJT7z5V) is responsible for the Catalog's initial indexing with VTEX Intelligent Search. After installing the application, this will be the first step to integrating it with the Catalog.

![start-integration](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/development-1.png)

</details>

## Production

### My store translation is not behaving as expected

<details>
<summary>My store is being translated when it shouldn't</summary>

- **Checking the default locale**

Access the API `http://portal.vtexcommercestable.com.br/api/tenant/tenants?q={accountName}` and check the `defaultLocale` file.

  >⚠️ Replace the `{accountName}` with your VTEX account name.

If the `defaultLocale` value doesn't match your store locale, [open a support ticket](https://help-tickets.vtex.com/smartlink/sso/login/zendesk) to report the issue.

</details>

### My routes are not behaving as expected

<details>
<summary>My redirect path doesn't work</summary>

- **Checking if the redirect is saved in the Rewriter**

    1. Install the GraphiQL IDE in your account by running `vtex install vtex.admin-graphql-ide@3.x`.
    2. Access the Admin and go to **Store Settings > Storefront > GraphiQL IDE**.
    3. Select the `vtex.rewriter@1.x` app from the dropdown list.
    4. Run the following query, replacing `{URL}` with the `from` path you are having trouble with:

    ```gql
    {
      redirect {
        get(path: "/{URL}") {
            from
            to
        }
      }
    }
    ```

    The expected answer is a JSON object containing all the redirects related to that path. Take the following example:

    ```json
    {
      "data": {
        "redirect": {
          "get": {
            "from": "/about-us",
            "to": "/my-store"
          }
        }
      }
    }
    ```

- **If the query doesn't return the redirect path**

    Access the Admin, go to **Storefront > Pages > Redirects**, and save the desired URL redirects. For more information, refer to the [Managing URL redirects](https://developers.vtex.com/docs/guides/vtex-io-documentation-managing-url-redirects) guide.

- **If the query returns the redirect path**

    Check if your Store Theme or another app has defined a route with the same path you are attempting to save as a redirect. If the route already exists, the redirect will be ignored.

</details>

### My store is presenting inconsistencies

<details>
<summary>Product price is different on Search Results and Product Detail pages</summary>

The Search Results and Product Details pages have different indexing processes. This can lead to differences in the price.

1. [Reindex](https://developers.vtex.com/docs/guides/vtex-io-documentation-understanding-how-store-url-indexing-works) the products presenting inconsistencies.
2. Check the value set for the [Search Result](https://developers.vtex.com/docs/apps/vtex.search-result) app's `simulationBehavior` prop. If set to `skip`, change it to `default`.

> ℹ️ When the `simulationBehavior` is set to `skip`, the Search Results page displays the cold price based on the user cache. In order to fetch and display the latest price registered in the catalog, change it to `default`.

</details>
