---
title: "Hide Print order and Reprint receipt buttons"
slug: "hide-print-order-and-reprint-receipt-buttons"
hidden: false
createdAt: "2021-12-08T14:27:15.056Z"
updatedAt: "2021-12-08T14:29:39.856Z"
---
By default, inStore shows the options to `Print order` and `Reprint receipt` in the [Order placed page](https://help.vtex.com/en/tracks/instore-using-the-app--4BYzQIwyOHvnmnCYQgLzdr/TrTtmCGVLTaCSmowGFYDI). If you want to hide these buttons, you can change their display by editing the `checkout-instore-custom.css` file. Check out the [How to customize inStore guide](https://developers.vtex.com/vtex-rest-api/docs/how-to-customize-instore#css-customizations) for further information on how to access this file.


## Edit the `checkout-instore-custom.css` file

To customize which cancellation options inStore will display, you must declare the following class and property in the `checkout-instore-custom.css` file.

In the **UI display** column below, you can see where the elements you can hide are rendered in the inStore UI. You can click on each image to enlarge it.

[block:parameters]
{
  "data": {
    "h-0": "CSS class name",
    "h-1": "Description",
    "h-2": "UI display",
    "0-0": "`print-details`",
    "0-1": "The class you can use to style the `Print order` and the `Reprint receipt` buttons.",
    "0-2": "![print-order](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX%20inStore/how-to-customize-instore/faaeea5-Group_1_25.png)\n\n![reprint-receipt](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/hide-print-order-and-reprint-receipt-buttons-0.png)"
  },
  "cols": 3,
  "rows": 1
}
[/block]
If you want to hide these elements, you must use their class selector and declare the `display` property with the value set as `none`, as exemplified below.

``` css
.print-details {
  display: none;
}
```