---
title: "List Antifraud Provider Manifest"
slug: "manifest"
excerpt: "Returns the custom fields of the antifraud provider manifest"
hidden: false
createdAt: "2021-04-30T17:21:06.429Z"
updatedAt: "2022-04-26T00:13:55.633Z"
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
<td><code>cardholderDocument</code></td>
<td>string</td>
<td></td>
<td>Describes the need for cardholder documentation to process antifraud analysis. Accepted values:
<br>
<code>required</code>: a cardholder document is mandatory.
<br>
<code>optional</code>: a cardholder document can be used, but is not required.
<br>
<code>unused</code>: a cardholder document is not required.</td>
</tr>
<tr>
<td><code>customFields</code></td>
<td>object</td>
<td></td>
<td>Describes the customized fields supported by the connector</td>
</tr>
<tr>
<td>&#x21B3; <code>name</code></td>
<td>string</td>
<td>Yes</td>
<td>Custom field name </td>
</tr>
<tr>
<td>&#x21B3; <code>type</code></td>
<td>string</td>
<td>Yes</td>
<td>Custom field type. Accepted values: <code>text</code>, <code>select</code></td>
</tr>
<tr>
<td>&#x21B3; <code>options</code></td>
<td>string</td>
<td></td>
<td>In case of <code>select</code> type, the possible params are <code>text</code> and <code>value</code></td>
</tr>
<tr>
<td>&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &#x21B3;<code>text</code></td>
<td>object</td>
<td></td>
<td>Custom field description</td>
</tr>
<tr>
<td>&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &#x21B3;<code>value</code></td>
<td>string</td>
<td></td>
<td>Custom field value</td>
</tr>
</table>

## Request examples and their responses

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET 'http:///%7Binsert%20URL%20here%7D/manifest' \\\n--header 'Content-Type: application/json' \\\n--header 'Accept: application/json'",
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
      "code": "{\n  \"cardholderDocument\": \"required\",\n  \"customFields\":[\n   {\n     \"name\":\"ApiKey\",\n     \"type\":\"text\"\n   }\n   {\n     \"name\":\"AnalysisLocation\",\n     \"type\":\"select\",\n     \"options\":[\n        {\n             \"text\":\"MEX\",\n             \"value\":\"Latin America\"\n        }\n        {\n             \"text\":\"USA\",\n             \"value\":\"United States\"\n        }\n      ]\n    }\n  ]\n}",
      "language": "curl",
      "name": "200 - OK"
    }
  ]
}
[/block]
