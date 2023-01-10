---
title: "B2B Organizations"
slug: "vtex-b2b-organizations"
excerpt: "vtex.b2b-organizations@1.17.0"
hidden: false
createdAt: "2021-10-26T13:12:33.521Z"
updatedAt: "2022-12-08T18:41:35.402Z"
---

>ℹ️ The **B2B Organizations** app is part of VTEX's [B2B Suite](https://developers.vtex.com/docs/guides/vtex-b2b-suite) solution: a collection of apps that allow stores to manage organizations, storefront roles and permissions, and checkout settings for B2B commerce relationships. We recommend that you use it alongside the other apps in this suite for all functionalities to work as expected.

In the B2B model, sales goals go beyond a high order conversion rate. They include simplifying the relationship between companies, reducing costs, and increasing performance by providing the customer with the best possible shopping experience.

B2B commerce relations are usually complex and often require a customized service. Therefore, grouping different users from the same company under an organization, and defining custom payment methods, product selections, and prices for each customer are common tasks in this scenario.

The **B2B Organizations** app enables you to group B2B users into organizations. You can assign specific payment methods, price tables, and product collections to each organization, allowing all of the organization's users to share the same commercial conditions. Each organization is further segmented into one or more cost centers, with its own shipping addresses.

## Before you start

First, make sure you have the [VTEX IO CLI (Command Line Interface)](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-install) installed in your machine.

