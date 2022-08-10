---
title: "Alternative API requests"
slug: "alternative-api-requests"
hidden: false
createdAt: "2021-12-14T14:24:06.624Z"
updatedAt: "2022-02-04T21:30:08.332Z"
---
As you may have noticed, many catalog API requests use VTEX IDs in order to create and update values. Fields like `BrandId`, `FieldId`, `FieldValueId`, `GroupId` and `CategoryId`.

While it is important to keep track of these IDs, there are some alternative endpoints that do not require them for performing some tasks.


## Create product using brand name and category path

[Create product API endpoint](https://developers.vtex.com/vtex-rest-api/reference/post-product)


### Example body:
```json
{
    "Name": "Test Product",
    "CategoryPath": "Storage/Hard Drive",
    "BrandName": "Sample Brand",
    "RefId": "310117069123",
    "Title": "Browser Title for this product",
    "LinkId": "test-product",
    "Description": "This is a cool product",
    "ReleaseDate": "2019-01-01T00:00:00",
    "IsVisible": true,
    "IsActive": true,
    "TaxCode": "",
    "MetaTagDescription": "tag test",
    "ShowWithoutStock": true,
    "Score": 1
}

```


## Create product specification using field, group names
API request: [Associate product specification using specification and group names](https://developers.vtex.com/vtex-rest-api/reference/put_api-catalog-pvt-product-productid-specificationvalue)


### Example body
```json
{
    "FieldName": "TesteAPI",
    "GroupName": "TestGroup",
    "RootLevelSpecification": true,
    "FieldValues": [
        "Value123"
        ]
}
```