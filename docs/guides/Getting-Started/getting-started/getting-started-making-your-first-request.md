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
![API Reference testing feature. Try it yourself!](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Getting%20Started/getting-started/getting-started-making-your-first-request-0_13.png)

See below the expected response in our `apiexamples` store:
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Getting%20Started/getting-started/getting-started-making-your-first-request-1_16.png)

If you get a `401 - Unauthorized` as response, review the authentication steps. Make sure that the right permissions are defined in the roles and that you copied the exact appKey and appToken values into the headers of the request.

If you received a `200 OK` response, congratulations on your first successful request to VTEX APIs!   🎉

## Using Postman

Our API reference documentation is built using the [Open API 3.0 (OAS 3.0)](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md) standard. The OAS 3.0 schemas are available for [download](https://github.com/vtex/openapi-schemas) in our GitHub repository.

![Download ZIP](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Getting%20Started/getting-started/getting-started-making-your-first-request-2_26.png)

You can import our API endpoints to [Postman](https://www.postman.com/product/api-client/) by downloading the JSON schemas you are interested in and following [these instructions](https://learning.postman.com/docs/postman/collections/working-with-openAPI).
