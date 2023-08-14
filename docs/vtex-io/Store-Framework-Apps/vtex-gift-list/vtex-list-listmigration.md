---
title: "List Migration"
slug: "vtex-list-listmigration"
hidden: false
createdAt: "2023-01-16T00:32:17.866Z"
updatedAt: "2023-01-16T00:32:17.866Z"
---

VTEX has a native feature for list management that can be verified on the [following document](https://help.vtex.com/en/subcategory/list-types--6aeeWirCBUwwCmeIWOgIWs). However, this feature works only for Legacy CMS Portal stores, making it impossible to use for IO and Faststore stores.

**Gift List app** was made to fill this gap, allowing all types of stores to work with lists. Because of that, a common demand is related to the migration of lists, from the native feature to the new app feature.

It is important to take a look at the following details to execute this process:

- The access page for lists will change. On the native feature, the access occurs by the `/giftlist` path. On the new feature, the access occurs by the home page subaccount where the app was installed;
- Both features work with a giftcard system to transfer purchase values to the guests for the list owner. Credits that a client receives in the native feature are valid for the app feature;
- It is necessary to migrate pieces of information related to gift lists, as list owners and items linked with each list;
- The credit transaction history isn't kept on the native feature. Because of that, it isn't possible to migrate this data for the app feature.

## Migration Process

The migration process will use different APIs to extract data from the native feature and insert data into the **Gift List app**. Between the two actions, it is necessary to treat the extracted data to model it for the data structure on the app.

The data extraction will be made with the following endpoint:
`[host]/api/addon/pvt/giftlist/get/[list-id]`. 

``list-id`` is an integer number representing the list creation sequence, starting with the number 1. For example, for a store with 170 lists created on the native method, there will be lists with ``list-ids`` between 1 and 170.

Native lists have diverse types of configuration, and the data structure can vary. Because of that, it is important to treat this data to adapt it to the data structure on the native app. Treating the extracted data, we can insert it into the app feature data structure. 

It can be made by GraphQL routes. All managing methods for MD v2 are available on our GraphQL layer, where they can be manipulated. The entity related to the app is ``vtex.list-graphql@3.5.0``. For more information, you can access the [following documentation](https://developers.vtex.com/docs/guides/graphql-ide).

> Gift List App has no responsibility for the success of the migration process since it is related to two different products.

For further information, please access our [Support Page](https://help.vtex.com/en/faq/como-funciona-o-suporte-da-vtex--3kACEfni4m8Yxa1vnf2ebe).