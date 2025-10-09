---
slug: 'vtex-tracking-api-changes-in-all-paths'
title: 'VTEX Tracking API: changes in all paths'
createdAt: 2020-11-10T12:00:00.000Z
hidden: true
type: 'improved'
excerpt: "We have unified our VTEX Tracking APIs into a single version, so it's no longer necessary to specify the version on the URL. We have also translated all paths to english."
tags:
    - VTEX Tracking
---

![Commerce APIs](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-tracking-api-changes-in-all-paths-0.png)

We have unified our VTEX Tracking APIs into a single version, so it's no longer necessary to specify the version on the URL. We have also translated all paths to english.

Previously, users could access `VTEX Tracking v1` and `VTEX Tracking v1.1` endpoints. The only difference between the two versions, was that `v1.1` retrieved a `pictures` object in delivery service responses. We have now unified both versions, and translated paths to english.

No endpoints were deleted, and no attributes were changed. Check out the updated documentation for the [unified VTEX Tracking APIs](https://developers.vtex.com/docs/api-reference/tracking#overview).

> ⚠️ The previous paths were not deprecated, and are still being maintained by the VTEX Tracking team. If your business' integration was built with the previous `v1` and `v1.1` endpoints, it will still run smoothly. No changes in your integrations should be done during the Black Friday period. We will communicate any updates, and deprecations of endpoints in the future.

| Previous path - v1                              | Previous Path - v1.1                              | Current Path                                     |
| ----------------------------------------------- | ------------------------------------------------- | ------------------------------------------------ |
| post `/receiver/v1/auth`                        | post `/receiver/v1.1/auth`                          | post **/receiver/auth**                          |
| get put post `/receiver/v1/servicos`              | get put post `/receiver/v1.1/servicos`              | get put post **/receiver/services**              |
| get `/receiver/v1/servicos/{{idDeliveryService}}` | get `/receiver/v1.1/servicos/{{idDeliveryService}}` | get **/receiver/services/{{idDeliveryService}}** |
| get `/receiver/v1/servicos/nf`                    | get `/receiver/v1.1/servicos/nf`                    | get **/receiver/services/invoice**               |
| get post `/receiver/v1/servicos/roteirizado`      | get post `/receiver/v1.1/servicos/roteirizado`      | get post **/receiver/services/routes**           |
| get post `/receiver/v1/servicos/roteirizacao`     | get post `/receiver/v1.1/servicos/roteirizacao`     | get post **/receiver/services/routes**           |
