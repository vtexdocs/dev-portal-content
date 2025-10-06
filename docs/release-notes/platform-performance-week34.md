---
title: Platform performance
excerpt: "Understand last week's VTEX IO performance improvement key points."
createdAt: "2019-08-29T14:47:00.000Z"
type: 'info'
---
Check out our latest releases on promoting an  **optimal VTEX IO infra performance**, ensuring a better, faster and more stable platform experience:

> No action for the releases below is warranted on your side. The performance improvement is already available to all VTEX IO users!

##  Decrease in latency for pages that use GraphQL

Previously, any product, category and search page needed to perform a special GraphQL query to find the rendered IDs for products, brands and categories, even if the IDs would not be needed. 

Now, this query is only performed when some content related to an ID is actually rendered onto these pages. In addition to optimizing IO's infrastructure, this improvement drastically reduces the time a user takes to access a page.

![](https://user-images.githubusercontent.com/52087100/63978326-79404c80-ca8c-11e9-8623-5393f852c8f9.png)

---

## Decrease in JavaScript bundle size

All comments on code and JavaScript assets source maps were removed from production workspaces. This release reduces the size of the assets used by these workspace to bytes, thereby improving their performance as well.

> ℹ️ Source maps are JSON files that map a workspace's minified code, creating source code references for the number of lines, variable names and functions, and etc., which means for the original non-minified code. In short, these are mapping formats commonly used to help with debugging an app.
