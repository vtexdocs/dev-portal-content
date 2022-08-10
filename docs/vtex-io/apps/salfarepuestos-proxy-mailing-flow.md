---
title: "Proxy Mailing Flow"
slug: "salfarepuestos-proxy-mailing-flow"
excerpt: "salfarepuestos.proxy-mailing-flow@0.0.5"
hidden: true
createdAt: "2022-07-26T17:09:26.800Z"
updatedAt: "2022-07-28T08:37:41.212Z"
---
This service allows you to handling the mailing to be able to cancel and generate orders without repeating notifications to the user.

## Flows

With this application you can customize the emails when the orders pass through the `order-created` and `invoiced` states. You also can skip notifications to the user when the order is created adding a custom app (in custom data) to the order, this custom app must have an `"id": "origin"`.

## Settings fields
There are 6 fields to complete for configure the app.
- Default email: is the email for mailing flows that doesn’t find any seller.

- Subscriber MasterData Entity List: here you can define one (at least) or more data entity acronyms for the subscribers to the mailing flow (example: seller and supervisor).

- Client Mailing Template Name (order-created): is the name of the message-		center template url.

- Client Mailing Template Name (invoiced): is the name of the message-center template url.

- Subscribers Mailing Template Name (order-created): is the name of the message-center template url.

- Subscribers Mailing Template Name (invoiced): is the name of the message-center template url.

You can see how to modify the templates [**here**](https://developers.vtex.com/vtex-rest-api/docs/how-to-set-up-functions-in-the-message-center-templates)

![Settings fields](https://user-images.githubusercontent.com/55720621/135907990-74d3fd11-e2fb-4232-9a79-e26772f71dba.png)
## Steps by step:
1. First you have to [**disable transactional emails**](https://help.vtex.com/en/tutorial/how-to-disable-a-transactional-email--frequentlyAskedQuestions_6715). 
2. You need to install this app running `vtex install vtexarg.proxy-mailing-flow@3.x` command on the *vtex toolbelt*.
3. Then you must hook the order status changes to this service. You can see how to do this [**here**](https://developers.vtex.com/vtex-rest-api/reference/order-hook-1#hookconfiguration) (you need admin super roll). Here the body example:
    >     {
    >       "filter": {
    >         "type": "FromWorkflow",
    >         "status": ["order-created", "invoiced"]
    >       },
    >       "hook": {
    >         "url": "https://{{accountName}}.myvtex.com/_v/proxy-mailing-flow/"
    >       }
    >     }
4. Configure the settings fields of the app in the link `https://{{account}}.myvtex.com/admin/apps/vtexarg.proxy-mailing-flow@3.x/setup`.