---
title: "Enable an Observation field on the Checkout page"
slug: "enable-an-observation-field-on-the-checkout-page"
hidden: false
createdAt: "2022-07-21T20:01:59.423Z"
updatedAt: "2022-10-20T17:36:09.001Z"
---
You can enable an **Observation** field on the Checkout page and use it to store additional information about the order.

The data entered in this field is sent via API to the Order Management System. They populate the `openTextField` field, which can be retrieved later either in the Admin or through an Orders API call.

By default, this field is disabled. To enable it, it is necessary to insert the following rule in the CSS via the APP [Checkout UI Settings](https://developers.vtex.com/vtex-developer-docs/docs/vtex-checkout-ui-settings) or by the Admin.

`.note { display: block; }`

Checkout code configuration page view in Admin:
![Observation field](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/guides/Checkout/customization/3bdc4a3-Observation_field_17.PNG)
