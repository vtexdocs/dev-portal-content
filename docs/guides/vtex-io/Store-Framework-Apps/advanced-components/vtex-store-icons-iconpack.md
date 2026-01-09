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

The following prefixes help in understanding the meaning of a specific icon.

| Prefix | Meaning |
| ------ | ------- |
|  bnd   | Brand                  |
|  hpa   | High Priority Actions  |
|  mpa   | Middle Priority Actions |
|  sti   | Status Indicator       |
|  inf   | Informative            |
|   nav  | Navigation             |

### SVG Fragments

| Icon                                    | ID                         |
| --------------------------------------- | -------------------------- |
| ![bnd-logo](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/bnd-logo.svg)  | bnd-logo |
| ![mpa-expand](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-expand.svg)  | mpa-expand |
| ![hpa-arrow-back](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/hpa-arrow-back.svg)  | hpa-arrow-back |
| ![hpa-arrow-from-bottom](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/hpa-arrow-from-bottom.svg)  | hpa-arrow-from-bottom |
| ![hpa-arrow-to-bottom](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/hpa-arrow-to-bottom.svg)  | hpa-arrow-to-bottom |
| ![hpa-calendar](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/hpa-calendar.svg)  | hpa-calendar |
| ![hpa-cart](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/hpa-cart.svg)  | hpa-cart |
| ![hpa-delete](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/hpa-delete.svg)  | hpa-delete |
| ![hpa-hamburguer-menu](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/hpa-hamburguer-menu.svg)  | hpa-hamburguer-menu |
| ![hpa-location-marker](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/hpa-location-marker.svg)  | hpa-location-marker |
| ![hpa-play](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/hpa-play.svg)  | hpa-play |
| ![hpa-profile](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/hpa-profile.svg)  | hpa-profile |
| ![hpa-save](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/hpa-save.svg)  | hpa-save |
| ![hpa-search](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/hpa-search.svg)  | hpa-search |
| ![hpa-telemarketing](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/hpa-telemarketing.svg)  | hpa-telemarketing |
| ![info-help-filled](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/inf-help--filled.svg)  | inf-help--filled |
| ![info-help-outline](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/inf-help--outline.svg)  | inf-help--outline |
| ![inf-star](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/inf-star.svg)  | inf-star |
| ![inf-tooltip--filled](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/inf-tooltip--filled.svg)  | inf-tooltip--filled |
| ![inf-tooltip--outline](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/inf-tooltip--outline.svg)  | inf-tooltip--outline |
| ![inf-warning--filled](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/inf-warning--filled.svg)  | inf-warning--filled |
| ![inf-warning--outline](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/inf-warning--outline.svg)  | inf-warning--outline |
| ![mpa-angle-down](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-angle--down.svg)  | mpa-angle--down |
| ![mpa-angle--up](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-angle--up.svg)  | mpa-angle--up |
| ![mpa-arrows](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-arrows.svg)  | mpa-arrows |
| ![mpa-bag](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-bag.svg)  | mpa-bag |
| ![mpa-bars](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-bars.svg)  | mpa-bars |
| ![mpa-bookmark--filled](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-bookmark--filled.svg)  | mpa-bookmark--filled |
| ![mpa-bookmark--outline](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-bookmark--outline.svg)  | mpa-bookmark--outline |
| ![mpa-clone-filles](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-clone--filled.svg)  | mpa-clone--filled |
| ![mpa-clone--outline](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-clone--outline.svg)  | mpa-clone--outline |
| ![mpa-cog](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-cog.svg)  | mpa-cog |
| ![mpa-columns](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-columns.svg)  | mpa-columns |
| ![mpa-credit-card](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-credit-card.svg)  | mpa-credit-card |
| ![mpa-edit--filled](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-edit--filled.svg)  | mpa-edit--filled |
| ![mpa-edit--outline](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-edit--outline.svg)  | mpa-edit--outline |
| ![mpa elypsis](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-elypsis.svg)  | mpa-elypsis |
| ![mpa-exchange](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-exchange.svg)  | mpa-exchange |
| ![mpa-export](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-export.svg)  | mpa-export |
| ![mpa-external-link](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-external-link--line.svg)  | mpa-external-link--line |
| ![mpa-external-link-outline](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-external-link--outline.svg) |mpa-external-link--outline |
| ![eyesight--filled--off](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-eyesight--filled--off.svg)  | mpa-eyesight--filled--off |
| ![eyesight--filled--on](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-eyesight--filled--on.svg)  | mpa-eyesight--filled--on |
| ![eyesight--outline--off](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-eyesight--outline--off.svg) |mpa-eyesight--outline--off |
| ![eyesight--outline--on](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-eyesight--outline--on.svg)  | mpa-eyesight--outline--on |
| ![mpa-filter--filled](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-filter--filled.svg)  | mpa-filter--filled |
| ![filter--outline](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-filter--outline.svg)  | mpa-filter--outline |
| ![filter-settings](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-filter-settings.svg)  | mpa-filter-settings |
| ![gallery](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-gallery.svg)  | mpa-gallery |
| ![globe](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-globe.svg)  | mpa-globe |
| ![heart](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-heart.svg)  | mpa-heart |
| ![link](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-link.svg)  | mpa-link |
| ![list-items](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-list-items.svg)  | mpa-list-items |
| ![location-input](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-location-input.svg)  | mpa-location-input |
| ![minus--filled](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-minus--filled.svg)  | mpa-minus--filled |
| ![minus--line](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-minus--line.svg)  | mpa-minus--line |
| ![minus--outline](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-minus--outline.svg)  | mpa-minus--outline |
| ![plus--filled](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-plus--filled.svg)  | mpa-plus--filled |
| ![plus--line](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-plus--line.svg)  | mpa-plus--line |
| ![plus--outline](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-plus--outline.svg)  | mpa-plus--outline |
| ![remove](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-remove.svg)  | mpa-remove |
| ![settings](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-settings.svg)  | mpa-settings |
| ![single-item](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-single-item.svg)  | mpa-single-item |
| ![store](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-store.svg)  | mpa-store |
| ![swap](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/mpa-swap.svg)  | mpa-swap |
| ![arrow--left](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/nav-arrow--left.svg)  | nav-arrow--left |
| ![arrow-right](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/nav-arrow--right.svg)  | nav-arrow--right |
| ![nav-caret--down](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/nav-caret--down.svg)  | nav-caret--down |
| ![nav-caret--left](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/nav-caret--left.svg)  | nav-caret--left |
| ![nav-caret--right](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/nav-caret--right.svg)  | nav-caret--right |
| ![nav-caret--up](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/nav-caret--up.svg)  | nav-caret--up |
| ![nav-home](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/nav-home.svg)  | nav-home |
| ![nav-minus](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/nav-minus.svg)  | nav-minus |
| ![nav-plus](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/nav-plus.svg)  | nav-plus |
| ![nav-thin-caret--left](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/nav-thin-caret--left.svg)  | nav-thin-caret--left |
| ![nav-thin-caret--right](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/nav-thin-caret--right.svg)  | nav-thin-caret--right |
| ![check--filled](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/sti-check--filled.svg)  | sti-check--filled |
| ![check--line](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/sti-check--line.svg)  | sti-check--line |
| ![sti-check--outline](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/sti-check--outline.svg)  | sti-check--outline |
| ![sti-clock](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/sti-clock.svg)  | sti-clock |
| ![close--filled](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/sti-close--filled.svg)  | sti-close--filled |
| ![close--line](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/sti-close--line.svg)  | sti-close--line |
| ![close--outline](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/sti-close--outline.svg)  | sti-close--outline |
| ![sti-discount](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/sti-discount.svg)  | sti-discount |
| ![sti-equals](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/sti-equals.svg)  | sti-equals |
| ![sti-loading](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/sti-loading.svg)  | sti-loading |
