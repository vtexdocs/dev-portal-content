---
title: "Sponsor Account"
slug: "vtex-io-documentation-sponsor-account"
hidden: false
createdAt: "2020-06-03T16:02:47.740Z"
updatedAt: "2022-12-13T20:17:44.643Z"
excerpt: "Learn what a Sponsor Account is and streamline the management of Edition Apps within your accounts ecosystem."
seeAlso:
  - "/docs/guides/vtex-io-documentation-edition-app"
  - "/docs/guides/vtex-io-documentation-becoming-a-sponsor-account"
---

A Sponsor Account is responsible for the development, maintenance, and distribution of [Edition Apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app). Its primary objective is to streamline the installation of multiple apps and configurations across a defined group of accounts. This is particularly valuable for organizations with hierarchical relationships among their accounts, such as the main VTEX account of a holding company or a brand with multiple sub-brands.

## Account hierarchy

The image below exemplifies the hierarchy among VTEX accounts.

![Accounts hierarchy](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-sponsor-account-0.png)

### The `vtex` account

At the top of this hierarchy is the `vtex` account, which assumes the role of a Sponsor Account for all other accounts on the VTEX platform. This is because the `vtex` account is responsible for the development and release of the two native Edition Apps that all others derive from:

- Edition Business (`vtex.edition-business@0.x`): Installs all the necessary apps to build a store with [Legacy CMS Portal](https://help.vtex.com/tutorial/o-que-e-o-cms--EmO8u2WBj2W4MUQCS8262).
- Edition Store (`vtex.edition-store@2.x`): Installs all the necessary apps to develop a store with the [Store Framework.](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-store-framework)

### Secondary Sponsor Accounts

In the second level of the account hierarchy, accounts that meet the [requirements to become a Sponsor Account](https://developers.vtex.com/docs/guides/vtex-io-documentation-becoming-a-sponsor-account) (e.g., `account2`) can release their own Edition App. These apps allow the Sponsor Account to enforce the installation of specific bundles of apps and settings in their child accounts (e.g., `account4`, `account5`, `account6`).

Becoming a Sponsor Account confers greater control over child accounts, ensuring that they adhere to the desired configuration and functionality standards. This flexibility is especially valuable for businesses with complex structures and unique requirements.

For more information on how to become a Sponsor Account, refer to the [Becoming a Sponsor Account](https://developers.vtex.com/docs/guides/vtex-io-documentation-becoming-a-sponsor-account) guide.
