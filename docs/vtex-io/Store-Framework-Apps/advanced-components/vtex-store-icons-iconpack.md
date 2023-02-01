---
title: "Icon Pack list"
slug: "vtex-store-icons-iconpack"
hidden: false
createdAt: "2020-09-23T16:25:14.423Z"
updatedAt: "2020-10-05T18:52:00.091Z"
---

This articles lists all SVG fragment identifiers.

## How to use this fragments?

First of all, you should add the `vtex.store-icons` to your dependencies in `manifest.json`.

This an example that show you how to use it.

```javascript
  import React from 'react'

  import Icon from 'vtex.store-icons'

  const IconSearch = ({ ...props }) => {
    return <Icon id="hpa-search" {...props} />
  }

  IconSearch.propTypes =  {
    /** Icon size, aspect ratio 1:1 */
    size: PropTypes.number,
    /** Icon viewBox. Default 0, 0, 16, 16 */
    viewBox: PropTypes.string,
    /** Define if will be used a active or muted className */
    isActive: PropTypes.bool,
    /** Active color class */
    activeClassName: PropTypes.string,
    /** Muted color class */
    mutedClassName: PropTypes.string,
  }
  export default IconSearch

 ```

## SVG Prefixes

We use a series of prefixes to help us understand what an specific icon means.

* bnd - Brand;
* hpa - High Priority Actions;
* mpa - Midle Priority Actions;
* sti - Status Indicator;
* inf - Informative;
* nav - Navigation

## SVG Fragments

| Icon                                    | ID                         |
| --------------------------------------- | -------------------------- |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/bnd-logo.svg)  | bnd-logo |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-expand.svg)  | mpa-expand |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/hpa-arrow-back.svg)  | hpa-arrow-back |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/hpa-arrow-from-bottom.svg)  | hpa-arrow-from-bottom |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/hpa-arrow-to-bottom.svg)  | hpa-arrow-to-bottom |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/hpa-calendar.svg)  | hpa-calendar |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/hpa-cart.svg)  | hpa-cart |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/hpa-delete.svg)  | hpa-delete |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/hpa-hamburguer-menu.svg)  | hpa-hamburguer-menu |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/hpa-location-marker.svg)  | hpa-location-marker |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/hpa-play.svg)  | hpa-play |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/hpa-profile.svg)  | hpa-profile |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/hpa-save.svg)  | hpa-save |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/hpa-search.svg)  | hpa-search |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/hpa-telemarketing.svg)  | hpa-telemarketing |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/inf-help--filled.svg)  | inf-help--filled |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/inf-help--outline.svg)  | inf-help--outline |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/inf-star.svg)  | inf-star |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/inf-tooltip--filled.svg)  | inf-tooltip--filled |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/inf-tooltip--outline.svg)  | inf-tooltip--outline |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/inf-warning--filled.svg)  | inf-warning--filled |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/inf-warning--outline.svg)  | inf-warning--outline |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-angle--down.svg)  | mpa-angle--down |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-angle--up.svg)  | mpa-angle--up |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-arrows.svg)  | mpa-arrows |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-bag.svg)  | mpa-bag |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-bars.svg)  | mpa-bars |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-bookmark--filled.svg)  | mpa-bookmark--filled |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-bookmark--outline.svg)  | mpa-bookmark--outline |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-clone--filled.svg)  | mpa-clone--filled |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-clone--outline.svg)  | mpa-clone--outline |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-cog.svg)  | mpa-cog |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-columns.svg)  | mpa-columns |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-credit-card.svg)  | mpa-credit-card |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-edit--filled.svg)  | mpa-edit--filled |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-edit--outline.svg)  | mpa-edit--outline |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-elypsis.svg)  | mpa-elypsis |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-exchange.svg)  | mpa-exchange |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-export.svg)  | mpa-export |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-external-link--line.svg)  | mpa-external-link--line |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-external-link--outline.svg)  | mpa-external-link--outline |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-eyesight--filled--off.svg)  | mpa-eyesight--filled--off |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-eyesight--filled--on.svg)  | mpa-eyesight--filled--on |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-eyesight--outline--off.svg)  | mpa-eyesight--outline--off |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-eyesight--outline--on.svg)  | mpa-eyesight--outline--on |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-filter--filled.svg)  | mpa-filter--filled |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-filter--outline.svg)  | mpa-filter--outline |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-filter-settings.svg)  | mpa-filter-settings |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-gallery.svg)  | mpa-gallery |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-globe.svg)  | mpa-globe |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-heart.svg)  | mpa-heart |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-link.svg)  | mpa-link |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-list-items.svg)  | mpa-list-items |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-location-input.svg)  | mpa-location-input |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-minus--filled.svg)  | mpa-minus--filled |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-minus--line.svg)  | mpa-minus--line |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-minus--outline.svg)  | mpa-minus--outline |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-plus--filled.svg)  | mpa-plus--filled |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-plus--line.svg)  | mpa-plus--line |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-plus--outline.svg)  | mpa-plus--outline |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-remove.svg)  | mpa-remove |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-settings.svg)  | mpa-settings |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-single-item.svg)  | mpa-single-item |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-store.svg)  | mpa-store |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/mpa-swap.svg)  | mpa-swap |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/nav-arrow--left.svg)  | nav-arrow--left |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/nav-arrow--right.svg)  | nav-arrow--right |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/nav-caret--down.svg)  | nav-caret--down |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/nav-caret--left.svg)  | nav-caret--left |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/nav-caret--right.svg)  | nav-caret--right |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/nav-caret--up.svg)  | nav-caret--up |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/nav-home.svg)  | nav-home |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/nav-minus.svg)  | nav-minus |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/nav-plus.svg)  | nav-plus |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/nav-thin-caret--left.svg)  | nav-thin-caret--left |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/nav-thin-caret--right.svg)  | nav-thin-caret--right |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/sti-check--filled.svg)  | sti-check--filled |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/sti-check--line.svg)  | sti-check--line |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/sti-check--outline.svg)  | sti-check--outline |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/sti-clock.svg)  | sti-clock |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/sti-close--filled.svg)  | sti-close--filled |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/sti-close--line.svg)  | sti-close--line |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/sti-close--outline.svg)  | sti-close--outline |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/sti-discount.svg)  | sti-discount |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/sti-equals.svg)  | sti-equals |
| ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/sti-loading.svg)  | sti-loading |
