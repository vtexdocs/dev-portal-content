---
title: Stack Layout
excerpt: "Components overlapping other components. If this seems like something difficult, that's because you're unfamiliar with Stack Layout."
createdAt: "2019-11-10T14:47:00.000Z"
type: 'info'
---
The Stack Layout component allows display blocks to stack on top of others in a easy way.

![stack-layout](https://user-images.githubusercontent.com/52087100/66655794-1c02f380-ec13-11e9-9120-c1390d8d0df2.png)
_Example of blocks using the Stack Layout_. 

## What has changed

Prior to this release, the only way to display blocks on top of others was to set each block's individual `zIndex` value.  

> ℹ️ The `z-index` is a property in CSS that controls the vertical stacking order of elements that overlap.

Now, each child declared in the `stack-layout` block will automatically receive a proportional value of `zIndex`. Therefore, the block will control the position of elements that overlap. 

## Main advantages

Differently from other layout components, which only considers the component's width and length for its position, Stack Layout **simplifies the layout construction** process in **3D** for elements that overlap.

## What you need to do

Make sure your store has the `stack-layout` [installed](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app). 

:eyes: Do not forget to check out the app [documentation](https://vtex.io/docs/app/vtex.stack-layout) for more details on its implementation.
