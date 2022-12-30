---
title: "Provider Authentication"
slug: "providerauthentication"
excerpt: "Use the application of provider for merchant's authentication."
hidden: false
createdAt: "2019-12-30T03:21:07.203Z"
updatedAt: "2020-09-29T21:34:34.754Z"
---
VTEX will redirect the merchant to your application using the `token` we retrieved earlier.

You're expected to have a signup/signin process on your side in order to authenticate the merchant, either as a new or as an existent user.

At this point, you can present your terms an conditions, a contract, and ask for merchant's final agreement to use your services.

Finally, you need to generate an `authorizationCode` that you must concatenate to the `returnUrl` we send earlier.

## Example:

---
> `returnUrl` = `https://admin.mystore.example.com/provider-return?authorizationCode=`
>
> `authorizationCode` = `7940597D-A63B`

##### Redirect the merchant to:

---
> `https://admin.mystore.example.com/provider-return?authorizationCode=7940597D-A63B`

## Request examples and their responses 
[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET 'https://{{providerApiEndpoint}}/authorization/redirect?applicationId=vtex&token={{token}}'",
      "language": "curl",
      "name": "Provider Authentication"
    }
  ]
}
[/block]