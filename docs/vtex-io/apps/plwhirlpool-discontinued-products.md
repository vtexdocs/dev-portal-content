---
title: "Discontinued Products PL"
slug: "plwhirlpool-discontinued-products"
excerpt: "plwhirlpool.discontinued-products@0.2.2"
hidden: true
createdAt: "2022-07-11T10:14:06.314Z"
updatedAt: "2022-07-11T10:14:06.314Z"
---
## FE and BE discontinued products app
* [BE app](#be-app)
* [FE app](#fe-app)

## BE app
### Full Catalog Update
`/_v/api/product/redirect`
Set up redirects for all unsellable or discontinued products and delete redirects previously set up for now buyable products

### Manage Redirect
`/_v/api/product/redirect/full`
Set up or delete redirects over specific products passed in the body of the call

## FE app
defines two interfaces, the first one for discontinued products and the other one for unsellable products

`DiscontinuedProducts`

`UnsellableProducts`