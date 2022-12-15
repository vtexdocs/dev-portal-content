---
title: "Including order variables in the transactional email template"
slug: "including-order-variables-in-the-transactional-email-template"
hidden: false
createdAt: "2022-09-20T14:13:22.078Z"
updatedAt: "2022-09-20T15:32:42.204Z"
---
In the **Message Center**, under the **Templates** tab, you will find the transactional email templates sent to your clients.

Some of them are fired when the status of an order changes. For example:
- **Order Confirmation**: email sent when the order was made successfully.
- **Billed Order**: email sent when the order is billed.
- **Delivery canceled**: email sent when the order is canceled.

You can customize all of the Message Center templates, and you have at your disposal a series of variables that allow you to dynamically add data to the email.

These variables are JSON properties that are in the **JSON Data** field and can be used in the email's HTML. Simply insert them into double keys, using the following format: `{{variable}}`

### Example
[block:callout]
{
  "type": "warning",
  "body": "Examples of JSON Data will only appear in the templates when you come up with the desired action in your store. If you have not transacted an order, a recurrence, or any other action, JSON Data will be blank."
}
[/block]
Let's say you want to enter the name of the carrier in the "product sent" email.

To do this, enter the "product sent" template and, in the **JSON Data** field, search for the `courier` property.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/670a3f7-Group_32.png",
        "Group 3(2).png",
        1204,
        656,
        "#000000"
      ]
    }
  ]
}
[/block]
The filled-in value for this property is just an example, but you can use it in the **HTML** field so that when the email is sent the customer sees the carrier that is actually responsible for the order delivery.

Note that the `courier` property is inside the `package` object. Therefore, you need to enter it as follows:

`{{package.courier}}`

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/903dd9e-Group_4.png",
        "Group 4.png",
        1202,
        989,
        "#000000"
      ]
    }
  ]
}
[/block]
As you see, the sample value ("Transportadora Teste Courier S.A.") was inserted in the preview screen, below the **HTML** and **JSON Data** fields.

### Other order email variables

Among the properties of order JSONs that can be used as variables in transactional email templates are:
[block:parameters]
{
  "data": {
    "h-0": "Properties",
    "h-1": "Definition",
    "0-0": "`courier`",
    "0-1": "Courier",
    "1-0": "`invoiceNumber`",
    "1-1": "Invoice number",
    "2-0": "`invoiceValue`",
    "2-1": "Invoice value",
    "3-0": "`invoiceUrl`",
    "3-1": "Invoice URL",
    "4-0": "`issuanceDate`",
    "4-1": "Date of issue",
    "5-0": "`trackingNumber`",
    "5-1": "Order tracking number",
    "6-0": "`invoiceKey`",
    "6-1": "Invoice access key",
    "7-0": "`trackingUrl`",
    "7-1": "Order tracking URL (informed by the carrier)"
  },
  "cols": 2,
  "rows": 8
}
[/block]