---
title: "Setting up alternate keys in Master Data v2"
slug: "setting-up-alternate-keys-in-master-data-v2"
hidden: false
createdAt: "2022-08-04T18:58:24.930Z"
updatedAt: "2022-08-04T19:08:53.907Z"
---
With Master Data v2 you can configure alternate keys, which are cross JSON schema.

There are two types of alternate keys:
- `Single`
- `Multiple`

The `Single` type sets the value of the field as unique in the data entity, while in the `Multiple` type, other documents may have this same value.

## Get documents using alternate keys

To get a document using an alternate key, add the following query in the search API:

```
/search?{{fieldName}}={{fieldValue}}
```

In this scenario, Master Data will not try to get the document in the indexer. It is a faster process than getting a single document in the indexer.

The `Multiple` type must be used in the case of low quantities of matching documents. For instance, the Profile System uses this `Multiple` index to get clients' addresses. The amount of addresses of a given client is less than one hundred. So this is a good use case.

If your alternate key has over one hundred matches available, you need to set the field as indexed and paginate your searches.