---
title: "Service"
slug: "vtex-io-documentation-service"
hidden: false
createdAt: "2021-04-06T14:55:45.779Z"
updatedAt: "2022-12-13T20:17:44.904Z"
---

In the VTEX IO ecosystem, services play a crucial role by allowing you to run .NET and Node.js code directly on VTEX servers. Services enable VTEX IO apps to export HTTP routes, GraphQL resolvers, and event handlers to the server.

## Developing services

To create and export services, you need to specify the `node` or `dotnet` [builders](https://developers.vtex.com/docs/guides/vtex-io-documentation-builders) in your app's [`manifest.json`](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest) file. Additionally, GraphQL services can be exported using the `graphql` builder.

> ℹ️ For a practical example, refer to our service example apps: [Node.js](https://github.com/vtex-apps/service-example), [.NET](https://github.com/vtex-apps/service-example-dotnet), and [GraphQL](https://github.com/vtex-apps/graphql-example).

For more information, check the [Developing services on VTEX IO](https://learn.vtex.com/docs/course-service-course-lang-en) course in the VTEX Learning Center.

## Configuring services

The configuration of your service depends on the selected builder  (`node` or `dotnet`). You will find the `service.json` file in the `/node` or `/dotnet` folder of your app. This configuration file is responsible for defining essential parameters, including timeout, memory allocation, routes, event handlers, and replicas.

Here's an example of a `service.json` file:

```json
{
  "memory": 256,
  "ttl": 10,
  "timeout": 2,
  "minReplicas": 2,
  "maxReplicas": 4,
  "routes": {
    "status": {
      "path": "/_v/status/:code",
      "public": true
    }
  }
}
```

## Service configuration parameters

Let's delve into the parameters you can set within the `service.json` file:

|Name  |Type  |Description  |
|--|--| -- |
|`events` | `object` |Maps a event handler to an object that describes sender or keys.|
|`maxReplicas` | `number` |Defines the maximum number of replicas available.|
|`minReplicas` | `number` |Defines the minimum number of replicas available when the service is running. |
|`memory` |`number`  |Allocates the specified memory size (in MB) allocated to the service.|
|`routes` | `object` |Maps route handlers to objects containining information about the route, such as `path` and `public`.|
|`timeout` | `number` |Sets the timeout (in seconds) for aborting a connection if a request takes too long.|
|`ttl` | `number` | Defines the time-to-live (in minutes) for how long the platform will keep the service running without receiving new requests (Default: 10 minutes; minimum: 10 minutes; maximum: 60 minutes).|
|`workers` | `number` |Specifies the number of workers to spawn for the service on production. (maximum: 4). |

Note that most of these fields are optional, and default values provided by the platform are often sufficient.
