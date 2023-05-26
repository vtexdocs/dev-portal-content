---
title: "My store is slow or unavailable"
slug: "my-store-is-slow-or-unavailable"
hidden: false
createdAt: "2023-05-11T10:17:18.615Z"
updatedAt: "2023-05-11T10:17:18.615Z"
---

If you are experiencing slow or non-functional operations in your store, there could be several underlying reasons.

You can always check the [VTEX status page](https://status.vtex.com) to learn if the platform is undergoing some instability. If the platform status is ok, try and go through the troubleshooting instructions below. Additionally, keep in mind that there could still be an unreported instability, so periodically checking the status page while following the troubleshooting steps can be helpful.

Below are various troubleshooting checks and instructions you can use to solve your store's issue:

- [Checking your connection](#checking-your-connection) - Make sure your internet connection is working properly.
- [Store is not working](#store-is-not-working) - Your store stopped functioning or had a go-live failure.
- [Store is slow](#store-is-slow) - Shopping operations work, but slowly.
- [Store Framework](#store-framework) - Additional checks and instructions for stores using [Store Framework](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-store-framework) as their storefront solution.
- [FastStore](#faststore) - Additional checks and instructions for stores using [FastStore](https://www.faststore.dev/) as their storefront solution.

## Checking your connection

Visit other websites to confirm whether your internet connection is working. Additionally, attempting to access your store using a different internet connection may also be helpful.

If you continue to encounter issues with your store, see the recommendations below depending on what is your issue.

## Store is not working

If your store had a go-live failure or was functioning normally and then stopped, see the topics below.

### Account in production

Your account must be set to production. Otherwise, your store will not be live. See this article for instructions on how to [put your account into production](https://help.vtex.com/tracks/go-live-your-store--4Ns5FxIiksmjsdX2yOTduM/7wFsbWgN4rnZsbjhv8IItX#putting-your-account-into-production).

### DNS propagation

DNS propagation may take up to 48 hours after [DNS pointing](https://help.vtex.com/tracks/go-live-your-store--4Ns5FxIiksmjsdX2yOTduM/12bQlMbJ68Ot0LIaO6Btkj#setting-up-dns-pointing). If you are within this timeframe, the store may not be accessible yet. Please be patient and allow sufficient time for DNS propagation to complete.

### Conflict in CDN domain registration

If you've registered your store's domain with the same CDN provider that BLERG uses, it may cause issues with CDN provisioning and result in a go-live failure. To avoid this, please refer to the go-live guide for instructions on how to resolve any conflicts related to [CDN domain registration](https://help.vtex.com/tracks/go-live-your-store--4Ns5FxIiksmjsdX2yOTduM/7wFsbWgN4rnZsbjhv8IItX#checking-domain-in-cdns).

### Type A pointing

Your DNS pointing must be of the type CNAME. There can not be any type A pointing coexisting with the CNAME, otherwise your go-live will most likely fail.

Learn more about how to [set up DNS pointing to VTEX](https://help.vtex.com/tracks/go-live-your-store--4Ns5FxIiksmjsdX2yOTduM/12bQlMbJ68Ot0LIaO6Btkj#setting-up-dns-pointing).

### Failure to generate SSL certificate

If your store failed to go-live after you [notified DNS pointing](https://help.vtex.com/tracks/go-live-your-store--4Ns5FxIiksmjsdX2yOTduM/12bQlMbJ68Ot0LIaO6Btkj#notifying-the-pointing), it may be that there was a failure to generate your SSL certificate. Refer to this guide to learn how to identify this issue and what to do in case of problems after [DNS pointing notification](https://help.vtex.com/tracks/go-live-your-store--4Ns5FxIiksmjsdX2yOTduM/12bQlMbJ68Ot0LIaO6Btkj#notifying-the-pointing)

### DNS provider settings

It may be a good idea to double check your DNS provider settings.

For example, if cloudflare is your DNS provider, their native proxy can interfere with SSL certificate, causing your store to go down. If this is your case, learn [how to disable the Cloudflare proxy](https://help.vtex.com/en/tutorial/disable-cloudflare-proxy--75QqsXAqR7NdkRc1GZPiXb).

### Reverse proxy

[Reverse proxy](https://help.vtex.com/en/tutorial/how-to-insert-a-reverse-proxy-in-front-of-vtex-services--4PFWsfRAKviNVPf1bYdiir) malfunction can cause store availability issues.

When you use a reverse proxy, you give up the optimized edge service managed by VTEX and are responsible for the site's actual provisioning, which is tasked with the settings, monitoring and feature management such as header forwarding, cookies and cache management. If this is your case, follow up with your infrastructure team or provider to learn if this is the cause of your problem. VTEX does not recommend using reverse proxies.

### Double check go-live procedures and timeline

A store's [go-live](https://help.vtex.com/tracks/go-live-your-store--4Ns5FxIiksmjsdX2yOTduM/1iP90RcJvlrfQhnlxM54wo) is a delicate series of processes, some being time sensitive. For example, once you register your domain in VTEX, you have up to seven days to set up DNS pointing.

See the [go-live guide](https://help.vtex.com/tracks/go-live-your-store--4Ns5FxIiksmjsdX2yOTduM/1iP90RcJvlrfQhnlxM54wo) to check whether there is anything you missed and how to fix it.

## Store is slow

The VTEX platform is designed to be multi-tenant and autoscalable, which means that it can handle the needs of several merchants simultaneously without impacting individual store performance. However, to ensure the health of your store, VTEX may occasionally throttle unintentionally abusive requests to the platform.

If your store is experiencing slow performance, it is likely due to storefront code customizations or composable integrations. We recommend checking these elements to ensure they are not sending excessive requests to VTEX, which can cause a throttle issue or bottleneck for your store.

If the issue persists, you can find further instructions below if you use [Store Framework](#store-framework) or [FastStore](#faststore) as your storefront solution.

## Store Framework

If your store uses [Store Framework](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-store-framework) and the topics above have not helped you, see the instructions below.

### Edition App compatibility

If your [go-live](https://developers.vtex.com/docs/guides/vtex-io-documentation-go-live) or [storefront migration](https://developers.vtex.com/docs/guides/vtex-io-documentation-migrating-storefront-from-legacy-to-io) has failed, it may be a good idea to check if you have the correct [account edition](https://developers.vtex.com/docs/guides/vtex-io-documentation-go-live#account-edition).

### Store Framework performance optimization

If your store is slow, check this [performance optimization guide](https://developers.vtex.com/docs/guides/vtex-io-documentation-best-practices-for-optimizing-performance) and implement the recommended settings.

## FastStore

If your store uses [FastStore](https://faststore.dev) and the topics above have not helped you, see the instructions below.

### Publishing failures

See this guide on [Debugging Releases and VTEX Headless CMS publishing errors](https://www.faststore.dev/how-to-guides/troubleshooting/debugging-releases-publishing).

### Lighthouse tests

[Lighthouse](https://www.faststore.dev/how-to-guides/performance/lighthouse) is an open source tool that helps developers assess website performance. Note that if you use [WebOps](https://www.faststore.dev/glossary#vtex-io-webops) in your FastStore project, it runs automatic Lighthouse tests with every pull request. It is very important that you mind these automatic tests' results so as to identify and mitigate any performance issues before they impact your store in production.

>ℹ️ Learn more about [using Lighthouse in your FastStore project](https://www.faststore.dev/how-to-guides/performance/lighthouse#how-to-run-lighthouse-audits).

### Best practices for fetching data with FastStore

Data fetching can have a negative impact on the performance of your storefront if not done correctly. See the [Best practices for fetching data on your storefront](https://www.faststore.dev/how-to-guides/faststore-api/fetching-api-data#best-practices-for-fetching-data) and make sure they are implemented.

### Third party scripts on FastStore

[Third party scripts](https://www.faststore.dev/how-to-guides/performance/handling-the-impact-of-third-party-scripts) may also cause your site to be slow, see this article to learn [how to handle the impact of third-party scripts](https://www.faststore.dev/how-to-guides/performance/handling-the-impact-of-third-party-scripts) on your FastStore project.
