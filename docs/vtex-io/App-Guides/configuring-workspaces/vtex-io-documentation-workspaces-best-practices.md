---
title: "Best practices on workspaces management"
slug: "vtex-io-documentation-workspaces-best-practices"
hidden: false
createdAt: "2023-02-07T16:08:55.480Z"
updatedAt: "2023-02-07T17:02:55.480Z"
excerpt: "Learn how to manage workspaces effectively"
---

Some best practices help ensure smooth development, effective testing, and secure deployments when working with workspaces. Refer to the following guidelines to avoid errors and store breakdowns:

## Workspace setup

Understanding workspaces: It is essential to understand the different types of [workspaces](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace) well and use them correctly.

- **Using development workspaces**: Making changes directly to the master workspace can potentially affect the user experience. You must create a separate [development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace/) and switch to it before starting any development work.

- **Developing a Store Theme**: Before developing your Store Theme, ensure your VTEX account has the [Store Edition app](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app) installed. Otherwise, you cannot implement the VTEX Store Framework successfully.

Developing a Store Theme or other apps using subaccounts **it is not recommended**. This practice may lead to inconsistencies that will make it impossible to install the app in the production workspace of the main account. You must use a **development workspace** of the main account.

## Managing collaborative projects

- **Using workspaces**: In collaborative projects that involve different workspaces, be aware of using **development workspaces** and ensure that code versioning is performed using appropriate tools such as GitHub, as development workspaces are disposable.

Never develop a Store Theme or other apps directly in the production workspace. If you do so, when it gets promoted to master, it may break your store.

- **Code versioning**: Use efficient code versioning practices to ensure the traceability of changes. This makes it easier to identify issues and revert changes if necessary.

To provide a structured process and avoid errors and loss of content, the collaboration must be done by utilizing pull requests for proposing and reviewing changes. These pull requests must be well-documented, fostering discussion and ensuring that modifications meet quality standards before merging.

## Testing and Quality Assurance

- **Pre-production testing**: Before moving any changes to the production workspace, conduct your tests in the development workspace to ensure all functionalities are working as expected.

>ℹ️ When working in development workspaces, apps must be **linked**. However, in production workspaces, apps must be **installed**.

- **A/B testing**: Before promoting the production workspace to master, [run A/B tests](https://developers.vtex.com/docs/guides/vtex-io-documentation-running-native-ab-testing) to compare traffic between these workspaces. This test reveals which version is best for your business needs.

## Deployment and workspace promotion

- **Checkout UI Custom**: if your store uses the [Checkout UI Custom](https://developers.vtex.com/docs/guides/vtex-checkout-ui-custom-v0) app, you must first publish its configurations on your new production workspace. Otherwise, you might lose the Checkout custom Javascript code and styles.

- **Core services data behavior**: Be careful about changes in the [VTEX Core Services](https://developers.vtex.com/docs/guides/getting-started#vtex-core-services) accessible via Admin, such as Catalog, Pricing, Promotions, Checkout and others. Changes made to these services in a specific workspace are reflected across all others, as the workspaces share the same VTEX Core Services.

The **Site Editor** is always linked to the workspace, meaning that changes made in a specific workspace do not reflect in others. The master workspace is the only environment where changes made in Site Editor reflect in the live store.

- **Updating live stores**: When performing a major update on your Store Theme, be aware of the steps outlined in [our documentation](https://developers.vtex.com/docs/guides/vtex-io-documentation-migrating-cms-settings-after-major-update) to avoid loss of content.

It is crucial that the same `threepath` structure be maintained in the new major, as changes to it result in a content loss in the Site Editor and potential store breakdown. If you need to change the `threepath` structure, it is necessary to configure the Site Editor again.

## Do’s and Don’ts

|✅ Do|❌ Don't|
|-----|-------|
|<ul><li>Create a development workspace to start any development work.</li><li>When developing a Store Theme, ensure your VTEX account has the Store Edition app installed.</li><li>Utilize appropriate tools, such as GitHub, to handle code versioning in your projects.</li><li>Run A/B tests before promoting a production workspace to master.</li><li>Feel free to perform tests in the Site Editor of your development workspace, as changes will not be reflected in others.</li></ul>|<ul><li>Use subaccounts to develop a Store Theme or other apps.</li><li>Start any development work in a production workspace.</li><li>Make changes in any module of VTEX Core Services when using a development or production workspace.</li><li>Change the `threepath` structure when updating a Store Theme.</li></ul>|

