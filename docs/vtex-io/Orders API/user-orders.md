---
title: "User Orders"
slug: "user-orders"
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2020-08-04T16:55:17.580Z"
---
[block:callout]
{
  "type": "warning",
  "body": "Only users authenticated to (or impersonating) the `clientEmail` account with a valid VTEX ID cookie (`VtexIdclientAutCookie_{{store}}`) are authorized to use these endpoints. \n\nTo list orders made by a specific user, use the [[GET] List Orders](https://developers.vtex.com/reference/orders#listorders) endpoint as seen below:\n\n`/api/oms/pvt/orders?f_creationDate=creationDate:[2020-01-01T00:00:00.000Z TO 2020-12-31T23:59:59.999Z]&q=user@example.com`",
  "title": ""
}
[/block]