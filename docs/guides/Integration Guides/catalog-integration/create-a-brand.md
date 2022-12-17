---
title: "Create a brand"
slug: "create-a-brand"
hidden: false
createdAt: "2022-11-30T21:02:15.884Z"
updatedAt: "2022-11-30T21:02:15.884Z"
---

[Brands](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/7i3sB8fgkqUp5NoH5yJtfh) work as product attributes that help end customers to identify a product and the business behind it.

A product needs to be associated with one brand to exist. Therefore, creating a Brand is a mandatory step when configuring your Catalog. Usually, it is the second step for catalog integration, after creating categories. For more information on Catalog structure and integration flow at VTEX, check our [Catalog overview](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview).

To create a brand, use the [Create Brand](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-brand) endpoint. In this endpoint, the request and the response follow the same structure. See the example below:

**Request and response body example**

```json
{
  "Id": 2000013,
  "Name": "Orma Carbon",
  "Text": "Orma Carbon",
  "Keywords": "orma",
  "SiteTitle": "Orma Carbon",
  "Active": true,
  "MenuHome": true,
  "AdWordsRemarketingCode": "",
  "LomadeeCampaignCode": "",
  "Score": null,
  "LinkId": "orma-carbon"
}
```

## Edit a brand

You can edit an existing brand by using the [Update Brand](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-put-brand) endpoint with the same request body structure as to create a brand. The only non-editable information is the Brand ID.

## Get brand list

You can get information about all the brands configured in your store by placing a request to one of the following endpoints:

- [Get Brand List](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-brand-list): Full list of brands in your store. This route's response is limited to 20k results. If you need to obtain more results, please use the [Get Brand List per page ](https://developers.vtex.com/vtex-rest-api/reference/brandlistperpage)endpoint instead to get a paginated response.
- [Get Brand List per page](https://developers.vtex.com/vtex-rest-api/reference/brandlistperpage): Paginated list of brands in your store.

## Get brand

You can retrieve information about a specific brand by making a request to [Get Brand](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-brand).

## Delete a brand

To delete a brand, use the [Delete Brand](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-delete-brand) endpoint. This action is permanent and cannot be undone.
