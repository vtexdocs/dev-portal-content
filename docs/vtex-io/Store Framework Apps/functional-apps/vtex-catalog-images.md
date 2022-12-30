---
title: "Catalog Images app"
slug: "vtex-catalog-images"
excerpt: "vtex.catalog-images@0.3.0"
hidden: false
createdAt: "2022-10-21T16:59:43.420Z"
updatedAt: "2022-10-21T16:59:43.420Z"
---
The Catalog Images app provides REST and [GraphQL](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-7-consuming-data#understanding-graphql) APIs for users to save or delete catalog images on File Manager without overriding images with the same name.

## Prerequisites

You must have an appKey and appToken to use as authentication headers in this application’s requests. Read [Authentication](https://developers.vtex.com/vtex-rest-api/docs/getting-started-authentication) for more information on how to obtain these credentials.


## Installation

Using the [VTEX IO CLI](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-installation-and-command-reference), log in to your desired account and workspace and run the following command:

```
vtex install vtex.catalog-images@0.x 
```

Once the installation is confirmed, you can use the Catalog Images app resources through REST API or GraphQL.


## REST API

There are two REST API endpoints available to manage images using the Catalog Images app:

* `POST` [Save image](#save-image)
* `DELETE` [Delete image](#delete-image)


### Save image

To save an image in File Manager, use the endpoint below. Make sure to send one image at a time and set the request body format to `multipart/form-data`.

```
POST
https://app.io.vtex.com/vtex.catalog-images/v0/{{accountName}}/{{workspace}}/images/save/{{filename}}
```

**Request body example:**
```json
form =@"path/to/file.png"
```

**Response body example (200 OK):**
```json
{
    "id": "special-offer.png",
    "slug": "/assets/vtex.catalog-images/products/special-offer___782206cd73597a717ed67eba399167a6.png",
    "fullUrl": "https://myvtexaccountname.vtexassets.com/assets/vtex.catalog-images/products/special-offer___782206cd73597a717ed67eba399167a6.png"
}
```

If there is already an image with the same filename given, the response will be Conflict (409) with the conflicted image URL in the response body. Otherwise, the response will be OK (200) with the `id`, `slug`, and `fullUrl` in the response body.


### Delete image

The following REST API route allows you to delete a Catalog image in File Manager:

```
DELETE
https://app.io.vtex.com/vtex.catalog-images/v0/{{accountName}}/{{workspace}}/images/save/{{filename}}
```

If the image exists and is successfully deleted, the response will be an empty body with status code OK (200). If the image does not exist, the response will be Not Found (404).


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