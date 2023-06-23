---
title: "Creating and managing coupons with Promotions API"
slug: "creating-and-managing-coupons-with-promotions-api"
hidden: false
createdAt: "2020-09-14T20:52:19.857Z"
updatedAt: "2022-06-28T18:25:27.448Z"
---

A coupon is a code that when entered in the cart grants the customer a discount on the price of purchase for a determined product.

To make a coupon available for use you need to associate the coupon to a **Promotion**.

A single coupon can be associated with one or more promotions by filling the `utmSource` or `utmCampain` fields with the same values for both coupon and promotion configuration.

>⚠️ Coupons cannot be deleted, only archived. It is important to emphasize that you can only archive one coupon at a time. You can edit and reuse a coupon, but the `coupon code` can not be modified.

## Restrictions

There’s a quantity limit to the active coupons. We recommend reusing coupons because a high number of coupons can compromise the Promotions & Taxes performance.

## How to create a coupon

You can create one coupon or multiple coupons at a time.

- To create a single coupon, use the <span class="api pg-type type-post">POST</span> [Create coupon](https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api#post-/api/rnb/pvt/coupon/) endpoint.
- If you want to create multiple coupons use the <span class="api pg-type type-post">POST</span> [Create multiple coupons](https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api#post-/api/rnb/pvt/multiple-coupons) endpoint.

>❗ If you try to create a coupon with an existing `coupon code`, the API will update the existing coupon.

## How to edit a coupon

Coupons can be edited and reused as you wish. However, the `coupon code` cannot be modified.

>ℹ️ There is a limited quantity of active coupons. Coupon reuse is highly recommended since a high number of coupons may compromise the Promotions & Taxes performance.

## How to archive a coupon

As said before, you can only archive one coupon at a time. You must use the <span class="api pg-type type-post">POST</span> [Archive coupon by coupon code](https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api#post-/api/rnb/pvt/archive/coupon/-couponCode-) endpoint to do so.

## Examples of usage

### Creating 50 coupons

To create 50 different coupons with `coupon codes` randomly generated, you must use the [Create multiple coupons](https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api#post-/api/rnb/pvt/multiple-coupons) endpoint with `quantity` set to `50`.

If you want to define the `coupon codes`, you can use this route as well, setting the `coupon codes` params with the desired values and `quantity` as `1` for each `coupon configuration`, as the example below.

```json
[
    {
        "quantity": 1,
        "couponConfiguration": {
            "utmSource": "cupom1",
            "utmCampaign": null,
            "couponCode": "test1",
            "isArchived": false,
            "maxItemsPerClient": 10,
            "expirationIntervalPerUse": "00:00:00"
        }
    },
    {
        "quantity": 1,
        "couponConfiguration": {
            "utmSource": "cupom2",
            "utmCampaign": null,
            "couponCode": "test2",
            "isArchived": false,
            "maxItemsPerClient": 5,
            "expirationIntervalPerUse": "00:10:00"
        }
    }
]
```

You can associate these 50 coupons to a single promotion by repeating the same `utmSource` or `utmCampaign` in all of them, and then linking that UTM tag to the promotion. This can be done for any number of coupons.

To create or update a promotion, check the <span class="api pg-type type-post">post</span> [Create Or Update Promotion](https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api#post-/api/rnb/pvt/calculatorconfiguration) endpoint.

### Creating single-use coupon and promotion

Sandy is a frequent client of your store and it is her birthday. You can use the [Create coupon](https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api#post-/api/rnb/pvt/coupon/) endpoint with the `coupon code` set to `Birthday123`, associate it to a promotion then, send it to her.

To enable the single-use of a coupon, you must restrict the promotion to a single-use as well so she use the `Birthday123` code on her checkout for only one purchase. To do so, follow the steps bellow:

1. In the Admin, select the **Promotions & Taxes** module.
2. Click on **Promotions**.
3. Click on the **New Promotion** > **Regular** button.
4. Check the selection box of `utm_source` and add the `Birthday123` code to the field.
   ![cupom-Birthday123](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/creating-and-managing-coupons-with-promotions-api-0.png)
5. Uncheck the unlimited selection boxes from the **How many times will your promotion be applied in your store** and **How many times will your promotion be applied in your store per client fields**.
6. Add the number one to each field to enable the single-use promotion.
   ![restricao-promo-single](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/creating-and-managing-coupons-with-promotions-api-1.png)
7. Click on **Save**.

### Coupon massive generation

To create a large number of coupons with the same settings, you can use the [Coupon Massive Generation](https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api#post-/api/rnb/pvt/coupons) endpoint. This endpoint will generate the determined quantity of coupons differing only their names through automatic generation.

First, set the query param `quantity` to `10`, for example. Then, make the following request body:

```json
{
  "utmSource": "cupom",
  "utmCampaign": null,
  "couponCode": "ctest",
  "isArchived": false,
  "maxItemsPerClient": 1,
  "expirationIntervalPerUse": "00:00:00"
}
```

The result for the request will be the creation of ten coupons with the same settings and the following response body:

```json
[
    "ctest-wzcp5lwt7yz1s7n",
    "ctest-rb6smoassp2xe71",
    "ctest-vpw84ag9tfi8khv",
    "ctest-ne26wgmidp5ctht",
    "ctest-127ng0ox09tho5l",
    "ctest-qsowch8c8s7jipo",
    "ctest-6acbsst6zpss75l",
    "ctest-0bksc2tzh5ai946",
    "ctest-4jjx8u2rrqj4ck9",
    "ctest-hxiox1isdp6padl"
]
```
