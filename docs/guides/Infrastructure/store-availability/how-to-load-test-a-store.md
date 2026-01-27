---
title: "How to load test a store"
slug: "how-to-load-test-a-store"
hidden: false
createdAt: "2022-03-28T19:18:32.969Z"
updatedAt: "2022-03-28T19:18:59.970Z"
excerpt: "Learn best practices for load testing your VTEX store, including how to simulate real user behavior and interpret test results effectively."
---
Load testing is the practice of determining whether a service can handle expected capacity using artificial load.

VTEX engineers regularly load test the platform to ensure it meets expectations for heavy traffic. Therefore, you do not need to load test the VTEX platform on your own.

However, if you need to load test specific scenarios, follow these principles to ensure safe testing and meaningful results:

- [Simulate real user behavior](#simulate-real-user-behavior)
- [Ensure your test is not the bottleneck](#ensure-your-test-is-not-the-bottleneck)
- [Understand how to interpret results from the test](#understand-how-to-interpret-results-from-the-test)

These principles are especially relevant when your test includes services that integrate or interact with the VTEX platform, such as Google Tag Manager or Facebook Pixel. Learn more about them below, including [How VTEX protects the platform against traffic attacks](#how-vtex-protects-the-platform-against-traffic-attacks) and [Notify VTEX about an upcoming load test](#notify-vtex-about-an-upcoming-load-test).

## Simulate real user behavior

Simulating real user behavior is essential for obtaining statistically meaningful results. Consider the following points when building your load test scenario:

### Customers shop for different products

In most cases, customers browse stores through different searches and products. Ensure your test automation doesn't always select the first product on the page or always search for the same term.

Instead, model the probability of users selecting products based on real user metrics from your store. If you don't have such data, we recommend using uniformly random variations of requests to VTEX APIs and pages.

The main reason for this is that selecting the same product repeatedly doesn't test the platform's infrastructure—it primarily tests the caching layer.

### Customers shop with different emails

When conducting load tests, ensure you test using a variety of customer emails. Each customer in your store has a unique email address, so it's important to simulate purchases from multiple customers as in real-world scenarios.

This realistic simulation contributes to more accurate load testing results, providing insights into how the platform performs under different user circumstances.

We recommend incorporating a randomized selection of email addresses when configuring your load test scenarios.

### Customers shop from different regions

Even if the load test focuses on a specific country, state, or region, customers will still shop from a range of IP addresses and locations.

Because of this, we recommend using various source IP addresses in your test and spreading the load over multiple destination IP addresses.

Our edge services have protective measures against increased load from a single IP address or region, which may be triggered if requests are significantly above standard or expected values. This may cause an outage in the load test, or worse, a localized outage of the store.

To ensure you're using various destination IP addresses, use tools such as [WhatsMyDns](https://www.whatsmydns.net/#A/). This allows you to check the domain for different regions close to your testing site. Run it multiple times to get different IPs for the same region as well.

### Customers shop at different times

Your customers' activities naturally spread through intervals of time, even during flash sales. A click from one customer may happen seconds after another customer's click. This difference is small for shopping behavior but significant when computing results in less than a second.

Ensure your load test spreads requests randomly over time and includes ramp-up and ramp-down configurations. These numbers depend heavily on what you're testing. Flash sales may ramp up in around five minutes and ramp down almost as fast, while Black Week and Cyber Monday sales may have ramp-up and ramp-down periods spread over hours.

Configuring a spread of requests allows the VTEX platform to smoothly scale up services according to new demand for resources.

To learn more about different behaviors you may encounter if the increase in requests is too sudden, see [How VTEX protects the platform against traffic attacks](#how-vtex-protects-the-platform-against-traffic-attacks) below.

## Ensure your test is not the bottleneck

To achieve the intended load, your testing infrastructure must be able to issue the rate and volume of requests that the VTEX platform will receive. Therefore, a large volume of requests requires matching infrastructure capacity. See below the bottlenecks your test could face.

### Network bandwidth

Your test will issue many requests and receive many responses from VTEX. Ensure your testing infrastructure has enough bandwidth to transmit all necessary requests and responses.

If you're conducting your test on the cloud, be careful when choosing compute instance types, as network bandwidth is often overlooked.

### Compute capacity

Though making requests is mostly an I/O-bound operation (meaning the bottleneck is often network bandwidth and latency), you can also have systems that aren't prepared to handle many requests due to lack of CPU and RAM resources.

Monitor resource usage in your test to ensure CPU and RAM are running below performance degradation levels. As a rule of thumb, keep CPU and RAM usage under 80%.

## Understand how to interpret results from the test

With the test simulating real user behavior, you should be able to interpret the test results and understand the outcomes and necessary actions. A failed test may not mean the platform can't handle the requested load, just as a successful test could still reveal points to consider.

### Understand the errors from the log

The primary way to understand what went wrong with a test is to examine the most common errors from test runs. You can query a search engine for error messages to see common reasons. However, remember they may not apply to your specific case.

### Check if the error comes from a third-party service

Depending on how you programmed your test, you may be querying third-party resources for images, ads, fonts, scripts, pixels, and more, in addition to VTEX resources.

Check if the requested URL matches a third-party source. If so, investigate the cause of errors with them as well. Keep in mind that third parties can have more restrictive limits on resource usage than the VTEX platform.

## How VTEX protects the platform against traffic attacks

Load tests should not be tagged as "special requests" in our platform, as that would separate the tests from reality. Therefore, requests from load tests receive the same treatment as any other requests, which includes defensive measures against increased load.

Because we're a [multi-tenant platform](https://developers.vtex.com/docs/guides/cloud-infrastructure), we have measures to prevent a surge of load in a single store from affecting the entire platform. Here are the most relevant measures:

### Rate Limiting

Our platform has limits on requests per IP, per account, per API route, and per other components of a request. These limits vary throughout the day and are not disclosed by VTEX. However, you can determine whether you reached the limit by analyzing the response of a given request.

A request that was rate-limited will receive a `429 Too Many Requests` response and contain a `Retry-After` header indicating when the client should try to issue another request. This is defined in [RFC6585](https://httpstatuses.com/429).

### Circuit Breaking

Some parts of our platform have circuit breakers—a feature that stops requests from reaching applications that are having trouble returning successful responses.

If an application returns too many errors in a short period of time, the circuit breaker is activated and requests stop flowing to that application, giving it time to recover to healthy behavior.

A request handled by a circuit breaker will return a `503 Service Unavailable` response status code.

## Notify VTEX about an upcoming load test

If you plan to run a load test on your store, contact [VTEX support](https://help.vtex.com/en/support) to notify VTEX of the test window and expected traffic volume.

This communication is for awareness purposes only, so our teams know that an intentional traffic increase is expected. VTEX does not plan, execute, or provide support for customer load tests, and the responsibility for designing and running the test remains entirely with the customer.
