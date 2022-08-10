---
title: "Making your first request"
slug: "getting-started-making-your-first-request"
excerpt: "Learn how to make an API request"
hidden: false
createdAt: "2020-01-15T18:58:34.632Z"
updatedAt: "2021-03-26T14:04:17.887Z"
---
Let's test a simple `GET` call to see if you receive a `200 OK` response. 

Check out the following example, where we use the **Try It** feature in the API Reference of these Developer Docs to try a GET Category request. The `{{appKey}}` and `{{appToken}}` in the image should be replaced by your own appKey and appToken.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/aab36e2-TryIt.png",
        "TryIt.png",
        1506,
        730,
        "#e3e1e1"
      ],
      "caption": "API Reference testing feature. Try it yourself!"
    }
  ]
}
[/block]
See below the expected response in our `apiexamples` store:
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/caf0563-6iodj1V.png",
        "6iodj1V.png",
        1034,
        493,
        "#52555a"
      ],
      "caption": "Sample response object received from a recently created account"
    }
  ]
}
[/block]
If you get a `401 - Unauthorized` as response, review the authentication steps. Make sure that the right permissions are defined in the roles and that you copied the exact appKey and appToken values into the headers of the request.

If you received a `200 OK` response, congratulations on your first successful request to VTEX APIs!   :tada:

## Using Postman
Our API reference documentation is built using the <a href="https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md" target="_blank">Open API 3.0 (OAS 3.0)</a> standard. The OAS 3.0 schemas are available for <a href="https://github.com/vtex/openapi-schemas" target="_blank">download</a> in our GitHub repository.

![Download ZIP](https://i.imgur.com/BT9IRsX.png)

You can import our API endpoints to <a href="https://www.postman.com/product/api-client/">Postman</a> by downloading the JSON schemas you are interested in and following <a href="https://learning.postman.com/docs/postman/collections/working-with-openAPI" target="_blank">these instructions</a>.