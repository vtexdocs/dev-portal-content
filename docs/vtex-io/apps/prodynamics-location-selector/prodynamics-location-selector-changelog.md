---
title: "Changelog"
slug: "prodynamics-location-selector-changelog"
excerpt: "prodynamics.location-selector@0.7.42"
hidden: true
createdAt: "2022-08-04T15:40:17.021Z"
updatedAt: "2022-08-04T16:35:40.204Z"
---
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [0.7.0] - 2022-02-07
### Added
- Add a MAX_SELLERS to filter the nearest sellers to a given position
### Changed
- Create a new session in every ni location or on reset seller selection

## [0.6.0] - 2022-02-07
### Added
- Add the `allSellers` object to location state

## [0.5.0] - 2022-02-07
### Fixed
- Fix bug on user address creation
- Refactor reducer types, moved to constants and types modules

## [0.4.0] - 2022-02-03
### Changed
- Refactor the `node/` middleware from **REST** to **GraphQL**
- Refactor the `react/` app from **fetch** to **apollo client**

### Fixed
- Read the `vtex_segment` from the location wrapper and cleans local data on `null`
- Remove self reference in `package.json`

### Added
- Add a query to get sellers info by ID

## [0.3.2] - 2022-01-28
### Fixed
- Fetch optional address data when user selects a saved location
- Re-order imports
- Error handling for fetch requests on a `useEffect`

## [0.3.1] - 2022-01-17
### Fixed
- Update styles for Google Places input
- Update the modal on close function

## [0.3.0] - 2022-01-07
### Fixed
- Update the modal styles
- Move from Modal.v1 to Modal.v2 from `vtex.styleguide`
### Added
- Add a new `post` endpoint for route `/_v/location/seller` to reset the selected seller
- Add the API request in the clear seller button component

## [0.2.0] - 2022-01-04
### Changed
- Move from `sessionStorage` to `localStorage` for the context stored values
- Rename constants 

### Fixed
- Remove unused dependencies
- Remove hard code Api Key for Google Maps

### Added
- Add a `sessionStorage` flag to control the login flow on reload the page
- Add integration with Google Maps to: 
  1. Move the marker in user location modal
  2. Fit the zoom on marker select on seller modal
  3. Dynamic zoom on input fill in user location modal (new address form)

## [0.1.0] - 2021-11-29
Improve the `node` middleware and fix the `react` component according to that
### Added
- New session client in the node middleware to update the session
- Add more function helpers and constants to manage the session

### Fixed
- Remove the `document.cookie` set method in the client now the middleware returns a `set-cookie` header
- Create two methods in session extended client:
  1. create the session with a `vtex_session` cookie
  2. fetch for sellers given a geolocation point (latitude and longitude)

## [0.0.7] - 2021-11-05
### Changed
- Update the schema used in Master Data queries
- Modify the way to iterate and fetch seller info in the middleware

### Fixed
- Update the Google Maps api key
- Update the component to handle errors on fetch sellers
- Fix the Google Places autocomplete input change

## [0.0.6] - 2021-10-01
### Fixed
- Remove unused dependencies
- Fixing the exported hook

## [0.0.4] - 2021-10-01
### Added
Exports the hook `useLocationModal` for integration in other apps
Add the documentation of the hook

### Fixed
Updating dependencies in both apps (`node` and `react`)

## [0.0.2] - 2021-09-23
### Fixed
- Add the country field to user saved address
- Allow edit email when order form had saved data
- Reset the seller state when chose new address

## [0.0.1] - 2021-09-22
### Added
-   Add all `location-selector` components to Apps.