# Bulk Import Spreadsheet

This guide will walk you through the process of filling out the bulk import spreadsheet for use with the [Bulk Import API](https://developers.vtex.com/docs/api-reference/buyer-organizations) to efficiently manage Buyer Organizations, Cost Centers, and Members through bulk import functionality.

## Step-by-step

1. Download the [template file](https://io.vtex.com.br/b2b-bulk-import/b2b-bulk-import-template.xlsx).
2. Fill in the file with buyer organization data following the specifications detailed in [File structure for import](#file-structure-for-import).

  >ℹ Ensure your file is in `.xlsx` format and does not exceed 50MB.

3. **Review and validate**: Double-check your data and ensure it aligns with this guidelines.

4. **Initiate Import**: Once your file is ready, upload it through the [upload file](https://developers.vtex.com/docs/api-reference/buyer-organizations#post-/api/b2b/import/buyer-orgs) and [start the import](https://developers.vtex.com/docs/api-reference/buyer-organizations#post-/api/b2b/import/buyer-orgs/-importId-) endpoint.

## File Structure for Import

Before diving into the import process, it's essential to understand the required file structure. Ensure your import file adheres to the guidelines outlined below.

### File Tabs

Your import file should consist of up to three tabs, each serving a specific purpose:

1. **Buyer Orgs Tab**: Contains detailed information about buyer organizations.
2. **Cost Centers Tab**: Dedicated to managing cost centers within organizations.
3. **Members Tab**: Stores information regarding members associated with organizations and cost centers.

### Buyer Orgs tab columns

Each new organization should have one cost center in the Buyer Orgs tab. Additional columns for each Custom Field configured for the merchant can be added at the end of the Buyer Orgs tab.

Fields marked with an asterisk `*` indicate required information.

| Column | Type | Description |
| - | - | - |
| Buyer Org ID* | String | A unique identifier for the buyer organization essential for tracking and future updates.       |
| Buyer Org Name* | String | The official name of the buyer organization. |
| Admin First Name* | String | The first name of the administrator overseeing the buyer organization. |
| Admin Last Name* | String | The last name of the administrator overseeing the buyer organization. |
| Admin Email* | String | The administrator's email address serves as the organization's primary point of contact. |
| Cost Center ID* | String | A unique identifier for the cost center essential for tracking and future updates. |
| Cost Center Name* | String | The name assigned to the cost center. |
| Address Type* | String | The classification of the address (e.g., residential, commercial). |
| Postal Code* | String | The postal code corresponding to the address. |
| Street* | String | The street name of the address. |
| Number* | String | The numerical identifier for the location (house/building number). |
| Complement* | String | Additional information regarding the address if any. |
| Neighborhood* | String | The specific neighborhood of the address. |
| City* | String | The city where the address is located. |
| State* | String | The state where the address is situated. |
| Country* | String | The country of the address. |
| Receiver Name* | String | The name of the individual who is the point of contact at the address. |
| Phone Number* | String | The contact number for the receiver. |
| Business Document*  | String | A document that contains essential business information (e.g., tax identification number). |
| Collections | String | Set the collection separated by comma allowed to the buyer organization. |
| Price Tables | String | Set the price tables separated by comma allowed to the buyer organization. |
| Payment Terms | String | Set the payment terms separated by comma allowed to the buyer organization. |
| Trade Policies | String | Set the trade policies separated by comma allowed to the buyer organization. |
| Sellers | String | Set the Sellers separated by comma allowed to the buyer organization. |

### Cost Centers tab

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
