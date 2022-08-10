---
title: "Promotions"
slug: "promotions-overview"
hidden: false
createdAt: "2021-05-20T18:50:02.913Z"
updatedAt: "2022-08-08T18:29:58.753Z"
---
[block:callout]
{
  "type": "info",
  "body": "📣 Help us improve our documentation! Share your feedback by filling out this [form](https://forms.gle/e32R6KD4L82X3ToeA)."
}
[/block]
This overview article goes over what you can accomplish with the VTEX Promotions and Taxes module, including relevant links to our developer documentation about this topic.

## Understanding promotion’s architecture in VTEX

A [promotion](https://help.vtex.com/en/tracks/promocoes--6asfF1vFYiZgTQtOzwJchR) is a discount granted to the customer. It may be associated with one or more products, with shipping or with a [trade policy](https://help.vtex.com/en/tutorial/criar-uma-politica-comercial--563tbcL0TYKEKeOY4IAgAE) (sales channels). At VTEX, the retailer can create a number of rules that, depending on the context of the purchase, will define whether and how the discount will be applied.

A tax is the opposite of a promotion, that is, it is an additional percentage added to the product price in order to increase the value.

Using the Promotions & Takes API allows you to manage and retrieve all promotions, coupons and tax rules from your VTEX store.

## Retrieving promotion information

A VTEX store can have different types of promotions and taxes for different kinds of trade policy. To retrieve information about your VTEX store promotions and taxes, access the available APIs:

* [Get All Promotions](https://developers.vtex.com/vtex-rest-api/reference/getallbenefits)
* [Get All Taxes](https://developers.vtex.com/vtex-rest-api/reference/getalltaxes)
* [Get Promotion or Tax By ID](https://developers.vtex.com/vtex-rest-api/reference/getcalculatorconfigurationbyid)
* [List archived Promotions](https://developers.vtex.com/vtex-rest-api/reference/getarchivedpromotions)
* [List archived Taxes](https://developers.vtex.com/vtex-rest-api/reference/getarchivedtaxes)

## Managing your Promotions

There are several actions a VTEX store can perform on promotions. In the next sections, you will find the main actions related to a store’s promotion management routine.

### Creating promotions or taxes

VTEX offers different types of promotions, you can create a promotion or tax, create multiple promotions by SKU and change the settings and data of any promotion using the APIs.

* [Create or Update Promotion or Tax](https://developers.vtex.com/vtex-rest-api/reference/createorupdatecalculatorconfiguration)
* [Create Multiple SKU Promotion](https://developers.vtex.com/vtex-rest-api/reference/post_api-rnb-pvt-import-calculatorconfiguration)

### Updating promotions with multiple SKUs

To update information from a Multiple SKU Promotion.

- [Update Multiple SKU Promotion](https://developers.vtex.com/vtex-rest-api/reference/put_api-rnb-pvt-import-calculatorconfiguration-promotionid)

### Archiving/Unarchiving promotions or taxes

If you no longer want a promotion to be used, you can move it to the list of archived promotions or unarchiving if you want to use it.

* [Archive Promotion or Tax](https://developers.vtex.com/vtex-rest-api/reference/archivepromotion-1)
* [Unarchive Promotion or Tax](https://developers.vtex.com/vtex-rest-api/reference/unarchivepromotion-1)

## Coupons

The coupon is a code entered in the cart by the customer. It grants a discount on the price of the purchase. To make a coupon available for use, you need to associate the coupon to a Promotion.

A single coupon can be associated with one or more promotions. But there’s a quantity limit to the active coupons. We recommend reusing coupons because a high number of coupons can compromise the Promotions & Taxes performance.
[block:callout]
{
  "type": "warning",
  "body": "Coupons cannot be deleted, only archived. It is important to emphasize that you can only archive one coupon at a time. You can edit and reuse a coupon, but the coupon code can not be modified."
}
[/block]
### Getting coupons

You can create one coupon or multiple coupons at a time. To create a single coupon, use the post *Create coupon* endpoint. If you want to create multiple coupons use the post *Create multiple coupons* endpoint.

To create a large number of coupons with the same settings, you can use the *Coupon Massive Generation* endpoint. This endpoint will generate the determined quantity of coupons differing only their names through automatic generation.
[block:callout]
{
  "type": "info",
  "body": "If you try to create a coupon with an existing coupon code, the API will update the existing coupon."
}
[/block]
* [Create coupon](https://developers.vtex.com/vtex-rest-api/reference/post_api-rnb-pvt-coupon)
* [Create multiple coupons](https://developers.vtex.com/vtex-rest-api/reference/post_api-rnb-pvt-multiple-coupons)
* [Coupon Massive Generation](https://developers.vtex.com/vtex-rest-api/reference/massivegeneration)

###  Retrieving coupon information

* [Get coupon by coupon code](https://developers.vtex.com/vtex-rest-api/reference/getbycouponcode)
* [Get archived coupon by coupon code](https://developers.vtex.com/vtex-rest-api/reference/getarchivedbycouponcode)
* [Get coupon usage](https://developers.vtex.com/vtex-rest-api/reference/getusage)
* [Get all coupons](https://developers.vtex.com/vtex-rest-api/reference/getall)

### Archiving/Unarchiving coupons

* [Archive coupon by coupon code](https://developers.vtex.com/vtex-rest-api/reference/archivebycouponcode)
* [Unarchive coupon by coupon code](https://developers.vtex.com/vtex-rest-api/reference/unarchivebycouponcode)

### Updating coupons

Coupons can be updated as you wish.

* [Update coupon](https://developers.vtex.com/vtex-rest-api/reference/update)
[block:callout]
{
  "type": "info",
  "body": "There is a limited quantity of active coupons. Coupon reuse is highly recommended since a high number of coupons may compromise the Promotions & Taxes performance."
}
[/block]
## Campaign Audiences

Campaign Audience is a feature that allows you to define the target audience for promotions, creating criteria for segmenting customers. 

Based on these criteria, the VTEX platform automatically validates whether customers are eligible for a particular campaign audience and, consequently, the associated campaign promotions.

### Creating campaign audiences

Using this API, you can create campaign audiences to segment your store's promotions based on defining [target audiences](https://help.vtex.com/en/tutorial/campaign-audiences--3o7lhpNseXY2WmjZO0gQ6m#target-audience) meeting specific criteria.

* [Create campaign audience](https://developers.vtex.com/vtex-rest-api/reference/setcampaignconfiguration)
[block:callout]
{
  "type": "info",
  "body": "To activate the newly created campaign audience, you must associate it to a [Campaign promotion](https://help.vtex.com/en/tutorial/campaign-promotion--1ChYXhK2AQGuS6wAqS8Ume)."
}
[/block]
### Retrieving campaign audience information

* [Get campaign audience configuration](https://developers.vtex.com/vtex-rest-api/reference/getcampaignconfiguration)
* [Get all campaign audiences](https://developers.vtex.com/vtex-rest-api/reference/getcampaignaudiences)

## Policy Engine

The Policy Engine API creates [promotion alarms](https://developers.vtex.com/vtex-rest-api/docs/using-policy-engine-api-on-promotion-alerts) when selling products with undesired prices and promotions. It will create conditions that will check if the prices and the promotions are correct.

If not, the system will alert the store with information about the product sold at unexpected prices.

### Creating a promotion alert

To create a new promotion alert, you should use this API. 

* [Create Policy](https://developers.vtex.com/vtex-rest-api/reference/policy_createorupdate)

### Retrieving policy engine information

* [Get Policy by ID](https://developers.vtex.com/vtex-rest-api/reference/policy_get)
* [Get Policy List](https://developers.vtex.com/vtex-rest-api/reference/policy_list)

### Evaluating policies

* [Evaluate Policies](https://developers.vtex.com/vtex-rest-api/reference/policy_evaluate)

### Updating an existing policy 

To update an existing promotion alert, you should use this API.

* [Update Policy](https://developers.vtex.com/vtex-rest-api/reference/put_api-policy-engine-policies-id)

### Deleting a policy

To delete an existing promotion alert, you should use this API.

* [Delete Policy by ID](https://developers.vtex.com/vtex-rest-api/reference/policy_delete)

## Adding optional configurations

There are optional settings available for you to manage your store’s orders. This allows you to take advantage of other VTEX capabilities, such as [B2B](https://help.vtex.com/en/tutorial/b2b-overview--5vb9SNXhX2bZnkpAh7ADdC).

* [Installing B2B Easy Set Up](https://developers.vtex.com/vtex-developer-docs/docs/installing-b2b-easy-set-up)