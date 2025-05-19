---
title: "RatingSummary"
excerpt: "Provides an overview of the information related to a product's reviews."
components:
  - RatingSummary.tsx
  - RatingDistribution.tsx
  - RatingDistributionItem.tsx
---

The `RatingSummary` component provides detailed information about a product’s rating reviews. The final component is composed of the following:

`RatingSummary`: Displays the average rating and total number of reviews. It also renders a button for writing a review and, if available, shows the rating distribution.
`RatingDistribution`: Renders an ordered list showing the percentage of reviews for each star rating from 1 to 5.
`RatingDistributionItem`: Represents a single rating level with a star icon, a percentage bar, and a numeric percentage label.

---

## Import

Import the component from [@faststore/ui](https://developers.vtex.com/docs/guides/faststore/components-index)

```tsx
import { RatingSummary, RatingDistribution, RatingDistributionItem } from '@faststore/ui'
```

### Import styles into your FastStore project

To apply the styles of this component in your FastStore project, import the following to your stylesheet:

```scss
@import '@faststore/ui/src/components/organisms/RatingSummary/styles.scss';

```

Follow the instructions in the [Importing FastStore UI component styles](https://developers.vtex.com/docs/guides/faststore/using-themes-importing-ui-components-styles) tutorial.

---

## Props

### RatingSummary

<ComponentPropsSection component="RatingSummary" />

### RatingDistribution

<ComponentPropsSection component="RatingDistribution" />

### RatingDistributionItem

<ComponentPropsSection component="RatingDistributionItem " />

---

## Design tokens

<TokenTable>
  <TokenRow
    token="--fs-rating-summary-width"
    value="100%"
  />
  <TokenDivider />
  <TokenRow
    token="--fs-rating-summary-width (tablet)"
    value="30%"
  />
  <TokenDivider />
  <TokenRow
    token="--fs-rating-summary-min-height"
    value="15rem"
  />
  <TokenRow
    token="--fs-rating-summary-line-height"
    value="1"
  />
  <TokenRow
    token="--fs-rating-summary-gap"
    value="var(--fs-spacing-4)"
  />
  <TokenRow
    token="--fs-rating-summary-padding"
    value="var(--fs-spacing-5)"
  />
  <TokenRow
    token="--fs-rating-summary-font-size"
    value="var(--fs-text-size-0)"
  />
  <TokenRow
    token="--fs-rating-summary-font-weight"
    value="var(--fs-text-weight-regular)"
  />
  <TokenRow
    token="--fs-rating-summary-border-radius"
    value="var(--fs-border-radius)"
  />
  <TokenRow
    token="--fs-rating-summary-background-color"
    value="var(--fs-color-neutral-1)"
    isColor
  />
</TokenTable>

### Nested elements

<OverviewSection>
    <RatingSummary
      id="rating-summary-example"
      ratingValue={4.2}
      reviewCount={18}
      distribution={{
        starsOne: 5,
        starsTwo: 3,
        starsThree: 2,
        starsFour: 4,
        starsFive: 4,
      }}
      textLabels={{
        ratingCounter: {
          multipleReviewsText: 'Reviews',
        },
      }}
    />
</OverviewSection>

```tsx
    <RatingSummary
      id="rating-summary-example"
      ratingValue={4.2}
      reviewCount={18}
      distribution={{
        starsOne: 5,
        starsTwo: 3,
        starsThree: 2,
        starsFour: 4,
        starsFive: 4,
      }}
      textLabels={{
        ratingCounter: {
          multipleReviewsText: 'Reviews',
        },
      }}
    />
```

#### Header

<TokenTable>
  <TokenRow
    token="--fs-rating-summary-header-vertical-gap"
    value="var(--fs-spacing-0)"
  />
  <TokenRow
    token="--fs-rating-summary-header-average-font-size"
    value="var(--fs-text-size-7)"
  />
  <TokenRow
    token="--fs-rating-summary-header-average-font-weight"
    value="var(--fs-text-weight-semibold)"
  />
  <TokenRow
    token="--fs-rating-summary-header-total-count-color"
    value="var(--fs-color-text-light)"
    isColor
  />
</TokenTable>

#### Distribution

<TokenTable>
  <TokenRow
    token="--fs-rating-distribution-vertical-gap"
    value="var(--fs-spacing-1)"
  />
</TokenTable>

#### Distribution item

<TokenTable>
  <TokenRow
    token="--fs-rating-distribution-item-gap"
    value="var(--fs-spacing-2)"
  />
  <TokenRow
    token="--fs-rating-distribution-item-star-gap"
    value="var(--fs-spacing-0)"
  />
  <TokenRow
    token="--fs-rating-distribution-item-star-icon-size"
    value="var(--fs-spacing-2)"
  />
</TokenTable>

#### Distribution item bar

<TokenTable>
  <TokenRow
    token="--fs-rating-distribution-item-bar-height"
    value="var(--fs-spacing-0)"
  />
  <TokenRow
    token="--fs-rating-distribution-item-bar-radius"
    value="var(--fs-border-radius-pill)"
  />
  <TokenRow
    token="--fs-rating-distribution-item-bar-track-color"
    value="var(--fs-color-neutral-2)"
    isColor
  />
  <TokenRow
    token="--fs-rating-distribution-item-bar-fill-color"
    value="var(--fs-color-main-2)"
    isColor
  />
  <TokenRow
    token="--fs-rating-distribution-item-bar-transition-function"
    value="var(--fs-transition-function)"
  />
  <TokenRow
    token="--fs-rating-distribution-item-bar-transition-property"
    value="var(--fs-transition-property)"
  />
  <TokenRow
    token="--fs-rating-distribution-item-bar-transition-timing"
    value="var(--fs-transition-timing)"
  />
</TokenTable>

---

## Customization

`data-fs-cart-sidebar`

`data-fs-cart-sidebar-title`

`data-fs-cart-sidebar-list`

`data-fs-cart-sidebar-footer`
