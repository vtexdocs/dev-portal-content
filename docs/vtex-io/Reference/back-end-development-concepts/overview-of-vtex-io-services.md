---
title: "Overview of VTEX IO Services"
slug: "overview-of-vtex-io-services"
hidden: true
createdAt: "2020-10-08T13:26:34.527Z"
updatedAt: "2020-10-08T13:26:34.527Z"
---
## Introduction
VTEX IO powers big e-commerce operations, and for most of that it's necessary to **run code on a server**. Services are how we run **Node.js or .NET** code on VTEX IO infrastructure, backed by API abstractions to improve developer experience.

Services can export **HTTP Routes**, **GraphQL resolvers** or **event handlers.**

Using the builders `node` or `dotnet`, you can export services from a VTEX IO app, just like themes or store blocks. It's easy to quickly setup, for example, a REST API with that.

## The `service.json` file

The `service.json` is a file that must exist on the folder of the service (`node/` or `dotnet/`), and it's with this file that you may **declare routes or events that the service must respond to.** It also configures parameters like *timeout* and *memory* about the deployment of that service.

This is the `node/service.json` from [vtex.service-example](https://github.com/vtex-apps/service-example) app:

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"memory\": 256,\n  \"ttl\": 10,\n  \"timeout\": 2,\n  \"minReplicas\": 2,\n  \"maxReplicas\": 4,\n  \"routes\": {\n    \"status\": {\n      \"path\": \"/_v/status/:code\",\n      \"public\": true\n    }\n  }\n}",
      "language": "json"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "After defining these configs, it's possible to export handler functions on node/index.ts file."
}
[/block]
Most of the fields on the service.json are optional, and default values will be used by the platform. 
[block:parameters]
{
  "data": {
    "h-0": "Name",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "routes",
    "1-0": "events",
    "2-0": "memory",
    "3-0": "ttl",
    "4-0": "timeout",
    "5-0": "minReplicas",
    "6-0": "maxReplicas",
    "7-0": "workers",
    "0-1": "Object",
    "1-1": "Object",
    "2-1": "Number",
    "3-1": "Number",
    "4-1": "Number",
    "5-1": "Number",
    "6-1": "Number",
    "7-1": "Number",
    "0-2": "A map from the name of a route handler you want to another object declaring path, public or other information about ReBAC",
    "1-2": "A map from the name of a event handler on the code to another object describing sender or keys",
    "2-2": "In MB. The size of memory to be allocated to that service.",
    "3-2": "In minutes. Time that the platform will keep the service running without receiving any requests. Default: 10. Max: 120",
    "4-2": "In seconds. VTEX IO infra will abort the connection if the request time is longer than that",
    "5-2": "When the service is running, how many minimum replicas will be available.",
    "6-2": "The largest amount of replicas that will be available.",
    "7-2": "Numbers of workers to spawn for that service on production. (Max: 4)"
  },
  "cols": 3,
  "rows": 8
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "It´s also possible to export GraphQL services, using the graphql builder. You can check vtex.graphql-example to see how it's done."
}
[/block]