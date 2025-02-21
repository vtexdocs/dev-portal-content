---
title: "My store is slow or unavailable"
slug: "my-store-is-slow-or-unavailable"
hidden: false
createdAt: "2023-05-11T10:17:18.615Z"
updatedAt: "2024-06-06T07:30:00.615Z"
excerpt: "If you are experiencing slow or non-functional operations in your store, there could be several underlying reasons."
tags:
    - faststore
    - store-framework
---

Keywords: performance | platform status | slow | unavailable | platform issues

If you are experiencing issues with your store, it is important to first determine whether the problem is that the store is unavailable or operating slowly. Identifying the specific issue will help you address it more effectively:

| Issue | Description | Solutions |
| ---- | ---- | ---- |
| **Store is unavailable** | The store stopped functioning or had a go-live failure.  | 1. [Checking VTEX Status page](#checking-vtex-status-page)<br>2. [Checking your connection](#checking-your-connection)<br>3. [Verifying DNS configuration](#if-the-store-is-unavailable-verifying-dns-configuration)<br>4. [Checking your storefront code and settings](#checking-your-storefront-code-and-settings) |
| **Store is slow** |  Shopping operations work, but slowly. It takes longer than expected to load or perform actions. | 1. [Checking VTEX Status page](#checking-vtex-status-page)<br>2. [Checking your connection](#checking-your-connection)<br> 3. [Reviewing customizations and integrations](#if-the-store-is-slow-reviewing-customizations-and-integrations)<br>4. [Checking your storefront code and settings](#checking-your-storefront-code-and-settings) |

Once you identify whether your store is unavailable or slow, follow the listed troubleshooting steps to solve the issue.

## Solutions

Below are various troubleshooting checks and instructions you can use to solve your store's issue.

### Checking VTEX Status page

Refer to the [VTEX status page](https://status.vtex.com) to check if the platform is undergoing some instability. If the status page indicates that the platform is functioning normally, move on to the next solutions.

>ℹ️ When you initially check the status page, there may be unreported instabilities, especially if it is a recent incident. Therefore, it is recommended that you periodically monitor the status page while following the troubleshooting steps provided.

### Checking your connection

Verify your internet connection by visiting other websites to ensure it is functioning properly. Alternatively, attempt to access your store using a different internet connection.

If the issues persist, refer to the recommendations below based on the issue you are experiencing.

### If the store is unavailable: Verifying DNS configuration

If your store had a go-live failure or was functioning normally and then stopped, see the topics below.

| Topic | Required action |
| :---- | :---- |
| **Account in production**  | Your account must be set to production. Otherwise, it will not be live. See this article for instructions on how to [put your account into production](https://help.vtex.com/tracks/go-live-your-store--4Ns5FxIiksmjsdX2yOTduM/7wFsbWgN4rnZsbjhv8IItX\#putting-your-account-into-production).  |
| **CDN domain registration**  | If you have registered your store's domain with the same CDN provider that VTEX uses (Cloudfront or Azion), it may cause issues with CDN provisioning and result in a go-live failure. To avoid this, please refer to the go-live guide for instructions on how to resolve any conflicts related to [CDN domain registration](https://help.vtex.com/tracks/go-live-your-store--4Ns5FxIiksmjsdX2yOTduM/7wFsbWgN4rnZsbjhv8IItX\#checking-domain-in-cdns). |
| **CNAME Type A pointing**  | Your DNS pointing must be of the type CNAME. There can not be any type A pointing coexisting with the CNAME, otherwise your go-live will most likely fail. Learn more about how to [set up DNS pointing to VTEX](https://help.vtex.com/tracks/go-live-your-store--4Ns5FxIiksmjsdX2yOTduM/12bQlMbJ68Ot0LIaO6Btkj\#setting-up-dns-pointing).  |
| **SSL certificate**  | If your store failed to go-live after you [notified DNS pointing](https://help.vtex.com/tracks/go-live-your-store--4Ns5FxIiksmjsdX2yOTduM/12bQlMbJ68Ot0LIaO6Btkj\#notifying-the-pointing), it may be that there was a failure to generate your SSL certificate. Refer to this guide to learn how to identify this issue and what to do in case of problems after [DNS pointing notification](https://help.vtex.com/tracks/go-live-your-store--4Ns5FxIiksmjsdX2yOTduM/12bQlMbJ68Ot0LIaO6Btkj\#notifying-the-pointing)  |
| **DNS provider settings**  | If you have not configured your DNS provider settings properly, VTEX may not be able to generate the SSL certificate, leading to store unavailability. See this guide on how to [Set up DNS pointing to VTEX](https://help.vtex.com/tracks/go-live-your-store--4Ns5FxIiksmjsdX2yOTduM/12bQlMbJ68Ot0LIaO6Btkj) and double check your DNS provider settings.  |
| **DNS propagation** | DNS propagation may take up to 48 hours after [DNS pointing](https://help.vtex.com/tracks/go-live-your-store--4Ns5FxIiksmjsdX2yOTduM/12bQlMbJ68Ot0LIaO6Btkj\#setting-up-dns-pointing). The length of this period depends on the Time To Live (TTL) you configured in your DNS provider. If you are within this timeframe, the store may not be accessible yet. Please be patient and allow sufficient time for DNS propagation to complete. |
| **DNS pointing deadline** | Once you register your domain in VTEX, you have up to seven days to set up DNS pointing. If you miss this deadline, you must [register your domain in VTEX](https://help.vtex.com/tracks/go-live-your-store--4Ns5FxIiksmjsdX2yOTduM/7sM5IMx02zaHvAFTm0OxiJ\#registering-the-domain-on-vtex) again. See the [go-live guide](https://help.vtex.com/tracks/go-live-your-store--4Ns5FxIiksmjsdX2yOTduM/1iP90RcJvlrfQhnlxM54wo) to learn details about this process. |
| **Cloudflare proxy**  | If [Cloudflare](https://www.cloudflare.com/) is your DNS provider, their native proxy can interfere with the SSL certificate, causing your store to go down. If this is your case, learn [how to disable the Cloudflare proxy](https://help.vtex.com/en/tutorial/disable-cloudflare-proxy--75QqsXAqR7NdkRc1GZPiXb).  |
| **Reverse proxy** | [Reverse proxy](https://help.vtex.com/en/tutorial/how-to-insert-a-reverse-proxy-in-front-of-vtex-services--4PFWsfRAKviNVPf1bYdiir) malfunction can cause store availability issues. When you use a reverse proxy, you give up the optimized edge service managed by VTEX and are responsible for the site's actual provisioning, which is tasked with the settings, monitoring and feature management such as header forwarding, cookies and cache management.<br><br>If this is your case, you can see this article on [How to insert a reverse proxy in front of VTEX services](https://help.vtex.com/en/tutorial/how-to-insert-a-reverse-proxy-in-front-of-vtex-services--4PFWsfRAKviNVPf1bYdiir) and follow up with your infrastructure team or provider to learn if this is the cause of your problem.<br><br>❗ **VTEX does not recommend using reverse proxies.** |

If the issue persists, you can find additional troubleshooting steps below for [Checking your storefront code and settings](\#checking-your-storefront-code-and-settings).

### If the store is slow: Reviewing customizations and integrations

The VTEX platform is designed to be multi-tenant and autoscalable, which means the platform can handle several merchants' needs simultaneously without impacting individual store performance.

To maintain the platform's overall health, VTEX may occasionally throttle unintentionally abusive requests. Therefore, if you notice slow performance, it is recommended to review your storefront code customizations and composable integrations.

 Ensure that these elements are not generating excessive requests to VTEX, as this can lead to throttling issues or bottlenecks for your store. By optimizing your requests and ensuring they are within acceptable limits, you can improve the overall performance of your store while ensuring compliance with VTEX's request throttling mechanisms.

If the issue persists, you can find additional troubleshooting steps below for [Checking your storefront code and settings](\#checking-your-storefront-code-and-settings).

### Checking your storefront code and settings

Depending on your selected storefront development solution, there are additional steps for troubleshooting a slow or unavailable store.

#### Store Framework

If your store uses [Store Framework](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-store-framework) and the topics above have not helped you, see the instructions below.

* **Edition App compatibility:**

  If your [go-live](https://developers.vtex.com/docs/guides/vtex-io-documentation-go-live) or [storefront migration](https://developers.vtex.com/docs/guides/vtex-io-documentation-migrating-storefront-from-legacy-to-io) has failed, it may be a good idea to check if you have the correct [account edition](https://developers.vtex.com/docs/guides/vtex-io-documentation-go-live\#account-edition).

* **Store Framework performance optimization:**
  
  If your store is slow, check this [performance optimization guide](https://developers.vtex.com/docs/guides/vtex-io-documentation-best-practices-for-optimizing-performance) and implement the recommended settings.

#### FastStore

If your store uses [FastStore](https://developers.vtex.com/docs/guides/faststore/docs-what-is-faststore) and the topics above have not helped you, see the instructions below.

* **Publishing failures**
  
  See this guide on [Debugging Releases and VTEX Headless CMS publishing errors](https://developers.vtex.com/docs/troubleshooting/my-pages-are-taking-too-long-to-be-published-on-headless-cms).
* **Lighthouse tests**

   [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) is an open-source tool that helps developers assess website performance. FastStore projects run automatic Lighthouse tests with every pull request. You need to consider the results of these automatic tests to identify and mitigate any performance issues before they impact your store in production.

  >ℹ️ Learn more about [using Lighthouse in your FastStore project](https://developers.vtex.com/docs/guides/faststore/1-onboarding-dashboard#lighthouse-scores).
* **Data fetching**

   Data fetching can negatively impact your storefront's performance if not done correctly on FastStore. See the [Best practices for fetching data on your storefront](https://developers.vtex.com/docs/guides/faststore/api-extensions-overview\#best-practices-for-fetching-data) and make sure they are implemented.

* **Third-party scripts**

   [Third-party scripts](https://developers.vtex.com/docs/guides/faststore/project-structure-handling-third-party-scripts) on FastStore may also cause your site to be slow. See this article to learn [how to handle the impact of third-party scripts](https://developers.vtex.com/docs/guides/faststore/project-structure-handling-third-party-scripts) on your FastStore project.
