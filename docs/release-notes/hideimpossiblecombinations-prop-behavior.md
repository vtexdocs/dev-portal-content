---
slug: "hideimpossiblecombinations-prop-behavior"
title: "hideImpossibleCombinations prop behavior"
createdAt: 2020-07-20T20:09:00.000Z
hidden: false
type: "fixed"
---

![Store Framework](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/hideimpossiblecombinations-prop-behavior-0.png)

Before this fix, [SKU Selector](https://vtex.io/docs/components/all/vtex.store-components/sku-selector/)'s `hideImpossibleCombinations` prop was not properly hiding impossible specifications (specifications that can't be chosen according to the filter previously selected) when defined as `true` in certain scenarios. 

In addition to that, when the prop value was  `false`, impossible specifications were not being displayed by the component in an intuitive way. Instead, their names were shown in a grey color, confusing users about the specification availability.

These behaviors are now fixed and the prop is working as expected, improving user experience when using the SKU Selector component. 

:information-source: *Check out this [link](https://www.loom.com/share/2f11b9f6ae6c4bcf9f23380d3f8bf9eb) to watch a practical demonstration of the error.*