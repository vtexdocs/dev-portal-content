---
title: "Keep your allowlist of VTEX IP addresses up to date"
slug: "2026-10-01-keep-your-allowlist-of-vtex-ip-addresses-up-to-date"
hidden: false
type: "info"
createdAt: "2026-10-01T12:00:00.000Z"
excerpt: "If you restrict access to your endpoints by IP address, periodically update your allowlist with the addresses published at ips.vtex.com to keep receiving requests from VTEX."
---

If your endpoints only accept requests from specific IP addresses, keeping your allowlist up to date is an ongoing task on your side. VTEX publishes the IP addresses it uses to send requests to your endpoints at [ips.vtex.com](http://ips.vtex.com), and that list is the reference your allowlist should follow.

## What needs to be done?

From time to time, compare the allowlist configured in your firewall, security group, or application with the addresses at [ips.vtex.com](http://ips.vtex.com), and add any address that is missing on your side.

We recommend making this review part of your regular maintenance routine, so that integrations where VTEX sends requests to endpoints you provide keep working as expected. Examples include:

- [Orders Hook](https://developers.vtex.com/docs/guides/orders-feed#hook), which notifies your endpoint about order updates.

If you don't restrict requests from VTEX by IP address, no action is needed.

## Learn more

- [VTEX IP addresses](http://ips.vtex.com)
- [Feed v3 and Hook](https://developers.vtex.com/docs/guides/orders-feed)
