---
title: "Organizations Challenge"
slug: "vtex-organizations-challenge"
hidden: false
createdAt: "2020-06-03T15:19:10.972Z"
updatedAt: "2021-11-18T19:27:08.494Z"
---
Organizations Challenge is an app that checks if users are allowed to view content, based on their roles and permissions within [Organizations](https://github.com/vtex-apps/organizations).


## Prerequisites

Before using the Organizations Challenge app, please make sure you meet the following prerequisites.


### Set up your development environment

Before starting with the B2B Store Theme setup itself, you must:

1. [Set up a workspace to develop in VTEX IO](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-2-basicsetuptodevelopinvtexio) on your machine.
2. Follow [these instructions](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-2-prerequesites) to make sure you meet all the prerequisites to develop using Store Framework.
3. Make sure your store’s catalog is integrated with VTEX Intelligent Search, as described in [this article](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/6wKQgKmu2FT6084BJT7z5V).


### Install required Organizations apps

Now you must install the required apps listed below. They are mandatory for the Organizations Challenge app to work properly.


#### Admin Organizations

In brief, the [Admin Organizations](https://github.com/vtex-apps/admin-organizations) app is responsible for managing the Roles and Permissions modules on your store’s Admin.

Run the command  `vtex install vtex.admin-organizations@1.x` on the CLI to install it in your store.


#### Organizations

The [Organizations](https://github.com/vtex-apps/organizations) app allows you to create an organization — a business store — and manage users under that organization with different roles.

Run the command `vtex install vtex.organizations@1.x` on the CLI to install it on your store.



### Create Master Data schemas

You must have the following Master Data schemas configured:

* [`BusinessPermission schema`](https://developers.vtex.com/vtex-developer-docs/docs/installing-the-b2b-store-theme#businesspermission-schema)
* [`BusinessRole schema`](https://developers.vtex.com/vtex-developer-docs/docs/installing-the-b2b-store-theme#businessrole-schema)
* [`BusinessOrganization schema`](https://developers.vtex.com/vtex-developer-docs/docs/installing-the-b2b-store-theme#businessorganization-schema)
* [`UserOrganization schema`](https://developers.vtex.com/vtex-developer-docs/docs/installing-the-b2b-store-theme#userorganization-schema)

Learn more about how to create these schemas in the [Create Master Data schemas](https://developers.vtex.com/vtex-developer-docs/docs/installing-the-b2b-store-theme#create-master-data-schemas) section of our guide on [Installing the B2B Store Theme](https://developers.vtex.com/vtex-developer-docs/docs/installing-the-b2b-store-theme).


### Create Master Data fields

You need to have the `isOrgAdmin` and `organizationId` fields configured in Master Data. Learn more about how to create this field in the [Create fields in Master Data](https://developers.vtex.com/vtex-developer-docs/docs/installing-the-b2b-store-theme#create-fields-in-master-data) section of our guide on [Installing the B2B Store Theme](https://developers.vtex.com/vtex-developer-docs/docs/installing-the-b2b-store-theme).


## Installation

First, add the app as a dependency in your theme’s `manifest.json` file, as follows:

```json
  "dependencies": {
    "vtex.organizations-challenge": "1.x"
  }
```

Then, follow the instructions below to set your theme’s blocks, manage roles and permissions and add permissions using the **Site Editor**.



### Set theme blocks

In your theme’s files, wrap the blocks you want to be visible only to the allowed logged-in users with `challenge-permission`.

This component will check if the user has permission to see the `allowed-content`, otherwise they will see the `disallowed-content`. 

In the example below, taken from the B2B Store Theme’s `product-summary-prices.jsonc` file, the product prices are only visible to logged-in users with the `view_prices` permission. Otherwise, the store will show the `"Log in or sign up to view prices"` message instead.

Example:

```json
{
  "challenge-permission#product-summary-price": {
    "blocks": [
      "allowed-content#product-summary-price",
      "disallowed-content#product-summary-price"
    ],
    "props": {
      "permissions": [{ "name": "view_prices" }]
    }
  },
  "allowed-content#product-summary-price": {
    "children": ["product-summary-price"]
  },
  "disallowed-content#product-summary-price": {
    "children": ["rich-text#product-summary-price"]
  },
  "rich-text#product-summary-price": {
    "props": {
      "blockClass": ["product-summary-price-message"],
      "text": "Log in or sign up to view prices"
    }
  }
}
```


### Manage roles and permissions

To manage users’ permissions to view prices, you must follow the steps below to associate them with the `view_prices` permission.

1. In the **Account Settings** module on VTEX’s Admin panel, click on **Authorizations** and then on **All Permissions**.

2. Check if the `view_prices` permission exists, as shown in the image below.

    ![Permissions](https://raw.githubusercontent.com/vtex-apps/organizations-challenge/master/docs/images/1-permissions.png "Permissions")

    If it already exists, proceed to step 3.

    If it does not exist yet, click on `New` and fill in the fields as follows:

      * **Name:** view_prices
      * **Label:** View Prices

    Click on `Save`.

3. In the **Account Settings** module, click on **Authorizations** and then on **All Roles**.
4. Check if the **sales_manager** role exists and is associated with the **View Prices** permission, as shown below.

    ![Roles](https://raw.githubusercontent.com/vtex-apps/organizations-challenge/master/docs/images/2-roles.png "Roles")

    If it already exists, proceed to step 5.

    If it does not exist yet, click on `New` and fill in the fields as follows:

      * **Name:** sales_manager
      * **Label:** Sales Manager
      * **Add Permissions:** click on `˅` and then on **View Prices**.

    Click on `Save`.

5. Go to the store’s website and log in as the desired user.

6. Click on `Hello, {name}` and then on `My Account`, as shown below. 

    ![My Account](https://raw.githubusercontent.com/vtex-apps/organizations-challenge/master/docs/images/3-myaccount.png "My Account")

7. Click on the **My Organization** tab.

8. Fill the data below and click on `Save`.

    * **Name:** organization name.
    * **Phone number:** organization phone number.
    * **Address:** address of the organization.
    * **Email:** email address of the organization.

The user will then be saved automatically with the **Sales Manager** role and the **View Prices** permission. If you refresh this page, you will be able to add other users as members of the organization and give them roles.

### Edit blocks’ permissions using Site Editor [OPTIONAL]

After the steps above, if you must edit the permissions allowed to see the defined blocks, you can do that either directly in the code – as explained in the [Set theme blocks](#set-theme-blocks) section – or using the **Site Editor**, on the VTEX Admin. This section will explain how to use the **Site Editor** with this purpose.

You should give a list of permissions to `challenge-permission` block from the **Site Editor** to allow or disallow relevant blocks.

1. In the **Store Setup** module on VTEX’s admin panel, click on **CMS** and then on **Site Editor**.

2. In the list of blocks, illustrated below, find the **Permission Challenge** block whose permissions you want to edit and click on it.

    ![Site Editor](https://raw.githubusercontent.com/vtex-apps/organizations-challenge/master/docs/images/4-siteeditor.png "Site Editor")

3. You will see the options below on the sidebar.

    ![Permission Challenge block](https://raw.githubusercontent.com/vtex-apps/organizations-challenge/master/docs/images/5-permissionchallengeblock.png "Permission Challenge block")

By clicking on the **Untitled content** field, you have the option to name this Permission Challenge block as you wish.

Under **Permissions**, you can click on `+ Add` to inform the **Name** of a permission allowed to see this block and click on `Apply` to save your changes.

![Allowed Permissions](https://raw.githubusercontent.com/vtex-apps/organizations-challenge/master/docs/images/6-allowedpermissions.png "Allowed Permissions")

The **view_prices** permission is already saved as an **Item** – if you click it you will have the option to change it, the same way you would create a new one.

If you perform any changes, make sure you click on `Apply`.

> ℹ The permission **Name** used on **Site Editor** must be valid on the **Permissions** page, as described in step 2 of the [Manage roles and permissions](#manage-roles-and-permissions) section.


## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization).

You can create a file called `vtex.challenge-permission.css` inside the `styles/css` folder to add your custom styles.

| CSS Handle |
| ---------  |
| `challengeContentWrapper` |