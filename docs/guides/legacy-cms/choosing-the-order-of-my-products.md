---
title: "Choosing the order of my products"
slug: "choosing-the-order-of-my-products"
hidden: true
createdAt: "2022-09-13T15:16:13.410Z"
updatedAt: "2022-09-13T15:16:13.410Z"
---
By default, the VTEX system orders products according to their importance on your site, i.e. by most sold and most viewed in the past thirty days.

However, you can change the order by using Querystring. Just enter a parameter in the URL to change the order of exhibition.

Parameters can also be used in URL mappings to redirect specific URLs to others, such as product listing pages. To learn more about this feature, go to [URL Mapping (301 Redirect)](https://help.vtex.com/en/tutorial/mapeamento-de-urls-redirectimento-301--frequentlyAskedQuestions_623).

These are the parameters:

- __Price (from lowest to highest)__: `?O=OrderByPriceASC`
- __Price (from highest to lowest)__: `?O=OrderByPriceDESC`
- __Best sellers__: `?O=OrderByTopSaleDESC`
- __Best rated__: `?O=OrderByReviewRateDESC`
- __Alphabetical order A-Z__: `?O=OrderByNameASC`
- __Alphabetical order Z-A__: `?O=OrderByNameDESC`
- __Release date (registered on the product)__: `?O=OrderByReleaseDateDESC`
- __Best discount__: `?O=OrderByBestDiscountDESC`
- __Score (from lowest to highest)__: `?O=OrderByScoreASC`
- __Score (from highest to lowest)__: `?O=OrderByScoreDESC`

For example: `http://www.{AccountName}.com/{departament}/{category}?O=OrderByPriceASC`

## Related articles
- [How does the Score field work?](https://help.vtex.com/en/tutorial/como-funciona-o-campo-score--1BUZC0mBYEEIUgeQYAKcae?&utm_source=autocomplete)
- [URL Mapping (301 Redirect)](https://help.vtex.com/en/tutorial/mapeamento-de-urls-redirecionamento-301--frequentlyAskedQuestions_623)