---
title: "Setting up Newsletter opt-in with Master Data v1"
excerpt: "Learn how to configure newsletter subscriptions with Master Data v1."
slug: "newsletter-inclusion-master-data-v1"
hidden: false
createdAt: "2022-10-20T18:16:54.439Z"
updatedAt: "2022-10-20T19:13:15.403Z"
---

In this article, we will guide you through configuring **Master Data** to collect the email addresses of customers who wish to subscribe to your newsletter. 

Newsletter inclusion is a form that can be integrated into any page of your store website (except checkout), allowing you to capture the email addresses of customers who express an interest in receiving updates about your store. This registration is usually associated with a store promotion.

Integrating newsletter subscriptions with **Master Data** streamlines customer management since all the store's registered customers are already stored in Master Data.

## Before you begin

- Install the SafeData app in your VTEX account. SafeData provides a middleware for retrieving and storing Master Data (v1 e v2) information directly from the frontend. For more information, please refer to the [SafeData documentation](https://developers.vtex.com/docs/apps/vtex.safedata).

## Instructions

Below, we provide a step-by-step guide to assist you in setting up this configuration:

1. Create the necessary fields in the CRM. This step is only necessary if you want an extra field in addition to those already in your CRM. If this is the case, please refer to the [Creating a field in Master Data
](https://help.vtex.com/tutorial/how-can-i-create-field-in-master-data) guide.
2. Implement the fields in the HTML of the page determined by the store.
  >⚠️ Please note that the `vtex.cmc:newsletterOptIn` control has been discontinued and should no longer be employed. Instead, use the HTML code created by your development team to achieve this functionality on the store's designated page.
3. Send the information via SafeData API. The SafeData app provides endpoints similar to Master Data endpoints. Use the example request below to update a user profile and enable newsletter opt-in:

**Method:** `PATCH`

**Path:**

```
https://{{accountName}}.vtexcommercestable.com.br/api/io/safedata/CL/documents/{{documentId}}
```

**Body:**
```json
{
  "firstName": "Jonh",
  "lastName": "Lennon",
  "email": "jonh.lennon@lennon.com.br",
  "isNewsletterOptIn": true
}
```

By following these steps and utilizing the SafeData API, you can efficiently manage and enhance your newsletter subscription process, keeping your customers engaged and informed. Your CRM will now reflect the email addresses of those who have opted to receive your newsletter.
