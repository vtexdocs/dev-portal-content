---
title: "Feed v3"
slug: "feed-v3"
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2020-12-03T22:06:59.718Z"
---
[block:callout]
{
  "type": "warning",
  "title": "Feed configuration and list interaction",
  "body": "To interact with the Feed configuration (filters, timeout, etc.), only the endpoints **Update Feed Configuration**, **Retrieve Feed Configuration** and **Delete Feed Configuration** should be utilized. These endpoints should **never** be used to interact with events in the Feed list.\n\nTo interact (retrieve or commit) with events of the Feed list, only the endpoints **Retrieve feed order status** and **Commit item feed order status** should be utilized. These endpoints should **never** be used to configure the Feed.\n\nMore information about Feed can be found in the articles [How the Orders Management Feed v3 works](https://help.vtex.com/en/tutorial/how-the-orders-management-feed-v3-works--5SzSKee2f666YCoWkm0eQC) and [Orders management Feed v3 setup](https://help.vtex.com/en/tutorial/orders-management-feed-v3-setup--5qDml3cQypWDRTgw69s4C1)."
}
[/block]