---
title: "Pricing"
slug: "pricing-overview"
hidden: false
createdAt: "2022-08-01T20:19:35.374Z"
updatedAt: "2022-08-05T17:29:19.253Z"
---
[block:callout]
{
  "type": "info",
  "body": "📣 Help us improve our documentation! Share your feedback by filling out this [form](https://forms.gle/e32R6KD4L82X3ToeA)."
}
[/block]
The Prices module, also called Pricing, is a system responsible for the creation, editing and storing of your SKU pricing data. This overview article goes over what you can accomplish with Pricing, including relevant links to our developer documentation about this topic.


## Understanding VTEX’s Pricing architecture

**Prices** represent your SKU sales value information. In VTEX, these prices are stored in **price tables.** In turn, these price tables can be applied to different **contexts**, like trade policies. These concepts are related as shown in the image below. Learn more about VTEX's pricing architecture in our [Pricing system architecture](https://help.vtex.com/tracks/prices-101--6f8pwCns3PJHqMvQSugNfP/7GptzvlPDVM11ojEjywIQx) article. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/db14048-Screen_Shot_2022-08-03_at_17.18.09.png",
        "Screen Shot 2022-08-03 at 17.18.09.png",
        640,
        790,
        "#a34b69"
      ],
      "sizing": "smart"
    }
  ]
}
[/block]
<br>

##  Importing prices from an ERP or Back office Integration

If your store has an ERP integration or another kind of integration for managing orders, it will be necessary to make an integration with VTEX’s platform. Defining prices for your SKUs is an important step when setting up your store. VTEX accounts are able to import prices through ERP integrations by following the guide linked below. 

* [Back office (ERP/PIM/WMS)](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-guide)
* [Import prices](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-import-prices)  

<br>

## Managing Prices

There are several actions a VTEX store can perform on prices. In the next sections, you will find the main actions related to a store’s pricing management routine.

