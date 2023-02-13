---
title: "Slider Layout"
slug: "vtex-slider-layout"
hidden: false
createdAt: "2020-06-03T15:19:47.985Z"
updatedAt: "2022-09-14T12:37:24.494Z"
---

Slider Layout is a flexible solution for building sliders of blocks within VTEX Store Framework, such as a carousel component.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-slider-layout-0.png)

> _In order to use the Slider Layout as a substitute to the [Carousel app](https://github.com/vtex-apps/carousel), check out the [Building a Carousel through lists and Slider Layout](https://developers.vtex.com/docs/guides/vtex-io-documentation-building-a-carousel-using-slider-layout) documentation._

## Integration with Google Analytics Enhanced Ecommerce

Slider layout also gives you the possibility to integrate your component with the [Google Analytics Enhanced Ecommerce feature](https://developers.google.com/analytics/devguides/collection/ua/gtm/enhanced-ecommerce). With this integration, you will be able to set up your promotion’s ID, name, and position on the [Site Editor](https://help.vtex.com/en/tutorial/site-editor-overview--299Dbeb9mFczUTyNQ9xPe1) to be shown on a Google Analytics dashboard.

To do so, you must go to your store’s Admin, click **Store Setup > CMS > Site Editor** and open the image configurations of the internal promotion you want to track. These configurations are displayed on the right side of the page.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-slider-layout-1.png)

> For more information about managing your page content, access [Managing page and template content](https://help.vtex.com/en/tutorial/managing-page-and-template-content--3tMbx6HXy4Fy5r9EhboG37).

With everything set up, Google Analytics is now able to track your internal promotions and generate reports of its views, clicks, click-through rate, conversions, and revenue.

## Configuration

1. Add the `slider-layout` app to your theme's dependencies in the `manifest.json` file:

```json
"dependencies": {
  "vtex.slider-layout": "0.x"
}
```

Now, you are able to use all blocks exported by the `slider-layout` app. Check out the full list below:

| Block name            | Description                                                                                                                                                                                                              |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `slider-layout`       | ![https://img.shields.io/badge/-Mandatory-red](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-slider-layout-2.png) Builds sliders of blocks for your store through its `children` list blocks. |
| `slider-layout-group` | Enables you to keep a group of `slider-layout` blocks in sync with each other. For more on this, check out the Advanced configurations section below.                                                                    |

2. Add the `slider-layout` block to your template. For example:

```json
  "slider-layout#text-test": {
    "props": {
      "itemsPerPage": {
        "desktop": 1,
        "tablet": 1,
        "phone": 1
      },
      "infinite": true,
      "showNavigationArrows": "desktopOnly",
      "blockClass": "carousel"
    },
    "children": ["rich-text#1", "rich-text#2", "rich-text#3"]
  },

  "rich-text#1": {
    "props": {
      "text": "Test1"
    }
  },
  "rich-text#2": {
    "props": {
      "text": "Test2"
    }
  },
  "rich-text#3": {
    "props": {
      "text": "Test3"
    }
  },
```

| Prop name              | Type                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Default value                          |
| ---------------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| `label`                | `string`            | `aria-label` attribute value to be used by the `<Slider/>` component when rendered. The `aria-label` value should explicitly tell users what the HTML element being inspected is responsible for.                                                                                                                                                                                                                                                                                                                                                                                                               | `slider`                               |
| `showNavigationArrows` | `enum`              | When navigation arrows should be rendered. Possible values are: `mobileOnly`, `desktopOnly`, `always`, or `never`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `always`                               |
| `showPaginationDots`   | `enum`              | When pagination dots should be rendered. Possible values are: `mobileOnly`, `desktopOnly`, `always`, or `never`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `always`                               |
| `infinite`             | `boolean`           | Whether the slider should be infinite (`true`) or not (`false`). When this prop is set as `false`, the slider will have an explicit end for users.                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `false`                                |
| `usePagination`        | `boolean`           | Whether the slider should use slide pages (`true`) or not (`false`). When this prop is set as `false`, the slider will use smooth scrolling for slide navigation instead of arrows.                                                                                                                                                                                                                                                                                                                                                                                                                             | `true`                                 |
| `itemsPerPage`         | `object`            | Number of slider items to be shown on each type of device. For more on this, check out the `itemsPerPage` object section below.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `{ desktop: 5, tablet: 3, phone: 1 }`  |
| `navigationStep`       | `number` / `enum`   | Number of slider items that should be displayed at a time when users click on one of the slider's arrows. It is also possible to set this prop value as `page`, meaning that the number of slider items to be displayed when one of the arrows is clicked on is equal to the number of slider items set per page (in the `itemsPerPage` prop).                                                                                                                                                                                                                                                                  | `page`                                 |
| `slideTransition`      | `object`            | Controls the transition animation between slides based on [CSS attributes](https://developer.mozilla.org/en-US/docs/Web/CSS/transition). For more on this, check out the `slideTransition` object section below.                                                                                                                                                                                                                                                                                                                                                                                                | `{ speed: 400, delay: 0, timing: '' }` |
| `autoplay`             | `object`            | Controls the autoplay feature behavior. For more on this, check out the `autoplay` object section below.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `undefined`                            |
| `fullWidth`            | `boolean`           | Whether the slides should occupy the full page width, making the arrows appear on top of them (`true`) or not (`false`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `true`                                 |
| `arrowSize`            | `number` / `object` | Slider arrows size (height and width) in pixels. This is a responsive prop, which means you can pass to it an object with different values for each breakpoint (`desktop`, `mobile`, `tablet`, and `phone`).                                                                                                                                                                                                                                                                                                                                                                                                    | `25`                                   |
| `centerMode`           | `enum` / `object`   | Defines the slider elements positioning on the screen. Possible values are: `center` (elements are centered, allowing users to see a peek of the previous and next slides), `to-the-left` (align elements to the left side, allowing users to see a peek of the next slide, but not the previous one), and `disabled` (disables the feature, rendering elements on the whole screen without taking a peek in the previous and next slides). Notice: This is a responsive prop, which means you can pass to it an object with different values for each breakpoint (`desktop`, `mobile`, `tablet`, and `phone`). | `disabled`                             |
| `centerModeSlidesGap`  | `number`            | Number of pixels between slides when `centerMode` is set to `center` or `to-the-left`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `undefined`                            |

- **`itemsPerPage` object**

| Prop name | Type     | Description                                      | Default value |
| --------- | -------- | ------------------------------------------------ | ------------- |
| `desktop` | `number` | Number of slides to be shown on desktop devices. | `5`           |
| `tablet`  | `number` | Number of slides to be shown on tablet devices.  | `3`           |
| `phone`   | `number` | Number of slides to be shown on phone devices.   | `1`           |

- **`slideTransition` object**

| Prop name | Type     | Description                                | Default value |
| --------- | -------- | ------------------------------------------ | ------------- |
| `speed`   | `number` | Transition speed (in `ms`).                | `400`         |
| `delay`   | `number` | Delay between slides transition (in `ms`). | `0`           |
| `timing`  | `string` | Timing function.                           | `''`          |

- **`autoplay` object**

| Prop name     | Type      | Description                                                                                     | Default value |
| ------------- | --------- | ----------------------------------------------------------------------------------------------- | ------------- |
| `timeout`     | `number`  | Timeout (in `ms`) between each slide.                                                           | `undefined`   |
| `stopOnHover` | `boolean` | Whether the auto play should stop when users are hovering the slider (`true`) or not (`false`). | `undefined`   |

## Advanced configurations

The `slider-layout-group` block is responsible for synchronizing the slides rendered by each one of the `slider-layout` blocks declared in it.

The `slider-layout-group` therefore does not render any specific component on your store's UI. In turn, it is a logical block that only expects to receive a `children` block list containing the desired `slider-layout` blocks to be rendered. For example:

```json
{
  "slider-layout-group#test": {
    "children": ["slider-layout#1", "slider-layout#2", "slider-layout#3"]
  }
}
```

Below, you can find a practical example using three `slider-layout` blocks inside of a `slider-layout-group`. Each of those `slider-layout`s received three `rich-text` blocks as `children` to serve as individual slides:

![slider-layout-group demo](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-slider-layout-3.gif)

> ⚠️ **\*All `slider-layout` blocks declared in the `slider-layout-group` must receive the same configuration, meaning the same props and values**. Due to implementation rules, they are only allowed to differ in their `children` block list. Notice the following: declaring `slider-layout` blocks with different configuration will result in unexpected behavior, leading to errors whose support is **not** granted by the VTEX Store Framework team.\*

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization).

| CSS Handles               |
| ------------------------- |
| `paginationDot--isActive` |
| `paginationDot`           |
| `paginationDotsContainer` |
| `slide--firstVisible`     |
| `slide--hidden`           |
| `slide--lastVisible`      |
| `slide--visible`          |
| `slideChildrenContainer`  |
| `slide`                   |
| `sliderArrows`            |
| `sliderLayoutContainer`   |
| `sliderLeftArrow`         |
| `sliderRightArrow`        |
| `sliderTrackContainer`    |
| `sliderTrack`             |
