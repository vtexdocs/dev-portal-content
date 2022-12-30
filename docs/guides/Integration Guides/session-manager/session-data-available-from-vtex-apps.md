---
title: "Session data available from VTEX apps"
slug: "session-data-available-from-vtex-apps"
hidden: false
createdAt: "2022-08-04T21:11:03.131Z"
updatedAt: "2022-08-04T21:24:24.490Z"
---
Below you can see all data from VTEX apps that is made available in **Session Manager**

## Store (vtex.store-session)

|     |     |
| --- | --- |
| **RunOnCreate** | true |
| **Inputs**        | `public`: cultureInfo, sc, locale |
|                   | `profile`: email, isAuthenticated |
| **Outputs**       | `store`: channel, countryCode, cultureInfo, currencyCode, currencySymbol |

This app is responsible for processing the current user on the session (by email, if available) and requesting the corresponding trade policy and related information. 

It is also sensitive to the `sc` input parameter, which is interpreted as a trade policy request. In other words, if it is present, the app checks if the requested trade policy is within the active options for that user and selects it, if possible. Otherwise, the user gets a 401 status code error if he is not authenticated or 403 if he is. 

The `locale` and `cultureInfo` input parameters are used to overwrite the `cultureInfo` output parameter to ensure the session language can be set according to the user’s preference.

## Authentication (vtex.authentication-session)

|     |     |
| --- | --- |
| **RunOnCreate** | false |
| **Inputs**        | `cookie`: VtexIdclientAutCookie, VtexIdclientAutCookie_.* |
| **Outputs**       | `authentication`: adminUserId, adminUserEmail, storeUserId, storeUserEmail |

This app is our primary authentication method, taking the VTEXID cookie from the request, validating it, and extracting the user or admin IDs.

## Profile (vtex.profile-session)

|     |     |
| --- | --- |
| **RunOnCreate** | false |
| **Inputs**        | `public`: storeUserEmail |
|                   | `authentication`: storeUserId |
|                   | `impersonate`: storeUserId |
| **Outputs**       | `profile`: id, email, firstName, lastName, phone, document, priceTables, isAuthenticated |

This app ensures the user information corresponds to the data loaded into the session. 

If the input parameter `storeUserEmail` is defined in the `public` namespace, it assumes there is no authentication cookie. As such, the output parameter `isAuthenticated` is set to `false`, and only the `priceTables` output parameter is loaded. On the other hand, if the input parameter `storeUserId` is defined in the `authentication` or `impersonate` namespace, all relevant information is loaded from Master Data.

## Rates and Benefits (vtex.rnb-session)

|     |     |
| --- | --- |
| **RunOnCreate** | false |
| **Inputs**        | `profile`: email |
|                   | `public`: utm_source, utm_campaign, postalCode |
| **Outputs**       | `rnb`: campaigns |

This app integrates with our Rates and benefits system, identifying which campaigns the user is eligible for.

## Checkout (vtex.checkout-session)

|     |     |
| --- | --- |
| **RunOnCreate** | false |
| **Inputs**        | `public`: regionId, country, postalCode, geoCoordinates |
| **Outputs**       | `checkout`: regionId, cartId |

The checkout app deals with the user's purchasing experience. Currently, it looks the user’s location up (to be a valid input the location must include the country and either `postalCode` or `geoCoordinates`). The output also contains the ID of the cart used during the checkout process.

## Impersonate (vtex.impersonate-session)

|     |     |
| --- | --- |
| **RunOnCreate** | false |
| **Inputs**        | `public`: vtex-impersonated-customer-email |
|                   | `cookie`: vtex-impersonated-customer-email |
|                   | `authentication`: adminUserEmail |
| **Outputs**       | `impersonate`: storeUserId, storeUserEmail, canImpersonate, account |

The impersonate app is the only app on session’s framework that does not come as part of the default bundle and must be manually installed on each store. It enables the feature of customer impersonation, which is particularly useful for telephone centers that must make purchases on the client’s behalf. It receives the `vtex-impersonated-customer-email` parameter, either through direct `POST` or cookie, and attempts to impersonate that user using the admin credentials in the session. If such a pair has permission for impersonation, then the impersonated user’s ID and email will be loaded into the session.