---
title: "Changes and limitations of the PII data architecture"
slug: "changes-and-limitations-pii-data-architecture"
hidden: true
createdAt: "2022-02-22T22:29:28.541Z"
updatedAt: "2023-05-16T09:38:36.446Z"
---
This document outlines the current limitations associated with the PII data architecture provided by VTEX. By acknowledging these limitations, we provide alternative approaches that may be necessary to ensure data privacy best practices.

Some commerce features of the VTEX platform are not available for accounts using the current PII platform beta version, while others may require adaptations when implemented by the store.

In this guide, you can learn about the changes and limitations you must be aware of when managing your customers' information with the [Profile System](https://developers.vtex.com/docs/guides/profile-system).

>❗ This feature is in closed beta phase, meaning we are working to improve it. Do not share this documentation with people outside of your company.

## Adaptation requirements for feature implementation

In this section, you can learn what VTEX features are available but require adaptation for accounts using the PII data architecture.

### Promotions - Customer cluster

To set up promotions for specific customer clusters in a way that is compatible with the PII data architecture, you must use the `piiClusterExpressions` field instead of `clusterExpressions` in [Promotions and Taxes API](https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api#post-/api/rnb/pvt/calculatorconfiguration).

### OMS

There are no longer restrictions to the use of these OMS features for PII data architecture accounts:

- Subscriptions
- VTEX DO
- Conversation tracker
- Shipping notifications

However, API requests to `/do`, `/conversationtracker`, `/subscriptions`, and `/shipping-tracker` paths must include the query parameter `reason` in order to retrieve unmasked PII information.

#### OMS API adaptations

In order to use order management APIs, you should adapt your integrations to use new endpoints, for features you may already have implemented in your store, such as retrieving order information or notifying invoices. See the table below to know which endpoints need adaptation and where to find the new reference.

| **Feature**                | **Previous endpoint**                                                                                                                                         | **New endpoint (PII data architecture)**                                                                                                                                        | **Payload changed** |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| Get order                  | `GET` [/api/oms/orders/{orderId}](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders/-orderId-)                                                               | `GET` [/api/orders/pvt/document/{orderId}](https://developers.vtex.com/docs/api-reference/orders-api-pii-version#get-/api/orders/pvt/document/-orderId-)                                                    | No                  |
| List orders                | `GET` [/api/oms/pvt/orders](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders)                                                                   | `POST` [/api/orders/extendsearch/orders](https://developers.vtex.com/docs/api-reference/orders-api-pii-version#post-/api/orders/extendsearch/orders)                                                    | Yes                 |
| Start handling order       | `POST` [api/oms/orders/{orderId}/start-handling](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/start-handling)                                           | `POST` [/api/orders/pvt/document/{orderId}/actions/start-handling](https://developers.vtex.com/docs/api-reference/orders-api-pii-version#post-/api/orders/pvt/document/-orderId-/actions/start-handling)                       | No                  |
| Cancel order               | `POST` [api/oms/pvt/orders/{orderId}/cancel](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/cancel)                                                 | `POST` [/api/orders/pvt/document/{orderId}/cancel](https://developers.vtex.com/docs/api-reference/orders-api-pii-version#post-/api/orders/pvt/document/-orderId-/cancel)                                         | No                  |
| Order invoice notification | `POST` [api/oms/orders/{orderId}/invoice](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/invoice)                                            | `POST` [api/orders/pvt/document/{orderId}/invoices](https://developers.vtex.com/docs/api-reference/orders-api-pii-version#post-/api/orders/pvt/document/-orderId-/invoices)                                | Yes                 |
| Send payment notification  | `POST` [/api/oms/pvt/orders/{orderId}/payments/{paymentId}/payment-notification](https://developers.vtex.com/docs/api-reference/orders-api/#post-/api/oms/pvt/orders/-orderId-/payments/-paymentId-/payment-notification) | `POST` [/api/orders/pvt/document/{orderId}/payment/{paymentId}/notify-payment](https://developers.vtex.com/docs/api-reference/orders-api-pii-version#post-/api/orders/pvt/document/-orderId-/payment/-paymentId-/notify-payment) | No                  |

### Master Data - CL, AD, BK entities

In the new solution architecture, Master Data will no longer have CL, AD, BK entities. There will be a new isolated system to protect those information, Profile System.

If you are integrated to Master Data API to get any of this data (CL, AD, BK entities) you will need to integrate with the new [Profile System APIs](https://developers.vtex.com/docs/guides/profile-system).

### Checkout

Although [Checkout](https://developers.vtex.com/docs/guides/orderform-fields) endpoints that retrieve order information use the same path, they may behave differently. Contracts are the same for masked data, but for complete data, you must include the query parameter: `reason`. Learn more about [retrieving unmasked data](https://developers.vtex.com/docs/guides/profile-system#masked-data).

### Payments

In order to be able to view transaction logs, store users must be assigned a role with the resource `View Payments Sensitive Data`, from the `PCI Gateway` product in the License Manager. Learn more about [License Manager resources](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3) and how to [Create roles](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#creating-a-role).


## Limitations

### Master Data

Note that **Master Data** features may be impacted in the following three aspects.

#### Triggers

At the moment, triggers are not supported by the PII platform version Profile System.

#### Orders Index 

This is a legacy integration that was deprecated. VTEX will disable it.

#### CL

Currently, Master Data custom CL fields are not supported.

### Pricing - Price tables

The [Price tables](https://help.vtex.com/en/tutorial/creating-price-tables--58YmY2Iwggyw4WeSCGg24S#) feature is not supported at this moment.

### OMS

VTEX’s Order Management System is impacted on a few different aspects. See details below.

#### Call center

You must disable call center impersonation at the License Manager.

#### Orders Admin interface

The PII rules have also been applied to the [Orders List (Beta)](https://help.vtex.com/tutorial/order-list-beta--2QTduKHAJMFIZ3BAsi6Pi) and [Order details](https://help.vtex.com/tutorial/order-details-page-beta--2Y75n54Cc9VizrlG1N6ZNl) pages. The pages have been adjusted so that: 

- By default, the account will see all data masked.
- Searches by name only work with the shopper's full name.
- Searches by document only work with the shopper's full document ID.

It is possible to configure PII preferences on OMS' interface of your VTEX Admin, by following these instructions:

1. In your VTEX Admin, in the Orders menu, select All Orders. Click on an order on the list.
2. Under the Customer information card, click on `PII Preferences`. 
3. Select one of the following options, to configure how you will view customer's PII and be audited depending on your choice:
    a. On all orders: View personal information and be audited on all orders.
    b. This order only: View PII content and be audited on this order only.
    c. Hide and do not audit: Browse orders without displaying personal information.
4. Click on `Confirm`.

#### Subscriptions

The subscription feature is compatible with the PII data architecture.

However, the **Subscriptions** Admin interface displays only masked PII. If you wish to see unmasked PII, you must use the [Subscriptions v3 API](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3) endpoints, while sending the `reason` query parameter. Learn more about [retrieving unmasked data](https://developers.vtex.com/docs/guides/profile-system#masked-data).

### MessageCenter - Admin panel

When you edit an email template on the **Message Center** Admin interface, you can see information about the last email sent from that template, rendered as an email. Currently, all values on the JSON Data will be masked.

### Gift card

The [gift card](https://help.vtex.com/en/subcategory/gift-card--3qWeS7abxCyC0G0GMq42gA#) feature is not supported for PII platform version accounts yet.

### Credit control

Currently, the [credit control](https://help.vtex.com/en/search?page=1&q=credit%20control) feature is not supported.