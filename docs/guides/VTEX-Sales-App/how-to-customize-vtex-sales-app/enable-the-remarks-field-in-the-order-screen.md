---
title: "Enable the Observation field in the order screen"
slug: "enable-the-remarks-field-in-the-order-screen"
hidden: false
createdAt: "2021-08-11T19:48:00.546Z"
updatedAt: "2024-10-23T09:35:52.440Z"
---

The VTEX Sales App app allows the use of an **Observation** field, where it's possible to store additional information regarding the order.

The data entered in this field is sent via API to the Order Management System. They populate the `openTextField` field, which can be retrieved later either in the Admin or through an [Orders API](https://developers.vtex.com/docs/api-reference/orders-api#overview) call.

A common example of using the **Observation** field is the case where the store wants to receive an identification number from the sales associate who made the sale, such as the **[sales associate code](https://developers.vtex.com/vtex-rest-api/docs/sales-associate-code)**. In this case, the sales associate has to enter this number in the **Observation** field whenever closing an order.

>ℹ️ To activate the Observation field on the order screen, open a [support ticket to VTEX](https://support.vtex.com/hc/pt-br/requests) requesting this feature.
