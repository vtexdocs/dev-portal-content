---
title: "Shelf template controls"
slug: "shelf-template-controls"
excerpt: "Get to know Legacy CMS controls for creating product shelves."
hidden: false
createdAt: "2022-09-08T14:28:04.492Z"
updatedAt: "2022-09-08T14:28:04.492Z"
---

The Legacy CMS Portal provides a range of controls for creating product shelves. Below, you'll find the most commonly used variables and properties for defining product shelves, including examples for reference.

## Declaring product variables

Product attributes can be stored in variables, and these are used in every template. To declare the variables and receive an attribute of a product, use the following command: 

```
#set ($variable=$attribute)
```

### Examples

- `#set($id = $product.Id)`  
- `#set($uri = $product.Uri)`  
- `#set($escapedName = $product.HtmlEscapedName)`  
- `#set($evaluationRate = $product.EvaluationRate)`  

## Product and SKU

| Property                | Description                                      |
|-------------------------|--------------------------------------------------|
| `$product.Id`           | Shows the product ID.                            |
| `$product.EscapedName`  | Shows the product name.                          |
| `$product.DescriptionShort` | Shows a brief product description.   |
| `$product.Uri`          | Shows the product link.                          |
|`$product.GetImageTag(number corresponding to the image)`| Shows the image and the type of image you want. It follows this list of image types: <ul><li>ProductImageShowcaseLittle (Size: 65×65) = 1;</li><li>ProductImageShowcaseMedium (Size: 90×90) = 29;</li><li>ProductImageShowcaseLarge (Size: 130×130) = 30;</li><li>MainProductImage (Size: 250×250) = 2;</li><li>ThumbProductImage (Size: 45×45) = 3;</li><li>ZoomProductImage (Size: 344×344) = 10;</li><li>File = 11;</li><li>ProductManual = 12;</li></ul><br/> The sizes of the images are according to the store's layout.|
|`$product.ProductField(IdField)`| Shows the value of a product field by passing the ID of this field as a parameter.|

## Price

| Property                          | Description                                                                                             |
|-----------------------------------|---------------------------------------------------------------------------------------------------------|
| `$product.ListPrice`              | Shows the "From" price of the product.                                                                  |
| `$product.BestPrice`              | Shows the best price of the product.                                                                    |
| `$product.HasBestPrice`           | Indicates whether there is a better price for the product (used in conditionals).                        |
| `$product.NumbersOfInstallment`   | Shows the number of installments of the best payment condition for the product.                          |
| `$product.InstallmentValue`       | Shows the value of the installment of the best payment condition for the product, i.e., the value of the largest interest-free installment. |
| `$product.MaxNumbersOfInstallment`| Shows the largest installment with or without interest for this product.                                |
| `$product.MaxInstallmentValue`    | Shows the value of the installment of the product's highest payment condition, i.e., the value of the largest installment with or without interest. |
| `$product.BestPricePlusTax`       | Shows the price PLUS the rates applied to it. Rate values that are set by region, i.e., by using zip codes, will not be displayed on the shelves. If more than one rate includes the same product, the values are summed and displayed by the control. |
| `$product.ListPriceMinusBestPrice`              | Shows the absolute difference between the "From" price and the best price of the product.                |
| `$product.ListPriceMinusBestPriceInPercent`    | Shows the difference (in percentage) of the price "From" to the best price.        |

## Departament and Category

| Property                | Description                                      |
|-----------------------|-----------------------------------------------|
| `$product.DepartmentName`         | Displays the name of the product's department.|
| `$product.DepartmentLink`         | Displays the link of the product's department.|
| `$product.CategoryName`           | Displays the name of the product's category.|
| `$product.CategoryLink`           | Displays the link of the product's category.|

## Brand

| Property              | Description                                   |
|-----------------------|-----------------------------------------------|
| `$product.BrandName`  | Shows the name of the product's brand.        |
| `$product.Brand`      | Shows the product's brand in a link-friendly format. |
| `$product.BrandLink`  | Shows the link to the brand.                   |

## Buy button

| Property                         | Description                                                                                                                                           |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$product.BottomBuyAllSku`       | Includes a buy button to add to the shelf list, where the product with specifications added by the customer is sent directly to the cart. If the product has already been purchased for the list, a specific class is added to the item for customization. The control must be added to the shelf template used in the “Lista-Prateleira” page template. |
| `$product.BottomBuy`             | Includes a buy button in the shop window that takes the customer directly to the cart if there is only 1 SKU.                                         |
| `$product.ButtonBuyModal(false,true)` | Includes a buy button that inserts the product into the cart and keeps the customer in the shop window. This control needs the `$product.AmountInCart` control to add a desired quantity textbox for adding to the cart. |
| `$product.AmountInCart`          | Inserts a textbox element to set the desired quantity of the product to be added to the cart. This control is used in conjunction with the control `$product.ButtonBuyModal(false,true)`. |

## Others

| Property                   | Description                                                                                                                      |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| `$product.EvaluationRate`  | Shows the product rating.                                                                                                       |
| `$product.HightLight`      | Shows the collections of highlights of which the product is part.                                                               |
| `$product.DiscountHightLight` | Shows the promotions with highlights of which the product is part. If the promotion has any condition of freight, payment method, or cluster, it will not be presented until these conditions are met. |
| `$product.IsInStock`       | Indicates whether the product has items in stock (used in conditionals).                                                        |
| `$product.Tax`             | Shows the rates registered for the product.                                                                                     |
| `$product.QuickView`       | Shows the Quick View button.                                                                                                    |
| `$product.Compare`         | Shows the checkbox to select the products to be compared.                                                                |
| `$product.BestRewardValue` | Displays the value for the "Fidelity Value" field of the SKU form.                                                               |
| `$product.PercentBougthAndBought` | Shows the percentage value on shelves of type "Who bought also bought."                                                        |
| `$product.PercentBoughtAlso` | Shows the percentage value on shelves of type "Who saw also bought."                                                             |
| `$product.PercentViewedAlso` | Shows the percentage value on shelves of type "Who saw also saw."                                                                |
| `$product.InsertSku`       | Shows the individual number of products in the shop window and a checkbox for each product SKU, allowing you to select which SKUs will be added to the list. To add more than one SKU, it is necessary to change the quantity inside the box and then select the checkbox for the SKU. If the quantity is changed and the checkbox of an SKU is selected, the quantity of this SKU will not change; only the next SKUs will be selected after changing the quantity in the box. |

