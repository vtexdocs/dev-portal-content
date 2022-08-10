---
title: "VTEX Tracking - Overview"
slug: "vtex-tracking-overview"
hidden: false
createdAt: "2020-11-09T20:58:06.373Z"
updatedAt: "2022-02-02T17:40:13.102Z"
---
This API is only available in our Brazilian operation, for VTEX Tracking customers. The APIs are used for consulting and registering services in the VTEX Tracking system.
[block:callout]
{
  "type": "info",
  "body": "We have unified our VTEX Tracking APIs into a single version, so it's no longer necessary to specify the version on the URL. We have also translated all paths to english. Check out our [changelog ](https://developers.vtex.com/vtex-developer-docs/changelog/vtex-tracking-api-changes-in-all-paths) to know more about the changes.\n\nThe previous paths were not deprecated, and are still being maintained by the VTEX Tracking team. If your business' integration was built with the previous `v1` and `v1.1` endpoints, it will still run smoothly. No changes in your integrations should be done during critical periods. We will communicate any updates, and deprecations of endpoints in the future.",
  "title": "Changes in VTEX Tracking endpoints"
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "- We recommend that customers call our GET endpoints only once in every 6 hours. \n- We do **not** recommend, and consider as a bad practice, to retrieve data from the same endpoint more than once during a 6-hour window. This represents a major load to our API that will slow down the overall usage of our systems.",
  "title": "Throttling warning"
}
[/block]
# Index

## Authentication
*Acquire the mandatory authentication to access the VTEX Tracking endpoints.*
<span class="api"><span class="pg-type type-post">post</span> [Asynchronous Login](https://developers.vtex.com/vtex-developer-docs/reference/vtex-tracking-api-authentication)   




## Delivery Services
*Operate all VTEX Tracking Delivery Services funcionalities*
<span class="api"><span class="pg-type type-post">post</span> [Post Delivery Service](https://developers.vtex.com/vtex-rest-api/reference/post-delivery-service) 
<span class="api"><span class="pg-type type-get">get</span> [Get Delivery Services List](https://developers.vtex.com/vtex-rest-api/reference/get-delivery-service-list) 
<span class="api"><span class="pg-type type-get">get</span> [Get Delivery Service by ID](https://developers.vtex.com/vtex-rest-api/reference/get-delivery-service-by-id) 
<span class="api"><span class="pg-type type-post">post</span> [Post Delivery Service With Route Scheduling](https://developers.vtex.com/vtex-rest-api/reference/post-delivery-service-route-scheduling) 
<span class="api"><span class="pg-type type-get">get</span> [Get Delivery Services List by Route](https://developers.vtex.com/vtex-rest-api/reference/get-delivery-service-list-by-route) 
<span class="api"><span class="pg-type type-get">get</span> [Get Delivery Service by Invoice](https://developers.vtex.com/vtex-rest-api/reference/get-delivery-service-list-by-invoice)