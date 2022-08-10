---
title: "Form component"
slug: "trackfield-store-components-form"
excerpt: "trackfield.store-components@0.18.0"
hidden: true
createdAt: "2022-07-05T22:31:25.101Z"
updatedAt: "2022-08-04T10:48:21.271Z"
---
Form component with two input fields and a submit button for event registrations made in the store.

![Media Placeholder](https://gitlab.com/acct.global/program-04/track-and-field-io/trackandfield.store-components/uploads/d65890b0f25f943bee755a1ce20fcab9/image.png)

## Getting Started

1. Create an entity in Master Data (V1) with the `FE` acronym with the following fields:

| Name       | Type     |
| ---------- | -------- |
| `name`     | `string` |
| `email`    | `string` |
| `campaign` | `string` |

2. Add the `store-components` app to your theme's dependencies in the `manifest.json`, for example:

```diff
"dependencies": {
+  "trackfield.store-components": "0.x"
}
```

3. Now you can use the form component anywhere in your store

```json
{
  "form#landing-page": {
    "props": {
      "titleForm": "Garanta o seu lugar",
      "labelFullName": "Nome completo:",
      "labelEmail": "E-mail:",
      "buttonSubmit": "Reservar meu lugar",
      "horizontalAlign": "CENTER",
      "backgroundColor": "#f0e9e9"
    }
  }
}
```

# `Form` Props

| Prop name               | Type     | Description                                                 | Default value |
| ----------------------- | -------- | ----------------------------------------------------------- | ------------- |
| `titleForm`             | `string` | Title used for form component. Sample: "Garanta seu lugar". | `""`          |
| `labelFullName`         | `string` | name of the first input. Sample: "insira seu nome completo" | `""`          |
| `labelEmail`            | `string` | name of the second input. Sample: "insira seu e-mail"       | `""`          |
| `buttonSubmit`          | `string` | name of the button submit. Sample: "Reservar meu lugar"     | `""`          |
| `horizontalAlign`       | `string` | position of the component.                                  | `""`          |
| `backgroundColor`       | `string` | color for the background.                                   | `""`          |
| `descriptionSuccess`    | `string` | message of the success.                                     | `""`          |
| `colorTitle`            | `string` | color for the title.                                        | `""`          |
| `colorLabels`           | `string` | color for the label.                                        | `""`          |
| `colorButtonSubmit`     | `string` | color for the text button.                                  | `""`          |
| `backgroundColorButton` | `string` | color for the background button.                            | `""`          |
| `colorTitleSucess`      | `string` | color for the success title.                                | `""`          |
| `campaignField`         | `string` | name of the campaign. Sample: "Continue em movimento"       | `""`          |

## Customization

The first thing that should be present in this section is the sentence below, showing users the recipe pertaining to CSS customization in apps:

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

Thereafter, you should add a single column table with the available CSS handles for the app, like the one below. Note that the Handles must be ordered alphabetically.

| CSS Handles                 |
| --------------------------- |
| `form`                      |
| `form__button`              |
| `form__input`               |
| `form__label`               |
| `form__section`             |
| `form__title`               |
| `form_container__success`   |
| `form_description__success` |
| `form_error__message`       |