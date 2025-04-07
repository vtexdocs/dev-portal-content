---
title: "FastStore: Improved breadcrumb navigation"
slug: "2025-04-30-breadcrumb-improvement"
hidden: false
type: "fixed"
createdAt: "2025-04-30T00:00:00.219Z"
updatedAt: ""
excerpt: "Store’s breadcrumb now displays only the main categories and has consistent styling on all pages."
---

Store’s [breadcrumb](https://developers.vtex.com/docs/guides/faststore/molecules-breadcrumb) navigation now maintains visibility during scrolling (no longer conflicts with the [`RegionBar`](https://developers.vtex.com/docs/guides/faststore/molecules-region-bar) component), removes redundant categories, applies consistent dropdown styling, and properly displays on PLP and Search pages.

## What has changed?

### Removed redundant categories

Previously, the breadcrumb displayed duplicate or similar categories, creating clutter. Now, only the main categories are shown.

| **Before** | **After** |
| ---------- | --------- |
| ![breadcrumb-before](https://vtexhelp.vtexassets.com/assets/docs/src/breadcrumb-before___e791d461cb57e09677e1604e0d77bb16.png) | ![breadcrumb-before](https://vtexhelp.vtexassets.com/assets/docs/src/breadcrumb-after___976fccfc280cda9cb3dd962e9e707b7c.png) |

### Improved visibility and styling

Resolved issues with the breadcrumb section display, including:

- **Scrolling behavior:** Either the `RegionBar` or breadcrumb remains visible when scrolling.

    | **Before** | **After** |
    | ---------- | --------- |
    | ![scrolling-behavior-before](https://vtexhelp.vtexassets.com/assets/docs/src/scrolling-behavior-before___f5ac656bb56e19bd9f7737c75d43302e.png) | ![scrolling-behavior-after](https://vtexhelp.vtexassets.com/assets/docs/src/scrolling-behavior-after___8b840a4d795738ee2d93716514e2d291.png) |

- **Dropdown menu styling:** Updated for consistency across pages.

    | **Before** | **After** |
    | ---------- | --------- |
    | ![dropdown-menu-before](https://vtexhelp.vtexassets.com/assets/docs/src/dropdown-menu-before___f885a2989e42f8882900305330ac4293.png) | ![dropdown-menu-after](https://vtexhelp.vtexassets.com/assets/docs/src/dropdown-menu-after___6cb408f330e4cec509b6f5490cf16f3f.png) |

- **Restored visibility on PLP and Search pages:** Breadcrumbs now appear correctly on all page types.

    | **Before** | **After** |
    | ---------- | --------- |
    | ![pages-before](https://vtexhelp.vtexassets.com/assets/docs/src/pages-before___86d8c3545de88349f492b2fb14409d5d.png) | ![pages-after](https://vtexhelp.vtexassets.com/assets/docs/src/pages-after___30f9becdaea4ae58d41338606f854e78.png) |

## What needs to be done?

To have these breadcrumb improvements in your FastStore project, update your project’s `@faststore/cli` to the latest version. To do this, follow the instructions in [Updating the '@faststore/cli' package version](https://developers.vtex.com/docs/guides/faststore/project-structure-updating-the-cli-package-version).
