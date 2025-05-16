---
title: "Pricing API - Overview"
slug: "pricing-api-overview"
hidden: true
createdAt: "2020-01-02T10:50:22.523Z"
updatedAt: "2025-05-16T17:29:59.041Z"
---
[block:callout]
{
  "type": "info",
  "body": "Check the new [Pricing onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/pricing-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Pricing and is organized by focusing on the developer's journey.",
  "title": "Onboarding guide"
}
[/block]
Pricing (v2) is the VTEX module responsible for the SKU's price list. At this module we have the base price of each SKU, some optional fixed prices by trade policy, and some rules that can be applied to generate dynamically different final prices according to the purchase context and the trade policy. The variables used in this collection are:

  * **{{accountName}}** = You VTEX account name.
  * **{{tradePolicyId}}** = Current Trade Policy ID.
  * **{{itemId}}** = SKU ID.
  * **{{X-VTEX-API-AppKey}}** and **{{X-VTEX-API-AppToken}}** = Credentials.

You can get more information about how to use this module and its business logic at [VTEX Help](http://help.vtex.com).

## Rate Limits

### Limits per route

- `GET`:  routes are not rate limited at the moment
- `PUT or POST`: `40 requests/second/account` in any **price insert/update route** with 1000 *Burst Credits*
- `DELETE`: `16 requests/second/account` in any **price deletion route**, with 300 *Burst Credits*.

### What are Burst Credits?

In case the account exceeds the limit frequency for a  `Rate Limiter` (for instance, when one account makes `41 requests/second` in any `price insert/update route`), we decrease from the *Burst Credit* count the exceeding (in this example, *1 Credit*).

In the event of the *Burst Credits* reaching **0 (zero)**, the request is blocked with a `Status 429` response.

The credits fill up over time when the route is not being used, in the same rate as the route's `Rate Limiter`. In our example, for each second not sending a **PUT or POST request**, we increase *40 Burst Credits* to this `Rate Limiter`

### New Response Headers

In the response headers of any request to Pricing v2 there are some new headers indicating the current status of the Rate Limiting.
This information may be useful to evaluate the ideal frequency to send requests to a route, and when to send a new request in the event of reaching a Rate Limit.

- `Ratelimit-Limit` - Total *Burst Credits* offered to a route
- `Ratelimit-Remaining` - How many *Burst Credits* are still available to use
- `Ratelimit-Reset` - How long (in seconds) it will take to the *Burst Credits* to fill up completely (It will fill up to the `Ratelimit-Limit`)
- `Retry-After` - Indicates how many seconds you will need to wait until the `Rate Limiter` accepts a new request to this route again. If this header response exists, this means your current request has been rate limited and has not been processed.

### How to integrate with Pricing v2 considering our Rate Limits

Integrate considering the limits of **requests/route/account** specified in the [*Limits per route*](#rate-limits) section, avoiding to surpass this frequency.

If you happen to be Rate Limited, wait the time in seconds specified in `Retry-After` before making another request to the service, and reduce the rate of requests per second that your integration is making.