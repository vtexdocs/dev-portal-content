---
title: "Sessions System Overview"
slug: "sessions-system-overview"
hidden: false
createdAt: "2022-09-20T20:22:27.378Z"
updatedAt: "2022-09-20T20:22:27.378Z"
---

VTEX’s Sessions System is an architecture that allows stores to handle complex B2B scenarios, regionalize customer experience and perform promotion segmentation by Campaign Audiences.

## How it works

The Sessions System operates using two cookies: `vtex_session` and `vtex_segment`. Learn how they work in the following sections.

### `vtex_session` cookie

Through the `vtex_session` cookie, the Sessions System identifies the information of a specific session of a user browsing in your store.

It is possible to see session properties by making a request to `GET` `https://{{accountname}}.{{environment}}.com.br/api/sessions?items={{namespace}}.{{value}},{{namespace}}.{{value2}}`.

The API returns several **namespaces**, which are the keys that group together certain types of information about the session.

Below, see a response example with basic data on a session:

```json
{
  "id": "840f8910-eb3b-4f25-8d51-a06445317906",
  "namespaces": {
    "account": {
      "id": {
        "value": "0e914df8-c516-45bc-a45a-0aab6482eaf7",
        "keepAlive": true
      },
      "accountName": {
        "value": "qamarketplace"
      }
    },
    "store": {
      "channel": {
        "value": "1"
      }
    },
    "impersonate": {
      "canImpersonate": {
        "value": "false"
      }
    },
    "profile": {
      "isAuthenticated": {
        "value": "false"
      }
    }
  },
  "version": 1,
  "active": true,
  "debug": false
}
```

Below you will find a list of possible namespaces that can be returned by the API:

- `account`: Namespace with account information where the session is happening.
- `checkout`: Namespace with information related to checkout, such as session cart ID (`cartId`) and region (`regionId`) that the checkout returns to identify the geographic location of the user browsing this session.
- `store`: Namespace with information about the current sales channel of the session.
- `cookie`: Namespace with information on the authentication cookies of the user.
- `impersonate`: Namespace that identifies if the logged in user has permission to impersonate another user and browse on that user’s behalf.
- `profile`: Namespace with information related to the customer’s profile logged into that session. Eligible price tables for that customer are listed in this namespace.
- `public`: Namespace with general information on a session, `utm_campaign`, `utm_source` and `utmi_campaign`. In this namespace, we also find `postalCode` or `geoCoordinates` and `country`, which are given to VTEX’s checkout so that it can return the `regionId`, require in the namespace `checkout`. These values follow the format defined in the [Checkout API reference](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/regions/-regionId-).
- `authentication`: Namespace with user authentication data in the context of the session.
- `rnb`: Namespace that gives information related to applicable Campaign Audiences and promotions for that session.

### `vtex_segment` cookie

The Sessions System also creates the `vtex_segment` cookie, which contains the information of the commercial conditions to be applied to a session.

It is possible to see the properties of a segment by making a `GET` request to `https://{{accountName}}.{{environment}}.com.br/api/segments/{{segmentToken}}`.

Below you will find a response example with data from a segment:

```json
{
  "campaigns": "vip",
  "channel": "1",
  "priceTables": "gold",
  "regionId": "U1cj",
  "utm_campaign": "black friday",
  "utm_source": "google",
  "utmi_campaign": "banner"
}
```

>ℹ️ The session identified by the `vtex_session` cookie is individual. However, the `vtex_segment`cookie uses information that can be shared among different users. For example: the same price table can be available to different users in distinct sessions. This way, `vtex_segment` is used to control the cache key of the pages.

## Changing information from a session

It is possible to change a session’s information by making a `POST` request to the following route:

`https://{{account-name}}.{{environment}}.com.br/api/sessions/{{session_token}}`

Below you can see an example of a request body used to update the information of a session:

```json
{
  "public": {
    "utm_campaign": {
      "value": "Black Friday"
    },
    "country": {
      "value": "USA"
    },
    "postalCode": {
      "value": "05408000"
    }
  }
}
```

## Main features related to the Sessions System

### Price tables

Price tables are identified by the sessions system in the namespace `profile`. Each price table displays customized prices for that identified user that is browsing in the store. You can create price tables for specific customer groups. Price tables can by used to handle B2B scenarios.

Learn more about [Configuring price tables for specific users](https://help.vtex.com/en/tutorial/setting-up-price-tables-for-specific-users--5S9oDOMHNmY4K0kAewAiWY).

### Region

The Region feature is identified by the sessions system in the namespace `checkout`, with the `regionId` property, which is generated when a `postalCode` or `geoCoordinates` and a `country` are added to a session. The feature's goal is to regionalize the experience of the user in the store.

It allows, for example, sellers to configure their own prices and marketplaces to be displayed according to the customer's region.

To configure price and availability according to the customer’s region, access our article about [setting up SKU price and availability by Region](https://help.vtex.com/en/tutorial/setting-up-price-and-availability-of-skus-by-region--12ne58BmvYsYuGsimmugoc).

### Campaign audiences

Campaign Audiences are clustering rules that allow promotions to be applied to customers that meet a set of criteria.

The campaign audiences feature works much like price tables. In the **Promotions & Taxes** module, you can create conditions that apply a promotion to a particular customer if campaign conditions are met.

Learn more about [Campaign Audiences](https://help.vtex.com/en/tutorial/campaign-audiences--3o7lhpNseXY2WmjZO0gQ6m).
