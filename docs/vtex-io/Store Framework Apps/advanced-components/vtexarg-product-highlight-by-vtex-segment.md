---
title: "Product Highlight by VTEX Segment"
slug: "vtexarg-product-highlight-by-vtex-segment"
excerpt: "vtexarg.product-highlight-by-vtex-segment@0.3.2"
hidden: false
createdAt: "2021-11-24T19:09:10.931Z"
updatedAt: "2022-03-15T18:24:10.878Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

The **Product Highlight by VTEX Segment** app allows shoppers to select a Whitelabel Seller available in their region, and it filters the product listing results accordingly. The app also uses a badge to highlight products of Whitelabel Sellers that are available in the shopper's region.

![Media Placeholder](https://user-images.githubusercontent.com/55905671/143295939-7d1b5625-5c57-46ad-a197-ef959db268de.gif)

---

## Before you start

Before configuring the **Product Highlight by VTEX Segment** app, make sure to create a collection for each Whitelabel Seller of your store (*See [Creating Collections Beta](https://help.vtex.com/en/tutorial/creating-collections-beta) for more information).* When naming your collection, make sure to use the following naming structure: `{sellerId}-{defaultCollectionName}`, where the `{sellerId}` is the `sellerId` of the Whitelabel Seller and `{defaultCollectionName}` is the name of the Collection.

![Colection Name](https://user-images.githubusercontent.com/55905671/143301880-ee440d48-eced-4750-9cd2-ae3f3588a8e4.png)

---

## Configuration 

To configure the **Product Highlight by VTEX Segment** app, you'll need to:
1. Set up the default configurations of the **Product Highlight by VTEX Segment** app via the VTEX Admin.
2. Add the **Product Highlight by VTEX Segment** to the store theme.

By the end of these steps, you'll have your store products highlighted according to the Whitelabel Seller selected.

## Setting up the Product Highlights app

1. Open the terminal and log in to the desired VTEX account using the [VTEX IO CLI](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-installation-and-command-reference).
2. Install the `vtexarg.product-highlight-by-vtex-segment` app on your account.
   ```sh
   vtex install vtexarg.product-highlight-by-vtex-segment
   ```
3. Open the VTEX Admin.
4. Go to **Account Settings > Apps > My apps**.
5. Look for the **Product Highlight by VTEX Segment** app and click on **Settings**.

   ![Product Highlight by VTEX Segment](https://user-images.githubusercontent.com/55905671/143299640-21b00a57-64bc-467c-917b-34a16d44bc51.png)

6. Fill in the presented fields as in the following:
   - **Default Seller Id** - Enter the default seller ID to use in cases the shopper's region is not detected (e.g., `jumboargentinav692lanus692`).
   - **Default Collection Name** - Enter the name of the collection corresponding to the default seller ID (e.g., `leyDeGondolas`). This is the `{defaultCollectionName}` part of the **Collection Name** (*See [Before you start](#before-you-start) for more information*).
   - **Image Url of Highlight** - Enter the URL of the ximage badge that will highlight the products. For example: ![Image Url of Highlight](https://user-images.githubusercontent.com/60782333/152064990-8990c5a7-3549-49c9-91b0-3bc3ad7604fb.png)
7. Click on **Save**.

### Adding the Product Highlights component to your store theme

1. Open your store theme in any code editor of your choice.
2. Open the `manifest.json` file and add the `vtexarg.product-highlight-by-vtex-segment` app as a peer dependency of your theme:
    ```diff
    "peerDependencies": {
       ...
    +  "vtexarg.product-highlight-by-vtex-segment": "0.x"
       ...
    }
    ```
3. Add the `product-highlight-by-vtex-segment` block to any child of the `store.product` template (Product Details Page template). For example:

    ```diff
    "store.product": {
        "children": [
        "flex-layout.row#product-main",
        ]
    },
    "flex-layout.row#product-main": {
        "children": [
        "flex-layout.col#right-col"
        ]
    },
    "flex-layout.col#right-col": {
        "children": [
    +     "product-highlight-by-vtex-segment"
        ]
    }
    ```

Now, see the [Customization](#customization) section to add custom styles to your component.

After [linking your store theme app](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-linking-an-app) in a development workspace, you'll be able to select a Whitelabel Seller available in your region from a dropdown menu list. 

![Select Whitelabel Seller](https://user-images.githubusercontent.com/55905671/143302341-6ba9d940-185f-4c9a-98c5-cb158f285d03.png)

You'll then be able to see the chosen badge in the product cards of the selected Whitelabel Seller's collection.

![Image Url of Highlight](https://user-images.githubusercontent.com/55905671/143302850-e8d39857-ffb6-49fc-b1cf-a7496733ac4c.png)

## Customization

To apply CSS customizations in this and other blocks, follow the [Using CSS Handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization) guide.

| CSS Handles |
| ----------- | 
| `productHighlightByVtexSegmentContainer` | 
| `imageOfHighlight` | 

---
<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:
<table>
  <tr>
    <td align="center"><a href="https://github.com/germanBonacchi"><img src="https://avatars.githubusercontent.com/u/55905671?v=4" width="100px;" alt=""/><br /><sub><strong>Germán Bonacchi</strong></sub></a><br /><a href="https://github.com/vtex-apps/product-highlight-by-vtex-segment/commits?author=germanBonacchi" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/arielabaruffaldi"><img src="https://avatars.githubusercontent.com/u/36748003?v=4" width="100px;" alt=""/><br /><sub><strong>Ariela Baruffaldi</strong></sub></a><br /><a href="https://github.com/vtex-apps/product-highlight-by-vtex-segment/commits?author=arielabaruffaldi" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/GuidoSdo"><img src="https://avatars.githubusercontent.com/u/33711188?v=4" width="100px;" alt=""/><br /><sub><strong>Guido Salcedo</strong></sub></a><br /><a href="https://github.com/vtex-apps/product-highlight-by-vtex-segment/commits?author=GuidoSdo" title="Code">💻</a></td>
  </tr>
</table>
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->