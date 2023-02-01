---
title: "Subscriptions v3 migration guide"
slug: "subscriptions-v3-migration-guide"
hidden: false
createdAt: "2021-02-04T15:24:59.474Z"
updatedAt: "2022-08-23T15:46:45.291Z"
---

The Subscriptions Module is an app developed by VTEX to facilitate recurring sales in your store. It works as an automatic scheduler, executing a repurchase at the frequency requested by the customer. Check out our article about [how subscriptions work](https://help.vtex.com/en/tutorial/como-funciona-a-assinatura--frequentlyAskedQuestions_4453) and the [Subscriptions V3 API reference](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3#overview) to know more.

This article explores all the changes the v3 module has brought, compared to the v2, and details the steps needed so your store is fully integrated with the new module.

## What changed

The v3 module’s changes include:

Improvements on how your customers view and manage their subscriptions in your store.

- How an order’s cycle date is calculated.
- What a subscription means to our system.
- Renaming some attributes.
- All API endpoints have gone through structural changes.

For stores that don’t consume our API in their integrations, it is not necessary to make any adaptation or setup, our system will implement the new module automatically.

For stores or partners that consumed our Subscriptions API, it is necessary to implement new endpoints so your integrations operate with the new module. The whole migration process will be carefully supervised by the VTEX team to guarantee a smooth transition.

## What is a “subscription” to Subscriptions v2?

In the Subscriptions v2 module, the entity subscription was an order composed of a single SKU tied to a given purchase setting. Purchase settings include the following attributes:

- User profile
- Address
- Payment method
- Frequency
- Start day of the subscription’s cycle

This principle allowed the store’s customers to subscribe to several SKUs using different delivery addresses and payment methods - which represented an evolution compared to the system’s first version.

This behavior required another entity to be created: the subscriptionGroup. It allowed subscribed SKUs with similar purchase settings to be grouped in your customers’ My Account page, so they could see their subscription orders in a more organized way. The diagram below illustrates those concepts:
![Subscription v2 concept diagram](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/subscriptions-v3-migration-guide-0.PNG)

![Subscription v2 grouping examples](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/subscriptions-v3-migration-guide-1.png)

## What is a “subscription” to Subscriptions v3?

For the 3rd version of our module, we have changed our system’s understanding of what is a subscription. Now, subscriptions are a list of SKUs, tied to a certain purchase setting.

This change takes out the need of creating a subscriptionGroup to arrange multiple SKUs.
Therefore, all operations function around the `subscription` entity (which holds all the data necessary to generate a subscription order), instead of `subscriptionGroup`. The diagram below illustrates the updated concept:
![Subscription v3 concept diagram](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/subscriptions-v3-migration-guide-2.PNG)

We have also renamed the entity `subscriptionOrder` to `subscriptionCycle`. Now a subscription is not tied necessarily to the first order.

## Calculating the cycle date

How our system calculates an order’s next cycle date has also changed:

- **Subscriptions v2**: it was calculated from the first order’s starting date. All cycle dates had to follow that first chosen date, users could not change it.
- **Subscriptions v3**: it is calculated based on the previous cycle date, instead of the first one ever. The first order’s date is only used for that first purchase, when the subscription hasn’t yet been executed.

This means users can change the date whenever they want, since the following orders will be executed based on the previous cycle date. To enable this feature, we have developed an API that allows users to choose exactly when they want their next order to be executed, without needing to change the subscription’s frequency as a work-around.

All changes between v2 and v3 modules are summarized in the table below:

| **Subscriptions v2**                                                      | **Subscriptions v3**                                                         |
|---------------------------------------------------------------------------|------------------------------------------------------------------------------|
| `subscriptionGroup`                                                       | -                                                                            |
| `subscriptionOrder`                                                       | `subscriptionCycle`                                                      |
| Subscription: order composed of an SKU tied to a certain purchase setting | Subscription: a list of SKUs, tied to a certain purchase setting             |
| Next cycle date: the same as the first order’s starting date          | Next cycle date: calculated based on the previous order’s cycle date |

## Migration

If your stores don’t rely on our API for any integrations, no adaptation or migration should be made - the new module will be implemented automatically by our system.

Stores that call our Subscriptions API must adapt their integrations, so the new module is fully operational. We remind you that the whole migration process will be fully supervised and assisted by the VTEX team, via ticket.

### Message center

Subscriptions v3 uses a different [Message center](https://help.vtex.com/en/tutorial/understanding-the-message-center--tutorials_84#) email template than v2 for the *Subscriptions - Next Order* stage of a given cycle.

Below you can see what the equivalent template is, if you wish to customize this transactional email:

| **Subscriptions v2**                                                       | **Subscriptions v3**   |
|----------------------------|-------------------------|
| `vtexcommerce-subscriptions-reminder` | `next-subscription-order-reminder` |

### API endpoints

We have standardized our endpoints’ structure, so your developer experience is more consistent. Check out the table below, to compare the changes to all endpoints:

| **Subscriptions v2**                                                       | **[Subscriptions v3](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3#overview)**                                                                                                                                                                        |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ALL] /api/rns/subscriptions/*                                             | Deprecated                                                                                                                                                                                  |
| [GET] /api/rns/subscriptions-group/:groupId:                               | [GET] [/api/rns/pub/subscriptions/:subscriptionId:](https://developers.vtex.com/vtex-developer-docs/reference/subscriptions-1#get_api-rns-pub-subscriptions-id)                             |
| [PATCH] /api/rns/subscriptions-group/:groupId:                             | [PATCH] [/api/rns/pub/subscriptions/:subscriptionId:](https://developers.vtex.com/vtex-developer-docs/reference/subscriptions-1#patch_api-rns-pub-subscriptions-id)                         |
| [GET] /api/rns/subscriptions-group                                         | [GET] [/api/rns/pub/subscriptions](https://developers.vtex.com/vtex-developer-docs/reference/subscriptions-1#get_api-rns-pub-subscriptions)                                                 |
| [GET] /api/rns/subscriptions-group/list                                    | [GET] [/api/rns/pub/subscriptions](https://developers.vtex.com/vtex-developer-docs/reference/subscriptions-1#get_api-rns-pub-subscriptions)                                                 |
| [GET] /api/rns/subscriptions-group/simulate/:groupId:                      | [GET] [/api/rns/pub/subscriptions/simulate](https://developers.vtex.com/vtex-developer-docs/reference/subscriptions-1#post_api-rns-pub-subscriptions-id-simulate)                           |
| [PATCH] /api/rns/subscriptions-group/:groupId:/cancel                      | [PATCH] [/api/rns/pub/subscriptions/:subscriptionId:](https://developers.vtex.com/vtex-developer-docs/reference/subscriptions-1#patch_api-rns-pub-subscriptions-id)                         |
| [POST] /api/rns/subscriptions-group/:groupId:/additem                      | [POST] [/api/rns/pub/subscriptions/:subscriptionId:/items](https://developers.vtex.com/vtex-developer-docs/reference/subscriptions-1#post_api-rns-pub-subscriptions-id-items)               |
| [GET] /api/rns/subscriptions-group/:groupId:/addresses                     | Deprecated, use the profile-system API.                                                                                                                                                     |
| [POST]/api/rns/subscriptions-group/:groupId:/addresses                     | Deprecated, use the profile-system API.                                                                                                                                                     |
| [GET] /api/rns/subscriptions-group/:groupId:/payment-systems               | Deprecated, use the profile-system API.                                                                                                                                                     |
| [GET] /api/rns/subscriptions-group/:groupId:/frequency-options             | [GET] [/api/rns/pvt/plans/:planId](https://developers.vtex.com/vtex-developer-docs/reference/plans#get_api-rns-pvt-plans-id)                                                                |
| [POST] /api/rns/subscriptions-group/:groupid:/instances/:instanceId:/retry | [POST] [/api/rns/pub/cycles/cycleId/retry](https://developers.vtex.com/vtex-developer-docs/reference/cycles#post_api-rns-pub-cycles-cycleid-retry)                                          |
| [GET] /api/rns/subscriptions-group/:groupId:/conversation-message          | Deprecated                                                                                                                                                                                  |
| [GET] /api/rns/subscriptions-group/:groupId:/will-create                   | Deprecated                                                                                                                                                                                  |
| [GET] /api/rns/subscriptions-group/:groupId:/config                        | Deprecated                                                                                                                                                                                  |
| [GET] /api/rns/subscriptions-group/nextPurchase/:dateSR:                   | [GET] [/api/rns/pub/subscriptions](https://developers.vtex.com/vtex-developer-docs/reference/subscriptions-1#get_api-rns-pub-subscriptions)                                                 |
| [GET] /api/rns/settings                                                    | Deprecated                                                                                                                                                                                  |
| [GET] /api/rns/report/reportStatus/:reportId:                              | [GET] [/api/rns/pvt/reports/:templateName/documents/:documentId](https://developers.vtex.com/vtex-developer-docs/reference/reports#get_api-rns-pvt-reports-reportname-documents-documentid) |
| [GET] /api/rns/report/subscriptionsByStatus                                | [POST] [/api/rns/pvt/reports/:templateName/documents](https://developers.vtex.com/vtex-developer-docs/reference/reports#post_api-rns-pvt-reports-reportname-documents)                      |
| [GET] /api/rns/report/subscriptionsByDate                                  | [POST] [/api/rns/pvt/reports/:templateName/documents](https://developers.vtex.com/vtex-developer-docs/reference/reports#post_api-rns-pvt-reports-reportname-documents)                      |
| [GET] /api/rns/report/subscriptionsScheduled                               | [POST] [/api/rns/pvt/reports/:templateName/documents](https://developers.vtex.com/vtex-developer-docs/reference/reports#post_api-rns-pvt-reports-reportname-documents)                      |
| [GET] /api/rns/report/subscriptionsOrderByDate                             | [POST] [/api/rns/pvt/reports/:templateName/documents](https://developers.vtex.com/vtex-developer-docs/reference/reports#post_api-rns-pvt-reports-reportname-documents)                      |
| [GET] /api/rns/report/subscriptionsUpdated                                 | [POST] [/api/rns/pvt/reports/:templateName/documents](https://developers.vtex.com/vtex-developer-docs/reference/reports#post_api-rns-pvt-reports-reportname-documents)                      |
