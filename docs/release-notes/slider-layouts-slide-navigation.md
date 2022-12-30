---
slug: "slider-layouts-slide-navigation"
title: "Slider Layout's slide navigation"
createdAt: 2020-07-31T14:04:00.000Z
hidden: false
type: "fixed"
---

![Store Framework](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/slider-layouts-slide-navigation-0.png)

The [Slider Layout app](https://vtex.io/docs/components/all/vtex.slider-layout/) has gone through fundamental changes in order to improve its usability and therefore the user experience on it.

Previously, the component was showing two main issues related to its slide navigation:

- Mobile delay - Mobile users were facing a delay when sliding through products using the touch instead of the arrow buttons.
- Rewind effect - Due to the lack of an infinite scroll feature, the component was presenting a rewind effect, taking users to the *first* listed product when the *last* one was displayed. This sense of *first* and *last*  products blocked users from performing smooth browsing between slides.

With this release, both issues were addressed and fixed. Now, the Slider Layout automatically works with a smooth slide transition (infinite scroll effect) and also quickly responds to user interaction on mobile devices.
