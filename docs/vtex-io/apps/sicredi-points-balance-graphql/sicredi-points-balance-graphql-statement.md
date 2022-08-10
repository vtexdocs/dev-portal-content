---
title: "statement Query"
slug: "sicredi-points-balance-graphql-statement"
excerpt: "sicredi.points-balance-graphql@0.2.0"
hidden: true
createdAt: "2022-07-25T16:24:12.632Z"
updatedAt: "2022-07-25T16:24:12.632Z"
---
### Usage

This app provides a query to get the statement user infos.

```graphql
query statement($walletId: String!) {
  statement(walletId: $walletId) {
    walletId
    from
    to
    page
    size
    sort {
      field
      direction
    }
    transactions {
      id
      type
      status
      title
      description
      createdDate
      amount
    }
  }
}
```