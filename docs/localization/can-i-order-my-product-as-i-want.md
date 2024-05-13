---
title: Can I order my product as I wish?
slug: can-i-order-my-product-as-i-wish
hidden: false
createdAt: 2022-09-08T14:19:54.761Z
updatedAt: 2022-09-08T14:19:54.761Z
---

By default, VTEX system orders products according to their relevance on the site, i.e. by most sold and most viewed.

However, there are ways to change this order: either through the Score field or by using Querystring.
How the Score field works is explained in [this article](https://help.vtex.com/en/tutorial/how-the-score-field-works--1BUZC0mBYEEIUgeQYAKcae).

The Querystring process is simpler: simply insert the parameter into the URL to change the order in which products are displayed.

The parameters are as follows:

- **Lowest price**: `?O=OrderByPriceASC`
- **Highest price**: `?O=OrderByPriceDESC`
- **Best sellers**: `?O=OrderByTopSaleDESC`
- **Best rated**: `?O=OrderByReviewRateDESC`
- **Alphabetical order A-Z**: `?O=OrderByNameASC`
- **Alphabetical order Z-A**: `?O=OrderByNameDESC`
- **Release date (associated with the product)**: `?O=OrderByReleaseDateDESC`
- **Highest discount**: `?O=OrderByBestDiscountDESC`
- **Lowest discount**: `?O=OrderByBestDiscountASC`
  For example: `http://www.{AccountName}.com/{departament}/{category}?O=OrderByPriceASC`

> ⚠️ You can only use one product order parameter at a time. Therefore, you have to choose the one that best suits your store's needs (remember that parameters can be changed at will).
