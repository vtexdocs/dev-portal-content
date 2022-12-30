---
title: "How to customize inStore"
slug: "how-to-customize-instore"
hidden: false
createdAt: "2021-08-11T17:17:40.610Z"
updatedAt: "2022-02-24T20:32:46.010Z"
---

[inStore](https://help.vtex.com/en/tracks/instore-getting-started-and-setting-up--zav76TFEZlAjnyBVL5tRc) is VTEX's main product for Unified Commerce operations. It’s an app that enables your store to provide a true omnichannel experience, seamlessly integrating your online and physical channels, and placing your customers at the business core.

You can customize the inStore experience according to your business needs by editing custom [JavaScript](#javascript-customizations) and [CSS](#css-customizations) files.

## JavaScript customizations

You can perform JavaScript customizations on the  `checkout-instore-custom.js` file, which you must access from the VTEX Admin home, following the steps below.

1. Access `https://{{AccountName}}.myvtex.com/admin` and following the steps below. Remember to replace `{{AccountName}}` with your VTEX account name.
2. In the main menu, click on **Checkout**.
3. Click on the store's gear symbol, as shown in the image below.
   ![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX%20inStore/e9fb85c-20._inStore_Customizations_-_1_-_EN_19.png)
4. Click on the **Code** tab and finally on the `checkout-instore-custom.js` file, which is in the **Files** list on the right-hand side of the screen, as illustrated in the image below.
   ![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX%20inStore/321ddf2-20._inStore_Customizations_-_2_-_EN_21.png)

\[block:callout]
{
"type": "info",
"body": "If you want to access the `checkout-instore-custom.js` file directly, you can enter the following URL in your browser: `https://{{AccountName}}.myvtex.com/admin/portal#/sites/default/code/files/checkout-instore-custom.js`. Make sure you replace `{{AccountName}}` with your VTEX account name.",
"title": "Useful tip"
}
\[/block]

### Edit the JavaScript file

`checkout-instore-custom.js` is a JavaScript file that accepts a number of functions, variables and objects responsible for changing standard behaviors of the inStore application.

To make any changes to the file, simply add or modify the lines of code directly in the file edit box. Check out our list of possible customizations to learn more.

Once you are done, click on the `Save` button, as shown in the image below.
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX%20inStore/e941660-20._inStore_Customizations_-_3_-_EN_37.png)

\[block:callout]
{
"type": "warning",
"body": "Always follow the customization instructions in this documentation and only make changes as indicated here, or inStore may not work as expected."
}
\[/block]

## CSS customizations

For CSS customizations, you need to edit the  `checkout-instore-custom.css` file, which you can access by following the same steps as to open the [JavaScript customizations](#javascript-customizations) file. In the **Files** section, just remember to open `checkout-instore-custom.css` instead.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX%20inStore/b95cbba-25._Enable_product_recommendations_-_1_-_EN_49.png_h_250)
Likewise, you can modify the CSS style sheet directly in the edit box.

When you have finished, make sure you click the `Save` button.

## List of customizations

You can make the following customizations on inStore:

- [Customize inStore login options](https://developers.vtex.com/vtex-rest-api/docs/customize-instore-login-options)
- [Change inStore language](https://developers.vtex.com/vtex-rest-api/docs/change-instore-language)
- [Enable the Observation field in the order screen](https://developers.vtex.com/vtex-rest-api/docs/enable-the-remarks-field-in-the-order-screen)
- [Enable the sales associate code](https://developers.vtex.com/vtex-rest-api/docs/sales-associate-code)
- [Enable cart transfer and capture between devices](https://developers.vtex.com/vtex-rest-api/docs/enable-cart-transfer-between-devices)
- [Enable order filter by sales associate](https://developers.vtex.com/vtex-rest-api/docs/enable-order-filter-by-sales-associate)
- [Force stock availability](https://developers.vtex.com/vtex-rest-api/docs/force-stock-availability)
- [Set up the order summary printing](https://developers.vtex.com/vtex-rest-api/docs/set-up-the-order-summary-printing)
- [Define payment methods displayed on inStore](https://developers.vtex.com/vtex-rest-api/docs/define-payment-methods-displayed-on-instore)

You can find more information on how to set up each customization on the following guides.
