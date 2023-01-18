---
slug: "safedata-can-now-block-the-anonymous-creation-of-documents-for-all-master-data-entities"
title: "SafeData can now block the anonymous creation of documents for all Master Data entities"
createdAt: 2023-01-18T16:53:15.322Z
hidden: false
type: "improved"
---

SafeData is an app that provides an easy-to-use, configurable middleware to retrieve and save information to Master Data V1 and V2. As of January 23, 2023, VTEX is improving the way you control the creation of documents with SafeData.

>❗ If your store uses SafeData to anonymously create Master Data documents in the data entities `CL` or `AD`, make sure to read the changes described below and make the necessary adaptations. Otherwise, SafeData might cease to work correctly in your store.

>ℹ️ Information type calloutLearn more about [how to use SafeData](https://developers.vtex.com/docs/guides/vtex-safedata).

## What changed?

SafeData allows anonymous users to create documents in Master Data [data entities](https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw#data-entities). This is useful for some scenarios, such as registering newsletter subscriptions.

However, it was previously not possible to prevent this behavior for Master Data v1 data entities `CL` and `AD`. Now you can choose to allow or block the anonymous creation of documents via SafeData for each entity you wish, including `CL` and `AD`, by setting the flag **Allow creating objects anonymously**.

## What needs to be done?

Starting january 23, 2023, SafeData will, by default, block the anonymous creation of Master Data documents for Master Data v1 [data entities](https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw#data-entities) `CL` and `AD`. So if your store uses SafeData to create documents anonymously in the data entities `CL` or `AD`, you must change your app settings in the admin panel to allow this behavior. Otherwise, documents will not be created anonymously and you will get integration errors.  

To allow this behavior, follow these steps:

1. Open the VTEX Admin panel.
2. Go to **ACCOUNT SETTINGS** > **Apps** > **My Apps**.
3. Click on the **SafeData** widget.
4. You will see a list of data entities with the corresponding. Set the **Allow creating objects anonymously** for each data entity that you wish to allow this behavior.


