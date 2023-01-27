---
title: "VTEX Tracking - Overview"
slug: "vtex-tracking-overview"
hidden: false
createdAt: "2020-11-09T20:58:06.373Z"
updatedAt: "2022-02-02T17:40:13.102Z"
---

This API is only available in our Brazilian operation, for VTEX Tracking customers. The APIs are used for consulting and registering services in the VTEX Tracking system.

> We have unified our VTEX Tracking APIs into a single version, so it's no longer necessary to specify the version on the URL. We have also translated all paths to english. Check out our [release notes](https://developers.vtex.com/updates/release-notes/vtex-tracking-api-changes-in-all-paths) to know more about the changes.\n\nThe previous paths were not deprecated, and are still being maintained by the VTEX Tracking team. If your business' integration was built with the previous `v1` and `v1.1` endpoints, it will still run smoothly. No changes in your integrations should be done during critical periods. We will communicate any updates, and deprecations of endpoints in the future.

>⚠️ We recommend that customers call our GET endpoints only once in every 6 hours. We do not recommend, and consider as a bad practice, to retrieve data from the same endpoint more than once during a 6-hour window. This represents a major load to our API that will slow down the overall usage of our systems.

## Index

### Authentication

Acquire the mandatory authentication to access the VTEX Tracking endpoints.

`POST` [Asynchronous Login](https://developers.vtex.com/docs/api-reference/tracking#post-/auth)

### Delivery Services

Operate all VTEX Tracking Delivery Services funcionalities.

`PUT` [Remove Packing List](https://developers.vtex.com/docs/api-reference/tracking#put-/services)
`POST` [Post Delivery Service](https://developers.vtex.com/docs/api-reference/tracking#post-/services)
`GET` [Get Delivery Services List](https://developers.vtex.com/docs/api-reference/tracking#get-/services)
`GET` [Get Delivery Service by ID](https://developers.vtex.com/docs/api-reference/tracking#get-/services/-idDeliveryService-)
`POST` [Post Delivery Service With Route Scheduling](https://developers.vtex.com/docs/api-reference/tracking#post-/services/routes)
`GET` [Get Delivery Services List by Route](https://developers.vtex.com/docs/api-reference/tracking#get-/services/routes)
`GET` [Get Delivery Service by Invoice](https://developers.vtex.com/docs/api-reference/tracking#get-/services/invoice)