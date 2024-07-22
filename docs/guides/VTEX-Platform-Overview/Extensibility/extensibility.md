---
title: "Extensibility"
slug: "extensibility"
hidden: false
createdAt: "2024-07-22T10:00:00.000Z"
updatedAt: ""
excerpt: "Understand how to extend VTEX capabilities beyond what comes out-of-the-box"
---

VTEX is a [complete platform](https://developers.vtex.com/docs/guides/composability#vtex-composable-and-complete), in the sense that it offers all the features out-of-the-box needed to run an ecommerce operation. The VTEX platform is also extensible, providing multiple ways to extend its basic functionality, including integrating third-party solutions and developing custom applications.

In this guide, we demonstrate VTEX’s extensibility in four types explained in the sections below:

- Data Services
- Commerce APIs
- Development Platform
- Composable SaaS (Software as a Service)

![Extensibility overview](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Verview/Extensibility/extensibility-overview.png)

## Data Services

[Master Data](https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw) is a key-document database solution that enables merchants to store, search, expand, and customize data. The solution allows custom behaviors with data and the creation of custom applications using its API endpoints and [VTEX IO client](https://developers.vtex.com/docs/guides/vtex-io-documentation-clients).

Master Data has the following advantages:

- **Native VTEX solution**: Start working with Master Data out-of-the-box, with no need to integrate an external database solution.
- **Scalable**: Store data as needed without worrying about usage limits.
- **No additional costs**: VTEX does not charge extra no matter how much you use Master Data resources.

There are two Master Data versions available (v1 and v2). Learn more about each of their features in the [Master Data](https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw#versions-available) guide. By default, Master Data v1 is responsible for storing customer data from the stores.

In Master Data, we have three main concepts about the data structure:

- [**Data entities**](https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw#data-entities): The definition of the data structures in table format. Each data entity has a name and is responsible for storing a data type. For instance, in Master Data v1, the CL data entity stores data from store customers.
- [**Documents**](https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw#documents): The rows of the tables, which are records of the data entity. In Master Data v1, each document represents one store customer in the CL data entity.
- [**Fields**](https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw#fields): The columns of the tables, which are the properties of the data entity. In Master Data v1, the CL data entity has the fields name, ID number, email, and phone number.

The following sections show how Master Data extends the basic functionality of a VTEX store.

### New entities and data schemas

Master Data comes with a default set of data entities necessary for basic ecommerce operations. Additionally, it allows customization and extension of the data models. This can be done in two ways depending on the Master Data version.

In Master Data v1, you can create and edit data entities [using its UI](https://help.vtex.com/en/tutorial/data-entity--tutorials_1265#creating-data-entities). In Master Data v2, you can create and edit [data schemas](https://developers.vtex.com/docs/guides/starting-to-work-on-master-data-with-json-schema) through the [API](https://developers.vtex.com/docs/api-reference/master-data-api-v2). The table below shows a summary of the data entity capabilities.

<details>
  <summary><b>Click here to view the capabilities table</b></summary>
  <table>
    <tr>
      <td><b>Capability</b></td>
      <td><b>Description</b></td>
      <td><b>Availability</b></td>
    </tr>
    <tr>
      <td>Define data entity name</td>
      <td>Define the name of the data entity when it is created. In Master Data v1, you must also choose its acronym, composed of two capital letters. For instance, the Address data entity has the acronym <code>AD</code>.</td>
      <td>
        <ul>
          <li>Master Data v1</li>
          <li>Master Data v2</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Define the fields and their properties</td>
      <td>In Master Data v1, you can use the UI to define the data entity fields and their properties. Some of the properties include the field type, and if the field is nullable, searchable, or filterable.<br><br>In Master Data v2, with JSON schema validation, requests that use properties different from what is defined in the selected schema are invalidated. For instance, you will get an error if you try to modify a field with string type to the value 2.</td>
      <td>
        <ul>
          <li>Master Data v1</li>
          <li>Master Data v2</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><code>id</code> field generation</td>
      <td>This determines how Master Data v1 generates the <code>id</code> field, which is used to identify documents in the data entities. It can be generated automatically using the <b>GUID</b> (Globally Unique Identifier) and <b>sequential numeric</b> options, or inserted manually when creating new documents.</td>
      <td>
        <ul>
          <li>Master Data v1</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Index or alternate keys</td>
      <td>Set up additional fields that work an <a href="https://developers.vtex.com/docs/guides/master-data-components#index">index</a>. This allows to retrieve documents without using the <code>id</code>.</td>
      <td>
        <ul>
          <li>Master Data v1</li>
          <li>Master Data v2</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Default fields</td>
      <td>Set the default fields. These are the fields shown when reading a document or making a search, and the <code>_fields</code> query parameter is not declared in the request.</td>
      <td>
        <ul>
          <li>Master Data v2</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Public fields</td>
      <td>Choose the fields that can be accessed without authentication. For instance, this can be useful for showing data publicly on the storefront.</td>
      <td>
        <ul>
          <li>Master Data v1</li>
          <li>Master Data v2</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Inherit schema</td>
      <td>The data entity inherits the declared schemas from other data entities.</td>
      <td>
        <ul>
          <li>Master Data v2</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Triggers</td>
      <td>Define automatic custom actions triggered by specific events with the data. For more details, see the <a href="#triggers">Triggers section</a>.</td>
      <td>
        <ul>
          <li>Master Data v1</li>
          <li>Master Data v2</li>
        </ul>
      </td>
    </tr>
  </table>
</details>

### Endpoints to read and write data

After defining the desired structure of the data in the data entities, you can start working with the data. Master Data has a complete CRUD (create, read, update, and delete) functionality. It allows storage, retrieval, edition, custom searches, and deletion of documents. You can make these operations through the UI in Master Data v1, or using the [API](https://developers.vtex.com/docs/guides/master-data-api) endpoints in both versions.

With the endpoints, it is possible to extend the store functionality with services using the Master Data API. For instance, it is possible to create an application for product reviews and ratings, where the reviews are stored in a reviews data entity.

The table below shows the Master Data endpoints to interact with documents:

<details>
  <summary><b>Click here to view the Master Data document endpoints table</b></summary>
  <table>
    <tr>
      <td><b>Endpoint name</b></td>
      <td><b>Method</b></td>
      <td><b>Description</b></td>
      <td><b>Reference</b></td>
    </tr>
    <tr>
      <td>Create new document</td>
      <td><code>POST</code></td>
      <td>Create a new document in the chosen data entity.</td>
      <td>
        <ul>
          <li><a href="https://developers.vtex.com/docs/api-reference/masterdata-api/#post-/api/dataentities/-acronym-/documents">Master Data v1</a></li>
          <li><a href="https://developers.vtex.com/docs/api-reference/master-data-api-v2/#post-/api/dataentities/-dataEntityName-/documents">Master Data v2</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Create partial document</td>
      <td><code>PATCH</code></td>
      <td>Create a new document in the chosen data entity.</td>
      <td>
        <ul>
          <li><a href="https://developers.vtex.com/docs/api-reference/masterdata-api/#patch-/api/dataentities/-acronym-/documents">Master Data v1</a></li>
          <li><a href="https://developers.vtex.com/docs/api-reference/master-data-api-v2/#patch-/api/dataentities/-dataEntityName-/documents">Master Data v2</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Get document</td>
      <td><code>GET</code></td>
      <td>Retrieve a document with the given <code>id</code>.</td>
      <td>
        <ul>
          <li><a href="https://developers.vtex.com/docs/api-reference/masterdata-api/#get-/api/dataentities/-acronym-/documents/-id-">Master Data v1</a></li>
          <li><a href="https://developers.vtex.com/docs/api-reference/master-data-api-v2/#get-/api/dataentities/-dataEntityName-/documents/-id-">Master Data v2</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Create document with custom ID or Update entire document</td>
      <td><code>PUT</code></td>
      <td>Create a new document in the chosen data entity with a specific <code>id</code>. If there is a document with this <code>id</code>, update the document instead, replacing the whole document with the request body.</td>
      <td>
        <ul>
          <li><a href="https://developers.vtex.com/docs/api-reference/masterdata-api/#put-/api/dataentities/-acronym-/documents/-id-">Master Data v1</a></li>
          <li><a href="https://developers.vtex.com/docs/api-reference/master-data-api-v2/#put-/api/dataentities/-dataEntityName-/documents/-id-">Master Data v2</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Update partial document</td>
      <td><code>PATCH</code></td>
      <td>Update the document with the given <code>id</code>. Change only the fields declared in the request body, while the other fields of the document keep the same values.</td>
      <td>
        <ul>
          <li><a href="https://developers.vtex.com/docs/api-reference/masterdata-api/#patch-/api/dataentities/-acronym-/documents/-id-">Master Data v1</a></li>
          <li><a href="https://developers.vtex.com/docs/api-reference/master-data-api-v2/#patch-/api/dataentities/-dataEntityName-/documents/-id-">Master Data v2</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Delete document</td>
      <td><code>DELETE</code></td>
      <td>Delete the document with the given <code>id</code>.</td>
      <td>
        <ul>
          <li><a href="https://developers.vtex.com/docs/api-reference/masterdata-api/#delete-/api/dataentities/-acronym-/documents/-id-">Master Data v1</a></li>
          <li><a href="https://developers.vtex.com/docs/api-reference/master-data-api-v2/#delete-/api/dataentities/-dataEntityName-/documents/-id-">Master Data v2</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Search documents</td>
      <td><code>GET</code></td>
      <td>Retrieve a list of documents from the given data entity. Use parameters to filter the results, including schemas and indexed fields.</td>
      <td>
        <ul>
          <li><a href="https://developers.vtex.com/docs/api-reference/masterdata-api/#get-/api/dataentities/-acronym-/search">Master Data v1</a></li>
          <li><a href="https://developers.vtex.com/docs/api-reference/master-data-api-v2/#get-/api/dataentities/-dataEntityName-/search">Master Data v2</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Scroll documents</td>
      <td><code>GET</code></td>
      <td>Retrieve a large amount of documents.  Use parameters to filter the results, including schemas and indexed fields.</td>
      <td>
        <ul>
          <li><a href="https://developers.vtex.com/docs/api-reference/masterdata-api/#get-/api/dataentities/-acronym-/scroll">Master Data v1</a></li>
          <li><a href="https://developers.vtex.com/docs/api-reference/master-data-api-v2/#get-/api/dataentities/-dataEntityName-/scroll">Master Data v2</a></li>
        </ul>
      </td>
    </tr>
  </table>
</details>

### Triggers

A [Master Data Trigger](https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw#triggers) is a mechanism that performs an action after creating or updating a document if the conditions set in the configuration are met. The possible actions with triggers are:

- Send an HTTP request.
- Send an email.
- Save a document in another data entity.

This functionality of acting from specific events in the data enables the creation of automated custom behaviors with the data. For example, you can configure a trigger to send an email to the customer when there is a new document in the CL data entity, that is the moment when the account is created. There are two possible ways to work with triggers depending on the Master Data version.

In Master Data v1, you configure triggers from the UI. For more details, see [How to create a trigger in Master Data v1](https://help.vtex.com/en/tutorial/creating-trigger-in-master-data--tutorials_1270).

In Master Data v2, you configure triggers in the v-triggers field in a JSON Schema of the data entity. This field is an array of objects, where each object represents a trigger. For more details, see [Setting up triggers in Master Data v2](https://developers.vtex.com/docs/guides/setting-up-triggers-in-master-data-v2).

### Custom Master Data apps with VTEX IO

Besides providing APIs to integrate with custom solutions, VTEX also has its development platform, [VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io). By developing an [IO app](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-a-vtex-app), it is possible to create a solution that uses Master Data API through [clients](https://developers.vtex.com/docs/guides/vtex-io-documentation-clients). Find more details about development with VTEX IO in the [Development Platform section](#development-platform).

By developing a Master Data app using VTEX IO, you can have the development environment, the code, and access to Master Data all inside VTEX. The process is different for each Master Data version, but the summary is cloning a boilerplate, defining the [policies](https://developers.vtex.com/docs/guides/vtex-io-documentation-policies), adding the [client](https://developers.vtex.com/docs/guides/vtex-io-documentation-clients), and creating the middleware functions. For more details, see the guides [Interacting with Master Data v1 through VTEX IO services](https://developers.vtex.com/docs/guides/interacting-with-master-data-v1-through-vtex-io-services), and [Create a Master Data CRUD app](https://developers.vtex.com/docs/guides/create-master-data-crud-app) for Master Data v2.

## Commerce APIs

VTEX is an API-first ecommerce platform, with all our core commerce services accessible through 750+ API endpoints. These endpoints provide many extensibility options, be it with third-party integrations or the development of custom solutions with VTEX IO.

You can find information about VTEX endpoints in our [API reference](https://developers.vtex.com/docs/api-reference) and our [List of REST APIs](https://developers.vtex.com/docs/guides/getting-started-list-of-rest-apis). For details about implementation with our APIs, see the sections for each service in our [API guides](https://developers.vtex.com/docs/guides).

We divide our endpoints into three categories depending on the operations performed.

### Endpoints to read and write data

Most endpoints go into this category since they are the access points to read and write data. They do more than manage data, such as in a database, by enabling all sorts of commerce functionalities in a store. For example, there are endpoints to create product categories, read order details, update a shipping policy, delete a SKU price, and more.

These endpoints are commonly used in back-office integrations. In this case, merchants use back-office software such as an ERP (Enterprise Resource Planning) or a PIM (Product Information Manager) to manage the commerce operations, and they integrate with VTEX. The endpoints are used to import data to VTEX, or access and control the data at VTEX through the back-office software interface. For more details, see our [backend integrations overview](https://help.vtex.com/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/7euXDZR5CCnVFSrXyczIhu) and [back-office integration guide](https://developers.vtex.com/docs/guides/erp-integration-guide).

### Hooks and Feeds for orders

Hooks and Feeds are specific integrations that allow communication through events. Hooks allow for calling an action right after an event occurs. Feeds are lists of events, where the receiver processes the events at its own pace.

At VTEX, Hooks and Feeds integrate back-office software, such as ERP, and VTEX OMS (Order Management System). Hooks and Feeds endpoints are part of the [Orders API](https://developers.vtex.com/docs/api-reference/orders-api). They are responsible for delivering order updates for specific statuses and enabling [order processing by the back-office software](https://developers.vtex.com/docs/guides/erp-integration-set-up-order-processing). Order processing operations include canceling, changing items, and issuing invoices.

[Feed v3](https://developers.vtex.com/docs/guides/orders-feed) is a list of events with order updates. For this type of integration, VTEX provides [endpoints](https://developers.vtex.com/docs/api-reference/orders-api#feed-v3) that allow the back-office software to query the items on the list, process the orders, and then remove the items from the list.

[Hook](https://developers.vtex.com/docs/guides/orders-feed#hook) is a channel for automatically receiving notifications about order updates. For this type of integration, the back-office software provides an [endpoint](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/orders/hook/config) for VTEX to send notifications regarding order updates. After receiving a notification, the back-office software may proceed to process the order.

For more details, see **Middleware configuration** and **Order integration** in our [Backend integrations overview](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/7euXDZR5CCnVFSrXyczIhu), and the [Set up order integration](https://developers.vtex.com/docs/guides/erp-integration-set-up-order-integration) guide.

### Extension points to change data flow

Extension points extend VTEX functionality by enabling access to external sources. This is done in two ways: hubs and protocols.

#### Hubs

Hubs are central access points for multiple providers, allowing one to select a service provider. Sometimes, VTEX can be one of the provider options, along with other external providers. At VTEX, we have the [Gift Card Hub](https://developers.vtex.com/docs/api-reference/giftcard-hub-api), which allows interaction with VTEX’s Gift Card and external Gift Card providers. The Gift Card options are available at Checkout.

#### Protocols

Protocols are rules defined by VTEX that allow external providers to implement their solutions, so they are available at VTEX. The rules are composed of endpoints that follow a specific structure (path, parameters, request body, response body) and are implemented by the providers. Once the implementation is done, VTEX calls the endpoints to access the provider’s solution.

For instance, in a payment integration using the Payment Provider Protocol, the [VTEX Payment Gateway](https://help.vtex.com/en/tutorial/what-is-a-payment-gateway--2KH9Wdi7F6swOU4amECSOk) calls the endpoints requesting the payment provider to perform the operations defined by the protocol. Possible payment operations are authorization, settlement, cancellation, and refund.

The available protocols at VTEX are:

- [Payment Provider Protocol](https://developers.vtex.com/docs/guides/integrating-a-new-payment-provider-on-vtex)
- [Antifraud Provider Protocol](https://developers.vtex.com/docs/guides/how-the-integration-protocol-between-vtex-and-antifraud-companies-works)
- [Gift Card Provider Protocol](https://developers.vtex.com/docs/api-reference/giftcard-provider-protocol)
- [Search Protocol](https://developers.vtex.com/docs/guides/external-search-provider-overview)
- [External Marketplace](https://developers.vtex.com/docs/guides/external-marketplace-integration-guide)
- [External Seller](https://developers.vtex.com/docs/guides/external-seller-integration-guide)
- [Tax Service](https://developers.vtex.com/docs/guides/tax-service-integration-guide)
- [Login integrations](https://developers.vtex.com/docs/guides/login-integration-guide)
- [Pick and Pack Last Mile Protocol](https://developers.vtex.com/docs/guides/vtex-pick-and-pack-carriers-integration-protocol)

## Development Platform

[VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io) is VTEX’s development platform for creating low-code custom solutions, both for the frontend and backend. The VTEX IO framework provides the tools to build and maintain [IO apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-a-vtex-app) by leveraging familiar technologies like [TypeScript](https://www.typescriptlang.org/), [React](https://react.dev/), [GraphQL](https://graphql.org/), [.NET](https://dotnet.microsoft.com/en-us/), and [Node.js](https://nodejs.org/en). VTEX IO allows the creation of storefront experiences, Admin panels, integration with VTEX and external services, and more.

The VTEX IO platform has a cloud-native infrastructure with automatic scaling. It means that developers can focus on the business solution without worrying about infrastructure concerns.

To learn more about the development details, see the [Developer experience](https://developers.vtex.com/docs/guides/developer-experience) guide.

### Frontend

Frontend solutions on VTEX IO are made for storefront and Admin.

- [Storefront apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-1-developing-storefront-apps-using-react-and-vtex-io) are made using the [Store Framework](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-store-framework). These apps can be a store theme, that determines the frontend structure of the store, or a collection of [frontend components](https://developers.vtex.com/docs/guides/store-components), that focus on specific parts of the shopping experience.
- [Admin apps](https://learn.vtex.com/docs/course-admin-lang-en) are apps that have at least one Admin panel. Store operators use these apps to configure and manage the shopping experience. Many useful components can be added to the panels including tables, dashboards, property fields in various formats (text, number, radio list, etc.), and more.

### Backend

Backend solutions on VTEX IO include services, access to APIs, and Pixel apps.

- [Services](https://developers.vtex.com/docs/guides/developing-services-on-vtex-io) are backend apps that run on Node or .NET. Services expose their functions by implementing REST or GraphQL APIs.
- IO apps use [Clients](https://developers.vtex.com/docs/guides/vtex-io-documentation-clients) to make API requests, both with REST and GraphQL. Clients enable access to VTEX commerce APIs, external endpoints, and other apps. Also, developers must declare the required [policies](https://developers.vtex.com/docs/guides/vtex-io-documentation-policies) to allow access to VTEX or external resources.
- [Pixel apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-1-developnativeintegrationswithpixelapps) are apps that run scripts on pages of a store website. They collect and analyze data for sales tracking, user support, and marketing services.

## Composable SaaS

VTEX is a composable platform for building commerce experiences by combining pre-built components, accelerating the implementation process. For more details about VTEX composable features, see our [Composability](https://developers.vtex.com/docs/guides/composability) guide. At VTEX, we offer two capabilities: VTEX IO apps and App Store apps.

### VTEX IO apps

[VTEX apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-a-vtex-app) are encolsed solutions made with VTEX IO that extends the functionalities of the VTEX platform. VTEX IO not only provides the tools for developers to develop apps, but also to publish and distribute these apps. After a developer publicly publishes an app, merchants can install the app in their stores at will. To [install VTEX IO apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app), use the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference).

There are multiple apps publicly availble that address all kinds of ecommerce scenarios, both from VTEX and third-party developers. Some solution examples that IO apps provide are frontend components, additional shopping exeriences, payment connectors, marketing and analytics tools, and many more. See the details about each app available at our [VTEX IO Apps section](https://developers.vtex.com/docs/vtex-io-apps).

>⚠️ We strongly recommend reading the app documentation before installation to avoid undesired behavior.

### App Store apps

Another way to use composition in a VTEX store is with Plug-and-Play apps from the [VTEX App Store](https://apps.vtex.com). Merchants can navigate the App Store and install apps with just a few steps, without code interaction.

There are more than 100 available apps developed by VTEX and third-party vendors, offering many commerce solutions. Some available functionalities are social marketing integrations, data collection and analytics, marketplace integrations, gift lists, and more. See more details in the [App Store](https://help.vtex.com/tracks/extensions-hub--AW7klkYMh557y5IUOgzco/2LDRvGujYsumxi7IlE7CEJ) article.
