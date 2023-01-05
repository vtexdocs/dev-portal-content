---
title: "How to load test a store"
slug: "how-to-load-test-a-store"
hidden: false
createdAt: "2022-03-28T19:18:32.969Z"
updatedAt: "2022-03-28T19:18:59.970Z"
---
Load testing is the practice of determining whether a service is able to handle the expected capacity with the use of artificial load.

VTEX engineers load test the platform regularly to ensure it matches the expectations for heavy load. Therefore, you do not need to load test the VTEX platform on your own.

However, if you still feel the need to load test specific scenarios, we recommend you follow some principles in order to guarantee a safe test and meaningful results:
- [Simulate real user behavior](#simulate-real-user-behavior)
- [Ensure your test is not the bottleneck](#ensure-your-test-is-not-the-bottleneck)
- [Understand how to interpret results from the test](#understand-how-to-interpret-results-from-the-test)

These principles are especially relevant when your test includes services that integrate or interact with the VTEX platform, such as Google Tag Manager or Facebook Pixel. Below you can learn more about them, as well as [How VTEX protects the platform against traffic attacks](#how-vtex-protects-the-platform-against-traffic-attacks) and [Schedule a load test](#schedule-a-load-test).

## Simulate real user behavior

Simulating real user behavior is key to obtaining statistically meaningful results to your test. Below are some points to consider when building your load test scenario:

### Customers shop for different products.

In most cases, customers browse stores going through different searches and products. Make sure your test automation is not always picking the first product on the page, or always searching for the same term in the search bar.

Instead, try to model the probability of a user picking products based on real user metrics from your store. If you do not have such data, we recommend using uniformly random variations of requests to VTEX APIs and pages.

The main reason for this is that picking the same product over and over does not test the platform’s infrastructure. It mostly tests our caching layer.

### Customers shop from different regions.

Even if the load test is focused on a specific country, state, or region, customers will still shop from a range of IP addresses and locations.

Because of this, we recommend you use various source IP addresses on your test and that it spreads the load over various destination IP addresses.

Our edge services have protective measures from increased load from a single IP address or region, and they may be triggered if requests are way above the standard or even expected values. This may cause an outage in the load test, or worse, a localized outage of the store.

To make sure that you are using various destination IP addresses, use tools such as [WhatsMyDns](https://www.whatsmydns.net/#A/). This allows you to check the domain for different regions close to your testing site. Run it multiple times so that you get different IPs for the same region as well.

### Customers shop at different times.

Your customers’ activities naturally spread through intervals of time, even in the case of flash sales. A click on one client may happen seconds after one in another client. This difference is small for shopping behavior, but a big one when computing results in less than a second.

Make sure your load test is spreading requests randomly over time. Also make sure that your load test has ramp-up and ramp-down configurations. These numbers depend heavily on what you are testing. Flash sales may ramp up in around five minutes and ramp down almost as fast, while Black Week and Cyber Monday sales may have a ramp up and down spread out over hours.

Configuring a spread of requests will allow the VTEX platform to smoothly scale up the services according to the new demand for resources. 

To learn more about different behaviors you may encounter in case the increase of requests is too sudden, see [How VTEX protects the platform against traffic attacks](#how-vtex-protects-the-platform-against-traffic-attacks) below. 

## Ensure your test is not the bottleneck

In order to achieve the intended load, your testing infrastructure must be able to issue the rate and amount of requests that the VTEX platform will receive. Therefore, a big amount of requests requires a matching size infrastructure. See below the bottlenecks your test could face.

### Network bandwidth

Your test will issue many requests and receive many responses from VTEX. Make sure that your testing infrastructure has enough bandwidth to transmit all the necessary requests and responses.

If you are doing your test on the cloud, be careful when choosing which types of compute instances you will use, as network bandwidth is often overlooked.

### Compute capacity

Though making requests is mostly an I/O-bound operation, meaning that the bottleneck of a system would often be the bandwidth and latency of the network, you can also have systems that are not prepared to handle as many requests because of lack of CPU and RAM resources.

Remember to monitor the resource usage on your test to ensure your CPU and RAM are running below performance degradation levels. As a rule of thumb, keep CPU and RAM usage under 80%.

## Understand how to interpret results from the test

With the test simulating real user behavior, you should be able to look at the test results and understand the outcomes and necessary actions. A failed test may not mean that the platform will not handle the requested load, just as a successful test could still bring some points to consider.

### Understand the errors from the log.

The main way to understand what went wrong with a test is to look at the most common errors from test runs. You can query a search engine for error messages and see the most common reasons. But remember that they may not apply to your case.

### Check if the error comes from a third-party service.

Depending on how you programmed your test, you may be querying third-party resources, for images, ads, fonts, scripts, pixels, and more, in addition to VTEX’s.

Check if the requested URL matches a third-party source. If so, investigate with them on the cause of errors as well. Keep in mind that a third party can have more restrictive limits on resource usage than the VTEX platform.

## How VTEX protects the platform against traffic attacks

Load tests are not and should not be tagged as “special requests” in our platform, as that would further separate the tests from reality. Therefore, requests from load tests receive the same treatment as any other, which includes defensive measures due to increased load.

Because we’re a multi-tenant platform, we have measures that our systems take to prevent a surge of load in a single store from affecting the whole platform. Here are the most relevant measures:

### Rate Limiting

Our platform has limits of requests per IP, per Account, per API route, and per other components of a request. These limits vary throughout the day and are not disclosed by VTEX. However, you can know whether you reached the limit by analyzing the response of a given request.

A request that was rate-limited will get a response of `429 Too Many Requests` and contain a `Retry-After` header indicating when the client should try to issue another request. This is what is defined in [RFC6585](https://httpstatuses.com/429).

### Circuit Breaking

Some parts of our platform have circuit breakers. Meaning a feature that stops requests from reaching applications that are having trouble returning successful responses. 

If an application is returning too many errors in a short period of time, the circuit breaker is activated and requests stop flowing to that application in hopes that less requests will give it time to recover back to healthy behavior.
    
A request that was handled by a circuit breaker will return a `503 Service Unavailable` response status code.

## Schedule a load test

If you wish to load test your store, contact [VTEX support](https://help.vtex.com/en/support) to let us know when to expect increased requests from your store.
