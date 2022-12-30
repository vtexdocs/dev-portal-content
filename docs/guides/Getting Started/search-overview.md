---
title: "Search"
slug: "search-overview"
hidden: false
createdAt: "2022-04-28T19:54:24.451Z"
updatedAt: "2022-09-13T20:26:18.916Z"
---
[block:html]
{
  "html": "<style>\n    .markdown-body .callout[theme=\"📣\"] {\n    --icon: \"\\f0a1\";\n    --icon-color: #142032;\n    --border: #142032;\n    --background: #f8f7fc;\n    --text: #4a596b;\n    }\n  </style>\n  <blockquote class=\"callout callout_loudspeaker\" theme=\"📣\">\n    <h3 class=\"callout-heading\"><span class=\"callout-icon\">📣</span>Help us improve our documentation! </h3>\n      <p>\n      Tell us about your experience with this article by filling out <button style=\"background-color:transparent;color:#f71963;text-decoration:underline;border:none;padding:0;cursor:pointer;font-size: var(--markdown-font-size,14px);\" onclick=\"closeModal()\">this form.</button>\n      </p>\n  </blockquote>"
}
[/block]
Intelligent Search is a [VTEX IO](https://vtex.com/us-en/store-framework/) alternative to Legacy Search. It assists the customer in their purchase journey and presents results from the first interaction with the search bar. The tool displays search and product suggestions that may interest the user. Intelligent Search also corrects spelling errors and understands words not contained in the product information.

## Setting up the Intelligent Search

### Search

The [VTEX Search app](https://developers.vtex.com/vtex-developer-docs/docs/vtex-search) is responsible for handling the new [Intelligent Search](https://help.vtex.com/tracks/vtex-intelligent-search) solution in IO stores by providing new UI components that enhance the search experience, such as the autocomplete feature.

![Search app](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/search-overview-0.gif)

### Intelligent Search API

The [Intelligent Search API](https://developers.vtex.com/vtex-rest-api/reference/intelligent-search-api-overview) allows you to consult the information about the user's search in your store and its terms. You can also access information about banners, facets, and suggested terms.

## Customizing the search experience of your store

### Search Result

[VTEX Search Result app](https://developers.vtex.com/vtex-developer-docs/docs/vtex-search-result) is responsible for handling the result fetched by the [VTEX Search API](https://developers.vtex.com/vtex-developer-docs/reference/search-api-overview) and displaying it to users. The app exports all store blocks expected in a search results page, such as the filters and the product gallery.

![Search Result](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/search-overview-1.png)

### Search Bar

The [Search Bar component](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-searchbar) shows a search bar with autocomplete options and displays the matching products.

![Search Bar](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/search-overview-2.png)

### Autocomplete

The [Autocomplete](https://developers.vtex.com/vtex-developer-docs/docs/vtex-search-autocomplete) is an alternative for the default VTEX autocomplete. The functionality displays previous search results based on current and previous searches. These results are presented in four different lists, which can be together or separated, depending on the customer's interaction.

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/search-overview-3.png)

### Banners

[Banners](https://developers.vtex.com/vtex-developer-docs/docs/vtex-search-banner) are the functionality responsible for displaying banners as promotional actions on the customer's search result page. This process is done by associating the words and filters selected when searching for these banners.

### Suggestions

[Suggestions](https://developers.vtex.com/vtex-developer-docs/docs/vtex-search-suggestions) is a component used to suggest search terms similar to the current query.

### DidYouMean

[DidYouMean](https://developers.vtex.com/vtex-developer-docs/docs/vtex-search-didyoumean) is a component used to suggest a possible misspelling correction to the current query.

## Search Control

The [Search Control](https://developers.vtex.com/vtex-rest-api/docs/search-control-fulltextsearchbox) control is responsible for generating the search box. Besides the search filed, the control renders a combo for restricting a search in one department.

## Customizing the search result

You can provide your customers with a more customized experience navigating the search result. You may want to present custom search results for each customer or even engage your users with specific products through an URL.

* [Segmenting the search result](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-segmenting-the-search-result)
* [Building a search results page with multiple layouts](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-building-a-search-results-page-with-multiple-layouts)
* [Creating a custom search results page](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-creating-a-custom-search-results-page)

![Segmenting the search result](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/search-overview-4.gif)

## Integrating an external search provider with VTEX

The [Search Protocol](https://developers.vtex.com/vtex-rest-api/docs/search-integration-guide) defines the contract between an external search provider and a VTEX store running on VTEX IO. If a search provider adheres to this protocol, it can completely replace the original VTEX search capabilities without needing to implement any front-end pages or react components.

* [Overview](https://developers.vtex.com/vtex-rest-api/docs/external-search-provider-overview)
* [Specification](https://developers.vtex.com/vtex-rest-api/docs/external-search-provider-specification)
* [Recipe](https://developers.vtex.com/vtex-rest-api/docs/external-search-provider-recipe)
* [Reference Implementations](https://developers.vtex.com/vtex-rest-api/docs/external-search-provider-reference)

## Integrating your search with Google services

You can integrate your store's search to some Google features, such as the Google Chrome language processing and Google Analytics. These integrations can help retailers analyze user queries, measure the store's main searched terms, and create a more accessible environment for customers.

* [Search Console](https://developers.vtex.com/vtex-developer-docs/docs/vtex-google-search-console)
* [Setting up Google Analytics search tracking](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-setting-up-google-analytics-search-tracking)
* [Speech to Text Search](https://developers.vtex.com/vtex-developer-docs/docs/vtexarg-speech-to-text)

## Consulting search information using Legacy Search

You can consult, search and sort products in the catalog using fulltext, category, and brand search terms.

* [How search parameters work](https://developers.vtex.com/vtex-rest-api/docs/how-search-parameters-work)

### Search API

* [CrossSelling](https://developers.vtex.com/vtex-rest-api/reference/productsearchwhosawalsosaw)
* [Search](https://developers.vtex.com/vtex-rest-api/reference/productsearch)
* [Offers](https://developers.vtex.com/vtex-rest-api/reference/get_api-catalog-system-pub-products-offers-productid)
* [Facets](https://developers.vtex.com/vtex-rest-api/reference/get_api-catalog-system-pub-facets-category-categoryid)
* [Autocomplete](https://developers.vtex.com/vtex-rest-api/reference/autocomplete)
