---
title: "Label"
slug: "vtex-log-label-overview"
hidden: true
createdAt: "2021-01-19T15:35:11.721Z"
updatedAt: "2021-01-28T17:15:44.257Z"
---
**VTEX Log** connects carriers and store owners to deliver better freight costs, and a simpler and smarter logistics operation. Our VTEX Log UI uses the following steps during a package's tracking process:

- Notification: our OMS notifies the carrier that a package is being dispatched.
- Label: tracking label is issued.
- Tracking: tracking of the package begins, and is repeated in cycles, until its final delivery.

For carriers to integrate with VTEX Log's Hub, our main system, it is necessary to develop apps in VTEX IO, and associate API routes to them. The carrier's apps integrate with the hub, that in turn are connected to other VTEX systems, fulfilling the steps cited above.

For the integration, carriers should develop VTEX IO apps for the [Notification](https://github.com/vtex-apps/carrier-hubs-examples/tree/main/carrier-notifier-example/docs), [Tracking](https://github.com/vtex-apps/carrier-hubs-examples/tree/main/carrier-tracking-example) and [Label](https://github.com/vtex-apps/label-emitter-example)  steps.

## Index

<span class="api pg-type type-post">post</span> [Notify Carrier with App](ref:notifycarrierwithapp)
<span class="api pg-type type-post">post</span> [Tracking Events with App](ref:trackingevents)
<span class="api pg-type type-post">post</span> [Emit Label with App](ref:emitlabelwithapp)
