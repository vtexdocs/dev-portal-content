---
title: "Expiring a shopper's password"
slug: "expiring-a-shoppers-password"
hidden: false
createdAt: "2023-05-24T22:18:24.684Z"
updatedAt: "2023-05-24T22:18:24.684Z"
---

You can use the VTEX ID API to expire a shopper's password. This means they will not be able to login until they create a new password on your website. In this article you can learn how to do this.

To maximize security and improve the shopper experience, we recommend that you follow the steps below to expire a shopper's password:

1. [Activate repeated password prevention](#preventing-repeated-passwords) (do this only the first time)
2. [Expire shopper password](#expiring-a-password-by-email)
3. [Notify the shopper](#notifying-the-shopper)

>ℹ️ Any user or [application key](https://developers.vtex.com/docs/guides/authentication-overview) that wishes to perform password expiration must have a [License Manager role](https://help.vtex.com/pt/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) that includes the [resource](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3) `Expire User Password`.

## Preventing repeated passwords

If you intend to expire shoppers' passwords, it may be a good idea to prevent them from using the same password repeatedly. 

To do this, use the following API request:

```
POST
https://{{accountName}}.{{environment}}.com.br/api/vtexid/pub/providers/setup/password/webstore/password
```

Request body:

```json
{
    "isActive": true,
    "allowRepeated": false
}
```

>⚠️ This configuration impacts all shoppers of your account. You only need to send this request this whenever you want to change this configuration.

## Expiring a password by email

You can use the API request below to expire the password associated with a specific shopper email:

```
POST
https://{{accountName}}.{{environment}}.com.br/api/vtexid/password/expire?email={{email}}
```

This request has no body.

A successful response will have status code `200` and an empty body.

>❗ This request does not trigger any notification. We strongly recommend that you [notify the user](#notifying-the-shopper) to prevent a frustrating shopping experience next time they try to login to your store.

## Notifying the shopper

Once you expire a shopper's password, they will not be able to login to your store. You must notify them of the expiration and instruct them to go to your store and create a new password.
