---
title: "Checking an app's bundle size"
slug: "how-to-check-an-apps-bundle-size-on-vtex-io"
hidden: true
createdAt: "2020-10-08T13:49:14.081Z"
updatedAt: "2021-04-07T18:24:29.765Z"
---
If you are building a custom react component, you can get a glimpse on the performance of your app by taking a look at the bundle size. 

## For apps in development mode (`vtex link`)
Access: https://{workspace}--{account}.myvtex.com/_v/private/assets/v1/linked/{app}@{version}/public/react/devReport.html

## For apps in production
Access: https://{workspace}--{account}.myvtex.com/_v/public/assets/v1/published/{app}@{version}/public/react/[prod|dev]Report.html

Here is an example of the result:
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/vtex-io/Storefront%20Guides/boosting-performance/b80fe93-bundle.png)