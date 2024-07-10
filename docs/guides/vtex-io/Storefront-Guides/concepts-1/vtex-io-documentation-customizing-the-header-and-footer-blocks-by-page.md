---
title: "Customizing the Header and Footer blocks by page"
slug: "vtex-io-documentation-customizing-the-header-and-footer-blocks-by-page"
hidden: false
createdAt: "2020-06-03T16:02:44.275Z"
updatedAt: "2022-12-13T20:17:44.048Z"
---
The Header and Footer are the two blocks that appear the most during a user's store navigation. From the homepage to the product page, from checkout to the Order Placed page, whatever a template's content may be, these two blocks will probably be present.

With that constancy in mind, you just need to declare these blocks once in the `blocks.jsonc` file, in a template of your choosing (usually it's `store.home`).

This is only possible because both Header and Footer have been previously defined behind the scenes as **default store interface elements**, allowing the Framework to identify the Header and Footer block as default for any other templates as well.

You may, however, want to apply a Header configured differently onto your Homepage and keep the default Framework Header for the Order Placed page or you may even not want any Footer on your product pages.

All of the above and more may be easily customized in the Header and Footer blocks, by simply **overwriting the specific automatic duplication** and **declaring the desired new configurations** thereafter.

## Step 1 - Overwriting automatic duplication

In the desired template, declare the code given as an example below to overwrite the Header and Footer automatic duplication.  

> ℹ Replace the `{headerBlock}` and `{footerBlock}` values with real block names. Also, replace the `{templateName}` value with a valid theme template, such as `product`, `search#category`, and `custom`.

```json
{
  "store.{templateName}": {
    "parent": { 
      "header": "{headerBlock}", 
      "footer": "{footerBlock}"
    }
  }
}
```

The code above works in scenarios where the Header **and** Footer will be overwritten. When overwriting just one of the two, keep the template's `parent` structure and determine which block will be customized. For example:

```json
{
  "store.{templateName}": {
    "parent": { 
      "header": "{headerBlock}"
    }
  }
}
```

## Step 2 - Applying new customizations

The next step is to configure the previously declared blocks in accordance with what's desired for this template.

If you want to apply new customizations to the blocks, simply follow the usual flow explained in the [Header](https://developers.vtex.com/docs/guides/vtex-store-header/) and [Footer](https://developers.vtex.com/docs/guides/vtex-store-footer/) documentation. For example:  

```json
{
  "store.product": {
    "parent": { 
      "header": "header#product"
    }
  },
  "header#product": {
    "blocks": [
      "header-layout.desktop",
      "header-layout.mobile"
    ]
  },
  "header-layout.desktop": {
    "children": [
      "header-row#1-desktop"
    ]
  },
  "header-row#1-desktop": {
    "children": ["telemarketing"],
    "props": {
      "fullWidth": true
    }
  }
}
```

It is possible, however, that you do not want new configurations, but rather want to remove the blocks from the template. In such a scenario, you need to declare the desired blocks and leave the `children` blank, as shown in the following example:

```json
{
  "store.custom#noheaderfooter": {
    "parent": {
      "header": "header#empty",
      "footer": "footer#empty"
    },
  },
  "header#empty": {
    "blocks": [
      "header-layout.desktop#empty",
      "header-layout.mobile#empty"
    ]
  },
  "header-layout.desktop#empty": {
    "children": []
  },
  "header-layout.mobile#empty": {
    "children": []
  },
  "footer#empty": {
    "blocks": [
      "footer-layout.desktop#empty",
      "footer-layout.mobile#empty"
    ]
  },
  "footer-layout.desktop#empty": {
    "children": []
  },
  "footer-layout.mobile#empty": {
    "children": []
  }
}
```

Once you save the changes and link your app, you'll see the new configurations for these blocks reflected on the desired page.
