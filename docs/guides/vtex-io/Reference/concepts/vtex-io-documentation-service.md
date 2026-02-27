---
title: "Service"
slug: "vtex-io-documentation-service"
hidden: false
createdAt: "2021-04-06T14:55:45.779Z"
updatedAt: "2022-12-13T20:17:44.904Z"
---

In the VTEX IO ecosystem, services play a crucial role by allowing you to run .NET and Node.js code directly on VTEX servers. They enable VTEX IO apps to export HTTP routes, GraphQL resolvers, and event handlers to the server.

## Developing services

To create and export services, specify the `node` or `dotnet` [builders](https://developers.vtex.com/docs/guides/vtex-io-documentation-builders) in your app's [`manifest.json`](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest) file. Additionally, GraphQL services can be exported using the `graphql` builder.

> ℹ️ For practical reference, see our service example apps: [Node.js](https://github.com/vtex-apps/service-example), [.NET](https://github.com/vtex-apps/service-example-dotnet), and [GraphQL](https://github.com/vtex-apps/graphql-example).

For more information, see the [Developing services on VTEX IO](https://learn.vtex.com/docs/course-service-course-lang-en) course in the VTEX Learning Center.

## Configuring services

The configuration of your service depends on the selected builder (`node` or `dotnet`). You'll find the `service.json` file in the `/node` or `/dotnet` folder of your app. This configuration file defines essential parameters, including timeout, memory allocation, routes, event handlers, and replicas.

Here's an example of a `service.json` file:

```json service.json
{
  "memory": 256,
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

Let's take a closer look into the parameters you can set within the `service.json` file:

|Name|Type|Description|
|--|--|--|
|`memory`|`number`|Defines the memory size (in MB) that should be allocated to the service. Default: 128, maximum: 1024.|
|`minReplicas`|`number`|Defines the minimum number of replicas available when the service is running. Minimum: 2 for installed apps and 1 for linked apps.|
|`maxReplicas`|`number`|Defines the maximum number of replicas available. Minimum: 5, maximum: 60.|
|`timeout`|`number`|Sets the timeout (in seconds) for aborting a connection if a request takes too long. This parameter only affects incoming requests to the app. It doesn't affect outgoing requests the app makes to other clients. Default: 10, minimum: 1, maximum: 60.|
|`workers`|`number`|Specifies the number of workers to spawn for the service in production. Minimum: 1, maximum: 4.|
|`rateLimitPerReplica`|`object`|This object contains global parameters whose values define global throttling limits for requests and events. The values of this object are overridden by the values set for a specific route or event.|
|`↳perMinute`|`number`|Defines the global maximum number of requests and event triggers allowed per minute per replica. This value is overridden by the value set for a specific route or event.|
|`↳concurrent`|`number`|Defines the global maximum number of requests and event triggers a replica can handle simultaneously for that application. This value is overridden by the value set for a specific route or event.|
|`events`|`object of objects`|Each object within this parameter represents one event. It maps an event handler to an object that describes the sender or topics. This parameter must be used both by the sender and the receiver of the event.|
|`↳topics`|`array of strings`|Identifiers of the event. Previously known as `keys`, which is now deprecated.|
|`↳sender`|`string`|Name of the app that sends the event.|
|`↳settingsType`|`string`|Possible values: `pure`, `workspace`, or `userAndWorkspace`. If set to `workspace` or `userAndWorkspace`, the app loads the settings of its dependencies.|
|`↳rateLimitPerReplica`|`object`|This object contains parameters whose values define specific throttling limits for the event. The values of this object override the global `rateLimitPerReplica` values.|
|`↳↳perMinute`|`number`|Defines the maximum amount of times this event is allowed to trigger per minute per replica. This value overrides the global `rateLimitPerReplica.perMinute` value.|
|`↳↳concurrent`|`number`|Defines the maximum number of times a replica can handle triggers of this event simultaneously. This value overrides the global `rateLimitPerReplica.concurrent` value.|
|`routes`|`object of objects`|Each object within this parameter represents one route. It maps route handlers to objects containing information about the route.|
|`↳path`|`string`|Path of the route. See [Service path patterns](https://developers.vtex.com/docs/guides/service-path-patterns) for details about path construction.|
|`↳public`|`boolean`|Defines if the route is public or private. If set to `true`, the route will be available at `{account}.myvtex.com` and `{account}.vtexcommercestable.com.br`. If set to `false`, the route will be available at `app.io.vtex.com/{vendor}.{appName}/v{majorVersion}/{account}/{workspace}` and will require a `VtexidClientAutCookie` for [authentication](https://developers.vtex.com/docs/guides/api-authentication-using-user-tokens). Authentication using `appKey` and `appToken` is not supported.|
|`↳access`|`string`|Specifies access level. Possible values: `public`, `authenticated`, or `authorized`.|
|`↳policies`|`array of objects`|Defines the actions allowed or denied on the route and by whom. Learn more in [Resource-based policies](https://developers.vtex.com/docs/guides/vtex-io-documentation-policies#resource-based-policies).|
|`↳rateLimitPerReplica`|`object`|This object contains parameters whose values define specific throttling limits for the route. The values of this object override the global `rateLimitPerReplica` values.|
|`↳↳perMinute`|`number`|Defines the maximum number of requests allowed per minute per replica for this route. This value overrides the global `rateLimitPerReplica.perMinute` value.|
|`↳↳concurrent`|`number`|Defines the maximum number of requests a replica can handle for this route. This value overrides the global `rateLimitPerReplica.concurrent` value.|

Note that most of these fields are optional, and default values provided by the platform are often sufficient.

> ℹ️ The VTEX platform sets the TTL (time-to-live) parameter for all IO apps to 24 hours. As of [this release](https://developers.vtex.com/updates/release-notes/2025-04-25-vtex-io-ttl-parameter-standardizeded-for-all-io-apps), app developers can no longer modify this parameter — any value declared in the `service.json` file will be ignored.

## Best practices

To help you configure your service, here are some best practices for the available parameters. These recommendations aim to improve performance and prevent application failures.

### Memory allocation

App developers must evaluate the `memory` usage of the app to choose a proper value for the memory parameter. Consider factors such as the complexity of your application and the size of the data structures instanced in the implementation. Adequate memory allocation helps prevent failures and performance issues.

### Timeout settings

Setting an appropriate `timeout` value prevents requests from timing out prematurely or causing resource exhaustion. Ideally, it's expected that applications have low response times most of the time, in the range of milliseconds, and don't fail to process the requests.

If an application has a low timeout setting but takes too long to respond, the platform will return a timeout response, and the data from the application won't be delivered to the client when expected. On the other hand, if the timeout setting is too high and the application typically responds quickly, the platform may take too long to return a timeout in case of failure, delaying the client's awareness that something went wrong.

Balancing between a low or high timeout setting depends on the expected response time and how quickly the requester needs that response to continue processing.

Testing response times to decide a proper timeout setting can be done in various ways including, but not limited to, different connection conditions (mobile vs. tethered, instabilities, etc.), requests from different locations, different workloads and settings (memory, replicas, etc.), and measuring percentiles of the slowest response times.

### Replica management

VTEX offers an autoscaling feature for the IO infrastructure that dynamically adjusts the number of app instances based on certain parameters. The number of app instances running in our infrastructure is called replicas. The minimum and maximum number of replicas for an app are determined by the `minReplicas` and `maxReplicas` parameters, respectively. The number of active replicas scales automatically according to the app demand across all accounts where it's installed.

The values of `minReplicas` and `maxReplicas` should be defined considering the expected demand for the app. If you have observability on the accounts where the app is installed, you can use metrics — such as the number of accesses or purchases and their fluctuations — to help determine the appropriate values.

### Route configuration

This configuration defines the paths of the endpoints that the app will expose, among other properties such as whether the endpoints are public or private and what permissions apply through policies. For more details on path construction, see [Service path patterns](https://developers.vtex.com/docs/guides/service-path-patterns). For more information about endpoint permissions, see [Resource-based policies](https://developers.vtex.com/docs/guides/vtex-io-documentation-policies#resource-based-policies).

### TTL management

Time-to-live (TTL) is the duration a service instance remains active on the platform without receiving new requests before it's shut down. TTL helps minimize resource waste from service instances.

When new requests are made and no instances are available to respond, the platform must start new instances to handle them, a process called a cold start. Cold starts are slower, so the first request handled by a new instance takes longer than usual. Subsequent requests are processed normally.

Depending on the service usage, a small TTL value can lead to cold starts happening more frequently, which causes slower response times.

### Worker configuration

VTEX IO services use the [Cluster module from Node.js](https://nodejs.org/api/cluster.html) for parallelism. A service starts with a main process and then creates child processes, or workers, to handle the load from requests. The number of workers is determined by the value of the `workers` parameter.

A higher number of workers is recommended when more processing capacity is required to handle requests, as this can reduce response times. Be aware that more workers also increase the memory usage of the service, so adjust the `memory` parameter accordingly. If your service performs well with a single worker or doesn't take advantage of parallelism, we recommend not declaring a `workers` value or setting it to 1.
