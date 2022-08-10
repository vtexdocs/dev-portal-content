---
title: "Banner"
slug: "gregory-search-banner"
excerpt: "gregory.search@2.9.1"
hidden: true
createdAt: "2022-08-05T14:52:00.354Z"
updatedAt: "2022-08-05T14:52:00.354Z"
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