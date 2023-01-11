---
title: "Implementing a Custom Search Resolver App"
slug: "external-search-provider-recipe"
hidden: false
createdAt: "2020-09-11T16:53:56.507Z"
updatedAt: "2020-10-30T20:45:34.170Z"
---

Supposing you want to integrate another search provider into VTEX, here are the steps you should follow to create an app that follows the VTEX Search Protocol:

1. Clone the VTEX Intelligent Search search resolver app: [https://github.com/vtex-apps/search-resolver/tree/v1.x](https://github.com/vtex-apps/search-resolver/tree/v1.x).
2. **TEMPORARY:** Uninstall any other search-resolver app that may be installed on the account you're using (`e.g: vtex.search-resolver@0.x`). You may need to do this in a separate workspace if the store is live
3. Change the `vendor` field on the app's `manifest.json` to map the account you're using.
4. Start changing the queries' resolvers implementations to retrieve and return the data from the external search engine you're integrating.

## Client

In VTEX IO, we have the concept of clients to abstract calling other services in a centralized class. If you've cloned the search resolver listed above, you will see that it grabs data by using the following client: [https://github.com/vtex-apps/search-resolver/blob/v1.x/node/clients/biggy-search.ts](https://github.com/vtex-apps/search-resolver/blob/v1.x/node/clients/biggy-search.ts). Change the implementation of this client to fetch data from the search provider that you want to integrate with.

## Resolvers

The main resolver file that you need to change is this [https://github.com/vtex-apps/search-resolver/blob/v1.x/node/resolvers/search/index.ts](https://github.com/vtex-apps/search-resolver/blob/v1.x/node/resolvers/search/index.ts). You can look for occurrences of `biggySearch` and change the data treatment to get the wanted behavior. Remember that you may want to leave some resolvers untouched and continue grabbing data from VTEX Catalog's APIs.

### Tips on Working with the Example

- Entries and files with `BiggySearchClient` should be modified and renamed accordingly to the search engine to be integrated.
- The main file to look at is `node/resolvers/search/index.ts`, where is implemented resolvers for search-related queries. It's important to notice that some resolvers **will not be modified** since they're connecting directly to VTEX APIs. This will be addressed on future releases of VTEX Search Protocol. You can find a list of all the queries to change the implementation in the specification section of this document.
- It's important to adapt the Typescript types into the code, because they're specific to VTEX Search.

## Troubleshooting

In case of any "Unknown errors", check if the version on `node/package.json` for the dependency `vtex.search-graphql` is up to date with the [latest version for the vtex.search-graphql app](https://github.com/vtex-apps/search-graphql/blob/master/manifest.json#L4). After changing the version on the URL, you need to run `yarn` inside the **node** folder before running `vtex link` again.
[block:html]
{
  "html": "<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css\" integrity=\"sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm\" crossorigin=\"anonymous\">\n<script src=\"https://code.jquery.com/jquery-3.2.1.slim.min.js\" integrity=\"sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN\" crossorigin=\"anonymous\"></script>\n<script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js\" integrity=\"sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q\" crossorigin=\"anonymous\"></script>\n<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js\" integrity=\"sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl\" crossorigin=\"anonymous\"></script>\n\n\n<a href=\"search-integration-guide\"<button type=\"button\" class=\"btn btn-outline-secondary\">Back</button></a>\n\n<style></style>"
}
[/block]