---
title: "FastStore: Improved search query with the `sponsoredCount` parameter"
slug: "2024-12-20-new-sponsored-count-parameter"
hidden: false
type: "added"
createdAt: "2024-12-20T00:00:00.219Z"
excerpt: "FastStore projects now include a new parameter to improve the management of sponsored product search results."
---

We've added a new parameter, `sponsoredCount`, to the search query. This parameter gives more control over the number of sponsored products returned in your store’s search results.

> ⚠ Extension API users: If you are using the [`ClientProductGallery`](https://developers.vtex.com/docs/guides/faststore/api-extensions-extending-queries-using-fragments#clientproductgalleryquery) fragment, this change may cause errors. Make sure your implementation is updated to handle the `sponsoredCount` parameter accordingly by following the instructions in the [next section](#api-extension-users).

## What needs to be done?

To have the new parameter enabled in your project, follow these steps:

1. Open your FastStore project using your preferred code editor.
2. Update your FastStore project to version `3.0.157` or later, by running the following:

   ```bash
   yarn upgrade -L --scope @faststore
   ```

3. Run `yarn build`.

### API extension users

If you are using the [`ClientProductGallery`](https://developers.vtex.com/docs/guides/faststore/api-extensions-extending-queries-using-fragments#clientproductgalleryquery) fragment, after updating the store version to the latest one, you may encounter the following error:

```bash
[FAILED] GraphQL Document Validation failed with 1 errors;
[FAILED]   Error 0: Fields "search" conflict because they have differing arguments. Use different aliases on the fields to fetch both if this was intentional.
[FAILED]     at /Users/fanny.chien/Work/faststore.store/.faststore/src/sdk/product/usePageProductsQuery.ts:11:5
[FAILED]     at /Users/fanny.chien/Work/faststore.store/.faststore/src/sdk/product/usePageProductsQuery.ts:3:5
[SUCCESS] Generate outputs
Running lifecycle hook "afterStart" scripts...
```

To fix it, follow these steps:

1. Go to the file where you are using the `ClientManyProducts` fragment, and add the missing `sponsoredCount` parameter.

    ```ts mark=8
    import { gql } from "@faststore/core/api";

    export const fragment = gql(`
    fragment ClientManyProducts on Query {
    search(
        first: $first
        after: $after
        sort: $sort
        term: $term
        selectedFacets: $selectedFacets
        sponsoredCount: $sponsoredCount  // Add this parameter!
    ) {
        … 
    }
    }
    `);
    ```

2. Save the changes.
3. Run `yarn build` once again.
