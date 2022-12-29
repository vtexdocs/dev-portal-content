---
title: "Create Authorization Token"
slug: "createauthorizationtoken"
excerpt: "Create token that will be used to identify the same context  when we redirect the merchant to your application."
hidden: false
createdAt: "2019-12-30T03:21:07.203Z"
updatedAt: "2020-09-29T21:30:30.929Z"
---
## Request body
---

<table>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>applicationId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>VTEX application identifier (always <code>vtex</code>)</td>
    </tr>
    <tr>
        <td><code>returnUrl</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>The base URL you need to use to form the final URL when redirecting the merchant back to VTEX</td>
    </tr>
</table>

<br></br>

## Response body
---

<table>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>applicationId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>The same <code>applicationId</code> sent in the request</td>
    </tr>
    <tr>
        <td><code>token</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>You must generate a token that will be used to identify the same context when we redirect the merchant to your application</td>
    </tr>
</table>

## Request examples and their responses
[block:code]
{
  "codes": [
    {
      "code": "curl --location --request POST 'https://{{providerApiEndpoint}}/authorization/token' \\\n--header 'Content-Type: application/json' \\\n--header 'Accept: application/json' \\\n--data-raw '{\n    \"applicationId\": \"vtex\",\n    \"returnUrl\": \"https://admin.mystore.example.com/provider-return?authorizationCode=\"\n}'",
      "language": "curl",
      "name": "Success"
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