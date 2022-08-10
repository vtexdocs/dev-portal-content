---
title: "Disable product recommendations"
slug: "enable-product-recommendations"
hidden: true
createdAt: "2021-08-11T19:18:54.813Z"
updatedAt: "2022-02-24T20:38:39.014Z"
---
By default, inStore shows a list of suggested products to the sales associate in two stages of the order:
- In the cart
- On the product page

If you want to hide these recommendations, you need to follow the steps below to edit the `checkout-instore-custom.css` and `checkout-instore-custom.js` files. To learn more about these files, read the [How to customize inStore](https://developers.vtex.com/vtex-rest-api/docs/how-to-customize-instore) guide.
[block:html]
{
  "html": "<br>"
}
[/block]
## Edit the CSS file

In the `checkout-instore-custom.css` file, you must include the following CSS rule:
[block:code]
{
  "codes": [
    {
      "code": "#recommendation-shelf {\n  display: none;\n}",
      "language": "css"
    }
  ]
}
[/block]
This rule hides the product recommendation component from the front-end.
[block:callout]
{
  "type": "info",
  "body": "After making changes in the code, make sure you press the `Save` button."
}
[/block]

[block:html]
{
  "html": "<br>"
}
[/block]
## Edit the JavaScript file

In addition to editing the CSS file, it is necessary to make a change to the `checkout-instore-custom.js` file.

1. Once you have opened it, you must add the `recommendationsEnabled` property inside the `window.INSTORE_CONFIG` object, with the value `false`.

The code block should look like this:
[block:code]
{
  "codes": [
    {
      "code": "window.INSTORE_CONFIG = {\n  recommendationsEnabled: false,\n}",
      "language": "javascript"
    }
  ]
}
[/block]
2. Click on `Save` to store your changes. 

[block:callout]
{
  "type": "danger",
  "body": "Do not remove any of the other properties present in the `window.INSTORE_CONFIG` object, to avoid breaking other functionalities."
}
[/block]

[block:html]
{
  "html": "<br>"
}
[/block]
## Check out your changes

1. Open the inStore app menu
2. Update the data by clicking the `Reset app local data` button.

Once this is done, the sales associates will no longer see product recommendations.