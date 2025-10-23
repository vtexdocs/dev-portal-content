---
title: "VTEX Activity Flow"
slug: "vtex-activity-flow"
excerpt: "Get started with Activity Flow, VTEX's Real User Monitoring (RUM) solution."
hidden: false
createdAt: "2025-10-23T13:37:06.246Z"
---

Activity Flow is VTEX's Real User Monitoring (RUM) solution that captures and analyzes shoppers' navigation actions to generate metrics and insights. These data are used by various internal and platform products to improve the user experience.

The tool tracks page views and sessions, offering a real-time view of the shopper's journey. It logs clicks and mouse movements to evaluate engagement and generate heatmaps, while also monitoring frontend errors and unhandled promise rejections that could hinder conversions. Additionally, it assesses Web Vitals performance metrics and analyzes HTTP requests to identify failures that may impact the user experience. When integrated with [VTEX Ads](https://developers.vtex.com/docs/guides/vtex-ads), it captures ad events, including impressions and clicks, for a comprehensive overview.

This guide provides an overview of the Activity Flow architecture and how to get started with its tracking capabilities.

## Activity Flow architecture

The Activity Flow architecture is designed to have a minimal performance impact due to efficient data handling and task scheduling. It consists of the following stages:

![af_architecture](https://vtexhelp.vtexassets.com/assets/docs/src/af_architecture___9b087c8725f7ed72a1c08142c17eaec1.png) 

1. **Capture user interactions:** Records shopper actions in the storefront or app and packages them into structured client payloads. It runs alongside the user interface, applying consent rules and basic context tagging so events can be reliably attributed later.
2. **Collect events:** Collects client signals at a backend endpoint, validates them, and routes valid items to durable queues while logging or rejecting malformed submissions.
3. **Buffer events:** Buffers incoming events to smooth traffic spikes and keep processing steady, grouping or streaming items so consumers can read them in order without overload.
4. **Process and store events:** Processes buffered data by cleansing, enriching, and deduplicating it, then stores the results in persistent systems to produce query-ready datasets for analysis.

## Next steps

Activity Flow is natively installed in all VTEX accounts. To install it in your headless store or in your mobile app, follow the appropriate guide below.

<Flex>

<WhatsNextCard
title="Installing Activity Flow in Headless stores"
description="Learn how to install Activity Flow in your Headless store."
linkTo="/docs/guides/installing-activity-flow-in-headless-stores"
linkTitle="See more"
/>

<WhatsNextCard
title="Installing Activity Flow in mobile apps"
description="Learn how to install Activity Flow in mobile apps."
linkTo="/docs/guides/installing-activity-flow-in-mobile-apps"
linkTitle="See more"
/>

</Flex>
