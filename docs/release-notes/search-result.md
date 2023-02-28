---
title: Search Result 
excerpt: "The search results page can now inform the user about the number of items displayed on the browser page, along with the total number of results found."
createdAt: "2019-08-22T14:47:00.000Z"
---

The search results page can now inform the user about the number of items displayed on the browser page, along with the total number of results found, all thanks to the new `showProductsCount` prop.

## What has changed

Before this prop, it wasn’t possible to dynamically render data on item quantity for the user, with only the total number of results found for that search being shown.

Now, the `showProductsCount` prop allows the retailer to decide whether to display this data to the customer.

![](https://user-images.githubusercontent.com/52087100/63536853-d8c9b580-c4ea-11e9-9837-00e4f05d8406.png)

## Main advantages

To support dynamic content, the new prop simultaneously shows the user data on the total number of products being displayed in the browser page along with the number of search results found. This **improves the user’s search experience**, providing the user with valuable feedback on the number of items already seen and the number of items left.

## What you need to do

The new prop is available starting with the [**Search Result**](https://github.com/vtex-apps/search-result) app version **3.28.0**. Make sure your store is already running this version or higher.
