---
title: "Catalog Images"
slug: "vtex-catalog-images"
hidden: false
createdAt: "2022-10-21T16:59:43.420Z"
updatedAt: "2022-10-21T16:59:43.420Z"
---

The Catalog Images app provides REST and [GraphQL](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-7-consuming-data#understanding-graphql) APIs for users to save or delete catalog images on File Manager without overriding images with the same name.

## Installation

Using the [VTEX IO CLI](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-installation-and-command-reference), log in to your desired account and workspace and run the following command to install the Catalog Images app:

```
vtex install vtex.catalog-images@0.x 
```

Once the installation is confirmed, you can use the Catalog Images app's resources through [REST API](#rest-api) or [GraphQL](#graphql) as long as you follow the [authentication process](#authentication).


## Authentication

First, you must have an appKey and appToken to use as authentication headers in this application’s requests. Read [Authentication](https://developers.vtex.com/vtex-rest-api/docs/getting-started-authentication) for more information on how to obtain these credentials.

Using your appKey and appToken, make the following API request to obtain a local token, which is required by the app. Replace `{{accountName}}` with your VTEX account name and `{{my_appkey}}` and `{{my_apptoken}}` with their respective values.

**Request local token:**

```curl
curl --location --request POST 'http://api.vtexcommercestable.com.br/api/vtexid/apptoken/login?an={{accountName}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "appkey": "{{my_appkey}}",
    "apptoken": "{{my_apptoken}}"
}'
```

**Response:**

```json
{
    "authStatus": "Success",
    "token": "{{local_token}}",
    "expires": 1673305329
}
```

The `token` value you will receive as a response is required for authentication in the app's API calls, explained in the following sections.


## REST API

There are two REST API endpoints available to manage images using the Catalog Images app:

* `POST` [Save image](#save-image)
* `DELETE` [Delete image](#delete-image)


### Save image

To save an image in File Manager, use the request below. Make sure to send one image at a time and set the request body format to `multipart/form-data`.

```curl
curl --location --request POST 'https://app.io.vtex.com/vtex.catalog-images/v0/{{accountName}}/{{workspace}}/images/save/{{fileName}}' \
--header 'VtexIdclientAutCookie:  {{token}}' \
--form '=@"{{filePath}}"'
```

Make sure to replace the following values in your request:

| **Property** | **Location** | **Type** | **Description** | **Example** |
|---|---|---|---|---|
| `accountName` | Path | String | Name of the VTEX account. | mystore |
| `workspace` | Path | String | Name of the workspace where you want to upload the image. | master |
| `fileName` | Path | String | Name and extension of the image file. | product.png |
| `token` | Header (`VtexIdClientAutCookie`) | - | Local token required for authentication. | - |
| `filePath` | Request body | String | Full path of the file. | /C:/Images/product.png |

If there is already an image with the same filename given, the response will be `Conflict (409)` with the conflicted image URL in the response body.

Otherwise, the response will be `OK (200)` with the `id`, `slug`, and `fullUrl` in the response body, as follows:

**Response body example (200 OK):**
```json
{
    "id": "special-offer.png",
    "slug": "/assets/vtex.catalog-images/products/special-offer___782206cd73597a717ed67eba399167a6.png",
    "fullUrl": "https://myvtexaccountname.vtexassets.com/assets/vtex.catalog-images/products/special-offer___782206cd73597a717ed67eba399167a6.png"
}
```


### Delete image

The following REST API route allows you to delete a Catalog image in File Manager:


```curl
curl --location -g --request DELETE 'https://app.io.vtex.com/vtex.catalog-images/v0/{{accountName}}/{{workspace}}/images/save/{{fileName}}' \
--header 'VtexIdclientAutCookie: {{token}}'
```

Replace the values as explained below: 

| **Property** | **Location** | **Type** | **Description** | **Example** |
|---|---|---|---|---|
| `accountName` | Path | String | Name of the VTEX account. | mystore |
| `workspace` | Path | String | Name of the workspace where you want to upload the image. | master |
| `fileName` | Path | String | Name and extension of the image file. | product.png |
| `token` | Header (`VtexIdClientAutCookie`) | - | Local token required for authentication. | - |

If there is already an image with the same `fileName` given, the response will be `Conflict (409)` with the conflicted image URL in the response body.


If the image exists and is successfully deleted, the response will be an empty body with status code `OK (200)`. If the image does not exist, the response will be `Not Found (404)`.


## GraphQL API

The following mutations are available for Catalog images using the app’s GraphQL API:

* [saveImage](#saveimage)
* [deleteImage](#deleteimage)


### saveImage

Use the following mutation to save an image on File Manager using GraphQL:

**Mutation:**
```graphql
saveImage(filename: String!, file: Upload!){
  id
  slug
  fullUrl
}
```


**Response body example (200 OK):**
```json
{
    "id": "special-offer.png",
    "slug": "/assets/vtex.catalog-images/products/special-offer___782206cd73597a717ed67eba399167a6.png",
    "fullUrl": "https://myvtexaccountname.vtexassets.com/assets/vtex.catalog-images/products/special-offer___782206cd73597a717ed67eba399167a6.png"
}
```


If there is already an image with the same name registered on File Manager, the response will contain an array of errors, including `CONFLICT_FILE_ERROR`.

**Response body example (409 Conflict):**
```json
"errors": [
    {
      [...]
      "extensions": {
        "code": "CONFLICT_FILE_ERROR",
        "data": {
          "statusCode": 409,
          "file": "https://sandboxintegracao.vtexassets.com/assets/vtex.catalog-images/src/car22___aabd8ae86160533e7090c024ac004bc6.jpg"
        }
      },
      [...]
    }
]
```


### deleteImage

Use the following mutation to delete an image on File Manager using GraphQL:

**Mutation:**
```graphql
deleteImage(filename: String!){
  statusCode
}
```


**Response body example (200 OK):**
```json
{
    "statusCode": "Ok"
}
```

If the image does not exist, the `statusCode` value in the response will be `NotFound`.