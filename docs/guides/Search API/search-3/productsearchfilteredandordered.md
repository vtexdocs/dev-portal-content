---
title: "Search for Products with Filter, Order and Pagination"
slug: "productsearchfilteredandordered"
excerpt: "Retrives general information about the store products. This information can be filtered and ordered by a number of options. It also can be pagineted, filtered and ordered."
hidden: false
createdAt: "2019-12-30T03:21:07.203Z"
updatedAt: "2021-08-31T18:21:45.777Z"
---
# Filters  

- **Filter by full text** - `ft={searchWord}`  
Ex: `ft=television`

- **Filter by category** - `fq=C:/{a}/{b}`  
{a} and {b} are categoryIds   
Ex: `fq=C:/1000041/1000049/`

- **Filter by brand** - `fq=B:/{a}/{b}`  
{a} and {b} are brandIds
Ex: `fq=B:/189385/189387/`

- **Filter by specification** - `fq=specificationFilter_{a}:{b}`  
{a} is the specificationId, {b} = specification value    
Ex: To filter products where the color is Blue, find the specificationId for color, supose it's 123 then it will be like this `fq=specificationFilter_123:Blue`

- **Filter by price range** - `fq=P:[{a} TO {b}]`  
{a} is the minimum price "from" and  {b} is the highest price "to"  
Ex: `fq=P:[0 TO 20]` will search products between 0.00 and 20.00.  

- **Filter by collection** - `fq=productClusterIds:{{productClusterId}}` 
where productClusterId also know as collectionId  
More information about collections: https://help.vtex.com/en/tutorial/creating-a-product-collection

- **Filter by product Id** - `fq=productId:{{productId}}`

- **Filter by sku Id** - `fq=skuId:{{skuId}}`

- **Filter by referenceId** - `fq=alternateIds_RefId:{{referenceId}}`

- **Filter by ean13** - `fq=alternateIds_Ean:{{ean13}}`

- **Filter by availability at a specific sales channel** - `fq=isAvailablePerSalesChannel_{{sc}}:{{bool}}`  
{{sc}} is the desired sales channel  
{{bool}} is true ou false, 1 or 0.  
Ex: seaching available products for the sales channel 4 `fq=isAvailablePerSalesChannel_4:1`

- **Filter by available at a specific seller** - `fq=sellerId:{{sellerId}}`

# Pagination

- **Initial item number** - `_from={{first}}`
- **Final item number** - `_to={{last}}`
[block:callout]
{
  "type": "warning",
  "body": "This endpoint returns a maximum of 50 items per response, so the difference between `_from` and `_to` should not exceed this number. It is also important to highlight that the result order is descending, from the highest product ID to the lowest."
}
[/block]
# Sorting

- **Price**  
`O=OrderByPriceDESC`  
`O=OrderByPriceASC`

- **Top Selling Products**  
`O=OrderByTopSaleDESC`

- **Best Reviews**  
`O=OrderByReviewRateDESC`

- **Name**  
`O=OrderByNameASC`  
`O=OrderByNameDESC`

- **Release Date**  
`O=OrderByReleaseDateDESC`

- **Best Discounts**  
`O=OrderByBestDiscountDESC`

- **Score**  
`O=OrderByScoreDESC`