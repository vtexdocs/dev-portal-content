---
title: "Product Image"
slug: "oficinareserva-custom-product-image"
excerpt: "oficinareserva.custom-product-image@1.0.0"
hidden: true
createdAt: "2022-08-01T15:22:10.783Z"
updatedAt: "2022-08-01T15:22:10.783Z"
---
It was not possible to customize VTEX's native Product Image. Therefore it was
necessary to import VTEX components and modify them via code in order to make
the store look the way we wanted.

## Desktop

On desktop, the photos are first displayed side by side. Besides that, there are
sticky thumbnails that stay visible on screen even if the user scrolls the page.
When the user clicks an image, a high quality version of the image is displayed
inside a modal.


## Mobile

On mobile devices, we used the default carousel component, with additional props
being passed to the swiper component so that we can control the number of photos
shown per page. The idea is that we can show one photo and a peak of the next
one.