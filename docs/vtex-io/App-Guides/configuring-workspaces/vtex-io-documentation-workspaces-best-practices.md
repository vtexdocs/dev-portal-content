---
title: "Best practices on workspaces management"
slug: "vtex-io-documentation-workspaces-best-practices"
hidden: false
createdAt: "2024-02-19T09:19:55.480Z"
updatedAt: "2024-02-21T16:19:56.480Z"
excerpt: "Learn how to manage workspaces effectively"
---

Refer to the following [workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace) guidelines to ensure smooth development, effective testing, secure deployments, and minimize errors and breakdowns.

## Workspace setup

Understanding workspaces is essential for effective development. Different types of workspaces, such as Development and Production ones, serve specific purposes and should be used appropriately.

- **Using development workspaces**: Create a separate [development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace/) and switch to it before starting any development work. Note that making changes directly to the master workspace can potentially affect the user experience.

- **[Store Framework] Developing a Store Theme**: Before developing a Store Theme app, ensure the [Store Edition app](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app) is installed in your account. Otherwise, you won't be able to use the Store Framework successfully.

- **App vendor**: Developing a Store Theme or other apps using [subaccounts](https://help.vtex.com/en/tutorial/creating-subaccount-multi-store-multi-domain--tutorials_510?&utm_source=autocomplete) is not recommended. This practice may lead to inconsistencies that will make it impossible to install the app in the production workspace of the main account. Always use a **development workspace** of the main account for such tasks.

## Managing collaborative projects

In collaborative projects that involve different workspaces, be aware of using **development workspaces** and ensure that code versioning is performed using appropriate tools, such as GitHub.

- **Using workspaces**: Never develop apps directly in the production workspace. If you do so, when it gets promoted to master, it may break your store.

- **Code versioning**: Use efficient code versioning practices to ensure the traceability of changes. This makes it easier to identify issues and revert changes if necessary. Use pull requests for proposing and reviewing changes, ensuring documentation and discussion to maintain quality standards

## Testing and Quality Assurance

From pre-production testing to implementing A/B testing strategies, discover how to maintain high standards of quality assurance throughout your development process.

- **Pre-production testing**: Before moving any changes to the production workspace, test your code in the development workspace and ensure all functionalities are working as expected.

- **Production testing**: Once you are satisfied with your code in the development workspace, release a candidate version of your app. Install and thoroughly test it in a production workspace. [Run A/B tests](https://developers.vtex.com/docs/guides/vtex-io-documentation-running-native-ab-testing) to compare traffic between these workspaces to understand which app version is best for your business needs.

## Deployment and workspace promotion

Implement these best practices to deploy changes and promote workspaces seamlessly, avoiding disruptions to your live store.

- **Checkout UI Custom**: If your store uses the [Checkout UI Custom](https://developers.vtex.com/docs/guides/vtex-checkout-ui-custom-v0) app, ensure configurations are published to the new production workspace to avoid losing the Checkout custom Javascript code and styles.

- **Core services data behavior**: Be careful about changes in the [VTEX Core Services](https://developers.vtex.com/docs/guides/getting-started#vtex-core-services) accessible via Admin, such as Catalog, Pricing, Promotions, Checkout, and others. Changes made to these services in a specific workspace are reflected across all others, as the workspaces share the same VTEX Core Services.

- **[Store Framework] Site Editor behavior**: Note that the **Site Editor** is always linked to the workspace, meaning that changes made in a specific workspace do not reflect in others. The master workspace is the only environment where changes made in Site Editor reflect in the live store.

- **[Store Framework] Updating live stores**: When performing a major update on your Store Theme, be aware of the steps outlined in the [Migrating CMS setting after a major theme update](https://developers.vtex.com/docs/guides/vtex-io-documentation-migrating-cms-settings-after-major-update) guide to avoid loss of content.

It is crucial that the same `treePath` structure be maintained in the new major, as changes to it result in a content loss in the Site Editor and potential store breakdown. If you need to change the `treePath` structure, make sure to configure the Site Editor again.

## Do’s and Don’ts

|✅ Do|❌ Don't|
|-----|-------|
|<ul><li>Create a development workspace to start any development work.</li><li>When developing a Store Theme, ensure your VTEX account has the Store Edition app installed.</li><li>Utilize appropriate tools, such as GitHub, to handle code versioning in your projects.</li><li>Feel free to perform tests in the Site Editor of your development workspace, as changes will not be reflected in others.</li></ul>|<ul><li>Do not use subaccounts to develop a Store Theme or other apps.</li><li>Do not start development work in a production workspace.</li><li>Do not make changes in any module of VTEX Core Services when using a development or production workspace. </li></ul>|
