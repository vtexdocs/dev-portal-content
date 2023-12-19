---
title: "Including order variables in the transactional email template"
slug: "including-order-variables-in-the-transactional-email-template"
excerpt: "Learn how to use variables and create custom Message Center templates."
hidden: false
createdAt: "2022-09-20T14:13:22.078Z"
updatedAt: "2022-09-20T15:32:42.204Z"
---

In the **Message Center**, under the **Templates** tab, you will find the transactional email templates sent to your clients.

Some of them are fired when the status of an order changes. For example:

- **Order Confirmation**: email sent when the order was made successfully.
- **Billed Order**: email sent when the order is billed.
- **Delivery canceled**: email sent when the order is canceled.

You can customize all of the Message Center templates, and you have a series of variables at your disposal that allow you to add data to the email dynamically.

These variables are JSON properties in the **JSON Data** field and can be used in the email's HTML. Insert them into double keys using the following format: `{{variable}}`

## Example

> ⚠️ Examples of JSON Data will only appear in the templates when you develop the desired action in your store. If you have not transacted an order, a recurrence, or any other action, JSON Data will be blank.

Let's say you want to enter the carrier's name in the "product sent" email.

To do this, enter the "product sent" template and search for the' courier' property in the **JSON Data** field.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/including-order-variables-in-the-transactional-email-template-0.png)
The filled-in value for this property is just an example, but you can use it in the **HTML** field so that when the email is sent, the customer sees the carrier that is actually responsible for the order delivery.

Note that the `courier` property is inside the `package` object. Therefore, you need to enter it as follows:

`{{package.courier}}`

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/including-order-variables-in-the-transactional-email-template-1.png)

As you see, the sample value ("Transportadora Teste Courier S.A.") was inserted in the preview screen, below the **HTML** and **JSON Data** fields.

## Other order email variables

Among the properties of order JSONs that can be used as variables in transactional email templates are:

```json
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
```
