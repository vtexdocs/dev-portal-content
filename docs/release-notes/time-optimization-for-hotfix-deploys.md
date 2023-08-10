---
slug: "time-optimization-for-hotfix-deploys"
title: "Time optimization for hotfix deploys"
createdAt: 2020-11-25T20:17:01.002Z
hidden: false
type: "improved"
---

![App Development](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/time-optimization-for-hotfix-deploys-0.png)

The VTEX IO team has finally made it possible to warp time exactly as those kids from Dark did in order to deploy your hotfixes in less than 7 minutes!

Using the VTEX IO CLI's `2.118.0` version or newer, you can now run `vtex deploy --force` in your terminal when needed.

>⚠️ The `--force` flag is only recommended for hotfixes! Normal deploys should use the `vtex deploy` as usual, since the 7 minutes are fundamental for testing your store's performance.
