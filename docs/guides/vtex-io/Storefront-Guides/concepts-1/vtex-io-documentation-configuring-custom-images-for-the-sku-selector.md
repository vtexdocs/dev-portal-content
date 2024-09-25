---
title: "Configuring custom images for the SKU Selector"
slug: "vtex-io-documentation-configuring-custom-images-for-the-sku-selector"
hidden: false
createdAt: "2020-06-03T16:02:44.330Z"
updatedAt: "2022-12-13T20:17:44.730Z"
---

By default, the [SKU selector](https://developers.vtex.com/docs/guides/vtex-store-components-skuselector) component uses **thumbnail images of SKU** when rendered.

![sku-selector-images](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-configuring-custom-images-for-the-sku-selector-0.png)

These images that the component uses are taken from the SKU's previously given information in admin's Catalog.

However, you can configure the SKU selector to display a **custom image**, meaning an image different than the default one used by the SKU. For example:

![sku-selector-image-custom](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-configuring-custom-images-for-the-sku-selector-1.png)

Follow the step-by-step below to see how to apply this configuration in your store.

## Instructions

1. Access the Admin and go to **Catalog > All Products**.
2. Find the desired product, and click the down arrow button. Then, click  **SKU**.
3. Find the desired SKU and click the corresponding **Edit** button.
4. Click the **Images** tab.
5. Click the **Insert** button to add a new SKU image.

![configuring-sku-selector-images](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-configuring-custom-images-for-the-sku-selector-2.png)

6. Upload the file in the `File` field and set an ID for the recently uploaded file in the `Label` field. Click on **Save** after performing all your changes.
7. In your theme's code `sku-selector` block, add the `thumbnailImage` prop, whose past value should be the same as the label added in the catalog. For example:

```json
"sku-selector":{
  "props": {
    "thumbnailImage": ["LabelName"]
  }
},
```

After completing step 7, you will be able to check a brand new image for your SKU selector.

The problem is that **this image is link to the SKU** through the catalog information, and therefore will also be rendered in its original format when users select the SKU in question.

The way out of this scenario is to **hide the custom image** that's linked to the SKU in the `product-images` block.

8. In the `product-images` block you can use the `hiddenImages` prop to activate a sort of image blacklist. This prop's value should be the custom image's label, the same one used in the previous step. For example:

```json
"product-images": {
  "props": {
    "displayThumbnailsArrows": true,
    "hiddenImages": ["LabelName"]
  }
},
```

> ⚠️ Remember to replace the value inserted in the brackets with real values, according to your SKU label.

Consequently, you'll be able to configure a customized image exclusively for your SKU selector component, without it affecting your store's layout or that of the SKU images displayed to users.

> ⚠️ *For this configuration to properly work, **all SKU custom images must have the same label value** (which must be the only value given between brackets). Otherwise, even by following the steps above, the SKU selector will continue to render the default images.*

### Specifying SKU color variations

Once you have configured the [custom images](###step-by-step), you should set a specific name to display the SKU color variations.

![color-variation](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-configuring-custom-images-for-the-sku-selector-3.png)

Follow the next step-by-step on how to configure the SKU color variations.

1. Access the Admin.
2. Go to **Catalog** > **Categories**.
3. Choose the desired category and in `ACTIONS` click on **Field(SKU)**
4. In **Field** click in the group's `Edit`.
5. In the fields **Name** and **Text** complete with a color variation name which you can check the values in the [SKU Selector component](https://github.com/vtex-apps/store-components/blob/e130859a02e5c5d5e9deb9494bde9cfb6a0babc2/react/components/SKUSelector/utils/index.ts#L50-L72). For example:

![color-name](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-configuring-custom-images-for-the-sku-selector-4.png)

6. Click on `Save` to make your changes available on SKU with thumbnail images.
