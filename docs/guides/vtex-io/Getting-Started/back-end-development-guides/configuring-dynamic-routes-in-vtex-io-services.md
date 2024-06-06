---
title: "Configuring dynamic routes in VTEX IO services"
slug: "configuring-dynamic-routes-in-vtex-io-services"
excerpt: "Learn how to define variable-length paths in your VTEX IO service."
hidden: false
createdAt: "2024-06-06T15:02:44.475Z"
updatedAt: "2024-06-06T15:02:44.475Z"
category: "App Development"
---

When developing a [VTEX IO service](https://developers.vtex.com/docs/guides/vtex-io-documentation-service), you may need to define a route that supports variable-length paths to handle requests effectively. This necessity arises when your service needs to capture dynamic query parameters from URLs with a variable number of segments.

In this guide, you will learn how to use wildcard notation to configure your [`service.json`](https://developers.vtex.com/docs/guides/calling-commerce-apis-1-getting-the-service-app-boilerplate#nodeservicejson-file) file, addressing the complexities of dynamic URL structures.

>ℹ️ Check out our documentation to learn more about [Service path patterns](https://developers.vtex.com/docs/guides/service-path-patterns).

## Example use case

As an example, consider you are developing a service that interfaces with the [Get list of products for a query](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/product_search/-facets-) endpoint.

The `facets` parameter of this API follows the format `/${facetKey1}/${facetValue1}/${facetKey2}/${facetValue2}/.../${facetKeyN}/${facetValueN}`, also allowing general filters such as `price`, `category-${n}`, `productClusterIds`, and `trade-policy`. The expected response lists the active products for a given query. To effectively interact with this API, your service needs to define a path that flexibly accommodates the variable structure of this API.

## Instructions

Follow the steps below to define these variable paths in your service:

### Step 1 - Defining the service routes

1. Open the `service.json` file in the app repository.
2. In `routes`, use `/*path` to define the desired service path.

See how the `service.json` file may be configured to consult the API route mentioned above:

```json
"productSearch": {
   "path": "/_v/api/intelligent-search/product_search/*path",
   "public": true
},
```

>ℹ️ Note that the `*` wildcard notation captures variable-length paths dynamically, allowing the endpoint to handle URLs with diverse structures and query parameters.This wildcard notation signals to the service that the endpoint's path can accommodate any number of segments beyond the specified prefix. For instance, in the configuration `"path"`: `"/_v/api/intelligent-search/product_search/*path"`, the `*/path` segment implies that the endpoint can handle URLs like `/_v/api/intelligent-search/product_search/segment1/segment2/.../segmentN`, where `segment1`, `segment2`, and so forth can vary in number and content.

### Step 2 - Accessing the path value in your route handler function

Open the file where your route handler is defined and use the following structure to access the `path` value:

```tsx
const {
  vtex: {
    route: {
      params: { path = '' },
    },
  },
} = ctx;

If necessary, break down the URL path into separate parts and filter out any empty segments as follows:

```tsx
const segments = path.split('/').filter(segment => segment !== '');
```

The `split()` method divides the URL path into an array of segments based on the delimiter, which in this case is the forward slash `('/')`. After splitting the URL, the `filter()` method removes empty strings from the array, ensuring that only meaningful URL segments are retained.
By decomposing a URL path into manageable segments, these segments can be dynamically parsed and used according to the needs of your service.
