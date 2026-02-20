---
title: "B2B Organizations (B2B Suite)"
slug: "vtex-b2b-organizations"
excerpt: "Learn how to group B2B users into organizations, assign payment methods, price tables, and product collections, and manage cost centers and users."
hidden: false
createdAt: "2021-10-26T13:12:33.521Z"
updatedAt: "2022-12-08T18:41:35.402Z"
---

> ⚠️ This documentation applies to B2B Suite only.

> ℹ️️ The **B2B Organizations** app is part of the VTEX [B2B Suite](https://developers.vtex.com/docs/guides/vtex-b2b-suite) solution: a collection of apps that allow stores to manage organizations, storefront roles and permissions, and checkout settings for B2B commerce relationships. We recommend using it alongside the other apps in this suite to ensure that all features work as expected.

In the B2B model, sales goals go beyond achieving a high conversion rate. They include simplifying the relationship between companies, reducing costs, and increasing performance by delivering the best possible shopping experience to customers.

B2B commerce relations are usually complex and often require a customized service. In this scenario, it is common to group various users from the same company under an organization and define custom payment methods, product selections, and prices for each customer. These tasks are part of the daily routine in B2B commerce.

The **B2B Organizations** app enables you to group B2B users into organizations. You can assign specific payment methods, price tables, and product collections to each organization, allowing all organization users to share the same commercial conditions. Additionally, each organization can be further segmented into one or more cost centers, each with its own shipping addresses.

## Before you begin

First, make sure you have the [VTEX IO CLI (Command Line Interface)](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-install) installed in your computer.

Please note that when you install the B2B Organizations app, the [Storefront Permissions](https://developers.vtex.com/docs/guides/vtex-storefront-permissions) will also be installed as a dependency app. This is because Storefront Permissions allows you to assign specific storefront roles to B2B users within an organization. This is particularly useful for organizations with multiple users who have different responsibilities, such as placing orders, approving orders, or managing organization users. Read the [Storefront Permissions](https://developers.vtex.com/docs/guides/vtex-storefront-permissions) app documentation to learn more about the available roles and how to customize their permissions.

If you want to manage roles and permissions in the VTEX Admin, you must install [Storefront Permissions UI](https://developers.vtex.com/docs/guides/vtex-storefront-permissions-ui) as well.

## Installation

You can install the **B2B Organizations** app by running the command `vtex install vtex.b2b-organizations` in your terminal, using [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference).

## User widget configuration

To enable the [user widget](#user-widget) in your storefront, this app provides a `b2b-user-widget` block that you can add to the account store theme. We recommend adding it to the store header, as shown below.

<img src="https://user-images.githubusercontent.com/77292838/159766647-a8d22a55-61da-4169-a1be-1072a4ca8d73.png"></img>

Follow the instructions below to display the user widget.

1. Open your store theme app repository in your local files.
2. In the `manifest.json` file, under `dependencies`, add `"vtex.b2b-organizations": "1.x"`:

   ```json
   "dependencies": {
       "vtex.b2b-organizations": "1.x"
     },
   ```

3. Within your store's theme `store` > `blocks` > `header` folder, edit the `header.jsonc` file, placing the `b2b-user-widget` block in the desired location, as exemplified below.

   We recommend placing it on the top row of the store header. Note that the `b2b-user-widget` block does not accept any props.

   ```json
   "header-layout.desktop": {
       "children": [
         "flex-layout.row#0-desktop",
         "flex-layout.row#1-desktop",
         "flex-layout.row#2-desktop",
         "flex-layout.row#3-desktop",
         "sticky-layout#4-desktop"
       ]
     },

     "flex-layout.row#0-desktop": {
       "children": ["b2b-user-widget"],
       "props": {
         "fullWidth": true
       }
     },
   ```

4. Publish and install the modified store theme. Read our documentation on [Making your theme content public](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-theme-content-public) for more information.

## Configuration

This is the store header for only one associated organization: <img src="https://i.imgur.com/5yXFU6y.png"></img>

This is the store header for more than one associated organization:

<img src="https://i.imgur.com/ScQtfIz.png"></img>

### `b2b-user-widget`

| Prop name      | Type      | Description                                                                                                             | Default value |
| -------------- | --------- | ----------------------------------------------------------------------------------------------------------------------- | ------------- |
| `showDropdown` | `boolean` | Controls whether the dropdown menu is displayed when multiple organizations are associated with the same email address. | `true`        |

## Customization

To apply CSS customizations to this and other apps, follow the instructions in [Using CSS handles for store customization](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization).

CSS handles are available for the **Organization Request Form** component and the **User Widget** component.

| **CSS handles**                   |
| --------------------------------- |
| `newOrganizationContainer`        |
| `newOrganizationInput`            |
| `newOrganizationAddressForm`      |
| `newOrganizationButtonsContainer` |
| `newOrganizationButtonSubmit`     |
| `userWidgetContainer`             |
| `userWidgetRow`                   |
| `userWidgetItem`                  |
| `userWidgetButton`                |
| `userWidgetImpersonationItem`     |
| `userWidgetImpersonationButton`   |
| `userWidgetImpersonationError`    |

## How the app works

The **B2B Organizations** app adds the following functionalities and components to your VTEX store, which are divided into three categories: VTEX Admin, Master Data v2, and Storefront features.

<table class="styles_table__k65Hc">
<thead>
  <tr>
    <th>Public</th>
    <th>Category</th>
    <th>Location</th>
    <th>Feature</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="8">B2B store admin</td>
    <td rowspan="8"><a href="https://developers.vtex.com/docs/guides/vtex-b2b-organizations#vtex-admin">VTEX Admin</a></td>
    <td>Organization Requests page</td>
    <td>Reviews organization requests.</td>
  </tr>
  <tr>
    <td>Organizations page</td>
    <td>Manages organizations.<br></td>
  </tr>
  <tr>
    <td rowspan="5">Organization Details page</td>
    <td>Manages cost centers associated with organizations.</td>
  </tr>
  <tr>
    <td>Manages collections associated with organizations.</td>
  </tr>
  <tr>
    <td>Manages payment terms associated with organizations.</td>
  </tr>
  <tr>
    <td>Manages price tables associated with organizations.</td>
  </tr>
  <tr>
    <td>Manages organization users.</td>
  </tr>
  <tr>
    <td>Message Center Templates page</td>
    <td>Manages email templates for the B2B Organizations app.</td>
  </tr>
  <tr>
    <td>B2B store admin or developers</td>
    <td><a href="https://developers.vtex.com/docs/guides/vtex-b2b-organizations#master-data-v2">Master Data v2</a></td>
    <td>Master Data API v2</td>
    <td>Retrieves and edits information related to organization requests, organizations, and cost centers stored in Master Data v2.</td>
  </tr>
  <tr>
    <td rowspan="6">B2B customer (organization user) with required permissions</td>
    <td rowspan="6"><a href="https://developers.vtex.com/docs/guides/vtex-b2b-organizations#storefront">Storefront</a></td>
    <td>Storefront form</td>
    <td>Requests a new organization.</td>
  </tr>
  <tr>
    <td rowspan="4">My Organization</td>
    <td>Manages organizations.</td>
  </tr>
  <tr>
    <td>Manages cost centers</td>
  </tr>
  <tr>
    <td>Manages users.</td>
  </tr>
  <tr>
    <td>Impersonates users.</td>
  </tr>
  <tr>
    <td>Storefront navigation</td>
    <td>User widget</td>
  </tr>
</tbody>
</table>

> ℹ️ This app can also be used together with [B2B Quotes](https://developers.vtex.com/docs/guides/vtex-orderquote), allowing order quotes to be managed at the organization level. Please read our B2B Quotes documentation for more details.

### VTEX Admin

After installing and configuring the **B2B Organizations** app, you can find its VTEX Admin capabilities accessing **Account Settings > B2B Organizations & Cost Centers**.

#### Organization Requests

To request the creation of an organization, B2B customers must complete the [Request New Organization form](#request-new-organization).

Once the customer completes this step, B2B store admins can review the organization request by navigating to **VTEX Admin** > **Account Settings** > **B2B Organizations & Cost Centers** > **Organization Requests** (or by accessing `/admin/b2b-organizations/requests`).

On this page, admins can view a list of all the organization requests placed in their store.

<img src="https://user-images.githubusercontent.com/77292838/159766650-d989a5bc-a33b-4fee-9e60-76f26567b067.png" alt="02-organization-requests"></img>

Each organization within the system can be assigned one of the following statuses: **pending**, **approved** or **declined**. Pending requests are the ones awaiting review.

To review a request, follow these steps:

1. Click a request from the table or click <img src="https://user-images.githubusercontent.com/77292838/159766633-dfcb818f-6bd7-4cd0-92dc-9c682fb50d04.png" width="10" alt-text="00-ellipsis" /> > `View`.
2. Leave a comment in the **Add note** field, if necessary.
3. Click `Approve` or `Decline`.

<img src="https://user-images.githubusercontent.com/77292838/159766653-ba4f6d4b-4bda-4856-86a3-0080f8d22e1e.png" alt="03-manage-organization-request"></img>

Upon approval, the request status will change to **Approved**, and the organization will be created. Notifications will be sent via email to both the [Organization Admin and the Sales Admins](https://developers.vtex.com/docs/guides/vtex-storefront-permissions#available-storefront-roles) to inform them of the approval. You can learn more about this notification in the [Email templates](#email-templates) section. In addition, the user designated as the Organization Admin will be granted access to the [My Organization](#my-organization) tab on the **My Account** page of your storefront.

If the organization request is declined, the request status will be changed to **Declined**, and the organization will not be created. The user assigned as the Organization Admin will receive an email notification informing this outcome. For further information about this notification, please refer to the [Email templates](#email-templates) section.

#### Organizations

The **Organizations** page displays a list of all the organizations created in your store and their respective statuses. It also allows store admins to:

- [Add organizations](#add-organization).
- Access the [Organization details](#organization-details) page, which includes organization data, cost centers, collections, payment terms, price tables, and users.

To access the page, go to **Account Settings** > **B2B Organizations & Cost Centers** > **Organizations** in the VTEX Admin (or access `/admin/b2b-organizations/organizations`).

<img src="https://user-images.githubusercontent.com/77292838/159766661-63f7191a-51c4-49d7-a34d-d909456f2692.png" alt="04-organizations"></img>

You can click `Refetch` to refresh the organization list on this page and retrieve information about recently created organizations.

To find a specific organization, you can use the search bar to search by name or apply filters based on the organization status.

Each organization can have one of the following statuses:

- **Active**: The organization has been approved by the store admins and is currently active.
- **On hold**: The organization is currently paused, which means its users are temporarily unable to complete purchases.
- **Inactive**: The organization has been deactivated by the store admins, so users will not be able to log in.

##### Adding organization

To manually create a new organization on the **Organizations** page, please follow these steps:

1. Click the `New` button.
2. Fill in the required information about the new organization, as illustrated in the image below.
   - **Name of organization:** Name of the organization you want to create.
   - **Name of cost center:** Name of the initial cost center associated with the organization.
   - **Country:** Country where the cost center is located.
   - **Postal code:** Postal code of the cost center address.
   - **Address Line 1:** Main address information, including the street number and street name where the cost center is located.
   - **Address Line 2:** Optional field for additional address information.
   - **City:** City where the cost center is located. This field will be completed automatically based on the postal code informed.
   - **State:** State where the cost center is located. This field will be completed automatically based on the postal code informed.
   - **Receiver:** Name of the person who will receive the orders at the specified address.
3. Click `Add`.

<img src="https://user-images.githubusercontent.com/77292838/159766663-e1b2005a-0c2d-4bec-84ad-612007f17d64.gif" alt="05-add-organization"></img>

> ℹ️ After creating the organization, you can add additional cost centers and addresses. The process for doing so is explained in the next section of this documentation.

#### Organization Details

On the **Organizations Details** page, you can view and edit the following information of an existing organization:

- [Organization name and status](#organization-name-and-status)
- [Cost centers](#cost-centers)
- [Collections](#collections)
- [Payment terms](#payment-terms)
- [Price tables](#price-tables)
- [Users](#users)

You can access this page by going to **Account Settings** > **B2B Organizations & Cost Centers** > **Organizations** in the VTEX Admin and clicking the organization whose details you want to view, or <img src="https://user-images.githubusercontent.com/77292838/159766633-dfcb818f-6bd7-4cd0-92dc-9c682fb50d04.png" width="10" alt-text="00-ellipsis" /> > `View`.

> ℹ️ Note that assigning collections, payment terms, and price tables to an organization is optional. If these are not assigned, users belonging to the organization will see the store default catalog, have access to all payment methods, and view the store default pricing.

##### Organization name and status

In the top section of the page, you will find the following information:

- **Organization Name:** Name of the organization. You can edit this information.
- **Status:** Status of the organization. You can set it to **Active**, **On Hold** or **Inactive** by selecting from a list.
- **Created:** Date when the organization was created.

<img src="https://user-images.githubusercontent.com/77292838/159766675-bd899388-7537-427d-af37-fc048aaf8636.png" alt="06-organization-name-status"></img>

##### Cost Centers

In the **Cost Centers** section, you can view all cost centers associated with the organization. VTEX Admin users can view and manage cost centers for any organization.

<img src="https://user-images.githubusercontent.com/77292838/159766678-0fd6c361-e1e6-470b-a9fc-c98b530c05e9.png" alt="07-cost-centers"></img>

> ℹ️ Each organization must have at least one cost center.

By default, each cost center allows the [payment terms](#payment-terms) that have been assigned to the parent organization. However, **Organization Admin** users can enable or disable individual payment terms at the cost center level. For more information on managing cost centers, please refer to the [Managing Cost Centers](#manage-cost-centers) section.

To create a new cost center, follow the steps below.

1. Click the `New` button.
2. Enter the required information about the new cost center, as illustrated in the image below.
   - **Name:** Name of the cost center.
   - **Country:** Country where the cost center is located.
   - **Postal code:** Postal code of the cost center address.
   - **Address Line 1:** Main address information, including the street number and street name where the cost center is located.
   - **Address Line 2:** Optional field for additional address information.
   - **City:** City where the cost center is located. This field will be completed automatically based on the postal code informed.
   - **State:** State where the cost center is located. This field will be completed automatically based on the postal code informed.
   - **Receiver:** Name of the person who will receive the orders at the specified address.
3. Click `Add`.

<img src="https://user-images.githubusercontent.com/77292838/159766680-5eb39381-a7da-4278-b8da-8cc7efe3e90a.gif" alt="08-add-cost-center"></img>

##### Cost Center Details

You can view or edit the details of an existing cost center by clicking on it on the **Organization Details** page.

This will lead you to the **Cost Center Details** page, where you can:

- View or edit the cost center **Name** and **Addresses**.
- View or edit the cost center **Business Document**.
- Add a new shipping address associated with the cost center.
- Delete the cost center.

<img src="https://user-images.githubusercontent.com/77292838/159766691-4557a032-a38c-4abb-a5a1-29019b833ad2.png" alt="09-cost-center-details"></img>

The **Business Document field** is optional and can be utilized to store business identifiers such as Tax ID, VAT ID, CNPJ, or similar identification numbers. If a Business Document is specified in a user's cost center, it will be automatically applied as the `corporateDocument` in the user's profile. Additionally, this business document will be attached to any orders placed by the user.

> ⚠️ Please note that the shipping addresses assigned to a cost center will only be accessible to users belonging to that specific cost center during the checkout process if you have installed [B2B Checkout Settings](https://developers.vtex.com/docs/guides/vtex-b2b-checkout-settings). Other addresses will not be available. Therefore, each cost center must have at least one shipping address.

To edit or delete an existing address, click <img src="https://user-images.githubusercontent.com/77292838/159766633-dfcb818f-6bd7-4cd0-92dc-9c682fb50d04.png" width="10" alt-text="00-ellipsis" /> next to it and select **Edit** or **Delete**.

To add a new shipping address for a cost center, follow these instructions:

1. Click `Add new address`.
2. Enter the required information for the new address.
   - **Country:** Country where the cost center is located.
   - **Postal code:** Postal code of the cost center's address.
   - **Address Line 1:** Main address information, including the street number and street name where the cost center is located.
   - **Address Line 2:** Optional field for additional address information.
   - **City:** City where the cost center is located. This field will be completed automatically based on the postal code informed.
   - **State:** State where the cost center is located. This field will be completed automatically based on the postal code informed.
   - **Receiver:** Name of the person who will receive the orders at the specified address.
3. Click `Add`.

Make sure to click `Save` in the top right of the **Cost Center Details** page to save any changes made.

If you want to delete the cost center, click `Delete` instead.

##### Collections

> ℹ️ You must use the **Collections Beta** solution to be able to associate collections with organizations using **B2B Organizations**. Read our article on [Creating Collections Beta](https://help.vtex.com/tutorial/creating-collections-beta--yJBHqNMViOAnnnq4fyOye) for more information.

This section allows you to manage the [product collections](https://help.vtex.com/tutorial/creating-collections-beta--yJBHqNMViOAnnnq4fyOye) assigned to the organization, which determines the assortment of products visible to organization users in the storefront.

To add a collection, select the collection you want to add from the **Available** list and click `Add to org`.

To remove a collection, select the collection you want to remove from the **Assigned to organization** list and click `Remove from org`.

<img src="https://user-images.githubusercontent.com/77292838/159766692-aec018f6-d09b-4290-a180-a0e2b7040295.gif" alt="10-collections"></img>

##### Payment Terms

In this section, you can choose which [payment conditions](https://help.vtex.com/en/tutorial/how-to-configure-payment-conditions--tutorials_455?&utm_source=autocomplete) are assigned to the organization, which determines which payment options are available to organization users during checkout.

Note that the available payment options can be further customized per cost center by the **Organization Admin**. See the [Managing Cost Centers](#manage-cost-centers) section for more information.

To add a payment term, select the option you want to add from the **Available** list and click `Add to org`.

To remove a payment term, select the option you want to remove from the **Assigned to organization** list and click `Remove from org`.

<img src="https://user-images.githubusercontent.com/77292838/159766697-27de2f5b-18b3-4067-a4f1-81da8fb61bc0.gif" alt="11-payment-terms"></img>

> ℹ️ To customize the checkout according to each organization user role, you need to install and configure [B2B Checkout Settings](https://developers.vtex.com/docs/guides/vtex-b2b-checkout-settings).

##### Price Tables

This section allows you to choose which [price tables](https://help.vtex.com/en/tutorial/creating-price-tables--58YmY2Iwggyw4WeSCGg24S) are assigned to the organization. The prices displayed to organization users in the storefront are determined by the selected price tables.

To add a price table, select the option you want to add from the **Available** list and click `Add to org`.

To remove a price table, select the option you want to remove from the **Assigned to organization** list and click `Remove from org`.

<img src="https://user-images.githubusercontent.com/77292838/159766700-34ebfaaf-f6fa-42b6-85a9-a83dca5505ef.gif" alt="12-price-tables"></img>

##### Users

This section displays a list of users associated with the organization, showing their **Email**, **Role** in the organization, and the **Cost Center** they are associated with.

<img src="https://user-images.githubusercontent.com/77292838/159766707-572dd167-e948-4300-b259-1c9cd0b8a341.png" alt="13-users-list"></img>

To add a new user to the organization, follow these steps:

1. In the **Users** list, click the `New` button.
2. Enter the user information, as illustrated below.
   - **Name:** Full name of the user.
   - **Email:** Email address of the user.
   - **Cost Center:** Cost center the user will be associated with.
   - **Role:** Role the user will have in the storefront. See more details on the available roles in the [Storefront Permissions documentation](https://developers.vtex.com/docs/guides/vtex-storefront-permissions#available-storefront-roles).
3. Click `Add`.

<img src="https://user-images.githubusercontent.com/77292838/159766710-4e35973c-880d-4e98-8f93-4a6c87d3f4e8.png" alt="14-add-new-user"></img>

Once you add a new user to the organization, a customer account will be created if an account does not already exist in your store for the provided email address.

To edit or remove an existing user, follow these steps:

1. Click the user you want to edit or delete in the **Users** list.
2. Edit the desired information.

   You can change the user's **Cost Center** and their **Role**.

   If you want to remove the user from the organization, click `Remove user` and skip the next step.

3. To apply your changes, click `Save`.

<img src="https://user-images.githubusercontent.com/77292838/159766713-03778c4a-370a-4c13-be4a-8f507cee0a73.png" alt="15-edit-user"></img>

If a user is removed from an organization, their account will continue to exist in the store, but they will no longer be associated with an organization, cost center, or B2B role. Thus, they will lose access to the details of their organization on the **My Organization** page.  Instead, they will have the option to [request the creation of a new organization](#request-new-organization), if necessary.
> ℹ️ As an optional feature, you can install the [Admin Customers](https://github.com/vtex/admin-customers) app for additional customer management capabilities on the VTEX Admin.

#### Email templates

The **B2B Organizations** app provides a set of four email templates to be sent to B2B organization users, which are triggered automatically based on specific changes:

| **Template name**               | **Recipient**                          | **Trigger**                                 |
| ------------------------------- | -------------------------------------- | ------------------------------------------- |
| **Organization Approved**       | Users with the Organization Admin role | The organization request has been approved. |
| **Organization Created**        | Users with a Sales Admin role          | The organization has been created.          |
| **Organization Declined**       | Users with the Organization Admin role | The organization request has been declined. |
| **Organization Status Changed** | Users with the Organization Admin role | The organization status has changed.        |

If you want to view or edit these templates, follow the steps below.

1. In the VTEX Admin, go to **Customer > Message center > Templates**.
2. Type `organization` in the search bar.
3. Click the template you want to view or edit.
4. Make the desired changes in the template. For detailed instructions on editing **Message Center** templates, refer to our documentation on [How to Create and Edit Transactional Email Templates.](https://help.vtex.com/en/tracks/transactional-emails--6IkJwttMw5T84mlY9RifRP/335JZKUYgvYlGOJgvJYxRO)
5. Click `Save`.

<img src="https://user-images.githubusercontent.com/77292838/159766714-6b5feaaf-3d81-472e-a713-55d952a1e556.gif" alt="16-templates"></img>

### Master Data v2

The **B2B Organizations** app stores information about organization requests, organizations, and cost centers in [Master Data v2](https://help.vtex.com/pt/tutorial/master-data-v2--3JJ1mlzuo88w22gO0gy0QS).

This means that store admins or developers can retrieve this information via the [Master Data API v2](https://developers.vtex.com/docs/api-reference/master-data-api-v2#overview) by using their **data entity name** as the value for the `data_entity_name` parameter.

You can see the data entity names in the table below.

| **Data entity names**   |
| ----------------------- |
| `organization_requests` |
| `organizations`         |
| `cost_centers`          |

### Storefront

Storefront capabilities, in turn, are accessible to B2B customers who visit a supplier store, provided that they are logged in and have the required permissions.

The following sections describe what your customer can do in your storefront after you have finished setting up the B2B Organizations app.

#### Requesting a new organization

If a B2B user is not currently associated with any organization, they have the option to request the creation of a new buyer organization in your store by completing the **Request New Organization** form. They can follow the steps below to do so.

1. Access the store website.
2. Click **My Account** > **My Organization**.
3. Provide the required information, as shown in the image below.
   - **Organization Name:** Name of the organization.
   - **User to become Organization Admin:** Section where you must provide information about the first user of the organization, who will be assigned as the Organization Admin.
     - **First Name:** First name of the Organization Admin user.
     - **Last Name:** Last name of the Organization Admin user.
     - **Email Address:** Email address of the Organization Admin user.
   - **Default Cost Center:** Section where you must provide information about the first cost center associated with the organization.
     - **Cost Center Name:** Name of the cost center.
     - **Business Document:** Optional field for a business document such as a Tax ID, Company registration number, etc.
     - **Country:** Country where the cost center is located.
     - **Postal code:** Postal code of the cost center's address.
     - **Address Line 1:** Main address information, including the street number and street name where the cost center is located.
     - **Address Line 2:** Optional field for additional address information.
     - **City:** City where the cost center is located. This field will be completed automatically based on the postal code informed.
     - **State:** State where the cost center is located. This field will be completed automatically based on the postal code informed.
     - **Receiver:** Name of the person who will receive the orders at the specified address.
4. Click `Submit`.

<img src="https://user-images.githubusercontent.com/77292838/159766733-14da23e9-55d6-44e8-8cfc-95d62e3b4ade.gif" alt="17-organization-request"></img>

After submitting the form, the request will be sent to a queue for review by the B2B store administrator. See the [Organization Requests](#organization-requests) section for more information.

The user designated as the **Organization Admin** for the new organization will receive an email notification when the request has been approved or declined by the store admin. Learn more about this notification in the [Email templates](#email-templates) section.

#### My Organization

Users designated as the **Organization Admin** or **Sales Admin** can manage their organization's details in the storefront on the **My Organization** page.

Users with the **Organization Buyer** or **Organization Approver** roles can also view a read-only version of this page.

To access **My Organization**, follow the instructions below.

1. Access the storefront and log in.
2. Click `Hello, {name}`.
3. Click **My Account**.
4. Go to **My Organization** on the sidebar. You will see the page below.

<img src="https://user-images.githubusercontent.com/77292838/159766773-4d62c3ed-4282-45a9-bf36-d0041684cc50.png" alt="18-my-organization"></img>

On this page, the user with the **Organization Admin** or **Sales Admin** roles can do the following:

- [Manage Cost Centers](#manage-cost-centers)
- [Manage Users](#manage-users)

##### Managing cost centers

Storefront users who have the **Organization Admin** or **Sales Admin** role can navigate to the Cost Centers section on the My Organization page to view the cost centers associated with their organization.

To add a new cost center, they should go to **My Account > My Organization**, where they will have access to the same options as described in the [Cost Centers](#cost-centers) section. They can view or edit the details of an existing cost center by clicking on it, similar to the process described in the [Cost Center Details](#cost-center-details) section.

**Organization Admins** can also view and/or edit the **Business Document** associated with each cost center, as described in [Cost Center Details](#cost-center-details).

In addition, **Organization Admins** can enable specific payment terms for a cost center by using the switch button to activate or deactivate the payment terms assigned to the organization, as shown below.
> ⚠️ This section will only be available on the **My Organization** page if [payment terms](#payment-terms) have been previously assigned to the organization by the VTEX Admin users.

<img src="https://user-images.githubusercontent.com/77292838/159766775-dd0a17bd-8418-401b-a377-7d4c9ed0cf11.png" alt="19-payment-terms-cost-center"></img>

##### Managing users

**Organization Admin** or **Sales Admin** storefront users can also view and manage the users of their organization in the **Users** section of the **My Organization**. To access this section, they can go to **My Account > My Organization**, where they will have access to the same options described in the [Users](#users) section of this documentation.

Users with the **Organization Admin** role can add, edit, or remove users with any of the following roles: **Organization Admin**, **Organization Approver**, and **Organization Buyer**.

Users with the **Sales Admin** role may add, edit, or remove users with any of the following roles: **Sales Admin**, **Sales Manager**, and **Sales Representative**.

###### Impersonating users

In telesales, assisted sales, or customer support scenarios where the B2B customer needs help from a salesperson to navigate the store or place orders, it is common to use impersonation.

In the **B2B Organizations** app, users with a profile with at least one of the permissions **impersonate-users-all**, **impersonate-users-organization**, or **impersonate-users-costcenter** will be able to impersonate another user. These permissions are available in the [Storefront Permissions](https://developers.vtex.com/docs/apps/vtex.storefront-permissions) and can be added to the user's profile using the [Storefront Permissions UI](https://developers.vtex.com/docs/guides/vtex-storefront-permissions-ui).

When impersonation is activated, it temporarily applies the email, organization, and cost center of the impersonated user to the storefront session. This allows impersonating users to do the following:

- Browse the store and view prices, products, shipping addresses, and payment methods as the impersonated user would see them.
- Take actions on behalf of the impersonated user, such as placing orders.
- Use the regular permissions of the impersonated user.

To use impersonation, users with **Sales** roles or the **Organization Admin** role must follow the steps below.

1. In the **Users** section of [My Organization](#my-organization), click <img src="https://user-images.githubusercontent.com/77292838/159766633-dfcb818f-6bd7-4cd0-92dc-9c682fb50d04.png" width="10" alt-text="00-ellipsis" /> in the row of the user they want to impersonate.
2. Click **Impersonate User**.

<img src="https://user-images.githubusercontent.com/77292838/159766777-1ff83458-cad0-46de-82e4-1e3c3e4bb144.png" alt="20-users"></img>

> ⚠️ It is not possible to impersonate emails with Sales roles.

#### User widget

To give storefront users visibility into their currently assigned organization, cost center, and role, this app provides a user widget that can be added to the account store theme:

<img src="https://user-images.githubusercontent.com/77292838/159766781-8edabb7e-292c-4c8e-a88e-ae937ec7db86.png" alt="21-user-widget"></img>

> ℹ️ To display the user widget, you must follow the instructions in the [User widget configuration](#user-widget-configuration) section.

If users click `Manage organization`, they can access the **My Organization** page directly.

In case impersonation is currently active, this block will also show the email of the user being impersonated, as well as the `Stop impersonation` button:

<img src="https://user-images.githubusercontent.com/77292838/159766784-6bce63af-9cc6-4ac4-bc59-460b74722dbe.png" alt="22-user-widget-impersonation"></img>
