---
title: "Analytics"
slug: "storefront-analytics"
hidden: false
createdAt: "2024-11-06T14:57:11.767Z"
updatedAt: ""
excerpt: "Explore how to leverage data to drive informed decisions and optimize your VTEX store performance."
---

Analytics involves collecting, processing, and analyzing data to identify patterns and insights that support decision-making. In ecommerce, analytics helps businesses understand user experience, optimize operations, and drive sales growth. 

By tracking customer interactions on your website, such as product views, and purchasing decisions, you gain insights into their needs and can tailor experiences to improve satisfaction and conversions.

To turn insights into actionable strategies, leveraging the right tools is essential. [Google Analytics (GA)](https://marketingplatform.google.com/intl/en-US_us/about/analytics/) is the most widely used web analytics tool globally. It offers comprehensive features for data collection, analysis, and reporting to help businesses understand and optimize their online presence.

The integration with Google Analytics is available for all VTEX stores. Learn more in [Configuring Google Analytics 4 in VTEX stores](https://help.vtex.com/en/tutorial/how-to-setup-google-analytics-in-vtex-store--G2P0rmSrEiqCcmUMyUUwG).

## Implementing Google Analytics

Integrating Google Analytics with your VTEX storefront allows you to track key ecommerce metrics and customer behavior, such as product views, cart activity, and checkout behavior, directly within the VTEX platform. 

To learn how to implement Google Analytics, refer to the relevant section based on the storefront solution your store uses.

### Store Framework

To handle Google Analytics in [Store Framework](https://developers.vtex.com/docs/guides/store-framework), a VTEX IO app implements the [Google Tag Manager (GTM)](https://tagmanager.google.com/) script, which includes setting event properties and adding the events to the `dataLayer`. 

> ℹ️ Learn more in the guide [Analytics on Store Framework](LINK)

Below, see the main characteristics of Google Analytics in Store Framework:

- It is easy to handle and maintain, as everything is already set up to automatically track and send data to GTM by using the native Google Tag Manager app. However, deviating from the predefined settings requires significant effort and customization, often defeating the framework's purpose.
- Gives the analytics events for free when using the native Google Tag Manager app and native blocks to compose your pages. In this case, you do not need to actively manage analytics, but this convenience comes with limitations and less control over customization.
- Can be difficult to determine where or when an event is fired, making debugging and customization more challenging. You rely on the predefined app’s events and DOM interactions, which can limit visibility and control.

### FastStore

In [FastStore](https://developers.vtex.com/docs/guides/faststore), there is no equivalent app; instead, all management is done directly within the storefront source code.

> ℹ️ Learn more in the guide [Analytics on FastStore](LINK)

Below, see the main characteristics of Google Analytics in FastStore:

- You can trigger your own events, customize them with your own types, and add any properties you choose. This flexibility empowers both developers and store managers to collect data in their preferred manner. Discover how to extend and customize types in the guide [Extending and customizing native types](https://v1.faststore.dev/reference/sdk/analytics/how-to-extend-types). To learn how to send custom events, see [Sending custom events](https://v1.faststore.dev/reference/sdk/analytics/how-to-send-custom-events).
- You have the flexibility to implement analytics according to your business needs, but you are responsible for firing events and ensuring completeness. Events will not automatically fire unless you include them, which requires careful attention from maintainers to avoid gaps in analytics.
- All analytics events can be found in the store repository. You can easily search for `sendAnalyticsEvent` calls to understand when and where events are triggered. Additionally, FastStore provides end-to-end (E2E) tests for [GA4 Recommended events](https://support.google.com/analytics/answer/9267735?sjid=7873480420853807302-SA), helping you identify and fix issues before they affect data collection.
