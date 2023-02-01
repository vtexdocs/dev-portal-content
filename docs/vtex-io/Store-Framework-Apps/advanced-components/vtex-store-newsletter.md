---
title: "Store Newsletter"
slug: "vtex-store-newsletter"
hidden: false
createdAt: "2020-10-30T13:37:40.344Z"
updatedAt: "2021-03-25T19:36:37.526Z"
---

The Store Newsletter app provides a set of blocks that you can use to create a newsletter subscription form.

![newsletter-demo](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-store-newsletter-0.png)

## Configuration

1. Add `vtex.store-newsletter` to your app's dependencies in the `manifest.json` file:

```diff
 "dependencies": {
+  "vtex.store-newsletter": "1.x"
 }
```

Now, you are able to use all blocks exported by the `store-newsletter` app. Check out the full list below:

| Block name                         | Description                                                                                                          |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `newsletter-form`                  | ![mandatory](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-store-newsletter-1.png) Top level block that provides context to all its children. |
| `newsletter-input-email`           | ![mandatory](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-store-newsletter-2.png) Renders an email input in the newsletter form.             |
| `newsletter-input-name`            | Renders an name input in the newsletter form.                                                                        |
| `newsletter-input-phone`           | Renders an phone input in the newsletter form.                                                                       |
| `newsletter-checkbox-confirmation` | Renders a confirmation checkbox in the newsletter form.                                                              |
| `newsletter-hidden-field`          | Doesn't render anything, but enables hidden fields on the form to fetch custom data and save them in the store's [Master Data](https://help.vtex.com/en/tutorial/what-is-master-data--4otjBnR27u4WUIciQsmkAw) whenever a user subscribes to the newsletter. |
| `newsletter-submit`                | ![mandatory](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-store-newsletter-3.png) Renders a `Submit` button for the newsletter form.         |

2. In the desired store template, such as the `store.home`, add the `newsletter-form` block and its desired children:

```json
{
  "store.home": {
    "children": ["newsletter-form"]
  },

  "newsletter-form": {
    "children": [
      "newsletter-input-email",
      "newsletter-input-name",
      "newsletter-submit"
    ]
  }
}
```

### `newsletter-form` props

| Prop name      | Type               | Description                                                                                                                                                                                                                                                         | Default value |
| -------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `ErrorState`   | `block`            | Block to be rendered if the submission of the form fails. If none is passed, a default error component will be rendered.                                                                                                                                            | `undefined`   |
| `SuccessState` | `block`            | Block to be rendered if form submission succeeds. If none is passed, a default success component will be rendered.                                                                                                                                                  | `undefined`   |
| `LoadingState` | `block`            | Block to be rendered while the form submission is loading. If none is passed, the default behavior is for the submit button to show a spinner during this loading period.                                                                                           | `undefined`   |
| `classes`      | `CustomCSSClasses` | Used to override default CSS handles. To better understand how this prop works, we recommend reading about it [here](https://github.com/vtex-apps/css-handles#usecustomclasses). Note that this is only useful if you're importing this block as a React component. | `undefined`   |

### `newsletter-input-email` props

| Prop name         | Type               | Description                                                                                                                                                                                                                                                         | Default value                                                            |
| ----------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `placeholderText` | `string`           | Placeholder text for the email input.                                                                                                                                                                                                                               | `Enter your email address` (translated according to the store's locale). |
| `inputLabel`      | `string`           | Label for the email input.                                                                                                                                                                                                                                          | `null`                                                                   |
| `errorMessage`    | `string`           | Error message to be shown if email is invalid.                                                                                                                                                                                                                      | `Invalid email address` (translated according to the store's locale).    |
| `classes`         | `CustomCSSClasses` | Used to override default CSS handles. To better understand how this prop works, we recommend reading about it [here](https://github.com/vtex-apps/css-handles#usecustomclasses). Note that this is only useful if you're importing this block as a React component. | `undefined`                                                              |

### `newsletter-input-name` props

| Prop name         | Type               | Description                                                                                                                                                                                                                                                         | Default value                                                   |
| ----------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| `placeholderText` | `string`           | Placeholder text for name input.                                                                                                                                                                                                                                    | `Enter your name` (translated according to the store's locale). |
| `inputLabel`      | `string`           | Label for the name input.                                                                                                                                                                                                                                           | `null`                                                          |
| `errorMessage`    | `string`           | Error message to be shown if name input is empty.                                                                                                                                                                                                                   | `Invalid name` (translated according to the store's locale).    |
| `classes`         | `CustomCSSClasses` | Used to override default CSS handles. To better understand how this prop works, we recommend reading about it [here](https://github.com/vtex-apps/css-handles#usecustomclasses). Note that this is only useful if you're importing this block as a React component. | `undefined`                                                     |

### `newsletter-input-phone` props

| Prop name         | Type               | Description                                                                                                                                                                                                                                                         | Default value                                                    |
| ----------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| `placeholderText` | `string`           | Placeholder text for phone input.                                                                                                                                                                                                                                   | `Enter your phone` (translated according to the store's locale). |
| `inputLabel`      | `string`           | Label for the phone input.                                                                                                                                                                                                                                          | `null`                                                           |
| `errorMessage`    | `string`           | Error message to be shown if phone input is empty.                                                                                                                                                                                                                  | `Invalid phone` (translated according to the store's locale).    |
| `classes`         | `CustomCSSClasses` | Used to override default CSS handles. To better understand how this prop works, we recommend reading about it [here](https://github.com/vtex-apps/css-handles#usecustomclasses). Note that this is only useful if you're importing this block as a React component. | `undefined`                                                      |

### `newsletter-checkbox-confirmation` props

| Prop name       | Type     | Description                                                                                                                                                                                                                          | Default value                                                                        |
| --------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `checkboxLabel` | `string` | Label for the confirmation checkbox. This prop supports the [ICU Message Format](https://format-message.github.io/icu-message-format-for-translators/), exposing two variables for you to interpolate: `firstLink` and `secondLink`. | `I agree to received this newsletter.` (translated according to the store's locale). |
| `firstLabelLink`     | `Object` | Configures the `firstLink` variable to be interpolated by the text passed to `checkboxLabel`. checkbox.                                                                                                                              | `undefined`.                                                                         |
| `secondLabelLink`    | `Object` | Configures the `secondLink` variable to be interpolated by the text passed to `checkboxLabel`. checkbox.                                                                                                                             | `undefined`                                                                          |
| `classes`         | `CustomCSSClasses` | Used to override default CSS handles. To better understand how this prop works, we recommend reading about it [here](https://github.com/vtex-apps/css-handles#usecustomclasses). Note that this is only useful if you're importing this block as a React component.                                      | `undefined`           |

- `firstLabelLink` and `secondLabelLink` objects:

| Prop name | Type     | Description                 | Default value |
| --------- | -------- | --------------------------- | ------------- |
| `url`     | `string` | The link's URL.             | `undefined`   |
| `text`    | `string` | Text displayed on the link. | `undefined`   |

### `newsletter-hidden-field` props

| Prop name | Type     | Description                 | Default value |
| --------- | -------- | --------------------------- | ------------- |
| `dynamicFields` | `[enum]` | Desired hidden fields responsible for saving the user's custom data on [Master Data](https://help.vtex.com/en/tutorial/what-is-master-data--4otjBnR27u4WUIciQsmkAw) once the newsletter form is submitted. Notice that the name of the fields must be written in an array and represent which user data they save. Possible values are: `bindingUrl` and `bindingId`. *Caution*: To properly save the data, you must also [create the desired filters](https://help.vtex.com/en/tutorial/how-can-i-create-a-field-in-master-data--frequentlyAskedQuestions_1829) in the Master Data's `Client` entity.  | `undefined` |

### `newsletter-submit` props

| Prop name           | Type     | Description                          | Default value                                             |
| ------------------- | -------- | ------------------------------------ | --------------------------------------------------------- |
| `submitButtonLabel` | `string` | Text displayed on the submit button. | `Subscribe` (translated according to the store's locale). |
| `classes`         | `CustomCSSClasses` | Used to override default CSS handles. To better understand how this prop works, we recommend reading about it [here](https://github.com/vtex-apps/css-handles#usecustomclasses). Note that this is only useful if you're importing this block as a React component.                                      | `undefined`           |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles                     |
| ------------------------------- |
| `confirmationCheckboxContainer` |
| `confirmationCheckboxLabel`     |
| `defaultErrorMessage`           |
| `defaultSuccessMessage`         |
| `emailInputContainer`           |
| `emailInputContainer--invalid`  |
| `emailInputLabel`               |
| `formSubmitContainer`           |
| `formSubmitContainer--invalid`  |
| `nameInputContainer`            |
| `nameInputContainer--invalid`   |
| `nameInputLabel`                |
| `newsletterForm`                |
| `phoneInputContainer`           |
| `phoneInputContainer--invalid`  |
| `phoneInputLabel`               |

