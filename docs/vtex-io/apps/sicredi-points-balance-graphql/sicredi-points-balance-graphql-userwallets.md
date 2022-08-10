---
title: "userWallets Query"
slug: "sicredi-points-balance-graphql-userwallets"
excerpt: "sicredi.points-balance-graphql@0.2.0"
hidden: true
createdAt: "2022-07-25T16:24:12.608Z"
updatedAt: "2022-07-25T16:24:12.608Z"
---
### Usage

This app provides a query to get the wallets user infos.

```graphql
query userWallets($documentNumber: String!, $creditUnion: String!) {
  userWallets(documentNumber: $documentNumber, creditUnion: $creditUnion) {
    documentNumber
    creditUnion
    wallets {
      id
      customerId
      productId
      documentNumber
      name
      branch
      creditUnion
      accountId
      balance
      status
    }
    totalBalance
    totalBalanceIntoCash
  }
}
```