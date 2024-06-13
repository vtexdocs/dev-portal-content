---
title: "My store does not reflect the overrides I created"
slug: "my-store-does-not-reflect-the-overrides-i-created"
hidden: false
createdAt: "2024-06-13T08:47:00.508Z"
excerpt: "During the Section overriding process], you can experience issues such as overridden components not appearing or not behaving as you expected."
tags:
    - faststore
---

[Section override](https://developers.vtex.com/docs/guides/faststore/overrides-overview) is a feature for customizing and creating new components for your FastStore storefront. However, you may encounter situations where the overridden components don't appear or function as intended.

Below are various troubleshooting checks and instructions you can use to solve your store's issue:

| Issue | Troubleshooting instructions |
| ----- | ---------------------------- |
| Overrides fail to display in your store. | [Check the `getOverriddenSection` function](#checking-the-getoverriddensection-function). |
| Overrides are not reflected in the Headless CMS. | [Remove default props](#removing-default-props). |
| Styles are not being applied to the component. | [Check custom section class names](#checking-custom-section-class-names).|

## Solution

To understand and correct each error, see the solutions below:

### Checking the `getOverriddenSection` function

If you encounter an error message mentioning a missing function named `getOverriddenSection`, it means you need to import it into your code.

This function is important for displaying product overrides within your store, allowing you to customize specific product page sections. Follow the steps below to import the function to your project:

1. Open the file where you are overriding the section, for example, `ProductDetailsWithCustomButton.tsx`.
2. At the top of the file, import the `getOverridenSetion` function:

   ```tsx
    import { getOverriddenSection } from '@faststore/core';
    ```

    Here's an example of how to use `getOverriddenSection` in your `ProductDetailsWithCustomButton.tsx` file:

    ```tsx
    import { ProductDetailsSection, getOverriddenSection } from '@faststore/core'

    const ProductDetailsWithCustomButton = getOverriddenSection({
    Section: ProductDetailsSection,
    components: {
        BuyButton: { Component: CustomBuyButton },
    },
    })
    ```

3. Run `yarn dev` to sync your changes with your development environment.

### Adding the section’s schema in the Headless CMS

If you can’t see the changes in the Headless CMS after [overriding a prop](https://developers.vtex.com/docs/guides/faststore/overrides-component-props) or a [section](https://developers.vtex.com/docs/guides/faststore/overrides-native-component), this may be due to a schema. The Headless CMS won’t display your custom section without one.

1. [Add the schema](https://developers.vtex.com/docs/guides/faststore/overrides-syncing-components-with-the-headless-cms) for the new section to the Headless CMS.
2. Replace the native section with your custom one. For detailed instructions, see the guide [Syncing components with the Headless CMS](https://developers.vtex.com/docs/guides/faststore/overrides-syncing-components-with-the-headless-cms).

### Removing default props

If the changes you made after [overriding a prop](https://developers.vtex.com/docs/guides/faststore/overrides-component-props) are not being reflected or not behaving as expected, this could be due to default prop definitions taking precedence. In this case, default props definitions may override yours when adding the section to the Headless CMS. Props changed via the Headless CMS take precedence over those defined in code through overrides. This can lead to confusion when you try to set a different default value in your code.

Consider removing default values to ensure your overrides work.

1. Identify the property you want to modify.
2. Check if the property has a default value set in the Admin.
3. If the property has a default value set in the Admin, open the `sections.json` file in your store code and find the property you want to change.
4. Remove the default value from your code.
5. Run `yarn cms sync` to sync the changes.

### Checking custom section class names

If the style you created is not being applied, make sure that the `className` added to the section matches the one declared in the stylesheet. For instance, if you declared `className: styles.simpleAlert` in the section, ensure that the corresponding style declaration in the stylesheet is `.simpleAlert`.

For more information, see the [Override section styles](https://developers.vtex.com/docs/guides/faststore/overrides-section-styles) article.
