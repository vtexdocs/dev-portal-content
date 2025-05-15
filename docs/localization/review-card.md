---
title: "ReviewCard"
excerpt: "Displays product review details in a structured card."
components:
  - ReviewCard.tsx
  - ReviewCardAuthor.tsx
  - ReviewCardDate.tsx
---

The `ReviewCard` component displays key details of a product review in a structured format. The final component is composed of the following:

- `ReviewCard`: Renders the main container that structures the review content. It displays the review title, text, rating, author information, and date, while managing expandable text functionality.
- `ReviewCardAuthor`: Displays the author’s name and verification status.
- `ReviewCardDate`: Displays the review date.

---
## Import

Import the component from [@faststore/ui](https://developers.vtex.com/docs/guides/faststore/components-index)

```tsx
import { ReviewCard, ReviewCardAuthor, ReviewCardDate } from '@faststore/ui'
```

### Import styles into your FastStore project

To apply the styles of this component in your FastStore project, import the following to your stylesheet:

```scss
@import '@faststore/ui/src/components/organisms/ReviewCard/styles.scss';

```

Follow the instructions in the [Importing FastStore UI component styles](https://developers.vtex.com/docs/guides/faststore/using-themes-importing-ui-components-styles) tutorial.

---
## Props

### ReviewCard

<ComponentPropsSection component="ReviewCard" />

### ReviewCardAuthor

<ComponentPropsSection component="ReviewCardAuthor" />

### ReviewCardDate

<ComponentPropsSection component="ReviewCardDate" />

---

## Design Tokens

<TokenTable>
  <TokenRow
    token="--fs-review-card-border-color"
    value="var(--fs-border-color-light)"
    isColor
  />
  <TokenRow
    token="--fs-review-card-border-width"
    value="var(--fs-border-width)"
  />
  <TokenRow
    token="--fs-review-card-padding-mobile"
    value="1.25rem 0"
  />
  <TokenRow
    token="--fs-review-card-gap-mobile"
    value="var(--fs-grid-gap-0)"
  />
</TokenTable>

### Nested Elements

<OverviewSection>
  <ReviewCard
    id="review-card-example"
    title="Great product!"
    text="I'm very satisfied with this product. It works well and meets my expectations."
    rating={5}
    author="John"
    date={new Date('2025-05-01')}
    isVerified={true}
    readMoreText="Read More"
    readLessText="Read Less"
  />
</OverviewSection>

```tsx
  <ReviewCard
    id="review-card-example"
    title="Great product!"
    text="I'm very satisfied with this product. It works well and meets my expectations."
    rating={5}
    author="John"
    date={new Date('2025-05-01')}
    isVerified={true}
    readMoreText="Read More"
    readLessText="Read Less"
  />
```
#### Header

<TokenTable>
  <TokenRow
    token="--fs-review-card-header-width-desktop"
    value="7rem"
  />
  <TokenRow
    token="--fs-review-card-header-gap"
    value="var(--fs-grid-gap-0)"
  />
</TokenTable>

#### Date

<TokenTable>
  <TokenRow
    token="--fs-review-card-date-color"
    value="var(--fs-color-text-light)"
    isColor
  />
  <TokenRow
    token="--fs-review-card-date-font-size"
    value="var(--fs-text-size-0)"
  />
  <TokenRow
    token="--fs-review-card-date-line-height"
    value="var(--fs-text-size-base)"
  />
  <TokenRow
    token="--fs-review-card-date-font-weight"
    value="var(--fs-text-weight-regular)"
  />
</TokenTable>

#### Text

<TokenTable>
  <TokenRow
    token="--fs-review-card-text-gap"
    value="var(--fs-spacing-0)"
  />
</TokenTable>

#### Title

<TokenTable>
  <TokenRow
    token="--fs-review-card-title-color"
    value="var(--fs-color-text)"
    isColor
  />
  <TokenRow
    token="--fs-review-card-title-font-size"
    value="var(--fs-text-size-2)"
  />
  <TokenRow
    token="--fs-review-card-title-font-weight"
    value="var(--fs-text-weight-medium)"
  />
  <TokenRow
    token="--fs-review-card-title-line-height"
    value="1.5"
  />
</TokenTable>

#### Text content

<TokenTable>
  <TokenRow
    token="--fs-review-card-text-content-color"
    value="var(--fs-color-text)"
    isColor
  />
  <TokenRow
    token="--fs-review-card-text-content-font-size"
    value="var(--fs-text-size-1)"
  />
  <TokenRow
    token="--fs-review-card-text-content-font-weight"
    value="var(--fs-text-weight-regular)"
  />
  <TokenRow
    token="--fs-review-card-text-content-line-height"
    value="1.5"
  />
</TokenTable>

#### Author

<TokenTable>
  <TokenRow
    token="--fs-review-card-author-gap"
    value="var(--fs-spacing-1)"
  />
  <TokenRow
    token="--fs-review-card-author-color"
    value="var(--fs-color-success-text)"
    isColor
  />
  <TokenRow
    token="--fs-review-card-author-font-size"
    value="var(--fs-text-size-0)"
  />
  <TokenRow
    token="--fs-review-card-author-font-weight"
    value="var(--fs-text-weight-regular)"
  />
  <TokenRow
    token="--fs-review-card-author-line-height"
    value="1.33"
  />
</TokenTable>

#### Desktop

<TokenTable>
  <TokenRow
    token="--fs-review-card-padding-desktop"
    value="var(--fs-spacing-3) 0 1.25rem"
  />
  <TokenRow
    token="--fs-review-card-gap-desktop"
    value="50px"
  />
</TokenTable>

---

## Customization

`data-fs-review-card`

`data-fs-review-card-header`

`data-fs-review-card-author="desktop | mobile"`

`data-fs-review-card-author-name`

`data-fs-review-card-date="desktop | mobile"`

`data-fs-review-card-text`

`data-fs-review-card-text-header`

`data-fs-review-card-text-title`

`data-fs-review-card-text-content`

`data-fs-review-card-text-content="expanded"`

`data-fs-review-card-text-read-more`

`data-fs-review-card-author-verified`
