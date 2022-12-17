---
title: "Categories"
slug: "categories"
hidden: false
createdAt: "2021-12-10T21:47:46.801Z"
updatedAt: "2022-11-22T17:13:51.833Z"
---
The category tree is the backbone of the Catalog, so it needs to be carefully planned and validated before importing to VTEX.

We strongly recommend starting to work on the category tree by creating a table similar to this one:

![Category tree table example](https://files.readme.io/8b98f38-tabela_2.PNG)

The idea behind this template is to allow easy visualization of how the tree is organized and how the specifications are being presented.

## Category inheritance

All specifications registered in the upper levels of the hierarchy are inherited by the lower categories. In the example above, we have what we call the root category "level zero". This means that all specs registered at this level (Gender, Simple Color, and Country) will be inherited by level 1.

Note that the Shirt category (level 2) has the `Style` field as a specification. This means that the product contained in this category will have as attributes the `Style` field and all others defined in the upper level, in this case, the root level.

Products must be associated with the categories at the lowest level of the category tree. In this example, they must be associated with the category: `Jeans` with `Pants` or `Polo` with `Shirt`.

## Limitations
- **Number of categories:** VTEX does not limit the number of categories that can be created.
- **Number of category levels:** VTEX supports more than three levels of categories but we strongly recommend having a maximum of three.

## FAQ
See below the answer to some frequently asked questions.

### When should I choose to import categories manually or by an integration via API?
It is not common for the customer to change the category tree once it is defined. Usually, specific changes may be required and can be made manually under VTEX Admin rather than having one more integration to take care of. Potentially we can find some cases where the category tree is built progressively according to the evolution of the store. But this typically happens during the validation of a new business. In that case, having category integration can be useful.

### What category fields are actually used by VTEX Intelligent Search?
- Title
- Description

### What are the best practices for Title and Meta Tag Description for SEO?
- The Title should be about 55 to 60 characters long. 
- When writing the Meta Tag Description, aim for about 1-2 sentences (140-160 characters) long. Offer a compelling reason to visit the webpage. Add a clear call to action, address an emotional pain point, or offer a specific benefit to visitors.
[block:callout]
{
  "type": "warning",
  "body": "Department, Category, and Subcategory titles can be customized using the VTEX Intelligent Search. So on the search navigation bar, the store can present different titles for each category level."
}
[/block]
## Pitfalls

- **Deleting categories:** Due to some relationships that categories have with other parts of the catalog, such as products, specifications, and collections, you cannot delete categories unless you clear the entire catalog.
- **Moving categories**: Although it is possible to move categories to different levels (higher/lower) and/or different departments, this is too risky because of the specifications attached to this category.  This action can create a mess with products because they will inherit not only the previous specifications but also the new ones. We recommend following the workaround described on the Help Center article [Deactivating and reorganizing categories](https://help.vtex.com/en/tutorial/deactivating-and-reorganizing-categories--tutorials_264#changing-the-category-tree).
- **Activating category:** Do not forget to activate the categories, otherwise products will not be indexed and thereafter will not be displayed on the website.

## API integration

To create a category, check our [Create a category](https://developers.vtex.com/vtex-rest-api/docs/create-a-category) guide.