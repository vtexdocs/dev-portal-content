---
title: "Abandoned Cart Service"
slug: "vtex-abandoned-cart-service"
excerpt: "vtex.abandoned-cart-service@3.1.3"
hidden: false
createdAt: "2022-08-05T15:20:02.558Z"
updatedAt: "2022-08-05T17:17:32.967Z"
---
This app can be used to trigger abandoned cart emails.

## App installation

To use it in your account, you can run the `vtex install vtex.abandoned-cart-service` command or install it from the Admin, accessing Apps -> Apps Store -> All Apps -> Abandoned Cart Service.

## VTEX IO stores configuration

To configure the functionality and use of the abandoned cart app in VTEX IO stores, follow the steps described in [Configuration for VTEX IO stores](https://help.vtex.com/en/tutorial/setting-up-abandoned-carts--tutorials_740#configuration-for-vtex-io-stores), using the message center and trigger configuration information available below.

### Message Center information

To configure the template, access the Message Center (https://{{account}}.myvtex.com/admin/message-center/#/templates). 

To provide a preview of what the email might look like, an example JSON Data (similar to the one shown below) is available in the JSON Data field of the Message Center. This information should not be saved or used in the email template.

```json
{
  "email": "test@test.com",
  "items": [
    {
      "id": "1",
      "productName": "product1",
      "image": "https://{{account}}.vteximg.com.br/arquivos/ids/155411/image1.jpg",
      "sellingPrice": 4100,
      "quantity": "1",
      "link": "product-one"
    },
    {
      "id": "2",
      "productName": "product2",
      "image": "https://{{account}}.vteximg.com.br/arquivos/ids/155403/image2.jpg",
      "sellingPrice": 3199,
      "quantity": "1",
      "link": "product-two"
    }
  ],
  "addToCartURL": "add?sku=1&qty=1&seller=1&sku=2&qty=1&seller=1"
}
```

JSON Data field:
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/63f9ac8-JSON_Data_field.PNG",
        "JSON Data field.PNG",
        1269,
        495,
        "#f6f3f6"
      ]
    }
  ]
}
[/block]
### Trigger configuration information

During the [Trigger configuration](https://help.vtex.com/en/tutorial/setting-up-abandoned-carts--tutorials_740#trigger-configuration) procedure, specifically in Step 11 (tab **If positive**), you should select *Send an HTTP Request* and add the following information in the fields:

- **URL**: https://{{account}}.myvtex.com/_v/abandoned-cart.
- **Method**: POST.
- **Headers**:
  _ **Name**: *content-type* / **Value**: *application/json*
  _ **Name**: *accept* / **Value**: *application/json*
- Content as JSON field:

```json
{
  "email": "{!email}",
  "skuURL": "{!rclastcart}",
  "template": "abandoned-cart",
  "additionalFields": {
    // In object you can add any additional field to send in the mail
    "firstName": "{!firstName}"
  }
}
```
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f48c16d-If_positive_tab.PNG",
        "If positive tab.PNG",
        1232,
        611,
        "#f4f5f6"
      ]
    }
  ]
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "The template information in the **Content as JSON field** above must be filled in with the same template ID configured in the message center."
}
[/block]
Template information in Master data:
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6cadb54-Content_as_JSON.PNG",
        "Content as JSON.PNG",
        879,
        154,
        "#f9f3f6"
      ]
    }
  ]
}
[/block]
Template ID in Message Center:
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9886e9a-Abandoned_cart.PNG",
        "Abandoned cart.PNG",
        1002,
        235,
        "#f9f6f8"
      ]
    }
  ]
}
[/block]