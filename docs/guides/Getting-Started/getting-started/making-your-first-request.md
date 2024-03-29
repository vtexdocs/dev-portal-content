---
title: "Making your first request"
slug: "making-your-first-request"
excerpt: "Learn how to make an API request"
hidden: false
createdAt: "2020-01-15T18:58:34.632Z"
updatedAt: "2021-03-26T14:04:17.887Z"
---

You can use the `TEST METHOD` button in [VTEX API reference](https://developers.vtex.com/docs/api-reference) to test API requests as you read the documentaion. In this tutorial you will learn how to use this feature.

## Before you begin

Requests to VTEX APIs usually require [authentication](https://developers.vtex.com/docs/guides/getting-started-authentication), either with [application keys](https://developers.vtex.com/docs/guides/getting-started-authentication#application-keys) or [user tokens](https://developers.vtex.com/docs/guides/getting-started-authentication#user-token). The Developer Portal `TEST METHOD` requires [application keys](https://developers.vtex.com/docs/guides/getting-started-authentication#application-keys), meaning a pair of `appKey` and `appToken`.

Make sure you have a valid pair of `appKey` and `appToken` associated with [roles](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) with the necessary [permissions](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3) to execute a request. If you do not have this credential yet, learn more about how to create application keys at the [Application keys](https://help.vtex.com/en/tutorial/application-keys--2iffYzlvvz4BDMr6WGUtet) guide.

## Testing a request on Developer Portal

>⚠️ The example below is based on the [List orders endpoint](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders), but these instructions apply for any endpoint you wish to try. Feel free to follow along.

To try out an API request directly on Developer Portal, follow these steps:

1. Head to the API reference page of the endpoint you wish to test, such as the [List orders](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders) endpoint.
2. Read the documentation and fill in necessary parameters of your request, such as headers, query parameters, and request body fields.
3. Scroll to the **Authentication** section. It may be on the top of the page at the right side of your screen, or on the bottom, depending on your window size.
4. Fill in your appKey in the `X-VTEX-API-AppKey` field.
5. Fill in your appToken in the `X-VTEX-API-AppToken` field.
6. Hover your mouse cursor over the `Base URL` field to see the `accountName` and `environment`.
7. Fill in the `accountName` field with your [VTEX account name](https://help.vtex.com/en/tutorial/what-is-an-account-name--i0mIGLcg3QyEy8OCicEoC).
8. Fill in the `environment`. If you do not know which environment to use, try `vtexcommercestable`.
9. Click the `TEST METHOD` button. This will send your request to the desired API endpoint.
10. Check your response below the request.

   ![request and response](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Getting-Started/getting-started/making-your-first-request-3.png)

If you receive a `200 OK`, a `201 Created` or a `204 No Content` response, it means you sucessfully made a request to a VTEX API.

>⚠️ If you get a `401 - Unauthorized` as response, review the [application key and token](https://developers.vtex.com/docs/guides/getting-started-authentication#application-keys) and try again. Make sure that the right [permissions](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3) are defined in the [roles](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) associated with the application key and that you copied the exact key and token values into the headers of the request.

## Using an API testing platform

You can export API specification or example requests to be used with [Postman](#using-postman) or the API platform of your choice.

### Request examples

As you fill in request parameters in VTEX API reference, as described above in steps 4 to 8, the request box is automattically updated. You can find this box below the `Base URL` field described above.

![request example](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Getting-Started/getting-started/making-your-first-request-4.png)

This means you can copy this content to be imported into other software.

### Downloading API specifications

Our API reference documentation is built using the [OpenAPI 3.0 (OAS 3.0)](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md) standard.

It is possible to download the OAS 3.0 schemas in three ways, via [GitHub](#github), the [API SPEC](#api-spec) button or the [POSTMAN](#postman) button.

#### GitHub

To download the schemas from GitHub, follow the steps below:

1. Access the repository [OpenAPI Schemas](https://github.com/vtex/openapi-schemas).
2. Click the **<>Code** button.
3. Click Download ZIP.

In a short time, the file with all the repository's schemas will be available on your computer.

#### API SPEC

In each Developer Portal API Reference you will find two buttons referring to the SPEC API at the top of the page: **DOWNLOAD OPENAPI SPEC** and **VIEW OPENAPI SPEC**.

The **DOWNLOAD OPENAPI SPEC** button is used to download the collection schema file in JSON format to the computer, the **VIEW OPENAPI SPEC** button is used to view the collection schema in the browser.

#### Postman

In each Developer Portal API Reference you will also find two buttons referring to Postman at the top of the page: **DOWNLOAD POSTMAN COLLECTION** and **VIEW POSTMAN COLLECTION**.

The **DOWNLOAD POSTMAN COLLECTION** button is used to download the collection schema file in JSON format. This file can be imported into POSTMAN for testing. The **VIEW POSTMAN COLLECTION** button is used to view the collection schema in your browser.

Another option for importing a schema into Postman is to copy the `cURL` from the desired API Reference and follow the tutorial [Import cURL commands](https://learning.postman.com/docs/getting-started/importing-and-exporting/importing-curl-commands/#import-a-curl-command-into-postman).
