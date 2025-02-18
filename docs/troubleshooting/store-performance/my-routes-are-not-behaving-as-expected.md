---
title: "My routes are not behaving as expected"
slug: "my-routes-are-not-behaving-as-expected"
excerpt: "Troubleshooting steps for issues with routes."
hidden: false
createdAt: "2025-01-30T14:25:00.00Z"
updatedAt: "2025-01-30T14:25:00.00Z"
tags:
    - routes
    - redirects
---

**Keywords:** Routes | Redirects | GraphiQL


If your store redirect path doesn't work and the routes are not behaving as expected, follow these troubleshooting steps.

## Solution

### Checking if the redirect is saved in the Rewriter

1. Install the GraphiQL IDE in your account by running `vtex install vtex.admin-graphql-ide@3.x`.
2. Access the Admin and go to **Store Settings > Storefront > GraphiQL IDE**.
3. Select the `vtex.rewriter@1.x` app from the dropdown list.
4. Run the following query, replacing `{URL}` with the `from` path you are having trouble with:

```graphql
  {
    redirect {
      get(path: "/{URL}") {
        from
        to
      }
    }
  }
```

The expected answer is a JSON object containing all the redirects related to that path. Take the following example:

```json
{
  "data": {
    "redirect": {
      "get": {
        "from": "/about-us",
        "to": "/my-store"
      }
    }
  }
}
```

### If the query doesn't return the redirect path

Access the Admin, go to **Storefront** > **Pages** > **Redirects**, and save the desired URL redirects. For more information, refer to the [Managing URL redirects](https://developers.vtex.com/docs/guides/vtex-io-documentation-managing-url-redirects) guide.

### If the query returns the redirect path

Check if your Store Theme or another app has defined a route with the same path you are attempting to save as a redirect. If the route already exists, the redirect will be ignored.
