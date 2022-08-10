---
title: "Cookie Disclaimer"
slug: "trackfield-store-components-cookiedisclaimer"
excerpt: "trackfield.store-components@0.18.0"
hidden: true
createdAt: "2022-07-05T22:31:25.061Z"
updatedAt: "2022-08-04T10:48:21.266Z"
---
a component to set a cookie and a modal to the costumer accept the cookies.

![Media Placeholder](https://gitlab.com/acct.global/program-04/track-and-field-io/trackandfield.store-components/uploads/d3cb1fc2d762106d5a68de6fbedd4bf5/image.png)

## Configuration

1. Add the `store-components` app to your theme's dependencies in the `manifest.json`, for example:

```diff
"dependencies": {
+  "trackfield.store-components": "0.x"
}
```

2. you are now able to use the cookie-disclaimer

```json
"cookie-disclaimer": {
    "props": {
      "privacyPoliceLink": "https://trackandfield.zendesk.com/hc/pt-br/articles/360051389514-Pol%C3%ADtica-de-Cookies-do-site-Track-Field",
      "disclaimerButtonText": "CONTINUAR E FECHAR",
      "cookieExpiration": 30,
      "openInNewWindow": true
    }
  }

```

### `cookie-disclaimer` props

| Prop name              | Type      | Description                                                                           | Default value |
| ---------------------- | --------- | ------------------------------------------------------------------------------------- | ------------- |
| `privacyPoliceLink`    | `string`  | a Link to your privacy police.                                                        | `""`          |
| `disclaimerButtonText` | `string`  | the text to 'accept cookies' button                                                   | `""`          |
| `cookieExpiration`     | `number`  | time for the cookie expires from the browser                                          | `""`          |
| `openInNewWindow`      | `boolean` | prop to set the html `target`, if true it will add a rel nofollow noopener noreferrer | `false`       |

## Customization

The first thing that should be present in this section is the sentence below, showing users the recipe pertaining to CSS customization in apps:

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

Thereafter, you should add a single column table with the available CSS handles for the app, like the one below. Note that the Handles must be ordered alphabetically.

| CSS Handles                        |
| ---------------------------------- |
| `cookies-disclaimer`               |
| `cookies-disclaimer__wrapper`      |
| `cookies-disclaimer__content`      |
| `cookies-disclaimer__button`       |
| `cookies-disclaimer__privacy-link` |