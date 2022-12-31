---
title: "How search parameters work"
slug: "how-search-parameters-work"
hidden: false
createdAt: "2022-09-12T20:50:49.238Z"
updatedAt: "2022-09-15T18:56:45.172Z"
---

> ⚠️ VTEX has two search options - Legacy Search and Intelligent Search. This article refers to the Legacy Search. To learn more about the Intelligent Search application, see [this track](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb).

When making a search on VTEX, there are different possibilities of URLs. The URLs of Departments and Categories are made up as follows:

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Search/how-search-parameters-work-0_17.png)

In the categories tree above, the links are as follows:

- `www.store.com/clothes`
- `www.store.com/clothes/women`
- `www.store.com/clothes/women/shirts`

The URL will always be made up with the term entered in the search field:

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Search/how-search-parameters-work-1_25.png)

`www.store.com/shoes`

The browsing filters also have specific URLs that are defined by certain parameters in the URL. These parameters are as follows:

## Default 1

|URL|
|-----|
|`www.store.com/busca/?fq=C:[DepartmentId/CategoryId/SubcategoryId]&fq=B:[BrandId]&fq=H:[CollectionId]&fq=specfct[ProductFieldId/Sku]:[SearchValue]&ft=[SearchTerm]`|

Where:

- **C:\[DepartmentId/CategoryId/SubcategoryId]**: shows products of a specific category, according to the IDs informed for the department, category, and subcategory. This code appears next to category names on **Products**>**Catalog**>**Categories**.
  ![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Search/how-search-parameters-work-2_46.png)

> ℹ️ The category ID can also be found on your editing page, at the end of the URL.

- **B:[BrandId]:** shows products of a specific brand, according to the ID informed. This code is shown at the end of the URL, on the page used for changing the brand, in **Products**>**Catalog**>**Brands**.
  ![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Search/how-search-parameters-work-3_56.png)
- **H:[CollectionId]**: shows products of a specific collection, according to the ID informed. This code is informed in collection editing, in **Store setup**>**CMS**>**Layout**>**CMS**>**Product Clusters (Collections)**.
  ![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Search/how-search-parameters-work-4_58.png)

> ⚠️ There are two ways to configure collections, through the CMS or the Collection module (Beta). This article is about how to [configure collections through the CMS](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).

- **spec_fct_[ProductFieldId/Sku]:[SearchValue]:** shows products whose product or SKU field value, with the indicated ID, is equal to the value informed. This code can be found on the page used for changing a product/SKU field, at the end of the URL.

```txt
https://store.myvtex.com/admin/Site/ProdutoForm.aspx?id=93
```

See below an example of the use of this field:

```txt
www.store.com.br/busca/?fq=spec_fct_1:110v
```

In the example above, all products whose **Voltage**(ID **1**) field is **110v** would be shown.

- **ft=[SearchTerm]**: This parameter represents a fulltext search (*Example: search of a specific term in the search field*) of the term specified according to the other parameters informed.

The parameters above can be matched in many ways. However, notice that the search order will be according to the order of the parameters informed. In other words, when you use a category parameter followed by a brand parameter, for example, the category will be searched first and, among the results found, a second search will be made for the brand.

## Default 2

> ℹ️ For stores hosted in VTEX IO, Default 2 should be used as standard.

|URL|
|---|
|`www.store.com.br/[CategoryName]/[BrandName]/[CollectionId]/[SearchValue]?map=c,b,productClusterIds,specificationFilter_[ProductFieldId/Sku]`|

Where:

- **/[CategoryName]?map=c**: shows products whose category is specified by the name informed in the URL.

- **/[BrandName]?map=b**: shows products whose brand is specified by the name informed in the URL.

- **/[CollectionId]?map=productClusterIds**: shows products whose collection is specified by the ID informed in the URL.

- **[SearchValue]?map=specificationFilter_[ProductFieldId/Sku]**: shows products whose product/SKU field value, with the indicated ID, is equal to the value informed.

The parameters above can also be matched among them. The order of the values informed in the `map` parameter will define the interpretation of each value present at the beginning of the URL (between `/`).

> ℹ️ For the best performance of your store, we recommend using the [Default 2](https://developers.vtex.com/vtex-rest-api/docs/how-search-parameters-work#default-2) case.
