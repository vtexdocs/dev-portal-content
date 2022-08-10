---
title: "Image Protocol"
slug: "vtex-image-protocol"
excerpt: "vtex.image-protocol@1.0.3"
hidden: true
createdAt: "2022-07-13T15:38:22.516Z"
updatedAt: "2022-07-14T13:16:53.631Z"
---
## Definition

This is an intermediary app between the store-image and the image-protocol-example, that helps implementing the image protocol.
It makes the call to the API endpoint defined in the image-protocol-example, passing the params from the store-image and retrieving the URLs that will be displayed in the store-image component.

![Diagram](../public/metadata/images/summary.png)

> **NOTE**: This app would be a dependency in the store-image component.

## Settings schema

In the `manifest.json` there is a new field called settingsSchema which declares a JSON Schema to receive the needed information.

```json
"settingsSchema": {
    "title": "Image Protocol Settings",
    "type": "object",
    "properties": {
      "token": {
        "title": "Token",
        "type": "string"
      },
      "endpoint": {
        "title": "REST API URL",
        "description": "Endpoint for the REST API",
        "type": "string"
      }
    }
  },
```

![API Endpoint Configuration](../public/metadata/images/configuration.png)

## External client

In order to consume data from an endpoint, an external client is needed. In `node/clients` the client is created.
In order to use its method this client can be used inside the resolver. The endpoint from the settingsSchema is also available though the apps client.

In `node/resolvers` :

```ts
export const getImage = async (
  _: unknown,
  { userId, imageProtocolId }: { userId: string; imageProtocolId: string },
  ctx: Context
) => {
  const {
    clients: { apps, imageProtocolImplementation },
  } = ctx
  const appId: string = process.env.VTEX_APP_ID as string
  const appSettings = await apps.getAppSettings(appId)
  const imageUrlResponse = await imageProtocolImplementation.getUrl(
    appSettings.endpoint,
    appSettings.token,
    { userId, imageProtocolId }
  )

  return imageUrlResponse
}
```

## GraphQL query

### In this app, the resolver is exposed as a query

```graphql
query($userId: String!, $imageProtocolId: String!) {
  getImage(userId: $userId, imageProtocolId: $imageProtocolId) {
    url
    urlMobile
  }
}
```

```json
{
  "userId": "",
  "imageProtocolId": "banner"
}
```

The response will be something similar to this:

```json
{
  "data": {
    "getImage": {
      "url": "https://lreyes.vtexassets.com/assets/vtex.file-manager-graphql/images/ef484a90-acb9-4f1b-8481-99e89a43a466___a3cf5c6525b1c13fdf06eb4a256f958d.jpg",
      "urlMobile": "https://lreyes.vtexassets.com/assets/vtex.file-manager-graphql/images/3767dbe7-0546-446b-b2e0-0e00ae282c3f___200c03de6f2e80dc23434cff4caf7f9a.jpeg"
    }
  }
}
```

#### Query String

For `?userId=query-string&imageProtocolId=query-string`, the values for the params are received in the requestInfo object that is passed to the getUrl method.

## Testing

In order to test it, first you need to link this application to your workspace. Then you can try in GraphiQL the query getImage to make sure this work as expected and you get the data saved.