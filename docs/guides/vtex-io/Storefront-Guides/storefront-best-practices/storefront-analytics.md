---
title: "Analytics"
slug: "storefront-analytics"
hidden: false
createdAt: "2024-12-18T17:53:38.402Z"
updatedAt: ""
excerpt: "Explore how to leverage data to drive informed decisions and optimize your VTEX store performance."
---

Analytics involves collecting, processing, and analyzing data to identify patterns and insights that support decision-making. In ecommerce, analytics helps businesses understand user experience, optimize operations, and drive sales growth.

By tracking customer interactions on your website, such as product views and purchasing decisions, you gain insights into their needs and can tailor experiences to improve satisfaction and conversion.

To turn insights into actionable strategies, leveraging the right tools is essential. [Google Analytics (GA)](https://marketingplatform.google.com/intl/en-US_us/about/analytics/), the world's most widely used web analytics tool, offers comprehensive features for data collection, analysis, and reporting to help businesses understand and optimize their online presence.

The integration with Google Analytics is available for all VTEX stores. Learn more in [Configuring Google Analytics 4 in VTEX stores](https://help.vtex.com/en/tutorial/how-to-setup-google-analytics-in-vtex-store--G2P0rmSrEiqCcmUMyUUwG).

## Implementing Google Analytics

Integrating Google Analytics with your VTEX storefront allows you to track key ecommerce metrics and customer behavior, such as product views, cart activity, and checkout behavior, directly within the VTEX platform.

To learn how to implement Google Analytics, see the section for your store's storefront solution.

### Store Framework

In [Store Framework](https://developers.vtex.com/docs/guides/store-framework), a VTEX IO app manages Google Analytics by implementing the [Google Tag Manager (GTM)](https://tagmanager.google.com/) script, setting event properties, and adding events to the `dataLayer`.

> ℹ️ Learn more in the guide [Analytics on Store Framework](https://developers.vtex.com/docs/guides/storefront-analytics-on-store-framework).

Below are the main characteristics of Google Analytics in Store Framework:

- It's easy to handle and maintain, as everything is configured to automatically track and send data to GTM by using the native Google Tag Manager app. However, deviating from the predefined settings requires significant effort and customization, often defeating the framework's purpose.
- Provides analytics events for free when using the native Google Tag Manager app and native blocks to compose your pages. In this case, you do not need to actively manage analytics, but this convenience comes with limitations and less control over customization.
- Identifying where or when an event is triggered can be challenging, making debugging and customization more challenging. You rely on the app's predefined events and DOM interactions, which may limit visibility and control.

### FastStore

In [FastStore](https://developers.vtex.com/docs/guides/faststore), there is no equivalent app; instead, all management is done directly within the storefront source code.

> ℹ️ Learn more in the guide [Analytics on FastStore](https://developers.vtex.com/docs/guides/faststore/analytics-overview).

Below are the main characteristics of Google Analytics in FastStore:

- You can trigger your own events, customize them with your own types, and add any properties of your choice. This flexibility empowers developers and store managers to collect data tailored to their business needs.
- You have the flexibility to implement analytics based on your business needs, but you are responsible for triggering events and ensuring their completeness. Events will not trigger automatically unless you include them, which requires careful attention from maintainers to avoid gaps in analytics.
- All analytics events can be found in the store repository. You can easily search for [`sendAnalyticsEvent`](https://developers.vtex.com/docs/guides/faststore/analytics-send-analytics-event) calls to understand when and where events are triggered. Additionally, FastStore provides end-to-end (E2E) tests for [GA4 Recommended events](https://support.google.com/analytics/answer/9267735?sjid=7873480420853807302-SA), helping you identify and fix issues before they impact data collection.
