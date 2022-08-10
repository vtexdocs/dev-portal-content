---
title: "Enabling an Observation field on the Checkout page"
slug: "enabling-an-observation-field-on-the-checkout-page"
hidden: false
createdAt: "2022-07-21T20:01:59.423Z"
updatedAt: "2022-07-21T20:30:16.613Z"
---
You can enable an **Observation** field on the Checkout page and use it to store additional information about the order.

The data entered in this field is sent via API to the Order Management System. They populate the `openTextField` field, which can be retrieved later either in the Admin or through an Orders API call.

By default, this field is disabled. To enable it, it is necessary to insert the following rule in the CSS via the APP [Checkout UI Settings](https://developers.vtex.com/vtex-developer-docs/docs/vtex-checkout-ui-settings) or by the Admin.

`.note { display: block; }`

Checkout code configuration page view in Admin:
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3bdc4a3-Observation_field.PNG",
        "Observation field.PNG",
        1169,
        453,
        "#f4f8fa"
      ]
    }
  ]
}
[/block]