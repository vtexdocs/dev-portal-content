---
title: "Overview"
slug: "graphql-ide"
hidden: false
createdAt: "2021-03-25T17:12:53.428Z"
updatedAt: "2021-10-26T23:27:34.148Z"
---

# Introduction

VTEX IO APIs are built with [GraphQL](https://graphql.org/) - a query language and a server-side runtime for fulfilling those queries with existing data.

Instead of working with server-defined endpoints that return fixed data structures as in  REST APIs, GraphQL allows developers to send queries containing the specific data that needs to be fetched over a single endpoint through a `POST` `HTTP` request.

That's how GraphQL provides solutions for some of the biggest challenges when designing APIs for modern applications.

Some of the advantages of working with GraphQL are:

- **Avoiding over- and under- fetching:** GraphQL prevents transferring unnecessary data over the network, and thus improves application efficiency, by allowing developers to request the exact data they need.
- **Providing a better developer experience:** Since GraphQL APIs are self-describing, a change in the API is automatically reflected in its documentation. Besides, when performing a query, if the developer types something wrong or makes an invalid query, detailed information regarding the errors are immediately provided. Also, if using an Integrated Development Environment (IDE), developers can take advantage of features such as autocomplete and syntax highlighting.
- **Facilitating continuous deployment:** GraphQL allows deprecating APIs on a field level. This way, GraphQL makes it possible to keep a single evolving version of an API. So, without the need for versioning, new features and capabilities can be added via new types and new fields without impacting the existing queries.

This way, by adopting GraphQL, VTEX IO provides more flexibility and efficiency.

# GraphQL basics

Now that you know why VTEX IO uses GraphQL and its main advantages, let's explore some GraphQL basics.

The capabilities of a GraphQL API can be defined as:

- **Queries** for retrieving data.
- **Mutations** for writing, overwriting, or deleting data.
- **Subscriptions** for receiving real-time data when a specific event happens.

All these operation structures, and also the types they consume, must be written down in GraphQL Schema Definition Language (SDL). This is what brings consistency between a query shape and its response shape.

Each field of a *schema* type is backed by a function called a *resolver*, which is provided by the GraphQL server developer.

Thus, whenever a GraphQL query is performed, the resolver functions related to the demanded fields fetch data from the appropriate data source and populate the queried fields.

GraphQL ecosystem is growing fast and powerful tools, such as Graph*i*QL, maximizes developer experience. In the next sections, you'll learn how to install GraphQL IDE in your VTEX account, and how to execute GraphQL queries and mutations with Graph*i*QL.

# Installing GraphQL IDE

1. Using your terminal and the [VTEX IO CLI](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-installation-and-command-reference), log in to your VTEX account.

2. Run `vtex use {workspaceName} --production` to use a production workspace or [create a production workspace](https://vtex.io/docs/recipes/development/creating-a-production-workspace/) from scratch.

> Remember to replace the values between the curly brackets according to your scenario.

> If you just want to run tests, consider using a development workspace.

3. Install the GraphQL IDE app by running `vtex install vtex.admin-graphql-ide@3.x` in your terminal.

4. In your browser, access `https://{workspace}--{account}.myvtex.com/admin`.

5. Under the **Store Setup** section, click on **GraphQL IDE**.

![graphql-adminsidebarmenu](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/graphql-ide-0.png)

On the right side of your screen, you'll now see a dropdown menu, containing the list of GraphQL APIs that are installed in the logged VTEX account.

6. Select the VTEX IO app you intend to send queries or mutations.

Now, everything is set up and you're ready to use Graph*i*QL.

> ℹ️ If you're not used to Graph*i*QL, check the following section to learn more about it.

# Using Graph*i*QL

[Graph*i*QL](https://github.com/graphql/graphiql) is an open-source tool for writing, validating, and testing GraphQL queries.

Graph*i*QL allows developers to validate GraphQL APIs by providing functionalities, such as:

- Autocompleting.
- Syntax highlighting.
- Real-time error reporting.
- Documentation explorer.

Let's now dive into the Graph*i*QL interface and features.

![graphiql](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/graphql-ide-1.png)

Graph*i*QL interface is divided into three main parts: one for writing queries, another one for checking the results, and a third one named *Query Variables*, which is optional and hidden at the bottom of the screen.

The *Query Variables* section is recommended in cases when the same query will be reused many times with different arguments. To make possible the use of dynamic values, one must place a dollar sign (`$`) before the variable name and, then, define the values for each field as JSON in the *Query Variables* section.

Another important section of Graph*i*QL is the *Documentation Explorer*, which can be consulted in the upper right-hand corner of the IDE. The *Documentation Explorer* allows developers to better understand a particular query, mutation, or type structure by providing a description and information about its schema.

> ℹ️ By being aware of types and queries schemas, backend and frontend teams can work in parallel without any problems.

Another feature of Graph*i*QL is keeping a log of all the performed queries and mutations, which can be consulted in the *History* panel.

Also, when writing a query in Graph*i*QL, some useful shortcuts are:

- `Ctrl + Space` (or `Shift + Space`) to display the autocomplete popup.
- `Ctrl + Enter` to run the GraphQL query.
- `Shift-Ctrl-P` to fix the indentation.
