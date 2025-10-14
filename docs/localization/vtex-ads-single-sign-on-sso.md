---
title: "VTEX Ads Single Sign On (SSO)"
slug: "vtex-ads-single-sign-on-sso"
excerpt: "Enable seamless user authentication across environments with VTEX Ads SSO integration."
hidden: false
createdAt: "2025-10-13T00:00:00.000Z"
updatedAt: "2025-10-13T00:00:00.000Z"
---
The purpose of Single Sign On is to allow users to switch between environments without having to log in again.

> 📘 API Authentication
> 
> <https://dash.readme.com/project/newtail-media/v1.0/refs/autenticacao>

## 1. Request redirect URL

| Attribute   | Description                                    | Type   | Required |
| :---------- | :--------------------------------------------- | :----- | :------- |
| seller_id   | Unique identifier of the advertiser/seller     | String | Yes      |
| seller_name | Name of the advertiser/seller                  | String | Yes      |
| user_email  | User email                                     | String | Yes      |
| user_name   | User name                                      | String | Yes      |

```json
curl --location --request POST 'https://api-retail-media.newtail.com.br/sso/marketplace'  
--header 'x-api-key: XXX'  
--header 'x-app-id: YYY'  
--header 'Content-Type: application/json'  
--data-raw '{  
  "seller_id": "1",
  "seller_name": "Store Example",  
  "user_email": "example@example.com.br",  
  "user_name": "User Example"  
}'
```

Response:

```json
{  
    "url_redirect": "https://app.newtail.com.br/login/marketplace?token=xxxxx"  
}
```

## 2. User redirection to the redirect URL

Once you have the redirect URL, simply redirect the user to this URL and the user will be logged into the platform without requiring any login integration.

## Login URL (user disconnection)

Optionally, we can redirect the user to a previously provided URL that will be used when the user is disconnected.
