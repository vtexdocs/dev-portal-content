---
title: "Managing product images in specific contexts"
createdAt: "2024-10-14T00:00:15.623Z"
updatedAt: ""
---

In this guide, learn how to control which product images appear in different sections of your store by labeling them with specific contexts in the VTEX Catalog. These contexts determine where the image is displayed and are defined as follows:

- **Gallery context:** Restricts the image to appear only in the Product Image Gallery, allowing you to curate a set of images highlighting key features.
- **SKU selector context:** Restricts the image to appear only in the SKU selector, providing a zoomed-in view for detailed examination.
- **Generic context (default):** Sets the image to appear in all sections.

For example, you may want to limit the number of images shown in the Product Details Page (PDP) gallery to highlight key features of the product.

| **Before** | **After** |
| ---------- | --------- |
| ![before-context](https://vtexhelp.vtexassets.com/assets/docs/src/before___bec5e5c536162b228cd4d50d0042c4a6.png) | ![after-context](https://vtexhelp.vtexassets.com/assets/docs/src/after___f6bb9be611ba511d7eee8558c34a2732.png) |
| The product image gallery displays all five images uploaded to the [Catalog](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ). | After limiting the number of images, only three product images are displayed to focus on the most important product features. |

By associating images with specific contexts, you can ensure they are displayed in relevant sections and only the most important images.

## Before you begin

To follow the instructions in this guide, you must understand the concepts of [API extensions](https://developers.vtex.com/docs/guides/faststore/api-extensions-overview) and [Section override](https://developers.vtex.com/docs/guides/faststore/overrides-overview).

## Instructions

For this tutorial, we will create a custom gallery for the PDP using the [label](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/17PxekVPmVYI4c3OCQ0ddJ#adding-an-image-to-the-sku) feature from the [VTEX Catalog](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ).

In this example, we will create a context by labeling selected images with the term `gallery`. This gallery will only display images that have been assigned the `gallery` label in the [catalog](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ).

### Step 1: Labeling images in the Catalog

Label your product images within the catalog with the label field.
The label field determines where product images should be displayed in your store.
To label your images, follow these steps:

1. Access the VTEX Admin.
2. Go to **Catalog > All Products** and navigate to the product you want to edit.
3. Click the `UPDATE` button and then click `SKU`.

    ![sku-images](https://vtexhelp.vtexassets.com/assets/docs/src/sku-images-admin___1baaa1f88be16795b892634b80676ccc.gif)

4. Go to the SKU you want to update and click `Edit`.
5. Click the `Images` tab.
6. For each SKU image you want to include in the gallery, set the **Label** field to **gallery**. These are the available labels:

    | Label name | Description |
    | ---------------- | ---------------- |
    | `gallery` | Restricts the image to appear only in the Product Image Gallery. |
    | `generic` | Includes the image in all contexts by default. Images labeled as `generic` are always displayed as part of the complete set of images. |
    | `skuvariation` | Designates the image for the SKU Selector. If no image has this label, the first image of the SKU is used. |

7. Click `Save Label` and `Save`.

### Step 2: Querying images by context

Update your store `ServerProduct` and `ClientProduct` fragments to fetch images based on their [assigned labels](#step-1-labeling-images-in-the-catalog). This ensures that only relevant images for specific contexts, like the PDP, are retrieved.

> ℹ️ For more information about fragments in the FastStore context, see the [Extending queries using fragments](https://developers.vtex.com/docs/guides/faststore/api-extensions-extending-queries-using-fragments) guide.

1. Open your store code in a code editor of your preference.
2. Go to `src/fragments/ServerProduct.ts` and add the following:

    //REMINDER: Add CodeHike

    ```js src/fragments/ServerProduct.ts
    import { gql } from '@faststore/core/api'
    
    export const fragment = gql`
    fragment ServerProduct on Query {
        product(locator: $locator) {
        galleryImages: image(context: "gallery", limit: 3) {
            url
            alternateName
        }
        }
    }
    `
    ```

3. Go to `src/fragments/ClientProduct` and add the following:

    //REMINDER: Add CodeHike

    ```js src/fragments/ClientProduct
    import { gql } from '@faststore/core/api'
    
    export const fragment = gql`
    fragment ClientProduct on Query {
        product(locator: $locator) {
        galleryImages: image(context: "gallery", limit: 3) {
            url
            alternateName
        }
        }
    }
    `
    ```

> ❕The `limit: 3` argument selects only three images. Omitting this argument returns all images labeled `gallery`. By default, all images are returned if no context label is found.

### Step 3: Overriding the `ImageGallery` component

Customize the default [ImageGallery](https://developers.vtex.com/docs/guides/faststore/organisms-image-gallery) component to showcase the images retrieved in the [previous step](#step-1-labeling-images-in-the-catalog). This override allows you to control how images are presented and interacted with on your PDP.

1. In your store code, create the `ProductDetails.tsx` file inside the `src/components/overrides` folder.
2. In the `ProductDetails.tsx` file, add the following content to it:

    //REMINDER: Add CodeHike

    ```tsx
    import { SectionOverride } from "@faststore/core";

    import { usePDP } from "@faststore/core";
    import { Image_unstable as Image } from "@faststore/core/experimental";

    import { ImageGallery, ImageGalleryViewer } from "@faststore/ui";
    import { useState } from "react";

    const SECTION = "ProductDetails" as const;

    const ImageComponent = ({ url, alternateName }: {url: string, alternateName?: string}) => {
    return <Image src={url} alt={alternateName} width={68} height={68}/>
    }

    const override: SectionOverride = {
    section: SECTION,
    components: {
        __experimentalImageGallery: {
        Component: () => {
                const { data } = usePDP();
            const [selectedIndex, setSelectedIndex] = useState<number>(0);
    
            const currentImage = data.product.galleryImages[selectedIndex];

            return (
            <ImageGallery
                images={data.product.galleryImages}
                ImageComponent={ImageComponent}
                selectedImageIdx={selectedIndex}
                setSelectedImageIdx={setSelectedIndex}
                data-fs-product-details-gallery="true"
            >
                <ImageGalleryViewer>
                <Image
                    sizes="(max-width: 360px) 50vw, (max-width: 768px) 90vw, 50vw"
                    width={691}
                    height={691 * (3 / 4)}
                    loading="eager"
                    src={currentImage.url}
                    alt={currentImage.alternateName}
                />
                </ImageGalleryViewer>
            </ImageGallery>
            );
        },
        },
    },
    };

    export { override };
    ```

   - The `ServerProduct` and `ClientProduct` fragments are accessed via the `usePDP` Hook.
   - Instead of using the images being passed to the [ImageGallery](https://developers.vtex.com/docs/guides/faststore/organisms-image-gallery) Component, we are using the `galleryImages` we defined.

3. Open a terminal and run `yarn dev` to sync the changes made in the previous instructions.
4. Open a pull request to your store with these changes. Once the pull request is reviewed and approved, merge it into the `main` branch.

### Considerations for SKU Selector Images

The FastStore API defines a specific name for images that are supposed to appear on the SKU Selector. The first image labeled `skuvariation` in the Catalog will automatically appear on the SKU Selector. If no image has the `skuvariation` label, the first image of the SKU will be displayed.

> ⚠ If an image needs to appear in the SKU Selector and Product Gallery, you must upload it twice and assign different labels.
