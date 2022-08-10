---
title: "Search all accounts"
slug: "searchallaccounts"
hidden: false
createdAt: "2019-12-24T00:49:31.616Z"
updatedAt: "2022-05-23T12:16:36.663Z"
---
## Paging params
---
<ul>
<li><strong>By page numbers</strong>:<code>?from={int}&to={int}</code></li>
</ul>

<br>

#### Other filters
---
For proper responses, you can use the filters below:

<ul>
<li><strong>By value</strong>: <code>?value={decimal}</code></li>
<li> <strong>By status</strong>: <code>?status={string}</code></li>
<li><strong>By Id</strong>: <code>?Id={string}</code></li>
<li><strong>By observation</strong>: <code>?observation={string}</code></li>
<li><strong>By creditAccountId</strong>: <code>?creditAccountId={creditAcountId}</code></li>
</ul>

<br>

## Combine filters
---

You can use the query parameter `op` to specify if filters will be evaluated as `AND` or `OR` for the query. In this case, the default is `AND`.

Let's see how it works? 

For example, if we take the query string `?value=100&status=Paid`, the criteria will build <strong>value=100 AND status=Paid</strong>. 

Now, if we take the same query string and add the `op` parameter, the result will be `?value=100&status=Paid&op=or` and the criteria will build <strong>value=100 OR status=Paid</strong>

<br>


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
        <td><code>balance</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>document</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>status</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td><code>documentType</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>creditLimit</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>updatedAt</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>createdAt</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <td><code>description</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td><code>availableCredit</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>preAuthorizedCredit</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>email</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>tolerance</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td></td>
    </tr>
<td><code>availableTolerance</code></td>
        <td>decimal</td>
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
      "code": "{\n            \"id\": \"\",\n            \"balance\": 0.0,\n            \"document\": \"\",\n            \"status\": \"Open\",\n            \"documentType\": \"CPF\",\n            \"creditLimit\": 5000.0,\n            \"updatedAt\": \"2020-03-26T19:04:49.0448493Z\",\n            \"createdAt\": \"2019-12-03T00:19:21.9198519Z\",\n            \"description\": \"\",\n            \"availableCredit\": 5000.0,\n            \"preAuthorizedCredit\": 0.0,\n            \"email\": \"\",\n            \"tolerance\": 0.0,\n            \"availableBalance\": 5000.0\n        },",
      "language": "json"
    }
  ]
}
[/block]