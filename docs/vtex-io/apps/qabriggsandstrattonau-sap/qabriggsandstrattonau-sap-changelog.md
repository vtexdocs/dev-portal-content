---
title: "Changelog"
slug: "qabriggsandstrattonau-sap-changelog"
excerpt: "qabriggsandstrattonau.sap@0.30.6"
hidden: true
createdAt: "2022-07-27T19:14:58.708Z"
updatedAt: "2022-08-09T17:36:51.563Z"
---
[site]: https://briggsandstratton.myvtex.com/
## [0.30.5] - 2022-07-12
### Added
- added manifest.json policies for individual sites.  Need this because order create hook always runs in briggsandstrattonqa/briggsandstratton account
but needs to call master data API for other sites.
- integrated bug fixes and route changes from previous versions with QA branch

## [0.30.4] - 2022-04-21
### Added
- added policies for all sites

## [0.30.2] - 2022-05-10
### Changed
 - Removed line of code that reset index to undefined when removing superseded items

## [0.30.1] - 2022-05-09
### Changed
 - Changed calls generated to order create service for tax/shipping calls and creating orders.  Code now uses configuration parameter to read sender value.  Done so ferris can use FRSP instead of ARITPP when creating orders

## [0.30.0] - 2022-04-27
### Changed
- Changed routes that require session data to have /_v/private prefix per VTEX team's advice.  need this to use session data

## [0.29.5] - 2022-04-21
### Changed
- Updated endpoints that require user data to use session cookie instead of storeUserAuthToken per VTEX team's advice.  workaround for issues with empty storeUserAuthToken

## [0.29.4] - 2022-04-21
### Changed
- Updated handling of superseeded items, individual failures no longer kill whole batch
- Adding all superseeded items in one request instead of individual add to cart calls

## [0.29.3] - 2022-04-18
### Fixed
- Superseded items no longer get processed if item quantity is set to 0
### Changed
- Updated logging in tax-shipping endpoint

## [0.29.2] - 2022-04-11
### Added 
 - Added and updated logging strategy on many endpoints
### Changed
 - Increased ttl and timeout settings

## [0.29.1] - 2022-03-31
### Fixed 
 - SAP order number display for ferris and snapper pro storefronts

## [0.29.0] - 2022-03-28
### Added
 - Changed logging messages
 - New endpoint to get SAP order number from VTEX order number

## [0.28.1] - 2022-03-16
### Added
 - Added logging to tax and shipping calls for troubleshooting purposes

## [0.28.0] - 2022-03-08
### Added
 - Added SAP inventory data to response of sync cart call so client-side code can reference if needed

## [0.27.5] - 2022-02-28
### Fixed
 - issue of Getting all user addresses for deleting
 - sending each  address call at a time to avoid 429 error
## [0.27.4] - 2022-02-24
### Fixed
 - Ferris and snapper pro orders not being submitted to SAP properly with accounts that didn't exist in EU storefront
 - Changed code to query proper master data endpoint based on where order was submitted

## [0.27.3] - 2022-02-24
### Changed
 - Modified timeout of sap client

## [0.27.2] - 2022-02-24
### Fixed
 - Redo fix for order duplication issue, orders were being continuously submitted to SAP
 - Fix issue with SAP number not being written to master data
 - Change call to master data to put instead of post which was causing error

## [0.27.2-beta.0] - 2022-02-24
### Fixed
 - Bypass all SAP order submission to prevent endless order looping

## [0.27.1] - 2022-02-24
### Fixed 
 - throwing error if there is err field in sap response

## [0.27.0] - 2022-02-23
### Added 
 - Retry for SAP order create call
### Changed
 - Error handling to retry only if SAP order create is failed
### Removed 
 - unused code 
 - Duplicated order status update function


## [0.26.0] - 2022-02-22
### Removed
- Vtex order id from SAP order create payload
### Fixed
- removing items from cart when getting 500 error from sap.
## [0.25.0] - 2022-02-21
### Added
- Added code to log payload and response for all SAP requests

## [0.24.0] - 2022-02-17
### Added
- sending vtexorderid to sap

## [0.23.0] - 2022-02-14
### Added
- Added PO Number hide and show on entering value feature.

## [0.22.0] - 2022-02-14
### Added
- added field for getting ponumber to send it to SAP order creation call
### Changed
- Modified production URLs.
### Fixed
- Fixed deliverytype value properly.
- Hided the “free” text to the right of the shipping method.

