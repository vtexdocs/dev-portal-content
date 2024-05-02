---
title: "Store Link"
slug: "vtex-store-link"
hidden: false
createdAt: "2020-06-03T15:19:30.090Z"
updatedAt: "2022-11-11T16:13:51.504Z"
---

The Store Link app provides blocks responsible for displaying links in other theme blocks, such as the Product Summary.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-store-link-0.png)

## Configuration

1. Add the `store-link` app to your theme's dependencies in the `manifest.json` file. You'll, then, be able to use all the [blocks](#blocks) exported by the `store-link` app and its respective [props](#props).

```diff
  "dependencies": {
+   "vtex.store-link": "0.x"
  }
```

2. Based on the exported list, choose the desired block and declare it in the block that will host the link. Find below an example of a `link.product` being used in the [`product-summary`](https://vtex.io/docs/components/product/vtex.product-summary) block:

```jsonc
{
  "link.product#product-page": {
    "props": {
      "href": "/{slug}/p",
      "label": "More details >"
    }
  },
  "product-summary.shelf": {
    "children": [
      "product-summary-image",
      "product-summary-name",
      "product-rating-inline",
      "product-summary-space",
      "product-summary-price",
      "link.product#product-page"
    ]
  },
}
```

>⚠️ Note that you must place the `link.product` block inside a block that provides a product context (e.g., [`ProductSummary`](https://vtex.io/docs/components/product/vtex.product-summary)). From the previous example, note that a `{slug}` placeholder is being passed onto the `href` prop. When rendered, this placeholder is overwritten by the value accrued from the closest product context, generating a link like `/everyday-necessaire/p`.

## Blocks

| Block     | Description                                     |
| -------------- | ----------------------------------------------- |
| `link.product` | A link that consumes the product context.       |
| `link`         | A normal link that doesn't consume any context. |

## Props

All blocks exported by `store-link` share the same props:

| Prop name | Type     | Description | Default value |
| --------- | -------- | ------------------------------------------------- | ------------- |
| `label`   | `string` | Link text.         | `undefined`   |
| `href`    | `string` | Link URL.         | `#`         |
| `scrollTo`    | `string` | Element anchor to scroll after navigation. (E.g. `"#footer"`)  | `undefined`         |
| `target`  | `string` | Where to display the linked URL. This prop works the same way as the target from [HTML `<a>` element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a). Since the [*anchor* element's target](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a#attr-target) default is `_self`, this prop will be set to `_self` if it's undefined.| `undefined`   |
| `displayMode` | `enum` | How the link should be displayed. Possible values are: `anchor` (displays a normal link with no styles) or `button` (displays a button that can be customized using the `buttonProps` prop.  | `anchor` |
| `buttonProps` | `object` | How the link button should be displayed. Use this prop only when the `displayMode` prop is set as `button`. | `{ variant: primary, size: regular }` |
| `escapeLinkRegex`   | `string` | RegExp, with global match, used to remove special characters within product specifications. (E.g. if you want to use `/[%]/g` then `escapeLinkRegex` = `[%]` )         | `undefined`   |
| `rel` | `string` | This prop specifies the relationship between the current document and the linked document (for better SEO). This prop works the same way as the `rel` attribute from `<a>`, the [HTML anchor element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a). Supported values can be found [here](https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types) | `undefined` |

- `buttonProps` object:

| Prop name | Type | Description | Default value |
| --- | --- | --- | --- |
| `variant` | `enum` | Link button visual proeminence. Possible values are: `primary` or `secondary` (values are set according to the [VTEX Styleguide](https://styleguide.vtex.com/#/Components/Forms/Button)).  | `primary` |
| `size` | `enum` | Link button size. Possible values are: `small`, `regular` or `large` (values are set according to the [VTEX Styleguide](https://styleguide.vtex.com/#/Components/Forms/Button)). | `regular` |

## Modus Operandi

When creating an URL link using the `href` prop, you can create hypotheticals query string values, as shown in the example below:

```json
{
  "link#foo": {
    "props": {
      "href": "/login?returnUrl={queryString.returnUrl}",
      "label": "Sign in"
    }
  }
}
```

Considering the `href` prop from the previous example, note that the URL link will be built correctly if the current page has the `returnUrl` query string. Otherwise, an empty value will take place.

Depending on the context used by the `link.product` block, you can use *product variables* to structure different URL paths for the `href` prop, such as a link to a given product department (`/{department}`).

| Product variable   | Description                                   |
| -------------- | --------------------------------------------- |
| `brand`      | Product brand name.                    |
| `brandId`    | Product brand ID.                     |
| `category1`  | Highest level category in the category tree.    |
| `category2`  | Second highest level category.                 |
| `category3`  | Third hieghest level category.                |
| `category4`  | Fourth highest level category.                 |
| `department` | Product department.                            |
| `productId`  | Product ID.                                    |
| `skuId`      | Current selected SKU ID.                       |
| `slug`       | The link text used to create the product link. |

To build URLs with variables related to product specifications, use the following format: `{specificationGroups.groupName.specifications.specificationName}`. Replace `groupName` and `specificationName` with the specification group and the product specification names accordingly. For example:

```jsonc
{
  "link.product#vtex": {
    "props": {
      "href": "{specificationGroups.Design.specifications.Dimensions}",
      "label": "VTEX"
    }
  }
}
```

In the example above, `Design` is the specification group name and `Dimensions` is the product specification name.

## Customization

To apply CSS customizations in this and other blocks, follow the [Using CSS handles for store customization](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization) guide. All blocks have the same handles.

| CSS Handles         |
| ------------------- |
| `childrenContainer` |
| `label`             |
| `link`              |
