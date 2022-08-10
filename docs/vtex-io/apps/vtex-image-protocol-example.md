---
title: "Image Protocol Example"
slug: "vtex-image-protocol-example"
excerpt: "vtex.image-protocol-example@0.5.2"
hidden: true
createdAt: "2022-07-13T15:42:20.964Z"
updatedAt: "2022-08-02T07:41:18.728Z"
---
![Admin Section: Image Protocol](../public//metadata/images/screenshots/desktop/desktop.png)

## Description

An example app to implement image protocol. This app creates a new section in the Admin panel through which the user can save data in vbase (in this specific case we are saving customer class, polygon, URLs for desktop and mobile, href to redirect and the id for the component that will render the content). At the same time this app creates an endpoint to retrieve the URLs using the data passed as params.

## GraphQL mutations

### In this example app, there are three mutations configured

- The first mutation is used to save the files and return the url

```graphql
mutation($file: Upload!) {
  uploadFile(file: $file) @context(provider: "vtex.file-manager-graphql") {
    fileUrl
  }
}
```

> **NOTE**: In order to use this mutation the file-manager-graphql is required as a dependency in the manifest.json:

```json
"dependencies": {
    "vtex.file-manager-graphql": "0.x"
  },
```

- The second one related to saving data in vbase

```graphql
mutation saveDataInfo(
  $customerClassValue: String
  $polygon: String
  $url: String
  $urlMobile: String
  $hrefImg: String
  $idImg: String
) {
  saveDataInfo(
    customerClassValue: $customerClassValue
    polygon: $polygon
    url: $url
    urlMobile: $urlMobile
    hrefImg: $hrefImg
    idImg: $idImg
  ) {
    customerClassValue
    polygon
    url
    urlMobile
    hrefImg
    idImg
  }
}
```

Query variables:

```json
{
  "customerClassValue": "test",
  "polygon": "test",
  "url": "url",
  "urlMobile": "url",
  "hrefImg": "url",
  "idImg": "banner"
}
```

- The third one related to delete data in vbase

```graphql
mutation removeFromList(
  $customerClass: String
  $polygon: String
  $imageProtocolId: String
) {
  removeFromList(
    customerClass: $customerClass
    polygon: $polygon
    imageProtocolId: $imageProtocolId
  ) {
    customerClass
    polygon
    imageProtocolId
  }
}
```

Query variables:

```json
{
  "customerClass": " test",
  "polygon": "test",
  "imgId": "banner"
}
```

### API REST Endpoint to save data from vbase

There is an endpoint that can be used on Postman to save data in vbase.
http://{workspace}--{account}.myvtex.com/\_v/image-protocol-example/save-info
To do that, you can set
![Save Info](../public/metadata/images/save-info.png)

### API REST Endpoint to delete data from vbase

There is an endpoint that can be used on Postman to delete data saved in vbase.
http://{workspace}--{account}.myvtex.com/\_v/image-protocol-example/remove
To do that, you have to send a body with customer class, polygon and image protocol id
![Delete Info](../public/metadata/images/delete-info.png)

### API REST Endpoint to get data from vbase

There is an endpoint that can be used on Postman to get the data saved in vbase.
http://{workspace}--{account}.myvtex.com/\_v/image-protocol-example/get-url
To do that, you can set userId and imageProtocolId as params
![Get Info](../public/metadata/images/get-info.png)

The endpoints used in the previous steps are defined as routes in `node/index.ts`

### Defining the route on _service.json_

```json
{
  "memory": 256,
  "ttl": 10,
  "timeout": 2,
  "minReplicas": 2,
  "maxReplicas": 4,
  "workers": 1,
  "routes": {
    "getUrl": {
      "path": "/_v/image-protocol-example/get-url",
      "public": true
    },
    "saveInfo": {
      "path": "/_v/image-protocol-example/save-info",
      "public": true
    },
    "deleteRecord": {
      "path": "/_v/image-protocol-example/remove",
      "public": true
    }
  }
}
```

The `service.json` file that sits on the root of the `node` folder holds informations about this service, like the maximum timeout and number of replicas, what might be discontinued on the future, but also **sets its routes**.

For cach _key_ on the `routes` object, there should be a **corresponding entry** on the exported Service object on `node/index.ts`, this will hook your code to a specific route.

```ts
import { method } from '@vtex/api'
export default new Service({
  ...
  graphql: {
    resolvers: {
      Mutation: {
        saveDataInfo,
        removeFromList,
      },
      Query: {
        getDataList,
        getPolygons,
      },
    },
  },
  routes: {
    getUrl: method({
      GET: [errorHandler, getUsersPolygon, getUserCustomerClass, getImgUrl],
    }),
    saveInfo: method({ POST: [validations, saveInfo] }),
    deleteRecord: method({ DELETE: [deleteRecord] }),
  },
  ...
})
```

### Access Control

You can also provide a `public` option for each route. If `true`, that resource will be reachable for everyone on the internet. If `false`, VTEX credentials will be requested as well.

#### HTTP methods

When you define a route on the `service.json`, your NodeJS handlers for that route will be triggered **on every HTTP method** (GET, POST, PUT...), so, if you need to handle them separately you need to implement a "sub-router". Fortunately, the _node-vtex-api_ provides a helper function `method`, exported from `@vtex/api`, to accomplish that behaviour. Instead of passing your handlers directly to the corresponding route on `index.ts`, you pass a `method` call passing **an object with the desired method as key and one handler as its corresponding value**.
In this case we use the GET method:

## Testing the app

In order to test it, first you need to link this application to your workspace and check if you see the section in the Admin panel. Then you can try in GraphiQL the mutation to save data and then test the endpoint on Postman to make sure this work as expected and you get the data saved.