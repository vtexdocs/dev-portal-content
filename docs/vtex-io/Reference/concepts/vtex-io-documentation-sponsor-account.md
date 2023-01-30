---
title: "Sponsor Account"
slug: "vtex-io-documentation-sponsor-account"
hidden: false
createdAt: "2020-06-03T16:02:47.740Z"
updatedAt: "2022-12-13T20:17:44.643Z"
---

A Sponsor Account is responsible for developing, maintaining, and distributing the [**Edition App**](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app) installed in its child accounts.

Having a specific Sponsor Account is convenient for accounts that keep a hierarchical relationship with others, such as the main VTEX account of a holding or a brand with many sub-brands.

The image below exemplifies the hierarchy among VTEX accounts.

![Accounts hierarchy](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-sponsor-account-0.png)

Notice that the `vtex` account sponsors all the other accounts of the VTEX platform. That's because the `vtex` account is responsible for the development and release of the two standard Edition Apps, which all others derive from:

- *Edition Business* (`vtex.edition-business@0.x`): installs all the necessary apps to build a store with VTEX [legacy CMS.](https://help.vtex.com/tutorial/o-que-e-o-cms--EmO8u2WBj2W4MUQCS8262)

- *Edition Store* (`vtex.edition-store@2.x`): installs all the necessary apps to develop a store with the [Store Framework.](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-store-framework)

In the second level of this hierarchy, accounts that meet the [requirements to become a Sponsor Account](https://developers.vtex.com/docs/guides/vtex-io-documentation-becoming-a-sponsor-account) (e.g., `account2`) can release their own Edition App. That means this account can enforce the installation of a specific bundle of apps and settings in their child accounts (e.g., `account4`, `account5`, `account6`) through their particular Edition App.

For more information, check our documentation on [becoming a Sponsor Account](https://developers.vtex.com/docs/guides/vtex-io-documentation-becoming-a-sponsor-account).
