---
title: "Overriding a native component in the CMS"
hidden: false
slug: "cms-overriding-a-native-component"
createdAt: "2026-08-26T12:00:00.000Z"
updatedAt: "2026-09-23T14:11:00.000Z"
---

> ⚠️ This guide applies to stores using the [CMS](https://developers.vtex.com/docs/guides/cms-for-faststore-storefronts) with FastStore versions `3` or `4`. For stores using Headless CMS (legacy), see the [Overriding a native component](https://developers.vtex.com/docs/guides/faststore/overrides-native-component) guide.

FastStore includes native component sections such as `ProductShelf`, `ProductDetails`, and `Breadcrumb`. When a native component already meets most of your store's needs, you can override it to keep its existing data fetching and behavior while changing only the parts you need.

In this guide, you'll override the native `ProductShelf` component to display a Pix discount message on its product cards. You'll also make this message configurable in the CMS, while keeping the native carousel unchanged.

![product-shelf-with-pix-discount](https://vtexhelp.vtexassets.com/assets/docs/src/override-component-3___06a05f31d4a330b60b57d046ba75f47b.png)

> ℹ️ If you need to create a section that doesn't have a native FastStore counterpart, see the [Creating a new section in the CMS](https://developers.vtex.com/docs/guides/creating-a-new-section) guide.

---

## Before you begin

Overriding a native component touches both your store code and the CMS, so you need a working CMS setup, the Content plugin installed locally, and a clear idea of which part of the section you want to change. Make sure the following is in place before you start:

- The [CMS](https://developers.vtex.com/docs/guides/cms-for-faststore-storefronts) must be installed and enabled in your VTEX account.
- The [Content plugin](https://developers.vtex.com/docs/guides/content-plugin) must be installed on your machine (`vtex plugins install @vtex/cli-plugin-content`) and up to date (`vtex plugins update`).
- You know your CMS store ID. It's the `contentSource.project` value in your project's `discovery.config.js`.
- Identify which native section and which overridable component you want to change. See the [List of native sections and overridable components](https://developers.vtex.com/docs/guides/faststore/building-sections-list-of-native-sections).

---

## Instructions

### Step 1 - Create the overridden section

1. Open your store project in a code editor.
2. In `src/components/sections`, create a `ProductShelf` folder with an `index.tsx` file.
3. Import the native section and `getOverriddenSection` from `@faststore/core`. Since we're keeping the native carousel, we only override the product card overridable component (`__experimentalProductCard`), wrapping the native card rather than replacing it:

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

// Keeps the native carousel untouched; only the product card overridable component is overridden.
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

### Step 2 - Declare the CMS schema

Run `vtex content init` if you haven't already. It prompts for a store ID (default shown is `faststore` — **type your actual CMS store ID instead**, matching `contentSource.project` in `discovery.config.js`) and scaffolds:

```sh
cms/{storeId}/
├── components/
│   └── cms_component__bannerExample.jsonc.example
└── pages/
    └── cms_content_type__landingPage.jsonc.example
```

These `.jsonc.example` files are placeholder templates, not live schemas,  `generate-schema` ignores them. Create your own `.jsonc` file (no `.example` suffix) instead.

In `cms/{storeId}/components`, create `cms_component__productshelf.jsonc`. Declare **every native field** of `ProductShelf`, then append your custom field:

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

### Step 3 - Register the override

In `src/components/index.tsx`, directly under `src/`, map the native section name to your component:

```tsx src/components/index.tsx
import ProductShelf from './sections/ProductShelf'

export default {
  ProductShelf,
}
```

> ⚠️ `src/components/index.tsx` must use a default export only. Named exports are not picked up.

The object key is what connects your code to the CMS definition, and must match the `$componentKey` exactly. When your component name differs from the native section name, map it explicitly:

```tsx
import CustomProductDetails from './sections/CustomProductDetails'

export default {
  ProductDetails: CustomProductDetails,
}
```

### Step 4 - Sync the schema with the CMS

1. Confirm the component compiles by running `yarn dev`.
2. Make sure you're logged in to the correct account (`vtex whoami` confirms).
3. From the root of your FastStore project, run:

   ```bash
   yarn cms-sync
   ```

4. Confirm the overriding:

   ```bash
     You are about to override default definitions for the following components:
     ProductShelf
     Are you sure? (y/N)
   ```

   ⚠️ This command publishes immediately to your live store. Confirm that the store ID matches `api.storeId`/`contentSource.project` in `discovery.config.js` before confirming. Uploading to the wrong store overwrites that store's schema.

5. Confirm your definition landed in the generated `schema.json` (under `cms/{storeId}`) in `components.ProductShelf.properties.productCardConfiguration.properties`, including both the native fields and `showPixDiscount`.

   > ⚠️ Never edit `schema.json` by hand. It is generated output. If a field is missing, fix the `.jsonc` file and run `yarn cms-sync` again.

### Step 5 - Verify in the CMS

1. In the Admin, open **Storefront > Content > All content** and select the entry that uses the section, such as **Home**.
2. Open the **Product Shelf** section and confirm that both the native fields and your new **"Show Pix discount?"** field appear under **Product Card Configuration**.
3. Toggle it on and **Save** (and publish/promote, if your CMS uses a draft/live branch split).

    ![show-pix-toogle](https://vtexhelp.vtexassets.com/assets/docs/src/show-pix-toogle___579842a11b21c9cca0df58a587a7d2b4.gif)

4. With the dev server still running, reload the page. CMS content changes take effect on the next request in local dev — no server restart needed for content, only for code changes (see Step 5.1).

> ℹ️ Uploading a schema registers the definition so it appears in the editor. It does not place the section on a page or guarantee that section has products to show.
