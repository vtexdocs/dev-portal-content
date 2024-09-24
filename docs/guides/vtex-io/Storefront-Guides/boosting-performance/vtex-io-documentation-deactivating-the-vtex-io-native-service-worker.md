---
title: "Deactivating the VTEX IO native service worker"
slug: "vtex-io-documentation-deactivating-the-vtex-io-native-service-worker"
hidden: false
createdAt: "2020-07-16T18:56:22.303Z"
updatedAt: "2022-12-13T20:17:44.052Z"
---

All stores built on the Store Framework include a native [Service Worker](https://developers.google.com/web/fundamentals/primers/service-workers). This service worker is integral to enabling your store to operate as a Progressive Web App (PWA), enhancing user experience by providing features like offline navigation, faster loading times, and the ability to add the store to the home screen.

While the native service worker greatly enhances the functionality of your store, you may find it necessary to integrate third-party services that also require their own service workers. Since a website can only support a single active service worker, conflicts may arise. In such cases, you have the option to deactivate the VTEX IO native service worker, allowing you to implement your desired third-party solution successfully.

## Instructions

1. Access the Admin.
2. Navigate to **Store Settings > Storefront > Store**.
3. Click the `Advanced` tab.
4. Enable the `Service Worker` option to deactivate the native service worker.

        ![service-worker-toggle-recipe](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-deactivating-the-vtex-io-native-service-worker-0.png)

5. Save your changes.

Once you save the changes, the VTEX Service Worker will be automatically disabled, allowing your store to function with the third-party service worker.
