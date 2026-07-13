---
title: "VBase deprecation for VTEX IO apps: Migration to Master Data"
slug: "2026-07-31-vbase-deprecation"
hidden: false
type: "deprecated"
createdAt: "2026-07-31T12:00:00.000Z"
excerpt: "VBase will be gradually deprecated for VTEX IO apps. Master Data becomes the platform's single database solution."
---

VBase will be gradually deprecated for VTEX IO apps, consolidating [Master Data](https://developers.vtex.com/docs/guides/master-data-introduction) as the single database solution offered by the VTEX platform. Apps that currently use VBase must migrate to Master Data before the shutdown dates below.

## What has changed?

VBase, the database service available to VTEX IO apps, will no longer be available for app development and running apps. The VBase deprecation will happen in the following phases:

| Date | Phase |
| :- | :- |
| September 1st, 2026 | [Publishing](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app) and [linking](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) new apps that use VBase are blocked. |
| March 1st, 2027 | Publishing and linking new [major versions](https://developers.vtex.com/docs/guides/vtex-io-documentation-releasing-a-new-app-version#understanding-app-versioning) of existing apps that use VBase are blocked. |
| September 1st, 2027 | VBase shutdown. Requests from apps to VBase will no longer work. |

## Why did we make this change?

Consolidating our database infrastructure on Master Data provides stores with a more reliable, scalable, and resilient foundation. This unified solution minimizes operational complexity and ensures a consistent, high-performance development experience across the VTEX platform.

## What needs to be done?

If you develop or maintain apps that use VBase, migrate them to Master Data before the dates above to avoid service disruptions. For implementation details, see the [Master Data CRUD guide](https://developers.vtex.com/docs/guides/create-master-data-crud-app).

### New apps

Use Master Data as the storage solution from the start. Starting September 1st, 2026, new apps using VBase will be blocked.

### Existing apps

Replace VBase usage with Master Data and publish the updated version before March 1st, 2027, as publishing new major versions of apps that use VBase will be blocked. Publishing new minor and patch versions will still be allowed after March 1st, 2027.

For exceptional cases requiring extended VBase support, [open a ticket](https://help.vtex.com/docs/tutorials/opening-tickets-to-vtex-support) with [VTEX support](https://support.vtex.com/hc/en-us) to discuss your specific needs.

### New integrations

Do not use VBase in new projects or integrations. Use Master Data instead. The following integration guides and template repositories currently reference VBase and will be updated to use Master Data:

| Integration | Template repository |
| :- | :- |
| [Payment provider](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework) | [payment-provider-example](https://github.com/vtex-apps/payment-provider-example) |
| [Anti-fraud provider](https://developers.vtex.com/docs/guides/how-the-integration-protocol-between-vtex-and-antifraud-companies-works) | [antifraud-provider-example](https://github.com/vtex-apps/antifraud-provider-example) |
| [External marketplace](https://developers.vtex.com/docs/guides/external-marketplace-integration-app-template) | [mkp-app-template](https://github.com/vtex/mkp-app-template) |
| [Search resolver](https://developers.vtex.com/docs/guides/external-search-provider-recipe) | [search-resolver](https://github.com/vtex-apps/search-resolver) |

For more information about modeling and storing data with Master Data, see [Master Data introduction](https://developers.vtex.com/docs/guides/master-data-introduction).
