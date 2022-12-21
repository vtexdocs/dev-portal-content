---
slug: "title-attribute-in-image-components"
title: "Title attribute in image components"
createdAt: 2020-09-02T14:55:00.000Z
hidden: false
type: "fixed"
---

![Store Framework](https://img.shields.io/badge/-Store%20Framework-red)

The title attribute was missing in store images due to the fact it was linked to the incorrect HTML element when the components were rendered - `a` instead of `img`.

This behavior is now [fixed](https://github.com/vtex-apps/store-image/pull/24) and the title attribute can be properly found and tracked.