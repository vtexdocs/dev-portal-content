---
title: "4. Get Credentials"
slug: "4getcredentials"
hidden: false
createdAt: "2020-05-13T21:52:02.370Z"
updatedAt: "2020-05-18T23:16:11.535Z"
---
#### RESPONSE BODY
---

<table>
  <tr>
      <td><code>applicationId</code></td>
      <td><b>string<b></td>
      <td>applicationId used</td>
  </tr>
  <tr>
      <td><code>appKey</code></td>
      <td><b>string</b></td>
      <td>Will be used in all request API Calls as X-VTEX-API-AppKey</td>
   </tr>
    <tr>
      <td><code>appToken</code></td>
      <td><b>string<b></td>
      <td>Will be used in all request API Calls as X-VTEX-API-AppToken</td>
  </tr>
</table>

<br>

#### REQUEST EXAMPLES AND THEIR RESPONSES
---
[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET '{{providerBaseUrl}}/authorization/credentials?authorizationCode={{authorizationCode}}&applicationId=vtex' \\\n--data-raw ''",
      "language": "curl",
      "name": "4. Get Credentials"
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