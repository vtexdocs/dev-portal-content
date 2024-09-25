---
title: "Customizing your store’s typography"
slug: "vtex-io-documentation-customizing-your-stores-typography"
hidden: false
createdAt: "2020-06-18T15:04:52.500Z"
updatedAt: "2022-12-13T20:17:44.827Z"
---

Effectively communicating with users requires careful consideration of your store's typography. It serves as a visual representation of your store's identity through distinctive styles, encompassing factors like font size and spacing.

> For additional information on customizing your store’s typography using the CMS, refer to the [Customizing your store’s typography](https://help.vtex.com/en/tutorial/customizing-your-stores-typography--2R0ByIjvJtuz99RK3OL5WP) guide.

## Before you begin

Before following this guide, ensure that you:

-  Review the [Best practices for using CSS handles](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization#best-practices) article.
-  Set up the [Assets](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-the-assets-builder/) builder in your Store Theme app's `manifest.json` file.
-  Set up the Styles builder to version `2.x` in your Store Theme app's `manifest.json` file. Note that previous versions of the Styles builder do not support the customization outlined in this guide.
  
  ```json manifest.json
  builders{
  ...
    "assets": "0.x",
    "styles": "2.x"
  }
  ```

## Instructions

1. Open your Store Theme app in your preferred code editor.
2. Create a new folder named `fonts` within the `assets` directory. 
3. Place the font files inside the `assets/fonts/` folder. Ensure font files have the extensions: `.ttf` or `.woff`.
4. In the `styles/configs` folder, create a new file named `font-faces.css`.
5. Use the `@font-face` rule to declare the desired CSS properties for your website's typography. For example:
  
  ```css font-faces.css
  @font-face {
    font-family: 'MyHelvetica';
    src: url(assets/fonts/MyHelvetica.woff2), url(assets/fonts/MyHelvetica.ttf);
    font-weight: bold;
  }
  ```
  
  > ℹ️ Fonts uploaded on the Assets Builder can be referenced in your CSS files by specifying their file path in the `src` property.

### Using font faces

The `font-faces.css` file is a global configuration. Utilize the declared font faces using the `font-family` property to specify the desired font for a particular component. Here's an example:

<table>
<td>
  
```css styles/configs/font-faces.css
@font-face {
  font-family: "Roboto";
  font-style: normal;
  font-weight: 400;
  src: local("Roboto"), local("Roboto-Regular"),
    url("assets/fonts/roboto-v20-latin-regular.woff2") format("woff2"),
    url("assets/fonts/roboto-v20-latin-regular.woff") format("woff");
}

@font-face {
  font-family: "Roboto";
  font-style: normal;
  font-weight: 500;
  src: local("Roboto Medium"), local("Roboto-Medium"),
    url("assets/fonts/roboto-v20-latin-500.woff2") format("woff2"),
    url("assets/fonts/roboto-v20-latin-500.woff") format("woff");
}
```

</td>
<td>

```css styles/css/vtex.minicart.css
.closeIconContainer::before {
  content: "My cart";
  font-size: 24px;
  line-height: 32px;
  font-family: Roboto;
  color: #000;
  font-weight: 500;
}
```

</td>
</table>
