---
title: "SearchProvider"
createdAt: "2025-02-18T19:02:14.003z"
---

`SearchProvider` is a React component that wraps an entire page, such as a Product Listing Page, to provide the necessary context for the faceted search. Faceted search allows users to filter and refine search results based on specific attributes (such as price, category, brand, etc.).

## Import

```tsx
import { SearchProvider } from '@faststore/sdk'
```

## Usage

The following example demonstrates how to implement faceted search using `SearchProvider`:

```tsx
import { SearchProvider, parseSearchState } from '@faststore/sdk'

function Page () {
  const params = useMemo(() => parseSearchState(new URL(window.href)), [])

  return (
    <SearchProvider
      onChange={(url: URL) => window.location.href = url.href}
      itemsPerPage={12}
      {...params}
    >
      {children}
    </SearchProvider>
  )
}
```

- `SearchProvider`: React component that provides search context.
- `parseSearchState`: Parses the current URL and extracts the search state (such as `sort`, `term`, `page`, etc.).
- `children`: Components wrapped by `SearchProvider`, which will have access to the search context.

## Props

The `SearchProvider` component accepts the following props:

| Prop | Type | Description |
| -------- | --------------- | ------------ |
| `onChange` | `(url: URL) => void` | Callback function that handles changes in the facet state. It updates the page URL when search parameters change. |
| `itemsPerPage` | `number` | Number of items displayed on a given page. |
| `sort` | `SearchSort` | Sorting criteria of the search result (such as `price_asc`, `orders_desc`, `discount_desc`, etc.). |
| `term` | `string / null` | Full-text term used in the search. |
| `page` | `number` | Current page index in search pagination. |
| `base` | `string` | Base URL path of the search page. Useful for localization and prefixing paths by locale (such as `/en-us/`). |
| `selectedFacets` | `Array<{ key: string, value: string }>` | Array of selected facets in the search. |
| `passThrough` | `URLSearchParams` | Additional URL parameters to preserve when building URLs. |

> ⚠ Don't include personalization facets, such as sales channel and price tables, in the `selectedFacets` property. Doing so may result in users having two channels — one from the Session context and another from the URL — which may lead to unexpected behavior.
