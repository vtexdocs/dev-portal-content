---
title: "List All GiftCard Providers"
slug: "listallgiftcardproviders"
excerpt: "Returns a collection of giftcard providers from a store."
hidden: false
createdAt: "2019-12-25T01:06:56.270Z"
updatedAt: "2020-07-10T19:40:41.058Z"
---
## Response body has the following properties: 
<table>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>id</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>serviceUrl</code></td>
        <td>string</td>
        <td>Yes</td>
        <td><td>
    </tr>
 <tr>
        <td><code>oauthProvider</code></td>
        <td>string</td>
        <td>Yes</td>
       <td></td>
    </tr>
 <tr>
        <td><code>caption</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td><code>preAuthEnabled</code></td>
        <td>boolean</td>
        <td>Yes</td>
       <td></td>
    </tr>
 <tr>
        <td><code>cancelEnabled</code></td>
        <td>boolean</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>appToken</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
 <tr>
        <td><code>appKey</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
 <tr>
        <td><code>_self</code></td>
        <td>object</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td>&#x21B3;<code>href</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>       
    </tr>
</table>

<br>

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "[\n    {\n        \"id\": \"\",\n        \"serviceUrl\": \"\",\n        \"oauthProvider\": \"\",\n        \"caption\": \"\",\n        \"preAuthEnabled\": true,\n        \"cancelEnabled\": true,\n\t\t\"appToken\": \"\",\n        \"appKey\": \"\",\n        \"_self\": {\n            \"href\": \"\"\n        }\n    }\n]",
      "language": "json"
    }
  ]
}
[/block]