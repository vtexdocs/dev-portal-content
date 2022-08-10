---
title: "Changelog"
slug: "qabriggsandstrattonsnapperpro-components-changelog"
excerpt: "qabriggsandstrattonsnapperpro.components@0.15.6"
hidden: true
createdAt: "2022-07-27T18:15:58.873Z"
updatedAt: "2022-07-27T19:32:56.294Z"
---
[site]: https://briggsandstratton.myvtex.com/
## [0.15.6] - 2022-07-27
## Changed
- Changed path to inventory service in sapproductcontext.tsx

## [0.15.5] - 2022-07-12
## Added
- Integrated previous version changes to QA branch version

## [0.15.4] - 2022-06-29
## Fixed
- show price as TBD if product is unavailable

## [0.15.3] - 2022-06-28
## Fixed
- stock component loading issue

## [0.15.2] - deprecated
## Added
- created pair product component

## [0.15.1] - 2022-06-02
## changed
- disabled unavailable add to cart button

## [0.15.0] - 2022-06-02 
## Added
- created sap-prices,sap-stocks and custom addtocart blocks

## [0.14.2] - 2022-04-27
### Changed
- Changed route to sync cart endpoint to include /_v/private prefix

## [0.14.1] - 2022-03-08
### Fixed
- Fixed currency bug by setting culture.currency based on order form returned by SAP integration

## [0.14.0] - 2022-03-08
### Added
- Added code in ValidateCart to write erp data to cache after validating cart

## [0.13.0][site] - 2022-02-23
### Added
- Added static messages in messages folder

## [0.12.0-beta.0][site] - 2022-02-03
### Added
- showing addtocart message to user if sap call status is 200
- showing minordqty message to use if minorderqty product is added
### Changed
- hiding message on eparts page when product is unavailable 


## [0.11.1-beta.1][site] - 2022-01-24
### Added
- created events for sap calls
### Changed
- changed message
 - Hide Add Address button on profile page.

## [0.11.0-beta.0][site] - 2022-01-24
### Depricated
## [0.10.0-beta.0][site] - 2022-01-24
### Fixed
  - Resized screen for popup
### Changed
  - alert popup message change

## [0.9.1-beta.0][site] - 2022-01-19
### Fixed
  - Set order form was after reurn. Move it to right place
## [0.9.0-beta.0][site] - 2022-01-19
### Added
  - Added error message pop up when Sync api fails and items removed
## [0.7.0-beta.0][site] - 2022-01-18
### Added
  - Show error message when Sync api fails
## [0.6.0-beta.0][site] - 2022-01-13
### Changed
  - Order Confirmation Page
## [0.5.0-beta.0][site] - 2021-12-18
### Added
  - set order data event to update the minicart price
  - block mini cart button until cart is synced
## [0.3.0-beta.0][site] - 2021-12-18
### Added
  - Calling sync api when new item is added to cart
  - Show cart vaildation loading message
## [0.2.0-beta.0][site] - 2021-12-17
### Added
  - Disabled save button after one click
  - Added loader to save button
  - Added disclaimer message on order quote page
## [0.1.0-beta.0][site] - 2021-11-30
### Added

- Added all custom blocks