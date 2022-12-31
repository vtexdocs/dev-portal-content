---
title: "Overview"
slug: "external-search-provider-overview"
hidden: false
createdAt: "2020-09-11T16:46:12.406Z"
updatedAt: "2020-10-30T20:44:33.600Z"
---

# What is the VTEX Search Protocol

A search engine is a crucial part of e-commerce. It can drive more sales if the search results are good and it can worsen the user experience if they are bad.

Changing the search provider usually involved changing code both in the front-end and in the back-end, creating unnecessary friction.

The idea behind the VTEX search protocol is to provide a clear contract between any VTEX store on VTEX IO and a search provider defined by a GraphQL schema. This contract enables low-effort switching between different search engines. And it also helps to speed up the development process of integration with a new search provider, because the integration will be completely decoupled from the front-end components.

Search protocol benefits both developers and VTEX stores!

## How it Works

The **VTEX Search Protocol** is a set of definitions and GraphQL schemas that allows VTEX IO applications to serve **e-commerce search results** that can be used by VTEX Store Framework.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Integration%20Guides/search-integration-guide/b4ac10c-search-protocol_22.png)
Creating a **search-resolver** service app on VTEX IO, which implements VTEX Search Protocol, allows any VTEX Account using VTEX IO to **install such an application** and, instantly, **change the store's provider for search results.** This is really useful as no frontend modification is required. It's also possible to distribute the search provider on [VTEX App Store](https://apps.vtex.com/) to make the installation process even simpler.

### Search Schema

The **GraphQL schema** for VTEX Search Protocol defines the set of **queries** necessary for Store Framework to retrieve search information. This also includes the appropriate GraphQL types that any search resolver app should respond to.

You can check this schema on the **vtex.search-graphql** app [here](https://github.com/vtex-apps/search-graphql). The schema definition is on `graphql/schema.graphql` but there's also a reference on the repository's `README.md`.

## Implementation Pre-requisites

- Access to a user in a VTEX account, with permissions to link and install apps
- TypeScript and Node.js familiarity
- [GraphQL](https://graphql.org/) familiarity
[block:html]
{
  "html": "<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css\" integrity=\"sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm\" crossorigin=\"anonymous\">\n<script src=\"https://code.jquery.com/jquery-3.2.1.slim.min.js\" integrity=\"sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN\" crossorigin=\"anonymous\"></script>\n<script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js\" integrity=\"sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q\" crossorigin=\"anonymous\"></script>\n<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js\" integrity=\"sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl\" crossorigin=\"anonymous\"></script>\n\n\n<a href=\"search-integration-guide\"<button type=\"button\" class=\"btn btn-outline-secondary\">Back</button></a>\n\n<style></style>"
}
[/block]
