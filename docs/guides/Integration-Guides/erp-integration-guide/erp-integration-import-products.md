---
title: "Import products"
slug: "erp-integration-import-products"
hidden: false
createdAt: "2020-03-11T20:58:07.913Z"
updatedAt: "2022-08-24T18:33:17.132Z"
---
In this step, you will send all product information from your ERP or PIM to VTEX. 

>⚠️ While this article provides the basic flow of integration, we recommend you check the implementation details provided on our [Product integration guide](https://developers.vtex.com/docs/guides/products) and [SKU integration guide](https://developers.vtex.com/docs/guides/skus), as well as the links in each **Learn more** section below.

## Before you begin

Before importing all your products and SKUs to VTEX it is very important to think about how you plan to display variations in your shelves and product pages. In some cases, it might be useful to split similar SKUs into different products, in others you might want to group them under the same product.

In VTEX, a **Product** is the abstract catalog unit that is displayed to buyers when they browse your store. An **SKU**, on the other hand, is the concrete catalog unit that is held in stock and represents the different variations (color, size and anything else) buyers can choose from. 

In other words, Products are displayed on shelves, while SKUs are displayed on product pages.

Another factor that needs to be taken into account is the selection of images to represent your catalog. High quality images might make a product more appealing, but their size may also negatively impact page loading time. Planning and organizing your product assets is extremely important.

Finally, **Trade Policies** are used in VTEX to differentiate the catalog, prices and logistics settings for each sales channel connected to your store. In general you will add all your products to the main trade policy (used by your store) and optionally include other trade policies to expose specific products to other marketplaces.

Again, it is all about offering a great navigation experience to buyers, with fast page loading, detailed product pages and amazing visuals. If you would like a conceptual overview of our Catalog, check out the [beginner track](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3rA2tTpIoEXdv2nzC27zxR) in our Help Center. 

## Import product

VTEX provides three different ways to register products in the catalog:

1. API Integration: Read our [Catalog getting started guide](https://developers.vtex.com/docs/guides/catalog-overview) for an overview of the integration flow. Find the collection with all available methods on [Catalog API Overview](https://developers.vtex.com/docs/guides/catalog-api-overview).
2. Spreadsheet:
   - Google Drive Import: Import the catalog from a single Google Drive file. See the [Google Drive Import app details](https://developers.vtex.com/docs/apps/vtex.google-drive-import@0.x).
   - Classic Method: Import the catalog using multiple files (Product, SKU, Specification, Image).
3. Manual input: Load Catalog data manually on VTEX Admin, as described in our [Catalog 101 track](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/1ROhz3Y7mfSMmCO1I1GxEL).

In order to import your products, it is possible that you have to use more than one method, depending on how the data is structured and what types of software are used in your operation. Usually, a combination of [API integration](https://developers.vtex.com/docs/guides/catalog-api-overview) and [Google Drive Import app](https://developers.vtex.com/docs/apps/vtex.google-drive-import@0.x) works best. Below you can see some of the use cases and choose the processes that best fit your needs.

>⚠️ It is worth noting that product information in ERPs is often not suitable to be used and displayed in an ecommerce. Because of that it needs to go through an enrichment process, which may include restructuring categories and creating more descriptive and appealing description texts, for example.

### Scenarios and examples

See below some product import flow examples given backend scenarios that differ in information availability. 

#### Backend provides basic information

Information availability:
- Name (possibly not ecommerce friendly)
- Reference code
- Brand
- No category

Product import steps:
1. Backend sends new product/sku to VTEX associated with a [mock category](https://developers.vtex.com/docs/guides/erp-integration-set-up-catalog#category-migration-from-erps) called **Integration**. 

   > If brands are not available, you may do the same, creating a mock brand called **Integration**, for products to be enriched later.

2. Store team uses the [Google Sheets method](https://github.com/vtex-apps/google-import) or Admin to manually enrich the imported catalog information, assigning the correct categories to each product in the **Integration** category.

   >❗ Make sure the **Integration** category is inactive, so that the incomplete products are not displayed in the store.

#### Backend provides categories

Information availability:
- Name (possibly not ecommerce friendly)
- Reference code
- Brand
- Category
- SKU dimensions
- Image
- Price
- Inventory

Product import steps:
1. Backend [sends new product](https://developers.vtex.com/docs/guides/products) or [SKU](https://developers.vtex.com/docs/guides/skus) to VTEX.
2. Backend [sends product image](https://developers.vtex.com/docs/guides/images).
3. Backend [sends price](https://developers.vtex.com/docs/guides/erp-integration-import-prices).
4. Backend [sends inventory](https://developers.vtex.com/docs/guides/erp-integration-import-inventory).

#### Backend provides enriched information

Information availability:
- Name (possibly not ecommerce friendly)
- Reference code
- Brand
- Category
- SKU dimensions
- Product and SKU specifications
- Image
- Price
- Inventory

Product import steps:
1. ERP [sends new product](https://developers.vtex.com/docs/guides/products) or [SKU](https://developers.vtex.com/docs/guides/skus) to VTEX.
2. ERP [sends product images](https://developers.vtex.com/docs/guides/images).
3. ERP or PIM sends the product or SKU [specifications](https://developers.vtex.com/docs/guides/specifications).
4. ERP [sends price](https://developers.vtex.com/docs/guides/erp-integration-import-prices).
4. ERP [sends inventory](https://developers.vtex.com/docs/guides/erp-integration-import-inventory).

These are just a couple of convenient examples, it may be the case that you run all your catalog integration and updates with the Google sheet import method. In order to set up the best method for your store, see some more details below.


#### Google Sheets import

Some characteristics that may indicate that Google Sheets import is your best option:
- Your operation does not have a large and/or experienced technical team.
- Your selection of products and SKUs do not change often.


#### API product import

To add a product to a category in your catalog, you should use the [Create Product](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/product) endpoint in the Catalog API.

You can use the [Get Product by Id](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-) endpoint or visit the *Products > Catalog > Products and SKUs* section of your Admin panel to check on your progress.

>⚠️ After importing any product be sure to save the `id` returned by VTEX. You are going to need it whenever you want to make changes to that specific product. If you have internal product codes, such as REFIDs, make sure to save each `id` associated with the corresponding REFID in your data base.

> See more details on our [Product integration guide](https://developers.vtex.com/docs/guides/products).


## Import Product Specifications 

To fill in the product specifications for a product in your catalog, you should use the [Create Product Specification](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/product/-productId-/specification) endpoint in the Catalog API.

You can use the [Get Product Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/-productId-/specification) endpoint to check on your progress. Alternatively, you can find the Product Specifications for the Product you're interested in by following the steps below:

1. Open the *Products > Catalog > Products and SKUs* section of your Admin panel;
2. Find the Product you are working on by using search/filters or scrolling down the list;
3. In the *Edit* column, click on the *Update* button corresponding to that product;
4. Click on the *Specifications* tab to open the corresponding panel;
5. You should now be able to see the Product Specifications you filled in for that Product.

> See more details on our [Product specification integration guide](https://developers.vtex.com/docs/guides/product-specifications).

## Add Product to Trade Policy

All products need to be linked to the main trade policy in order to be displayed in your VTEX store. You may also link products to other trade policies you create to expose them in other sales channels, such as external marketplaces.

To add a Product to a Trade Policy, you should use the [Associate Product with Trade Policy](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/product/-productId-/salespolicy/-tradepolicyId-) endpoint in the Catalog API. To undo that action, use the [Remove Product from Trade Policy](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/product/-productId-/salespolicy/-tradepolicyId-) endpoint. 

You can use the **Get Trade Policies Linked to Product** endpoint to check on your progress. Alternatively, you can enable/disable trade policies for the Product you're interested in by following the steps below:

1. Open the *Products > Catalog > Products and SKUs* section of your Admin panel;
2. Find the Product you are working on by using search/filters or scrolling down the list;
3. In the *Edit* column, click on the *Update* button corresponding to that product;
4. You should now be able to see the Trade Policies you linked to that Product.

> The ID of the main trade policy is always 1, but you can use the [Get Sales Channel List](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/saleschannel/list) endpoint in the Catalog API to get more information on the trade policies that are available in your store. To enable a new trade policy, follow the instructions provided in our [Help Center article](https://help.vtex.com/faq/how-to-configure-a-new-trade-policy--frequentlyAskedQuestions_700?locale=en).

## Import SKU 

To add an SKU to a Product in your catalog, you should use the [Create SKU](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/stockkeepingunit) endpoint in the Catalog API.

You can use the [Get SKU list by Product Id](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitByProductId/-productId-) endpoint or visit the *Products > Catalog > Products and SKUs* section of your Admin panel to check on your progress.

> See more details on our [SKU integration guide](https://developers.vtex.com/docs/guides/skus).

## Import SKU Specifications 

To fill in the SKU specifications for an SKU in your catalog, you should use the [Create SKU Specification](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/stockkeepingunit/-skuId-/specification) endpoint in the Catalog API.

You can use the [Get SKU Specifications](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/specification) endpoint to check on your progress. Alternatively, you can find the SKU Specifications for the SKU you're interested in by following the steps below:

1. Open the *Products > Catalog > Products and SKUs* section of your Admin panel;
2. Find the Product that includes the SKU you are working on in the Product list;
3. In the *Edit* column, click on the dropdown button and select *Sku*;
4. Find the SKU you are working on in the SKU list;
5. In the *Edit* column, click on the *Change* button;
6. Click on the *Specifications* tab to open the corresponding panel;
7. You should now be able to see the SKU Specifications you filled in for that SKU.

> See more details on our [SKU specifications integration guide](https://developers.vtex.com/docs/guides/sku-specifications).

## Import SKU Image 

An image is needed in order to activate an SKU. To add an image to an SKU, you should use the [Create SKU File](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/stockkeepingunit/-skuId-/file) endpoint in the Catalog API.

You can use the [Get SKU File](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/file) endpoint to check on your progress. Alternatively, you can find the SKU Images for the SKU you're interested in by following the steps below:

1. Open the *Products > Catalog > Products and SKUs* section of your Admin panel;
2. Find the Product that includes the SKU you are working on in the Product list;
3. In the *Edit* column, click on the dropdown button and select *Sku*;
4. Find the SKU you are working on in the SKU list;
5. In the *Edit* column, click on the *Change* button;
6. Click on the *Images* tab to open the corresponding panel;
7. You should now be able to see the SKU Images you added to that SKU.

>ℹ️ See more details on our [Catalog images integration guide](https://developers.vtex.com/docs/guides/products).

## Wrapping up

If you have done things correctly, you should have imported all your products and their information to your catalog. This includes the Products, Product Specifications, SKUs, SKU Specifications and Images.

>⚠️ When registering products through ERP in a store's catalog, you may notice that the integration might not work at first. Instead, the API might return a `Timeout` error. Sometimes the answer lies in a simple system issue, regardless of whether or not the integration was correctly configured. In other cases, the error occurs because of a coding problem.
> No matter the scenario, `Timeout` is a way for the system to inform the user that command took more time than expected to complete the required task. Even though it is considered an \"error\", getting a `Timeout` is foreseen within the integration flow. Because of this, the code should envision retries. If this happens, repeat the product registration process normally. If, even by doing so, the problem still persists, seek the assistance of our support team to evaluate the situation.