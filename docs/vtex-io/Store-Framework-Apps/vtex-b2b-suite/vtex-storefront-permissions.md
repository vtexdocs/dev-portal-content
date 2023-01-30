---
title: "Storefront Permissions"
slug: "vtex-storefront-permissions"
hidden: false
createdAt: "2021-07-20T17:06:30.143Z"
updatedAt: "2022-12-09T21:28:45.069Z"
---

> ℹ️ The **Storefront Permissions** app is part of VTEX’s [B2B Suite](https://developers.vtex.com/docs/guides/vtex-b2b-suite) solution, which is a collection of apps that allow stores to manage organizations, storefront roles and permissions, and checkout settings for B2B commerce relationships. We recommend that you use it alongside the other apps in this suite for all functionalities to work as expected.

When navigating a B2B store as a customer, it is common for a main user from an organization to have other people under their structure, each with their own information and access privileges.

Within an organization, each user can have different roles, such as a professional buyer that places orders with budget limits from a predefined cost center or  a manager in charge of reviewing and approving orders. These roles can be associated with multiple permissions, depending on the actions this user needs to perform.

The **Storefront Permissions** app stores a predefined set of roles and app permissions related to what B2B users can access and do in your storefront, making this information available for other integrated apps to check. This is useful for stores who want to set specific app permissions for users with different roles in an organization.


## Available storefront roles

In the following table, you can see the available storefront roles, their key used for identification in the app’s code, and their description.

| **Role** | **Key** | **Description** |
|---|---|---|
| Store Admin | `store-admin` | Store administrator, that is, a user who has access to the VTEX Admin. |
| Sales Admin | `sales-admin` | Sales administrator user who can manage all sales users. |
| Sales Manager | `sales-manager` | Sales manager user who can manage sales users in the same organization, as well as assist or impersonate buyers during navigation or purchase. |
| Sales Representative | `sales-representative` | Sales representative user who can assist or impersonate buyers in the same cost center during navigation or purchase. |
| Organization Admin | `customer-admin` | Main organization user who manages the organization information, as well as its members and cost centers. |
| Organization Approver | `customer-approver` | Organization user who can take a saved cart or quote that was created by an **Organization Buyer** and use it to place an order. |
| Organization Buyer | `customer-buyer` | Organization user who has the ability to add items to cart. If the **B2B Quotes** app is installed, they are also able to save their cart for future use or create a quote. |


## How it works

**Storefront Permissions** communicates automatically with other [B2B Suite](https://developers.vtex.com/docs/guides/vtex-b2b-suite) apps, such as [B2B Organizations](https://developers.vtex.com/docs/guides/vtex-b2b-organizations), where it enables different organization management capabilities depending on each user’s role.

It also allows you to configure available permissions when developing your own app, associate them with the predefined roles, and have these permissions checked by other applications – if you perform the steps described in the [Advanced app integration](#advanced-app-integration-optional) section.

The **Storefront Permissions** app does not contain an interface – it operates “backstage”, storing the predefined roles and serving as a bridge to communicate with other apps in order to check user permissions. If you would like to manage roles and app permissions using the VTEX Admin interface, you must also install the [Storefront Permissions UI](https://developers.vtex.com/docs/guides/vtex-storefront-permissions-ui) app. As an optional feature, you can install the [Admin Customers](https://developers.vtex.com/vtex-developer-docs/docs/vtex-admin-customers) app for additional customer management capabilities.


## Before you start

Make sure you have the [VTEX IO CLI (Command Line Interface)](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-install) installed in your machine.

If you opt to develop your own app and [integrate](#advanced-app-integration-optional) it with **Storefront Permissions**, read our documentation on [Developing an app](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-developing-an-app).


## Installation

You can install the app by running `vtex install vtex.storefront-permissions` in your terminal, using the [VTEX IO CLI](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-installation-and-command-reference).


## Advanced app integration [optional]

If you would like to develop your own app and integrate it with **Storefront Permissions**, follow the steps below.

1. Open your app’s repository.
2. In the `manifest.json` file, add `vtex.storefront-permissions` under the `builders` property, as follows.

    ```json
    "builders": {
    "vtex.storefront-permissions": "1.x"
    }
    ```

3. In the root folder, create a new folder named `vtex.storefront-permissions`.
4. In the `vtex.storefront-permissions` folder, create a `configuration.json` file. The content of this file should follow the format below. Keep in mind that you must replace the example information with the `name` of your app and its `features`.

    ```json
    {
      "name": "My awesome app",
      "features": [
        {
          "label": "View",
          "value": "view-awesome-things",
          "roles": ["store-admin","sales-admin","sales-manager","sales-representative","customer-admin","customer-approver","customer-buyer"]
        },
        {
          "label": "Create",
          "value": "create-awesome-things",
          "roles": ["store-admin","sales-admin","sales-manager","sales-representative"]
        },
        {
          "label": "Delete",
          "value": "delete-awesome-things",
          "roles": ["store-admin","sales-admin","sales-manager","sales-representative"]
        },
        {
          "label": "Special Access",
          "value": "allow-special-access",
          "roles": ["store-admin","sales-admin"]
        }
      ]
    }
    ```

    Below you can find a description of each property.

    | **Property** | **Type** | **Description** |
    |---|---|---|
    | `name` | string | Name of your app. |
    | `features` | array of objects | List of features related to your app – the functionalities of your app that you want to set permissions for users to be able to access or not. |
    |  ⤷  | object | Object containing information about each feature of your app. |
    |    ⤷ `label` | string | Name or description of the feature. |
    |    ⤷ `value` | string | Identifier key you want to use for the feature, as used in your app’s [custom storefront components](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-developing-custom-storefront-components). Do not use space or special characters in this field. |
    |    ⤷ `roles` | array of strings | List with the keys for all the roles you want to associate with the permission to use the feature by default. You can find more information about each role and its key in the [Available Storefront Roles section](#available-storefront-roles) of this documentation. |

5. Make sure you refer to the `value` – the identifier key – for each feature you want to set permissions for in your [custom storefront components](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-developing-custom-storefront-components)’ code, when developing your app.

    Example: in the B2B Organizations app, one of the permissions created is represented by the following object.

    ```json
    {
      "label": "Create Cost Center",
      "value": "create-cost-center-organization",
      "roles": ["store-admin","sales-admin","customer-admin"]
    }
    ```

    Therefore, in a [custom storefront component’s code](https://github.com/vtex-apps/b2b-organizations/blob/366a28add226eac5d9b104bb13a9f2cd1d574f02/react/components/CostCenterDetails.tsx) in TypeScript, whenever referring to this feature, it uses `create-cost-center-organization`.


Once you are done developing and installing your own app, if you have [Storefront Permissions UI](https://developers.vtex.com/docs/guides/vtex-storefront-permissions-ui), the features of your app associated with each role will be automatically loaded on the **Storefront Permissions** page. For more details on this, read our documentation on the [Storefront Permissions UI](https://developers.vtex.com/docs/guides/vtex-storefront-permissions-ui) app.


### GraphQL queries

Now that your app is integrated, you can write a GraphQL query on your app to check the current user's permission within the context of your app.

First, you need to associate your test user to a Role containing your app's permission by following the [B2B Organizations documentation](https://developers.vtex.com/docs/guides/vtex-b2b-organizations#users).

It is not necessary to declare your app name nor user credentials, the query will take care of these details.


#### checkUserPermission

This query allows you to check which permissions a user has in the context of your app. When the query is performed, **Storefront Permissions** checks which app the request is coming from, and returns the current user's permissions for that specific app.

The response will be a list with all the permissions the current user has on the app.

Sample query:

```graphql
query permissions {
  checkUserPermission @context(provider: "vtex.storefront-permissions") {
    role {
      id
      name
      slug
    }
    permissions
  }
}
```


Sample response:


```graphql
{
  "data":{
    "checkUserPermission": {
      "role": {
        "id": "00549c22-f39d-11eb-82ac-0a55b612700f",
        "name": "Admin",
        "slug": "customer-admin"
      },
      "permissions": ["view-awesome-things","create-awesome-things","delete-awesome-things"]
    }
  }
}
```



#### hasUsers

This query allows you to check if there are any users associated with a specific role. The response will be a boolean, with `"hasUsers": true` if there are users with this role or `false` if there are not.

Sample query:


```graphql
query hasUsers {
  hasUsers(slug: "sales-admin")
    @context(provider: "vtex.storefront-permissions")
}
```


Sample response:


```graphql
{
  "data": {
    "hasUsers": true
  }
}
```



#### checkImpersonation

This query allows you to check if the current user is [impersonating](https://developers.vtex.com/docs/guides/vtex-b2b-organizations#impersonate-users) another user, and retrieve information on the impersonated user.

Sample query:


```graphql
query checkImpersonation {
  checkImpersonation {
    firstName
    lastName
    email
    userId
    error
  }
}
```


Sample response:


```graphql
{
  "data": {
    "checkImpersonation": {
      "firstName": "Andrew",
      "lastName": "Smith",
      "email": "testemail@mail.com",
      "userId": "aaaaa-bbbb-cccc-dddd-eeeee",
      "error": null
    }
  }
}
```

#### getSessionWatcher

Using Session Watcher, **Storefront Permissions** detects changes to the user authentication to trigger changes to its cart and navigation, based on associated price tables, collections, profile information and shipping options.

This query fetches Session Watcher’s status, that is, whether it is active or not. The response will be a boolean, with `true` meaning that it is enabled or `false` meaning it is disabled.

Sample query:

```graphql
query getSessionWatcher {
  getSessionWatcher
}
```


Sample response:


```graphql
{
  "data": {
    "getSessionWatcher": false
  }
}
```



### GraphQL mutation


#### impersonateUser

Using this mutation, you can inform the `userId` to [impersonate an user](https://developers.vtex.com/docs/guides/vtex-b2b-organizations#impersonate-users). To remove impersonation, send an empty `userId` instead.

Sample mutation:


```graphql
mutation impersonateUser($userId: ID)
@context(provider: "vtex.storefront-permissions") {
  impersonateUser(userId: $userId) {
    status
    message
  }
}
```

#### setSessionWatcher

If your account is not using `vtex.b2b-organizations` you may want to disable the Session Watcher to avoid unnecessary operations. To do so, set the `active` property to `false` in the mutation exemplified below.

The response will be a boolean, with `true` for a successful operation or `false` for a failure.

Sample mutation:

```graphql
mutation setSessionWatcher {
  sessionWatcher(active: false)
}
```

Sample response:

```graphql
{
  "data": {
    "sessionWatcher": true
  }
}
```