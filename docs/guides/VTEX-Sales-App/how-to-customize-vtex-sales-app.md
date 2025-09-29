---
title: "How to customize VTEX Sales App"
slug: "how-to-customize-vtex-sales-app"
excerpt: "Learn how to customize the VTEX Sales App."
hidden: false
createdAt: "2021-08-11T17:17:40.610Z"
updatedAt: "2025-09-29T17:32:46.010Z"
---

[VTEX Sales App](https://help.vtex.com/en/tracks/vtex-sales-app-getting-started-and-setting-up--zav76TFEZlAjnyBVL5tRc) is VTEX's main product for Unified Commerce operations. It’s an app that enables your store to provide a true omnichannel experience, seamlessly integrating your online and physical channels, and placing your customers at the core of the business.

You can customize the VTEX Sales App experience according to your business needs by editing custom [JavaScript](#javascript-customizations) and [CSS](#css-customizations) files.

## JavaScript customizations

You can perform JavaScript customizations on the  `checkout-instore-custom.js` file, which you must access from the VTEX Admin home, following the steps below.

1. Access `https://{{AccountName}}.myvtex.com/admin` and follow the steps below. Remember to replace `{{AccountName}}` with your VTEX account name.
2. In the main menu, click on **Checkout**.
3. Click on the store's gear icon, as shown in the image below.
![sales-app-customizations-1](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/inStore_Customizations_-_1_-_EN.png)
4. Click on the **Code** tab and then click on the `checkout-instore-custom.js` file, which is in the **Files** list on the right side of the screen, as illustrated in the image below.
   ![sales-app-customizations-2](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/inStore_Customizations_-_2_-_EN.png)

> ℹ️️ If you want to access the `checkout-instore-custom.js` file directly, you can enter the following URL in your browser: `https://{{AccountName}}.myvtex.com/admin/portal#/sites/default/code/files/checkout-instore-custom.js`. Make sure you replace `{{AccountName}}` with your VTEX account name.

### Edit the JavaScript file

`checkout-instore-custom.js` is a JavaScript file that accepts a number of functions, variables and objects responsible for changing standard behaviors of the VTEX Sales App application.

To make any changes to the file, simply add or modify the lines of code directly in the file edit box. Check out our list of possible customizations to learn more.

Once you are done, click on the `Save` button, as shown in the image below.
![sales-app-customizations-3](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/inStore_Customizations_-_3_-_EN.png)

>⚠️ Always follow the customization instructions in this documentation and only make changes as indicated here, otherwise, VTEX Sales App may not work as expected.

## CSS customizations

For CSS customizations, you need to edit the  `checkout-instore-custom.css` file, which you can access by following the same steps as to open the [JavaScript customizations](#javascript-customizations) file. In the **Files** section, remember to open `checkout-instore-custom.css` instead.

![enable-product-recommendations-1](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/Enable_product_recommendations_-_1_-_EN.png)
Likewise, you can modify the CSS stylesheet directly in the edit box.

When you have finished, make sure you click the `Save` button.

## List of customizations

You can make the following customizations on VTEX Sales App:

- [Change VTEX Sales App language](https://developers.vtex.com/vtex-rest-api/docs/change-vtex-sales-app-language)
- [Hide anonymous customer option](https://developers.vtex.com/docs/guides/hide-anonymous-customer-option)
- [Define payment methods displayed on VTEX Sales App](https://developers.vtex.com/docs/guides/define-payment-methods-displayed-on-vtex-sales-app)
- [Enable the Observation field in the order screen](https://developers.vtex.com/vtex-rest-api/docs/enable-the-remarks-field-in-the-order-screen)
- [Enable the sales associate code](https://developers.vtex.com/vtex-rest-api/docs/sales-associate-code)
- [Enable cart transfer and capture between devices](https://developers.vtex.com/vtex-rest-api/docs/enable-cart-transfer-between-devices)
- [Force stock availability](https://developers.vtex.com/vtex-rest-api/docs/force-stock-availability)
- [Add extra text to the order summary print](https://developers.vtex.com/docs/guides/add-extra-text-to-the-order-print)
- [Hide Print order and Reprint receipt buttons](https://developers.vtex.com/docs/guides/hide-print-order-and-reprint-receipt-buttons)
- [Enable partial cancellation for Debit or Credit Direct sales](https://developers.vtex.com/docs/guides/enable-partial-cancellation)
- [Hide cancellation buttons](https://developers.vtex.com/docs/guides/hide-cancellation-buttons)
- [Allow manual prices on VTEX Sales App](https://developers.vtex.com/docs/guides/allow-manual-prices-on-vtex-sales-app)
- [Integration VTEX Sales App Local stock sale](https://developers.vtex.com/docs/guides/integration-vtex-sales-app-local-stock-sale)

You can find more information on how to set up each customization in the following guides.
