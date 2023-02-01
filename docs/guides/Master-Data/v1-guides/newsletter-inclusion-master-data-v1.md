---
title: "Implementing newletter opt in with Master Data v1"
slug: "newsletter-inclusion-master-data-v1"
hidden: false
createdAt: "2022-10-20T18:16:54.439Z"
updatedAt: "2022-10-20T19:13:15.403Z"
---
Newsletter inclusion is a form that can be entered on any page of your site (except checkout) to get the email address of customers interested in receiving news about the store. This registration is usually associated with a store promotion.

This article will also help configure the inclusion of email addresses of customers who want to receive a newsletter, using Master Data.
[block:callout]
{
  "type": "warning",
  "body": "The `vtex.cmc:newsletterOptIn` control is discontinued and should no longer be used."
}
[/block]
This option for configuration in Master Data is convenient because the details of all your customers are kept in the same place since all the store’s registered customers are already in Master Data. In other words, it is the appropriate place for customer maintenance and action, and having all the records in one place makes life easier.

Here is a step-by-step guide to this configuration.

1. Create the fields you need in the CRM. This step is only necessary if you want an extra field in addition to those already in your CRM. If this is the case, [access our manual for the maintenance of data entities](https://help.vtex.com/tutorial/how-can-i-create-field-in-master-data).
2. Create these fields in the HTML of the page determined by the store. The big change here is that a control is no longer used for this, instead, you use an HTML code created by the store or by the agency.
3. Send the information via [SafeData API](https://developers.vtex.com/docs/guides/vtex-safedata). See more details below.

## Using SafeData to send newsletter information

[SafeData](https://developers.vtex.com/docs/guides/vtex-safedata) provides a middleware to retrieve and save Master Data (v1 e v2) information directly from the frontend. Learn more with the [SafeData guide](https://developers.vtex.com/docs/guides/vtex-safedata).

Once you [install the SafeData app](https://developers.vtex.com/docs/guides/vtex-safedata#getting-started), some endpoints will become available to you, that is very similar to Master Data endpoints. Use a request like the example below to update a user profile to opt-in to the newsletter:

Method
```
PATCH
```

Path
```
https://{{accountName}}.vtexcommercestable.com.br/api/io/safedata/CL/documents/{{documentId}}
```

Body
```
{
  "firstName" : "Jonh",
  "lastName" : "Lennon",
  "email" : "jonh.lennon@lennon.com.br"
  “isNewsletterOptIn”: true
}
```

After this, you can see in your CRM the email addresses which have opted to receive the newsletter.