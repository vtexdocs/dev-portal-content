---
slug: "custom-data-info-on-order-graphql"
title: "Back button as modal close button"
createdAt: 2020-07-08T14:13:00.000Z
hidden: false
type: "removed"
---

![Store Framework](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/custom-data-info-on-order-graphql-0.png)

The browser's Back button no longer works as a modal closing button when configuring the [Modal Layout app](https://vtex.io/docs/components/all/vtex.modal-layout/).  

Previously, it was possible to close the Modal component using the browser's Back button. This feature was extremely useful for users from mobile devices since the modal opened in them works as a brand new page.

In the meantime, this feature was leading users to a poor experience when using desktop devices since the Back button wasn't working as it should. Instead, it only closed modals (if any on the page).  

In order to improve the website navigation, this feature was removed meaning that the Modal Layout now depends on its own button in order to be properly closed.
