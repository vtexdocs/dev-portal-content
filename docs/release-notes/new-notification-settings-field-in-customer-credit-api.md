---
slug: "new-notification-settings-field-in-customer-credit-api"
title: "New notificationsSettings field in Customer Credit API"
createdAt: 2020-05-06T23:10:14.202Z
hidden: false
type: "improved"
---

You can now schedule a timeline in [Customer Credit API](https://developers.vtex.com/reference/customer-credit-api-overview) for pre-payment and post-payment e-mail notifications. Up to three triggers can be set for each timeline using the `notificationsSettings` field of the [[PUT] Create or change store configuration](https://developers.vtex.com/reference/store-configuration#createorchangestoreconfiguration) endpoint.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/db65442-Prepayment-PostPayment-Timeline.png",
        "Prepayment-PostPayment-Timeline.png",
        1666,
        1260,
        "#f4f4f5"
      ]
    }
  ]
}
[/block]
For now the field can only be edited using the [Customer Credit API](https://developers.vtex.com/reference/customer-credit-api-overview), but it will be available shortly in the Admin panel.