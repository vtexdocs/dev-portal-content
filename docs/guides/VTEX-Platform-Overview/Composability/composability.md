---
title: "Composability"
slug: "composability"
hidden: false
createdAt: "2024-05-29T10:00:00.000Z"
updatedAt: ""
excerpt: "Understand what makes VTEX a Composable and Complete ecommerce solution."
---

Composability in ecommerce allows merchants to build and customize online shopping experiences by combining modular components or services. A composable commerce platform consists of loosely coupled microservices, enabling merchants to:

- Choose which services to use.
- Choose alternative service providers.
- Customize services.

In this guide, we will show VTEX’s approach to composability and provide an overview of the composable capabilities of the VTEX Commerce Platform.

## VTEX: Composable and complete

Our platform stands out for its composability and comprehensive features, offering a flexible and robust solution for digital commerce.


VTEX provides **composability** by:

- Allowing businesses to choose and customize services and integrations.
- Supporting native services and third-party providers.

VTEX offers a **complete** platform through:

- Core modules that support running a full ecommerce operation.
- Multiple combinations of native services, extensions, integrations, and add-ons.
- Development frameworks for creating custom solutions.

To take full advantage of our composable capabilities, we recommend using VTEX as the commerce engine and combining it with integrations, extensions, and add-ons. The platform is flexible enough so merchants can change the store configuration over time. Start using as many native features as possible, then gradually extend and exchange for external solutions.

Here are some features that demonstrate how VTEX is composable and complete:

- [750+ API endpoints](https://developers.vtex.com/docs/api-reference)
- 900+ live connections, including [payment providers](https://help.vtex.com/en/tutorial/list-of-payment-providers-by-country--2im3BEGXxSAcRuxEaIHPvp) and [marketplaces](https://help.vtex.com/en/tutorial/marketplace-strategies-at-vtex--tutorials_402#integrating-with-a-certified-marketplace)
- [No-code extensibility through the VTEX Admin](https://help.vtex.com/en/tracks/extensions-hub--AW7klkYMh557y5IUOgzco/3lWdpzjyhHVwzMC7pTG0QS)
- Services that emit [events](https://developers.vtex.com/docs/guides/services-2-handling-and-receiving-events) and [logs](https://help.vtex.com/en/tutorial/audit--5RXf9WJ5YLFBcS8q8KcxTA)
- [70+ decoupled microservices](https://developers.vtex.com/docs/guides)
- [Headless commerce](https://developers.vtex.com/docs/guides/headless-commerce)
- [Multi-tenant infrastructure](https://developers.vtex.com/docs/guides/cloud-infrastructure#saas-multi-tenancy)
- [Auto-scalable servers](https://developers.vtex.com/docs/guides/cloud-infrastructure#scalability)
- [Extensible VTEX IO apps](https://apps.vtex.com/)

## Pragmatic Composability

Pragmatic Composability is the digital commerce architectural approach that empowers merchants to leverage the native services of our ecommerce platform for their core needs and selectively compose custom-built and best-of-breed applications that will deliver a business advantage.

At VTEX, merchants can choose how composable their stores will be. They can be completely native, full of integrations and customizations, or something in between. Generalizing the many composition possibilities, we came up with four cases that represent the levels of composability regarding the commerce experience, illustrated below.

![Pragmatic composability](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/Composability/pragmatic-composability.png)

The most appropriate model will depend on the level of digital maturity and specialization needed for each business. In these cases, merchants use VTEX as the commerce engine and choose which components of the commerce experience will be decoupled.

It should also be noted that choosing a case or set of features at the beginning does not exclude the possibility of changing the architecture later. Adding new features and decoupling functions with third-party integrations is possible over time.

Learn more about each model in the following sections.

### Complete Platform

The complete platform case uses mostly VTEX's native features including frontend application and infrastructure, [CMS (Content Management System)](https://help.vtex.com/en/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/6OCY6S9tqBXPD5mgpbBInC), [Search](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/3qgT47zY08biLP3d5os3DG), [commerce modules](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/75MX4aorniD0BYAB8Nwbo7), and [APIs](https://developers.vtex.com/docs/guides/getting-started-list-of-rest-apis). This option often offers the quickest time to market and the lowest total cost of ownership. VTEX takes care of all maintenance and updates of its native modules, while also allowing frontend and backend customizations via [VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io) if merchants wish to create them.

### Headless Commerce

This case uses a Digital Experience Platform (DXP) decoupled from the native commerce infrastructure. As a single provider, the DXP usually handles the Storefront Application, Frontend Infrastructure, CMS, and Search & Personalization. A headless model with a single DXP provider is a good option to build a store’s frontend from scratch without having to handle multiple frontend systems and the commerce infrastructure.

> ℹ️ VTEX has a native service that allows developers to build headless storefronts: [FastStore](https://developers.vtex.com/docs/guides/faststore/docs-what-is-faststore), a starter headless storefront that uses VTEX infrastructure. FastStore can be customized, extended, and combined with [Headless CMS](https://developers.vtex.com/docs/guides/faststore/headless-cms-overview) and [Intelligent Search](https://help.vtex.com/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/3qgT47zY08biLP3d5os3DG).

### Frontend as a Service (FEaaS)

For companies looking for a specific search solution or CMS and who want to use the same content in several channels, the FEaaS option may be ideal. It is a common scenario where the company already uses a specific search provider or CMS before migrating to VTEX.

In this case, they can combine a third-party FEaaS provider with independent CMS and search solutions. This can become more expensive to use and maintain given the multiple systems involved and the need for orchestrating all of them.

> ℹ️ [FastStore](https://developers.vtex.com/docs/guides/faststore/docs-what-is-faststore) can also work as the FEaaS with third-party CMS and search solutions.

### Best of Breed

For maximum composability and flexibility, businesses with a mature development team or willing to pay specialized agencies may choose this model, selecting a best-of-breed provider for each commerce module. This option is the most appropriate when merchants want complete control over the deployment and infrastructure layers. Still, it means higher implementation time, increased costs, and the development of an API Gateway, or a Backend for Frontend (BFF) layer. In addition, it will require handling multiple vendors for integrations.

Projects of this kind may take years to implement, but merchants can progressively integrate each module. VTEX has the advantage of having native solutions for each module to achieve a faster time to market.

> ℹ️ Although we identify these four cases, pragmatic composability allows for many other combinations of composing your architecture.
