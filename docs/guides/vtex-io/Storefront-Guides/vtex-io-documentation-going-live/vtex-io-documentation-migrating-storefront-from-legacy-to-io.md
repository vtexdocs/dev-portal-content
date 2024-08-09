---
title: "Migrating your storefront from Legacy CMS Portal to Store Framework"
slug: "vtex-io-documentation-migrating-storefront-from-legacy-to-io"
hidden: false
createdAt: "2022-10-25T18:41:04.323Z"
updatedAt: "2024-08-09T15:42:08.321Z"
---

VTEX provides different storefront solutions for you to choose from based on your operation’s needs: [Store Framework](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-store-framework) and [FastStore](https://developers.vtex.com/docs/guides/faststore/docs-what-is-faststore). However, there are still stores running the [Legacy CMS Portal](https://help.vtex.com/en/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/1oN446gRGcR2s70RvBCAmj).

If your store uses Legacy CMS Portal, we strongly recommend migrating it to Store Framework. For implementation details, see the following sections.

> ℹ️ If you wish to migrate your store from another commerce platform, the instructions below do not apply. In this case, follow the steps in the [Go Live guide](https://developers.vtex.com/docs/guides/vtex-io-documentation-go-live).

## Instructions

To migrate your store from Legacy CMS Portal to [Store Framework](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-store-framework), follow these steps:

1. [Setup workspaces](#step-1---setting-up-workspaces)
2. [Develop and test](#step-2---developing-and-testing-your-storefront)
3. [Go live](#step-3---going-live)

>⚠️ Consider planning the entire go-live process at least two weeks in advance, as some of the steps below are time-sensitive.

### Step 1 - Setting up workspaces

[Workspaces](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace) are isolated environments, which means they can be understood as different versions of the same VTEX account.

To develop and test your store, we recommend that you create at least one [development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace) and one [production workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-production-workspace). But it may be a good idea to create more workspaces based on your development needs. Learn how to manage workspaces effectively in [Best practices on workspaces management](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspaces-best-practices).

>⚠️ Do not use subaccounts instead of [workspaces](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace). This can cause loss of Master Data information, including client profiles, and delays in project changes being displayed on the storefront due to cache unpredictability. It may even cause store downtime when going live with the new storefront.

#### Setting the Edition app

Once you have created your workspaces, [open a support ticket](https://help.vtex.com/en/support) requesting the installation of the `vtex.edition-store@3.x` or a more recent version of the [Edition app](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app) in the workspaces created previously. Do not forget to include the names of the workspaces you wish to use in this process.

To check which version of the Edition app is installed in a workspace, run the following command: `vtex edition get`. Learn about its different versions in the [Edition app](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app) guide.

>⚠️ Do not request the Edition change for the master workspace of your store. This will cause some features, such as My Account, to stop working properly.

### Step 2 - Developing and testing your storefront

At this point, it is up to your development team to plan and develop your store’s frontend experience. Check these guides to learn how to use VTEX IO to create amazing storefronts with [Store Framework](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-store-framework):

- [CMS IO basic concepts](https://help.vtex.com/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/4yB9wSl79cArd68aRBnBZ2)
- [Storefront implementation overview](https://developers.vtex.com/docs/guides/storefront-implementation)
- [Storefront apps overview](https://developers.vtex.com/docs/guides/store-framework-apps)
- [Building a Store Framework theme](https://developers.vtex.com/docs/guides/getting-started-3)

### Step 3 - Going live

Once you have developed and tested your new storefront and everything is ready in a production workspace, it is time to go live. This means seamlessly switching the storefront being displayed to shoppers at your store’s domain. Follow these steps to accomplish this task:

1. Promote the production workspace running your new storefront to master. Learn more about how to [promote a workspace to master](https://developers.vtex.com/docs/guides/vtex-io-documentation-promoting-a-workspace-to-master).
2. Request VTEX internal DNS pointing change for Store Framework via [support ticket](https://help.vtex.com/en/support). Use the ticket to schedule the change according to the information below at least three business days before your planned go-live date. This last step will cause your new storefront to go live.

When opening the ticket, keep in mind that you must:

- Request VTEX internal DNS pointing change only after you have promoted your production workspace to master.
- Make it clear that you wish to go live in the ticket title.
- Indicate a time from 9 a.m. to 5 p.m. (UTC-3) for the change to happen.
- Indicate whether your store has any [trade policy conditional rules](https://help.vtex.com/en/tutorial/criar-uma-politica-comercial--563tbcL0TYKEKeOY4IAgAE).
