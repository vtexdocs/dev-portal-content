---
title: "Store theme"
slug: "novomodecol-novomodecol"
excerpt: "novomodecol.novomodecol@0.0.24"
hidden: true
createdAt: "2022-07-06T17:18:28.785Z"
updatedAt: "2022-08-04T20:36:15.157Z"
---
Our boilerplate theme to create stores in the VTEX IO platform.

## Preview
![store-theme-default](https://user-images.githubusercontent.com/1354492/63937047-e8d81c80-ca37-11e9-86fc-61e88847bbfb.png)

## Tutorial
To understand how things work check our tutorial [Build a store using VTEX IO](https://vtex.io/docs/getting-started/build-stores-with-store-framework/1/)

## Dependencies
All store components that you see on this document are open source too. Production ready, you can found those apps in this GitHub organization.

## Test form
To confirm that the forms we have created store information, we check it with the following query
https://novomodecol.myvtex.com/admin/graphql-ide / option -> vtex.store-graphql

query TestNews {
  documents(
      acronym: "NewsletterV2",
      fields: ["firstName", "emailAddress","birth","agreement","gender"],
      schema:"NewsletterVtexio") {
    fields {
      key
      value
    }
  }
}