---
title: "Enabling product purchase from search with QuickOrder"
excerpt: "This feature allows customers to add products directly to their cart from search results, simplifying the purchase process."
---
 
**QuickOrder** is a feature that allows customers to add products directly to their cart from search results, simplifying the purchase process. It reduces the number of steps required to complete a purchase, making it especially useful for B2B stores that involve bulk and frequent orders.
QuickOrder can help in the following scenarios:

- Minimizing clicks to add items to the cart.
- Simplifying processes for bulk and frequent orders.
- Improving the usability of search results.
- Handling complex product variations.

## Before you begin

Before implementing QuickOrder, make sure you have:

- A FastStore project onboarded through [WebOps](https://developers.vtex.com/docs/guides/faststore/getting-started-2-starting-the-project).
- [VTEX Intelligent Search](https://help.vtex.com/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/3qgT47zY08biLP3d5os3DG) installed and integrated in your store.
- An understanding of [Section Override](https://developers.vtex.com/docs/guides/faststore/overrides-overview) to follow along with the instructions.

## Use case: B2B store

The B2B store use case is optimized for business buyers who need to add large quantities of products — including multiple variants — to their cart directly from search results. In this configuration, the `SearchProductItem` component displays available stock and allows for higher quantity inputs, streamlining the purchasing process for repeat and bulk orders.
QuickOrder in a B2B context supports two interaction patterns:

- **Simple quantity input**: The buyer sets the desired quantity next to each search result and adds it to the cart directly.

 ![quick-order-quantity-selector](https://vtexhelp.vtexassets.com/assets/docs/src/quickorder-b2b-search-results___2e7fec0b94420c3014a48c1fec6ce813.png)
  
- **SKU Matrix (bulk variant selection)**: For products with multiple variants (e.g., sizes, colors), clicking the add-to-cart button opens a sidebar panel where the buyer can select combinations and quantities across all SKUs at once, then add everything to the cart in a single action.

 ![quick-order-sku-matrix-right-sidebar](https://vtexhelp.vtexassets.com/assets/docs/src/quickorder-sku-matrix___79ff33859a20bd179905ac6298541d2b.png)

### Instructions

#### Step 1 - Override the `SearchProductItem` component

1. In your FastStore project, navigate to `src/components/overrides` and create a `SearchProductItem.tsx` file.
2. Add the following code to the file:

  ```tsx
  import { SectionOverride } from "@faststore/core";
  import { SearchProductItemContent_unstable } from "@faststore/core/experimental";
   
  const SECTION = "SearchInput" as const;
   
  const override: SectionOverride = {
    section: SECTION,
    components: {
      SearchProductItemContent: {
        Component: (props) => (
          <SearchProductItemContent_unstable
            {...props}
            quickOrderSettings={{
              quantitySelector: {
                maxQuantity: 999,
              },
              outOfStockLabel: "Out of stock",
            }}
          />
        ),
      },
    },
  };
   
  export { override };
  ```

  The code above overrides the `SearchProductItemContent` component to enable QuickOrder with the following settings:
    - `maxQuantity`: Sets the upper limit for the quantity selector. Adjust this value to meet your store's requirements.
    - `outOfStockLabel`: Defines the label displayed when a product is out of stock.

3. Open the terminal and run `yarn dev` to sync the changes locally.
4. Access your store's local development URL to verify that the search results now display a quantity selector and an add-to-cart button next to each product.

#### Step 2 - Enable the SKU Matrix sidebar for bulk variant selection

For products with multiple SKUs, you can extend QuickOrder with the **SKU Matrix** sidebar, which lets buyers choose variants and quantities in a single interaction.
>⚠️ The SKU Matrix sidebar (`__experimentalSKUMatrixSidebar`) is an experimental feature. Its API and behavior may change in future releases.

1. In `src/components/overrides`, create a `Navbar.tsx` file and add the following:

  ```tsx
  import { SectionOverride } from "@faststore/core";
   
  const SECTION = "Navbar" as const;
   
  const override: SectionOverride = {
    section: SECTION,
    components: {
      __experimentalSKUMatrixSidebar: {
        Component: () => null,
      },
    },
  };
   
  export { override };
  ```

   The `__experimentalSKUMatrixSidebar` override registers the SKU selection sidebar in the Navbar. This allows buyers to view and select all available SKU combinations for a product from a drawer panel, without leaving the search results page.

2. Update your `SearchProductItem.tsx` override to enable the SKU Matrix:

  ```tsx
  import { SectionOverride } from "@faststore/core";
  import { SearchProductItemContent_unstable } from "@faststore/core/experimental";
   
  const SECTION = "SearchInput" as const;
   
  const override: SectionOverride = {
    section: SECTION,
    components: {
      SearchProductItemContent: {
        Component: (props) => (
          <SearchProductItemContent_unstable
            {...props}
            quickOrderSettings={{
              skuMatrix: {
                enabled: true,
              },
              quantitySelector: {
                maxQuantity: 999,
              },
              outOfStockLabel: "Out of stock",
            }}
          />
        ),
      },
    },
  };
   
  export { override };
  ```

   With `skuMatrix.enabled` set to `true`, the add-to-cart button in search results opens the SKU Matrix sidebar for products with multiple variants, allowing buyers to pick variant combinations and quantities before adding everything to the cart.

3. Run `yarn dev` to apply the changes locally.
4. Perform a search and click the add-to-cart button on a product with multiple SKUs. The SKU Matrix panel should open.

#### Step 3 - Promote your changes

After testing locally, follow these steps to deploy the changes to production:

1. In your local store code, create a new branch with the changes you made.
2. Push the changes to the new branch and publish it.
3. Open a pull request in the store repository.
4. If the checks and reviews are all good, merge the branch with the main one.

>ℹ️ For more details on customizing components in FastStore, see [Section Override](https://developers.vtex.com/docs/guides/faststore/overrides-overview). For information about the Search components used in QuickOrder, see [SearchProducts](https://developers.vtex.com/docs/guides/faststore/molecules-search-products).
