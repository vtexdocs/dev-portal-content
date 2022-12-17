---
title: "Checkout customization guide"
slug: "checkout-customization-guide"
hidden: false
createdAt: "2022-05-20T00:39:53.375Z"
updatedAt: "2022-06-20T17:35:43.313Z"
---
All VTEX stores have a native Checkout UI ready to be used from the beginning of their operations on the platform. However, if the merchant wants to change some features on this UI, VTEX also offers the option of customizing the Checkout. This functionality can be performed in two ways: by Admin VTEX or Apps.

## Customizing Checkout UI - Admin VTEX

In the Checkout section, located in the Admin VTEX side menu, you can access one or more websites (stores) registered in your account and perform checkout settings, including UI customization.

By clicking on the `blue gear` button of the chosen website, and selecting the **Code** tab, you will have access to a list of files and templates, where you can edit or import the HTML information. 
[block:callout]
{
  "type": "info",
  "body": "The same files shown in the Code tab are publicly available in the route https://{accountName}.myvtex.com/files/"
}
[/block]

### Edit Information

To edit Checkout UI information, access the following files/templates:

- HTML Header: _template_ _checkout-header_
- HTML Footer: _template_ _checkout-footer_
- CSS: _file checkout6-custom.css_
- JS: _file checkout6-custom.js_

[block:callout]
{
  "type": "warning",
  "body": "It is not possible to edit information in HTML body of the page."
}
[/block]
### Import Information

You can import additional information and files by clicking on the `New` button and then on **File upload**, located in the **Code** tab. 
[block:callout]
{
  "type": "warning",
  "body": "The action of importing information is not recommended for CSS files and it is prohibited for JS files. Using non-standard files can cause side effects, such as your store breaking or stopping your sales."
}
[/block]
For more information, access [configuring template in the SmartCheckout](https://help.vtex.com/en/tutorial/configurar-template-no-smartcheckout--frequentlyAskedQuestions_599#).

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/guides/Checkout/customization/a8afebf-Code_page_47.PNG)

### Legacy CMS

In stores using the Legacy CMS, files are managed by the **Files Manager**. The CMS and JS files are located in the route https://{accountName}.myvtex.com/arquivos/, and named respectively as _checkout-custom.css_ and _checkout-custom.js_.
[block:callout]
{
  "type": "warning",
  "body": "Modifications made to Legacy CMS files will be applied to all websites (stores) of your account at the same time."
}
[/block]
For more information, access [View the contents of the store's CSS files](https://help.vtex.com/en/tutorial/view-the-contents-of-the-stores-css-files--U5v7DXpRSee86uqiKQUQi#).

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/guides/Checkout/customization/f62ee29-CMS_File_manager_60.PNG)

[block:callout]
{
  "type": "danger",
  "body": "VTEX does not support the use of custom scripts and is not responsible for any damages that their use may cause. Using custom scripts can break your store or stop sales."
}
[/block]
## Customizing Checkout UI - Apps

In addition to Admin VTEX, you can use two apps to customize your store’s Checkout UI: _Checkout UI Settings_ and _Checkout UI Custom_.
[block:callout]
{
  "type": "warning",
  "body": "If you want to use the Checkout UI Settings app, any script changes made through it will override HTML, CSS, and JS information made through [Admin VTEX](https://developers.vtex.com/vtex-developer-docs/docs/vtex-checkout-ui-settings)."
}
[/block]
### Checkout UI Settings app

The Checkout UI Settings app allows you to customize your store's through the terminal and the [VTEX IO Toolbelt](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-install). This app, if compared to the [Admin VTEX](https://docs.google.com/document/d/15oDUQtf4Tywt0aLhp6fhQsuw7P-ieI6WS4Qz1wJJEWY/edit#heading=h.29eil9ypzyao) method, offers the possibility to:

- Perform A/B Testing 
- Easily track all changes made to the UI (through app versions)
- Apply quick rollbacks to a previous version, if needed. 

[block:callout]
{
  "type": "warning",
  "body": "It is highly recommended that you have prior experience using IO apps (VTEX Store Framework) before choosing this checkout UI configuration option."
}
[/block]
For more information, access the [Checkout UI Settings Guide](https://developers.vtex.com/vtex-developer-docs/docs/vtex-checkout-ui-settings).

### Checkout UI Custom app

The Checkout UI Custom app can be used to quickly apply pre-defined customization options (e.g. show items unit price, text size, colors) that have already been approved by VTEX. For more information, access the [Checkout UI Custom Guide](https://developers.vtex.com/vtex-developer-docs/docs/vtex-checkout-ui-custom-v0). 

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/guides/Checkout/customization/b49efd2-Checkout_UI_Custom_view_97.PNG)
