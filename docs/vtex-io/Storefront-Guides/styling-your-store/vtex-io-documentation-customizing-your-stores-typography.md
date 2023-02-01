---
title: "Customizing your store’s typography"
slug: "vtex-io-documentation-customizing-your-stores-typography"
hidden: false
createdAt: "2020-06-18T15:04:52.500Z"
updatedAt: "2022-12-13T20:17:44.827Z"
---
In addition to being crucial for communicating with users, a store’s typography should be a reflection of its identity, using its characteristic styles, such as font size and spacing.

Whether using the admin’s CMS or your store theme CSS files, Store Framework gives you the flexibility to customize your store’s typography according to your business needs.

> ⚠️ If you want to perform your store's typography customization in **the Admin's CMS**, refer to [Customizing your store’s typography documentation in the Help Center](https://help.vtex.com/tutorial/personalizando-a-tipografia-da-sua-loja--2R0ByIjvJtuz99RK3OL5WP).

## Before you start

Bear in mind that for the customization to work, the **Styles builder of your store must be 2. x.** To successfully migrate to Styles Builder 2.x, you must update the version of the `styles` builder in the `manifest.json` file of your store theme app, as the example below:

```json
builders{
...
"styles": "2.x"
}
```

In the following, check the [best practices of CSS handles](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization#best-practices) to review and update every CSS customization for your store elements.

## Step by step

### Using store theme CSS files

1. Open your store theme directory using a code editor of your preference.
2. Create a new folder inside the `assets` directory called `fonts`. Make sure your app have the [assets builder in its manifest](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-the-assets-builder/).
3. Add the font files inside this folder (`assets/fonts/`).

>⚠️  The font files must be in the following file extensions: `.ttf` or `.woff`.

4. In `styles/configs` folder, create a new file called `font-faces.css`.
5. Use the `@font-face` rule declaring the CSS properties you desire to apply in your website typography. For example:

```css
@font-face {
  font-family: 'MyHelvetica';
  src: url(assets/fonts/MyHelvetica.woff2), url(assets/fonts/MyHelvetica.ttf);
  font-weight: bold;
}
```

> ℹ️  Notice that fonts uploaded on Assets builder can be referenced in your CSS files by declaring the desired file path in the `src` property.

>⚠️ The `font-faces.css` is a global file meaning its configurations are applied to all texts from the website. If you want to customize a component's typography independently, overriding the global configurations,you should declare the `font-faces.css` file still and refer the desired component font using the `font-family` property in the app's CSS overriding file.
