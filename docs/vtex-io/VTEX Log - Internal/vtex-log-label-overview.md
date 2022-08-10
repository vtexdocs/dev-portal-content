---
title: "VTEX Log - Label Overview"
slug: "vtex-log-label-overview"
hidden: true
createdAt: "2021-03-17T02:43:30.670Z"
updatedAt: "2021-03-17T02:49:42.052Z"
---
VTEX Log connects carriers and store owners to deliver better freight costs, and a simpler and smarter logistics operation. Our VTEX Log UI uses the following steps during a package's tracking process:

- Notification: our OMS notifies the carrier that a package is being dispatched.
- Label: tracking label is issued.
- Tracking: tracking of the package begins, and is repeated in cycles, until its final delivery.

For carriers to integrate with VTEX Log's Hub, our main system, it is necessary to develop apps in VTEX IO, and associate API routes to them. The carrier's apps integrate with the hub, that in turn are connected to other VTEX systems, fulfilling the steps cited above.

For the integration, carriers should develop VTEX IO apps for the [Notification](https://github.com/vtex-apps/carrier-hubs-examples/tree/main/carrier-notifier-example/docs), [Label](https://github.com/vtex-apps/label-emitter-example) and [Tracking](https://github.com/vtex-apps/carrier-hubs-examples/tree/main/carrier-tracking-example) steps.

# Index 
<span class="api"><span class="pg-type type-post">post</span> [Emit Label with App](ref:emitlabelwithapp-1)