---
title: "Flixmedia"
slug: "vtex-flixmedia"
hidden: false
createdAt: "2020-06-03T15:19:51.305Z"
updatedAt: "2021-10-13T18:37:48.020Z"
---
> ⚠️ This app is now supported by ACCT. For more information and support, email `support@acct.global`.

Flixmedia first party integration app. The [solution](https://flixmedia.eu/) enhances your website content, capturing retail partners, engaging shoppers, and increasing sale rates.

## Configuration

### Step 1 - Installing the Flixmedia app

#### Using VTEX App Store

1. Access the Apps section in your account's admin page.
2. Look for the Flixmedia app.
3. Click on the `Install` button.

#### Using VTEX IO CLI

In your terminal, log into your VTEX account and [install](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app/) the `vtex.flixmedia@0.x` app.

> ℹ️ *You can confirm if the app has been properly installed by running `vtex ls`.*

### Step 2 - Defining the app settings

1. Access the Flixmedia app in your admin's Apps section.
2. Fill out the fields according to your Flixmedia data.
3. Save your changes.

![flixmedia-gif](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-flixmedia-0.gif)

### Step 3 - Updating your store theme

1. Add the Flixmedia app to your theme's dependencies in the `manifest.json` file:

```diff
 dependencies: {
+  "vtex.flixmedia": "0.x"
 }
```

2. Declare the `product-details.flixmedia` block in the `store.product`'s children list, as shown below:

```json
"store.product": {
  "children": [
    "product-description.flixmedia",
  ]
}
```

3. [Deploy your changes](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-theme-content-public).

## Customization

No CSS Handles are available yet for the app customization.
