---
title: "[Deprecating] Admin Example"
slug: "novicompu-app-stores"
excerpt: "novicompu.app-stores@1.0.0"
hidden: true
createdAt: "2022-07-07T05:43:46.424Z"
updatedAt: "2022-07-07T05:43:46.424Z"
---
_We're working on our new design system. Please get in touch if you are part of VTEX product team and working on an admin app. If you are external to VTEX you can still use this repo._

An example admin app that adds a menu button to the admin sidebar and a navigation via parameter example.

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