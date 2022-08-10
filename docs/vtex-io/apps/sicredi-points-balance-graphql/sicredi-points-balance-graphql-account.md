---
title: "account Query"
slug: "sicredi-points-balance-graphql-account"
excerpt: "sicredi.points-balance-graphql@0.2.0"
hidden: true
createdAt: "2022-07-25T16:24:12.661Z"
updatedAt: "2022-07-25T16:24:12.661Z"
---
### Usage

This app provides a query to get the account user infos.

```graphql
query account($documentNumber: String!) {
  account(documentNumber: $documentNumber) {
    creditUnion
    branch
    number
    type
    product
    status
    brand
    source
    openingDate
    name
    documentNumber
    relationType
    isFavorite
  }
}
```