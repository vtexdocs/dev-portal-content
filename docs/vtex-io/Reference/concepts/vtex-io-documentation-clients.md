---
title: "Clients"
excerpt: "Learn more about VTEX IO Clients and their advantages."
slug: "vtex-io-documentation-clients"
hidden: false
createdAt: "2022-02-16T13:52:17.234Z"
updatedAt: "2022-12-13T20:17:43.979Z"
---

Clients serve as intermediaries that initiate and maintain interactions with both external and internal services. Whether interfacing with VTEX IO Services, VTEX Core Commerce APIs, or external APIs, Clients are crucial in enabling seamless communication and data exchange. This guide will explore the concept of Clients and provide a list of native Clients available in VTEX IO.

## Understanding Clients

Clients are essentially configurations implemented within the VTEX IO platform to abstract and streamline communication with various services. They simplify the process of sending requests and receiving responses, acting as intermediaries between an app and the other services it relies on.

In simpler terms, think of Clients as the messengers of an app, responsible for reaching out to other services, gathering information, and returning it to your application.

## Advantages of using Clients

Clients offer various advantages when it comes to managing interactions and data exchange between your app and other services. They ensure that your app functions effectively by handling the complexity of communication with other services.

When developing VTEX IO apps, using Clients can help you manage and streamline complexity. Clients centralize communication logic, making it easier to maintain and scale your codebase. VTEX IO Clients come equipped with several built-in features that enhance the functionality and performance of your applications:

- **Cache:** Clients incorporate caching mechanisms to store and retrieve data efficiently, reducing the load on services and improving response times.
- **Native metrics support:** Clients integrate with performance monitoring and analytics tools, providing insights into service usage and performance.
- **Retry and timeout options:** Clients offer configurable retry and timeout settings, ensuring robustness and resilience in the face of network issues or service unavailability.
- **Billing tracking:** Clients can track usage and resource consumption, aiding in billing and cost optimization.

### List of native Clients

VTEX offers some native Clients, allowing developers to save time and effort when interacting with services such as VTEX Core Commerce APIs and other internal services.

The [`@vtex/clients`](https://github.com/vtex/io-clients) package provides the following clients for IO apps using the `node` Builder:

| Client             | Description | Methods                                                                                                                                                        |
| ------------------ | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `affiliate`        | Handles affiliate-related operations. | `registerAffiliate`, `changeNotification`, `createSeller`, `getSellerList`                                                                                     |
| `catalog`          | Handles catalog-related tasks such as retrieving product and SKU information. | `getProductsAndSkus`, `getSkuById`, `changeNotification`, `createSeller`, `getSellerList`, `getSellerById`, `getSkuContext`, `getCategoryById`, `getBrandById` |
| `Checkout`         | Deals with order form configurations and custom Checkout data. | `getOrderFormConfiguration`, `setOrderFormConfiguration`, `setSingleCustomData`                                                                                |
| `Logistics`        | Manages logistics and inventory-related tasks. | `getDockById`, `pickupById`, `listPickupPoints`, `nearPickupPoints`, `shipping`, `listInventoryBySku`                                                          |
| `OMS`              | Handles order management operations. | `listOrders`, `userLastOrder`, `order`, `orderNotification`, `cancelOrder`                                                                                     |
| `omsApiProxy`      | Acts as a proxy for OMS API operations. | `orders`, `orderFormId`, `customData`, `register`                                                                                                              |
| `ratesAndBenefits` | Handles Rates and Benefits data. | `getAllBenefits`, `getPromotionById`, `createOrUpdatePromotion`, `createMultipleSkuPromotion`, `updateMultipleSkuPromotion`                                    |
| `suggestions`      | Handles product suggestions and versions. | `getAllSuggestions`, `getSuggestionById`, `sendSkuSuggestion`, `deleteSkuSuggestion`, `getAllVersions`, `getVersionById`                                       |

| Factory      | Description                          | Methods                                                                                                   |
| ------------ | ------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| `masterData` | Interacts with Master Data services. | `get`, `save`, `update`, `saveOrUpdate`, `saveOrUpdatePartial`, `delete`, `search`, `searchRaw`, `scroll` |
| `vbase`      | Interacts with VBase services.       | `get`, `getRaw`, `getWithMetadata`, `save`, `trySaveIfhashMatches`                                        |

## Developing Clients

Consider developing your own clients if you require integration with other services not covered by VTEX native clients. Custom clients extend VTEX IO native Clients, leveraging caching and versioning functionalities.

> ⚠️ Note that direct communication with APIs is generally discouraged in favor of implementing a dedicated Client.

Learn how to create Clients of your own by accessing the [Developing Clients](https://developers.vtex.com/docs/guides/vtex-io-documentation-how-to-create-and-use-clients) guide.
