---
title: Experimental exports - Hooks and Components
slug: experimental-exports-hooks-and-components
hidden: false
createdAt: 2024-09-17T17:30:15.623Z
updatedAt: ""
---

FastStore provides [hooks](#list-of-hooks-and-components) and components to extend native features within your [custom sections](https://developers.vtex.com/docs/guides/faststore/building-sections-creating-a-new-section) and [overridden components](https://developers.vtex.com/docs/guides/faststore/overrides-overview).

For example, you can create a custom [BuyButton](https://developers.vtex.com/docs/guides/faststore/molecules-buy-button) that adds products to the cart and displays a personalized message based on user preferences or order history.

Before you begin

All experimental [hooks and components](#list-of-hooks-and-components) are suffixed with `_unstable`, indicating that they are subject to change and may not be stable for use in production.

## Instructions

1. Open your store project in a code editor, then open the component or section file where you want to import the hook or component.

2. Declare the hook or component into your custom component file.

   ```tsx
   import { use{ComponentName}_unstable as use{ComponentName} } from '@faststore/core/experimental'
   ```

3. Incorporate the imported hook or component into your custom component logic. In the following example, the `useCartToggleButton_unstable` hook enables toggling the cart.

   ```tsx mark=3
   import React from 'react'
   import { Button as UIButton } from '@faststore/ui'
   import { useCartToggleButton_unstable as useCartToggleButton } from '@faststore/core/experimental'

   export default function CustomBuyButton() {
   const { onClick: toggleCart } = useCartToggleButton()
   return (
       <UIButton
       variant="primary"
       onClick={() => {
           toggleCart()
       }}
       >
       New Buy Button
       </UIButton>
   )
   }
   ```

4. Save your changes.

5. Open a terminal and run `yarn dev` to test the implementation.

## List of hooks and components

Explore the features of the experimental hooks and the `Image_unstable` component.

- [Hooks](#hooks)
- [`Image_unstable` component](#image_unstable-component)

### Hooks

Hooks provide features or statuses from native components that you can integrate into your custom components. Here's a list of available hooks:

| Hook | Description |
| --- | --- |
| `useSession_unstable` | Accesses and manages current session information. |
| `sessionStore_unstable` | Stores and retrieves session data. |
| `validateSession_unstable` | Validates the current user session. |
| `useCart_unstable` | Accesses the current cart's status and actions. |
| `cartStore_unstable` | Stores and retrieves cart details. |
| `useBuyButton_unstable` | Leverages the behavior of the native [BuyButton](https://developers.vtex.com/docs/guides/faststore/molecules-buy-button). |
| `useCartToggleButton_unstable` | Adds a cart toggle feature to custom components. |
| `useCheckoutButton_unstable` | Leverages the behavior of the native checkout button. |
| `useRemoveButton_unstable` | Leverages the behavior of the native remove button. |
| `useQuery_unstable` | Retrieves data from a GraphQL endpoint. |
| `useLazyQuery_unstable` | Retrieves data from a GraphQL endpoint on demand. |
| `useNewsletter_unstable` | Accesses the newsletter subscription feature. |
| `useDiscountPercent_unstable` | Calculates the discount percentage for a given price. |
| `useFormattedPrice_unstable` | Formats a price value based on the current locale. |
| `useLocalizedVariables_unstable` | Provides localized variables for use in components. |
| `useProductGalleryQuery_unstable` | Retrieves product gallery images. |
| `useProductLink_unstable` | Generates a product link based on the product ID. |
| `useProductQuery_unstable` | Retrieves product details. |
| `useProductsPrefetch_unstable` | Preloads product details for a given list of product IDs. |
| `useSearchHistory_unstable` | Accesses the user's search history. |
| `useSuggestions_unstable` | Provides suggestions based on the user's search query. |
| `useTopSearch_unstable` | Retrieves the top search results. |
| `useFilter_unstable` | Enables filtering for product listings. |
| `useDelayedFacets_unstable` | Delays facet application to improve performance. |
| `useDelayedPagination_unstable` | Delays pagination to improve performance. |
| `getShippingSimulation_unstable` | Retrieves the shipping simulation data, which can be used to display shipping costs, options, and delivery estimates. |

### `Image_unstable` component

Use the [`Image_unstable`](https://github.com/vtex/faststore/blob/105a8b2f69ffd8438532d7c9eb959ed26a567675/packages/core/src/components/ui/Image/Image.tsx) component to optimize image performance on your storefront. This component uses [Thumbor](https://www.thumbor.org/) for image resizing and cropping, caching the results on a Content Delivery Network (CDN). Use it whenever you need to [create a new section for the Headless CMS](https://developers.vtex.com/docs/guides/faststore/building-sections-creating-a-new-section).

```tsx mark=2
import { HeroImage as UIHeroImage } from '@faststore/ui'
import { Image_unstable as Image } from '@faststore/core/experimental'

export default function CustomHeroImage() {
  return (
    <UIHeroImage>
      <Image
        src="https://storeframework.vtexassets.com/arquivos/ids/160965/est.jpg?v=637752924295370000"
        alt="Two puffs and two small desks placed together, accompanied by various color pencils."
        width={360}
        height={240}
        sizes="(max-width: 360px) 50vw, (max-width: 768px) 90vw, 50vw"
      />
    </UIHeroImage>
  )
}
```