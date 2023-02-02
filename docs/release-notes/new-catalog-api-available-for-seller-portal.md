---
title: "New Catalog API available for Seller Portal"
slug: "new-catalog-api-available-for-seller-portal"
type: "added"
createdAt: "2022-10-20T14:45:00.000Z"
hidden: false
excerpt: "We have released the [Catalog API - Seller Portal](https://developers.vtex.com/docs/api-reference/catalog-api-seller-portal#overview) to enable sellers using Seller Portal to massively create, fetch and edit information concerning products, SKUs, brands and categories."
---

![Commerce APIs](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/new-catalog-api-available-for-seller-portal-0.png)

> ℹ️ The new Catalog API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX's discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us).

The [Seller Portal](https://help.vtex.com/en/tutorial/how-to-set-up-your-store-on-seller-portal--6w1vBdRH2uuBGmUqgNQjwK) is an edition of the VTEX platform for sellers to connect and sell their products on marketplaces, providing sellers with the essential capabilities for an ecommerce operation.

Previously, sellers were limited to integrating their catalog manually through the Seller Portal interface.

Now, we have released the [Catalog API - Seller Portal](https://developers.vtex.com/docs/api-reference/catalog-api-seller-portal#overview) to enable sellers using Seller Portal to massively create, fetch and edit information concerning products, SKUs, brands and categories.

The following endpoints are now available:

### Product

- get [Get Product by ID](https://developers.vtex.com/vtex-rest-api/reference/getproduct)
- put [Update Product](https://developers.vtex.com/vtex-rest-api/reference/putproduct)
- get [Get Product Description by Product ID](https://developers.vtex.com/vtex-rest-api/reference/getproductdescription)
- get [Get Product by external ID, SKU ID, SKU external ID or slug](https://developers.vtex.com/vtex-rest-api/reference/getproductquery)
- post [Create Product](https://developers.vtex.com/vtex-rest-api/reference/postproduct)

### SKU

- get [Search for SKU](https://developers.vtex.com/vtex-rest-api/reference/searchsku)
- get [Get List of SKUs](https://developers.vtex.com/vtex-rest-api/reference/listsku)

### Brand

- get [Get List of Brands](https://developers.vtex.com/vtex-rest-api/reference/listbrand)
- post [Create a Brand](https://developers.vtex.com/vtex-rest-api/reference/postbrand)
- get [Get Brand by ID](https://developers.vtex.com/vtex-rest-api/reference/getbrand)
- put [Update Brand](https://developers.vtex.com/vtex-rest-api/reference/putbrand)

### Category

- get [Get Category Tree](https://developers.vtex.com/vtex-rest-api/reference/getcategorytree)
- put [Update Category Tree](https://developers.vtex.com/vtex-rest-api/reference/updatecategorytree)
- get [Get Category by ID](https://developers.vtex.com/vtex-rest-api/reference/getbyid-1)
- post [Create a Category](https://developers.vtex.com/vtex-rest-api/reference/createcategory)
