---
title: "How to configure tradeName to use in the organization search field"
slug: "how-to-configure-tradename-to-use-in-the-organization-search-field"
hidden: false
createdAt: "2024-10-07t09:00:09.698z"
updatedAt: "2024-10-07t09:00:09.698z"
---

The `tradeName` field is used to identify buyer and supplier companies on the platform. When configured as `Filterable`, the field allows users to filter data and search for companies based on their trade name. The `tradeName` is displayed as one of the identification attributes on the **Organizations** page in the VTEX Admin, enabling its use in record search and filtering.

To configure the `tradeName` field, follow the steps below:

1. In VTEX Admin, go to **Store Settings** > **Storefront** > **Master Data**.

![Master Data](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/B2B-Suite/settings/masterdata1.png)

2. After logging in, click **Advanced settings** as shown in the image below.

![Advanced Settings](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/B2B-Suite/settings/masterdata2.png)

3. In the Settings column, click on Data structure.

![Data Structure](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/B2B-Suite/settings/masterdata3.png)

4. Click **Data Entities**, find the CL row, and click the **Edit** button as shown in the image below.

![Data Entities](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/B2B-Suite/settings/masterdata4a.png)

![Edit Customer](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/B2B-Suite/settings/masterdata4b.png)

5. Find the **tradeName** field and click `Is filterable`.

![Filterable](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/B2B-Suite/settings/masterdata5.png)

6. Click **Save**.

![Save](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/B2B-Suite/settings/masterdata6.png)

7. Click the **Publish** button to apply the changes

![Publish](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/B2B-Suite/settings/masterdata7.png)