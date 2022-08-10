---
title: "Bazaarvoice"
slug: "vtex-bazaarvoice"
excerpt: "vtex.bazaarvoice@2.2.6"
hidden: false
createdAt: "2020-06-03T15:19:16.075Z"
updatedAt: "2022-08-01T16:08:12.306Z"
---
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors)

## Description

This is a Bazaarvoice first party integration app that is responsible for showing the components related to Bazaarvoice Reviews in your store.

:loudspeaker: **Disclaimer:** Don't fork this project; use, contribute, or open issue with your feature request.

## Release schedule

| Release |       Status        | Initial Release | Maintenance LTS Start | End-of-life | Store Compatibility |
| :-----: | :-----------------: | :-------------: | :-------------------: | :---------: | :-----------------: |
|  [1.x]  | **Current Release** |   2019-06-14    |                       |             |         2.x         |


See our [LTS policy](https://github.com/vtex-apps/awesome-io#lts-policy) for more information.

## Table of Contents

- [Usage](#usage)
  - [Configuration](#configuration)
  - [Styles API](#styles-api)
    - [CSS namespaces](#css-namespaces)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Tests](#tests)

## Usage

To use the bazaarvoice components add the [product reviews](https://github.com/vtex-apps/product-review-interfaces/tree/master/example
) blocks into your theme as you would with any other block.

#### Configuration

You can set some options of the Reviews component in the CMS:

| Prop name      | Type     | Description                                          | Default value |
| -------------- | -------- | ---------------------------------------------------- | ------------- |
| `Quantity of reviews per page`         | `number` | the number of reviews that a review page will have                                            | `10`           |
| `Quantity of reviews on the first page`         | `number` | the number of reviews that the first review page will have                                            | Same as the value above          |

### Styles API

This app provides some CSS classes as an API for style customization.

To use this CSS API, you must add the `styles` builder and create an app styling CSS file and add `vtex.bazaarvoice` to your theme `peerDependencies`.

1. Add the `styles` builder to your `manifest.json`:

```json
  "builders": {
    "styles": "1.x"
  }
```

2. Add `vtex.bazaarvoice` to `peerDependencies` in your `manifest.json`:

```json
  "peerDependencies": {
    "vtex.bazaarvoice": "1.x"
  }
```

3. Create a file called `vtex.bazaarvoice.css` inside the `styles/css` folder. Add your custom styles:

```css
.container {
  margin-top: 10px;
}
```

#### CSS namespaces

Below, we describe the namespaces that are defined in the bazaarvoice.

| Token name   | Description                                          | Component Source                     |
| ------------ | ---------------------------------------------------- | ------------------------------------ |
| reviews  |   The reviews component | [NoReviews](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/NoReviews.tsx),    [Reviews](https://github.com/vtex-apps/bazaarvoice/blob/master/react/Reviews.js)|
| reviewsTitle  | The reviews title  | [NoReviews](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/NoReviews.tsx),    [Reviews](https://github.com/vtex-apps/bazaarvoice/blob/master/react/Reviews.js)  |
| ratingSummary  |  Rating Summary |  [RatingSummary](https://github.com/vtex-apps/bazaarvoice/blob/master/react/RatingSummary.js) |
| ratingSummaryContainer  | Main container of the Rating Summary  | [RatingSummary](https://github.com/vtex-apps/bazaarvoice/blob/master/react/RatingSummary.js)  |
| ratingSummaryStars  | Stars of the Rating Summary  | [RatingSummary](https://github.com/vtex-apps/bazaarvoice/blob/master/react/RatingSummary.js)  |
| ratingSummaryStars--loading  | Style of the Stars of the Rating Summary when they are loading  | [RatingSummary](https://github.com/vtex-apps/bazaarvoice/blob/master/react/RatingSummary.js)  |
| ratingSummaryWrite  | 'Write Review' link next to the stars of the Summary Container  | [RatingSummary](https://github.com/vtex-apps/bazaarvoice/blob/master/react/RatingSummary.js)  |
| ratingInline  | Rating in Line  | [RatingInLine](https://github.com/vtex-apps/bazaarvoice/blob/master/react/RatingInline.tsx)  |
| reviewForm  |  Review Form |  [ReviewForm](https://github.com/vtex-apps/bazaarvoice/blob/master/react/ReviewForm.js) |
| ratingStars  |  Container of the rating stars | [Stars](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Stars.tsx)  |
| ratingStarsInactive  | Style of the Stars when they are inactive  | [Stars](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Stars.tsx)   |
| ratingStarsActive  | Style of the Stars when they are active  | [Stars](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Stars.tsx)   |
| histogramStarContainer  | Histogram Star Container  | [Histogram](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Histogram.tsx)  |
| histogramOuterContainer | Histogram most external container | [Histogram](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Histogram.tsx)  |
| histogramContainer |  Histogram main container | [Histogram](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Histogram.tsx)  |
| histogramLine | Histogram line containing the data of a certain amount of star  | [Histogram](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Histogram.tsx)   |
| histogramStar | Histogram Star  | [Histogram](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Histogram.tsx)  |
| histogramBar | Histogram Bar  | [Histogram](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Histogram.tsx)  |
| histogramBarValue |  Histogram Bar filling | [Histogram](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Histogram.tsx)  |
| histogramCount | The count at the side of the histogram bar  | [Histogram](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Histogram.tsx)  |
| secondaryHistogramLine |  Histogram line containing the data of the secondary ratings |[Histogram](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Histogram.tsx)   |
| secondaryHistogramLabel |  The label of a secondary histogram line | [Histogram](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Histogram.tsx)   |
| secondaryHistogramBar | Secondary ratings' histogram bar  | [Histogram](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Histogram.tsx)   |
| secondaryHistogramBarValue | Secondary ratings' histogram bar filling  | [Histogram](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Histogram.tsx)   |
| secondaryHistogramCount |  Secondary ratings' histogram count | [Histogram](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Histogram.tsx)   |
| reviewHistogramBar | Review Histogram Bar   | [Review](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Review.tsx)  |
| reviewHistogramBarValue | Review Histogram Bar filling  | [Review](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Review.tsx)  |
| histogramDivisions | Histogram division that separates it in five sections  | [HistogramBar](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/HistogramBar.tsx)   |
| review | Review  |  [Review](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Review.tsx)  |
| reviewRating | Review Rating  | [Review](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Review.tsx)   |
| reviewTitle |  Review Title | [Review](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Review.tsx)   |
| reviewSubmittedField | Review 'submitted' field  | [Review](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Review.tsx)   |
| reviewByField | Review 'by' field | [Review](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Review.tsx)   |
| reviewFromField | Review 'from' field  | [Review](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Review.tsx)   |
| reviewText | Review text  | [Review](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Review.tsx)   |
| reviewImagesContainer | Review image container  | [Review](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Review.tsx)   |
| reviewImage | Review image  | [Review](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Review.tsx)   |
| reviewsContainer |  Reviews container |  [ReviewsContainer](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/ReviewsContainer.tsx) |
| reviewsContainerHead |  Reviews Container head | [ReviewsContainer](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/ReviewsContainer.tsx)  |
| reviewsContainerTitle | Reviews container title  | [ReviewsContainer](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/ReviewsContainer.tsx)  |
| reviewsContainerDropdowns |  Reviews container dropdown buttons | [ReviewsContainer](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/ReviewsContainer.tsx)  |
| reviewsContainerSortDropdown | Reviews container sort button  | [ReviewsContainer](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/ReviewsContainer.tsx)  |
| reviewsContainerStarsDropdown | Reviews container stars button  | [ReviewsContainer](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/ReviewsContainer.tsx)  |
| reviewsContainerWriteButton | Reviews container write button  | [ReviewsContainer](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/ReviewsContainer.tsx)  |
| noReviewsContainer | Container that appears when there are no reviews  | [NoReviews](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/NoReviews.tsx)  |
| writeReviewButton |  Write review button | [ReviewsContainer](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/ReviewsContainer.tsx),  [NoReviews](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/NoReviews.tsx) |
| activeStar | Active star  | [Stars](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Stars.tsx)  |
| activeStarContainer | Active star container  |  [Stars](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Stars.tsx) |
| inactiveStar | Inactive star  |  [Stars](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Stars.tsx) |
| inactiveStarContainer | Inactive star container  |  [Stars](https://github.com/vtex-apps/bazaarvoice/blob/master/react/components/Stars.tsx) |

## Troubleshooting

You can check if others are experiencing similar issues [here](https://github.com/vtex-apps/bazaarvoice/issues). Also, feel free to [open issues](https://github.com/vtex-apps/bazaarvoice/issues/new) or contribute with a pull request.

## Contributing

Take a look at these guidelines: [how to contribute](https://github.com/vtex-apps/awesome-io#contributing).

## Tests

To execute our tests go to `react/` folder and run `yarn test`

### Travis CI

[![Build Status](https://travis-ci.org/vtex-apps/menu.svg?branch=master)](https://travis-ci.org/vtex-apps/menu)