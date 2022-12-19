---
title: "Flex Layout"
slug: "vtex-flex-layout"
excerpt: "vtex.flex-layout@0.20.1"
hidden: false
createdAt: "2020-06-03T15:19:18.642Z"
updatedAt: "2022-09-01T17:03:52.331Z"
---
Flex Layout is a **layout structure** built within VTEX IO store framework. It allows the construction of complex custom layouts using the concept of **rows** and **columns**, setting the desired structure and positioning of blocks in a given page.

![Screen Shot 2019-08-21 at 4 05 19 PM](https://user-images.githubusercontent.com/27777263/63467270-736abb80-c43b-11e9-8a7b-dfe8f218f081.png)
_Example of a page layout built using Flex Layout, following the one row with two columns model_

## Configuration

There are **two basic building blocks of Flex Layout**: the `flex-layout.row` and the `flex-layout.col`. You should **never** use `flex-layout`.

If you are already familiar with the [`flexbox`](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) layout used in CSS, Flex Layout should be easy to get a grasp since that's what being used by `flex-layout.row` and `flex-layout.col` under the hood.

You can use **any** array of blocks as `flex-layout.row` and `flex-layout.col` children.

The props below support [`responsive-values`](https://github.com/vtex-apps/responsive-values), meaning that you can define to the same prop different values based on each device's screen size, such as mobile and desktop.

### `flex-layout.row`

| Prop name                  | Type                              | Description                                                                                                             | Default value |
| -------------------------- | --------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------- |
| `blockClass`               | `String`                          | Block container class. This prop’s set value functions as a block identifier for CSS customizations. (                  | `""`          |
| `borderColor`              | `String`                          | The color of the border.                                                                                                | `undefined`   |
| `borderWidth`              | `0...5`                           | A `number` or `string` magnitude for the `bw` Tachyons token to be applied to the row.                                  | `undefined`   |
| `border`                   | `String \| String[]`              | An array to define in which sides of the row a border should be applied to (`top`, `right`, `bottom`, `left` or `all`). | `undefined`   |
| `colGap`                   | `0...10`                          | A `number` or `string` magnitude for the `pr` Tachyons token to be applied to columns inside of the `flex-layout.row`.  | `undefined`   |
| `colSizing`                | `equal`&#124;`auto`               | Controls the width of the columns inside the `flex-layout.row`.                                                         | `equal`       |
| `fullWidth`                | `Boolean`                         | Whether or not the component should ocuppy all the available width from its parent.                                     | `false`       |
| `horizontalAlign`          | `left`&#124;`right`&#124;`center`&#124;`between`&#124;`around` | Controls horizontal alignment for the items inside the `flex-layout.row`.   It defaults to `between` if `colSizing` is `auto` and to `left` otherwise.                                             | `left`        |
| `colJustify`               | `enum` | Controls the space between columns and borders of the `flex-layout.row`, according to the `justify-content` CSS property. Possible values are `between` (adding no space between borders and columns) and `around` (adding the space). | `between` |
| `marginBottom`             | `0...10`                          | A `number` or `string` magnitude for the `mb` Tachyons token to be applied to the row.                                  | `undefined`   |
| `marginTop`                | `0...10`                          | A `number` or `string` magnitude for the `mt` Tachyons token to be applied to the row.                                  | `undefined`   |
| `paddingBottom`            | `0...10`                          | A `number` or `string` magnitude for the `pb` Tachyons token to be applied to the row.                                  | `undefined`   |
| `paddingTop`               | `0...10`                          | A `number` or `string` magnitude for the `pt` Tachyons token to be applied to the row.                                  | `undefined`   |
| `preserveLayoutOnMobile`   | `Boolean`                         | Whether or not the `flex-layout.row` should break into a column layout on mobile.                                       | `false`       |
| `preventHorizontalStretch` | `Boolean`                         | Prevents the row from stretching horizontally to fill its parent width.                                                 | `false`       |
| `preventVerticalStretch`   | `Boolean`                         | Prevents the row from stretching vertically to fill its parent height with `items-stretch` token.                       | `false`       |
| `rowGap`                   | `0...10`                          | A `number` or `string` magnitude for the `pb` Tachyons token to be applied to columns inside of the `flex-layout.row`.  | `undefined`   |
| `htmlId`                   | `String`                          | This prop adds an html id on `flexRow` and it can be changed from Site Editor. This enables the possibility to access a section from page using links.                                                                                | `undefined`   |
### `flex-layout.col`

| Prop name                | Type                              | Description                                                                                                                | Default value |
| ------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `blockClass`             | `String`                          | Block container class. This prop’s set value functions as a block identifier for CSS customizations                        | `""`          |
| `borderColor`            | `String`                          | The color of the border.                                                                                                   | `undefined`   |
| `borderWidth`            | `0...5`                           | A `number` or `string` magnitude for the `bw` Tachyons token to be applied to the column.                                  | `undefined`   |
| `border`                 | `String \| String[]`              | An array to define in which sides of the row a border should be applied to (`top`, `right`, `bottom`, `left` or `all`).    | `undefined`   |
| `horizontalAlign`        | `left`&#124;`right`&#124;`center` | Controls horizontal alignment for the items inside the `flex-layout.col`.                                                  | `left`        |
| `marginLeft`             | `0...10`                          | A `number` or `string` magnitude for the `ml` Tachyons token to be applied to the column.                                  | `undefined`   |
| `marginRight`            | `0...10`                          | A `number` or `string` magnitude for the `mr` Tachyons token to be applied to the column.                                  | `undefined`   |
| `paddingLeft`            | `0...10`                          | A `number` or `string` magnitude for the `pl` Tachyons token to be applied to the column.                                  | `undefined`   |
| `paddingRight`           | `0...10`                          | A `number` or `string` magnitude for the `pr` Tachyons token to be applied to the column.                                  | `undefined`   |
| `preventVerticalStretch` | `Boolean`                         | Prevents the row from stretching vertically to fill its parent height with `height: 100%`, using `height: "auto"` instead. | `false`       |
| `rowGap`                 | `0...10`                          | A `number` or `string` magnitude for the `pb` Tachyons token to be applied to rows inside of the `flex-layout.col`.        | `undefined`   |
| `verticalAlign`          | `top`&#124;`middle`&#124;`bottom` | Controls vertical alignment for the items inside the `flex-layout.col`.                                                    | `top`         |
| `width`                  | `"0...100%"`&#124;`"grow"`        | Sets the width of the column. Accepts either a percentage or `"grow"`.                                                     | `undefined`   |

## Modus Operandi

- The highest level in a Flex Layout is **always** made of a row. Therefore, it is only possible to add a `flex-layout.col` inside of a `flex-layout.row` - never as a first-level block.
- Each row and column can have as **many levels as needed**.
- When creating levels, it is necessary to **alternate between rows and columns**. Within a row, you can only place columns, and within columns, only rows.
- Be mindful about the structure that you set in your flex layout does not only affect your code organization, but also reflects in the way that blocks will be shown and managed through the Site Editor admin. Therefore, it is always important to **take the organization of both code and Site Editor into account when planning to apply the Flex Layout** onto a page.

To better understand Flex Layout's practical operation, you can access the recipe on [Using Flex Layout](https://vtex.io/docs/recipes/templates/using-flex-layout/)

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles      |
| ---------------- |
| `flexColChild`   |
| `flexCol`        |
| `flexRowContent` |
| `flexRow`        |

## Contributors ✨

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!