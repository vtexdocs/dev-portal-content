---
title: "VTEX Composable Components"
slug: "vtex-composable-components"
hidden: false
createdAt: "2024-05-29T10:00:00.000Z"
updatedAt: ""
excerpt: "Learn about the components VTEX offers to build a composable store"
---

Various components are available in a VTEX store to fulfill the multiple types of digital commerce businesses. This guide details each component of the platform and explains their composable features.

![Composable architecture](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/Composability/composable-architecture.png)

In the tables below, each component is classified by type.

- **Built-in** type means that the component comes installed out-of-the-box with the VTEX store.
- **Plug-and-play** type means that the component does not come installed, but it can be installed with a few steps and, after configuration in some cases, it will be ready to use.
- If a component is neither **Built-in** nor **Plug-and-play**, it may require a more complex configuration or a development stage.

> ℹ️ The specific set of components used in a store will vary according to each scenario and business model. See the [Store architecture](https://developers.vtex.com/docs/guides/store-architecture) guide for more details about store implementation in specific scenarios.

If you want to experiment with composability and simulate building a store architecture, see the details in the [Interactive Marchitecture tool](https://developers.vtex.com/docs/guides/interactive-marchitecture-tool) guide.

## Commerce Platform

VTEX Commerce Platform provides a set of core commerce features out-of-the-box for Digital Commerce, Experience Management, Order Management, and Marketplace Management that help merchants start their operations smoothly and efficiently.

### Digital Commerce

<table>
  <tr>
    <td><b>Component</b></td>
    <td><b>Description</b></td>
    <td><b>Type</b></td>
  </tr>
  <tr>
    <td>Catalog</td>
    <td>In the <a href="https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/75MX4aorniD0BYAB8Nwbo7#catalog">Catalog</a>, merchants can manage the category tree (departments, categories, and subcategories), brands, products, SKUs, and specifications. Merchants can use this module natively through the Admin or <a href="https://developers.vtex.com/docs/api-reference/catalog-api">Catalog API</a>, import the data from a spreadsheet, or integrate it with an external back office tool. For more details, see <b>ERP</b> and <b>PIM/CPQ</b> in <a href="#integrations">Integrations</a>.</td>
    <td>Built-in</td>
  </tr>
  <tr>
    <td>Price</td>
    <td>
      In the <a href="https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/75MX4aorniD0BYAB8Nwbo7#prices">Prices module</a>, merchants can manage price details for the store's SKUs. Merchants can use this module natively through the Admin or <a href="https://developers.vtex.com/docs/api-reference/pricing-api">Pricing API</a>, import the data from a spreadsheet, or integrate it with an external back office tool. For more details, see <b>ERP</b> and <b>PIM/CPQ</b> in <a href="#integrations">Integrations</a>.<br><br>
      There are options to use only fixed prices or modify them for different contexts including trade policies, customer groups, and promotions.<br><br>
      There is also the option to use the <a href="https://developers.vtex.com/docs/guides/pricing-hub-overview">Pricing Hub</a>, where merchants store the prices in an external platform integrated with VTEX, so they are accessed via Checkout.
    </td>
    <td>Built-in</td>
  </tr>
  <tr>
    <td>Promotions</td>
    <td>The <a href="https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/75MX4aorniD0BYAB8Nwbo7#promotions">Promotions</a> module manages discounts on store customers' shopping carts. It is also responsible for dealing with <a href="https://help.vtex.com/en/tutorial/creating-surchargestaxes--tutorials_321">taxes</a>. Discounts can be applied in many ways including specific products, target audiences, bundles, shipping, or coupons. Merchants can use this module natively through the Admin or <a href="https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api">Promotions & Taxes API</a>.</td>
    <td>Built-in</td>
  </tr>
  <tr>
    <td>Checkout</td>
    <td>
      The <a href="https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/3MYcZaojb5HSUg6ufm6GxQ#checkout">Checkout</a> module is responsible for the shopping cart. It coordinates data from Catalog, Price, Promotions, Logistics, and Payments to complete the purchase process and place orders. There are many customization options such as optimization of shipping options, geolocation shipping calculation, abandoned cart, UI customization, and others.<br><br>
      With the <a href="https://developers.vtex.com/docs/api-reference/checkout-api">Checkout API</a>, it is possible to develop custom solutions with <a href="https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io">VTEX IO</a> or <a href="https://developers.vtex.com/docs/guides/headless-cart-and-checkout">headless implementation</a>.
    </td>
    <td>Built-in</td>
  </tr>
  <tr>
    <td>Payment Gateway</td>
    <td>
      The <a href="https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/3MYcZaojb5HSUg6ufm6GxQ#payments">Payments</a> module configures the payment conditions and deals with the transactions. Within this module is our <a href="https://help.vtex.com/en/tutorial/what-is-a-payment-gateway--2KH9Wdi7F6swOU4amECSOk">Payment Gateway</a>, which transmits the payment data using <a href="https://help.vtex.com/en/tutorial/what-is-the-connector--3lze0Cu0bmyC6u2o2iaeEA">connectors</a> from various payment providers. The VTEX Payment Gateway is mandatory, but the merchant can choose the providers for payment processing. For more details, see <b>Payments</b> in <a href="#integrations">Integrations</a>.<br><br>
      Besides having the basic payment functionalities, merchants can add <a href="https://help.vtex.com/en/tutorial/what-is-anti-fraud--69SjFCc4rC6Ii0OMAeYAsG">anti-fraud providers</a>, <a href="https://help.vtex.com/en/tutorial/customer-credit-overview--1uIqTjWxIIIEW0COMg4uE0">Customer Credit</a>, <a href="https://help.vtex.com/en/tutorial/what-is-an-e-wallet--4v5wcOe4A0SiaimWM2cU60">digital wallets</a>, and <a href="https://help.vtex.com/en/tutorial/gift-card--tutorials_995">gift cards</a> to the payment experience.
    </td>
    <td>Built-in</td>
  </tr>
  <tr>
    <td>Channel Management</td>
    <td>
      At VTEX, we have <a href="https://help.vtex.com/en/tracks/unified-commerce-strategies--3WGDRRhc3vf1MJb9zGncnv/2LGAiUnHES1enjHsfi8fI3">Unified Commerce Strategies</a> to deal with different sales channels. Merchants can sell through multiple channels including directly from their website, physical stores, Sales App, and more. This strategy allows all the data (order processing, payment transactions, etc.) to be shared between channels and accessible from the Admin. Besides that, order processing and fulfillment can be mixed between channels. For instance, an ecommerce sale can have the option to pick up specific items in the physical store, or a physical store sale can be delivered to the customer’s address.<br><br>
      Among the available sales channel options, we have the <a href="https://help.vtex.com/en/tutorial/marketplace-strategies-at-vtex--tutorials_402">Marketplace Strategies</a>, which allows merchants to sell products on marketplaces, or for their store to become a marketplace and sell products from sellers.
    </td>
    <td>Built-in</td>
  </tr>
  <tr>
    <td>B2B Organizations</td>
    <td><a href="https://developers.vtex.com/docs/apps/vtex.b2b-organizations">B2B Organizations</a> is a <a href="https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-a-vtex-app">VTEX IO app</a> from the <a href="https://developers.vtex.com/docs/apps/vtex.b2b-organizations">B2B Suite</a>. It enables merchants to group B2B (Business-to-Business) users into organizations and apply specific custom payment methods, product selections, and prices for customers of the same organization. Each organization is further segmented into one or more cost centers, with their shipping addresses, which will be available for cost center users at checkout.</td>
    <td>Plug-and-play</td>
  </tr>
  <tr>
    <td>Request for Quote</td>
    <td><a href="https://developers.vtex.com/docs/apps/vtex.b2b-quotes">Request for Quote</a> is a <a href="https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-a-vtex-app">VTEX IO app</a> from the <a href="https://developers.vtex.com/docs/apps/vtex.b2b-organizations">B2B Suite</a>. It allows B2B users to create quotes and saved carts, which are then shared with the other members of their organization. This enables price negotiations between them and the store’s sales representatives, and order approval flows within their organization.</td>
    <td>Plug-and-play</td>
  </tr>
</table>

### Experience Management

<table>
  <tr>
    <td><b>Component</b></td>
    <td><b>Description</b></td>
    <td><b>Type</b></td>
  </tr>
  <tr>
    <td>Headless CMS</td>
    <td><a href="https://developers.vtex.com/docs/guides/faststore/headless-cms-overview">Headless CMS</a> is part of our <a href="https://developers.vtex.com/docs/guides/faststore/docs-what-is-faststore">FastStore toolkit</a>. It allows merchants to store content in a decoupled data layer and deliver it as structured data to a VTEX store with FastStore via an API.</td>
    <td>Requires implementation</td>
  </tr>
  <tr>
    <td>Intelligent Search</td>
    <td>
      <a href="https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/3qgT47zY08biLP3d5os3DG">Intelligent Search</a> is a native VTEX platform search solution, working regardless of the channel (website, mobile app, conversational, etc.). Its features include autocomplete, filters, synonyms, and relevance rules. To add Intelligent Search to a store, install the <a href="https://developers.vtex.com/docs/apps/vtex.search">Search app</a>.<br><br>
      Besides Intelligent Search, it is possible to integrate third-party search solutions into a VTEX store. For more details, see <b>Search & Personalization</b> in <a href="#integrations">Integrations</a>.
    </td>
    <td>Yes</td>
  </tr>
  <tr>
    <td>Storefront Application</td>
    <td>VTEX has alternatives for storefront applications. For <a href="https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/67SCtUreXxKYWhZh8n0zvZ">website frontend implementation</a>, we have Store Framework and FastStore. Merchants can also build a complete custom solution, e.g., a custom mobile app, using our <a href="https://developers.vtex.com/docs/api-reference">APIs</a>.</td>
    <td>No</td>
  </tr>
  <tr>
    <td>PWA Application</td>
    <td>Progressive Web Application (PWA) is natively available for every VTEX IO store. Merchants can configure a push notification to install the store’s PWA on the customer’s device. For more details, see <a href="https://help.vtex.com/en/tutorial/enabling-pwa-push-notifications-in-your-store--1be3ZPhbsgZSbE7h5H46pG">Enabling PWA push notifications in your store</a>.</td>
    <td>Built-in</td>
  </tr>
</table>

### Distributed Order Management

<table>
  <tr>
    <td><b>Component</b></td>
    <td><b>Description</b></td>
    <td><b>Type</b></td>
  </tr>
  <tr>
    <td>Inventory Management</td>
    <td>
      <a href="https://help.vtex.com/en/tutorial/managing-stock-items--tutorials_139">Inventory management</a> is a page in the Admin where merchants can view SKU (Stock Keeping Unit) inventory data and define SKU quantities in <a href="https://help.vtex.com/en/tutorial/warehouse--6oIxvsVDTtGpO7y6zwhGpb">warehouses</a>.<br><br>
      Also, merchants can <a href="https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/7euXDZR5CCnVFSrXyczIhu#inventory">import inventory data</a> from spreadsheets or through the <a href="https://developers.vtex.com/docs/api-reference/logistics-api">Logistics API</a>, which allows integration with external tools. For more details, see <b>ERP</b>, <b>OMS/WMS</b>, and <b>PIM/CPQ</b> in <a href="#integrations">Integrations</a>.
    </td>
    <td>Built-in</td>
  </tr>
  <tr>
    <td>Logistics</td>
    <td>
      The <a href="https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/75MX4aorniD0BYAB8Nwbo7#logistics">Logistics</a> module is responsible for managing the transportation and storage of merchandise, and shipping orders to customers. The main set of configurations in Logistics is the Shipping strategy, which comprises shipping policies, warehouses, and loading docks.<br><br>
      Merchants can make all the configurations in the Admin or through the <a href="https://developers.vtex.com/docs/api-reference/logistics-api">Logistics API</a>, which allows integrations with external tools. For more details, see <b>ERP</b>, <b>OMS/WMS</b>, and <b>PIM/CPQ</b> in <a href="#integrations">Integrations</a>.<br><br>
      Also, merchants can choose the carriers in the <a href="https://help.vtex.com/en/tutorial/shipping-policy--tutorials_140">shipping policy</a>. For more details, see <b>Carriers</b> in <a href="#integrations">Integrations</a>.
    </td>
    <td>Built-in</td>
  </tr>
  <tr>
    <td>Shipping Network</td>
    <td>
      <a href="https://help.vtex.com/en/tutorial/vtex-shipping-network-dashboard--51e8tx1IehiN4ZtURRWU92">VTEX Shipping Network</a> is an <a href="https://help.vtex.com/tracks/next-steps-after-the-go-live--3J7WFZyvTcoiwkcIVFVhIS/1t2QBZvrOBSLgvHaAV9fYm">add-on</a> that offers the option of connecting carriers to create an integrated delivery network. It gathers order tracking data directly from carriers, keeping merchants and their customers up to date. Its Admin dashboards show a managerial view of the shipping costs and the revenue from the shipping rates.<br><br>
      ⚠️ <i>This feature is only available in Brazil.</i>
    </td>
    <td>Yes</td>
  </tr>
</table>

### Marketplace Management

<table>
  <tr>
    <td><b>Component</b></td>
    <td><b>Description</b></td>
    <td><b>Type</b></td>
  </tr>
  <tr>
    <td>Seller Management</td>
    <td><a href="https://help.vtex.com/en/tutorial/seller-management--6eEiOISwxuAWJ8w6MtK7iv">Seller Management</a> is a VTEX Admin page where marketplace operators can <a href="https://help.vtex.com/en/tutorial/adicionar-seller--tutorials_392">add sellers</a>, input their information, and manage their status. The page features metrics that allow marketplaces to assess their operation. It supports both VTEX sellers with a VTEX account, and external sellers integrated with VTEX. For more details, see <b>Third-party Sellers</b> in <a href="#integrations">Integrations</a>.</td>
    <td>Built-in</td>
  </tr>
  <tr>
    <td>Offer Quality & Management</td>
    <td>
      The <a href="https://help.vtex.com/en/tutorial/offer-management--7MRb9S78aBdZjFGpbuffpE">Offer Management</a> module allows sellers to track the sending and syncing of their offers on all sales channels integrated with the store in the Admin. At VTEX, an offer is a SKU from a seller that has been sent to a sales channel with price and inventory information configured.<br><br>
      It allows tracking offers sent to the following channels: <a href="https://help.vtex.com/en/tracks/configurar-integracao-do-mercado-livre--2YfvI3Jxe0CGIKoWIGQEIq">Mercado Libre</a>, <a href="https://help.vtex.com/en/tracks/configurar-integracao-da-netshoes--5Ua87lhFg4m0kEcuyqmcCm">Netshoes</a>, and VTEX marketplaces. Other marketplaces can add support to Offer Management in their connectors by using the <a href="https://developers.vtex.com/docs/api-reference/marketplace-apis-offer-management">Offer Management API</a> and following the <a href="https://developers.vtex.com/docs/guides/sent-offers-integration-guide-connectors">Offer Management integration guide</a>.<br><br>
      <a href="https://help.vtex.com/en/tutorial/offer-quality-filters--4xm0gi8leCyxHj8YdgHSJH">Offer Quality Filters</a> is an Admin page where marketplaces add and manage the requirement groups applied to the received SKU cataloging process. Marketplaces can create and apply mandatory and optional requirements on this page to filter the sellers’ offers.
    </td>
    <td>Built-in</td>
  </tr>
  <tr>
    <td>Seller Portal</td>
    <td>
      <a href="https://help.vtex.com/en/tutorial/seller-portal-getting-started-for-the-marketplace--6ccErY3mCcfoW0qGXf167">Seller Portal</a> is an edition of the VTEX platform for VTEX or third-party sellers to connect and sell their products on marketplaces. The portal provides sellers with the essential capabilities for ecommerce operations like catalog, prices, logistics, and order management. It also has a dashboard that shows sales performance and allows integration with ERP.<br><br>
      We also have the <a href="https://developers.vtex.com/docs/guides/seller-portal-edition-app">Seller Portal Edition App</a>, which allows VTEX marketplaces to create a customized Seller Portal.
    </td>
    <td>Built-in</td>
  </tr>
  <tr>
    <td>Marketplaces and Integrations</td>
    <td>
      <a href="https://help.vtex.com/en/tutorial/marketplaces-and-integrations--5AcBO1t29nhq7rBHas9b6V">Marketplaces and Integrations</a>, previously known as Marketplace Network, is a page in the Admin with a catalog of companies interested in partnerships. This page allows registration, search, and contact between marketplaces and sellers to sign commercial agreements. There are both VTEX and external marketplaces available.<br><br>
      VTEX marketplaces are VTEX customers that choose to make their environment available for sellers to sell products. After a merchant <a href="https://help.vtex.com/en/tutorial/configuring-vtex-marketplace--7splyp5MqIyt2Iyz5jsNzb">configures their VTEX store to become a marketplace</a>, it will be available for sellers to connect at the <b>Marketplaces and Integrations</b> page.<br><br>
      External marketplaces are marketplace stores that are not VTEX customers and, after <a href="https://developers.vtex.com/docs/guides/external-marketplace-integration-guide">developing a connector</a> to integrate with VTEX, they become available for sellers to connect at the <b>Marketplaces and Integrations</b> page. For more details, see <b>Third-Party Marketplaces</b> in <a href="#integrations">Integrations</a>.
    </td>
    <td>Built-in</td>
  </tr>
</table>

## Platform interaction

There are two ways for merchants to interact with a VTEX store: VTEX Admin and Developer Tooling.

### VTEX Admin

A panel to manage the entire digital commerce experience in one place with a complete feature set out-of-the-box. The [Admin](https://help.vtex.com/en/tutorial/vtex-admin-start-here--531cHtUCUi3puRXNDmKziw) has pages with dashboards, settings, and detailed information from our [core modules](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/75MX4aorniD0BYAB8Nwbo7). For instance, in the Admin, merchants can manage catalog, prices, and inventory, add payment options, view transactions, order status, customer data, sales performance, and more. Adding new features in the Admin to the store is also possible through the Extensions Hub.

<table>
  <tr>
    <td><b>Component</b></td>
    <td><b>Description</b></td>
    <td><b>Type</b></td>
  </tr>
  <tr>
    <td>Dashboards</td>
    <td>
      <a href="https://help.vtex.com/en/tutorial/dashboards-overview--1yn2nZUoXtDO3teTEJsCNl">Dashboards</a> is a section in the Admin that centralizes the dashboard pages, which display analytical data for the store’s unified commerce. Three dashboards are available:
      <ul>
        <li><a href="https://help.vtex.com/en/tutorial/store-overview--P8ahguoRs0U3PzmXg2wuQ">Overview</a>: Shows key metrics that impact the store revenue. It has charts about the evolution of sales, conversion rate, and sales funnel.</li>
      </ul>
      <ul>
        <li><a href="https://help.vtex.com/en/v4/docs/sales-performance--6gx46RGRzWO8qgaVck7PRp">Sales Performance</a>: Shows and analyzes order data from stores and sellers, in the case of stores that <a href="https://help.vtex.com/en/tutorial/marketplace-strategies-at-vtex--tutorials_402#acting-as-a-marketplace">operate as marketplaces</a>.</li>
      </ul>
      <ul>
        <li><a href="https://help.vtex.com/en/v4/docs/web-page-performance--7DeyhX8cGtG9PtAGkL8zvc">Web Page Performance</a>: Uses <a href="https://developers.google.com/speed/docs/insights/v5/about">Google's PageSpeed Insights</a> tool to track the performance of the store’s URLs.</li>
      </ul>
    </td>
    <td>Built-in</td>
  </tr>
  <tr>
    <td>Releases</td>
    <td>
      <a href="https://help.vtex.com/en/tutorial/planner-release-concept-beta--4pWhQTXG0aIIsi2TYxxRkZ">Releases</a> is a <a href="https://www.faststore.dev/">FastStore</a> feature that allows the efficient management of changes to a store. A release is a change or a group of changes that can be published together. This feature includes two pages:
      <ul>
        <li><a href="https://help.vtex.com/en/tutorial/planner-releases-page-beta--2p7IiVD6K8i1iRiwHph5sw">Releases</a>: This page lists all existing releases. It allows several <a href="https://help.vtex.com/en/tutorial/planner-actions-on-releases-beta--1zsomdifPEQkdV6RW93JyW">actions</a> including creation, scheduling, publishing, and deleting releases.</li>
      </ul>
      <ul>
        <li><a href="https://help.vtex.com/en/tutorial/planner-calendar-page-beta--46wSZ7Z5xoXQPP0xHfIx9C">Calendar</a>: This page shows a calendar of releases per month, week, or day. It allows merchants to see the releases on their publication date or time, access their details, and create new releases.</li>
      </ul>
    </td>
    <td>Built-in, after installing FastStore</td>
  </tr>
  <tr>
    <td>User & Account Management</td>
    <td>
      The <a href="https://help.vtex.com/tutorial/account-management--2vhUVOKfCaswqLguT2F9xq">Account page</a> allows merchants to view and manage their VTEX account details, such as the company’s logo, trading name, legal name, and the stores in the account.<br><br>
      On the <a href="https://help.vtex.com/tutorial/managing-users--tutorials_512">Users page</a>, merchants can view and manage Admin users. When creating or editing users, merchants can choose their <a href="https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc">roles</a>, which define what a user can access.
    </td>
    <td>Built-in</td>
  </tr>
  <tr>
    <td>Extensions Hub</td>
    <td>
      At VTEX, extensions are tools designed to expand VTEX’s stores out-of-the-box capabilities. Extensions include <a href="https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-a-vtex-app">VTEX IO apps</a>, <a href="https://help.vtex.com/en/tutorial/what-is-the-connector--3lze0Cu0bmyC6u2o2iaeEA">payment connectors</a>, <a href="https://help.vtex.com/en/tutorial/integrating-with-marketplace">marketplace integrations</a>, and others. The <a href="https://help.vtex.com/en/tracks/extensions-hub--AW7klkYMh557y5IUOgzco/3lWdpzjyhHVwzMC7pTG0QS">Extensions Hub</a> is a section of the Admin that centralizes the management of extensions. It has the following pages:
      <ul>
        <li><b>App Store:</b> A page where merchants can find and acquire apps, giving additional functionalities to their stores. Some apps are free, and others are paid. There are apps developed by VTEX and by <a href="https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4yPqZQyj0t675QpcG7H6yl#implementation-partners">implementation partners</a>.</li>
      </ul>
      <ul>
        <li><b>App Management:</b> This page shows the installed apps in the account and allows merchants to install, configure, uninstall, and delete apps.</li>
      </ul>
    </td>
    <td>Built-in</td>
  </tr>
</table>

### Developer Tooling

Various tools to create new features for the VTEX platform. Development can be done by the merchant’s tech team or by [partner agencies](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4yPqZQyj0t675QpcG7H6yl#implementation-partners). There are many ways to build new features at VTEX including apps and storefront features using [VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io), custom behaviors with data in [Master Data](https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw), and [integrations](#integrations) using our [APIs](https://developers.vtex.com/docs/api-reference), which extend VTEX’s out-of-the-box capabilities.

<table>
  <tr>
    <td><b>Component</b></td>
    <td><b>Description</b></td>
    <td><b>Type</b></td>
  </tr>
  <tr>
    <td>VTEX IO Storefront Platform</td>
    <td>
      VTEX has the following technologies for <a href="https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/67SCtUreXxKYWhZh8n0zvZ#frontend-development-technologies-on-vtex">storefront development</a>:
      <ul>
        <li><a href="https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-store-framework">Store Framework</a>: A technology framework for storefront implementation focused on the composable commerce model. It allows the combination of different VTEX IO apps to build a storefront. With this technology, the store's implementation is based on pre-built components, also known as blocks, and component customization is made for specific business needs. This framework is based on React, TypeScript, Node.js, and GraphQL.</li>
      </ul>
      <ul>
        <li><a href="https://developers.vtex.com/docs/guides/faststore/docs-what-is-faststore">FastStore</a>: Our newer storefront technology to create stores focused on performance and stability. It is an open-source toolkit based on <a href="https://react.dev/">React</a> and the <a href="https://jamstack.org/">Jamstack</a> architecture. It has many features that enhance the development experience including a starting template, headless technology, Admin UI panels for management, and integration with GitHub.</li>
      </ul>
    </td>
    <td>Built-in</td>
  </tr>
  <tr>
    <td>APIs</td>
    <td>VTEX is an API-first platform with 750+ endpoints. <a href="https://developers.vtex.com/docs/api-reference">VTEX REST APIs</a> allow interaction with over 70 microservices to build custom solutions, such as <a href="#integrations">integrations</a> and <a href="https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-a-vtex-app">VTEX IO apps</a>. Using our APIs requires <a href="https://developers.vtex.com/docs/guides/authentication">Authentication</a> with keys or tokens for users and integrations. IO apps can use the APIs through <a href="https://developers.vtex.com/docs/guides/vtex-io-documentation-clients">clients</a>. See our <a href="https://developers.vtex.com/docs/guides">API guides</a> for details on how to use our APIs for specific scenarios.</td>
    <td>Built-in</td>
  </tr>
  <tr>
    <td>Master Data Management</td>
    <td>
      <a href="https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw">Master Data</a> is a VTEX highly customizable database platform. It allows merchants to store, search, expand, and customize data. There are two versions available: v1 and v2. The main differences are that v1 has a graphical interface and v2 uses <a href="https://developers.vtex.com/docs/guides/starting-to-work-on-master-data-with-json-schema">JSON schemas</a> for structuring data. <a href="https://developers.vtex.com/vtex-rest-api/reference/master-data-api-v2-overview">Master Data’s API</a> enables integration with external systems and applications, such as IO apps.<br><br>
      Master Data has a <a href="https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw#triggers">trigger</a> mechanism that allows custom behaviors with data interaction. For instance, merchants can configure to send an email or an HTTP request when a customer's data changes.
    </td>
    <td>Built-in</td>
  </tr>
  <tr>
    <td>VTEX IO App Platform</td>
    <td>
      <a href="https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io">VTEX IO</a> is a development platform with high-performance management, scalability, and robust security. It offers the tools to develop, manage, install, and deploy <a href="https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-a-vtex-app">apps</a>, allowing the creation of custom solutions that extend the VTEX platform capabilities. Many app types are available for different scenarios, including storefront themes and components, Admin apps, and backend services.<br><br>
      VTEX offers a wide range of <a href="https://developers.vtex.com/docs/vtex-io-apps">readily available apps</a> that merchants can install and developers can use as <a href="https://developers.vtex.com/docs/guides/vtex-io-documentation-dependencies">dependencies</a>.<br><br>
      Developers can <a href="https://developers.vtex.com/docs/guides/vtex-io-documentation-submitting-your-app-in-the-vtex-app-store">make their apps publicly available</a> in the <a href="https://help.vtex.com/en/tracks/extensions-hub--AW7klkYMh557y5IUOgzco/2LDRvGujYsumxi7IlE7CEJ">App Store</a>, enabling merchants to install these apps on their stores.<br><br>
      See our <a href="https://developers.vtex.com/docs/guides/developer-experience">Developer Experience</a> guide and <a href="https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/7euXDZR5CCnVFSrXyczIhu#extensions-and-apps">Extensions and apps overview</a> for more details about developing and using IO apps.
    </td>
    <td>Built-in</td>
  </tr>
</table>

## Integrations

Integrations allow external providers to provide their solutions for VTEX stores by leveraging [VTEX APIs](https://developers.vtex.com/docs/api-reference). Many integrations are readily available from our partner ecosystem, which merchants only need to install and configure before using. It is also possible to develop new integrations following our integration guides or to request from our [partners](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4yPqZQyj0t675QpcG7H6yl#implementation-partners). For more information about how integrations work, see our [Backend integrations overview](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/7euXDZR5CCnVFSrXyczIhu) and the **Integration Guides** section in our [Developer Portal](https://developers.vtex.com/docs/guides). The types of integrations available at VTEX are:

<table>
  <tr>
    <td><b>Component</b></td>
    <td><b>Description</b></td>
    <td><b>Type</b></td>
  </tr>
  <tr>
    <td>ERP</td>
    <td>
      ERP (Enterprise Resource Planning) is the main back office software, responsible for managing the essential parts of the operation related to Catalog, Pricing, Logistics, and Orders.<br><br>
      Some parts of the operation that an ERP deals with can be delegated to other software types: A <b>WMS</b> can manage Logistics, a <b>PIM</b> can manage Catalog, and a <b>CPQ</b> can manage Pricing. See the details about integration with these software types below in this table.<br><br>
      An ERP integrates with VTEX to exchange data and give commands. These integrations are implemented using the APIs from each module (<a href="https://developers.vtex.com/docs/api-reference/catalog-api">Catalog</a>, <a href="https://developers.vtex.com/docs/api-reference/pricing-api">Pricing</a>, <a href="https://developers.vtex.com/docs/api-reference/logistics-api">Logistics</a>, and <a href="https://developers.vtex.com/docs/api-reference/orders-api">Orders</a>). The integration is done in two phases, an initial setup for importing product-related data, and a middleware setup for configuring the order processing.<br><br>
      Merchants can choose which ERP to use with VTEX, and what parts of the operation they want to integrate. Some ERPs in the market already have an integration implemented with VTEX, so merchants only need to configure through the UI. Otherwise, the integration must be developed by the merchant technical team or an <a href="https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4yPqZQyj0t675QpcG7H6yl#implementation-partners">implementation partner</a>.<br><br>
      For details about implementing ERP integrations, see <b>ERP integration</b> in our <a href="https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/7euXDZR5CCnVFSrXyczIhu#erp-integration">Backend integrations overview</a> and our <a href="https://developers.vtex.com/docs/guides/erp-integration-guide">Back office integration</a> guide.
    </td>
    <td>Plug-and-play if the ERP integration is implemented. Requires implementation otherwise.</td>
  </tr>
  <tr>
    <td>OMS/WMS</td>
    <td>
      OMS (Order Management System) is a tool to handle order processing. VTEX has its own OMS, but merchants can integrate external software, usually an ERP, with the <a href="https://developers.vtex.com/docs/api-reference/orders-api">Orders API</a> to receive order events and handle order processing. There are two types of order integrations for receiving order events:
      <ul>
        <li>Feed: the external software reads a queue of order events.</li>
      </ul>
      <ul>
        <li>Hook: the external software receives automatic notifications about order updates.</li>
      </ul>
      After receiving an event, the external software handles the order with various possible actions and returns the result to VTEX’s OMS. It is possible to change, cancel, invoice, and track an order during handling.<br><br>
      For details about implementing integrations with our OMS, see <b>Middleware configuration</b>, <b>Order integration</b>, and <b>Order Processing</b> in our <a href="https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/7euXDZR5CCnVFSrXyczIhu">Backend integrations overview</a>, <a href="https://developers.vtex.com/docs/guides/orders-feed">Feed v3</a>, <a href="https://developers.vtex.com/docs/guides/erp-integration-set-up-order-integration">Set up order integration</a>, and <a href="https://developers.vtex.com/docs/guides/erp-integration-set-up-order-integration">Setup order processing</a> guides.<br><br>
      WMS (Warehouse Management System) is a back office software responsible for inventory and logistics management of the operation. At VTEX, integrations with this software send inventory data (warehouses and SKU amounts). For more details, see <b>Inventory</b> in our <a href="https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/7euXDZR5CCnVFSrXyczIhu#inventory">Backend integrations overview</a>, and our <a href="https://developers.vtex.com/docs/guides/erp-integration-import-inventory">Import inventory</a> guide.
    </td>
    <td>Plug-and-play if the OMS/WMS integration is implemented. Requires implementation otherwise.</td>
  </tr>
  <tr>
    <td>PIM/CPQ</td>
    <td>
      PIM (Product Information Manager) is a back office software that deals with catalog and product data. At VTEX, PIM integrations can send information about the <a href="https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/7euXDZR5CCnVFSrXyczIhu#category-tree">category tree</a>, brands, products, SKUs, and specifications using the <a href="https://developers.vtex.com/docs/api-reference/catalog-api">Catalog API</a>. For more details, see <b>Catalog architecture</b> and <b>Importing products</b> in our <a href="https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/7euXDZR5CCnVFSrXyczIhu">Backend integrations overview</a>, <a href="https://developers.vtex.com/docs/guides/erp-integration-set-up-catalog">Set up catalog</a>, and <a href="https://developers.vtex.com/docs/guides/erp-integration-import-products">Import products</a> guides.<br><br>
      CPQ (Configure Price Quote) is a back office software that deals with product prices. At VTEX, CPQ integrations can send information about the product prices using the <a href="https://developers.vtex.com/docs/api-reference/pricing-api">Pricing API</a>. For more details, see <b>Prices</b> in our <a href="https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/7euXDZR5CCnVFSrXyczIhu#prices">Backend integrations overview</a>, and our <a href="https://developers.vtex.com/docs/guides/erp-integration-import-prices">Import prices</a> guide.
    </td>
    <td>Plug-and-play if the PIM/CPQ integration is implemented. Requires implementation otherwise.</td>
  </tr>
  <tr>
    <td>CRM</td>
    <td>
      CRM (Customer Relationship Management) is software that helps track information and interactions between a company and its customers. At VTEX, customer data is usually stored in <a href="https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw">Master Data v1</a>. CRM integrations can send customer data (name, email, address, ID number, etc.) to VTEX using the <a href="https://developers.vtex.com/docs/api-reference/masterdata-api">Master Data v1 API</a>. For more details, see <b>Customer data</b> in our <a href="https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/7euXDZR5CCnVFSrXyczIhu#middleware-configuration">Backend integrations overview</a>, and our <a href="https://developers.vtex.com/docs/guides/erp-integration-import-prices">Import prices</a> guide.<br><br>
      For more details, see <b>Customer data</b> in our <a href="https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/7euXDZR5CCnVFSrXyczIhu#middleware-configuration">Backend integrations overview</a>, and our <a href="https://developers.vtex.com/docs/guides/import-customer-data">Import customer data</a> guide.
    </td>
    <td>Plug-and-play if the CRM integration is implemented. Requires implementation otherwise.</td>
  </tr>
  <tr>
    <td>Third-Party Marketplaces</td>
    <td>
      VTEX <a href="https://help.vtex.com/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w">sellers</a> can offer their products on VTEX and third-party/external <a href="https://help.vtex.com/en/tutorial/what-is-a-marketplace--680lLJTnmEAmekcC0MIea8">marketplaces</a>. See the list of external marketplaces available at <a href="https://help.vtex.com/en/tutorial/estrategias-de-marketplace-na-vtex--tutorials_402#integrating-with-a-certified-marketplace">Marketplace strategies at VTEX</a>.<br><br>
      For marketplaces not integrated with VTEX but want to offer products from VTEX sellers, a custom connector can be developed for this integration. VTEX provides a set of APIs and instructions to facilitate the process. For more information, see our <a href="https://developers.vtex.com/docs/guides/external-marketplace-integration-guide">External Marketplace</a> integration guide.
    </td>
    <td>Plug-and-play if the marketplace integration is implemented. Requires implementation otherwise.</td>
  </tr>
  <tr>
    <td>Search & Personalization</td>
    <td>
      By default, VTEX offers <a href="https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/3qgT47zY08biLP3d5os3DG">Intelligent Search</a> as a search engine, but merchants can use other search solutions instead. Our <a href="https://developers.vtex.com/docs/guides/search-integration-guide">Search Protocol</a> enables third-party search solutions to integrate with VTEX. The protocol allows integration with the minimum amount of work and VTEX customers to easily switch between search providers without changes in the storefront.<br><br>
      At its core, the Search Protocol is a set of definitions and GraphQL schemas that allows IO apps to serve ecommerce search results that can be used by the <a href="https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-store-framework">VTEX Store Framework</a>.<br><br>
      For easy integration of already implemented solutions, you can find search provider apps on the <a href="https://apps.vtex.com">App Store</a>.
    </td>
    <td>Plug-and-play if the search integration is implemented. Requires implementation otherwise.</td>
  </tr>
  <tr>
    <td>Marketing & Analytics</td>
    <td>
      Marketing & Analytics integrations are provided as VTEX IO apps. Marketing integrations allow stores to connect with marketing platforms and attract customers. Analytics integrations collect and process customer session data. Check out the available apps for <a href="https://apps.vtex.com/all-apps#marketing">Marketing and affiliate programs</a> and <a href="https://apps.vtex.com/all-apps#review">Reviews, ratings, and Analytics</a> on the App Store.<br><br>
      If the integration is not implemented, a <a href="https://developers.vtex.com/docs/guides/vtex-io-documentation-1-developnativeintegrationswithpixelapps">Pixel app</a> can be developed. This type of app runs scripts on all pages of a store website and natively integrates the store with a third-party solution, such as sales tracking, user support, and marketing services.
    </td>
    <td>Plug-and-play if the marketing/analytics app is implemented. Requires implementation otherwise.</td>
  </tr>
  <tr>
    <td>Payments</td>
    <td>
      Payment integrations allow payment providers to operate at VTEX stores. If the payment provider is integrated, the merchant must have a contract with the provider and configure the payment options through the VTEX Admin. See the details in the <b>Payments</b> section of our <a href="https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/3MYcZaojb5HSUg6ufm6GxQ#payments">VTEX modules overview</a>. Find the providers supported by VTEX in the <a href="https://help.vtex.com/en/tutorial/list-of-payment-providers-by-country--2im3BEGXxSAcRuxEaIHPvp">List of Payment Providers by Country</a>.<br><br>
      If a payment provider is not integrated, the payment company or an <a href="https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4yPqZQyj0t675QpcG7H6yl#implementation-partners">implementation partner</a> can develop an integration, also called a <a href="https://help.vtex.com/en/tutorial/what-is-the-connector">connector</a>, following our <a href="https://help.vtex.com/en/tutorial/payment-provider-protocol--RdsT2spdq80MMwwOeEq0m">Payment Provider Protocol</a>. The connector implementation must have the endpoints described in the <a href="https://developers.vtex.com/docs/api-reference/payment-provider-protocol">Payment Provider Protocol API</a> and will be called by the VTEX’s Payment Gateway. The protocol is flexible enough to support the implementation of various payment <a href="https://developers.vtex.com/docs/guides/payments-integration-payment-methods">methods</a>, <a href="https://help.vtex.com/en/tutorial/how-to-configure-payment-conditions--tutorials_455">conditions</a>, and <a href="https://developers.vtex.com/docs/guides/payments-integration-purchase-flows">purchase flows</a>. For more details, see <a href="https://developers.vtex.com/docs/guides/integrating-a-new-payment-provider-on-vtex">Integrating a new payment provider</a>.
    </td>
    <td>Plug-and-play if the payment provider is implemented. Requires implementation otherwise.</td>
  </tr>
  <tr>
    <td>Carriers</td>
    <td>
      <a href="https://help.vtex.com/en/tutorial/transportadoras-na-vtex--7u9duMD5UQa2QQwukAWMcE">Carriers</a> are companies that deliver orders to customers. The standard way to add carriers to VTEX is by <a href="https://help.vtex.com/en/tutorial/creating-a-shipping-policy--66rJO4LKBdyMJOH6Z3dsaT">creating shipping policies</a> in the Logistics module. Another option is to use the <a href="https://help.vtex.com/en/tutorial/vtex-shipping-network-dashboard--51e8tx1IehiN4ZtURRWU92">VTEX Shipping Network</a> add-on, which supports over 20 carrier partners. Also, there are dedicated carrier apps in the <a href="https://apps.vtex.com/all-apps#omnichannel">App Store</a>.<br><br>
      ⚠️ <i>VTEX Shipping Network is only available in Brazil.</i>
    </td>
    <td> Plug-and-play</td>
  </tr>
  <tr>
    <td>Third-party Sellers</td>
    <td>For <a href="https://help.vtex.com/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w">sellers</a> not integrated with VTEX but want to sell their products on a VTEX marketplace, a custom connector can be developed for this integration. VTEX provides a set of APIs and instructions to facilitate the process. For more information, see our <a href="https://developers.vtex.com/docs/guides/external-seller-integration-guide">External Seller</a> integration guide.</td>
    <td>Plug-and-play if the seller integration is implemented. Requires implementation otherwise.</td>
  </tr>
</table>

## Add-ons

Add-ons are additional solutions offered by VTEX to meet specific business needs. They can be purchased separately through a subscription agreement. You can find more details on [Add-on products](https://help.vtex.com/en/tracks/next-steps-after-the-go-live--3J7WFZyvTcoiwkcIVFVhIS/1t2QBZvrOBSLgvHaAV9fYm). Some add-ons available at VTEX are:

<table>
  <tr>
    <td><b>Component</b></td>
    <td><b>Description</b></td>
    <td><b>Type</b></td>
  </tr>
  <tr>
    <td>Sales App</td>
    <td><a href="https://help.vtex.com/en/tracks/instore-getting-started-and-setting-up--zav76TFEZlAjnyBVL5tRc/7fnnVlG3Kv1Tay9iagc5yf">VTEX Sales App</a> is our main solution for <a href="https://help.vtex.com/tracks/unified-commerce-strategies--3WGDRRhc3vf1MJb9zGncnv">Unified Commerce</a> operations. The solution includes a mobile app used by sales associates from physical stores. The app enables sales associates to serve customers and complete the entire sales process from helping to choose the right products to payment and delivery.</td>
    <td>Yes, upon subscription / additional costs</td>
  </tr>
  <tr>
    <td>Live Shopping</td>
    <td>The <a href="https://vtex.com/us-en/live-shopping">Live Shopping</a> app enables an interactive ecommerce experience that combines live streaming and online shopping. Its key features include real-time interaction, personalized content, and data analytics for performance tracking. Events with Live Shopping lead to increased engagement, add-to-cart ratio, and conversion rates.</td>
    <td>Yes, upon subscription / additional costs</td>
  </tr>
  <tr>
    <td>Personal Shopper</td>
    <td><a href="https://vtex.com/us-en/vtex-personal-shopper/">VTEX Personal Shopper</a> is an app used by sales associates that brings the physical store shopping experience to the digital environment. It offers one-to-one video chats with customers, enabling product demonstration, real-time answers to queries, and direct addition of products to the cart.</td>
    <td>Yes, upon subscription / additional costs</td>
  </tr>
  <tr>
    <td>Assisted Sales (SuiteShare)</td>
    <td><a href="https://help.vtex.com/pt/tracks/suiteshare--khP0p8mjIYRIpvM7Cb4Zr">Assisted Sales (SuiteShare)</a>, previously known as Conversational Commerce, is a marketing platform for WhatsApp, helping to attract more clients, capture customer data, and integrate with sales tools. The platform allows for organizing customer support, integrating with major CRMs, and measuring results. The solution is based on the official WhatsApp API.</td>
    <td>Yes, upon subscription / additional costs</td>
  </tr>
  <tr>
    <td>Pick and Pack</td>
    <td>
      <a href="https://help.vtex.com/en/tutorial/vtex-pick-and-pack--1OOops3WrUyz7e0bnhkfXU">VTEX Pick and Pack</a> is a solution that helps merchants manage the order fulfillment process, including picking, packing, and delivery, from physical stores and warehouses to customers' addresses or pickup points. It provides real-time tracking, route optimization, and data analytics to improve efficiency and performance. The solution consists of:
      <ul>
        <li>Fulfillment: Admin app for store operators to manage orders in the store or warehouse.</li>
      </ul>
      <ul>
        <li>Last Mile: Admin app for store operators to instruct drivers on the delivery, and access proof of collecting and delivering.</li>
      </ul>
      <ul>
        <li>Mobile Applications: Applications for mobile devices used by pickers and drivers in the fulfillment.</li>
      </ul>
    </td>
    <td>Yes, upon subscription / additional costs</td>
  </tr>
  <tr>
    <td>VTEX Shield</td>
    <td><a href="https://help.vtex.com/en/tutorial/vtex-shield--2CVk6H9eY2CBtHjtDI7BFh">VTEX Shield</a> offers additional, customizable protection layers for stores prioritizing platform resilience and the security standards guaranteed by VTEX's existing security certifications and practices.</td>
    <td>Yes, upon subscription / additional costs</td>
  </tr>
  <tr>
    <td>Ad Network</td>
    <td><a href="https://help.vtex.com/en/tutorial/vtex-ad-network-beta--2cgqXcBuJmXN2livQvClur">VTEX Ad Network</a> connects VTEX stores with brands interested in advertising their products. This connection allows advertisers and merchants to boost their business.</td>
    <td>Yes, upon subscription / additional costs</td>
  </tr>
</table>
