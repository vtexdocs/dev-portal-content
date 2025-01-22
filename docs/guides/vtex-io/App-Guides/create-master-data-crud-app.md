---
title: "Creating a Master Data v2 CRUD app"
excerpt: "Learn how to create a Master Data v2 CRUD apps in VTEX IO."
slug: "create-master-data-crud-app"
hidden: false
createdAt: "2022-10-13T18:45:34.059Z"
updatedAt: "2022-10-17T13:53:29.359Z"
---

This guide will teach you how to build a Master Data v2 CRUD (Create, Read, Update, Delete) application within VTEX IO using the `masterdata` builder. [Master Data](https://help.vtex.com/tutorial/master-data--4otjBnR27u4WUIciQsmkAw) is a native key-document database that allows you to efficiently store, search, expand, and personalize your data. While it is possible to integrate Master Data into any VTEX IO app by connecting to the [Master Data API](https://developers.vtex.com/docs/api-reference/master-data-api-v2#overview), this is not the most efficient approach.

To streamline your development experience, we recommend leveraging the `masterdata` [builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-builders) to create apps with [Master Data v2](https://help.vtex.com/tutorial/master-data--4otjBnR27u4WUIciQsmkAw) features, including data creation, editing, and deletion.

> If you prefer to use Master Data v1, check [Creating a VTEX IO service to interact with Master Data v1](https://developers.vtex.com/docs/guides/interacting-with-master-data-v1-through-vtex-io-services).

## Before you begin

Before diving into coding your app, it's essential to grasp some fundamental concepts:

- Master Data
  - [Basic components](https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw#basic-components).
  - [Infrastructure](https://developers.vtex.com/docs/guides/master-data-infrastructure).
  - [Working with JSON Schemas in Master Data v2](https://developers.vtex.com/docs/guides/working-with-json-schemas-in-master-data-v2).
  - [Schema lifecycle](https://developers.vtex.com/docs/guides/master-data-schema-lifecycle).
- VTEX IO service development
  - [Developing services on VTEX IO](https://learn.vtex.com/docs/course-service-course-lang-en).

## Instructions

To create a [Master Data](https://help.vtex.com/tutorial/master-data--4otjBnR27u4WUIciQsmkAw) app, follow these steps:

### Step 1 - Defining the data structure

Before diving into coding, take time to plan your data structure. Since you will be setting up a VTEX IO service app with a focus on [Master Data](https://help.vtex.com/tutorial/master-data--4otjBnR27u4WUIciQsmkAw)'s basic elements, ensure you have well-defined data entities and written schemas prepared for each entity your app will interact with.

For each [data entity](https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw#data-entities) that your app will interact with, plan and prepare its corresponding [JSON schema](https://developers.vtex.com/docs/guides/working-with-json-schemas-in-master-data-v2). See an example below:

<details>
<summary>Schema example</summary>

```json
{
  "$schema": "http://json-schema.org/schema#",
  "title": "my_schema",
  "type": "object",
  "properties": {
    "string_field_example": {
      "type": "string"
    },
    "number_field_example": {
      "type": "number"
    },
    "boolean_field_example": {
      "type": "boolean"
    }
  },
  "required": [
    "number_field_example",
    "string_field_example"
  ],
  "v-default-fields": [
    "number_field_example",
    "string_field_example"
  ]
}
```

</details>

### Step 2 - Editing the `manifest.json` file

1. Use the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference) and run `vtex init` to copy the [service-example](https://github.com/vtex-apps/service-example) boilerplate files to your computer.
2. Add the `masterdata` builder to your [manifest file](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest).

```diff
 "builders": {
     ...
+    "masterdata": "1.x",
 }
```

3. Add the following [policies](https://developers.vtex.com/docs/guides/vtex-io-documentation-policies) to your app’s `manifest.json` file:

```json
[{
    "name": "outbound-access",
    "attrs": {
        "host": "api.vtex.com",
        "path": "/api/*"
     }
},
{
    "name": "ADMIN_DS"
 }]
```

### Step 3 - Using the `masterdata` builder

1. Create a folder named `masterdata` at the root of your app. This will be your Master Data configuration folder.
2. For each data entity your app interacts with, create a dedicated folder inside the `masterdata` directory.
3. Within each data entity folder, create a file named `schema.json`. The folder structure should resemble the following:

  ```
  masterdata
   | --myEntity
         | --schema.json
  ```

4. Populate the `schema.json` file with the [JSON schema](https://developers.vtex.com/docs/guides/working-with-json-schemas-in-master-data-v2) corresponding to the respective and save your changes. Notice that each data entity must have its own `schema.json` with a valid JSON schema.
5. In the terminal, run `vtex link` to test your code.

Note that your app creates regular Master Data entities accessible via the [Master Data v2 endpoints](https://developers.vtex.com/docs/api-reference/master-data-api-v2#overview). The naming convention for the entities follows this pattern: `{vendor}_{appName}_{entityName}`.

> ⚠️ Note that each time you install or link a different version of your app, the `masterdata` builder creates a new schema with the app’s name and version. Hence, since Master Data v2 data entities have a limit of 60 schemas per entity, ensure to [delete unused schemas](https://developers.vtex.com/docs/api-reference/master-data-api-v2#delete-/api/dataentities/-dataEntityName-/schemas/-schemaName-) to prevent from running into issues.

### Step - 4 - Generating TypeScript typings

Run `vtex setup -i` at the root of your project. This command will generate all TypeScript typings for your data entity, making them available for import in your app. You can find them in your `node/node_modules` folder.

> ⚠️ Whenever you change a data entity schema, you must regenerate the TypeScript typings. Hence, if you run into issues related to the data entity typings, try regenerating the typings. Also, ensure to run `vtex setup -i` before releasing your app so that the typings will not be tied to your development workspace.

### Step 5 - Using the `node` builder

1. In the terminal, change to the `node` folder of your app.
2. Run `yarn add @vtex/clients` to install the `clients` package.
3. Open the file `node/clients/index.ts` and import the following modules:
  
  ```ts
  import { masterDataFor } from '@vtex/clients'
  import { myEntity } from 'vendor.appName' // Replace with the names of your data entity, store, and app.
  ```
  
  >⚠️ When importing your data entity typings from the app, follow the format `{vendor}.{appName}`, as specified in your `manifest.json`. If the app does not recognize the generated typings import, try deleting the `node/node_modules` folder. Then run `yarn` to reinstall dependencies and `vtex setup` to regenerate the typings. Finally, run `vtex link` to check if everything is functioning correctly.

4. In the same `node/clients/index.ts` file, create a new property for the `Clients` class to create a client for your data entity. This represents the data entity you are working with. See this code example:

```ts
public get entity() {
  return this.getOrSet('entity', masterDataFor<myEntity>('entity'))
}
```

### Step 6 - Configuring Master Data triggers

To configure [Master Data triggers](https://developers.vtex.com/docs/guides/setting-up-triggers-on-master-data-v2) in your app, follow these steps:

1. Create a folder named `triggers` inside your `masterdata/{dataEntity}` folder.
2. Create a JSON file inside the `triggers` folder.
3. Declare your triggers in the JSON file, following the same format described for the `v-triggers` field when [setting up Master Data v2 triggers](https://developers.vtex.com/docs/guides/setting-up-triggers-on-master-data-v2).
   
### Step 7 - Creating Master Data functions

Now that your app is set up, you can begin coding Master Data functions, such as saving, editing, retrieving, or deleting data. You can then use these functions in your app’s  `resolvers` and `middlewares`.

Master Data functions are available via global context through `ctx.clients.{entityName}.{function}()`. Below, you can see more details on each function. These functions are equivalent to those performed by [Master Data v2 endpoints](https://developers.vtex.com/docs/api-reference/master-data-api-v2#overview).

#### Get

The `get()` function returns a document by its ID. You may specify what fields you want to be returned. If you do not, all fields in the document will be returned.

| **Argument** | **Required** | **Type** | **Description**                                                                                |
|--------------|--------------|----------|------------------------------------------------------------------------------------------------|
| `id`           | Yes          | String   | ID of the document you wish to retrieve.                                                       |
| `fields`       | No           | Array of strings    | List of the names of the fields you wish to be returned. If not sent, all fields are returned. |

<details>
<summary>Example: Getting a complete document of the `Book` entity.</summary>

```ts
ctx.client.Book.get(id: 'sdfg3543df5g4h3d5fh47d')
```

</details>

<details>
<summary>Example: Getting the name and release date of a given book from the `Book` entity.</summary>

```ts
ctx.client.Book.get(id: 'sdfg3543df5g4h3d5fh47d’, fields:['name', 'releaseDate'])
```

</details>

#### Save

The `save()` function saves a new document to your data entity and returns the generated ID for that new document.

This function’s arguments follow the format you described when setting up JSON schemas in your [data structure](#data-structure).

<details>
<summary>Example: Saving a new document to the `Book` data entity.</summary>

```ts
ctx.client.Book.save({
  name: 'Dom Quixote',
  releaseDate: 1605,
  author: 'Miguel de Cervantes'
})
```

</details>

#### Update

The `update()` function an existing document by ID.

| **Argument** | **Required** | **Type** | **Description**                                                                                |
|--------------|--------------|----------|------------------------------------------------------------------------------------------------|
| `id`           | Yes          | String   | ID of the document you wish to update.                                                       |
| `{document-data}`      | Yes           | Corresponding to the types declared in the schema    | This function’s arguments follow the format you described when setting up JSON schemas in your [data structure](#data-structure). Required fields apply even for partial updates. |

<details>
<summary>Example: Updating a document’s `rating` field in the `Book` entity.</summary>

```ts
ctx.client.Book.udpate(
  id: 'sdfg3543df5g4h3d5fh47d',
  {
    name 'Dom Quixote',
    rating: 4,5
  }
)
```

</details>

#### Save or update

The `saveOrUpdate()` function updates an existing document by ID or creates a new document if you do not send an ID.

| **Argument** | **Required** | **Type** | **Description**                                                                                |
|--------------|--------------|----------|------------------------------------------------------------------------------------------------|
| `id`           | No         | String   | ID of the document you wish to update. If you send an ID, the document is updated. Otherwise, a new document is created.                                                       |
| `{document-data}`      | Yes           | Corresponding to the types declared in the schema    | This function’s arguments follow the format you described when setting up JSON schemas in your [data structure](#data-structure). Required fields apply even for partial updates. |

<details>
<summary>Example: Updating a document’s `rating` field in the `Book` entity.</summary>

```ts
ctx.client.Book.saveOrUpdate(
  id: ‘sdfg3543df5g4h3d5fh47d’,
  {
    name ‘Dom Quixote’,
    rating: 4,5
  }
)
```
</details>

<details>
<summary>Example: Saving a new document to the `Book` data entity.</summary>


```ts
ctx.client.Book.saveOrUpdate({
  name: 'Dom Quixote',
  releaseDate: 1605,
  author: 'Miguel de Cervantes'
})
```

</details>

#### Delete

The `delete()` function deletes a document by ID.

| **Argument** | **Required** | **Type** | **Description**                                                                                |
|--------------|--------------|----------|------------------------------------------------------------------------------------------------|
| `id`           | Yes          | String   | ID of the document you wish to delete.                                                       |


<details>
<summary>Example: Deleting a document of the `Book` entity.</summary>

```ts
ctx.client.Book.delete(id: 'sdfg3543df5g4h3d5fh47d')
```

</details>

#### Search

The `search()` function returns an array of documents that satisfy the criteria described in the arguments.

| **Argument** | **Required** | **Type**         | **Description**                                                                                |
|--------------|--------------|------------------|------------------------------------------------------------------------------------------------|
| `page`         | Yes          | Integer          | Number of the page you wish to retrieve.                                                       |
| `pageSize`     | Yes          | Integer          | Number of documents that should be returned in each page.                                                |
| `fields`       | No           | Array of strings | Names of the fields you wish to be returned. If not sent, all fields are returned. |
| `where`        | No           | String           | Filtering condition.                                                                           |

<details>
<summary>Example: Searching names and release dates of all books by the author Miguel de Cervantes.</summary>

```ts
ctx.client.Book.search(
  pagination: {
    page: 1,
    pageSize: 10
  },
  fields: ['name', 'releaseDate'],
  where: 'name=Miguel de Cervantes'
)
```

</details>
