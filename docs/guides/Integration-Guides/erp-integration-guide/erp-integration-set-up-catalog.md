---
title: Set up catalog
slug: erp-integration-set-up-catalog
hidden: false
createdAt: 2020-03-11T20:58:09.345Z
updatedAt: 2022-05-04T13:47:44.670Z
---
In this step, we give you an overview of how to prepare your catalog structure to receive all of your products.

> While this article provides the basic flow of integration, we recommend you check the implementation details provided on our [Catalog integration guide](https://developers.vtex.com/docs/guides/catalog-integration), as well as each **Learn more** section below.

## Before you begin

Before uploading your entire catalog to VTEX it is very important to think carefully about your desired catalog structure. The way you structure your catalog and product specifications can have a great impact on site navigation, order integration and other aspects of your store.

Most VTEX stores structure their **Category Tree** into three hierarchical levels: **Departments**, **Categories** and **Subcategories**. Some stores might benefit from using only a two-level structure of Departments and Categories. You could even go as simple as only using Departments to segment your product assortment.

**Brands** are also an important aspect to consider, as it is very common for clients to search for products using them as a keyword. When brands are associated with products, you can use them as filters in your store navigation.

Each category in your store might also use **Specification Fields** to hold extra information needed to fully describe the Products or SKUs it contains. You should consider which fields would need to be associated with Products or SKUs for each category.

In the end, the goal is to make navigation easier for your customers and to improve the chance that all category and product pages on your website will be properly indexed. If you would like a conceptual overview of our Catalog, check out the [beginner track](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3rA2tTpIoEXdv2nzC27zxR) in our Help Center.

## Create Departments, Categories and Subcategories

To create your Category Tree, you should use the [Create Category](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/category) endpoint in the Catalog API. 

Start by creating your Departments, then your Categories, then your Subcategories. In between steps, you can use the [Get Category Tree](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/category/tree/-categoryLevels-) endpoint or visit the **Products > Catalog > Categories** section of your Admin panel to check on your progress. 


### Category migration from ERPs

The category tree is very important for your VTEX store and it is possible that the category structure represented in your Enterprise Resource Planning (ERP) software or Product Information Manager (PIM) is not optimized for that end. In this case, your ecommerce category tree may end up being different from the tree in your previous system.

If you find yourself in that situation, we recommend creating an inactive mock category called, for example, **Integration,** that will not be used in the storefront but can receive each and every product and SKU when importing. After all of your catalog has been imported, the products can be manually arranged into their new categories appropriate for your ecommerce. This can be done in the Admin or with a spreadsheet, with the [Google Drive Import app](https://github.com/vtex-apps/google-import).

> For more details, see our [Catalog categories integration guide](https://developers.vtex.com/docs/guides/categories).

## Create Brands

To add a new Brand to your catalog, you should use the [Create Brand](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/brand) endpoint in the Catalog API. 

Adding Brands to your catalog allows you to filter products in your storefront using this attribute. Brands need to be created before you can associate products with them, so it's a good idea to do this when setting up your catalog. You can use the [Get Brand List](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/brand/list) endpoint or visit the **Products > Catalog > Brands section** of your Admin panel to check on your progress.

>⚠️ If your backend does not have brand information, you can perform the same process mentioned above for [category migration](https://developers.vtex.com/docs/guides/erp-integration-set-up-catalog#category-migration-from-erps), by creating an inactive mock brand, used exclusively for migration. The products' information can later be manually enriched.

> For more details, see our [Catalog brands integration guide](https://developers.vtex.com/docs/guides/brands).

## Create Specifications Groups

To add Specification Groups to a category, you should use the [Create Specification Group](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/specificationgroup) endpoint in the Catalog API.

> Specification Fields are always grouped into Specification Groups. Because of that, you will need to create at least one Specification Group for each category that will need extra information to fully describe the Products or SKUs it contains.

Start creating Specification groups at the Departments level, then at the Categories level and finally at the Subcategories level. You can use the [List Specifications Groups by Category](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/specification/groupbycategory/-categoryId-) endpoint to check on your progress or visit the Specifications Group list for the category you're interested in by accessing the **Products > Catalog > Categories** section of your Admin panel.

>⚠️ Keep in mind that Specification Groups in a category are recursively applied to all its children in the Category Tree. If a field is not used by all children of a category, it should not be associated with one of its Specification Groups.

> For more details, see our [Catalog specifications integration guide](https://developers.vtex.com/docs/guides/specifications).

## Create Specification Fields

To add Specification Fields to a Specification Group, you should use the [Create Specifications Field](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog_system/pvt/specification/field) endpoint in the Catalog API.

Go through each of the Specification Groups you created previously and add the fields you need, one at a time. There are eight field types to choose from: 

1. Text
2. Multi-Line Text
3. Number
4. Combo
5. Radio
6. Checkbox
7. Indexed Text
8. Indexed Multi-Line Text.

> Specification Values must be specified for enumerated field types. If a Specification Field type is Combo, Radio or Checkbox, you will need to create Specification Values to represent the options that can be selected for that field.

> ℹFor more details, see our [Catalog specifications integration guide](https://developers.vtex.com/docs/guides/specifications).

## Create Specification Values

To add Specification Values to a Specification Field, you should use the [Create Specification Field Value](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog_system/pvt/specification/fieldValue) endpoint in the Catalog API.

Make sure you add Specification Values to all Specification Fields that require them - Combo, Radio and Checkbox. You can use the [Get Specifications Values By Field Id](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/fieldvalue/-fieldId-) endpoint to check on your progress. Alternatively, you can find the list of Specification Values for the Field you're interested in by following the steps below:

1. Open the *Products > Catalog > Categories* section of your Admin panel;
2. Select the Category where you created the Specification Field;
3. Click on the *Actions* dropdown and open the appropriate Field list (Product or SKU);
4. Find the Specification Field you're interested in (it should be an enumerated field type);
5. Click on the dropdown in the Edit column and open the Values list;
6. You should now be able to see the Specification Values you created for that Field.

> You can use the **Position** parameter to choose the order in which Specification Values are shown for enumerated field types. For example: if you want the Specification Value `110V` to show before `220V` in a `Voltage` Specification Field.

> For more details, see our [Catalog specifications integration guide](https://developers.vtex.com/docs/guides/specifications).

## Wrapping up

After following the instructions in this step, you should have set up your catalog, including the category tree, brands and specifications needed to completely describe your products. This should enable you to upload all your products in the next step.