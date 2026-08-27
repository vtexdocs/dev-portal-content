---
title: "Overriding a native component in the CMS"
hidden: false
slug: "cms-overriding-a-native-component"
createdAt: "2026-08-26T12:00:00.000Z"
updatedAt: "2026-08-26T20:30:00.000Z"
---

> ⚠️ This guide applies to stores using the [CMS](https://developers.vtex.com/docs/guides/cms-for-faststore-storefronts) with FastStore versions `3` or `4`. For stores using Headless CMS (legacy), see the [Overriding a native component](https://developers.vtex.com/docs/guides/faststore/overrides-native-component) guide.

FastStore includes native component sections such as `ProductShelf`, `ProductDetails`, and `Breadcrumb`. When a native component already meets most of your store's needs, you can override it to keep its existing data fetching and behavior while changing only the parts you need.

In this guide, you'll override the native `ProductShelf` component by adding a CMS-editable **Show Pix discount?** toggle to it product cards, while keeping the native carousel unchanged.

| Before | After |
| ------ | ----- |
| ![product-shelf-before](https://vtexhelp.vtexassets.com/assets/docs/src/override-component-1___904b839803dde8e865ecd1c89068e6ec.png) | ![product-shelf-after](https://vtexhelp.vtexassets.com/assets/docs/src/override-component-3___06a05f31d4a330b60b57d046ba75f47b.png) |

> ℹ️ If you need to create a section that doesn't have a native FastStore counterpart, see the [Creating a new section in the CMS](https://developers.vtex.com/docs/guides/cms-creating-a-new-section) guide.

---

## Before you begin

- The [CMS](https://developers.vtex.com/docs/guides/cms-for-faststore-storefronts) must be installed and enabled in your VTEX account.
- The [Content plugin](https://developers.vtex.com/docs/guides/content-plugin) must be installed on your machine (`vtex plugins install @vtex/cli-plugin-content`) and up to date (`vtex plugins update`) — an outdated plugin fails with a version-mismatch error the first time you run any `vtex content` command.
- You know your CMS store ID. It's the `contentSource.project` value in your project's `discovery.config.js` — **not** your VTEX account name. Every `cms/` folder path and every `vtex content` prompt below expects this ID.
- Identify which native section and which overridable component (slot) you want to change. See the [List of native sections and overridable components](https://developers.vtex.com/docs/guides/faststore/building-sections-list-of-native-sections).

---

## How overriding works

Overriding a native section involves two independent layers. Both are required, and changing only one is the most common source of confusion.

| Layer | File | What it controls |
| ----- | ---- | ---------------- |
| **Behavior** | `src/components/sections/**` + `src/components/index.tsx` | Which React components render inside the section |
| **Content** | `cms/{storeId}/components/cms_component__*.jsonc` | Which fields editors see in the CMS |

### Where your override files actually need to live

This is the part that cost the most time to get right, so it gets its own section.

The FastStore CLI's dev/build step copies your **entire** `src/` folder into `.faststore/src/customizations/src/`. That's not a paraphrase — it's literally what the CLI does internally:

```js
// @faststore/cli, simplified
copySync(userSrcDir, tmpCustomizationsSrcDir)
// userSrcDir            = <project>/src
// tmpCustomizationsSrcDir = .faststore/src/customizations/src
```

The practical consequence: your override component belongs at `src/components/sections/ProductShelf/index.tsx` and your registration file at `src/components/index.tsx` — **directly under `src/`, not inside a `src/customizations/` folder that you create yourself.**

If you nest your files under `src/customizations/src/components/index.tsx` (a reasonable-looking convention, and one you may see suggested elsewhere), the whole `customizations` folder you created gets swept up by the copy above and lands one level too deep: `.faststore/src/customizations/src/customizations/src/components/index.tsx`. That file compiles cleanly, your CMS field saves fine in Admin, and nothing errors — but the module FastStore actually imports at runtime (`src/customizations/src/components`, resolved inside the generated `.faststore` tree) still resolves to the framework's default stub:

```ts
// what stays loaded if your files are nested one level too deep
export default {}
```

Your override silently never runs. There is no warning for this.

**How to verify you got it right:** after `yarn dev` finishes its first compile, open `.faststore/src/customizations/src/components/index.tsx` directly and confirm it contains *your* code, not `export default {}`. If it doesn't, your files are in the wrong place — move them to `src/components/index.tsx` / `src/components/sections/{Name}/`, delete `.faststore/` entirely, and restart `yarn dev` to force a clean resync.

### The schema supersession rule

When your `.jsonc` file declares a `$componentKey` that matches a native section name, your definition **supersedes** the native definition for that key. The generated schema extends the platform base:

```json
{
  "$base": "vtex.faststore@4",
  "components": {
    "ProductShelf": { "...": "your definition" }
  }
}
```

The practical consequence is important: **any native field you omit disappears from the CMS editor.** To override `ProductShelf` and add one field, your `.jsonc` must declare all of the native fields *plus* your new one. There is currently no `$extends` reference that inherits a native section's properties — `$extends` is always `["#/$defs/base-component"]`, which supplies only the shared base, not the section's own fields.

> ⚠️ Because native fields are copied rather than inherited, your schema can drift when FastStore adds a field to a native section upstream. Re-check your overridden sections' schemas when upgrading `@faststore/core`.

### Choosing how to override a slot

`getOverriddenSection` accepts two forms per component, and they are **mutually exclusive**:

- `{ props: { ... } }` — keep the native component, change its props.
- `{ Component: MyComponent }` — replace the component entirely.

If you supply both, `props` is ignored and a warning is logged to the browser console. To replace a component *and* configure it from the CMS, wrap it in a function that closes over the CMS configuration (shown in [Step 1](#step-1---create-the-overridden-section)).

You don't have to replace every slot a section exposes. `ProductShelf` has two: `__experimentalCarousel` and `__experimentalProductCard`. If you only need to change the product card, simply omit `__experimentalCarousel` from your `components` object — the native carousel keeps rendering untouched.

> 💡 To find a section's exact slot names and native prop shape for the version you have installed, read the source directly: `node_modules/@faststore/core/src/components/sections/{Name}/DefaultComponents.ts` lists the slots, and `node_modules/@faststore/core/src/components/ui/{Name}/{Name}.tsx` shows how they're called. These names and props are internal APIs and can change between versions — checking your actual installed version beats trusting any doc, including this one.

---

## Instructions

### Step 1 - Create the overridden section

1. Open your store project in a code editor.
2. In `src/components/sections`, create a `ProductShelf` folder with an `index.tsx` file.
3. Import the native section and `getOverriddenSection` from `@faststore/core`. Since we're keeping the native carousel, we only override the `__experimentalProductCard` slot — wrapping the native card rather than replacing it:

```tsx src/components/sections/ProductShelf/index.tsx
import { useMemo, type ComponentProps } from 'react'
import { getOverriddenSection, ProductShelfSection } from '@faststore/core'
import NativeProductCard, {
  type ProductCardProps,
} from 'src/components/product/ProductCard'

import styles from './PixDiscountBadge.module.scss'

type NativeProductShelfProps = ComponentProps<typeof ProductShelfSection>

type ProductShelfProps = Omit<
  NativeProductShelfProps,
  'productCardConfiguration'
> & {
  productCardConfiguration?: NativeProductShelfProps['productCardConfiguration'] & {
    /**
     * Shows a "% off paying with Pix" message below the product card, computed
     * from the same discount used by the native discount badge.
     */
    showPixDiscount?: boolean
  }
}

// Keeps the native carousel untouched; only the product card slot is overridden.
function withPixDiscount(showPixDiscount: boolean) {
  return function PixDiscountProductCard(props: ProductCardProps) {
    if (!showPixDiscount) {
      return <NativeProductCard {...props} />
    }

    const {
      offers: {
        lowPrice,
        offers: [{ listPrice }],
      },
    } = props.product

    const discountPercentage =
      listPrice > 0 ? Math.round(100 - (lowPrice / listPrice) * 100) : 0

    return (
      <div data-fs-pix-discount-card>
        <NativeProductCard {...props} />
        {discountPercentage > 0 && (
          <span className={styles.pixDiscountBadge}>
            {discountPercentage}% off paying with Pix
          </span>
        )}
      </div>
    )
  }
}

function ProductShelf(props: ProductShelfProps) {
  const { showPixDiscount = false, ...productCardConfiguration } =
    props.productCardConfiguration ?? {}

  // Memoized so a new component identity isn't created on every render.
  const OverriddenProductShelf = useMemo(
    () =>
      getOverriddenSection({
        Section: ProductShelfSection,
        components: {
          __experimentalProductCard: {
            Component: withPixDiscount(showPixDiscount),
          },
        },
      }),
    [showPixDiscount]
  )

  return (
    <OverriddenProductShelf
      {...props}
      productCardConfiguration={productCardConfiguration}
    />
  )
}

export default ProductShelf
```

```scss src/components/sections/ProductShelf/PixDiscountBadge.module.scss
.pixDiscountBadge {
  display: block;
  margin-top: var(--fs-spacing-tiny, 0.25rem);
  color: var(--fs-color-success-text, var(--fs-color-main-3));
  font-size: var(--fs-text-size-0);
  font-weight: var(--fs-text-weight-medium);
}
```

> ⚠️ We import the native card via `src/components/product/ProductCard` (no relative path) — this resolves to the framework's default because our project doesn't have a file at that exact path, shadowing it. If you *do* create your own file at that same path (e.g. to fully replace the card everywhere, not just inside this shelf), that new file becomes what resolves — and this override would then need a relative import instead to still reach the original. Know which one you're doing.

### Step 2 (optional) - Replacing a slot's component entirely, with CMS configuration

The pattern above wraps the native component. If instead you want to **replace** a slot outright (e.g. swap the carousel for a different library) and still configure it from the CMS, remember `props` and `Component` are mutually exclusive — so the section itself must read the CMS prop and forward it into the replacement, closing over it in a wrapper:

```tsx
function withCarouselConfiguration(configuration: CarouselConfiguration = {}) {
  const defined = Object.fromEntries(
    Object.entries(configuration).filter(([, v]) => v !== undefined)
  )

  return function ConfiguredCarousel(props: CarouselProps) {
    return <YourCarousel {...props} {...defined} />
  }
}

// inside your section component, alongside the productCardConfiguration handling:
const OverriddenProductShelf = useMemo(
  () =>
    getOverriddenSection({
      Section: ProductShelfSection,
      components: {
        __experimentalCarousel: {
          Component: withCarouselConfiguration(carouselConfiguration),
        },
        // ...other slots
      },
    }),
  [carouselKey] // JSON.stringify(carouselConfiguration) — CMS returns a new object each render
)
```

This part is architecturally consistent with how `getOverriddenSection` works, but — unlike Step 1 — we didn't build and verify a full carousel replacement in this pass. If you go this route, budget time to actually test it; introducing a new carousel library is a real dependency decision, not just a code pattern.

### Step 3 - Declare the CMS schema

Run `vtex content init` if you haven't already. It prompts for a store ID (default shown is `faststore` — **type your actual CMS store ID instead**, matching `contentSource.project` in `discovery.config.js`) and scaffolds:

```sh
cms/{storeId}/
├── components/
│   └── cms_component__bannerExample.jsonc.example
└── pages/
    └── cms_content_type__landingPage.jsonc.example
```

These `.jsonc.example` files are placeholder templates, not live schemas — `generate-schema` ignores them. Create your own `.jsonc` file (no `.example` suffix) instead.

In `cms/{storeId}/components`, create `cms_component__productshelf.jsonc`. Declare **every native field** of `ProductShelf`, then append your custom field:

> ℹ️ To read the exact native definition for your installed version, open `node_modules/@faststore/core/cms/faststore/components/cms_component__productshelf.jsonc` and copy it as your starting point. This is the reliable way to avoid dropping fields — don't retype them from memory or from a doc (including this one).

```jsonc cms/{storeId}/components/cms_component__productshelf.jsonc
{
  "$extends": ["#/$defs/base-component"],
  "$componentKey": "ProductShelf",
  "$componentTitle": "Product Shelf",
  "title": "Product Shelf",
  "description": "Add custom shelves to your store",
  "type": "object",
  "required": ["title", "numberOfItems", "after", "sort"],
  "properties": {
    "title": { "type": "string", "title": "Title" },
    "numberOfItems": {
      "type": "integer",
      "title": "Total number of items",
      "default": 5,
      "description": "Total number of items. The quantity may be smaller if the query returns fewer products."
    },
    "itemsPerPage": {
      "type": "integer",
      "title": "Number of items per page",
      "default": 5,
      "description": "Number of items to display per page in carousel"
    },
    "after": {
      "type": "string",
      "title": "After",
      "default": "0",
      "description": "Initial pagination item"
    },
    "sort": {
      "title": "Sort",
      "description": "Items order",
      "default": "score_desc",
      "enum": [
        "discount_desc", "name_asc", "name_desc", "orders_desc",
        "price_asc", "price_desc", "release_desc", "score_desc"
      ],
      "enumNames": [
        "Discount: higher to lower", "Name: A-Z", "Name: Z-A",
        "Orders: higher to lower", "Price: lower to higher",
        "Price: higher to lower", "Release date: newer to older",
        "Relevance: higher to lower"
      ]
    },
    "term": { "type": "string", "title": "Search term" },
    "selectedFacets": {
      "title": "Facets",
      "type": "array",
      "items": {
        "title": "Facet",
        "type": "object",
        "required": ["key", "value"],
        "properties": {
          "key": {
            "title": "Key",
            "description": "For collections use: productClusterIds",
            "type": "string",
            "default": "productClusterIds"
          },
          "value": {
            "title": "Value",
            "description": "The ID of the VTEX Collection to pull products from. Verify it exists and has products under Catalog > Collections before using it here — see the troubleshooting note below.",
            "type": "string",
            "default": "140"
          }
        }
      }
    },
    "taxesConfiguration": {
      "title": "Taxes Configuration",
      "type": "object",
      "properties": {
        "usePriceWithTaxes": { "title": "Should use taxes to calculate the price?", "type": "boolean", "default": false },
        "taxesLabel": { "title": "Tax label to be displayed", "type": "string", "default": "Tax included" }
      }
    },
    "productCardConfiguration": {
      "title": "Product Card Configuration",
      "type": "object",
      "properties": {
        "showDiscountBadge": { "title": "Show discount badge?", "type": "boolean", "default": true },
        "bordered": { "title": "Cards should be bordered?", "type": "boolean", "default": true },

        "showPixDiscount": {
          "title": "Show Pix discount?",
          "description": "Displays a \"% off paying with Pix\" message below the product card, using the same discount already applied to the product.",
          "type": "boolean",
          "default": false
        }
      }
    }
  },
  "readOnly": false,
  "writeOnly": false,
  "deprecated": false,
  "$abstract": false
}
```

### Step 4 - Register the override

In `src/components/index.tsx` — directly under `src/`, per the [warning above](#where-your-override-files-actually-need-to-live) — map the **native section name** to your component:

```tsx src/components/index.tsx
import ProductShelf from './sections/ProductShelf'

export default {
  ProductShelf,
}
```

> ⚠️ `src/components/index.tsx` must use a **default export only**. Named exports are not picked up.

The object key is what connects your code to the CMS definition, and must match the `$componentKey` exactly. When your component name differs from the native section name, map it explicitly:

```tsx
import CustomProductDetails from './sections/CustomProductDetails'

export default {
  ProductDetails: CustomProductDetails,
}
```

### Step 5 - Generate and upload the schema

1. Confirm the component compiles: `yarn dev`. Then check `.faststore/src/customizations/src/components/index.tsx` actually contains your code (see [the callout above](#where-your-override-files-actually-need-to-live)) — do this every time, it's the cheapest way to catch the nesting mistake before it wastes your afternoon.

2. Generate the aggregated schema:

   ```bash
   vtex content generate-schema cms/{storeId}/components cms/{storeId}/pages --out cms/{storeId}/schema.json
   ```

   If you're overriding a native component (as we are with `ProductShelf`), this prompts:

   ```bash
     You are about to override default definitions for the following components:
     ProductShelf
     Are you sure? (y/N)
   ```

   This is expected — answer **yes**.

3. Confirm your definition landed in the generated `schema.json` under `components.ProductShelf.properties.productCardConfiguration.properties`, including both the native fields and `showPixDiscount`.

   > ⚠️ Never edit `schema.json` by hand. It is generated output. If a field is missing, fix the `.jsonc` file and regenerate.

4. Make sure you're logged in to the correct account (`vtex whoami` confirms), then upload:

   ```bash
   vtex content upload-schema cms/{storeId}/schema.json
   ```

   This command is interactive and asks two things, in order:
   - **Store ID to associate** — type your CMS store ID again (matching `contentSource.project`). There's no `-s`/`--store` flag to pass this on the command line in current plugin versions; some older references show one, but check `vtex content upload-schema --help` against what you actually have installed.
   - **Version to publish** — it looks up the latest published version for that store ID and suggests a semver bump (e.g. `1.0.0` → `1.1.0`). Accept the suggestion or type your own.

   > ⚠️ This command publishes immediately to your **live** CMS store — there's no separate "are you sure" step after the version prompt. Confirm the store ID matches `api.storeId`/`contentSource.project` in `discovery.config.js` before running it; uploading to the wrong store overwrites that store's schema.

   > ⚠️ Run this in a real, interactive terminal. Piping answers into it (for automation or scripting) is unreliable — a wrong or mistimed answer gets silently absorbed by whichever prompt happens to be active, with no error to warn you.

### Step 6 - Verify in the CMS

1. In the Admin, open **Storefront > Content** and select the entry that uses the section, such as **Home**.
2. Open the **Product Shelf** section and confirm that both the native fields and your new **"Show Pix discount?"** field appear under **Product Card Configuration**.
3. Toggle it on and **Save** (and publish/promote, if your CMS uses a draft/live branch split).

    ![show-pix-toogle](https://vtexhelp.vtexassets.com/assets/docs/src/show-pix-toogle___579842a11b21c9cca0df58a587a7d2b4.gif)

4. With the dev server still running, reload the page. CMS content changes take effect on the next request in local dev — no server restart needed for content, only for code changes (see Step 5.1).

> ℹ️ Uploading a schema **registers** the definition so it appears in the editor. It does not place the section on a page or guarantee that section has products to show — see the troubleshooting note below if a shelf renders empty even with everything wired up correctly.
