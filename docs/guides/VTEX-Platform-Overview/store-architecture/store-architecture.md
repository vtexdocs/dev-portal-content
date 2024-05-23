---
title: "Store architecture"
slug: "store-architecture"
hidden: false
createdAt: "2024-05-23T10:18:55.338Z"
updatedAt: "2024-05-23T10:18:55.338Z"
excerpt: "Learn about the VTEX reference architectures"
seeAlso:
 - "/docs/guides/understanding-vtex-reference-architectures"
 - "/docs/guides/store-architecture-use-cases"
---

Store architecture is the main way to communicate a unified vision of a particular project to all stakeholders, ensuring clarity for everyone involved and translating business needs into software components and project requirements.

There are different types and levels of architecture, but as a general rule, it should work as a reference for both technical and business teams. Moreover, store architectures define and make it clear to all stakeholders what are the roles and responsibilities of each player, how different systems interoperate, and how data is transmitted between them.

To enhance the understanding of the related aspects and show how VTEX connects with the ecosystem, we designed VTEX reference models of architecture, which are based on the more common digital commerce strategies. These reference architectures, also known as blueprints, are diagrams created to represent the interactions between VTEX modules and the business and are conceived as a starting point for a project. These reference architectures were designed following the guidelines which are in the [Understanding reference architectures](#LINK) guide.

>ℹ️ To learn more about the main characteristics of the accounts that relate to the planning of your store’s architecture, check out the [Accounts and architecture](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4yPqZQyj0t675QpcG7H6yl) guide.

Below are an overview of the main use cases for common scenarios:

- [Business-to-customer (B2C)](#business-to-customer-b2c)
- [Business-to-business (B2B)](#businesss-to-business-b2b)
- [Franchise accounts (Omnichannel)](#franchise-accounts-omnichannel)
- [Multi-language and Multi-currency](#multi-language-and-multi-currency)
  - [Single account, multi-bindings](#single-account-multi-bindings)
  - [Multi-account](#multi-account)

## Business-to-customer (B2C)

The business-to-customer (B2C) is the most common business model in VTEX and the base for the other business models.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/basic-b2c.png)

## Business-to-business (B2B) 

The main characteristic of a [business-to-business (B2B)](https://help.vtex.com/en/tutorial/b2b-overview--5vb9SNXhX2bZnkpAh7ADdC) model is that transactions occur between two or more legal entities.

B2B projects are usually more extensive and complex than projects in the B2C business model, as they often feature complex pricing structures, tailored product catalogs, customized user permissions, and extensive integrations with back office systems to manage various business operations effectively

Below, you can see a reference architecture of a B2B store using [B2B Suite](https://developers.vtex.com/docs/apps/vtex.b2b-suite).

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/Basic B2B.png)

## Franchise accounts (Omnichannel)

This is a very common architecture model that integrates physical stores with ecommerce as [franchise accounts](https://help.vtex.com/en/tutorial/what-is-a-franchise-account--kWQC6RkFSCUFGgY5gSjdl) in VTEX. 

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/franchises-omni.png)

## Multi-language and Multi-currency

Some of our customers are present in multiple countries and want to have every local store running on VTEX. To serve this customer, we provide the multi-language and multi-currency architectures.

### Single account, multi-bindings

In this architecture, there is a single VTEX account bound to multiple languages and currencies, in a [multidomain](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4yPqZQyj0t675QpcG7H6yl#multistore) perspective.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/multi-currency-language-single-account.png)

### Multi-account

In this architecture, there is a main VTEX account that will act as a seller in all secondary VTEX accounts, acting as [marketplaces](https://help.vtex.com/en/tutorial/estrategias-de-marketplace-na-vtex--tutorials_402#being-a-vtex-marketplace). These secondary accounts are conceived as [new environments](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4yPqZQyj0t675QpcG7H6yl#additional-environment).

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/multi-currency-language-multi-account.png)

>ℹ️ To deep dive into these store architectures, check out the [Store architecture use cases](https://developers.vtex.com/docs/guides/store-architecture-use-cases) guide.
