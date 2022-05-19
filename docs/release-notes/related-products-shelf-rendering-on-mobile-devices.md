---
slug: "related-products-shelf-rendering-on-mobile-devices"
title: "Related Products Shelf rendering on mobile devices"
createdAt: 2020-07-09T11:57:00.000Z
hidden: false
type: "fixed"
---

![https://img.shields.io/badge/-VTEX%20Store%20Framework-red](https://img.shields.io/badge/-VTEX%20Store%20Framework-red)

Due to an implementation detail in the `isMobile` prop, the Related Products Shelf component was only being rendered in its desktop mode, even when displayed on mobile devices. 

This undesirable behavior is now [fixed](https://github.com/vtex-apps/shelf/pull/227) and the Related Products Shelf is working for mobile users as expected.

:sparkles: *We would not be able to deliver this amazing result if it was not for [Sahan Jayawardana](https://github.com/sahanljc) from Clouda Inc! Our sincere thanks, Sahan!*