---
title: "Sessions System Overview"
slug: "sessions-system-overview"
hidden: false
createdAt: "2022-09-20T20:22:27.378Z"
updatedAt: "2022-09-20T20:22:27.378Z"
---

VTEX’s **Sessions System** is a new architecture that allows stores to use new platform features and potentialize its use. With the installation of the new sessions system, your store will be able to handle complex **B2B** scenarios, will be able to **regionalize the experience** of your customer and perform promotions segmentations by **Campaign Audiences**.

## Functioning of the Sessions System

### Cookie vtex_session

The Sessions System identifies, through the `vtex_session` cookie, the information of a specific session of a user browsing in your store.
It is possible to see the properties of a sessions by doing a `GET` on the route `{{accountname}}.{{environment}}.com.br/api/sessions?items={{namespace}}.{{value}},{{namespace}}.{{value2}}`.

In the JSON reply, the API returns several **namespaces**. The namespaces are the keys that group together certain types of information about the session.

Below, you may see the example of reply with basic data on a session:

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
- `public`: Namespace with general information on a session, `utm_campaign`, `utm_source` and `utmi_campaign`. In this namespace, we also find information about `country` and `postalCode`, which are given to VTEX’s checkout so that it can return the `regionId`, require in the namespace `checkout`.
- `authentication`: Namespace with user authentication data in the context of the session.
- `rnb`: Namespace that gives information related to applicable Campaign Audiences and promotions for that session.

### Cookie vtex_segment

VTEX Sessions also creates the cookie `vtex_segment`. This cookie contains the information with the commercial conditions to be applied to a session.

It is possible to see the properties of a segment by doing a `GET` on the route `{{accountName}}.{{environment}}.com.br/api/segments/{{segmentToken}}`

Below you will find an example of answer with data from a segment:

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

It’s important to stress that the session identified by the cookie `vtex_session` is **individual**. However, the cookie `vtex_segment` uses information that can be **shared** among different users. For example: the same price table can be available to different users in distinct sessions. This way, `vtex_segment` is used to control the cache key of the pages.

## Changing information from a session

It is possible to change a session’s information by performing a `POST` on the following route:

`{{account-name}}.{{environment}}.com.br/api/sessions/{{session_token}}`

Below you can see an example of a `body` used to update the information of a session:

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

### Price Tables

The feature Price Table is identified by the sessions system in the namespace `profile`. The price table displays customized prices for that identified user that is browsing in the store. You can create price table for specific customer groups. The Price Tables can by used mainly to handle B2B scenarios. To configure the price tables in your store, access our documentation about [how to configure Price Tables](https://help.vtex.com/en/tutorial/setting-up-price-tables)

### Region

The region feature is identified by the sessions system in the namespace `checkout`, with the `regionId` property, which is generated when a `postalCode` and a `country` are added to a session. The feature’s objective is to regionalize the experience of the user in the store. It allows, for example, sellers to configure their own prices and marketplaces to display according to the customer’s region. To configure price and availability according to the customer’s region, access our article about [setting up SKU price and availability by Region](https://help.vtex.com/en/tutorial/%20setting-up-price-and-availability-of-skus-by-region).

### Campaign Audiences

Campaign Audiences are clustering rules that allow promotions to be applied to customers that meet the campaign rules. The Campaign Audiences feature works much like Price Tables. In the **Promotions & Taxes** module, you can create conditions that apply a promotion to a particular customer if campaign conditions are met.
