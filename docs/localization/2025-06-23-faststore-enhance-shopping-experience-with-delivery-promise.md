---
title: "FastStore: Enhance shopping experience with Delivery Promise"
slug: "2025-06-23-faststore-enhance-shopping-experience-with-delivery-promise"
type: added
excerpt: " Delivery Promise is now available for FastStore."
createdAt: ""
updatedAt: ""
hidden: false
---

Delivery Promise is now available in FastStore, enabling stores to present only products that can be delivered to a shopper’s address or picked up at nearby locations.

## What has changed?

Previously, shoppers could encounter scenarios where the storefront displayed products that appeared available but could not be delivered to their address. This led to friction and frustration at checkout when they discovered certain items in their cart were undeliverable, resulting in abandoned purchases and negative experiences.

Now, Delivery Promise addresses these issues by offering a centralized, automated, and real-time system that provides delivery estimations for available products based on the shopper’s location.

## What is new?

**Delivery Promise** introduces the following by default:

- **`RegionPopover` component:** Allows users to enter or update their location. It’s used when location data is missing or when a store’s default postal code applies. Available in [`@faststore/core`](https://developers.vtex.com/docs/guides/faststore/project-structure-overview#packagejson), `RegionPopover` uses the [`Popover`](https://developers.vtex.com/docs/guides/faststore/molecules-popover) component as its UI base.

- **Hooks:**
  - `useRegion`: Access or update the user’s region information, such as postal code or location
  - `useRegionModal`: Handle modal display logic for region selection, especially when the input of location is mandatory.
  - `useGeoLocation`: Interact with the browser’s geolocation API or related client-side mechanisms to auto-detect the user’s location.

- **APIs:**
  - `productCount`: Provides the total number of products based on location.
  - `pickupPoints`: Enables querying and returning a list of pickup points based on location.
  - `validateSession`: Updates the shopper’s session with their current location whenever it changes, ensuring Delivery Promise displays accurate product availability and delivery estimates. This information is saved in the session (and `vtex_session` cookie) and used by other VTEX services like Checkout and Intelligent Search to offer suitable delivery options.

## Why did we make this change?

**Delivery Promise** enhances the overall shopping experience by providing:

- **Location-based product availability:** Product availability dynamically filtered by shopper location.
- **Flexible shopper location detection:** Automatic location capture, fallback to saved addresses, or use of a default postal code for logged-in and guest shoppers.
- **Real-time search integration:** Integrated with [Intelligent Search](https://help.vtex.com/tracks/vtex-intelligent-search) to synchronize search results, product listings, filters, and tags in real time, showing only relevant products.

## What needs to be done?

To enable Delivery Promise in your FastStore project, go to the `discovery.config.js` file and, under the `deliveryPromise` section, set the `enable` object to `true`.

For detailed instructions, see the [Delivery Promise](LINK) guide.
