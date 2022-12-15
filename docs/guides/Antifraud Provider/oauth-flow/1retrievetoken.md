---
title: "1. Retrieve Token"
slug: "1retrievetoken"
excerpt: "In this API Call VTEX will expect a token to be created."
hidden: false
createdAt: "2020-05-13T21:52:02.370Z"
updatedAt: "2021-11-24T20:47:58.411Z"
---
#### REQUEST HEADERS 
---

<table>
  <tr>
        <td><b>Header</b></td>
        <td><b>Value</b></td>
    </tr>
    <tr>
        <td><code>Accept</code></td>
        <td><b>application/json</b></td>
    </tr>
    <tr>
        <td><code>Content-Typen</code></td>
        <td><b>application/json</b></td>
    </tr>
</table>

#### REQUEST BODY
<table>
  <tr>
      <td><code>applicationId</code></td>
      <td><b>string</b></td>
      <td>Always will have the [vtex] value</td>
  </tr>
  <tr>
      <td><code>returnUrl</code></td>
      <td><b>string</b></td>
      <td>Return URL. VTEX Url Web site. You will redirect the user after he completes the login/logon 
    in your payment provider web site.  
    The Url will contain a query string parameter 
    called <b>authorizationCode</b> that will be passed empty and that you MUST fill before return the user </td>
  </tr>
</table>



#### RESPONSE BODY
---

<table>
  <tr>
      <td><code>token</code></td>
      <td><b>string</b></td>
      <td>Payment Provider Token. Used to identify the context after you receive the redirected user to your site</td>
  </tr>
</table>



#### REQUEST EXAMPLES AND THEIR RESPONSES
---
[block:code]
{
  "codes": [
    {
      "code": "curl --location --request POST '{{providerBaseUrl}}/authorization/token' \\\n--header 'Content-Type: application/json' \\\n--data-raw '{\n    \"applicationId\": \"vtex\",\n    \"returnUrl\":\"https://storevtex.vtexpayments.com/?authorizationCode=\"\n}'",
      "language": "curl",
      "name": "1. Retrieve Token"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"applicationId\": \"vtex\",\n  \"token\": \"358a5bea-07d0-4122-888a-54ab70b5f02f\"\n}",
      "language": "curl",
      "name": "200 - OK"
    }
  ]
}
[/block]