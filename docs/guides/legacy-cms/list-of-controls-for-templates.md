---
title: "List of controls for templates"
slug: "list-of-controls-for-templates"
hidden: false
createdAt: "2022-09-08T14:21:08.318Z"
updatedAt: "2022-09-08T14:21:08.318Z"
---
The controls listed in this article can be used by your store's *front-end* developer to create the store page layout in the **Storefront > Layout** module.

- [General controls](#general-controls)
- [Controls for product pages](#controls-for-product-pages)
- [RichSnippets Controls](#richsnippets-controls)
- [Controls for department, category, and search pages](#controls-for-department-category-and-search-pages)
- [Other controls](#other-controls)
- [Deprecated controls](#deprecated-controls)

## General controls

You can use the controls listed below on most pages in your store.

| Control | Description |
| ------- | ----------- |
| `<vtex.cmc:breadCrumb/>` | **Breadcrumb:** indicates the user's current location on your store's website and the pages they accessed to get to the current one. Works on product, department, category, and search pages. |
| `<vtex.cmc:fullTextSearchBox/>` | **Search control:** displays the search bar in your store. For more information, read [Search Control - fulltextSearchBox](https://developers.vtex.com/docs/guides/search-control-fulltextsearchbox). |
| `<vtex.cmc:welcomeMessage/>` | **Welcome message:** displays a welcome message to anyone accessing your store. To customize this message, go to the **Store Settings > Storefront** module and click on **Settings**. In the Store texts tab, look for the `topbarSaudacao` command in the ID options and select it. In the text box that will appear automatically, you can edit the welcome message and then `Save`. |
| `<vtex:metaTags/>` | **Meta Tags:** defines the page’s Meta Tags — tags that are useful for search engines to identify your content easily. |
| `<vtex.cmc:canonicalPage disable="true"/>` | **Disable canonical tag:** if this control is set to `true`, the canonical tag will be disabled on the given page. Using this tag informs search engines about duplicate content and prioritizes them correctly in page tracking. |
| `<vtex.cmc:departmentLinks/>` | **Department links:** displays links to the first level of categories (departments) created in the Admin. For the category to be listed, the Menu field must be enabled when [creating the category](https://help.vtex.com/en/tutorial/registering-a-category--tutorials_206).     |
| `<vtex.cmc:departmentNavigator/>` | **Department menu:** displays a menu with your store’s departments and categories (1st and 2nd level). To display the link for the complete list, the Menu field must be enabled when [creating categories](https://help.vtex.com/en/tutorial/registering-a-category--tutorials_206). This menu also displays brands with the *[Display in Home menu](https://help.vtex.com/en/tutorial/campos-de-cadastro-de-marca--37Ky7lTbEkiWIAYA80EMyI#)* option enabled and category specifications, such as size and color, for example. This control is indicated to be used as a lateral menu. |
| `<vtex.cmc:searchTitle/>` | **Page title:** displays the title of department, category, and search pages. |
| `<vtex.cmc:productQuickView/>` | **QuickView:** this control needs to be added before closing the `</body>` tag in the QuickView page template. It is fundamental for loading the files needed on the page. |
| `<vtex.cmc:ProductQueryStringReferenceShelf/>` | **Shelf:** allows you to configure a shelf in your store using the attributes listed below.  |

See below a description of the attributes of the **Shelf** control `<vtex.cmc:ProductQueryStringReferenceShelf/>`:

| Tag attribute | Description |
| ------------- | ----------- |
| `layout`                    | Shelf template ID. Required attribute. |
| `itemCount`                 | Number of items to be displayed. Required attribute. |
| `columnCount`               | Number of columns. Required attribute.       |
| `showUnavailable`           | When this attribute is set to `true`, the page will display out-of-stock products. |
| `selectionMode=”batch-buy”` | Non-required attribute that allows to order products in lots. |
| `isTrackable`               | When this attribute is set to `true`, this control is trackable. |
| `InternalCampaign`          | Name of the internal [campaign audience](https://help.vtex.com/en/tutorial/creating-campaign-audiences--6cnuDZJzIkIeocewAQQK4K). |
| `InternalPart`              | Internal *ViewPart* name.   |


Example of usage of the **Shelf** control:
```
<vtex.cmc:ProductQueryStringReferenceShelf layout="e2ed81f5-6241-4418-a47b-018d7482fcf0" itemCount="3" columnCount="3" showUnavailable="true" isTrackable="true" InternalCampaign="Destaque landing" InternalPart="Prateleira destaque"/>

```
## Controls for product pages

| Control | Description  |
| -------- | ----------- |
| `<vtex.cmc:ProductGifts />` |	**Display giveaways on the product page:** displays the giveaways attached to the product, if you have configured a Buy One Get One promotion in your store. [See how to configure this type of promotion](https://help.vtex.com/en/tutorial/how-to-set-a-buy-and-win-promotion-gift-for-a-specific-sku--4QlFtwxAju6qOwaCi2YS0G). |
| `<vtex.cmc:productName/>` |	**Product name:** displays the name of the product. |
| `<vtex.cmc:brandName/>` |	**Product brand with link:** displays the product brand, with a link to access a list of the brand’s products in your store.
| `<vtex.cmc:ProductImage/>` | **Thumbnail of the main product image:** displays a miniature representation of the main product image. To enable zoom in the image, you need to add the `zoom` attribute to the tag. Example: `<vtex.cmc:ProductImage zoom="on"/>`. |
| `<vtex.cmc:productReference/>` | **Product reference code:** displays the product’s reference code. |
| `<vtex.cmc:skuReference/>` |	**SKU reference code:** displays the reference code of the SKU. |
| `<vtex.cmc:skuPrice/>` |	**List prices, Computed prices, Installments, and “Save” promotion:** List prices and “Save” promotions are only displayed if the product’s computed price is lower than its list price. The most advantageous installment plan will be displayed to the customer, considering the total price of the order and only interest-free payment options. Does not display information when the product display mode is **SKU list**. |
| `<vtex.cmc:skuSelection />` |	**SKU selection:** allows to select the product variation following the Admin configuration (`radio` and `combo`). |
| `<vtex.cmc:OtherPaymentMethod/>` |	**View other payment methods:** displays the best payment and installment conditions for a SKU. The SKU must be available in stock for the control to be displayed. This control does not work for categories displayed as "List" in products with multiple SKUs.  |
| `<vtex.cmc:Delivery/>` |	**Availability:** displays the estimated time it will take for the product to be available, considering the default logistics route. |
| `<vtex.cmc:stockKeepingUnitRewardValue/>` |	**Loyalty Program Value:** displays the value of the SKU in the store's loyalty program. |
| `<vtex.cmc:BuyTogether/>` |	**Buy together:** displays the SKUs selected in the **Display together** field when adding a given SKU. |
| `<vtex.cmc:ProductDescription/>` |	**Product description:** displays the information entered in the **Description** field in the product registration form. |
| `<vtex.cmc:productDescriptionShort/>` |	**Product short description:** displays the value entered in the **Additional description** field in the product registration form. |
| `<vtex.cmc:productSpecification/>` |	**Product specification:** additional properties that can be added to your products. |
| `<vtex.cmc:StockKeepingUnitAttributes/>` |	**SKU specification:** also displays "unstructured attributes" used in sellers' products. |
| `<vtex.cmc:stockKeepingUnitMeasures/>` |	**Actual SKU dimensions:** shows the SKU’s height, width, length, and weight. |
| `<vtex.cmc:ProductTag/>` |	**Associated tags** |
| `<vtex.cmc:PageSearch/>` |	**Search within the product page** |
| `<vtex.cmc:BuyButton/>` |	**Buy button:** displays the button to add the product to the shopping cart. If the product is out of stock, this control will display the “Notify me” option, [if it is enabled](https://help.vtex.com/en/tutorial/set-up-the-avise-me--2VqVifQuf6Co2KG048Yu6e).  |
| `<vtex.cmc:BuyInPage/>` |	**Buy button (Asynchronous):** this control adds the product to the shopping cart asynchronously, i. e. without leaving the product page. For this control to work properly, it is required to use the `<vtex.cmc:AmountItemsInCart/>` control [as described in this article](#controls-for-department-category-and-search-pages). |
| `<vtex.cmc:stockKeepingUnitAmountAndUnitSelection />` | **Quantity selector with multiplier unit:** renders a fractional quantity field, considering the unit of measure and unit multiplier set for that SKU. The result is the quantity to be purchased. |
| `<vtex.cmc:evaluationRate/>` |	**Star ratings given by users:** displays users’ total ratings. |
| `<vtex.cmc:UserReview/>` |	**Ratings and reviews:** adds the option to rate and review products. Displays customer ratings and comments. |
| `<vtex.cmc:giftListInsertSku/>` |	**Add product to a list** |
| `<vtex.cmc:GiftListFormV2/>` |	**Form for creating a list** |
| `<vtex.cmc:HightLight/>` |	**Collection highlight flag** |
| `<vtex.cmc:discountHightLight/>` |	**Promotion highlight flag** |
| `<vtex.cmc:sellerDescription />` |	**Seller description:** name and image added for the seller of a given product. |
| `<vtex.cmc:SellerOptions />` |	**Seller options:** displays the sellers that offer the product, the product’s price on each seller and installment options (shows up to three different prices). |
| `<vtex.cmc:SalesChannelDropList />` |	**Trade policy list:** displays a list of available trade policies. |
| `<vtex:contentPlaceHolder id="ColecaoQVVT"/>` |	**”People who looked at this item also looked at” shelf:** in the CMS, adds a control of type **Related products**. When editing the element, select `QuemViu_Viu_Tambem` in the `_Tipo` field and create a new shelf template. |
| `<vtex:contentPlaceHolder id="ColecaoQVCT"/>` |	**“People who looked at this item also purchased” shelf:** in the CMS, adds a control of type **Related products**. When editing the element, select `QuemComprou_Viu_Tambem` in the `_Tipo` field and create a new shelf template. For this control to function correctly, your store needs a high flow of visitors and purchases.  |
| `<vtex:contentPlaceHolder id="ColecaoQCCT"/>` | **People who purchased this item also purchased” shelf:** in the CMS, adds a control of type **Related products**. When editing the element, select `QuemComprou_Comprou_Tambem` in the `_Tipo` field and create a new shelf template. |
| `<vtex:contentPlaceHolder id="Similares"/>` |	**Similar/Related products:** in the CMS, adds a control of type **Related products**. When editing the element, select `Similar` in the **Tipo** field. |
| `<vtex:contentPlaceHolder id="Acessorios"/>` |	**Accessories:** in the CMS, adds a control of type **Related products**. When editing the element, select `Acessorios` in the **Tipo** field. |
| `<vtex:contentPlaceHolder id="Sugestoes"/>` |	**Suggestions:** in the CMS, adds a control of type **Related products**. When editing the element, select `Sugestao` in the **Tipo** field. |
| `<vtex.cmc:facebookLike/>` |	**Facebook Like** |


### RichSnippets controls

The `<vtex.cmc:productRichSnippets />` control adds specific tags for information sharing with social networks, such as Google microformats, Facebook Open Graph, and Twitter card. Here are the testing tools:

1. [Google Structured Data Testing Tool](https://www.google.com/webmasters/tools/richsnippets)
2. [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/)
3. [Twitter Card Validator](https://cards-dev.twitter.com/validator)

| Property | Possible values |
|----------|-----------------|
| `showGoogle` |`{ “1”, “true”, “on”, “yes” }` |
| `showFacebook` | `{ “1”, “true”, “on”, “yes” }` |
| `Twitter` | `@accountname` of the Twitter account
| `doNotshowPrice` | `{ “1”, “true”, “on”, “yes” }` |
| `googleRate` | `{ “1”, “true”, “on”, “yes” }` |
| `fbAdmins` ||
| `fbAppId` ||

| Control | Examples of usage |
| ------- | ----------------- |
| `<vtex.cmc:productRichSnippets showGoogle="1"/>` | In order for the product to be indexed on Google, the control needs to be in the `<body>` tag.
| `<vtex.cmc:productRichSnippets showFacebook="1" fbAdmins="[fbAdmins]" fbAppId="[fbAppId]"/>` | For Facebook, the control needs to be in the `<head>` tag. `fbAdmins` and `fbAppId` settings are optional. |
| `<vtex.cmc:productRichSnippets Twitter="[TwitterAccount]"/>` | For Twitter, the control can be added to `<head>` or `<body>` tags. Settings can also be grouped together. |

## Controls for department, category, and search pages

| Control | Description |
|---------|-------------|
| `<vtex.cmc:advancedSearchFilter/>` |	**Advanced Search Filter**
| `<vtex.cmc:singleDepartmentNavigator/>` |	**Department menu:** the available attribute is `keepCurrentPath`. When the attribute is set to `true`, products will be displayed on the page. |
| `<vtex.cmc:searchNavigator/>` |	**Search menu/filter:** displays a menu with your store’s departments and categories (1st and 2nd level). To display the link for the **complete list**, the **Menu** field must be enabled when [creating categories](https://help.vtex.com/en/tutorial/registering-a-category--tutorials_206). |
| `<vtex.cmc:miniCart/>` | **Minicart control:** a shopping cart control used in the top menu on all pages — except Checkout and the order confirmation page. This control displays shopping cart information: items, quantities, and prices. |
| `<vtex.cmc:AmountItemsInCart>` | **Number of items in the shopping cart:** displays basic information about the shopping cart. It is required to use this control if you use the `<vtex.cmc:BuyInPage/>` control. You can use it for [KitLook](https://help.vtex.com/en/tutorial/how-to-assemble-a-look-kit--tutorials_266) cases, for example. |
| `<vtex.cmc:searchResult/>` | Product search result. See below the attributes of this control. |

See below a description of the `<vtex.cmc:searchResult/>` control attributes:

| Tag attribute | Description |
| --------------------------- | ---------------------------------------------------------------------------- |
| `layout`                    | Required attribute. Code of the shelf (template) that will display products. |
| `itemCount`                 | Required attribute. Number of items per page. |
| `columnCount`               | Required attribute. Number of columns. |
| `showUnavailable`           | When the attribute is set to true, out-of-stock products should be displayed. |
| `selectionMode=”batch-buy”` | Non-required attribute that allows to order products in lots. |
| `isTrackable`               | When the attribute is set to true, this control is trackable. |
| `InternalCampaign`          | Internal campaign audience name. |
| `InternalPart`              | Internal *ViewPart* name. |

Example of usage of search results:
```
<vtex.cmc:searchResult layout="48e223e6-da80-4610-b3d5-4e5cfaf94f13" itemCount="10" columnCount="4" isTrackable="true" InternalCampaign="Resultado busca landing" InternalPart="Resultado Busca" /> 
```

For more information, read the tutorial [Shelf template controls](https://developers.vtex.com/docs/guides/shelf-template-controls).

## Other controls

| Control | Description  |
|---------|--------------|
|`<vtex.cmc:orderList/>`| Displays the customer order list on the **Orders** section in **My account** – `/account/orders` |
|`<vtex.cmc:accountUserProfile/>`| Displays the customer's data in **My account** – `/account` |
|`<vtex.cmc:accountAddress/>`| Displays the customer’s addresses in **My account** page – `/account`|
| `<vtex.cmc:sellerInfo />` |	Displays the seller’s information on the platform, and should be used on the seller's detail page in the `seller-info` folder. |


## Deprecated controls

| Control | Description | Page |
| ------- | ----------- | ---- |
| `<vtex.cmc:productPageTitle/>`| **Product title:** deprecated control. | Product page |
| `<vtex.cmc:stockKeepingUnitSelection/>` | **SKU selection:** deprecated control. Now you need to use `<vtex.cmc:skuSelection/>`. | Product page |
| `<vtex.cmc:skuRichSelection changeImage="1"/>` | **SKU checkbox selection:** deprecated control.     | Product page |
| `<vtex.cmc:shippingValue/>` | **Calculate shipping cost and delivery time frame:** deprecated control, because it presents a [known issue](https://help.vtex.com/es/known-issues/a-viewpart-shippingvalue-nao-exibe-prazos-em-horas-corretamente--5hvl9eGxPLZAuNcFAFc9Vb#). | Product page |
| `<vtex.cmc:stockKeepingUnitService/>`                                  | **SKU services:** deprecated control.       | Product page |
| `<vtex.cmc:StockKeepingUnitPriceHistory Months="6" Percentile="100"/>` | **Price history**     | Product page |
| `<vtex.cmc:evaluationRate/>`    |   **Consumer rating (stars):** deprecated control. It previously displayed the average of star ratings by customers.           | Product page |
| `<vtex.cmc:UserReview/>`| **Ratings and comments:** deprecated control. It previously displayed an option to rate products, a form to make comments, results of ratings, and comments made. | Product page |
| `<vtex.cmc:welcomeMessage/>` | **User login:** deprecated control.  It was responsible for creating the IPI cookie used by the `<vtex.cmc:UserReview/>` control. Without it, when trying to make a review, the login was required in a loop. | Product page |
