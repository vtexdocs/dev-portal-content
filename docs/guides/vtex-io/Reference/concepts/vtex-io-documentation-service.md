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

```json service.json
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

|Name|Type|Description|
|--|--|--|
|`memory`|`number`|Defines the memory size (in MB) that should be allocated to the service. Default: 128, maximum: 1024.|
|`minReplicas`|`number`|Defines the minimum number of replicas available when the service is running. Minimum: 2 for installed apps and 1 for linked apps.|
|`maxReplicas`|`number`|Defines the maximum number of replicas available. Minimum: 5, maximum: 60.|
|`timeout`|`number`|Sets the timeout (in seconds) for aborting a connection if a request takes too long. This parameter affects only incoming requests to the app. It does not affect outgoing requests that the app makes to other clients. Default: 10, minimum: 1, maximum: 60.|
|`ttl`|`number`|Defines the time-to-live (in minutes) for how long the platform will keep each instance of the service running without receiving new requests. Default: 10, minimum: 10, maximum: 60. The requested value is only honored for the most recent stable version of the app. Older versions, versions that have not been deployed, linked apps, or beta versions will have the value overridden to 10.|
|`workers`|`number`|Specifies the number of workers to spawn for the service on production. Minimum: 1, maximum: 4.|
|`rateLimitPerReplica`|`object`|This object contains global parameters whose values define specific throttling limits for requests and events. The values of this object are overridden by the values set for a specific route or event.|
|`↳perMinute`|`number`|Defines the global maximum number of requests and event triggers allowed per minute per replica. This value is overridden by the value set for a specific route or event.|
|`↳concurrent`|`number`|Defines the global maximum number of requests and event triggers a replica will handle simultaneously for that application. This value is overridden by the value set for a specific route or event.|
|`events`|`object of objects`|Each object inside this parameter represents one event. Maps an event handler to an object that describes the sender or topics. This parameter must be used both by the sender and the receivers of the event.|
|`↳topics`|`array of strings`|Identifiers of the event. Previously known as `keys`, which is now deprecated.|
|`↳sender`|`string`|Name of the app that sends the event.|
|`↳settingsType`|`string`|Possible values: `pure`, `workspace`, or `userAndWorkspace`. If `workspace` or `userAndWorkspace`, the app loads the settings of the apps it depends on.|
|`↳rateLimitPerReplica`|`object`|This object contains parameters whose values define specific throttling limits for the event. The values of this object override the global `rateLimitPerReplica` values.|
|`↳↳perMinute`|`number`|Defines the maximum amount of times this event is allowed to trigger per minute per replica. This value overrides the global `rateLimitPerReplica.perMinute` value.|
|`↳↳concurrent`|`number`|Defines the maximum amount of times a replica will handle triggers of this event simultaneously. This value overrides the global `rateLimitPerReplica.concurrent` value.|
|`routes`|`object of objects`|Each object inside this represents one route. Maps route handlers to objects containing information about the route.|
|`↳path`|`string`|Path of the route. Check [Service path patterns](https://developers.vtex.com/docs/guides/service-path-patterns) for details about path construction.|
|`↳public`|`boolean`|Defines if the route is public or private. If `true`, the route will be available at `{account}.myvtex.com` and `{account}.vtexcommercestable.com.br`. If `false`, the route will be at `app.io.vtex.com/{vendor}.{appName}/v{majorVersion}/{account}/{workspace}` and will require a `VtexidClientAutCookie` for [authentication](https://developers.vtex.com/docs/guides/api-authentication-using-user-tokens). Using `appKey` and `appToken` for authentication will not work.|
|`↳access`|`string`|Possible values: `public`, `authenticated`, or `authorized`.|
|`↳policies`|`array of objects`|Defines the actions allowed or denied with the route by whom. More details on [Resource-based Policies](https://developers.vtex.com/docs/guides/vtex-io-documentation-policies#resource-based-policies).|
|`↳rateLimitPerReplica`|`object`|This object contains parameters whose values define specific throttling limits for the route. The values of this object override the global `rateLimitPerReplica` values.|
|`↳↳perMinute`|`number`|Defines the maximum number of requests allowed per minute per replica for this route. This value overrides the global `rateLimitPerReplica.perMinute` value.|
|`↳↳concurrent`|`number`|Defines the maximum number of requests a replica will handle for this route. This value overrides the global `rateLimitPerReplica.concurrent` value.|

Note that most of these fields are optional, and default values provided by the platform are often sufficient.

> ℹ️ The VTEX platform defines the TTL (time-to-live) parameter for all IO apps as 24 hours. As of [this release](https://developers.vtex.com/updates/release-notes/2025-04-25-vtex-io-ttl-parameter-standardizeded-for-all-io-apps), app developers can no longer modify this parameter, which will be ignored if declared in the `service.json` file.

## Best practices

To help configuring your service, we describe some best practices below about many of the parameters available. This should help achieve good performance and avoid failures with your application.

### Memory allocation

App developers have to evaluate the `memory` usage of the app to choose a proper value for the memory parameter. Consider factors such as the complexity of your application, and the size of the data structures instanced in the implementation. Adequate memory allocation helps prevent failures and performance issues.

### Timeout settings

Setting an appropriate `timeout` value prevents requests from timing out prematurely or causing resource exhaustion. Ideally, it is expected that applications have low response times most of the time, in the range of milliseconds, and do not fail to process the requests.

In scenarios where an application has a low timeout setting and takes too long to respond, the platform will respond to the request with a timeout response and the data from the app will not be delivered to the client when the request could be processed. On the other hand, in scenarios where the timeout setting is high and the application usually does not take long to respond, if a problem occurs with the processing of the request, the platform will take too long to respond with a timeout and inform the client that a problem has occurred.

Balancing between a low or high timeout setting depends on the time that is expected to deliver a response and how fast the requester requires the response to perform its work.

Testing response times to decide a proper timeout setting can be done in various ways including, but not limited to, different connection conditions (mobile vs. tethered, instabilities, etc.), requests from different locations, different workloads and settings (memory, replicas, etc.), and measuring percentiles of the slowest response times.

### Replica management

VTEX has an autoscaling feature for the IO infrastructure, which dynamically controls the number of instances of each app obeying certain parameters. We call replicas the number of instances of an app running in our infrastructure. The minimum and maximum replicas an app can have are determined by the parameters `minReplicas` and `maxReplicas`, respectively. The current replicas increase and decrease automatically according to how much the app is requested in the platform, considering all the accounts where the app is installed.

The values of `minReplicas` and `maxReplicas` should be defined considering the expected demand for the app. If you have observability on the accounts where the app is installed, some metrics can help define the parameters, e.g., the number of accesses or purchases and how they fluctuate.

### Route configuration

This configuration defines the paths of the endpoints that the app will expose, among other properties like if it is public or private, and the permissions through policies. For more details about the path construction, read [Service path patterns](https://developers.vtex.com/docs/guides/service-path-patterns). For more information about permissions of the endpoints, read [Resource-based Policies](https://developers.vtex.com/docs/guides/vtex-io-documentation-policies#resource-based-policies).

### TTL management

Time-to-live (TTL) is the time that a service instance will keep running in the platform without receiving new requests before it is shut down. By having a TTL, we can minimize resource wastage from service instances.

When new requests are made and there are no instances available to respond, the platform has to start new instances to process and respond to the requests, a process that we call cold start. A cold start is slow, so the first request a new instance responds to takes longer than usual, and the following requests are processed as usual.

Depending on the service usage, a small TTL value can lead to cold starts happening more frequently, which causes slower response times. We recommend increasing the TTL above the default value only if you frequently notice slow response times that can be caused by cold starts.

### Worker configuration

VTEX IO services use the [Cluster module from Node.js](https://nodejs.org/api/cluster.html) for parallelism. A service starts with a main process and then creates child processes, or workers, to handle the load from requests. The number of workers is determined by the value of the `workers` parameter.

A higher number of workers is recommended when more processing capacity is required to handle requests, which can reduce response times. Be aware that more workers also increase the memory usage of the service, so adjust the `memory` parameter accordingly. If your service performs well with a single worker or does not take advantage of parallelism, we recommend not declaring a `workers` value or setting it to 1.
