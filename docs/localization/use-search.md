---
title: "useSearch"
createdAt: "2025-02-18T19:02:14.003z"
---

The `useSearch` hook provides access to the search context managed by the `SearchProvider` component. It enables reading and modifying the search state, such as sorting criteria, selected facets, and pagination. Use this hook to build interactive search features like sorting dropdowns, facet filters, and pagination controls.

## Import

```tsx
import { useSearch } from '@faststore/sdk'
```

## Usage

The following example shows how to implement a sorting dropdown using `useSearch`:

```tsx
import { useSearch } from '@faststore/sdk'

// Example: A sort dropdown to change the search sorting criteria

const keyMap = {
  price_desc: 'Price, descending',
  price_asc: 'Price, ascending',
  orders_desc: 'Top sales',
  name_asc: 'Name, A-Z',
  name_desc: 'Name, Z-A',
  release_desc: 'Release date',
  discount_desc: 'Discount',
  score_desc: 'Relevance',
}

const keys = Object.keys(keyMap)

function Component () {
  const {
    setSort,
    state: { sort },
  } = useSearch()

  return (
    <select
      onChange={(e) => setSort(keys[e.target.selectedIndex])}
      value={sort}
    >
      {keys.map((key) => (
        <option key={key} value={key}>
          {keyMap[key]}
        </option>
      ))}
    </select>
  )
}
```

`useSearch`: Accesses the search context to read and update the search state.
`keyMap`: Maps sorting keys to user-friendly labels.
`setSort`: Updates the sorting criteria.
`sort`: Contains the current sorting criteria from the search state.

## API reference

The `useSearch` hook returns an object with the following properties and functions:

| Variable name | Data type | Description |
| -------- | --------------- | ------------ |
| `itemsPerPage` | `number` | Number of items displayed per page. |
| `state` | `SearchState` | Contains the current state of the search, including selected facets, sorting criteria, and pagination. |
| `setSort` | `(sort: SearchSort) => void` | Updates the sorting criteria of the search results. |
| `setTerm` | `(term: string / null) => void` | Updates the full-text search term. |
| `setPage` | `(page: number) => void` | Updates the current page in the search pagination. |
| `removeFacet` | `(facet: Facet) => void` | Removes a specific facet from the search state. |
| `toggleFacet` | `(facet: Facet) => void` | Toggles a specific facet in the search state. If the facet is already selected, it will be removed; otherwise, it will be added. |
| `toggleFacets` | `(facets: Facet[]) => void` | Toggles multiple facets in the search state. |
| `addPrevPage` | `() => void` | Prepends a page of results to the current list (used in infinite scroll). |
| `addNextPage` | `() => void` | Appends a page of results to the current list (used in infinite scroll). |
