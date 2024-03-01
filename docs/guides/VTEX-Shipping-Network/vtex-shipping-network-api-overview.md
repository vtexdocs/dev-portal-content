---
title: "VTEX Shipping Network - Overview"
slug: "vtex-shipping-network-api-overview"
hidden: false
createdAt: "2021-01-19T15:24:17.429Z"
updatedAt: "2022-04-08T20:15:36.694Z"
---
**VTEX Shipping Network** connects carriers and store owners to deliver better freight costs, and a simpler and smarter logistics operation. Our VTEX Shipping Network  UI uses the following steps during a package's tracking process:

- Notification: our OMS notifies the carrier that a package is being dispatched.
- Label: tracking label is issued.
- Tracking: tracking of the package begins, and is repeated in cycles, until its final delivery.

For carriers to integrate with VTEX Shipping Network's Hub, our main system, it is necessary to develop apps in VTEX IO, and associate API routes to them. The carrier's apps integrate with the hub, that in turn are connected to other VTEX systems, fulfilling the steps cited above.

For the integration, carriers should develop VTEX IO apps only for the [Notification](https://github.com/vtex-apps/carrier-hubs-examples/tree/main/carrier-notifier-example/docs) and [Tracking](https://github.com/vtex-apps/carrier-hubs-examples/tree/main/carrier-tracking-example)  steps. The Label app will be developed internally by the VTEX Shipping Network team, our partners.

## Index

- `POST` [Notify carrier with app](https://developers.vtex.com/docs/api-reference/vtex-shipping-network-api#post-/-app_name-/v-app_version-/-account-/-workspace-/notify)
- `POST` [Tracking events with app](https://developers.vtex.com/docs/api-reference/vtex-shipping-network-api#post-/-app_name-/v-app_version-/-account-/-workspace-/tracking)
