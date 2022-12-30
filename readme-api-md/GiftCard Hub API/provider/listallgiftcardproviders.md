---
title: "List All GiftCard Providers"
slug: "listallgiftcardproviders"
excerpt: "Returns a collection of giftcard providers from a store."
hidden: false
createdAt: "2019-12-25T01:06:56.270Z"
updatedAt: "2021-07-01T18:46:01.313Z"
---
## Response body has the following properties

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
        <td>Gift Card provider’s id</td>
    </tr>
    <tr>
        <td><code>serviceUrl</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>URL from the provider</td>
    </tr>
    <tr>
        <td><code>oauthProvider</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Provider’s authentication</td>
    </tr>
    <tr>
        <td><code>caption</code></td>
        <td>string</td>
        <td></td>
        <td>Description about the provider</td>
    </tr>
    <tr>
        <td><code>preAuthEnabled</code></td>
        <td>boolean</td>
        <td>Yes</td>
        <td>Related to the pre-authorization that can happen on the transaction generated through the provider</td>
    </tr>
    <tr>
        <td><code>cancelEnabled</code></td>
        <td>boolean</td>
        <td>Yes</td>
        <td>It says if it is possible to cancel the transaction, generated through the provider</td>
    </tr>
    <tr>
        <td><code>appToken</code></td>
        <td>string</td>
        <td></td>
        <td>Credential that will identify the provider inside VTEX</td>
    </tr>
    <tr>
        <td><code>appKey</code></td>
        <td>string</td>
        <td></td>
        <td>Credential that will identify the provider inside VTEX</td>
    </tr>
    <tr>
        <td><code>_self</code></td>
        <td>object</td>
        <td>Yes</td>
        <td>It is an object that carries an auto reference from the provider at the Hub (on its API)</td>
    </tr>
    <tr>
        <td>&#x21B3;<code>href</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>This is one of the fields inside the_self . It is exactly the route that identifies this provider on the
            Hub’s API, but it is not the same thing as the serviceURL</td>
    </tr>
</table>

## Response body example

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
