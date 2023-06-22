---
title: "Hide anonymous customer option"
slug: "hide-anonymous-customer-option"
hidden: false
createdAt: "2021-12-08T14:20:49.769Z"
updatedAt: "2021-12-08T14:30:18.357Z"
---

By default, inStore shows the option to continue as an anonymous customer in the **[New order page](https://help.vtex.com/en/tracks/vtex-sales-app-using-the-app--4BYzQIwyOHvnmnCYQgLzdr/2l56Bc2V1Xjv93JddsdEMi)**. If you want to hide this option, you can change its display by editing the `checkout-instore-custom.css` file. Check out the [How to customize VTEX Sales App guide](https://developers.vtex.com/vtex-rest-api/docs/how-to-customize-vtex-sales-app#css-customizations) for further information on how to access this file.

## Edit the `checkout-instore-custom.css` file

To customize the display of the container with the `Continue as anonymous` button, you must declare the following IDs and properties in the `checkout-instore-custom.css` file.

In the **UI display** column below, you can see how the element you can hide is rendered in VTEX Sales App’s UI. You can click on each image to enlarge it.

```json
{
"data": {
"h-0": "CSS ID selector name",
"h-1": "Description",
"h-2": "UI display",
"0-0": "`customer-anonymous-container`",
"0-1": "The ID selector you can use to style the `Continue as anonymous` button. This button enables you to place an order on VTEX Sales App without identifying the customer.",
"0-2": "![continue-as-anonymous](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/hide-anonymous-customer-option-0.png)"
},
"cols": 3,
"rows": 1
}
```

If you want to hide this element, you must use its ID selector and declare the display property with the value set as none in the `checkout-instore-custom.css` file, as exemplified below.

```css
#customer-anonymous-container {
    display: none;
}
```
