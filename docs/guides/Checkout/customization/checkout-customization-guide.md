---
title: "Checkout customization guide"
slug: "checkout-customization-guide"
hidden: false
createdAt: "2022-05-20T00:39:53.375Z"
updatedAt: "2022-06-20T17:35:43.313Z"
---

All VTEX stores have a native Checkout UI available from the start of their operations on the platform. However, if the merchant wants to modify certain features of this UI, VTEX also offers the option to customize Checkout. This functionality can be performed in two ways: by VTEX Admin or Apps.

## Customizing Checkout UI - VTEX Admin

In the Checkout section, located in the VTEX Admin side menu, you can access one or more websites (stores) registered in your account and perform checkout settings, including UI customization.

By clicking the `blue gear` button on the chosen website and selecting the **Code** tab, you will see a list of files and templates where you can edit or import HTML.

> ℹ️ The same files shown in the Code tab are publicly available in the route `https://{accountName}.myvtex.com/files/`.

### Editing information

To edit Checkout UI information, access the following files/templates:

- HTML Header: *template* *checkout-header*
- HTML Footer: *template* *checkout-footer*
- CSS: *file checkout6-custom.css*
- JS: *file checkout6-custom.js*

>⚠️ You can't edit information in the HTML body of the page.

### Importing information

You can import additional information and files by clicking the `New` button, then selecting **File upload**, located in the **Code** tab.

>⚠️ Importing information is not recommended for CSS files and is not supported for JS files. Using non-standard files can cause side effects, such as breaking your store or disrupting sales.

For more information, see [configuring template in the SmartCheckout](https://help.vtex.com/en/tutorial/configurar-template-no-smartcheckout--frequentlyAskedQuestions_599#).

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/checkout-customization-guide-0.PNG)

### CMS Portal (Legacy)

In stores using the CMS Portal (Legacy), files are managed by the **Files Manager**. The CSS and JS files are located at the route `https://{accountName}.myvtex.com/arquivos/` and are named *checkout-custom.css* and *checkout-custom.js*, respectively.

>⚠️ Modifications made to CMS Portal (Legacy) files will be applied to all websites (stores) of your account at the same time.

For more information, see [View the contents of the store's CSS files](https://help.vtex.com/en/tutorial/view-the-contents-of-the-stores-css-files--U5v7DXpRSee86uqiKQUQi#).

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/checkout-customization-guide-1.PNG)

> ❗ VTEX doesn't support the use of custom scripts and isn't responsible for any damages that their use may cause. Using custom scripts can break your store or stop sales.

## Customizing Checkout UI - Apps

In addition to VTEX Admin, you can use two apps to customize your store’s Checkout UI: *Checkout UI Settings* and *Checkout UI Custom*.

>⚠️ If you want to use the Checkout UI Settings app, any script changes made through it will override HTML, CSS, and JS information made through [VTEX Admin](#customizing-checkout-ui-vtex-admin).

### Checkout UI Settings app

The Checkout UI Settings app allows you to customize your store's Checkout UI through the terminal and the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-install). Compared to the [VTEX Admin](https://developers.vtex.com/docs/guides/vtex-checkout-ui-settings) method, this app provides:

- Perform A/B testing
- Easily track all changes made to the UI (through app versions)
- Apply quick rollbacks to a previous version, if needed.

>⚠️ We highly recommend that you have prior experience using IO apps (VTEX Store Framework) before choosing this checkout UI configuration option.

For more information, see the [Checkout UI Settings Guide](https://developers.vtex.com/docs/guides/vtex-checkout-ui-settings).

### Checkout UI Custom app

The Checkout UI Custom app can be used to quickly apply predefined customization options (for example, show item unit prices, text sizes, and colors) that have already been approved by VTEX. For more information, see the [Checkout UI Custom Guide](https://developers.vtex.com/docs/guides/vtex-checkout-ui-custom-v0).

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/checkout-customization-guide-2.PNG)
