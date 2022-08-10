---
title: "Render Server"
slug: "vtex-render-server"
excerpt: "vtex.render-server@8.165.3"
hidden: true
createdAt: "2022-07-13T17:00:11.325Z"
updatedAt: "2022-07-18T14:28:11.093Z"
---
This app is responsible for server-side rendering of all render apps.

# Render Server
> The HTTP server for the VTEX Render framework.

# Table of Contents
- [How It Works](https://github.com/vtex/render-server#how-it-works)
    - [Introduction](https://github.com/vtex/render-server#introduction)
    - [Features](https://github.com/vtex/render-server#features)
        - [Routes](https://github.com/vtex/render-server#routes)
        - [Critical CSS](CriticalCSS.md)
    - [System Design](https://github.com/vtex/render-server#system-design)
        - [Basic Request Workflow](https://github.com/vtex/render-server#basic-request-flow)
        - [Cache layers](https://github.com/vtex/render-server#cache-layers)
        - [Rendering Pipeline](https://github.com/vtex/render-server#rendering-pipeline)
- [Usage Example](https://github.com/vtex/render-server#usage-example)
- [Contributing](https://github.com/vtex/render-server#contributing)
- [Monitoring](https://github.com/vtex/render-server#monitoring)
- [Related Repositories](https://github.com/vtex/render-server#related-repositories)
- [License](https://github.com/vtex/render-server#license)

# How It Works
## Introduction
The purpose of this app is to fetch all the data that is necessary to render a page and pass it to the black-box
[render SSR service](https://github.com/vtex/render-ssr).

Since [SSR is CPU-bound](https://medium.com/airbnb-engineering/operationalizing-node-js-for-server-side-rendering-c5ba718acfc9), we decided to
split SSR computation and fetching of informations. The CPU-heavy side sits at [render-ssr](https://github.com/vtex/render-ssr) and the IO-bound side of fetching assets and metadata sits here.


## Features

- Data fetching for SSR
- Canonical name resolution for apps

### Routes
More detailed routing can be found at `service.json` and `index.ts`.

Important routes: 

+ `/render`  
  Accepts: `GET`, `OPTIONS`  
  **What does it do?**: In few words, fetches all components that need to be rendered, all
  assets that are needed to do that, and sends the CPU-intensive task of rendering to `render-ssr`.  
    + `renderGet`: Creates a state that middlewares will use
    throughout the request, and calls them.
    + `error`: caches any error that other middleware threw.
    logs the person out if that happens.
    + `timing`: Adds all the server timings (how long each function took) to a request header.
    + `authorization`: checks if the request needs authorization, and
    if so, ensures it has the correct authorization.
    + `segment`: Adds information about channel, country code,
    culture info, currency code and currency symbol to the request.
    + `culture`: Adds information about the locale, language and
    country to the request.
    + `meta`: Adds metadata about gocommerce or vtex services to the request.
    + `page`: Fetches all the components, extensions and messages that the
    render server actually has to render.
    + `legacy`: If the request requires json output (legacy behaviour), Adds the correct
    cross-origin header.
    + `cache`: layer of in-memory stale cache.
    + `runtime`: picks and flattens informations gathered in the other middleware to send to the
    SSR service.
    + `render`: Fetches all assets needed to render the page, decides whether to server-side render,
    and sends to SSR service if so.

+ `/canonical`  
  Accepts: `GET`, `OPTIONS`  
  **What does it do?**:
    - Resolves canonical path of the requested page
    and sends it to `/render`. All implementation is
    inside `handlers/canonical.ts` and `resources/canoncical.ts`.

## System Design
### Basic request flow
The main route of this service is `/render`, and `/canonical` is just a wrapper for the rendering.

Example of request:  
GET `/render`
```json

[Insert example here]

```

### Cache layers
Since this application receives lots of repeated requests,
heavy caching is involved. Here, we'll explain all the
cache layers that this service uses.

1. CloudFront cache  
  Before the request even reaches the server, it passes through
  CloudFront's cache service.
  Should there be a 500 Internal Server Error, cloudfront caches the
  bad response for 10s. If the result is an OK message instead,

2. KubeRouter SmartCache
  Routes that describe `"smartcache": true` in `service.json` also have caching by KubeRouter.
  This cache works by combining `X-Vtex-Meta` tags of buckets read in vbase to make an `eTag`
  to be saved as HTTP-Cache for the client. Unless some data in vbase changes, the client will
  hold that eTag cache until it expires.

3. In-Memory caching  
  `render-server` also has a layer of stale cache, in `middleware/cache.ts`. It is a 10 minute
  cache for production that is also a 6 hour cache in case some servers go down.

4. App caching
  Finally, the app that is being rendered can also have cached data. But that is beyond control
  of this microservice.

### Rendering Pipeline

TODO

## Usage Example
To see `render-server` in action, just link this app with `vtex link` and access the store's home of your current account/workspace.

For example, if your are in the `storecomponents` account and in the `test` workspace, just access `test--storecomponents.myvtex.com` as check the logs in your terminal.

# Contributing
Please check [this link](https://github.com/vtex-apps/awesome-io).

The most important files of this repository are:

- `index.ts`
- `handlers/render.ts`
- `middleware/index.ts`
- all middleware

# Monitoring
After releasing, it's extremely important to monitor how your changes are affecting the system. For this, we use tools like Splunk, Prometheus and the kubernetes's dashboard.

[Splunk](https://splunk7.vtex.com/en-US/app/vtex_colossus/dashboards) is usefull for catching internal bugs and watching performance trends. It can be useful when performing optimizations or doing hot fixes.

[Prometheus](http://prometheus.aws-us-east-1.vtex.io/?orgId=1) gives you a better picture of how the VTEX IO infra feels and responds to our application. This is handy if you want to know how the status codes are distributed and if the application is frequently restarting. Additionally, it is a useful way of measuring cluster utilization.  Example: How many replicas and how much memory are used in deployment.

[Kubernetes](https://dashboard.aws-us-east-1.vtex.io/#!/overview?namespace=vtexio) dashboard is great for catching bugs inside the application. This is where you can see all of your `print` and `console.log`s and make quick rollbacks.

# Related Repositories
- (Asset Server)[https://github.com/vtex/asset-server]
- (Render SSR)[https://github.com/vtex/render-ssr]

# License
> Proprietary software. (c) VTEX.