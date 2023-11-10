---
title: "Adding telesales impersonated email using the Session Manager"
slug: "adding-telesales-impersonated-email-using-the-session-manager"
hidden: false
createdAt: "2022-08-04T22:00:42.668Z"
updatedAt: "2022-08-04T22:30:28.283Z"
---
For B2B ecommerce operations, telesales operators must be able to conclude purchases on behalf of customers, by "impersonating" them. This is because, in this scenario, it is common for sales to be made on the platform, but not directly by the customer.

In order to allow this type of selling, VTEX offers the telesales feature, through which an operator "takes the place" of the final customer during the process of choosing the products and the checkout. The operator takes over the customer's user, with limited permissions, and is able to make purchases.

## Telesales Toolbar 

The [telesales toolbar](https://help.vtex.com/en/tutorial/telesales-toolbar--tutorials_5500) is the most straightforward way to use the telesales feature. A top bar appears on the store's frontend once the registered operator logs in to the store environment. It is displayed in all site areas, except on the [My Orders screen](https://help.vtex.com/en/tutorial/how-my-account-works--2BQ3GiqhqGJTXsWVuio3Xh#orders).

These are the steps required to use the telesales toolbar:
1. [Create a telesales user](https://help.vtex.com/tutorial/como-criar-um-usuario-de-televendas--frequentlyAskedQuestions_4227).
2. [Make a purchase via telesales](https://help.vtex.com/tutorial/comprar-em-nome-do-cliente-pelo-televendas--4gsnClNy1iUCkSK6y0GI2O).

Also you can [customize the telesales toolbar](https://help.vtex.com/tutorial/usando-e-customizando-toolbar-de-televendas--tutorials_5500).

## Session API 

Although the telesales toolbar is the simplest option to allow "impersonated" purchases, you can use the Session Manager API to achieve the same effect, but with greater control by the store.

[Session Manager](https://developers.vtex.com/vtex-rest-api/docs/session-manager) is a system that tracks the current browsing session of all end customers in VTEX stores. Its API allows the store to gather relevant session information, automatically captured and stored in a safe and easily accessible location.

For more complex B2B operations, building an integration directly with the Session Manager API may be interesting. In this case, instead of impersonating the customer through the telesales toolbar, the store inserts the customer's email address to be impersonated into the Session Manager’s information. 

If the session administrator has permission to impersonate customers, each impersonated user’s ID and email will be loaded into the session, and the operator can make purchases on their behalf.

### Installing the vtex.impersonate-session app 

A session is made up of JSON objects, which are fed with information from a series of apps installed in the store. One of these apps is the `vtex.impersonate-session`, which allows impersonating customers.

This app is not installed by default in VTEX stores. So, first of all, you need to install it. For this, you must use VTEX CLI. If it is not yet installed on your computer, install it by running the command below on your terminal:

```
yarn global add vtex
```
[block:callout]
{
  "type": "info",
  "body": "Learn more about [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference)."
}
[/block]
Once the CLI is installed, log into your store by running the command:
```
vtex login
```

Now, let's install the `vtex.impersonate-session` app. Type the following command:
```
vtex install vtex.impersonate-session
```

The app is already installed in your store, and the customer impersonation feature has been enabled.

### Using Session Manager to impersonate customers

The `vtex.impersonate-session` app, like all apps with session dependencies, monitors changes to their inputs and modifies session parameters through their outputs.

It receives the `vtex-impersonated-customer-email` parameter through a direct `POST` or cookie and tries to impersonate the user who owns this email by using the administrator’s credentials in the session. If these credentials are allowed to impersonate customers (in other words, if the operator has the telesales role), the ID and email of the impersonated user are loaded into the session.

These are the request's inputs:
- `public`: `vtex-impersonated-customer-email`
- `cookie`: `vtex-impersonated-customer-email`
- `authentication`: `adminUserEmail`

And these are the outputs returned by the app:

- `impersonate`: `storeUserId`, `storeUserEmail`, `canImpersonate`, `account`

See an example of an object sent in the request:
```json
{
    "public": {
        "vtex-impersonated-customer-email": {
            "value": "client@gmail.com"
        },
        "authentication": {
            "value": "operator@gmail.com"
        }
    }
}
```

Example response body:
```json
"public": {
            "vtex-impersonated-customer-email": {
                "value": "client@gmail.com"
            },
            "authentication": {
                "value": "operator@gmail.com"
            }
        },
        "impersonate": {
            "canImpersonate": {
                "value": "true"
            },
            "account" : {
                "value": "myStore"
            }
        }
```