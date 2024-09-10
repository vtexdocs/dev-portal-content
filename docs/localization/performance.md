---
title: "Performance"
slug: "performance"
hidden: false
createdAt: "2024-09-10T12:08:37.773Z"
updatedAt: ""
excerpt: "Explore best practices and tools for continuously optimizing website performance."
---

In ecommerce, website performance directly impacts the shopper experience. It may affect **sales conversion rate**, **user session time**, and other relevant metrics. Every millisecond counts, influencing the shopper's decision-making process and affecting your store's **search engine ranking**. Therefore, ensuring that your website is as fast and performant as possible is crucial, which leads to **high scores in [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) audits**.

## Performance slowdowns

As your project becomes more complex, many factors may slow down website performance. For this reason, maintaining optimal website performance is a **continuous effort** that requires commitment.

Some things to keep in mind:

- **Third-party scripts:** Third-party scripts are one of the leading causes of performance slowdowns. These scripts trigger additional network requests to multiple servers and are likely to block DOM construction, keeping the main thread busy and delaying pages rendering.

- **Page weight:** Page weight is the total size of a web page, including all the resources that need loading (i.e., images, stylesheets, and other static files). The heavier the files and data your website sends to the client, the longer the browser takes to render your page. Hence, reducing page weight is a great opportunity to improve website performance.

  Page weight issues are mainly related to:

    - Uncompressed files.
    - Unoptimized images.
    - Unoptimized fonts.
    - Unclean code.

- **HTTP requests:** When a user visits a web page, the browser sends multiple HTTP requests to load all the resources (i.e., images, stylesheets, fonts, etc.) needed to render the web page. Downloading these resources, however, significantly impacts the loading time of the page. Therefore, besides optimizing images, compressing files, and reducing download size, it is also important to consider minimizing download frequency.

- **Render-blocking resources:** Render-blocking resources are scripts, stylesheets, and code files sequentially downloaded, parsed, and executed by the browser. When the browser faces a render-blocking resource, it stops the entire rendering process until these critical files are processed first. Although these resources take a considerable time for the browser to process, they may not be crucial for the user experience.

## Monitoring tools

There are several tools available for identifying performance issues and helping improve website performance, such as:

- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview)/[PageSpeed Insights](https://pagespeed.web.dev/): An open-source automated tool created by Google used to identify common problems related to the quality of a webpage through audits.
- [SpeedCurve](https://speedcurve.com/): Live dashboards that monitor web application experience across different browsers and platforms and provide visibility over performance.
- [PartyTown](https://partytown.builder.io/): A lazy-loaded library to help relocate resource-intensive scripts into a [web worker](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API), keeping them off the [main thread](https://developer.mozilla.org/en-US/docs/Glossary/Main_thread).
- [Google DevTools](https://developer.chrome.com/docs/devtools/): A set of web developer tools built directly into the Google Chrome browser.
