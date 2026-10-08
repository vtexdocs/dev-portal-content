---
title: "CSS variables in Checkout extensions"
slug: "css-variables-in-checkout-extensions"
hidden: false
createdAt: "2026-06-16T00:00:00.000Z"
updatedAt: "2026-06-16T00:00:00.000Z"
excerpt: "Reference for the CSS variables available to style Checkout extensions consistently with the core visual design."
---

> ⚠️ This feature is only available for stores using [B2B Buyer Portal](https://help.vtex.com/en/docs/tutorials/b2b-buyer-portal), which is currently available to selected accounts.

CSS variables are standardized values for styling that help maintain visual consistency across Checkout extensions. These variables allow you to easily align with the core visual design of the Checkout application.

For more information on how to apply CSS to your extensions, see [Using CSS in Checkout extensions](https://developers.vtex.com/docs/guides/using-css-in-checkout-extensions).

## Available CSS variables

Here are the variables currently available for use in your CSS:

- **`--fc-colors-brand-primary`**: Represents the primary brand color used throughout the Checkout. You can use this variable to ensure your extension matches the core branding.

```css
.custom-button {
  background-color: var(--fc-colors-brand-primary);
}
```

You can also use the following variations of the primary color:

- **`--fc-colors-brand-primary-40`**
- **`--fc-colors-brand-primary-60`**
- **`--fc-colors-brand-primary-80`**
- **`--fc-colors-brand-primary-darker`**

```css
.custom-button-40 {
  background-color: var(--fc-colors-brand-primary-40);
}
.custom-button-60 {
  background-color: var(--fc-colors-brand-primary-60);
}
.custom-button-80 {
  background-color: var(--fc-colors-brand-primary-80);
}
.custom-button-darker {
  background-color: var(--fc-colors-brand-primary-darker);
}
```

- **`--fc-colors-light-gray-100`, `--fc-colors-light-gray-300`, `--fc-colors-light-gray-400`, and `--fc-colors-dark-gray-1000`**: Represent the gray variations used throughout the Checkout. You can use these variables to ensure your extension matches the core branding.

```css
.custom-text {
  background-color: var(--fc-colors-light-gray-100);
}
```

- **`--fc-fonts-sans`**: Represents the default sans-serif font used in the Checkout. Use this variable to ensure your text aligns with the core font styles.

```css
.custom-text {
  font-family: var(--fc-fonts-sans);
}
```

- **`--fc-button-font-size`**: Represents the font size used in buttons throughout the Checkout.

```css
.button {
  font-size: var(--fc-button-font-size);
}
```

- **`--fc-button-line-height`**: Represents the line height used in buttons throughout the Checkout.

```css
.button {
  line-height: var(--fc-button-line-height);
}
```

- **`--fc-button-font-weight`**: Represents the font weight used in buttons throughout the Checkout.

```css
.button {
  font-weight: var(--fc-button-font-weight);
}
```

These CSS variables help keep your extensions consistent with the core design while allowing flexibility for custom styles.

> ℹ️ In future releases, we will add support for more tokens and CSS variables to maintain visual consistency between the extensions and the Checkout core.
