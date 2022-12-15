---
title: "Product Instant Publishing"
slug: "instantpublishing"
excerpt: "This endpoint will index a specific product immediately"
hidden: true
createdAt: "2021-01-14T20:48:13.155Z"
updatedAt: "2022-08-22T17:13:35.272Z"
---
[block:callout]
{
  "type": "danger",
  "body": "This API is deprecated.",
  "title": "Deprecated"
}
[/block]
## Response body object has the following properties

| Attribute              | Type    | Description                                                                           |
| ---------------------- | ------- | ------------------------------------------------------------------------------------- |
| `message` | string | Message informing either the error or the success |
| `currentNumberOfPublishes` | integer | Total number of publishes made in the last 24 hours |
| `maxNumberOfPublishes` | integer | Maximum number of publishes you are allowed to make in a 24 hours span |
| `level` | integer | level of indexation. Where `0` it’s successfully indexed, `1` it’s partially indexed and `2` is not indexed. |

## Response body example
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"message\": \"Product indexed successfully\",\n    \"currentNumberOfPublishes\": 1,\n    \"maxNumberOfPublishes\": 20,\n    \"level\": 0\n}",
      "language": "json"
    }
  ]
}
[/block]
If published with success, the response will have a status code `200 OK`, with the previous response body.
[block:callout]
{
  "type": "warning",
  "body": "Depending on the product, there may be errors during some post-indexation processes. Either way, the main product requested is indexed. The API will return a status code `417 - Expectation Failed`, with the message “Product partially indexed” and a `\"level\": 1` indexation.",
  "title": "Attention"
}
[/block]

[block:api-header]
{
  "title": "Prerequisites"
}
[/block]
To use the Product Instant Publishing API, you need to install the `vtex.instant-publishing` app to a workspace. After installed, you must have the `Instant Publish` resource on your access profile. Only afterwards all this setup, you can use this API.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/63f7b0d-Screenshot_32.png",
        "Screenshot_32.png",
        1446,
        798,
        "#e8e8e8"
      ]
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Error mapping"
}
[/block]
**Product is not active:**
`400 -  Bad Request`
Message: "Product with id ‘{{productId}}’ is not active"


**Product not found:**
`400 - Bad Request`
Message: "Product with id ‘{{productId}}’ not found"


**Product API limit reached:**
`429 - Too many requests`
Message: "Too many requests to ‘/api/catalog/pvt/product/{{productId}}"

**Unexpected error:**
`500 - Internal Server Error`
Message: StackTrace from the error

**Franchise account indexing:**
`400 - Bad Request`
Message: “Cannot index a franchise account”

**Maximum number of publishes reached:**
`403 - Forbidden`
Message: “Max number of 20 publishes reached”


[block:api-header]
{
  "title": "Limits and Auditing the API"
}
[/block]
The API is limited by **20 success **requests in a span of 24 hours by store, and this value is not configurable. Error requests does not count into the limit.

*Example*: 20 requests were made, but only 19 were successful. Therefore, you still have 1 success request available to publish a product.


A API has an internal auditing, containing the following logs:
- Account name
- VTEX IO Workspace 
- Product Id
- User
- Product status
- App version
- Time of the request

[block:api-header]
{
  "title": "API usage tips"
}
[/block]
We still haven’t measured the impact of the several cache layers between the search system and final product page. To avoid unnecessary caching and therefore delaying the changes to be reflected, we suggest to not enter the product page close to its publishing.