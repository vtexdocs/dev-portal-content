---
title: "Customize checkout confirmation pages"
slug: "customize-checkout-confirmation-pages"
hidden: false
createdAt: "2022-07-22T12:35:58.498Z"
updatedAt: "2022-10-20T17:35:49.970Z"
---
All order confirmation information at checkout is available on the Placed Orders and Order Confirmation pages. If the merchant wants to change some features on these UIs, VTEX also offers the option of customizing them.

Order Placed page example:

![Página de confirmação de pedido (Order Placed)](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/guides/Checkout/customization/d1564c7-Pgina_de_confirmao_de_pedido_Order_Placed_12.png)

In the Checkout section, located in the Admin VTEX side menu, you can access one or more websites (stores) registered in your account and perform checkout settings, including UI customization.

By clicking on the `blue gear` button of the chosen website, and selecting the **Code** tab, you will have access to a list of files and templates, where you can edit or import the HTML information. 
[block:callout]
{
  "type": "info",
  "body": "The same files shown in the Code tab are publicly available in the route https://{accountName}.myvtex.com/files/"
}
[/block]
## Edit Information

To edit Checkout confirmation UI information, access the following templates:

- **checkout-confirmation-bottom**
- **checkout-confirmation-footer**
- **checkout-confirmation-header**
- **checkout-confirmation-top**

Code tab view:
![Checkout confirmation information codes section](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/guides/Checkout/customization/ec842da-checkout_confirmation_information_codes_section_33.png)

[block:callout]
{
  "type": "warning",
  "body": "It is important to note that any customization performed on the templates will be applied to both pages at the same time (Order Placed and Order Confirmation)."
}
[/block]
Template areas on the page:
![Página de confirmação de pedido com imports de HTML](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/guides/Checkout/customization/e23bee0-Pgina_de_confirmao_de_pedido_com_imports_de_HTML_42.png)

# Customizing styles

You can also edit the Checkout Confirmation interface via CSS classes. Your styles should be added in a `<stile>` tag in one of the HTML templates loaded on the page.

CSS class areas on the page:

![Página de OrderPlaced do Checkout Confirmation com classes de customização marcadas.png](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/guides/Checkout/customization/2691dcc-Pgina_de_OrderPlaced_do_Checkout_Confirmation_com_classes_de_customizao_marcadas_50.png)

To customize the Checkout Confirmation styles, use the following classes:
[block:code]
{
  "codes": [
    {
      "code": ".cconf-alert // Confirmation alert\n.cconf-client-email // Element that carries customer's email\n.cconf-address // Card with order address\n.cconf-payment // Card with payment method\n.cconf-summary // Card with order summary\n.cconf-product-table // Table with product's orders\n.cconf-product // Table's line with order\n.cconf-continue-button // Button leading back to the store",
      "language": "css"
    }
  ]
}
[/block]
# JS customization

The page may also be changed through Javascript using the files **checkout-confirmation-custom.js** or **checkout-confirmation-custom4.js** (depending on the version of Checkout confirmation you are using, v3 or v4), which can be accessed by selecting the **Code** tab at the Admin.
