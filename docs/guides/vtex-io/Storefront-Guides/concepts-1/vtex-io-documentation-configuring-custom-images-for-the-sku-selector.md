---
title: "Configuring custom images for the SKU Selector"
slug: "vtex-io-documentation-configuring-custom-images-for-the-sku-selector"
hidden: false
createdAt: "2020-06-03T16:02:44.330Z"
updatedAt: "2025-12-04T17:55:04.654Z"
---

In this guide, you'll learn how to configure custom images for the [SKU selector](https://developers.vtex.com/docs/guides/vtex-store-components-skuselector) component. By following these steps, you can display a specific image for each SKU in the selector, different from the default thumbnail.

By default, the SKU selector component uses thumbnail images of the SKU when rendered, as show below. The component uses images from the SKU's information in the Admin Catalog:

![sku-selector-images](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-configuring-custom-images-for-the-sku-selector-0.png)

However, you can configure the SKU selector to display a custom image, meaning an image different than the default one used by the SKU. For example:

![sku-selector-image-custom](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-configuring-custom-images-for-the-sku-selector-1.png)

## Instructions

### Step 1 - Adding an image to an SKU

To display a custom imagem in the SKU Selector, first you need to upload the image and associate it with the desired SKU:

1. In the VTEX Admin, go to **Catalog > Products & SKUs**.
2. Find the desired product and click the down arrow to see its SKUs.
3. Click the desired SKU to edit it.
4. In the **Media > Images** section, click `Add` and choose one of the options to upload an image:
   - **Choose files:** Upload images stored on your computer.
   - **Add links:** Upload images using a URL.
5. Hover over the uploaded image, click the menu icon (`⋮`), and then click `Edit Metadata`.
6. In the **Label** field, enter a unique ID for the image. This label will be used to identify the custom image.
7. Click on **Save** to save your changes.

![images-sku](https://vtexhelp.vtexassets.com/assets/docs/src/images-sku___4d9cf27b7ceecb129993e38302b1d66c.gif)

### Step 2 - Configure the `sku-selector` block

Now, you must configure your theme to use the custom imagem in the SKU Selector component:

1. In your theme's code, find the `sku-selector` block.
2. Add the `thumbnailImage` prop, setting its value to the label you created in the previous step. For example:

 ```json
 "sku-selector":{
   "props": {
     "thumbnailImage": ["LabelId"]
   }
 },
 ```
 > ⚠️ Replace `LabelId` with the exact label you set for your custom image.

After completing this step, your SKU Selector will display the new custom image.

### Step 3 - Hide the custom image from the main product gallery

By default, the custom image you added will also appear in the main product image gallery. To prevent this behavior, you can hide it by following these steps:

1. In your store theme's code, find the `product-images` block.
2. Add the `hiddenImages` prop, setting its value to the same label used for your custom image. For example:

 ```json
 "product-images": {
   "props": {
     "displayThumbnailsArrows": true,
     "hiddenImages": ["LabelId"]
   }
 },
 ```

> ⚠️ Replace `LabelId` with the exact label you set for your custom image. All SKUs using a custom image must use the same label value for both `thumbnailImage` and `hiddenImages` props.

After completing this step, you'll have a custom image exclusively for your SKU selector, which will not appear in the main product gallery.

### Step 4 - (Optional) Specify SKU color variations

To display color variations for SKUs with specific names, you can create an SKU field.

![color-variation](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-configuring-custom-images-for-the-sku-selector-3.png)

Follow these steps to configure SKU color variations:

1. In the VTEX Admin, go to **Catalog > Categories**.
2. Click the desired category, then click `ACTIONS` <i class="fas fa-angle-down"></i>.
3. From the dropdown menu, select `Field (SKU)`.

 ![categories-field-sku](https://vtexhelp.vtexassets.com/assets/docs/src/categories-field-sku___69f678555a769e29e77e252e0945510d.png)

4. Click `New field` and configure each field accordingly. For more details on this, see the instructions on [Creating an SKU field](https://help.vtex.com/docs/tutorials/adding-sku-specifications-or-fields#creating-an-sku-field).
5. Click `Save` to create the new field.

   ![color-name](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-configuring-custom-images-for-the-sku-selector-4.png)

>⚠️ Once created, SKU fields can't be deleted, and required fields must be filled for all SKUs in that category, or they may become inactive. 

8. In the row of the field you just created, click the down arrow <i class="fas fa-angle-down"></i> next to the `Edit` button and select `Values`.
9. Create a `New value` or `Edit` a previously defined value.
10. In the **Name** field, enter each color value on a new line (for example, Off-white, Blue, Black).
11. Click `Save` to save your changes.

>ℹ️ Learn more about this process in the guide [Adding SKU specifications or fields](https://help.vtex.com/docs/tutorials/adding-sku-specifications-or-fields#creating-an-sku-field).

Your changes will now be available for SKUs with thumbnail images.
