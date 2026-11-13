---
title: "VTEX IO Observability: Querying and visualizing app logs and metrics (Beta)"
slug: "2026-12-08-vtex-io-observability-beta"
hidden: false
type: "added"
createdAt: "2026-12-08T00:00:00.000Z"
excerpt: "VTEX IO Observability is now available in beta, giving you access to production logs and metrics from your VTEX IO apps through the VTEX IO Observability API and the Grafana plugin."
tags:
  - VTEX IO
seeAlso:
  - "/docs/guides/vtex-io-observability-overview"
  - "/docs/guides/vtex-io-observability-api-guide"
  - "/docs/guides/vtex-io-observability-plugin"
  - "/docs/api-reference/observability-api"
---

[**VTEX IO Observability**](https://developers.vtex.com/docs/guides/vtex-io-observability-overview) is now available in beta, giving you access to production logs and metrics from your [VTEX IO apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-a-vtex-app) to monitor app health, investigate errors, and analyze performance. You can query this data programmatically with the [**VTEX IO Observability API**](https://developers.vtex.com/docs/api-reference/observability-api)** or visualize it in [**Grafana**](https://grafana.com/) with the [**VTEX IO Observability plugin for Grafana**](https://developers.vtex.com/docs/guides/vtex-io-observability-plugin).

> ⚠️ **VTEX IO Observability** is currently in beta, which means that VTEX is working to improve it. If you have any questions, contact [VTEX Support](https://help.vtex.com/en/support).

## What has changed

**VTEX IO Observability** introduces the following capabilities for apps running in production:

- **Account-isolated logs and metrics:** Access application logs written with the `@vtex/api` `logger` (filterable by log level, workspace, trace IDs, and message patterns) and HTTP request metrics pre-aggregated to one-minute intervals (`gauge`, `sum`, and `histogram`). Logs and metrics are isolated per VTEX account and retained for three days by default.
- **VTEX IO Observability API:** Query logs and metrics in the **Grafana** data frame format with filters, metric aggregations, ordering, and pagination, and discover observed apps, queryable fields, metric names, and API capabilities.
- **VTEX IO Observability plugin for Grafana:** Connect **Grafana** directly to the API as a data source to explore logs and visualize predefined request rate, error rate, and latency percentile metrics in dashboards and **Explore** without writing API requests. Because the plugin is in beta, it is not listed in the **Grafana** plugin catalog and must be installed manually or with **Docker** from the [plugin GitHub releases page](https://github.com/vtex/vtexio-grafana-plugin/releases).

## What needs to be done

To adopt **VTEX IO Observability**, make sure your app has your VTEX account as its vendor, uses version `7.x` of the [`node` builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-node-builder) with the standard `logger` from `@vtex/api`, and is deployed and installed in a production workspace. Authenticate API requests in the [VTEX IO Observability API guide](https://developers.vtex.com/docs/guides/vtex-io-observability-api-guide) or configure the data source in the [**VTEX IO Observability plugin for Grafana**](https://developers.vtex.com/docs/guides/vtex-io-observability-plugin) guide using a VTEX [API key and token](https://help.vtex.com/en/docs/tutorials/generated-keys) associated with a role that includes the `colossus-read-logs` permission.
