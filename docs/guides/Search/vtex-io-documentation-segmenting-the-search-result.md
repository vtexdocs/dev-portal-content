---
title: "Segmenting the search result"
slug: "vtex-io-documentation-segmenting-the-search-result"
hidden: false
createdAt: "2021-12-29T16:02:23.423Z"
updatedAt: "2024-02-23T07:17:44.718Z"
---

In some situations, such as B2B accounts, you may want to present custom search results for each of your customers. To this end, this tutorial will guide you on how to segment the search result page of your store.

Take the following example in which different results for the same search are obtained based on the customer's email.

![Segmented Catalog B2B](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-segmenting-the-search-result.gif)

> ⚠️ This app only works on your store's final domain when the customer is logged in. If the customer navigates without authentication, the filter will not be inserted into their session. Note that, in the `myvtex` environment, the app always functions because authentication is enforced at all times.

> ⚠️ If you are using the [B2B Suite](https://developers.vtex.com/docs/guides/vtex-b2b-suite) solution, the configuration described in this guide is not necessary, because the [B2B Organizations](https://developers.vtex.com/docs/guides/vtex-b2b-organizations) app allows product collections to be assigned to organizations.

## Instructions

To create segmented search results, we'll create a new VTEX IO app from the [`vtex.search-segment-resolver`](https://github.com/vtex-apps/search-segment-resolver) boilerplate and customize it to establish our own segmentation rules.

1. Clone the `vtex.search-segment-resolver` app into your machine:

   ```sh
   git clone https://github.com/vtex-apps/search-segment-resolver
   ```

2. Open the `search-segment-resolver` project in any code editor of your preference.
3. Go to the `manifest.json` file and replace the `vendor` value with the name of your VTEX account.
4. Go to the `node/resolvers` folder and open the `searchSegment.ts` file.

   > ℹ️ The `segmentSearch` function is responsible for providing a JSON array of facets. For example, if you want to segment the search by the `shoes` category, the `segmentSearch` function returns `[{"key": "category-1", "value": "shoes"}]`.
5. Replace the `searchSegment` definition with your own segmentation rules. Take the following example in which we segmented the search result to filter by the `123`collection for `vtex.com.br` emails and by the `456` collection otherwise:

   ```ts
   export const queries = {
      searchSegment: async (ctx: any, args: SearchSegmentInput, __: Context) => {
        const userEmail = args.userEmail
        const domain = userEmail.split('@')[1]
 
        return domain === 'vtex.com.br' ? [{ key: 'productClusterIds', value: '123' }] : [{ key: 'productClusterIds', value: '456' }]
      },
   }
   ```

   Notice that the `searchSegment` function receives the `args` variable, which has the `SearchSegmentInput` type:

   ```ts
   interface SearchSegmentInput {
      // User email
      userEmail?: string
      // Whether the user is authenticated or not
      isAuthenticated?: boolean
      // Array of selected facets (optionally you can control it by the session itself)
      selectedFacets?: SelectedFacet[]
   }
   ```
   
   > ⚠️ Filtering by facets in the final domain requires adding the facet to the `public` namespace, a configuration that this app does not handle by default. You need to ensure this step is completed manually by following the [Sessions System](https://developers.vtex.com/docs/guides/sessions-system-overview#changing-information-from-a-session) guide if required.

6. [Create a development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace) and [link your app](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) to test if your segmentation rules are working as expected.
7. Once you finish your tests, follow all the necessary steps to [make your app publicly available](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available) before promoting it to master.
