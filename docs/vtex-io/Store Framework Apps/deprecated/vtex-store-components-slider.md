---
title: "Slider"
slug: "vtex-store-components-slider"
excerpt: "vtex.store-components@3.132.2"
hidden: false
createdAt: "2020-06-03T16:04:30.371Z"
updatedAt: "2021-12-30T14:00:48.284Z"
---
![https://img.shields.io/badge/-Deprecated-red](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-store-components-slider-0.png)

>⚠️ **Warning**
>
> **The Slider component has been deprecated in favor of the [Slider Layout](https://developers.vtex.com/vtex-developer-docs/docs/vtex-slider-layout) app**. Although support for this component is still given, it's strongly recommended that you update your store theme with the Slider Layout's blocks in order to keep up with the component's evolution.

`Slider` is a VTEX component that allows to show a collection of children components through a slide. To accomplish that, an external library called [react-slick](https://github.com/akiran/react-slick) is used.
This component can be imported and used by any VTEX app.

## Usage

You should follow the usage instruction in the main [README](/README.md#usage).

To import it into your code: 
```js
import { Slider } from 'vtex.store-components'
```

You can use it in your code like a React component with the jsx tag: `<Slider>`. 
```jsx
<Slider
  ssrFallback={this.ssrFallback()}
  sliderSettings={sliderSettings}
  scrollByPage={isScrollByPage}
  defaultItemWidth={DEFAULT_SHELF_ITEM_WIDTH + gap}
>
  {...}
</Slider>
```

#### Configuration

Through the Storefront, you can change the `Slider`'s behavior and interface. However, you also can make in your theme app, as Store theme does.

| Prop name | Type | Description |
| --------- | ---- | ----------- |
| `sliderSettings` | `Settings` | The slider settings |
| `adaptToScreen` | `Boolean` | Makes the items per page to adapt by the slider width |
| `defaultItemWidth` | `Number` | Default item width, it's necessary when the adaptToScreen is true | 
| `scrollByPage` | `Boolean` | If the scroll of items is by page or not |
| `leftArrowClasses` | `String` | Left arrow custom classes |
| `rightArrowClasses` | `String` | Right arrow custom classes |
| `dotsClasses` | `String` | Dots custom classes | 
| `children` | `Node!` | Array of items to be rendered inside the slider |

Settings:

For more information on the slider settings, [access](https://react-slick.neostack.com/) the official documentation og the react-slick library.

### Styles API
You should follow the Styles API instruction in the main [README](/README.md#styles-api).

#### CSS Namespaces
Below, we describe the namespace that are defined in the `Slider`.

| Class name | Description | Component Source |
| ---------- | ----------- | ---------------- |
| `arrowRight` | The right arrow of the slider | [index](/react/components/Slider/index.js) |
| `arrowLeft` | The left arrow of the slider | [index](/react/components/Slider/index.js) |
| `dots` | The slider dots | [index](/react/components/Slider/index.js) |