Note that installing B2B Organizations will also result in [Storefront Permissions](https://developers.vtex.com/docs/guides/vtex-storefront-permissions) being installed as a dependency app, because it allows you to grant specific storefront roles for B2B users in an organization. This is especially useful for organizations with multiple users who have different responsibilities, such as placing orders, approving orders or managing the organization users. See the [Storefront Permissions](https://developers.vtex.com/docs/guides/vtex-storefront-permissions) app documentation for information on the available roles and how to customize their permissions.

If you want to be able to manage roles and permissions on the VTEX Admin, you must install [Storefront Permissions UI](https://developers.vtex.com/docs/guides/vtex-storefront-permissions-ui) as well.

## Installation

You can install the **B2B Organizations** app by running `vtex install vtex.b2b-organizations` in your terminal, using the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference).

## User widget configuration

To enable the [user widget](#user-widget) in your storefront, this app provides a `b2b-user-widget` block that you can add to the account's store theme. We recommend that you add it to the store header, as shown below.

![01-user-widget-header](https://user-images.githubusercontent.com/77292838/159766647-a8d22a55-61da-4169-a1be-1072a4ca8d73.png)

Follow the instructions below to display the user widget.

1. Open your store theme app's repository in your local files.
2. In the `manifest.json` file, under `dependencies`, add `"vtex.b2b-organizations": "1.x"`, like so:

   ```json
   "dependencies": {
       "vtex.b2b-organizations": "1.x"
     },
   ```

3. Within your store theme's `store` > `blocks` > `header` folder, edit the `header.jsonc` file, placing the `b2b-user-widget` block in the desired location, as exemplified below.

   We recommend placing it on the top row of the store header. The `b2b-user-widget` block accepts no props.

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

4. Publish and install the modified store theme. You can follow our documentation on [Making your theme content public](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-making-your-theme-content-public) to do so.

## Configuration

If we have only one associated organization:
![](https://i.imgur.com/5yXFU6y.png)

If we have more than one associated organization:
![](https://i.imgur.com/ScQtfIz.png)

### `b2b-user-widget`
| Prop name                  | Type                              | Description                                                                                                             | Default value |
| -------------------------- | --------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------- |
| `showDropdown`               | `Boolean`                          | controls whether we are viewing the dropdown if we have more than one organization associated with the same email.                  | `true`          |

## Customization

In order to apply CSS customizations in this and other apps, follow the instructions on [Using CSS Handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization).

CSS handles are available for the **Organization Request Form** component and the **User Widget** component.

| **CSS Handles**                   |
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

The **B2B Organizations** app adds the following functionalities and components to your VTEX store, divided into VTEX Admin, Master Data v2, and Storefront capabilities:

<table class="styles_table__k65Hc">
<thead>
  <tr>
    <th>Public</th>
    <th>Availability</th>
    <th>Location</th>
    <th>Feature</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="8">B2B store administrator</td>
    <td rowspan="8"><a href="https://developers.vtex.com/docs/guides/vtex-b2b-organizations#vtex-admin">VTEX Admin</a></td>
    <td>Organization Requests page</td>
    <td>Review Organization Requests</td>
  </tr>
  <tr>
    <td>Organizations page</td>
    <td>Manage Organizations<br></td>
  </tr>
  <tr>
    <td rowspan="5">Organization Details page</td>
    <td>Manage Cost Centers associated with organizations</td>
  </tr>
  <tr>
    <td>Manage Collections associated with organizations</td>
  </tr>
  <tr>
    <td>Manage Payment Terms associated with organizations</td>
  </tr>
  <tr>
    <td>Manage Price Tables associated with organizations</td>
  </tr>
  <tr>
    <td>Manage organization Users</td>
  </tr>
  <tr>
    <td>Message Center Templates page</td>
    <td>Manage email templates related to the B2B Organizations app</td>
  </tr>
  <tr>
    <td>B2B store administrator or developers</td>
    <td><a href="https://developers.vtex.com/docs/guides/vtex-b2b-organizations#master-data-v2">Master Data v2</a></td>
    <td>Master Data API v2</td>
    <td>Retrieve and edit information on organization requests, organizations, and cost centers stored in Master Data v2</td>
  </tr>
  <tr>
    <td rowspan="6">B2B customer (organization user) with required permissions</td>
    <td rowspan="6"><a href="https://developers.vtex.com/docs/guides/vtex-b2b-organizations#storefront">Storefront</a></td>
    <td>Storefront form</td>
    <td>Request New Organization</td>
  </tr>
  <tr>
    <td rowspan="4">My Organization</td>
    <td>Manage Organization</td>
  </tr>
  <tr>
    <td>Manage Cost Centers</td>
  </tr>
  <tr>
    <td>Manage Users</td>
  </tr>
  <tr>
    <td>Impersonate Users</td>
  </tr>
  <tr>
    <td>Storefront navigation</td>
    <td>User Widget</td>
  </tr>
</tbody>
</table>

>ℹ This app can also be used together with [B2B Quotes](https://developers.vtex.com/vtex-developer-docs/docs/vtex-orderquote), allowing order quotes to be managed at the organization level. Please read our B2B Quotes documentation for more details.

### VTEX Admin

After installing and setting up the **B2B Organizations** app, its VTEX Admin capabilities can be found by accessing **Account Settings > B2B Organizations & Cost Centers**.

#### Organization Requests

To request the creation of an organization, B2B customers must fill in the [Request New Organization form](#request-new-organization).

Once this step is done by the customer, B2B store administrators may review the organization request by going to **VTEX Admin** > **Account Settings** > **B2B Organizations & Cost Centers** > **Organization Requests** (or at `/admin/b2b-organizations/requests`).

In this page, they can view a list of all the organization requests placed in their store.

![02-organization-requests](https://user-images.githubusercontent.com/77292838/159766650-d989a5bc-a33b-4fee-9e60-76f26567b067.png)

Each organization can have a status of **pending**, **approved** or **declined**. Pending requests are the ones that still need review.

To review a request, you must:

1. Click on a request from the table or click on <img src="https://user-images.githubusercontent.com/77292838/159766633-dfcb818f-6bd7-4cd0-92dc-9c682fb50d04.png" width="10" alt-text="00-ellipsis"/> > `View`.
2. Write a comment on the **Add note** field, if necessary.
3. Click on `Approve` or `Decline`.

![03-manage-organization-request](https://user-images.githubusercontent.com/77292838/159766653-ba4f6d4b-4bda-4856-86a3-0080f8d22e1e.png)

Upon approval, the request status will change to **Approved** and the organization will be created. The [Organization Admin and the Sales Admins](https://developers.vtex.com/docs/guides/vtex-storefront-permissions#available-storefront-roles) will be notified about this via email. You can learn more about this notification in the [Email templates](#email-templates) section. In addition, the user designated as the Organization Admin will be granted access to the [My Organization](#my-organization) tab on the **My Account** page of your storefront.

If the organization request is declined, the request status will be changed to **Declined** and the organization will not be created. The user designated as the Organization Admin is notified via email of this result. Read more about this notification in the [Email templates](#email-templates) section.

#### Organizations

The **Organizations** page includes a list of all the organizations created in your store and their respective status, and also allows store administrators to:

- [Add organizations](#add-organization).
- Access the [Organization details](#organization-details) page, which includes organization data, cost centers, collections, payment terms, price tables and users.

To access the page, go to **Account Settings** > **B2B Organizations & Cost Centers** > **Organizations** in the VTEX Admin (or at `/admin/b2b-organizations/organizations`).

![04-organizations](https://user-images.githubusercontent.com/77292838/159766661-63f7191a-51c4-49d7-a34d-d909456f2692.png)

You can click `Refetch` to refresh the organizations list on this page, fetching information about recently created organizations.

It is possible to use the search bar to find an organization by name or filter the organizations by status.

Each organization can have one of the following statuses:

- **Active**: the organization has been approved by the store administrators and it is currently active.
- **On hold**: the organization is currently paused, which means its users are not allowed to complete purchases at the moment.
- **Inactive**: the organization has been deactivated by the store administrators, so its users will not be able to login.

##### Add organization

You can manually create a new organization on the **Organizations** page. Follow these steps to do so:

1. Click on the `New` button.
2. Fill in the required information about the new organization, as illustrated in the image below.
   - **Name of organization:** name of the organization you want to create.
   - **Name of cost center:** name of the initial cost center associated with the organization.
   - **Country:** country where the cost center is located.
   - **ZIP:** postal code of the cost center address.
   - **Address Line 1:** primary address information, including street number and street name where the cost center is located.
   - **Address Line 2:** optional field for additional address information.
   - **City:** city where the cost center is located. This is filled in automatically based on the ZIP code informed.
   - **State:** state where the cost center is located. This is filled in automatically based on the ZIP code informed.
   - **Receiver:** name of the person that will receive orders in the informed address.
3. Click on `Add`.

![05-add-organization](https://user-images.githubusercontent.com/77292838/159766663-e1b2005a-0c2d-4bec-84ad-612007f17d64.gif)

>ℹ Additional cost centers and addresses may be added after creating the organization, as explained in the next section of this documentation.

#### Organization Details

In the **Organizations Details** page, you can see and edit the information of an existing organization:

- [Organization Name and Status](#organization-name-and-status)
- [Cost Centers](#cost-centers)
- [Collections](#collections)
- [Payment Terms](#payment-terms)
- [Price Tables](#price-tables)
- [Users ](#users)

You can access this page by going to **Account Settings** > **B2B Organizations & Cost Centers** > **Organizations** in the VTEX Admin and clicking on the organization whose details you want to view, or on <img src="https://user-images.githubusercontent.com/77292838/159766633-dfcb818f-6bd7-4cd0-92dc-9c682fb50d04.png" width="10" alt-text="00-ellipsis"/> > `View`.

>ℹ Note that assigning collections, payment terms, and price tables to an organization is optional. If these are not assigned, users of the organization will see the store's default catalog, have access to all payment methods, and see the store's default pricing.

##### Organization Name and Status

In the top section of the page, you can view the following information:

- **Organization Name:** name of the organization. This information can be edited.
- **Status:** status of the organization. You can set it to **Active**, **On Hold** or **Inactive** by selecting from a list.
- **Created:** date when the organization was created.

![06-organization-name-status](https://user-images.githubusercontent.com/77292838/159766675-bd899388-7537-427d-af37-fc048aaf8636.png)

##### Cost Centers

In the **Cost Centers** section, you can view all the cost centers associated with the organization. VTEX Admin users can view and manage cost centers for any organization.

![07-cost-centers](https://user-images.githubusercontent.com/77292838/159766678-0fd6c361-e1e6-470b-a9fc-c98b530c05e9.png)

>ℹ Each organization must have at least one cost center.

By default, each cost center will allow all of the [payment terms](#payment-terms) that have been assigned to the parent organization. However, **Organization Admin** users have the ability to enable or disable individual payment terms at the cost center level. See [Manage Cost Centers](#manage-cost-centers) for more information on this.

To create a new cost center, follow the steps below.

1. Click on the `New` button.
2. Fill in the required information about the new cost center, as illustrated in the image below.
   - **Name:** name of the cost center.
   - **Country:** country where the cost center is located.
   - **ZIP:** postal code of the cost center address.
   - **Address Line 1:** primary address information, including street number and street name where the cost center is located.
   - **Address Line 2:** optional field for additional address information.
   - **City:** city where the cost center is located. This is filled in automatically based on the ZIP code informed.
   - **State:** state where the cost center is located. This is filled in automatically based on the ZIP code informed.
   - **Receiver:** name of the person that will receive orders in the informed address.
3. Click on `Add`.

![08-add-cost-center](https://user-images.githubusercontent.com/77292838/159766680-5eb39381-a7da-4278-b8da-8cc7efe3e90a.gif)

##### Cost Center Details

You can view or edit the details of an existing cost center by clicking on it in the **Organization Details** page.

This will lead you to the **Cost Center Details** page, where you can:

- View or edit the cost center's **Name** and **Addresses**.
- View or edit the cost center's **Business Document**.
- Add a new shipping address associated with the cost center.
- Delete the cost center

![09-cost-center-details](https://user-images.githubusercontent.com/77292838/159766691-4557a032-a38c-4abb-a5a1-29019b833ad2.png)

The optional **Business Document** field may be used to store a Tax ID, VAT ID, CNPJ, or similar business identifier. If a Business Document is present in a user's cost center, it will be applied as the `corporateDocument` in the user's profile and therefore attached to any orders placed by the user.

>⚠️ The shipping addresses assigned to a cost center will be available to that cost center's users at checkout if you install [B2B Checkout Settings](https://developers.vtex.com/docs/guides/vtex-b2b-checkout-settings). No other addresses will be available. Therefore, each cost center must have at least one shipping address.

To edit or delete an existing address, click <img src="https://user-images.githubusercontent.com/77292838/159766633-dfcb818f-6bd7-4cd0-92dc-9c682fb50d04.png" width="10" alt-text="00-ellipsis"/> next to it and select **Edit** or **Delete**.

If you would like to add a new shipping address related to that cost center, follow these instructions:

1. Click on `Add new address`.
2. Fill in the required information about the new address.
   - **Country:** country where the cost center is located.
   - **ZIP:** postal code of the cost center address.
   - **Address Line 1:** primary address information, including street number and street name where the cost center is located.
   - **Address Line 2:** optional field for additional address information.
   - **City:** city where the cost center is located. This is filled in automatically based on the ZIP code informed.
   - **State:** state where the cost center is located. This is filled in automatically based on the ZIP code informed.
   - **Receiver:** name of the person that will receive orders in the informed address.
3. Click on `Add`.

Make sure to click `Save` in the top right of the **Cost Center Details** page after any changes.

If you want to delete the cost center, click on `Delete` instead.

##### Collections

>ℹ You must use the **Collections Beta** solution to be able to associate collections to organizations using **B2B Organizations**. Read our article on [Creating Collections Beta](https://help.vtex.com/tutorial/creating-collections-beta--yJBHqNMViOAnnnq4fyOye) for more information.

This section allows you to manage the [product collections](https://help.vtex.com/tutorial/creating-collections-beta--yJBHqNMViOAnnnq4fyOye) assigned to the organization. Your selections define the assortment of products the organization users will see in the storefront.

To add a collection, select the collection you want to add from the **Available** list and click `Add to org`.

To remove a collection, select the collection you want to remove from the **Assigned to organization** list and click `Remove from org`.

![10-collections](https://user-images.githubusercontent.com/77292838/159766692-aec018f6-d09b-4290-a180-a0e2b7040295.gif)

##### Payment Terms

In this section, you can choose which [payment conditions](https://help.vtex.com/en/tutorial/how-to-configure-payment-conditions--tutorials_455?&utm_source=autocomplete) are assigned to the organization. Your selections determine which payment options are available to organization users during checkout.

Note that the available payment options can be further customized per cost center by the **Organization Admin**. Check the [Manage Cost Centers](#manage-cost-centers) section for more information on this.

To add a payment term, select the option you want to add from the **Available** list and click `Add to org`.

To remove a payment term, select the option you want to remove from the **Assigned to organization** list and click `Remove from org`.

![11-payment-terms](https://user-images.githubusercontent.com/77292838/159766697-27de2f5b-18b3-4067-a4f1-81da8fb61bc0.gif)

>ℹ To customize the checkout according to each organization user's role, you need to install and configure [B2B Checkout Settings](https://developers.vtex.com/docs/guides/vtex-b2b-checkout-settings).

##### Price Tables

This section allows you to choose which [price tables](https://help.vtex.com/en/tutorial/creating-price-tables--58YmY2Iwggyw4WeSCGg24S) are assigned to the organization. The price tables you select determine the prices the organization users will see in the storefront.

To add a price table, select the option you want to add from the **Available** list and click `Add to org`.

To remove a price table, select the option you want to remove from the **Assigned to organization** list and click `Remove from org`.

![12-price-tables](https://user-images.githubusercontent.com/77292838/159766700-34ebfaaf-f6fa-42b6-85a9-a83dca5505ef.gif)

##### Users

This section presents a list of users associated with the organization, showing their **Email**, their **Role** in the organization and the **Cost Center** they are associated with.

![13-users-list](https://user-images.githubusercontent.com/77292838/159766707-572dd167-e948-4300-b259-1c9cd0b8a341.png)

To add a new user to the organization, follow these steps:

1. In the **Users** list, click on the `New` button.
2. Fill in the user's information, as illustrated below.
   - **Name:** full name of the user.
   - **Email:** email of the user.
   - **Cost Center:** cost center the user will be associated with.
   - **Role:** role the user will have in the storefront. See more details on the available roles in the [Storefront Permissions documentation](https://developers.vtex.com/docs/guides/vtex-storefront-permissions#available-storefront-roles).
3. Click on `Add`.

![14-add-new-user](https://user-images.githubusercontent.com/77292838/159766710-4e35973c-880d-4e98-8f93-4a6c87d3f4e8.png)

Once you add a new user to the organization, if a customer account did not already exist in your store for the provided email address, it will be created.

To edit or remove an existing user, follow these steps:

1. Click on the user you want to edit or delete in the **Users** list.
2. Edit the desired information.

   You can change the user's **Cost Center** and their **Role**.

   If you want to remove the user from the organization, click `Remove user` instead and skip the next step.

3. To apply your changes, click `Save`.

![15-edit-user](https://user-images.githubusercontent.com/77292838/159766713-03778c4a-370a-4c13-be4a-8f507cee0a73.png)

If a user is removed from an organization, their account will continue to exist in the store, but they will no longer be assigned to an organization, a cost center, and a B2B role. Thus, they will no longer have access to details of their organization in the **My Organization** page. Instead, they will have the ability to [request the creation of a new organization](#request-new-organization), if necessary.

>ℹ As an optional feature, you can install the [Admin Customers](https://github.com/vtex/admin-customers) app for additional customer management capabilities on the VTEX Admin.

#### Email templates

The **B2B Organizations** app provides a set of four email templates to be sent to B2B organization users, triggered automatically based on specific changes:

| **Template name**               | **Recipient**                          | **Trigger**                                 |
| ------------------------------- | -------------------------------------- | ------------------------------------------- |
| **Organization Approved**       | User with the Organization Admin role  | The organization request has been approved. |
| **Organization Created**        | Users with a Sales Admin role          | The organization has been created.          |
| **Organization Declined**       | User with the Organization Admin role  | The organization request has been declined. |
| **Organization Status Changed** | Users with the Organization Admin role | The organization status has changed.        |

If you want to view or edit any of these templates, follow the steps below.

1. In the VTEX Admin, go to **Customer > Message center > Templates**.
2. In the search bar, type `organization`.
3. Click on the template you want to view or edit.
4. Make the desired changes in the template. You can learn more about editing **Message Center** templates by reading our documentation on [How to create and edit transactional email templates](https://help.vtex.com/en/tracks/transactional-emails--6IkJwttMw5T84mlY9RifRP/335JZKUYgvYlGOJgvJYxRO).
5. Click on `Save`.

![16-templates](https://user-images.githubusercontent.com/77292838/159766714-6b5feaaf-3d81-472e-a713-55d952a1e556.gif)

### Master Data v2

The **B2B Organizations** app stores information about organization requests, organizations, and cost centers in [Master Data v2](https://help.vtex.com/pt/tutorial/master-data-v2--3JJ1mlzuo88w22gO0gy0QS).

This means that it is possible for store administrators or developers to fetch this information using the [Master Data API v2](https://developers.vtex.com/docs/api-reference/master-data-api-v2#overview), by using their **data entity name** as the value for the `data_entity_name` parameter.

You can see the data entity names in the table below.

| **Data entity names**   |
| ----------------------- |
| `organization_requests` |
| `organizations`         |
| `cost_centers`          |

### Storefront

Storefront capabilities, in turn, are accessible to B2B customers who visit a supplier's store, provided that they are logged in and have the required permissions.

The following sections describe what your customer can do in your storefront, after you've finished setting up the B2B Organizations app.

#### Request New Organization

A B2B user who is not already part of an organization can request the creation of a new buyer organization in your store by filling in the **Request New Organization** form. They can follow the steps below to do so.

1. Access the store website.
2. Click on **My Account** > **My Organization**.
3. Provide the required information, as shown in the image below.
   - **Organization Name:** name of the organization.
   - **User to become Organization Admin:** section where you must provide information about the first user of the organization, who will be assigned as the Organization Admin.
     - **First Name:** first name of the Organization Admin user.
     - **Last Name:** last name of the Organization Admin user.
     - **Email Address:** email address of the Organization Admin user.
   - **Default Cost Center:** section where you must provide information about the first cost center associated with the organization.
     - **Cost Center Name:** name of the cost center.
     - **Business Document:** optional field for a business document such as a Tax ID, CNPJ, etc.
     - **Country:** country where the cost center is located.
     - **ZIP:** postal code of the cost center address.
     - **Address Line 1:** primary address information, including street number and street name where the cost center is located.
     - **Address Line 2:** optional field for additional address information.
     - **City:** city where the cost center is located. This is filled in automatically based on the ZIP code informed.
     - **State:** state where the cost center is located. This is filled in automatically based on the ZIP code informed.
     - **Receiver:** name of the person that will receive orders in the informed address.
4. Click `Submit`.

![17-organization-request](https://user-images.githubusercontent.com/77292838/159766733-14da23e9-55d6-44e8-8cfc-95d62e3b4ade.gif)

After submitting the form, the request will be sent to a queue for review by the B2B store administrator  for more details on this, refer to the [Organization Requests](#organization-requests) section.

The user designated as the **Organization Admin** for the new organization will receive an email notification when the request has either been approved or declined by the store administrator. You can learn more about this notification in the [Email templates](#email-templates) section.

#### My Organization

Users who are designated as the **Organization Admin** or **Sales Admin** can manage the details of their organization in the storefront, on the **My Organization** page.

Users with the **Organization Buyer** or **Organization Approver** roles can also view a read-only version of this page.

To access **My Organization**, follow the instructions below.

1. Access the storefront and log in.
2. Click `Hello, {name}`.
3. Click on **My Account**.
4. Go to **My Organization** on the sidebar. You will see the page below.

![18-my-organization](https://user-images.githubusercontent.com/77292838/159766773-4d62c3ed-4282-45a9-bf36-d0041684cc50.png)

On this page, the user with the **Organization Admin** or **Sales Admin** roles may do the following:

- [Manage Cost Centers](#manage-cost-centers)
- [Manage Users](#manage-users)

##### Manage Cost Centers

**Organization Admin** or **Sales Admin** storefront users can find the cost centers associated with their organization in the **Cost Centers** section of the **My Organization** page.

To add a new cost center, they should go to **My Account > My Organization**, where they have access to the same options described in [Cost Centers](#cost-centers). It is possible to view or edit the details of an existing cost center by clicking on it, the same way as described in [Cost Center Details](#cost-center-details).

**Organization Admins** may also view and/or edit the **Business Document** assigned to each cost center, as described in [Cost Center Details](#cost-center-details).

In addition, **Organization Admins** can enable specific payment terms for a cost center, by using the toggle button to activate or deactivate the payment terms assigned to the organization, as shown below.

>⚠️ This section will only be available on the **My Organization** page if [payment terms](#payment-terms) have previously been assigned to the organization by the VTEX Admin users.

![19-payment-terms-cost-center](https://user-images.githubusercontent.com/77292838/159766775-dd0a17bd-8418-401b-a377-7d4c9ed0cf11.png)

##### Manage Users

**Organization Admin** or **Sales Admin** storefront users can also see and manage the users of their organization in the **Users** section in **My Organization**. To do this, they should go to **My Account > My Organization**, where they have access to the same options described in the [Users](#users) section of this documentation.

Users with the **Organization Admin** role may add, edit, or remove users with any of the following roles: **Organization Admin**, **Organization Approver**, and **Organization Buyer**.

Users with the **Sales Admin** role may add, edit, or remove users with any of the following roles: **Sales Admin**, **Sales Manager**, and **Sales Representative**.

###### Impersonate Users

In telesales, assisted sales, or customer support scenarios where the B2B customer needs help from a salesperson to navigate the store or place orders, it is common to make use of impersonation.

In the **B2B Organizations** app, only users with **Sales** roles or the **Organization Admin** role may impersonate another user.

This action will temporarily apply the impersonated user's email, organization, and cost center to their storefront session. It allows the impersonating users to do the following:

- Browse the store and see the prices, products, shipping addresses and payment methods that would be seen by the impersonated user.
- Take actions on behalf of the impersonated user, such as placing orders.
- Use their regular permissions.

To use impersonation, users with **Sales** roles or the **Organization Admin** role must follow the steps below.

1. In the **Users** section of [My Organization](#my-organization), click on <img src="https://user-images.githubusercontent.com/77292838/159766633-dfcb818f-6bd7-4cd0-92dc-9c682fb50d04.png" width="10" alt-text="00-ellipsis"/> in the row of the user they want to impersonate.
2. Click on **Impersonate User**.

![20-users](https://user-images.githubusercontent.com/77292838/159766777-1ff83458-cad0-46de-82e4-1e3c3e4bb144.png)

#### User widget

To give storefront users visibility into their currently assigned organization, cost center, and role, this app provides a user widget which can be added to the account's store theme:

![21-user-widget](https://user-images.githubusercontent.com/77292838/159766781-8edabb7e-292c-4c8e-a88e-ae937ec7db86.png)

>ℹ To display the user widget, it is necessary to follow the instructions in the [User widget configuration](#user-widget-configuration) section.

If users click `Manage organization`, they can access the **My Organization** page directly.

In case impersonation is currently active, this block will also show the email of the user being impersonated, as well as a `Stop impersonation` button:

![22-user-widget-impersonation](https://user-images.githubusercontent.com/77292838/159766784-6bce63af-9cc6-4ac4-bc59-460b74722dbe.png)
