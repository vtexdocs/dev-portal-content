---
title: "Retrieve feed items"
slug: "getfeedorderstatus1"
excerpt: "Retrieve items from feed queue."
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2021-11-30T22:54:22.082Z"
---
The event will be removed if the message "send retry" is equal to, or greater than the maximum retention period.
[block:callout]
{
  "type": "warning",
  "body": "This API will return **404 Not Found** if there is no [Feed Configuration](https://developers.vtex.com/vtex-rest-api/reference/feed-v3#feedconfiguration) available for the given X-VTEX-API-AppKey.",
  "title": "Feed Configuration is required"
}
[/block]