---
title: "Icon Pack list"
slug: "vtex-store-icons-iconpack"
hidden: false
createdAt: "2020-09-23T16:25:14.423Z"
updatedAt: "2023-09-29T18:52:00.091Z"
---

Check out the available icons to use in your store described in [Store Icon](https://developers.vtex.com/docs/apps/vtex.store-icons) guide.

## Usage

Add the `vtex.store-icons` to your dependencies in `manifest.json`.

This is an example on how to use it:

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

The following prefixes help to understand what a specific icon means.

| Prefix | Meaning |
| ------ | ------- |
|  bnd   | Brand                  |
|  hpa   | High Priority Actions  |
|  mpa   | Midle Priority Actions |
|  sti   | Status Indicator       |
|  inf   | Informative            |
|   nav  | Navigation             |

### SVG Fragments

| Icon                                    | ID                         |
| --------------------------------------- | -------------------------- |
| ![bnd-logo](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/bnd-logo.svg)  | bnd-logo |
| ![mpa-expand](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-expand.svg)  | mpa-expand |
| ![hpa-arrow-back](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/hpa-arrow-back.svg)  | hpa-arrow-back |
| ![hpa-arrow-from-bottom](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/hpa-arrow-from-bottom.svg)  | hpa-arrow-from-bottom |
| ![hpa-arrow-to-bottom](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/hpa-arrow-to-bottom.svg)  | hpa-arrow-to-bottom |
| ![hpa-calendar](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/hpa-calendar.svg)  | hpa-calendar |
| ![hpa-cart](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/hpa-cart.svg)  | hpa-cart |
| ![hpa-delete](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/hpa-delete.svg)  | hpa-delete |
| ![hpa-hamburguer-menu](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/hpa-hamburguer-menu.svg)  | hpa-hamburguer-menu |
| ![hpa-location-marker](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/hpa-location-marker.svg)  | hpa-location-marker |
| ![hpa-play](https://github.com/vtex-apps/store-icons/blob/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/hpa-play.svg)  | hpa-play |
| ![hpa-profile](https://github.com/vtex-apps/store-icons/blob/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/hpa-profile.svg)  | hpa-profile |
| ![hpa-save](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/hpa-save.svg)  | hpa-save |
| ![hpa-search](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/hpa-search.svg)  | hpa-search |
| ![hpa-telemarketing](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/hpa-telemarketing.svg)  | hpa-telemarketing |
| ![info-help-filled](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/inf-help--filled.svg)  | inf-help--filled |
| ![info-help-outline](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/inf-help--outline.svg)  | inf-help--outline |
| ![inf-star](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/inf-star.svg)  | inf-star |
| ![inf-tooltip--filled](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/inf-tooltip--filled.svg)  | inf-tooltip--filled |
| ![inf-tooltip--outline](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/inf-tooltip--outline.svg)  | inf-tooltip--outline |
| ![inf-warning--filled](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/inf-warning--filled.svg)  | inf-warning--filled |
| ![inf-warning--outline](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/inf-warning--outline.svg)  | inf-warning--outline |
| ![mpa-angle-down](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-angle--down.svg)  | mpa-angle--down |
| ![mpa-angle--up](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-angle--up.svg)  | mpa-angle--up |
| ![mpa-arrows](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-arrows.svg)  | mpa-arrows |
| ![mpa-bag](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-bag.svg)  | mpa-bag |
| ![mpa-bars](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-bars.svg)  | mpa-bars |
| ![mpa-bookmark--filled](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-bookmark--filled.svg)  | mpa-bookmark--filled |
| ![mpa-bookmark--outline](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-bookmark--outline.svg)  | mpa-bookmark--outline |
| ![mpa-clone-filles](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-clone--filled.svg)  | mpa-clone--filled |
| ![mpa-clone--outline](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-clone--outline.svg)  | mpa-clone--outline |
| ![mpa-cog](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-cog.svg)  | mpa-cog |
| ![mpa-columns](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-columns.svg)  | mpa-columns |
| ![mpa-credit-card](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-credit-card.svg)  | mpa-credit-card |
| ![mpa-edit--filled](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-edit--filled.svg)  | mpa-edit--filled |
| ![mpa-edit--outline](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-edit--outline.svg)  | mpa-edit--outline |
| ![mpa elypsis](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-elypsis.svg)  | mpa-elypsis |
| ![mpa-exchange](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-exchange.svg)  | mpa-exchange |
| ![mpa-export](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-export.svg)  | mpa-export |
| ![mpa-external-link](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-external-link--line.svg)  | mpa-external-link--line |
| ![mpa-external-link-outline](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-external-link--outline.svg)  | mpa-external-link--outline |
| ![eyesight--filled--off](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-eyesight--filled--off.svg)  | mpa-eyesight--filled--off |
| ![eyesight--filled--on](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-eyesight--filled--on.svg)  | mpa-eyesight--filled--on |
| ![eyesight--outline--off](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-eyesight--outline--off.svg)  | mpa-eyesight--outline--off |
| ![eyesight--outline--on](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-eyesight--outline--on.svg)  | mpa-eyesight--outline--on |
| ![mpa-filter--filled](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-filter--filled.svg)  | mpa-filter--filled |
| ![filter--outline](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-filter--outline.svg)  | mpa-filter--outline |
| ![filter-settings](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-filter-settings.svg)  | mpa-filter-settings |
| ![gallery](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-gallery.svg)  | mpa-gallery |
| ![globe](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-globe.svg)  | mpa-globe |
| ![heart](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-heart.svg)  | mpa-heart |
| ![link](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-link.svg)  | mpa-link |
| ![list-items](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-list-items.svg)  | mpa-list-items |
| ![location-input](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-location-input.svg)  | mpa-location-input |
| ![minus--filled](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-minus--filled.svg)  | mpa-minus--filled |
| ![minus--line](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-minus--line.svg)  | mpa-minus--line |
| ![minus--outline](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-minus--outline.svg)  | mpa-minus--outline |
| ![plus--filled](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-plus--filled.svg)  | mpa-plus--filled |
| ![plus--line](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-plus--line.svg)  | mpa-plus--line |
| ![plus--outline](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-plus--outline.svg)  | mpa-plus--outline |
| ![remove](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-remove.svg)  | mpa-remove |
| ![settings](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-settings.svg)  | mpa-settings |
| ![single-item](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-single-item.svg)  | mpa-single-item |
| ![store](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-store.svg)  | mpa-store |
| ![swap](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/mpa-swap.svg)  | mpa-swap |
| ![arrow--left](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/nav-arrow--left.svg)  | nav-arrow--left |
| ![arrow-right](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/nav-arrow--right.svg)  | nav-arrow--right |
| ![nav-caret--down](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/nav-caret--down.svg)  | nav-caret--down |
| ![nav-caret--left](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/nav-caret--left.svg)  | nav-caret--left |
| ![nav-caret--right](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/nav-caret--right.svg)  | nav-caret--right |
| ![nav-caret--up](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/nav-caret--up.svg)  | nav-caret--up |
| ![nav-home](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/nav-home.svg)  | nav-home |
| ![nav-minus](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/nav-minus.svg)  | nav-minus |
| ![nav-plus](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/nav-plus.svg)  | nav-plus |
| ![nav-thin-caret--left](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/nav-thin-caret--left.svg)  | nav-thin-caret--left |
| ![nav-thin-caret--right](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/nav-thin-caret--right.svg)  | nav-thin-caret--right |
| ![check--filled](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/sti-check--filled.svg)  | sti-check--filled |
| ![check--line](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/sti-check--line.svg)  | sti-check--line |
| ![sti-check--outline](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/sti-check--outline.svg)  | sti-check--outline |
| ![sti-clock](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/sti-clock.svg)  | sti-clock |
| ![close--filled](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/sti-close--filled.svg)  | sti-close--filled |
| ![close--line](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/sti-close--line.svg)  | sti-close--line |
| ![close--outline](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/sti-close--outline.svg)  | sti-close--outline |
| ![sti-discount](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/sti-discount.svg)  | sti-discount |
| ![sti-equals](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/sti-equals.svg)  | sti-equals |
| ![sti-loading](https://raw.githubusercontent.com/vtex-apps/store-icons/bb60df29809a4edbc13b3e0febd6a3d9eb996ab4/docs/sti-loading.svg)  | sti-loading |
