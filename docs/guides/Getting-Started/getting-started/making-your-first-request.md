---
title: "Making your first request"
slug: "making-your-first-request"
excerpt: "Learn how to make your first API request using the VTEX API Reference and popular API testing tools like Postman."
hidden: false
createdAt: "2020-01-15T18:58:34.632Z"
updatedAt: "2021-03-26T14:04:17.887Z"
---

In this guide, you'll learn how to make your first API request using the [VTEX API reference](https://developers.vtex.com/docs/api-reference) and the built-in `TEST METHOD` feature.

You'll also discover how to import API specifications into popular API testing platforms such as Postman for easier testing and integration.

## Before you begin

To interact with VTEX APIs, you need to authenticate your requests. [Authentication](https://developers.vtex.com/docs/guides/getting-started-authentication) can be done via either [application keys](https://developers.vtex.com/docs/guides/getting-started-authentication#api-keys) or [user tokens](https://developers.vtex.com/docs/guides/getting-started-authentication#user-token). 

For testing using the Developer Portal `TEST METHOD` feature, you will need a valid [API key](https://developers.vtex.com/docs/guides/getting-started-authentication#api-keys), which consists of a pair of an `appKey` and `appToken`. These credentials should be associated with [roles](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) that grant you the necessary [permissions](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3) to run the desired requests. If you don't have this credential yet, refer to the [Application keys](https://help.vtex.com/en/tutorial/api-keys--4bFEmcHXgpNksoePchZyy6) guide to learn how to create them.

## Testing a request in the Developer Portal

To test an API request directly in the Developer Portal, follow these steps:

1. Go to the API reference page of the endpoint you wish to test, such as the [List orders](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders) endpoint.
2. Read the documentation and fill in the required parameters, such as headers, query parameters, and request body fields.
3. In the **Authentication** section, enter your `appKey` and `appToken` in the respective fields: `X-VTEX-API-AppKey` and `X-VTEX-API-AppToken`.
4. Hover over the `Base URL` field to see the `accountName` and `environment` fields.
5. Enter your [VTEX account name](https://help.vtex.com/en/tutorial/what-is-an-account-name--i0mIGLcg3QyEy8OCicEoC) in the `accountName` field.
10. Fill in the `environment` field. If you're unsure which environment to use, try `vtexcommercestable`.
11. Click the `TEST METHOD` button to send your request to the desired API endpoint.
12. Check the API response below the request. A successful request will return a `200 OK`, `201 Created`, or `204 No Content status`. For more information on status codes, refer to [Response status codes
](https://developers.vtex.com/docs/guides/api-response-codes).

   ![request and response](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Getting-Started/getting-started/making-your-first-request-3.png)

>⚠️ If you get a `401 - Unauthorized` response, double-check your [API key and token](https://developers.vtex.com/docs/guides/getting-started-authentication#api-keys). Ensure the values are correctly entered in the request headers, and verify that they are associated with the appropriate [roles](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) and [permissions](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3).

## Using an API testing platform

For more advanced testing, you can export the API specifications or copy example requests to integrate with tools like [Postman](https://www.postman.com/) and other API testing platforms.

### Using request examples

You can copy the generated request from the VTEX API reference and use it in Postman, or export it to other tools for further testing. For example, to import the request into Postman, copy the `cURL` request from the desired API Reference and follow the [Postman Import cURL commands](https://learning.postman.com/docs/getting-started/importing-and-exporting/importing-curl-commands/#import-a-curl-command-into-postman) guide.

1. Open the desired API Reference in the VTEX Developer Portal.
2. Fill in the request parameters as needed. The request box will automatically update with the full request.
3. In the **Language** section, select the programming language you'd like to use (Node.js, Python, or Shell).
4. Copy the example request displayed below the **Base URL** field. 

![request example](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Getting-Started/getting-started/making-your-first-request-4.png)

### Downloading API specifications

The VTEX API documentation follows the [OpenAPI 3.0 (OAS 3.0)](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md) standard, which provides a detailed description of the API's structure and behavior. You can download the API specifications as follows:

- **GitHub:** Access the [OpenAPI Schemas](https://github.com/vtex/openapi-schemas)  repository, click the `<>Code` button, and click `Download ZIP` to download the schema files.
- **API SPEC:** On the Developer Portal API Reference page, click `DOWNLOAD OPENAPI SPEC` to download the schema in JSON format. Alternatively, click `VIEW OPENAPI SPEC` to view it in your browser.
- **Postman:** On the Developer Portal API Reference page, click `DOWNLOAD POSTMAN COLLECTION` to download the collection schema in JSON format. Alternatively, click `VIEW POSTMAN COLLECTION` to view it in your browser.

Once you've downloaded the OpenAPI spec or Postman collection, you can import them into your preferred API testing tool for easy integration and testing.

