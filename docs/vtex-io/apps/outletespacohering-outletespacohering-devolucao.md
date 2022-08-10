---
title: "[ WORK IN PROGRESS ] Admin Example"
slug: "outletespacohering-outletespacohering-devolucao"
excerpt: "outletespacohering.outletespacohering-devolucao@0.10.12"
hidden: true
createdAt: "2022-07-04T21:05:24.191Z"
updatedAt: "2022-07-25T16:25:40.448Z"
---
An example admin app that adds a menu button to the admin sidebar.

# PREVIEW NOTICE :construction:

We're working on the **admin builder**, which will allow you to define two files: `admin/routes.json` file with everything you need to create an admin interface (routes paths and components), and `admin/navigation.json` which alows your admin app to insert itself in the sidebar navigation. This is a temporary example!

### How to develop admins

1. Admins always declare routes in `/admin/app/<route>`

2. Declare the `admin` builder in your manifest

3. When installed, the user navigates to `/admin/<route>`, but your app runs in an iframe that points to `/admin/app/<route>`.

4. You can develop directly in the `/admin/app` route for convenience, but don't forget to test it inside the iframe. :)


### Quickstart

1. Clone this repo

2. `yarn --cwd react/` for code completion

3. `vtex link`

4. Navigate to `workspace--account.myvtex.com/admin/app/example`