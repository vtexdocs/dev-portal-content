---
title: "Images"
slug: "images"
hidden: false
createdAt: "2021-12-14T14:21:31.352Z"
updatedAt: "2022-02-04T21:29:02.633Z"
---

Product images are associated with SKUs.

To learn more, see this article about [Best practices with catalog images](https://help.vtex.com/en/tutorial/best-practices-for-using-images-in-the-catalog--738K2yfq5U86kUI2k4AQIk). It may also be helpful to [compress the images](https://help.vtex.com/en/tutorial/how-the-automatic-compacting-of-images-works) you use in your store.

## Data Model

| **Field**    | **Description**    | **Required**    | **Type**   | **Default**    |
|---|---|---|---|---|
| Id    | ID of `SkuImage` (`SkuFileId`). This is the ID that is used to delete/update it.   | No    | Integer    | AutoIncrement    |
| ArchiveId    | Unique identifier of the Image file.    | No    | Integer    | -    |
| SkuId    | ID of SKU    | Yes    | Integer    | null    |
| Name    | Name of SKU’s file    | No*   | String    | null    |
| IsMain    | Set the image as the main image for the product.    | No    | Boolean (true/false)    | null    |
| Label    | Image label    | No    | String    | false    |
| Url    | External image URL   | Yes    | String    | -    |

## API implementation

### Register SKU image

To register an image to an SKU, it must be hosted on an external server and with read permission. Then you may use the [Create SKU file API endpoint](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-sku-file).

#### Example request

Body:

```json
{
    "IsMain": true,
    "Label": "Main",
    "Name": "Nike-Red-Janoski-1",
    "Url": "https://m.media-amazon.com/images/I/610G2-sJx5L._AC_UX695_.jpg"
}
```

Response:

```json
{
    "Id": 520,
    "SkuId": 70,
    "ArchiveId": 155467,
    "IsMain": true,
    "Label": "Main"
}
```

### Change SKU image

To change an existing SKU image that already existed, you can use the [Update SKU file endpoint](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-put-sku-file).

>⚠️ In order to update a SKU file the image needs to be uploaded again.

#### Example request

Body:

```json
{
    "IsMain": true,
    "Label": "Main2",
    "Name": "Nike-Red-Janoski-1",
    "Url": "https://m.media-amazon.com/images/I/610G2-sJx5L._AC_UX695_.jpg"
}
```

Response:

```json
{
    "Id": 520,
    "SkuId": 70,
    "ArchiveId": 155467,
    "IsMain": true,
    "Label": "Main2"
}
```

### Remove SKU Image

To remove an SKU image use the [Delete SKU image by file ID API request](https://developers.vtex.com/vtex-rest-api/reference/delete_api-catalog-pvt-stockkeepingunit-skuid-file-skufileid). You will need the `SkuFileId`.

### Remove all SKU images

To delete all images of one specific SKU, use the [Delete all SKU file API endpoint](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-delete-sku-file).
