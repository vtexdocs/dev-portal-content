---
title: "New cache configuration for Rewriter and Render Server apps"
slug: "2024-05-03-new-cache-configuration-for-rewriter-and-render-server-apps"
type: "added"
createdAt: "2024-03-27T11:00:00.000Z"
updatedAt: "2024-03-27T11:00:00.000Z"
hidden: false
excerpt: "The new settings allow client-side cache to be available for longer periods, which can improve page loading latency."
---
We are releasing an update to the [Rewriter](https://developers.vtex.com/docs/apps/vtex.rewriter) and the [Render Server](https://developers.vtex.com/docs/apps/vtex.rewriter) apps that allows merchants to overwrite cache-control default settings in the Admin.

## What has changed?

Within the apps’ settings page, there are three new settings that merchants can use:

|Name|Type|Description|
|-|-|-|
|Overwrite cache control settings|`boolean`|When enabled, this setting unlocks two other settings, **Max-Age overwrite** and **Stale Revalidate overwrite**, which overwrites the default cache update times.|
|Max-Age overwrite|`number`|Overwrites the `max-age` header default value. This header specifies the maximum amount of time, in seconds, for which a resource should be considered fresh. After this time elapses, the client must revalidate the resource with the server before using it again. For example, if a response includes `Cache-control: max-age=3600`, it means the resource can be cached by the client for up to 3600 seconds (1 hour) before it needs to check with the server for a fresh version.|
|Stale Revalidate overwrite|`number`|Overwrites the `stale-while-revalidate` header default value. This header allows a client to continue using a cached version of a resource even after it has become stale, i.e., expired according to the `max-age` header. The value of this header indicates the maximum amount of time, in seconds, that the client is allowed to serve a stale response while it revalidates the resource with the server in the background. For example, Cache-control: `stale-while-revalidate=3600` means that the client can serve a stale version of the resource for up to 3600 seconds while it revalidates the resource with the server.|

![Cache-control settings](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/cache-control-settings.jpg)

## Why did we make this change?

By increasing the `max-age` and `stale-while-revalidate` times, clients will be able to use the cached content for longer periods. Depending on the store’s scenario, these changes can lead to reduced latency and improved performance.

## What needs to be done?

The new settings are available in every store using VTEX IO. To access them, open your store’s Admin and navigate to the Rewriter and the Render Server page settings, where you will be able to define the new cache-control values.

For more information, see the [Cache-control settings](https://developers.vtex.com/docs/guides/cache-control-settings) article.
