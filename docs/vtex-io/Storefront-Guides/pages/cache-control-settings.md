---
title: "Cache-control settings"
slug: "cache-control-settings"
hidden: false
createdAt: "2024-03-27T11:00:00.000Z"
updatedAt: "2024-03-27T11:00:00.000Z"
---
Cache-control headers are directives used in HTTP responses to specify caching parameters for a client. These headers help in improving performance and reducing server load by allowing clients to cache resources locally for a certain period and serve stale content while updating it in the background, thus minimizing the impact of network latency. You can find more details in the [AWS documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html).

The [Rewriter](https://developers.vtex.com/docs/guides/rewriter) and the [Render Server](https://developers.vtex.com/docs/guides/render-server) apps have some settings that allow merchants to control the cache behavior when Cache-control headers are used. The Rewriter app is responsible for Product Detail Pages (PDP) and Product Listing Pages (PLP), while the Render Server app is responsible for the homepage and landing pages.

To access these app settings:

1. Open your store’s Admin.
2. Go to **Apps** > **Extensions Hub** > **App Management**.
3. Search for **Rewriter** or **Render Server**, depending on the app you want to configure.
4. In the corresponding app’s box, click on <i class="fa fa-gear"></i> **Settings**.

By default, these apps have defined times to update the cache, and these settings allow to override these times.

- **Overwrite cache control settings**: When enabled, this setting unlocks two other settings, **Max-Age overwrite** and **Stale Revalidate overwrite**, which overwrites the default cache update times.
- **Max-Age overwrite**: This setting overwrites the `max-age` header default value. This header specifies the maximum amount of time (in seconds) for which a resource should be considered fresh. After this time elapses, the client must revalidate the resource with the server before using it again. For example, if a response includes `Cache-control: max-age=3600`, it means the resource can be cached by the client for up to 3600 seconds (1 hour) before it needs to check with the server for a fresh version.
- **Stale Revalidate overwrite**: This setting overwrites the `stale-while-revalidate` header default value. This header allows a client to continue using a cached version of a resource even after it has become stale (i.e., expired according to the `max-age` header). The value of this header indicates the maximum amount of time (in seconds) that the client is allowed to serve a stale response while it revalidates the resource with the server in the background. For example, Cache-control: `stale-while-revalidate=3600` means that the client can serve a stale version of the resource for up to 3600 seconds while it revalidates the resource with the server.

![Cache-control settings](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/cache-control-settings.jpg)

>⚠ We suggest changing those settings carefully since they can affect the time cached on a page. These settings may impact how long changes made to the platform take effect in the storefront. If you are not sure about it, we suggest keeping the default values.