## [0.21.1] - 2022-02-10
### Fixed
- URL switching based on settings
## [0.21.0] - 2022-02-10
### Changed
- strategy for getting product weight on checkout page.
### Fixed
- validating user from orderform instead of using storeuserauthtoken

## [0.20.0] - 2022-02-07
### Added
- Showing login popup whenever tax call returns 401 status.
### Fixed
- Item Removed Popup issue: Instead of isquantitychanged used removeditem field.
- Fixed weights flash off and on in cart page.

## [0.19.0] - 2022-02-03
### Changed
- displayed contact info as dealerid,accountid,and name instead of phone and firstname
- added logic for update userdetails everytime
- added logic to show minimum order qty message in frontend
### Fixed
- Fixed Shipping options for items over 25kg.

## [0.18.0] - 2022-01-31
### Fixes
 - Fixed tax issue by updating the deliveryType in checkout.js
 - Fixed breaking Shipping panel.
 - Fixed paymentData not loading.
 - Fixed Tax Error dialog.s

## [0.17.2] - 2022-01-27
### Fixed
 - Increased TTL to 60 to make sure app doesn't sleep if there is no request received
## [0.17.1] - 2022-01-27
### Changed
 - Shipping method values while creating order in SAP
 - Update shipping methods with correct names - checkout.js
 - The checkout page will make an call to the product specification endpoint to get the product weight.

### Fixed
 - ship options hiding issue in checkout.js

## [0.17.0] - 2022-01-27
### Depricated

## [0.15.0] - 2022-01-19
### Added
 - Inventory validation was mistakenly deleted. Now its available
### Changed
 - Send removed items as response to cart sync
### Fixes
 - Fixied order log - URL was wrong
## [0.14.3] - 2022-01-13
### Fixes
 - Fixied order log - URL was wrong
## [0.14.2] - 2022-01-13
### Fixes
 - Fixied order log
## [0.14.1] - 2022-01-13
### Fixes
- Make Order create status change and log non-blocking
- Make sure item is getting relved only when SAP fails
- Pass the index when removing item
## [0.14.0] - 2022-01-13
### Added
- New SAP create order approach
- Delete products if SAP call fails
## [0.13.0] - 2022-01-13
### Changed
- SuperSeeding & Fixing min qty logic
## [0.12.0] - 2022-01-10
### Added
- SAP user data service for frontend
## [0.11.2] - 2022-01-06
### Fixed
- Update the orders with admin creds
## [0.11.1] - 2022-01-03
### Fixed
- Use unit multiplier for item price & tax
## [0.11.0] - 2022-01-03
### Changed
- Used partOrg to compensate supersets
- Consider min order quantity while adding product
## [0.10.1] - 2021-12-30
### Fixed
- Formating order line item xml in parser
## [0.10.0] - 2021-12-30
### Added
- SAP create order
- Log the sap number in order notes
- Event handler for order create
## [0.9.0] - 2021-12-30
### Added
- SAP order simulate for getting tax & shipping
- Cart client for adding tax & shipping items to cart
- SAP config in admin
- get tax & shipping service call
- Checkout.js implementation to update the shipping & tax

## [0.8.0] - 2021-12-29
### Changed
- Return changed order form data in sync cart call
## [0.7.0] - 2021-12-29
### Fixed
- Proxy issues
## [0.5.0] - 2021-12-28
### Added
- Cart sync api call from cart page based on client side events
- Update shipping address based on address available in master data
### Fixed
- Accept the customer sync api with id
## [0.4.0] - 2021-12-22
### Added
- Added cart item sync on checkout page
## [0.3.2] - 2021-12-20
- Handling SAP error
## [0.3.1] - 2021-12-20
- Added logs for debuging
## [0.3.0] - 2021-12-20
- Created new client for cart updates
  - This will use store user's token to update their order
- Added sync-cart service
- New typings for inventory & order form
- Get order form
  - Get user data based on the order email
  - Get sap data for given items or all order items
  - send sap & ordr form to next midleware
- Update order form
  - Map SAP data with order form data
  - Set qty to 0 if reuested qty is greater than SAP
  - Send update order form item with sap price
  - Return price changed & qty changed flag as response
## [0.2.0] - 2021-11-14
### Added
- Initial Implementations
- XML parsing
- SAP clients