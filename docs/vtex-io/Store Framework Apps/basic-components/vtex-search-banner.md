---
title: "Banner"
slug: "vtex-search-banner"
excerpt: "vtex.search@2.13.1"
hidden: false
createdAt: "2021-02-23T17:09:08.532Z"
updatedAt: "2022-07-07T20:18:50.885Z"
---
A simple banner with that can configured to appear depending on the context of the search.

## Configuration

The banner entity is composed by the following fields:

| Field                | Description                                                                                                      |
| -------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `Active`             | Indicates if banner is active or not.                                                                            |
| `Banner name`        | Field used as an id.                                                                                             |
| `Type banner`        | Indicates the banner type. It can be `HTML` or `IMAGE`.                                                          |
| `HTML` / `Image URL` | Html or image to be inserted.                                                                                    |
| `Area`               | Indicates which area the banner should appear. It is importante when there is multiple banners in the same page. |
| `Terms`              | List of terms for this banner.                                                                                   |
| `Period`             | The period that this banner will be active.                                                                      |
| `Attributes`         | List of selected attributes for this banner.                                                                     |

## Usage

Add the `search-banner` block to the `search-result-layout.desktop` or `search-result-layout.mobile`. For example:

```json
{
  "search-result-layout.desktop": {
    "children": [
      "flex-layout.row#banner-one"
    ]
  },
  "search-banner#one": {
    "props": {
      "area": "one",
      "blockClass": "myBanner",
      "horizontalAlignment": "center"
    }
  },
  "flex-layout.row#banner-one": {
    "children": [
      "search-banner#one"
    ]
  }
}
```

## Props

| Prop name             | Type     | Description                                                             | Default value |
| --------------------- | -------- | ----------------------------------------------------------------------- | ------------- |
| `area`                | `String` | Idicates the area. It needs to match the area configured in the banner. | -             |
| `blockClass`          | `String` | Defines a custom class for the banner div.                              | -             |
| `horizontalAlignment` | `String` | Defines the horizontal alignment for the banner.                        | `"center"`    |

The possible values for `horizontalAlignment` are:
| Values |
| --------- |
| `"left"` |
| `"right"` |
| `"center"`|

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles    |
| -------------- |
| `searchBanner` |