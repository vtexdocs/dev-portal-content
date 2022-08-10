---
title: "Authentication"
slug: "getting-started-authentication"
excerpt: "Learn how to get authorization to access VTEX REST APIs."
hidden: false
createdAt: "2020-01-15T18:58:34.836Z"
updatedAt: "2021-09-02T15:57:13.976Z"
---
VTEX offers a series of open APIs so that retailers and partners can make highly customizable integrations with our systems.

Most of these APIs are private and, as so, require you to provide a pair of credentials before you can access them.

These credentials are:
* An `appKey`
* An `appToken`

They work as a pair of ID and password, and must be created inside your store's administration panel.
[block:api-header]
{
  "title": "Creating the appKey and appToken"
}
[/block]
To generate app keys in your account, you should follow the instructions seen in the [Application Keys](https://help.vtex.com/en/tutorial/application-keys--2iffYzlvvz4BDMr6WGUtet) article in our Help Center.
[block:api-header]
{
  "title": "Using the appKey and appToken to authenticate"
}
[/block]
Now it's time to authenticate your first integration with a VTEX API.

You will do it by using the `appKey` and `appToken` you've just created as values of your request's **authentication headers**.

1. The `appKey` should be provided through the `X-VTEX-API-AppKey` header.
2. The `appToken` should be provided through the `X-VTEX-API-AppToken` header.
[block:callout]
{
  "type": "info",
  "body": "According to the [W3C definition of Message Headers in HTTP requests](https://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html#sec4.2), header names are case-insensitive. `X-VTEX-API-AppKey`, `x-vtex-api-appkey` or any other variation in the authentication headers will work the same way."
}
[/block]
Great job! You should now be able to authenticate and use VTEX APIs on your account.

Let's do that in the next step of this introduction.