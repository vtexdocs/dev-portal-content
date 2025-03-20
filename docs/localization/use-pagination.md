---
title: "usePagination"
createdAt: "2025-02-18T19:02:14.003z"
---

The `usePagination` hook provides the pagination links (`next`/`prev`) for navigating through search results. These links can be used with the `<link />` tag to improve SEO and user experience by indicating the relationship between pages (example: `rel="next"` and `rel="prev"`).

## Import

```tsx
import { usePagination } from '@faststore/sdk'
```

## Usage

The following example demonstrates how to implement a paginated navigation system using `usePagination`:

```tsx
import { usePagination } from '@faststore/sdk'

function Component () {
  const totalProducts = 100 // Total number of products returned by the search query
  const { next, prev } = usePagination(totalProducts)

  return (
    <>
      {prev && (
        <a href={prev.link} rel="prev">
          Previous Page
        </a>
      )}
      {next && (
        <a href={next.link} rel="next">
          Next Page
        </a>
      )}
    </>
  )
}
```

- `usePagination`: Generates pagination links (`next` and `prev`) based on the total number of products in the search results.
- `totalProducts`: Total number of products returned by the search query. This value is used to calculate the pagination links.
- `rel="prev"` and `rel="next"`: Help search engines understand the relationship between pages, improving SEO.

## API reference

The `usePagination` hook returns an object containing `next` and `prev` pagination links:

| Variable name | Data type | Description |
| -------- | --------------- | ------------ |
| `prev` | `{ cursor: number; link: string}` / `false` | Object containing the cursor position and link for the previous page of the search result. If there's no previous page, this value will be `false`. Example: `{ cursor: 10, link: '/search?page=10' }`. |
| `next` | `{ cursor: number; link: string}` / `false` | Object containing the cursor position and link for the next page of the search result. If there's no next page, this value will be `false`. Example: `{ cursor: 20, link: '/search?page=20' }`. |
