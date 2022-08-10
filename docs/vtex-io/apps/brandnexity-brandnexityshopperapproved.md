---
title: "Brandnexity Shopper Approved"
slug: "brandnexity-brandnexityshopperapproved"
excerpt: "brandnexity.brandnexityshopperapproved@1.0.7"
hidden: true
createdAt: "2022-07-18T14:45:47.742Z"
updatedAt: "2022-07-18T14:45:47.742Z"
---
1. Add the app to your theme's dependencies in the `manifest.json`:

You need [vtex shopper approved](https://github.com/vtex-apps/shopper-approved) because both app work together. If you already has vtex.shopper-approved install only brandnexity-shopper-approved.

```bash
vtex install vtex.shopper-approved@1.x
vtex install brandnexity.shopper-approved@0.x
```

```jsonc
{
    "dependencies": {
        "vtex.shopper-approved": "1.x",
        "vtex.shop-review-interfaces": "0.x",
        "brandnexity.shopper-approved": "0.x"
    }
}
```

2. In your admin dashboard, navigate to Apps > Shopper Approved and input the following settings:

**Into VTEX Shopper Approved**

- Shopper Approved site ID: Enter the site ID from your Shopper Approved account.

- Shopper Approved Initial Survey token: Enter the Initial Survey token from your Shopper Approved account.

- Shopper Approved domain: Enter your store domain as it appears in your Shopper Approved account. Typically this is in the form yourstore.com.

**Into Brandnexity Shopper Approved**

- Shopper Approved site ID: Enter the site ID from your Shopper Approved account.

- Shopper Approved Initial Survey token: Enter the Initial Survey token from your Shopper Approved account.


**Brandnexity Shopper Approved exclusively blocks**

3. Add the `starShelfs` block in all `product-summary.shelf` inside the SHELFS that you want to show the STARS. This block will show the stars on shelfs.

![image](https://gitlab.com/acct.global/code-witchers/brandnexity/brandnexity.tackoftheday/uploads/ee52615695e6f71ecd1e4ce854b42af9/image.png)

```jsonc
{
    "product-summary.shelf": {
        "children": ["starShelfs"]
    }
}
```

5. Add the `pixelPdpStars` on your product page inside your `store.product`. This block will show the STARS on product page with an ancor to `productPageReview` block.

![image](https://gitlab.com/acct.global/code-witchers/brandnexity/brandnexity.tackoftheday/uploads/e90452629748e10aff7ec451909bbbe9/image.png)

```jsonc
{
    "store.product": {
        "children": ["flex-layout.row#product-main"]
    },
    "flex-layout.row#product-main": {
        "children": ["flex-layout.col#right-col"]
    },
    "flex-layout.col#right-col": {
        "children": ["pixelPdpStars"]
    }
}
```

6. Add the `productPageReview` block in your `store.product` at the product page. We recommend to use `flex-layout.row`. This block will show the comments from the product and a button to do new product reviews.

![image](https://gitlab.com/acct.global/code-witchers/brandnexity/brandnexity.tackoftheday/uploads/9037dc67ed32c884bd91e9a54ebcde61/image.png)

```jsonc
{
    "store.product": {
        "children": ["flex-layout.row#shopperApproved-reviews"]
    },
    "flex-layout.row#shopperApproved-reviews": {
        "props": {
            "blockClass": "shopperApproved"
        },
        "children": ["productPageReview"],
        "title": "Shopper Approved Review"
    }
}
```

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/BeatrizMiranda"><img src="https://avatars2.githubusercontent.com/u/28959326?v=4" width="100px;" alt="Beatriz Miranda"/><br /><sub><b>Beatriz Miranda</b></sub></a><br /><a href="" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/JoseMeneghetti"><img src="https://avatars2.githubusercontent.com/u/43099776?s=460&u=4668a920af4bbc5214a9d245ced2745b70feb07c&v=4" width="100px;" alt="Jose Ricardo photo"/><br /><sub><b>José Ricardo</b></sub></a><br /><a href="" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!