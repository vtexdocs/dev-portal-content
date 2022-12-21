---
slug: "new-notification-settings-field-in-customer-credit-api"
title: "New notificationsSettings field in Customer Credit API"
createdAt: 2020-05-06T23:10:14.202Z
hidden: false
type: "improved"
---

![Commerce APIs](https://img.shields.io/badge/-Commerce%20APIs-brightgreen)

You can now schedule a timeline in [Customer Credit API](https://developers.vtex.com/reference/customer-credit-api-overview) for pre-payment and post-payment e-mail notifications. Up to three triggers can be set for each timeline using the `notificationsSettings` field of the [\[PUT\] Create or change store configuration](https://developers.vtex.com/reference/store-configuration#createorchangestoreconfiguration) endpoint.
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/release-notes/db65442-Prepayment-PostPayment-Timeline_10.png)
For now the field can only be edited using the [Customer Credit API](https://developers.vtex.com/reference/customer-credit-api-overview), but it will be available shortly in the Admin panel.
