---
title: "Create a category"
slug: "create-a-category"
hidden: false
createdAt: "2022-03-16T18:40:49.494Z"
updatedAt: "2022-03-16T18:40:49.494Z"
---
Categories organize your product assortment within your ecommerce. They work as hierarchical levels of product classification, making your client’s search for a product easier and keeping your store organized. 

Creating a category is the most basic configuration you must do in Catalog. For a product to exist, it must have a category associated with it. 

To create a category, one can use the [Create category](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-category) endpoint. See the request body example below of the creation of a category called Clothing:

**Request body**

```json
{
    "Name": "Clothing",
    "FatherCategoryId": null,
    "Title": "Clothing",
    "Description": "Shop from brands like Patagonia, The North Face, Billabong, Columbia, and more to dress yourself for success.",
    "Keywords": "Clothing,apparel,clothes, clothing department",
    "IsActive": true,
    "ShowInStoreFront": true,
    "ShowBrandFilter": true,
    "ActiveStoreFrontLink": true,
    "GlobalCategoryId": 772,
    "StockKeepingUnitSelectionMode": "SPECIFICATION",
    "Score": null
}
```

**Response body**

```json
{
    "Id": 2000089,
    "Name": "Clothing",
    "FatherCategoryId": null,
    "Title": null,
    "Description": "Shop from brands like Patagonia, The North Face, Billabong, Columbia, and more to dress yourself for success.",
    "Keywords": "Clothing,apparel,clothes, clothing department",
    "IsActive": true,
    "ShowInStoreFront": true,
    "ShowBrandFilter": true,
    "ActiveStoreFrontLink": true,
    "GlobalCategoryId": 772,
    "StockKeepingUnitSelectionMode": "SPECIFICATION",
    "Score": null,
    "LinkId": null,
    "HasChildren": false
}
```

In this example, the created category is a parent category, which means that it is not inside another category. A *parent category* can have subcategories, or *children categories*, associated with it. To create a subcategory, you must insert the parent category ID on the `"FatherCategoryId"`. 

[block:callout]
{
  "type": "warning",
  "body": "You cannot delete a category unless you make a [full cleanup](https://help.vtex.com/en/tutorial/database-maintenance-full-cleanup--34P9LGs7BCIQK6acQom802) of the catalog."
}
[/block]
## Edit a category

You can edit an existing category by using the [Update Category](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-put-category) endpoint.

## Get category tree

You can get information of all the category tree or just some specific level by using the [Get Category Tree](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-category-tree) endpoint.

##Get a category

You can get information about a specific category by using the [Get Category by ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-category)
 endpoint.