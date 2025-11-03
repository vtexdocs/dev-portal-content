---
title: Access control by permissions in the B2B Suite
slug: "2025-11-03-access-control-by-permissions-in-the-b2b-suite"
hidden: false
type: "improved"
createdAt: "2025-11-03T00:00:00.219Z"
updatedAt: "2025-11-03T00:00:00.219Z"
excerpt: "The B2B Suite now includes an Access Control List (ACL) to manage user permissions for buyer organizations, cost centers, and members."
tags:
    - B2B Suite
---

The [B2B Suite](https://developers.vtex.com/docs/apps/vtex.b2b-suite) now allows you to configure specific permissions to control user access to buyer organizations, cost centers, and members in the VTEX Admin. This feature ensures security and control, allowing only authorized users to view and edit this information.

## What has changed?

We've implemented the new **Access Control List (ACL)** feature in the B2B Suite,  allowing administrators to define which users can view or edit:

- Buyer organizations
- Cost centers
- Members linked to an organization

If the user doesn't have the required permissions, the **Buyer Organizations** section won't be displayed in the Admin.

## What needs to be done?

1. Update the B2B Suite apps to the latest major versions using the commands below in the terminal:

    ```json
    vtex install vtex.storefront-permissions@3.0.0 --force
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

2. Check legacy dependencies using the command:

    ```json
    vtex deps list | grep <app-name-without-version>
    ```

   If there are any apps with an older version, update them as described in step 1.

3. Add the necessary permissions to roles in the Admin, within the Buyer Organizations/Management resource:

    | Permission                | Description                                                     |
    |----------------------------|-----------------------------------------------------------------|
    | **buyer_organization_view** | Allows viewing organizations, cost centers, and users.          |
    | **buyer_organization_edit** | Allows creating, editing, and deleting organizations, cost centers, and users. |

4. If you use custom apps that depend on `b2b-organizations-graphql` and `storefront-permissions`, update the `manifest.json`file to include permission [policies](https://developers.vtex.com/docs/guides/vtex-io-documentation-policies):

    ```json
    "policies": [
    { "name": "buyer_organization_view" },
    { "name": "buyer_organization_edit" }
    ]
    ```

> ℹ️ For more information, see the [Enabling an access control list (ACL) in B2B Suite](https://developers.vtex.com/docs/guides/enabling-an-access-control-list-acl-in-b2b-suite) documentation.
