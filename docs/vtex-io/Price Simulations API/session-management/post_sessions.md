---
title: "Update Order Configuration"
slug: "post_sessions"
excerpt: "Updates the Order Configuration. You should use this route every time you edit a configuration value"
hidden: false
createdAt: "2020-09-04T15:44:57.989Z"
updatedAt: "2020-09-04T19:02:42.230Z"
---
## Request body has the following properties:
[block:parameters]
{
  "data": {
    "0-0": "public",
    "1-0": "customSessionKeys",
    "2-0": "value",
    "2-1": "string",
    "2-2": "Order Configuration criteria. This is a serialized JSON object",
    "1-1": "object",
    "1-2": "Contains every schema criteria",
    "0-1": "object",
    "0-2": "Object to register session criteria"
  },
  "cols": 3,
  "rows": 3
}
[/block]
## Request body example:

[block:code]
{
  "codes": [
    {
      "code": "{\n  public:{\n    customSessionKeys:{\n      value: \"{\"state\":\"ES\",\"orderType\":\"res\"}\"\n    }\n  }\n}",
      "language": "json"
    }
  ]
}
[/block]