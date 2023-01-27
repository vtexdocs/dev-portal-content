---
title: "Hide cancellation buttons"
slug: "hide-cancellation-buttons"
hidden: false
createdAt: "2021-12-02T22:09:11.883Z"
updatedAt: "2021-12-02T22:14:46.075Z"
---

By default, inStore shows the options to `Cancel total order` and `Cancel order` in the [Order placed page](https://help.vtex.com/en/tracks/instore-using-the-app--4BYzQIwyOHvnmnCYQgLzdr/TrTtmCGVLTaCSmowGFYDI). If you want to hide these buttons, you can change the display of cancellation options by editing the `checkout-instore-custom.css` file. Check out the [How to customize inStore guide](https://developers.vtex.com/vtex-rest-api/docs/how-to-customize-instore#css-customizations) for further information on how to access this file.

## Edit the checkout-instore-custom.css file

To customize which cancellation options inStore will display, you must declare the following IDs and properties in the `checkout-instore-custom.css` file.

In the **UI display** column below, you can see where the elements you can hide are rendered in the inStore UI. You can click on each image to enlarge it.
[block:parameters]
{
"data": {
"h-0": "CSS ID selector name",
"h-1": "Description",
"h-2": "UI display",
"0-0": "`cancel-total-order`",
"1-0": "`cancel-order`",
"0-1": "The ID selector you can use to style the `Cancel full order` button. This button enables total cancellation of orders.",
"1-1": "The ID selector you can use to style the `Cancel order of this package` button. This button enables partial cancellation of orders, which means you can cancel individual packages.",
"0-2": "![cancel-full-order](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX%20inStore/how-to-customize-instore/hide-cancellation-buttons-0_26.png)",
"1-2": "![cancel-order-package](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX%20inStore/how-to-customize-instore/hide-cancellation-buttons-1_27.png)"
},
"cols": 3,
"rows": 2
}
[/block]

If you want to hide one or both of these elements, you must use their respective ID selector and declare the `display` property with the value set as `none`, as exemplified below.

[block:code]
{
  "codes": [
    {
      "code": "#cancel-total-order {\n    display: none;\n}\n\n#cancel-order {\n    display: none;\n}",
      "language": "css"
    }
  ]
}
[/block]
