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

<table>
  <tr>
   <td><strong>Field</strong>
   </td>
   <td><strong>Description</strong>
   </td>
   <td><strong>Required</strong>
   </td>
   <td><strong>Type</strong>
   </td>
   <td><strong>Default</strong>
   </td>
  </tr>
  <tr>
   <td>Id
   </td>
   <td>ID of `SkuImage` (`SkuFileId`). This is the ID that is used to delete/update it.
   </td>
   <td>No
   </td>
   <td>Integer
   </td>
   <td>AutoIncrement
   </td>
  </tr>
  <tr>
   <td>ArchiveId
   </td>
   <td>Unique identifier of the Image file.
   </td>
   <td>No
   </td>
   <td>Integer
   </td>
   <td>-
   </td>
  </tr>
  <tr>
   <td>SkuId
   </td>
   <td>ID of SKU
   </td>
   <td>Yes
   </td>
   <td>Integer
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>Name
   </td>
   <td>Name of SKU’s file
   </td>
   <td>No*
   </td>
   <td>String
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>IsMain
   </td>
   <td>Set the image as the main image for the product.
   </td>
   <td>No
   </td>
   <td>Boolean (true/false)
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>Label
   </td>
   <td>Image label
   </td>
   <td>No
   </td>
   <td>String
   </td>
   <td>false
   </td>
  </tr>
  <tr>
   <td>Url
   </td>
   <td>External image URL
   </td>
   <td>Yes
   </td>
   <td>String
   </td>
   <td>-
   </td>
  </tr>
</table>


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

[block:callout]
{
  "type": "warning",
  "body": "In order to update a SKU file the image needs to be uploaded again."
}
[/block]

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