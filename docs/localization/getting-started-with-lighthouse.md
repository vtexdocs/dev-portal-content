---
title: "Getting started with Lighthouse"
slug: "getting-started-with-lighthouse"
hidden: false
createdAt: "2024-09-11T15:31:19.301Z"
updatedAt: ""
excerpt: ""
---

<img align="right" src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-io-documentation-getting-started-with-lighthouse-3.png"/>

How users experience your website directly impacts relevant ecommerce metrics, such as user session time and sales conversion rate. Adopting the right tools and strategies to comprehend how shoppers perceive and interact with your website is important to improving your store’s performance. One of the most cutting-edge tools available for assessing your website’s performance from the user’s point of view is [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview).

In this guide, learn how [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) can help you to optimize your website.

## Lighthouse overview

[Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) is a free, open-source tool developed by Google that identifies common issues and provides insights into a website’s performance, usability, and overall quality.

By auditing a web app's URL, Lighthouse generates detailed reports detailing how the page performs according to web standards and developers’ best practices. These insights help enhance the website's quality and user experience.

Lighthouse audits are grouped into five categories:

- [**Performance**](https://web.dev/lighthouse-performance): Evaluates how users perceive and experience a web page by testing key Web Metrics.
- [**Accessibility**](https://web.dev/lighthouse-accessibility/): Evaluates the page usability for people with disabilities or impairments.
- [**SEO**](https://web.dev/lighthouse-seo/): Checks if the page is optimized for search engine results ranking.
- [**Progressive web apps**](https://web.dev/lighthouse-pwa/): Validates the aspects of a Progressive Web App, checking whether a full application-like experience is offered.
- [**Best practices**](https://web.dev/lighthouse-best-practices/): Evaluates the overall code health of a webpage. It also runs checks on best practices for modern web development, most related to security aspects.

## Running Lighthouse audits

There are different ways to conduct a Lighthouse audit: from [PageSpeed Insights](https://pagespeed.web.dev/), in [Chrome DevTools](https://developer.chrome.com/docs/lighthouse/overview/#devtools), from the [command line](https://developer.chrome.com/docs/lighthouse/overview/#cli), or via a [Chrome extension](https://developer.chrome.com/docs/lighthouse/overview/#extension).

>⚠ Although Lighthouse is a powerful tool for inspecting web page quality, it operates only at the URL level. To ensure comprehensive coverage of the web page quality, we strongly recommend testing at least the Home page, a Product Details Page (PDP), and a Collection page of your store.

### FastStore WebOps - Lighthouse Scores

For stores using [FastStore](https://developers.vtex.com/docs/guides/faststore),  you can run Lighthouse audit using the ways presented in the prior section and you can also streamline your web audits by using the [Lighthouse Scores](https://developers.vtex.com/docs/guides/faststore/1-onboarding-dashboard#lighthouse-scores) tool for the [FastStore WebOps](https://developers.vtex.com/docs/guides/faststore/1-onboarding-overview) app.

![WebOps Previews](https://vtexhelp.vtexassets.com/assets/docs/src/lighthouse-scores-webops___f9a501c9132684e7398456db26da2547.png)

Checking these reports helps you keep track of how each PR affects your store's performance, SEO, and accessibility.

Lighthouse reports is a native tool on WebOps. See the [Lighthouse Scores](https://developers.vtex.com/docs/guides/faststore/1-onboarding-dashboard#lighthouse-scores) documentation for more information on using this tool.

## Performance audit

When you submit a URL to Lighthouse to audit your web page performance, it creates a report with the following information:

- [**Performance Score and Metrics**](#performance-score-and-metrics): A weighted average of the *Metrics scores* and the results of independent metrics that aim to represent the user's perception of performance.
- [**Opportunities**](#opportunities): Suggestions and documentation on how to make the page load faster with estimated potential savings.
- [**Diagnostics**](#diagnostics): Additional guidance that developers can explore to improve their pages' performance further.
- [**Passed audits**](#passed-audits): *Opportunities* and *Diagnostics* suggestions that have already been implemented on the page.
- [**Additional information**](#additional-information): Details about the sampled data, including the data collection period, devices used for emulation, chrome version, etc.

In general, only **Metrics** — not the outcomes of **Opportunities** and **Diagnostics** — affect the overall **Performance Score**. However, there is an indirect relationship because implementing Opportunities and Diagnostics suggestions will likely also improve the Metric scores.

### Performance Score and Metrics

The Lighthouse **Performance Score** provides an estimated representation of users' perception of performance. Even if, for a computer, performance could be better described as the time it takes for the whole page to load, this specific metric may not necessarily correspond to anything the user cares about. From the user's point of view, performance is a perception of how he experiences page loading and how responsive a page feels.

To ensure that Lighthouse metrics are relevant to users, they are structured around a few key questions:

![page journey](https://vtexhelp.vtexassets.com/assets/docs/src/Pageloadjourney___7473ce5c7bd0bb307a2c371b06097a4c.png)

1. **Is it happening?** When the first visual activities occur and the user notices that the page is loading. If the server does not respond quickly, the user may feel that there is a problem and leave the page.
2. **Is it useful?** When there is enough valuable content rendered. This moment is capable of keeping the user engaged.
3. **Is it usable?** When the UI seems ready for interaction. This moment can be frustrating if users try to interact with the visible content, but the page is still busy.
4. **Is it delightful?** The moment after loading that guarantees smooth and free-of-lag interactions.

Given these four moments during the page load journey, a series of individual metrics were created, considering what could be relevant for users in each of these moments, such as the time taken for the first contentful paint to be displayed and for the page to become interactive. A weighted average of these metrics determines the final Lighthouse **Performance Score**:

| Audit | Weight |
| ------- -| ---------- |
| [Total Blocking Time (TBT)](#total-blocking-time-tbt--30) | 30% |
| [Largest Contentful Paint (LCP)](#largest-contetful-paint--25) | 25% |
| [Cumulative Layout Shift (CLS)](#cumulative-layout-shift-cls--15) | 25% |
| [First Contentful Paint (FCP)](#first-contentful-paint-fcp--10) | 10% |
| [Speed Index (SI)](#speed-index-si--10)| 10% |

The following sections briefly explain each of these metrics. Notice that the **Total Blocking Time**, **Largest Contentful Paint**, and **Cumulative Layout Shift** have higher weights and, consequently, a greater impact on the overall **Performance Score**. Therefore, paying close attention to these two metrics is paramount.

>⚠ Due to frequent adjustments to Google's ranking formula, the overall **Performance Score** may vary over time. To stay up to date with Lighthouse's latest updates, we recommend visiting the [Lighthouse performance scoring](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring) article.

When running Lighthouse, you will notice that the metrics results obey a color code according to the following ranges:

| Code | Meaning | Range |
| ---------|-----------|---------- |
| <span className="text-4xl text-red-500">▲</span> | Poor | 0-49 |
| <span className="text-3xl text-orange-500">■</span> | Needs improvement | 50-89 |
| <span className="text-3xl text-green-500">●</span> | Good | 90-100 |

#### Total Blocking Time (TBT) | 30%

The [**Total Blocking Time (TBT)**](https://web.dev/lighthouse-total-blocking-time/) is the amount of time between the [**First Contentful Paint (FCP)**](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint) and [**Time to Interactive (TTI)**](https://developer.chrome.com/docs/lighthouse/performance/interactive) during which user inputs, such as mouse clicks, screen taps, or keyboard presses are blocked. When a page has a long TBT, the user may notice the delay and perceive the page as sluggish.

![Total Blocking Time](https://vtexhelp.vtexassets.com/assets/docs/src/tbt___d3d358d1f5dc2882b717f2ab07a7c8d5.png)

User interaction is blocked when a long task blocks the main thread and impedes the browser from responding to other requests. The blocking time starts to be counted after 50ms. For example, if a function takes 150ms to execute, the blocking time is 100ms. Therefore, the **Total Blocking Time** of a page is the sum of the blocking time of each long task that occurs during page load.

Check in the following how Lighthouse classifies TBT times:

|TBT time (milliseconds)|Color-coding|
|--|--|
|Over 600|<span className="text-2xl text-red-500">▲</span>  Poor|
|200 - 600|<span className="text-xl text-orange-500">■</span> Needs improvement|
|0 - 200|<span className="text-xl text-green-500">●</span> Good|

TBT is mainly affected by JavaScript and third-party scripts parsing and execution. Besides removing or reducing JavaScript code, it is possible to improve TBT by splitting long tasks into smaller ones, improving code efficiency, and implementing lazy loading.

>ℹ️ For information on improving TBT, refer to [Google's guidelines](https://web.dev/lighthouse-total-blocking-time/#how-to-improve-your-tbt-score).

#### Largest Contentful Paint (LCP) | 25%

[**Largest Contentful Paint (LCP)**](https://web.dev/lcp/) measures the time it takes to render the largest visible element of the page within the viewport. Fast LCPs help reassure the user that the page is useful.

|LCP time (seconds)|Color-coding|
|--|--|
|Over 4|<span className="text-2xl text-red-500">▲</span>  Poor|
|2.5-4|<span className="text-xl text-orange-500">■</span> Needs improvement|
|0-2.5|<span className="text-xl text-green-500">●</span> Good|

The metric only considers the loading time of elements significantly relevant to the user experience, such as:

- `<img>` elements,
- `<image>` elements inside an `<svg>` element.
- `<video>` elements.
- Elements with a background image loaded via the `url()` function.
- Block-level elements, such as `<h1>`, `<h2>`, `<div>`, `<ul>`, `<table>`, etc.

LCP is primarily affected by the following factors:

- Long server response times.
- Render-blocking resources, such as CSS stylesheets, font files, and JavaScript scripts.
- Resource size and load time.
- Client-side rendering.

>ℹ️ For information on how to improve LCP, refer to [Google's guidelines](https://web.dev/fcp/#how-to-improve-fcp).

#### Cumulative Layout Shift (CLS) | 25%

The [**Cumulative Layout Shift (CLS)**](https://web.dev/cls/) metric measures the impact of undesired content shifts that occur during the entire lifespan of a page.

A layout shift occurs when a visible element changes its initial position from one rendered frame to the next. A website with a low CLS has a steady page display without any elements shifting around. High CLSs may annoy users and affect how they interact with the page, causing them to click an unwanted button or link, for example.

![Cumulative Layout Shift](https://vtexhelp.vtexassets.com/assets/docs/src/cls___0bb6a4c7ea83b32047329627b93a786a.png)

|CLS|Color-coding|
|--|--|
|Over 0.25|<span className="text-2xl text-red-500">▲</span>  Poor|
|0.1 - 0.25|<span className="text-xl text-orange-500">■</span> Needs improvement|
|0 - 0.1|<span className="text-xl text-green-500">●</span> Good|

This metric is mostly affected by images, ads, embeds, and iframes without pre-defined dimensions and by content dynamically inserted by JavaScript on the client side (e.g., a bar that suddenly appears on the header).

>ℹ️ For information on improving CLS, refer to [Google's guidelines](https://web.dev/cls/#how-to-improve-cls).

#### First Contentful Paint (FCP) | 10%

[**First Contentful Paint (FCP)**](https://web.dev/fcp/) measures the time it takes for the browser to render the first bit of content from the Document Object Model (DOM). Short FCP times mean fast visual activity from the browser. They reassure the user that something is happening during the page load and, therefore, are more likely to keep users engaged.

![First Contentful Paint](https://vtexhelp.vtexassets.com/assets/docs/src/lcp___772cb8feaa8a68d31c429ccd60041395.png)

Check in the following how Lighthouse classifies FCP times:

|FCP time (seconds)|Color-coding|
|--|--|
|Over 3|<span className="text-2xl text-red-500">▲</span>  Poor|
|1.8-3|<span className="text-xl text-orange-500">■</span> Needs improvement|
|0-1.8|<span className="text-xl text-green-500">●</span> Good|

The FCP affects most of the other metrics and serves as a huge red flag if it is taking too long. This metric can be affected by:

- Long server response times.
- Render-blocking resources, such as CSS stylesheets, font files, and JavaScript scripts.
- Script-based elements above the fold.
- Large DOM trees.
- Multiple 301 redirects.

>ℹ️ For information on improving FCP, refer to [Google's guidelines](https://web.dev/fcp/#how-to-improve-fcp).

#### Speed Index (SI) | 10%

The [**Speed Index (SI)**](https://web.dev/speed-index/) indicates how quickly a page's elements become visible in the viewport. The Speed Index is a synthetic value that computes the visual differences between frames captured during the page load. Until all content is visible, each frame is scored considering its visual completeness. The individual scores are then summed up to give the page's Speed Index.

![Speed Index](https://vtexhelp.vtexassets.com/assets/docs/src/speedindex___7137f968e28cfbc2c0c1388a9c17e8bb.png)

Check how Lighthouse classifies SI times:

|SI time (seconds)|Color-coding|
|--|--|
|0ver 5.8|<span className="text-2xl text-red-500">▲</span>  Poor|
|3.4-5.8|<span className="text-xl text-orange-500">■</span> Needs improvement|
|0-3.4|<span className="text-xl text-green-500">●</span> Good|

The Speed Index is a unified metric that considers many other metrics and audits, which can help you figure out whether your page speed optimizations are working. Generally speaking, most improvements to your page's [First Contentful Paint](#first-contentful-paint-fcp--10) and [Largest Contentful Paint](#largest-contentful-paint-lcp--25) are also likely to improve the *Speed Index*.

>ℹ️ For information on improving SI, refer to [Google's guidelines](https://web.dev/speed-index/#how-to-improve-your-speed-index-score).

### Opportunities

The **Opportunities** section provides insights that could potentially help your page load faster. The priority level of each opportunity is denoted by the same color coding used for the metrics. High priorities are indicated by red triangles, medium priorities by orange squares, and low priorities by gray circles.

Use the **Opportunities** section to determine which improvements will benefit your page the most. The more significant the opportunity, the more likely it will affect your **Performance Score**.

Click each opportunity to get more detailed information and documentation on fixing the related issues. Also, notice that unless you have a specific reason for focusing on a particular metric, it is usually better to focus on improving your overall **Performance Score**.

### Diagnostics

The **Diagnostics** section provides more information about the performance of your application. It indicates the largest contentful paint element of your page, lists the longest tasks on the main thread and displays the cache lifetime, among other useful details.

Once again, the details presented in this section do not directly affect the **Performance Score** but are likely to improve the metric values if considered.

### Passed audits

The **Passed audits** section lists all the audits that the page passed. Once you implement Opportunities and Diagnostics suggestions, you can retest your page and check if they appear in the Passed Audits section.

### Additional information

The **Additional information** section shares the following details about the sampled data:

- Data collection period
- Visit durations
- Devices
- Network connections
- Sample size
- Chrome version

![Additional information](https://vtexhelp.vtexassets.com/assets/docs/src/additional-info___b0ba8b0e27f40a84f634c70976a16e16.png)