Before using our Pricing API Reference, check out our [Pricing v2 - API Reference Overview](https://developers.vtex.com/vtex-rest-api/reference/pricing-api-overview) for more details about rate limits.

[block:callout]
{
  "type": "info",
  "body": "Pricing v2 is the second generation of our pricing module, and is the only version currently available in VTEX. We have [discontinued Pricing v1](https://help.vtex.com/en/announcements/pricing-v1-module-will-be-discontinued-update-your-store-by-september--46YxKNOCLH2Ykw6a9uyxXB) in 2020 and our documentation refers to Pricing v2."
}
[/block]
### Creating base and fixed prices

An SKU's [base price](https://help.vtex.com/tracks/prices-101--6f8pwCns3PJHqMvQSugNfP/3XcXp0r5WrJvogB8KIX4Kx) represents the SKU's reference price for all price tables. This means that if another price is not created for the SKU in another price table, it inherits the item's base price. Its value is calculated from multiplying the SKU's _Cost Price_ with its _Markup_, or the desired profit margin for the SKU's sale.

The [fixed price](https://help.vtex.com/tracks/prices-101--6f8pwCns3PJHqMvQSugNfP/3HxF2u5VwidqnUGnFoKdDy) is an SKU's price for a specific price table that weighs more than any of the other pricing types, which results in the pricing module ignoring the other values when a fixed price is associated with an SKU.



* [Create or Update Base Price or Fixed Prices](https://developers.vtex.com/vtex-rest-api/reference/createupdatepriceorfixedprice)
* [Scheduling prices for a range of hours](https://developers.vtex.com/vtex-rest-api/docs/scheduling-prices-for-a-range-of-hours) 



### Updating price tables

A [price table](https://help.vtex.com/tracks/prices-101--6f8pwCns3PJHqMvQSugNfP/1wAm5m3IUfIj6maBdaRJt8) is a set of SKU prices that can be applied to a specific context. These tables store the price information that is displayed on a store's page. We can look at the price table as an entity that stores and delivers computed prices of its SKUs. 


* [Update rules for a price table](https://developers.vtex.com/vtex-rest-api/reference/put_pipeline-catalog-pricetableid)
* [Master Data](https://developers.vtex.com/vtex-rest-api/docs/master-data-introduction) is used to [connect a price table to a desired context](https://help.vtex.com/en/tutorial/criando-promocao-para-um-cluster-de-clientes--tutorials_342)

### Managing fixed prices for price tables or trade policies (sales channels)

[Trade policies](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV), or sales channels, are used in VTEX to differentiate the catalog, prices and logistics settings for each sales channel connected to your store. You may use them, for example, if you want the same list of SKUs to have different prices in each marketplace where your store is selling.

Manage prices configured in price tables or in different trade policies (sales channels) through the endpoints below. 

* [Create or Update Fixed Prices on a price table or trade policy](https://developers.vtex.com/vtex-rest-api/reference/createorupdatefixedpricesonpricetableortradepolicy)
* [Delete Fixed Prices on a price table or trade policy](https://developers.vtex.com/vtex-rest-api/reference/deletefixedpricesonapricetableortradepolicy-1)


### Deleting price by SKU

It is possible to use the following API calls to delete individual SKU prices. 

* [Delete price](https://developers.vtex.com/vtex-rest-api/reference/deleteprice)

It is only possible to delete a price table by removing all of the prices inserted in it, and in sequence requesting it to our Support. 

[block:callout]
{
  "type": "warning",
  "body": "It is only possible to delete a price table by removing all of the prices inserted in it, and in sequence requesting it to our [VTEX Support](https://help.vtex.com/support?cultureInfo=en-us).",
  "title": "Deleting price tables"
}
[/block]
<br>

##  Retrieving pricing information

You can fetch information related to prices in multiple ways and about specific topics. To know more about retrieving prices' content, see the links below.

### Price by SKU

* [Get price](https://developers.vtex.com/vtex-rest-api/reference/getprice)


### Fixed price

* [Get fixed prices](https://developers.vtex.com/vtex-rest-api/reference/getfixedprices)


### Price tables

* [Get rules for a price table](https://developers.vtex.com/vtex-rest-api/reference/getrulesforapricetable)
* [Get all price tables and their rules](https://developers.vtex.com/vtex-rest-api/reference/getallpricetablesandrules)
* [List price tables](https://developers.vtex.com/vtex-rest-api/reference/listpricetables)
* [Get Fixed Prices on a price table or trade policy](https://developers.vtex.com/vtex-rest-api/reference/getfixedpricesonapricetable)


### Fixed prices

* [Get fixed prices](https://developers.vtex.com/vtex-rest-api/reference/getfixedprices)


### Computed prices

There are some criteria that the system takes into account when deciding what an SKU's selling price for a specific price table should be. This price is called the [computed price](https://help.vtex.com/tracks/prices-101--6f8pwCns3PJHqMvQSugNfP/7GptzvlPDVM11ojEjywIQx#computed-price).

* [Get Computed Price by price table or trade policy](https://developers.vtex.com/vtex-rest-api/reference/getcomputedpricebypricetable)


### Pricing configuration and status

Retrieve information about your VTEX Admin's pricing configurations and Pricing status. 

* [Get Pricing Configuration](https://developers.vtex.com/vtex-rest-api/reference/getpricingconfig)
* [Get Pricing Status](https://developers.vtex.com/vtex-rest-api/reference/getpricingv2status) 

<br>

## Additional settings (optional)

Besides setting up your basic pricing configurations, there are optional additional settings you can make to customize prices for different scenarios and applications in your ecommerce architecture. See the following links for more information. 


### Storefront customization

Edit your storefront with [VTEX IO Store Framework](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-what-is-vtex-store-framework) to add basic or advanced components related to prices in your store. 

* [Store Framework basic components: Product Price app](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-price)
* [Displaying asynchronous prices](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-displaying-asynchronous-prices)
* [Internationalizing product prices](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-internationalizing-product-prices)
* [Translating the component - Adjusting price representations](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-8-translating-the-component#adjusting-price-representations)
* [Enabling Manual Price in my store](https://developers.vtex.com/vtex-rest-api/docs/enabling-manual-price-in-my-store)

<br>

### Pricing simulation - B2B

There are multiple ways you can [configure your B2B store](https://developers.vtex.com/vtex-developer-docs/docs/b2b-setup) with VTEX. The links below go over the different pricing settings required for B2B scenarios. 

The Price Simulations API allows you to configure custom price selectors for B2B stores, based on the context set by the Orders Configuration app.



* [Pricing Simulation Overview](https://developers.vtex.com/vtex-rest-api/reference/price-simulations-api-overview)
* [Get custom prices schema](https://developers.vtex.com/vtex-rest-api/reference/get_-v-custom-prices-session-schema)
* [Create or update custom prices schema](https://developers.vtex.com/vtex-rest-api/reference/post_-v-custom-prices-session-schema)
* [Update Order Configuration](https://developers.vtex.com/vtex-rest-api/reference/post_sessions)
* [Get price association by ID](https://developers.vtex.com/vtex-rest-api/reference/get_-v-custom-prices-rules-priceassociationid)
* [Disassociate price association by ID](https://developers.vtex.com/vtex-rest-api/reference#delete_-v-custom-prices-rules-priceassociationid)
* [Update price association by ID](https://developers.vtex.com/vtex-rest-api/reference#put_-v-custom-prices-rules-priceassociationid)

<br>

### External marketplace integration

If you are an [external marketplace](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide) that wishes to integrate with VTEX sellers, you can see the links below to learn how to get price information from sellers.

* [External marketplace - marketplace / seller architecture ](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-architecture#pricing--promotions)
* [External marketplace - How to keep prices updated](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-price-update)