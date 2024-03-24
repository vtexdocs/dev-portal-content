---
title: "GraphQL"
slug: "graphql-ide"
hidden: false
createdAt: "2021-03-25t17:12:53.428Z"
updatedAt: "2021-10-26t23:27:34.148Z"
seeAlso:
 - "/docs/guides/rewriter-graphql-api"
 - "/docs/guides/search-graphql"
---

VTEX IO APIs are built with [GraphQL](https://graphql.org/) — a query language and a server-side runtime for fulfilling those queries with existing data.

Instead of working with server-defined endpoints that return fixed data structures as in REST APIs, GraphQL allows developers to send queries containing the specific data that needs to be fetched over a single endpoint through a `POST` `HTTP` request.

That is how GraphQL provides solutions for some of the biggest challenges when designing APIs for modern applications.

Some of the advantages of working with GraphQL are:

- **Avoiding over and under-fetching:** GraphQL prevents transferring unnecessary data over the network and thus improves application efficiency by allowing developers to request the exact data they need.
- **Providing a better developer experience:** Since GraphQL APIs are self-describing, a change in the API is automatically reflected in its documentation. Besides, when performing a query, detailed information regarding the errors is immediately provided if the developer types something wrong or makes an invalid query. Also, if using an Integrated Development Environment (IDE), developers can take advantage of features such as autocomplete and syntax highlighting.
- **Facilitating continuous deployment:** GraphQL allows deprecating APIs on a field level. This way, GraphQL makes it possible to keep a single evolving version of an API. So, without the need for versioning, new features and capabilities can be added via new types and new fields without impacting the existing queries.

Thus, by adopting GraphQL, VTEX IO provides more flexibility and efficiency.

## GraphQL basics

Now that you know why VTEX IO uses GraphQL and its main advantages, let's explore some GraphQL basics.

The capabilities of a GraphQL API can be defined as:

- **Queries** for retrieving data.
- **Mutations** for writing, overwriting, or deleting data.
- **Subscriptions** for receiving real-time data when a specific event happens.

All these operation structures and the types they consume must be written in the GraphQL Schema Definition Language (SDL). This is what brings consistency between a query shape and the response shape.

Each field of a *schema* type is backed by a function called a *resolver*, which the GraphQL server developer provides.

Thus, whenever a GraphQL query is performed, the resolver functions related to the requested fields fetch data from the appropriate data source and populate the queried fields.

The GraphQL ecosystem is growing fast, and powerful tools, such as Graph*i*QL, maximize developer experience. In the following sections, you will learn how to install GraphQL IDE in your VTEX account and how to execute GraphQL queries and mutations with Graph*i*QL.

## Installing GraphQL IDE

1. Using your terminal and the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference), log in to your VTEX account.

2. Run `vtex use {workspaceName} --production` to use a production workspace or [create a production workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-production-workspace) from scratch.

> Remember to replace the values between curly brackets according to your scenario.

> If you just want to run tests, consider using a development workspace.

3. Install the GraphQL IDE app by running `vtex install vtex.admin-graphql-ide@3.x` in your terminal.

4. In your browser, go to `https://{workspace}--{account}.myvtex.com/admin`.

5. Under the **Store Settings > Storefront**, click **GraphQL IDE**.

![graphql-adminsidebarmenu](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/graphql-ide-0.png)

On the right side of your screen, you will now see a dropdown menu with the list of GraphQL APIs installed in the logged VTEX account.

6. Select the VTEX IO app you intend to send queries or mutations to.

Now, everything is set up, and you're ready to use Graph*i*QL.

> ℹ️ If you are not used to Graph*i*QL, check the following section to learn more.

## Using Graph*i*QL

[Graph*i*QL](https://github.com/graphql/graphiql) is an open-source tool for writing, validating, and testing GraphQL queries.

Graph*i*QL allows developers to validate GraphQL APIs by providing functionalities, such as:

- Autocomplete.
- Syntax highlighting.
- Real-time error reporting.
- Documentation explorer.

Now let's dive into the Graph*i*QL interface and features.

![graphiql](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/graphql-ide-1.png)

The Graph*i*QL interface is divided into three main parts: one for writing queries, another one for checking the results, and a third one named *Query Variables*, which is optional and hidden at the bottom of the screen.

The *Query Variables* section is recommended in cases when the same query will be reused many times with different arguments. In order to use dynamic values, you must place a dollar sign (`$`) before the variable name and then define the values for each field as JSON in the *Query Variables* section.

Another important section of Graph*i*QL is the *Documentation Explorer*, which can be found in the upper right-hand corner of the IDE. The *Documentation Explorer* allows developers to better understand a particular query, mutation, or type structure by providing a description and information about its schema.

> ℹ️ By being aware of types and query schemas, backend and frontend teams can work in parallel without friction.

Another feature of Graph*i*QL is keeping a log of all the queries and mutations that are run, which can be viewed through the *History* dashboard.

Also, when writing a query in Graph*i*QL, some useful shortcuts are:

- `Ctrl + Space` (or `Shift + Space`) to display the autocomplete popup.
- `Ctrl + Enter` to run the GraphQL query.
- `Shift-Ctrl-P` to fix the indentation.
