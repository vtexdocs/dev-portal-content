---
title: "Get Credentials"
slug: "getcredentials"
excerpt: "Get the credentials of merchant."
hidden: false
createdAt: "2019-12-30T03:21:07.203Z"
updatedAt: "2020-09-29T21:37:04.097Z"
---
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
        <td><code>appKey</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>The value we will send in the header <code>X-VTEX-API-AppKey</code> for the payment flow</td>
    </tr>
    <tr>
        <td><code>appToken</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>The value we will send in the header <code>X-VTEX-API-AppToken</code> for the payment flow</td>
    </tr>
</table>

## Request examples and their responses
[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET 'https://{{providerApiEndpoint}}/authorization/credentials?authorizationCode={{authorizationCode}}&applicationId=vtex' \\\n--header 'Content-Type: application/json' \\\n--header 'Accept: application/json'",
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
      "code": "{\n  \"applicationId\": \"vtex\",\n  \"appKey\": \"c5a5e3f1-4a77-4a00-8b53-0d1adb3e9628\",\n  \"appToken\": \"57ea254d-f3d3-488d-88d7-129766037ed1\"\n}",
      "language": "curl",
      "name": "200 - OK"
    }
  ]
}
[/block]