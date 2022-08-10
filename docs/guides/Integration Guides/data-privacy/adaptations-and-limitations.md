---
title: "Adaptations and limitations"
slug: "adaptations-and-limitations"
hidden: true
createdAt: "2022-02-22T22:29:28.541Z"
updatedAt: "2022-08-08T15:30:31.954Z"
---
[block:callout]
{
  "type": "danger",
  "body": "This feature is in closed beta phase, meaning we are working to improve it. Do not share this documentation with people outside of your company.",
  "title": "Closed beta"
}
[/block]
In order to integrate with the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and manage your customers’ information in compliance with data privacy laws, you should be mindful of some adaptations and limitations that will impact other integrations you may have.


## Adaptations

### OMS API

In order to use order management APIs, you should adapt your integrations to use new endpoints, for features you may already have implemented in your store, such as retrieving order information or notifying invoices. See the table below to know which endpoints need adaptation and where to find the new reference.

| **Feature**                | **Previous endpoint**                                                                                                                                         | **New endpoint (PII compliant)**                                                                                                                                        | **Payload changed** |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| Get order                  | `GET` [/api/oms/orders/{orderId}](https://developers.vtex.com/vtex-rest-api/reference/getorder)                                                               | `GET` [/api/orders/pvt/document/{orderId}](https://developers.vtex.com/vtex-rest-api/reference/getorderpiicompliant)                                                    | No                  |
| List orders                | `GET` [/api/oms/pvt/orders](https://developers.vtex.com/vtex-rest-api/reference/listorders)                                                                   | `POST` [/api/orders/extendsearch/orders](https://developers.vtex.com/vtex-rest-api/reference/listorderspiicompliant)                                                    | Yes                 |
| Start handling order       | `POST` [api/oms/orders/{orderId}/start-handling](https://developers.vtex.com/vtex-rest-api/reference/starthandling)                                           | `POST` [/api/orders/pvt/document/{orderId}/actions/start-handling](https://developers.vtex.com/vtex-rest-api/reference/starthandlingpiicompliant)                       | No                  |
| Cancel order               | `POST` [api/oms/pvt/orders/{orderId}/cancel](https://developers.vtex.com/vtex-rest-api/reference/cancelorder)                                                 | `POST` [/api/orders/pvt/document/{orderId}/cancel](https://developers.vtex.com/vtex-rest-api/reference/cancelorderpiicompliant)                                         | No                  |
| Order invoice notification | `POST` [api/oms/orders/{orderId}/invoice](https://developers.vtex.com/vtex-rest-api/reference/invoicenotification)                                            | `POST` [api/orders/pvt/document/{orderId}/invoices](https://developers.vtex.com/vtex-rest-api/reference/invoicenotificationpiicompliant)                                | Yes                 |
| Send payment notification  | `POST` [/api/oms/pvt/orders/{orderId}/payments/{paymentId}/payment-notification](https://developers.vtex.com/vtex-rest-api/reference/sendpaymentnotification) | `POST` [/api/orders/pvt/document/{orderId}/payment/{paymentId}/notify-payment](https://developers.vtex.com/vtex-rest-api/reference/sendpaymentnotificationpiicompliant) | No                  |



### Master Data - CL, AD, BK entities 

In the new solution architecture, Master Data will no longer have CL, AD, BK entities. There will be a new isolated system to protect those information, Profile System.

If you are integrated to Master Data API to get any of this data (CL, AD, BK entities) you will need to integrate with the new [Profile System APIs](https://developers.vtex.com/vtex-rest-api/docs/profile-system).

### Checkout

[Checkout](https://developers.vtex.com/vtex-rest-api/reference/orderform-fields) endpoints that deal with getting order information keep the same paths but with different behaviors. Contracts are the same for masked data, but for complete data you must include the query parameter: `reason`. Learn more about [retrieving unmasked data](https://developers.vtex.com/vtex-rest-api/docs/profile-system#masked-data).

### Payments

In order to be able to view transaction logs, store users must be assigned a role with the resource `View Payments Sensitive Data`, from the `PCI Gateway` product in the License Manager. Learn more about [License Manager resources](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3) and how to [Create roles](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#creating-a-role).


## Limitations

### Master Data

Note that **Master Data** features may be impacted in the following two aspects.

#### Orders Index 

This is a legacy integration that was deprecated. VTEX will disable it.

#### CL

Master Data custom CL fields are not supported.


### Promotions - Customer cluster

The **Customer cluster** field will be disabled when creating a promotion, which means it will not be possible to apply [promotions to specific customer clusters](https://help.vtex.com/en/tutorial/creating-promotion-for-a-customer-cluster--tutorials_342), since cluster segmentation is based on PII stored in CL entity fields.


### Pricing - Price tables

The [Price tables](https://help.vtex.com/en/tutorial/creating-price-tables--58YmY2Iwggyw4WeSCGg24S#) feature is not suported.

### OMS 

VTEX’s Order Management System is impacted by in a few different features. See details below.

#### Conversation tracker


Transactional email messages will continue to work normally, shoppers will still receive status updates. However, messages will no longer be tracked in the Admin, that is, it will no longer be stored on our platform.


#### DO


Your store should not enter any data that contains PII information.


#### Shipping notifications


Your store should not enter any data that contains PII information. In addition, tracking information cannot contain PII.

For example, feel free to use sentences like these, without including shoppers’ addresses: “Your order was sent to the distribution center”, “Your order was sent to the residence”, among others.


#### Subscriptions


VTEX will disable subscriptions.

#### Call center


You must disable call center impersonation must be disabled at the License Manager.


#### Orders Admin interface

The PII rules have also been applied to the [Orders List (Beta)](https://help.vtex.com/tutorial/order-list-beta--2QTduKHAJMFIZ3BAsi6Pi) and [Order details (Beta)](https://help.vtex.com/tutorial/order-details-page-beta--2Y75n54Cc9VizrlG1N6ZNl) pages. The pages have been adjusted so that: 

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
5. Click on `Confirm`. 


### MessageCenter - Admin panel

When you edit an email template on the **Message Center** Admin interface, you can see information about the last email sent from that template, rendered as an email. All values on the JSON Data will be masked.

### My account

The [My account](https://help.vtex.com/en/tutorial/how-does-my-account-work--2BQ3GiqhqGJTXsWVuio3Xh#) section, which allows shoppers to view their profile and orders’ information, is not supported in the PII compliant system for the time being.

### Gift card

The [gift card](https://help.vtex.com/en/subcategory/gift-card--3qWeS7abxCyC0G0GMq42gA#) feature is not supported.

### Credit control

The [credit control](https://help.vtex.com/en/search?page=1&q=credit%20control) feature is not supported.