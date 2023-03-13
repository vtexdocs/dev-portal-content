---
title: "Get banner list for a specific search"
slug: "get-banner-list-for-a-specific-search"
hidden: false
createdAt: "2022-10-14T21:11:36.747Z"
updatedAt: "2022-11-02T14:39:45.843Z"
---

It is possible to display banners as promotional actions on the customer's search result page. This process is done through an association between the words and facets that represent filters selected when making a search. For more information on how to configure a banner, check the [Configuring Banners](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/4ViKEivLJtJsvpaW0aqIQ5#) article.

To retrieve a list of banners for a specific search, use the [Get list of banners registered for query](https://developers.vtex.com/vtex-rest-api/reference/get_banners-facets) endpoint. You can filter the endpoint response by defining the search’s `facets` and the term's `locale` and `query`.

**Response body example:**

```json
{
  "banners": [
	{
  	"id": "summersale",
  	"name": "Summer Sale",
  	"area": "1",
  	"html": "<h1>This is a test</h1>"
	}
  ]
}
```