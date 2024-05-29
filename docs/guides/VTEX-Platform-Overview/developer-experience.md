---
title: "Developer experience"
slug: "developer-experience"
hidden: false
createdAt: "2024-05-24T10:18:55.338Z"
updatedAt: "2024-05-24T10:18:55.338Z"
excerpt: "Learn how our platform enhances the developer experience."
seeAlso:
 - "/docs/guides/store-framework"
---

This guide offers an overview of the tools and resources available to development teams. In the following sections, you will learn about the various features we provide for developers in our ecosystem and the opportunities for sharing knowledge and collaborating within the community.

- [App development](#app-development): Develop and manage your VTEX IO apps.
- [Storefront development](#storefront-development): Explore VTEX’s storefront solutions.
- [Contributions and collaboration](#contributions-and-collaboration): Contribute to the VTEX ecosystem by sharing your knowledge.

## App development

[VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io) is our development platform that simplifies building, managing, and scaling ecommerce solutions by offering a comprehensive suite of tools and services,  manual coding efforts while ensuring performance, scalability, and security for your projects.

Within the VTEX IO platform, you can leverage familiar technologies and frameworks like [TypeScript](https://www.typescriptlang.org/), [React](https://react.dev/), [GraphQL](https://graphql.org/), and [Node](https://nodejs.org/en) to enable rapid development and evolution. This set of technologies allows you to build custom web storefronts, customize the shopper experience, integrate with third-party systems, and create custom applications or other components to extend the VTEX IO’s functionalities.

Next, you will find an overview of the main capabilities of the VTEX IO platform.

### Developer tools

Learn about the essential developer tools, which equip you with the knowledge to streamline your app development journey with VTEX IO.

#### Command Line Interface (CLI)

A Command Line Interface (CLI) is a text-based interface used to interact with a computer system or software application by typing commands into a terminal or command prompt. It allows users to perform tasks such as running programs, managing files, and configuring settings efficiently.

To build and develop any project in the VTEX IO, use the pre-configured [**VTEX IO CLI**](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference). This CLI is the starting and ending point for any development on the VTEX platform. It provides the ability to perform actions relevant to the development process, such as releasing new app versions, for example.

>ℹ️ For [FastStore](https://developers.vtex.com/docs/guides/faststore/docs-what-is-faststore) projects, we also offer the [**FastStore CLI**](https://developers.vtex.com/docs/guides/faststore/getting-started-3-faststore-cli). This CLI tool connects the source code in [`@faststore/core`](https://developers.vtex.com/docs/guides/faststore/project-structure-overview#packagejson) package with your customizations and extensions for your FastStore project.

#### Workspaces

[Workspaces](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace) are isolated environments for app development, acting as separate versions of the same account. There are three types of workspaces in VTEX:

- **Master**: A unique production workspace that reflects the live store content.
- [**Development workspaces**](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace): Environments that allow testing changes in real time. They provide freedom in code development without affecting user traffic and the live store. Necessary when making changes to storefronts or developing a new VTEX IO app.
- [**Production workspaces**](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-production-workspace): Mainly used to validate VTEX IO apps. These workspaces handle traffic, so they can be used to run [A/B tests](#ab-tests) and can be [promoted to master](https://developers.vtex.com/docs/guides/vtex-io-documentation-promoting-a-workspace-to-master).

To learn how to manage workspaces effectively in your projects, check out the [Best practices on workspaces management](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspaces-best-practices) guide.

#### A/B Tests

After [linking your app](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) in a production workspace, it is possible to run an [A/B test](https://developers.vtex.com/docs/guides/vtex-io-documentation-running-native-ab-testing) to compare traffic and choose the workspace that performs better in terms of user engagement and conversions.

#### Builders

[Builders](https://developers.vtex.com/docs/guides/vtex-io-documentation-builders) streamline the development experience by abstracting complex implementation details, enabling developers to focus on enhancing stores’ capabilities. Acting as bridges, builders allow different parts of an app to work together by configuring and connecting to necessary services.

There are various [types of builders](https://developers.vtex.com/docs/guides/vtex-io-documentation-builders#list-of-builders), each equipped with pre-built functionalities and integration options, facilitating quick feature implementation for specific tasks or functionalities. For example, some builders focus on [developing new storefront apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-react-builder), [setting styles for your components](https://developers.vtex.com/docs/guides/vtex-io-documentation-styles-builder) within your [Store Theme app](https://developers.vtex.com/docs/guides/vtex-io-documentation-3-settingyourstoretheme), [publishing app documentation](https://developers.vtex.com/docs/guides/vtex-io-documentation-docs-builder), among others.

By leveraging builders, developers can extend the functionality of the VTEX platform without starting from scratch. This modular approach promotes flexibility, scalability, and efficiency in developing and customizing VTEX-based ecommerce solutions, accelerating development cycles, promoting code reusability, and facilitating rapid [deployment](#deployment) of new functionalities.

#### Edition apps

[Edition apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app) are collections of VTEX apps that define the functionalities available in a VTEX account. They consist of a bundle of settings, policies, backend, and frontend apps, aiming to streamline the setup and management of essential configurations quickly and efficiently.

We offer two native Edition Apps:

- **Edition Store**: For Store Framework stores.
- **Edition Business**: For Legacy CMS Portal stores.

>ℹ️ To learn how to develop your own Edition App, check out the [Developing an Edition App](https://developers.vtex.com/docs/guides/vtex-io-documentation-configuring-an-edition-app) guide.

### VTEX Apps

[VTEX Apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-a-vtex-app) expand VTEX platform capabilities across various aspects of digital commerce, such as marketing, analytics, logistics, security, and store design.

We offer the following types of apps:

- [**Storefront apps**](https://developers.vtex.com/docs/guides/vtex-io-documentation-1-developing-storefront-apps-using-react-and-vtex-io): React components that enhance the functionality and user experience of your store, such as product carousels or navigation menus.
- [**Backend apps**](https://developers.vtex.com/docs/guides/vtex-io-documentation-service): Node or .NET Core services that enable VTEX IO apps to export HTTP routes, GraphQL resolvers, and event handlers to the server.
- [**Pixel apps**](https://developers.vtex.com/docs/guides/vtex-io-documentation-1-developnativeintegrationswithpixelapps): Collect user data for third-party services by running scripts on all pages of a store website.
- [**Edition apps**](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app): Bundles of settings, policies, backend, and frontend apps encapsulated into a single app.

You can take advantage of our [VTEX IO apps](https://developers.vtex.com/docs/vtex-io-apps), which are pre-built solutions typically developed and maintained by VTEX that can be easily integrated into your store. These apps can be discovered, installed, and managed through the [VTEX App Store](#vtex-app-store).

If you cannot find an app that meets your business needs, you can create customized solutions by [developing your own VTEX app](https://developers.vtex.com/docs/guides/vtex-io-documentation-developing-an-app) using the [VTEX IO](#app-development).

We provide some ready-to-use [code templates](https://developers.vtex.com/docs/guides/code-samples) to simplify your development process when creating a VTEX IO app. Using one of them, you do not need to write the boilerplate code, ensuring development agility, quality and compliance with platform standards.

>ℹ️ To learn about the relevant aspects to consider when developing VTEX IO apps, check out the [Before creating an app for your store](https://help.vtex.com/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/7euXDZR5CCnVFSrXyczIhu#before-creating-an-app-for-your-store) article.

#### VTEX App Store

You can make your apps available to the VTEX ecosystem on the [VTEX App Store](https://developers.vtex.com/docs/guides/vtex-app-store), a marketplace for VTEX IO plug-and-play solutions.

>ℹ️ To learn about the homologation requirements for the VTEX App Store, check out the [App Store Guidelines](https://developers.vtex.com/docs/guides/vtex-io-documentation-homologation-requirements-for-vtex-app-store).

#### Deployment

Once a new app has been developed, it must be deployed to the VTEX IO production workspace to make it publicly available. The deployment process is the following:

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/making-an-app-publicly-available.png)

- [**Releasing a new app version**](https://developers.vtex.com/docs/guides/vtex-io-documentation-releasing-a-new-app-version): Marks the beginning by releasing the app using Git, updating the version in `manifest.json`, and documenting changes in CHANGELOG.md.
- [**Publishing**](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app): The app version becomes a candidate version, ready for testing and validation in a production workspace.
- [**Testing**](https://developers.vtex.com/docs/guides/ab-tests): Run [A/B tests](#ab-tests).
- [**Deploying**](https://developers.vtex.com/docs/guides/vtex-io-documentation-deploying-the-app-stable-version): Update the app version across all accounts where the app is installed.
- [**Promoting**](https://developers.vtex.com/docs/guides/vtex-io-documentation-promoting-a-workspace-to-master): Optional step to promote the production workspace to master.

>ℹ Check [Deploying a new app version](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available) for more details on this flow.

>ℹ️ To learn about app versioning in VTEX IO, refer to [SemVer standard](https://semver.org/) and our [Understanding app versioning](https://developers.vtex.com/docs/guides/vtex-io-documentation-releasing-a-new-app-version) article.

Our deployment process integrates an automated Continuous Integration and Continuous Delivery (CI/CD) framework, facilitating seamless building and testing whenever changes occur in the source code. Through this CI/CD pipeline, we ensure swift and dependable delivery of new features and updates, while maintaining high standards of code quality.

## Storefront development

VTEX provides different options for storefront development, each with its own characteristics, according to your business needs:

- [**FastStore**](https://developers.vtex.com/docs/guides/faststore/docs-what-is-faststore): Innovative storefront technology based on the [Jamstack](https://jamstack.org/) architecture. FastStore prioritizes performance and stability, offering development teams an easily maintainable solution for editing store pages.
- [**Store Framework**](https://developers.vtex.com/docs/guides/store-framework): Composable and flexible commerce model, allowing integration of [VTEX IO apps](https://developers.vtex.com/docs/vtex-io-apps) for dynamic storefronts.
- [**Legacy CMS Portal**](https://developers.vtex.com/docs/guides/vtex-io-documentation-migrating-storefront-from-legacy-to-io): Legacy storefront technology, that relies on HTML, CSS, and JavaScript, with code management exclusively through the VTEX Admin. This technology is no longer available to new stores starting with VTEX.

## Contributions and collaboration

The [VTEX Community](https://community.vtex.com/) is an ecosystem where our clients and partners can interact, ask questions, and exchange information. It is the go-to place to find answers and discuss VTEX products.

The VTEX Community provides forums and discussion groups where members can ask questions, share insights, and seek assistance from peers and experts. These forums cover various topics related to development, implementation, optimization, and best practices for using the VTEX IO platform.

Developers can participate in the VTEX Community, sharing knowledge, contributing code, and collaborating with the ecosystem to improve the platform and address common challenges.
