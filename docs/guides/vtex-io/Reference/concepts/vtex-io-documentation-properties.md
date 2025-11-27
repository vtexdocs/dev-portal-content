---
title: "Properties"
slug: "vtex-io-documentation-properties"
hidden: false
createdAt: "2020-11-23T13:33:26.418Z"
updatedAt: "2022-12-13T20:17:44.194Z"
excerpt: "Learn what properties (props) are in VTEX IO, how they work, and the data types you can use to customize blocks in the Store Framework."
---

A property is defined by a JSON (JavaScript Object Notation) object. A JSON object consists of a set of key-value pairs enclosed in curly braces (`{}`). Each key paired with its corresponding value forms a property, which represents a characteristic of that object. Consider the following JSON object:

```json
{
 "name": "Pedro",
 "height": 1.90
}
```

In this example, `name` and `height` are the property keys, and `"Pedro"` and `1.90` are their respective values.

> ℹ️ The key and value can also be called property name and property value, respectively.

## Properties in React and Store Framework

In the context of VTEX IO, properties (commonly referred to as `props`) are used to configure the behavior and appearance of [blocks](https://developers.vtex.com/docs/guides/vtex-io-documentation-4-declaring-a-theme-block) within the [Store Framework](https://developers.vtex.com/docs/guides/store-framework). The `props` configured for a `block` in a [Store Theme](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-theme) determine how the component is rendered in the user interface. The more `props` a block supports, the more flexible and customizable it becomes.

## Property types

The value of a property can be one of several data types. The following table describes the most common types used for block properties in VTEX IO.

| Type      | Value Format                                                                                              | Example                                                                                             |
| --------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `string`  | A text value enclosed in double quotes (`""`).                                                            | `"Hello, World!"`                                                                                   |
| `number`  | An integer or a floating-point number. Do not use quotes.                                                 | `10` or `23.45`                                                                                     |
| `boolean` | A logical value, which must be either `true` or `false`. Do not use quotes.                               | `true`                                                                                              |
| `object`  | A collection of key-value pairs enclosed in curly braces (`{}`).                                          | `{ "fontSize": 16, "fontWeight": "bold" }`                                                          |
| `array`   | An ordered list of values of the same data type, enclosed in square brackets (`[]`).                      | `["image1.jpg", "image2.jpg"]`                                                                      |
| `enum`    | A value from a predefined list of options, enclosed in double quotes (`""`).                              | `"horizontal"` or `"vertical"`                                                                      |
| `block`   | The name of another block to be rendered, enabling component [composition](https://developers.vtex.com/docs/guides/vtex-io-documentation-composition).                          | `"icon-cart#header"` (from the [Store Icons](https://developers.vtex.com/docs/guides/vtex-store-icons) app) |
