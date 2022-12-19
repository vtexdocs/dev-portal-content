---
title: "Shelf template controls"
slug: "shelf-template-controls"
hidden: false
createdAt: "2022-09-08T14:28:04.492Z"
updatedAt: "2022-09-08T14:28:04.492Z"
---
VTEX system offers some controls for the creation of shelves.

Products attributes can be stored in variables, and these are used in every template. To declare the variables and receive an attribute of a product, use the following command: `#set ($variable=$attribute)`

### Examples

- `#set($id = $product.Id)`  
- `#set($uri = $product.Uri)`  
- `#set($escapedName = $product.HtmlEscapedName)`  
- `#set($evaluationRate = $product.EvaluationRate)`  

### Product and SKU

`$product.Id`

Shows the product ID.

`$product.EscapedName`

Shows the product name.

`$product.DescriptionShort`

Shows a brief description of the product.

`$product.Uri`

Shows the product link.

`$product.GetImageTag(number corresponding to the image)`

Shows the image and the type of image you want. It follows this list of image types:

- ProductImageShowcaseLittle (Size: 65×65) = 1;
- ProductImageShowcaseMedium (Size: 90×90) = 29;
- ProductImageShowcaseLarge (Size: 130×130)= 30;
- MainProductImage (Size: 250×250)= 2;
- ThumbProductImage (Size: 45×45)= 3;
- ZoomProductImage (Size: 344×344)= 10;
- File = 11;
- ProductManual = 12.

**Note:** _The sizes of the images are according to the layout of the store_

`$product.ProductField(IdField)`

Shows the value of a product field by passing the ID of this field as a parameter.

### Price

`$product.ListPrice`

Shows the "From" price of the product.

`$product.BestPrice`

Shows the best price of the product.

`$product.HasBestPrice`

Indicates whether there is a better price for the product (used in conditionals).

`$product.NumbersOfInstallment`

Shows the number of installments of the best payment condition for the product.

`$product.InstallmentValue`

Shows the value of the installment of the best payment condition for the product, that is, the value of the largest interest-free installment for this product.

`$product.MaxNumbersOfInstallment`

Shows the largest installment with or without interest for this product.

`$product.MaxInstallmentValue`

Shows the value of the installment of the product's highest payment condition, that is, the value of the largest installment with or without interest for that product.

`$product.BestPricePlusTax`

Shows the price PLUS the rates applied to it.

**Note**: _Rate values that are set by region, ie by using zip codes, will not be displayed on the shelves. If there is more than one rate that includes the same product, the values are summed and displayed by the control._

`$product.ListPriceMinusBestPrice`

Shows the absolute difference of the "From" price to the best price of the product.

`$product.ListPriceMinusBestPriceInPercent`

Shows the difference (in percentage) of the price "From" to the best price of the product.

### Departament and Category

`$product.DepartmentName`

Displays the name of the product's department.

`$product.DepartmentLink`

Displays the link of the product's department.

`$product.CategoryName`

Displays the name of the product's category.

`$product.CategoryLink`

Displays the link of the product's category.

### Brand

`$product.BrandName`

Shows the name of the product's brand. Ex.: "Oliveira Juices"

`$product.Brand`

Shows the product's brand in a format recommended for creating links. Ex.: "oliveira-juices"

`$product.BrandLink`

Shows the brand's link.

### Buy button

`$product.BottomBuyAllSku`

Includes a buy button to add to the list shelf, where the product with specification added by the customer is sent directly to the cart. If the product in question has already been purchased for the list, a specific class will be added to the item. This way, you can customize the layout also for this status.

_Note: Control must be added to the shelf template used in the “Lista-Prateleira” page template._

`$product.BottomBuy`

Includes a buy button in the shop window that takes the customer directly to the cart if there is only 1 SKU.

`$product.ButtonBuyModal(false,true)`

Includes a buy button that inserts the product into the cart and keeps the customer in the shop window.

_OBS: The above control needs the `$product.AmountInCart` control to add a desired quantity textbox to add to the cart._

`$product.AmountInCart`

Inserts a textbox element to set the desired quantity of the product to be added to the cart.

_OBS: This control is used in conjunction with the control `$product.ButtonBuyModal(false,true)`_

### Others

`$product.EvaluationRate`

Shows the product rating.

`$product.HightLight`

Shows the collections of highlights of which the product is part.

`$product.DiscountHightLight`

Shows the promotions with highlight of which the product is part.

_Note: If the promotion has any condition of freight, payment method or cluster, it will not be presented until these conditions are met._

`$product.IsInStock`

Indicates whether the product has items in stock (used in conditionals).

`$product.Tax`

Shows the rates registered for the product.

`$product.QuickView`

Shows the Quick View button.

`$product.Compare`

Shows the check box to select the products that will be compared.

`$product.BestRewardValue`

Displays the value for the "Fidelity Value" field of the SKU form.

`$product.PercentBougthAndBought`

Shows the percentage value on shelves of type "Who bought also bought".

`$product.PercentBoughtAlso`

Shows the percentage value on shelves of type "Who saw also bought".

`$product.PercentViewedAlso`

Shows the percentage value on shelves of type "Who saw also saw".

`$product.InsertSku`

Shows the individual amount of products in the shop window and a checkbox for each product SKU allowing you to select which SKUs will be added to the list. To add more than one SKU it is necessary to change the quantity inside the box and then select the checkbox for the SKU. If the quantity is changed and the checkbox of an SKU is selected, the quantity of this SKU will not change, only the next SKUs selected after changing the quantity in the box.