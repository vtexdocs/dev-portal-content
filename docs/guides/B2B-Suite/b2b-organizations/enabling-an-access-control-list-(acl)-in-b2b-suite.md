---
title: "Enabling an access control list (ACL) in B2B Suite"
slug: "enabling-an-access-control-list-(acl)-in-b2b-suite"
hidden: false
createdAt: "2025-11-03t09:00:09.698z"
updatedAt: "2025-11-03t09:00:09.698z"
---

The **Access Control List (ACL)** feature in B2B Suite allows you to restrict access to resources such as **buyer organizations**, **cost centers**, and **members** in the VTEX Admin. You need to set up specific permissions to allow the users to view or manage these resources.

If a user doesn't have the required permissions, they won't be able to access the **Buyer organizations** section in the Admin.

## Required permissions

To allow access to the apps related to B2B Organizations in the Admin, you need to add the following roles:

| Nome da permissão           | Descrição                                                                 |
|------------------------------|---------------------------------------------------------------------------|
| **buyer_organization_view** | Allows viewing organizations, cost centers, and users.             |
| **buyer_organization_edit** | Allows creating, editing, and deleting organizations, cost centers, and users. |

These permissions are available under the **Buyer Organizations/Management** resource.
Follow the steps below to access this resource in the Admin:

1. Access the VTEX Admin.
2. In the upper right corner, click the icon with your initial.
3. Click **Account settings**.
4. Click **User roles**.

## Updating B2B Suite apps

To enable the ACL feature, follow the steps below:

1. Open the terminal [Using VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-usage).
2. Run the commands below to update the B2B Suite apps.

```json
vtex install vtex.storefront-permissions@3.1.0 --force
vtex install vtex.b2b-organizations-graphql@2.0.1 --force
vtex install vtex.b2b-quotes-graphql@4.0.1 --force
vtex install vtex.b2b-orders-history@2.0.1
vtex install vtex.storefront-permissions-ui@3.0.1
vtex install vtex.b2b-organizations@3.0.1
vtex install vtex.b2b-quotes@3.0.1
vtex install vtex.storefront-permissions-components@2.0.1
vtex install vtex.b2b-admin-customers@2.0.1
vtex install vtex.b2b-my-account@2.0.0
vtex install vtex.b2b-checkout-settings@3.0.1 --force
vtex install vtex.b2bstore@5.0.0
vtex install vtex.b2b-suite@2.0.0
```

> ℹ️ If any of the apps above is not installed in your store, update only the ones you have.

3. Run the command below to check if there are any dependencies on older versions.

```json
vtex deps list | grep <app-name-without-version>
```

4. If there are any apps with an older version, update them as described in step 2

>⚠️ To revert to the previous version, install the previous versions of each app.

## Updating custom apps with ACL support

If your account uses custom apps that depend on the **b2b-organizations-graphql** or **storefront-permissions** apps, you need to update the `manifest.json` file to include the permission policies.

The `manifest.json` file is located at the **root of the app repository**. 
Open the file in a code editor and add the following policies in the `policies` section:

```json
"policies": [
  {
    "name": "buyer_organization_view"
  },
  {
    "name": "buyer_organization_edit"
  }
]
```

After saving the file, publish the app again to apply the changes.