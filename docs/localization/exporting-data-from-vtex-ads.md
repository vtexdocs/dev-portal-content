---
title: "Exporting data from VTEX Ads"
slug: "exporting-data-from-vtex-ads"
excerpt: "Learn how to export data from VTEX Ads using S3-compatible connections for events and aggregated data."
hidden: false
createdAt: "2025-10-13T00:00:00.000Z"
updatedAt: "2025-10-13T00:00:00.000Z"
---
VTEX Ads provides data export capabilities that allow you to extract campaign events and aggregated performance data. Integration always occurs using an S3-compatible connection that must be provided by the data receiver.

## Prerequisites

Before setting up data export, ensure you have:

- An S3-compatible storage solution configured.
- Proper access credentials for your chosen storage provider.
- Network connectivity between VTEX Ads and your storage endpoint.

## Credentials

Credentials must be securely shared with the VTEX team through agreed-upon secure channels. The integration supports the following cloud storage providers:

- **AWS S3**: Requires `Access Key ID` and `Access Key Secret`
- **Google Cloud Storage**: Requires `Service Account` credentials
- **Azure Blob Storage**: Requires connection string or account key

> ⚠️ **Security**: Never share credentials through unsecured channels. Use encrypted communication methods as agreed between parties.

## Export Types

VTEX Ads supports three types of data export:

- **[Event Export](https://developers.vtex.com/docs/guides/exporting-ads-events)**: Export raw event data including clicks, impressions, and conversions for detailed analysis and custom reporting.

- **[Aggregated Data Export](https://developers.vtex.com/docs/guides/exporting-aggregated-data-from-vtex-ads)**: Export pre-processed performance metrics and campaign statistics for business intelligence and reporting purposes.

- **[Ads Reports Export](https://developers.vtex.com/docs/guides/exporting-ads-reports)**: Export comprehensive advertising reports with campaign performance data, conversion metrics, and ROI analysis.
