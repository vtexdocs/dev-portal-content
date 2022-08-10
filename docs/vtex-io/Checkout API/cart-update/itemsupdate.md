---
title: "Update cart items"
slug: "itemsupdate"
excerpt: "With the Items Update request you can:\n\r\n\r1. Add items to the cart;\n\r2. Change the quantity of one or more items in a specific cart;\n\r3. Remove items from the cart (by changing their quantity to 0)."
hidden: false
createdAt: "2020-02-05T23:27:53.590Z"
updatedAt: "2020-02-28T14:34:06.552Z"
---
**Example of request body:** 
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"orderItems\": [\n        {\n            \"quantity\": 0,\n            \"index\": 0\n        },\n        {\n            \"seller\": \"1\",\n            \"quantity\": 1,\n            \"id\": \"38\"\n        },\n        {\n            \"seller\": \"1\",\n            \"quantity\": 2,\n            \"id\": \"35\"\n        }\n    ]\n}",
      "language": "json"
    }
  ]
}
[/block]