---
title: "How search parameters work"
slug: "how-search-parameters-work"
hidden: false
createdAt: "2022-09-12t20:50:49.238z"
updatedAt: "2022-09-15t18:56:45.172z"
---

> ⚠️ VTEX has two search options: Legacy Search and Intelligent Search. This article is about Legacy Search. To learn more about the Intelligent Search application, see [this track](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb).

When making a search on VTEX, there are different options for URLs. The URLs of departments and categories are formatted according to the category tree.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/how-search-parameters-work-0.png)

For example, in the category tree above, the URLs are the following:

- `www.store.com/clothes`
- `www.store.com/clothes/women`
- `www.store.com/clothes/women/shirts`

The URL will always contain the term entered in the search field:

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/how-search-parameters-work-1.png)

`www.store.com/shoes`

The browsing filters also have specific URLs defined by certain parameters in the URL, which can follow one of these options:

* [Default 1](#default-1): Valid only for Legacy CMS Portal stores.
* [Default 2](#default-2): Valid for Legacy CMS Portal and VTEX IO stores. Recommended for best performance results.

## Default 1

> ⚠️ This option works only for Legacy CMS Portal stores. Refer to [Default 2](#default-2) for VTEX IO stores.

| URL |
| - |
| `www.store.com/busca/?fq=C:[DepartmentId/CategoryId/SubcategoryId]&fq=B:[BrandId]&fq=H:[CollectionId]&fq=specfct[ProductFieldId/Sku]:[SearchValue]&ft=[SearchTerm]` |

Where:

- **C:\[DepartmentId/CategoryId/SubcategoryId]:** Shows products of a specific category based on the IDs indicated for the department, category, and subcategory. This code appears next to category names in **Products** > **Catalog** > **Categories**. ![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/how-search-parameters-work-2.png)

  > ℹ️ The category ID can also be found on your edit page at the end of the URL.

- **B:[BrandId]:** Shows products from a specific brand based on the indicated ID. This code is shown at the end of the URL, on the page used for changing the brand, in**Products**>**Catalog**>**Brands**. ![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/how-search-parameters-work-3.png)
- **H:[CollectionId]**: Shows products of a specific collection based on the indicated ID. This code is indicated when editing a collection in**Store setup** > **CMS** > **Layout** > **CMS** > **Product Clusters (Collections)**. ![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/how-search-parameters-work-4.png)

  > ⚠️ There are two ways to configure collections: through the CMS or the Collections module (Beta). This article explains how to [configure collections through the CMS](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).

- **spec_fct_[ProductFieldId/Sku]:[SearchValue]:** Shows products whose product or SKU field value, with the indicated ID, is equal to the entered value. This code can be found on the page for changing a product/SKU field at the end of the URL.

  ```txt
  https://store.myvtex.com/admin/Site/ProdutoForm.aspx?id=93
  ```

  Below is an example of how to use this field:

  ```txt
  www.store.com.br/busca/?fq=spec_fct_1:110v
  ```

  In the example above, all products whose **Voltage**(ID **1**) field is **110v** would be displayed.

- **ft=[SearchTerm]**: This parameter represents a full-text search (for example, searching a specific term in the search field) of the specified term based on the other indicated parameters.

The parameters above can be matched in many ways. However, note that the search order will follow the order of the indicated parameters. In other words, when you use a category parameter followed by a brand parameter, the category will be searched first. Then, a second search will be made for the brand among the category results.

## Default 2

> ℹ️ Stores hosted in VTEX IO must use Default 2.

| URL                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------- |
| `www.store.com.br/[CategoryName]/[BrandName]/[CollectionId]/[SearchValue]?map=c,b,productClusterIds,specificationFilter_[ProductFieldId/Sku]` |

Where:

- **/[CategoryName]?map=c**: Displays products whose category is specified by the name indicated in the URL.

- **/[BrandName]?map=b**: Displays products whose brand is specified by the name indicated in the URL.

- **/[CollectionId]?map=productClusterIds**: Displays products whose collection is specified by the ID indicated in the URL.

- **[SearchValue]?map=specificationFilter_[ProductFieldId/Sku]**: Displays products whose product/SKU field value, with the indicated ID, is equal to the entered value.

The parameters above can also be matched among them. The order of the values indicated in the `map` parameter will define the interpretation of each value present at the beginning of the URL (between `/`).
