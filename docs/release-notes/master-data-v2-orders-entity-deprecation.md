---
title: "Master Data v2 orders entity deprecation"
slug: "master-data-v2-orders-entity-deprecation"
hidden: false
createdAt: 2023-04-11T09:18:00.000Z
type: "deprecated"
excerpt: "VTEX will deprecate the order entity of Master Data v2 in October 2023. Learn how to adapt your store integrations."
---

VTEX is deprecating the [Master Data v2 orders entity](https://developers.vtex.com/docs/guides/using-master-data-v2-triggers-to-interact-with-orders). While some stores may use this entity to create order integrations, we recommend using the [orders feed or hook](https://developers.vtex.com/docs/guides/orders-feed) as they provide a more effective way to create this type of integration. We encourage all users to update their integrations accordingly to ensure a seamless transition.

## What has changed?

This feature has already been deprecated for accounts that used this data entity previously and did not interact with it in 2022.

As of October 2023, VTEX will deprecate the [Master Data v2 orders entity](https://developers.vtex.com/docs/guides/using-master-data-v2-triggers-to-interact-with-orders) for all accounts.

For now, deprecation only means that VTEX will no longer register new orders' data to the entity. Stores will still be able to view previously recorded information in the Master Data v2 order entity.

## What needs to be done?

If you have order integrations that depend on the Master Data v2 data entity, you must adapt your implementation to use the [orders feed or hook](https://developers.vtex.com/docs/guides/orders-feed) instead as soon as possible. See this articles to learn how to do this:

- [Orders feed and hook guide](https://developers.vtex.com/docs/guides/orders-feed)
- [Setting up an order integration](https://developers.vtex.com/docs/guides/erp-integration-set-up-order-integration)
