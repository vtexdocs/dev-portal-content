---
slug: "vtex-tracking-api-changes-in-all-paths"
title: "VTEX Tracking API: changes in all paths"
createdAt: 2020-11-10T12:00:00.000Z
hidden: true
type: "improved"
---

![Commerce APIs](https://img.shields.io/badge/-Commerce%20APIs-brightgreen)

We have unified our VTEX Tracking APIs into a single version, so it's no longer necessary to specify the version on the URL. We have also translated all paths to english.

Previously, users could access `VTEX Tracking v1` and `VTEX Tracking v1.1` endpoints. The only difference between the two versions, was that `v1.1` retrieved a `pictures` object in delivery service responses. We have now unified both versions, and translated paths to english.

No endpoints were deleted, and no attributes were changed. Check out the updated documentation for the [unified VTEX Tracking APIs](https://developers.vtex.com/vtex-developer-docs/reference/authentication).
[block:callout]
{
  "type": "warning",
  "body": "The previous paths were not deprecated, and are still being maintained by the VTEX Tracking team. If your business' integration was built with the previous `v1` and `v1.1` endpoints, it will still run smoothly. No changes in your integrations should be done during the Black Friday period. We will communicate any updates, and deprecations of endpoints in the future.",
  "title": "All versions are still available"
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Previous path - v1",
    "h-1": "Previous Path - v1.1",
    "h-2": "Current Path",
    "0-0": "<span class=\"api\"><span class=\"pg-type type-post\">post</span> /receiver/v1/auth",
    "1-0": "<span class=\"api\"><span class=\"pg-type type-get\">get</span><span class=\"api\"> <span class=\"pg-type type-put\">put</span><span class=\"api\"><span class=\"pg-type type-post\">post</span>/receiver/v1/servicos",
    "2-0": "<span class=\"api\"><span class=\"pg-type type-get\">get</span> /receiver/v1/servicos/{{idDeliveryService}}",
    "3-0": "<span class=\"api\"><span class=\"pg-type type-get\">get</span> /receiver/v1/servicos/nf",
    "4-0": "<span class=\"api\"><span class=\"pg-type type-get\">get</span><span class=\"api\"><span class=\"pg-type type-post\">post</span> /receiver/v1/servicos/roteirizado",
    "0-1": "<span class=\"api\"><span class=\"pg-type type-post\">post</span> /receiver/v1.1/auth",
    "1-1": "<span class=\"api\"><span class=\"pg-type type-get\">get</span><span class=\"api\"><span class=\"pg-type type-put\">put</span> <span class=\"api\"><span class=\"pg-type type-post\">post</span>/receiver/v1.1/servicos",
    "0-2": "<span class=\"api\"><span class=\"pg-type type-post\">post</span> **/receiver/auth**",
    "1-2": "<span class=\"api\"><span class=\"pg-type type-get\">get</span><span class=\"api\"><span class=\"pg-type type-put\">put</span> <span class=\"api\"><span class=\"pg-type type-post\">post</span>**/receiver/services**",
    "2-2": "<span class=\"api\"><span class=\"pg-type type-get\">get</span> **/receiver/services/{{idDeliveryService}}**",
    "3-2": "<span class=\"api\"><span class=\"pg-type type-get\">get</span> **/receiver/services/invoice**",
    "4-2": "<span class=\"api\"><span class=\"pg-type type-get\">get</span><span class=\"api\"><span class=\"pg-type type-post\">post</span> **/receiver/services/routes**",
    "2-1": "<span class=\"api\"><span class=\"pg-type type-get\">get</span> /receiver/v1.1/servicos/{{idDeliveryService}}",
    "3-1": "<span class=\"api\"><span class=\"pg-type type-get\">get</span> /receiver/v1.1/servicos/nf",
    "4-1": "<span class=\"api\"><span class=\"pg-type type-get\">get</span><span class=\"api\"><span class=\"pg-type type-post\">post</span> /receiver/v1.1/servicos/roteirizado",
    "5-0": "<span class=\"api\"><span class=\"pg-type type-get\">get</span> \n <span class=\"api\"><span class=\"pg-type type-post\">post</span> /receiver/v1/servicos/roteirizacao",
    "5-1": "<span class=\"api\"><span class=\"pg-type type-get\">get</span> \n <span class=\"api\"><span class=\"pg-type type-post\">post</span> /receiver/v1.1/servicos/roteirizacao",
    "5-2": "<span class=\"api\"><span class=\"pg-type type-get\">get</span> \n <span class=\"api\"><span class=\"pg-type type-post\">post</span> **/receiver/services/routes**"
  },
  "cols": 3,
  "rows": 6
}
[/block]
