---
title: "Factors Query"
slug: "sicredi-points-balance-graphql-factors"
excerpt: "sicredi.points-balance-graphql@0.2.0"
hidden: true
createdAt: "2022-07-25T16:24:12.601Z"
updatedAt: "2022-07-25T16:24:12.601Z"
---
### Usage

This app provides a query to get the factors values for cashback and points.

```graphql
query Factors {
  factors @context(provider: "sicred.points-balance-graphql") {
    key
    value
  }
}
```