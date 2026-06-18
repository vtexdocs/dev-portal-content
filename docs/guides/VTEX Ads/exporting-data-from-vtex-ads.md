---
title: "Exporting data from VTEX Ads"
slug: "exporting-data-from-vtex-ads"
excerpt: "Learn how to export data from VTEX Ads using S3-compatible connections for events and aggregated data."
hidden: false
createdAt: "2026-06-18T00:00:00.000Z"
updatedAt: "2026-06-18T00:00:00.000Z"
---
You can export campaign events and aggregated performance data from **VTEX Ads** using an S3-compatible connection. Provide the connection details for your storage endpoint before setting up the integration. This guide covers shared prerequisites and credentials. For setup steps, choose the export type that matches your use case in [Export types](#export-types).

## Before you begin

Make sure you have the following before setting up data export:

- You configured an S3-compatible storage solution.
- You have valid credentials for your storage provider.
- Your storage endpoint has network connectivity to VTEX Ads.

## Credentials

Share credentials with the VTEX team only through agreed secure channels. Data export supports the following cloud storage providers:

- **AWS S3**: Requires an `access key ID` and a `secret access key`.
- **Google Cloud Storage**: Requires `service account` credentials.
- **Azure Blob Storage**: Requires a `connection string` or an `account key`.

> ⚠️ Never share credentials through unsecured channels. Use encrypted communication methods as agreed between parties.

## Export types

VTEX Ads supports three types of data export:

- **[Event Export](https://developers.vtex.com/docs/guides/exporting-ads-events)**: Export raw event data including clicks, impressions, and conversions for detailed analysis and custom reporting.
- **[Aggregated Data Export](https://developers.vtex.com/docs/guides/exporting-aggregated-data-from-vtex-ads)**: Export pre-processed performance metrics and campaign statistics for business intelligence and reporting purposes.
- **[Ads Reports Export](https://developers.vtex.com/docs/guides/exporting-ads-reports)**: Export comprehensive advertising reports with campaign performance data, conversion metrics, and return on investment (ROI) analysis.
