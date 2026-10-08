---
title: "Issues when customizing FastStore icons"
slug: "issues-when-customizing-faststore-icons"
hidden: false
createdAt: "2026-05-19T00:00:00.000Z"
updatedAt: "2026-07-03T11:00:00.000Z"
excerpt: "Troubleshoot common issues when adding custom icons or overriding native icons in a FastStore project."
domainFilters:
  - FastStore
symptomFilters:
  - Loading failure
  - Rendering mismatch
---

FastStore users may encounter issues when customizing the icon set in their store, either by [adding a custom icon](https://developers.vtex.com/docs/guides/faststore/managing-icons-adding-custom-icons) or [overriding a native icon](https://developers.vtex.com/docs/guides/faststore/managing-icons-overriding-native-icons). The icon may not appear, look distorted, or ignore the theme colors. In some cases, the default FastStore icons may stop rendering after the change.

| Issue | Possible cause | Solution |
| ----- | -------------- | -------- |
| The icon doesn't appear, or the override has no effect in the storefront. | The `id` doesn't match the `name` prop, or `icons.svg` isn't in the right location. | [Verify the icon configuration](#verify-the-icon-configuration) |
| The icon renders, but looks distorted or the size is inconsistent. | The `viewBox` is missing, the markup is incompatible, or there are hardcoded dimensions. | [Fix the SVG markup](#fix-the-svg-markup) |
| The icon ignores the theme and renders in a fixed color. | The paths use hardcoded `fill` or `stroke` values instead of `currentColor`. | [Make the icon respect the theme](#make-the-icon-respect-the-theme) |
| Default FastStore icons stopped rendering after the customization. | The custom `icons.svg` replaced the default file without including the original symbols. | [Restore the default icons](#restore-the-default-icons) |

## Solutions

To solve your issue, follow one of the paths below based on the symptom you're seeing.

### Verify the icon configuration

Use this path when the icon doesn't appear at all or when an override has no effect.

1. Open `/public/icons.svg` and confirm that the `id` on the `<symbol>` element exactly matches the `name` prop passed to the `Icon` component, including capitalization. For overrides, the `id` must remain identical to the original icon's `id`.
2. Make sure `icons.svg` is at the root of `/public/`, not inside a subfolder.
3. Run `yarn dev` (or `yarn build`) to copy the file into the build output.
4. Clear your browser cache and reload the local store to confirm the icon now appears.

### Fix the SVG markup

Use this path when the icon renders but looks broken, distorted, or inconsistently sized.

1. Open the `<symbol>` for your icon in `/public/icons.svg`.
2. Confirm the `viewBox` attribute is set and matches the original artwork dimensions (for example, `viewBox="0 0 256 256"`). For overrides, use the same `viewBox` as the original symbol to keep consistent sizing across components.
3. Remove hardcoded `width` and `height` attributes from the `<symbol>` so the icon can be scaled by the `Icon` component.
4. Check that the SVG paths are valid and self-contained, with no references to external files or `<defs>` outside the symbol.
5. Remove transforms, clip paths, or masks that depend on context outside the original SVG.
6. Save the file, rebuild the project, and check the icon in the storefront.

### Make the icon respect the theme

Use this path when the icon appears in a fixed color and ignores the surrounding text color or theme.

1. Open the `<symbol>` for your icon in `/public/icons.svg`.
2. Replace hardcoded `fill` and `stroke` attribute values with `currentColor` so the icon inherits the surrounding text color.
3. Remove any inline `style` or `color` attributes that pin the icon to a specific color.
4. Save the file, rebuild the project, and verify the icon now reflects the theme.

### Restore the default icons

Use this path when default FastStore icons stop rendering after you add a custom icon or apply an override.

1. Open your terminal and run `yarn dev` to make sure the `.faststore` folder is up to date.
2. Copy `.faststore/public/icons.svg` again into your store's `/public/` folder, overwriting the current file.
3. Reapply your customizations to the new copy:
    - For custom icons, add your new `<symbol>` entries following the [Adding custom icons](https://developers.vtex.com/docs/guides/faststore/managing-icons-adding-custom-icons) guide.
    - For overrides, replace the contents of the relevant `<symbol>` entries following the [Overriding native icons](https://developers.vtex.com/docs/guides/faststore/managing-icons-overriding-native-icons) guide.
4. Rebuild the project and confirm the default and custom icons are both visible.

> ⚠️ If the issue continues after following these steps, open a ticket with [VTEX Support](https://support.vtex.com/hc/en-us).
