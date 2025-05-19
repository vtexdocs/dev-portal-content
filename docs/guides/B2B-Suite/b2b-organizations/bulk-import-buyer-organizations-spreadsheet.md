---
title: "Bulk Import Buyer Organizations Spreadsheet"
slug: "bulk-import-buyer-organizations-spreadsheet"
hidden: false
createdAt: "2024-03-26t09:00:09.698z"
updatedAt: "2025-04-28t09:00:09.698z"
---

This guide will walk you through the process of filling out the bulk import spreadsheet for use with the [Bulk Import API](https://developers.vtex.com/docs/api-reference/buyer-organizations) to efficiently manage Buyer Organizations, Cost Centers, and Members through bulk import functionality.

## Before you begin

To use the bulk import of buyer organizations, you must first install and configure the [B2B Suite](https://developers.vtex.com/docs/apps/vtex.b2b-suite) which includes the [B2B Organizations](https://developers.vtex.com/docs/apps/vtex.b2b-organizations) app.

>⚠️ Bulk Import does not allow updating (editing) existing data in organizations or cost centers. This functionality is exclusively intended for creating and managing members.

## Step-by-step

1. Download the [template file](https://images.ctfassets.net/alneenqid6w5/PkYPXgHoDpok9ajVXQcM2/e5ff6b732ad776d2d04946855e109f15/b2b-bulk-import-template_v1.xlsx).
2. Fill in the file with buyer organizations data following the specifications detailed in [File structure for import](#file-structure-for-import).

  >ℹ Ensure your file is in `.xlsx` format and does not exceed 50MB.

3. Once your file is ready, upload it by making a request to the [Upload file](https://developers.vtex.com/docs/api-reference/buyer-organizations#post-/api/b2b/import/buyer-orgs) endpoint.
4. Validate file content by making a request to the [Validate file](https://developers.vtex.com/docs/api-reference/buyer-organizations#post-/api/b2b/import/buyer-orgs/validate/-importId-) endpoint.
5. Once the file is successfully validated, start the bulk data import by making a request to the [Start import](https://developers.vtex.com/docs/api-reference/buyer-organizations#post-/api/b2b/import/buyer-orgs/-importId-) endpoint.

## File structure for import

Before starting the upload and import process, it is essential to understand the required file structure. Ensure your import file adheres to the guidelines outlined below.

### File tabs

The import file should be structured with up to three tabs, each serving a distinct purpose:

1. [Buyer Orgs tab](#columns-in-the-buyer-orgs-tab): Contains detailed information about buyer organizations.
2. [Cost Centers tab](#columns-in-the-cost-centers-tab): Dedicated to managing cost centers within organizations.
3. [Members tab](#columns-in-the-members-tab): Stores information regarding members associated with organizations and cost centers.

### Columns in the Buyer Orgs tab

Each new organization should have one cost center in the Buyer Orgs tab. Additional columns for each custom field configured for the merchant can be added at the end of the Buyer Orgs tab.

Check the default columns present in this tab in the table below. Mandatory information is marked with `*`.

| Column | Type   | Description |
| - | - | - |
| Buyer Org ID* | String | Unique identifier for the buyer organization, for tracking and future updates. |
| Buyer Org Name* | String | Official name of the buyer organization. |
| Admin First Name* | String | First name of the administrator overseeing the buyer organization. |
| Admin Last Name* | String | Last name of the administrator overseeing the buyer organization. |
| Admin Email* | String | Administrator's email address serves as the organization's primary point of contact. |
| Cost Center ID* | String | Unique identifier for the cost center essential for tracking and future updates. |
| Cost Center Name* | String | Name assigned to the cost center. |
| Address Type* | String | Classification of the address (e.g., residential, commercial). |
| Postal Code* | String | Postal code corresponding to the address. |
| Street* | String | Street name of the address. |
| Number* | String | Numerical identifier for the location (house/building number). |
| Complement* | String | Additional information regarding the address if any. |
| Neighborhood* | String | Neighborhood of the address. |
| City* | String | City where the address is located. |
| State* | String | State where the address is situated. |
| Country* | String | Country of the address. |
| Receiver Name* | String | Name of the individual who is the point of contact at the address. |
| Phone Number* | String | Contact number for the receiver. |
| Business Document* | String | Document that contains essential business information (e.g., tax identification number). |
| Collections | String | Collections allowed to the buyer organization, separated by comma. |
| Price Tables | String | Price tables allowed to the buyer organization, separated by comma. |
| Payment Terms | String | Payment terms allowed to the buyer organization, separated by comma. |
| Trade Policies | String | Trade policies allowed to the buyer organization, separated by comma. |
| Sellers | String | Sellers allowed to the buyer organization, separated by comma. |

### Columns in the cost centers tab

This tab is required only for organizations with multiple cost centers. If the buyer organization has only one cost center, do not fill this tab.

Check the default columns present in the Cost Centers tab in the table below. Mandatory information is marked with `*`.

| Column | Type | Description |
| - | - | - |
| Buyer Org ID* | String | Unique identifier for the buyer organization essential for tracking and future updates. |
| Cost Center ID* | String | Unique identifier for the cost center essential for tracking and future updates. |
| Cost Center Name* | String | Name assigned to the cost center. |
| Address Type* | String | Classification of the address (e.g., residential, commercial). |
| Postal Code* | String | Postal code corresponding to the address. |
| Street* | String | Street name of the address. |
| Number* | String | Numerical identifier for the location (house/building number). |
| Complement* | String | Additional information regarding the address. |
| Neighborhood* | String | Neighborhood of the address. |
| City* | String | City where the address is located. |
| State* | String | State where the address is situated. |
| Country* | String | Country of the address. |
| Receiver Name* | String | Name of the individual who is the point of contact at the address. |
| Phone Number* | String | Contact number for the receiver. |
| Business Document*| String | Document that contains essential business information (e.g. tax identification number). |

### Columns in the Members tab

This tab is required only for organization with multiple members. If the buyer organization has only one member, do not fill this information.

Check the default columns present in the Cost Centers tab in the table below. Mandatory information is marked with `*`.

| Column | Type | Description |
| - | - | - |
| Buyer Org ID* | String | Unique identifier linking the member to a specific buyer organization. |
| Cost Center ID* | String  | Identifier linking the member to a specific cost center within the organization. |
| Name* | String  | Member's full name used for identification and communication. |
| Email* | String  | Email address of the member serving as a primary point of contact for communication. |
| Role Id* | GUID | Unique identifier denoting the member's role within the organization. |
| Can Impersonate | Boolean | Indicates if the member can impersonate another user within the system. |
