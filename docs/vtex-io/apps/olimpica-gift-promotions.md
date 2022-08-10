---
title: "[ WORK IN PROGRESS ] Manhattan Gift Promotions"
slug: "olimpica-gift-promotions"
excerpt: "olimpica.gift-promotions@0.0.10"
hidden: true
createdAt: "2022-08-09T15:57:39.742Z"
updatedAt: "2022-08-09T15:57:39.742Z"
---
An Manhattan Gift Promotions app that adds a menu button to the admin sidebar with the purpose of create and update only gift promotions.

### Quickstart

1. Clone this repo

2. `yarn --cwd react/` for code completion

3. `vtex link`

4. Navigate to `workspace--account.myvtex.com/admin/custom/promotion`

# Query and mutation example

### getAllPromotions

```
{
    getAllPromotions {
      idCalculatorConfiguration
      lastModifiedUtc
      name
      beginDate
      endDate
      isActive
      description
      type
      utmSource
      utmCampain
      utmiCampaign
      status
      percentualTax
      isArchived
      hasMaxPricePerItem
      isTax
      Campaigns
      activateGiftsMultiplier
      effectType
      scope
      maxUsage
      idsSalesChannel
      areSalesChannelIdsExclusive
}
```

### getPromotionById

```
{
  getPromotionById(id: "1b807784-6a17-4adf-8b5e-61058b82f356") {
    idCalculatorConfiguration
    name
    description
    beginDateUtc
    endDateUtc
    lastModified
    daysAgoOfPurchases
    isActive
    isArchived
    isFeatured
    disableDeal
    activeDaysOfWeek
    offset
    activateGiftsMultiplier
    newOffset
    maxPricesPerItems
    cumulative
    nominalShippingDiscountValue
    absoluteShippingDiscountValue
    nominalDiscountValue
    maximumUnitPriceDiscount
    percentualDiscountValue
    rebatePercentualDiscountValue
    percentualShippingDiscountValue
    percentualTax
    shippingPercentualTax
    percentualDiscountValueList1
    percentualDiscountValueList2
    skusGift {
      quantitySelectable
      gifts {
        id
        name
        quantity
        sellers {
          id
          name
        }
      }
    }
    nominalRewardValue
    percentualRewardValue
    orderStatusRewardValue
    maxNumberOfAffectedItems
    maxNumberOfAffectedItemsGroupKey
    applyToAllShippings
    nominalTax
    origin
    idSeller
    idSellerIsInclusive
    idsSalesChannel
    areSalesChannelIdsExclusive
    marketingTags
    marketingTagsAreNotInclusive
    paymentsMethods
    stores
    campaigns
    storesAreInclusive
    categories
    categoriesAreInclusive
    brands
    brandsAreInclusive
    products {
      id
      name
    }
    productsAreInclusive
    skus
    skusAreInclusive
    collections1BuyTogether
    collections2BuyTogether
    minimumQuantityBuyTogether
    quantityToAffectBuyTogether
    enableBuyTogetherPerSku
    listSku1BuyTogether
    listSku2BuyTogether
    coupon
    totalValueFloor
    totalValueCeling
    totalValueIncludeAllItems
    totalValueMode
    collections {
      id
      name
    }
    collectionsIsInclusive
    restrictionsBins
    cardIssuers
    totalValuePurchase
    slasIds
    isSlaSelected
    isFirstBuy
    firstBuyIsProfileOptimistic
    compareListPriceAndPrice
    isDifferentListPriceAndPrice
    zipCodeRanges
    itemMaxPrice
    itemMinPrice
    installment
    isMinMaxInstallments
    minInstallment
    maxInstallment
    merchants
    clusterExpressions
    clusterOperator
    paymentsRules
    giftListTypes
    productsSpecifications
    affiliates
    maxUsage
    maxUsagePerClient
    multipleUsePerClient
    type
    useNewProgressiveAlgorithm
    percentualDiscountValueList
  }
}

```

### createPromotion

```
mutation createPromotion($data: IPromotion) {
    createPromotion(data: $data) {
        idCalculatorConfiguration
        name
        description
        beginDateUtc
        endDateUtc
        lastModified
        daysAgoOfPurchases
        isActive
        isArchived
        isFeatured
        disableDeal
        activeDaysOfWeek
        offset
        activateGiftsMultiplier
        newOffset
        maxPricesPerItems
        cumulative
        nominalShippingDiscountValue
        absoluteShippingDiscountValue
        nominalDiscountValue
        maximumUnitPriceDiscount
        percentualDiscountValue
        rebatePercentualDiscountValue
        percentualShippingDiscountValue
        percentualTax
        shippingPercentualTax
        percentualDiscountValueList1
        percentualDiscountValueList2
        skusGift {
            quantitySelectable
            gifts {
                id
                name
                quantity
                sellers {
                    id
                    name
                }
            }
        }
        nominalRewardValue
        percentualRewardValue
        orderStatusRewardValue
        maxNumberOfAffectedItems
        maxNumberOfAffectedItemsGroupKey
        applyToAllShippings
        nominalTax
        origin
        idSeller
        idSellerIsInclusive
        idsSalesChannel
        areSalesChannelIdsExclusive
        marketingTags
        marketingTagsAreNotInclusive
        paymentsMethods
        stores
        campaigns
        storesAreInclusive
        categories
        categoriesAreInclusive
        brands
        brandsAreInclusive
        products {
            id
            name
        }
        productsAreInclusive
        skus
        skusAreInclusive
        collections1BuyTogether
        collections2BuyTogether
        minimumQuantityBuyTogether
        quantityToAffectBuyTogether
        enableBuyTogetherPerSku
        listSku1BuyTogether
        listSku2BuyTogether
        coupon
        totalValueFloor
        totalValueCeling
        totalValueIncludeAllItems
        totalValueMode
        collections {
            id
            name
        }
        collectionsIsInclusive
        restrictionsBins
        cardIssuers
        totalValuePurchase
        slasIds
        isSlaSelected
        isFirstBuy
        firstBuyIsProfileOptimistic
        compareListPriceAndPrice
        isDifferentListPriceAndPrice
        zipCodeRanges
        itemMaxPrice
        itemMinPrice
        installment
        isMinMaxInstallments
        minInstallment
        maxInstallment
        merchants
        clusterExpressions
        clusterOperator
        paymentsRules
        giftListTypes
        productsSpecifications
        affiliates
        maxUsage
        maxUsagePerClient
        multipleUsePerClient
        type
        useNewProgressiveAlgorithm
        percentualDiscountValueList
    }
}

```