---
title: "Understanding VTEX reference architectures"
slug: "understanding-vtex-reference-architectures"
hidden: false
createdAt: "2024-05-20T10:45:55.338Z"
updatedAt: "2024-05-20T10:45:55.338Z"
excerpt: "Learn how each element is represented in VTEX reference architectures."
seeAlso:
 - "/docs/guides/store-architecture"
 - "/docs/guides/store-architecture-use-cases"
---

The VTEX reference architectures follow a common market methodology that segments the main agents involved in the solution in a simple, orderly, and logical manner. The structure of the design highlights the systems in blocks, colors, and objective descriptions of connections, facilitating visualization and understanding by all stakeholders.

In this guide, you will learn how each element is represented in the VTEX architectures, considering the [characteristics of the modules](#captions-colors-and-connections):

- [Macro elements: Layers](#macro-elements-layers)
- [Micro elements: Components](#micro-elements-components)
  - [Merchant Channels](#merchant-channels)
  - [VTEX Core Services](#vtex-core-services)
  - [Third-Party](#third-party)
  - [Back Office](#back-office)

## Captions, colors, and connections

Different colors are used to identify the characteristics of the modules presented, such as where they are executed and which involved part provides them.

Understand the meaning of each representation below:

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/Store-architecture/legend-and-colors.jpg)

1. **Module code developed exclusively by VTEX with execution in VTEX infrastructure**: Pink background and pink border.
2. **Module code not developed exclusively by VTEX (customizations) with execution in VTEX infrastructure**: White background and pink border.
3. **Module code not developed exclusively by VTEX (customizations) with execution outside VTEX infrastructure**: White background and black border.
4. **Back office services, which are executed outside VTEX infrastructure**: Gray background and black border.
5. **Optional module (e.g., Integration Layers)**: Dashed border.

The connection between modules and systems should be represented with arrows, which the arrowheads indicate the destination of the information and its return:

6. **Black arrows**: Used for asynchronous calls, which are not real-time.
7. **Blue arrows**: Used for synchronous calls, in real-time.

## Macro elements: Layers

The macro elements represent the entities involved in the project. In general, four major layers are considered: **Merchant Channels**, **VTEX Core Services**, **Third-Party**, and **Back Office**.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/Store-architecture/macro-elements-layers.jpg)

Within each of these blocks, there are micro elements, which are the components that constitute the project. These components can be modules, apps, integration systems, sellers, sales channels, or any other component relevant to the architecture.

## Micro elements: Components

Now equipped with knowledge about the macro elements, it is possible to understand the components that constitute the four major layers: [Merchant Channels](#merchant-channels), [VTEX Core Services](#vtex-core-services), [Third-Party](#third-party), and [Back Office](#back-office).

### Merchant Channels

The merchant channels are the different digital sales channels used by the store, such as the website, PWA, and mobile app.

From the architecture standpoint of ecommerce, the multiple channels should be highlighted to ensure that all stakeholders understand how the store interfaces with the end customer.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/Store-architecture/merchant-channels.jpg)

### VTEX Core Services

VTEX Core Services are the essential components or frameworks provided by VTEX within the platform. These services include modules such as [Catalog](https://developers.vtex.com/docs/guides/catalog-overview), [Order Management System (OMS)](https://developers.vtex.com/docs/guides/orders-overview), [Pricing](https://developers.vtex.com/docs/guides/pricing-overview), among others. They constitute the foundation of the VTEX platform, empowering businesses to effectively manage and conduct their ecommerce strategies.

Considering the architecture of a [B2C store](https://developers.vtex.com/docs/guides/store-architecture-use-cases), the diagram below presents the blocks with pink background and border, representing the native components of VTEX.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/Store-architecture/vtex-core-services.jpg)

Within the main block, there is the **VTEX IO - Apps** block, which contains the custom apps for [frontend](https://developers.vtex.com/docs/guides/vtex-io-documentation-1-developing-storefront-apps-using-react-and-vtex-io), [backend](https://developers.vtex.com/docs/guides/developing-services-on-vtex-io), and [Admin](https://learn.vtex.com/docs/course-admin-lang-en).

>ℹ️ Although they are executed in VTEX infrastructure, the development and maintenance of custom apps for frontend, backend, and VTEX Admin are responsibility of the store development team.

Also within the VTEX IO - Apps block, you will find the [VTEX App](https://developers.vtex.com/docs/vtex-io-apps), which are plug-and-play solutions developed and maintained by VTEX.

### Third-Party

Third-party systems or modules executed and maintained externally to VTEX include payment providers, data monitoring systems, and customization services. According to business needs, third-party systems or modules could replace a native VTEX feature or provide a completely new one.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/Store-architecture/third-party.jpg)

### Back office

An ecommerce operation may use several external systems to manage its resources and information, such as Enterprise Resource Planning (ERP), Customer Relationship Management (CRM), and Warehouse Management System (WMS), among others.

These systems belong to the [Merchant Back office](https://developers.vtex.com/docs/guides/erp-integration-guide) layer, as you can see in the following diagram:

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/Store-architecture/back-office.jpg)

