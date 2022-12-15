---
title: "Search all invoices"
slug: "searchallinvoices"
excerpt: "Returns all invoices according to the informed query params in the request."
hidden: false
createdAt: "2019-12-24T00:49:31.616Z"
updatedAt: "2022-05-23T12:15:06.773Z"
---
## Paging params

---
<ul>
<li><strong>By page numbers</strong>:<code>?from={int}&to={int}</code></li>
</ul>

## Date params

---

You can refine the API response using the two date params that will always be used in ISO8601 format.

<ul>
  <li><strong>By creation date</strong>: <code>?createdDateFrom={dateISO8601}&createDateTo={dateISO8601}</code></li>
  <li><strong>By due date</strong>: <code>?dueDateFrom={dateISO8601}&dueDateTo={dateISO8601}</code></li>
  </ul>

## Other filters

---
For proper responses, you can use the filters below:

<ul>
<li><strong>By value</strong>: <code>?value={decimal}</code></li>
<li> <strong>By status</strong>: <code>?status={string}</code></li>
<li><strong>By Id</strong>: <code>?Id={string}</code></li>
<li><strong>By observation</strong>: <code>?observation={string}</code></li>
<li><strong>By creditAccountId</strong>: <code>?creditAccountId={creditAcountId}</code></li>
</ul>

## Combine filters

---

You can use the query parameter `op` to specify if filters will be evaluated as `AND` or `OR` for the query. In this case, the default is `AND`.

Let's see how it works?

For example, if we take the query string `?value=100&status=Paid`, the criteria will build <strong>value=100 AND status=Paid</strong>.

Now, if we take the same query string and add the `op` parameter, the result will be `?value=100&status=Paid&op=or` and the criteria will build <strong>value=100 OR status=Paid</strong>

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
        <td></td>
    </tr>
    <tr>
        <td><code>friendlyId</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td><code>status</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td><code>value</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td><code>accountId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td><code>creditValue</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td><code>createdAt</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td><code>resolvedAt</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td><code>updatedAt</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td><code>paymentLink</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td><code>originalDueDate</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td><code>dueDate</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td><code>installment</code></td>
        <td>number</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td><code>orderId</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td><code>observation</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td><code>transactionId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td><code>numberOfInstallments</code></td>
        <td>number</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td><code>creditAccountId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
</table>

## Response body example

[block:code]
{
  "codes": [
    {
      "code": "{\n            \"id\": \"\",\n            \"friendlyId\": \"\",\n            \"status\": \"Paid\",\n            \"value\": 101.22,\n            \"accountId\": \"\",\n            \"creditValue\": 0.0,\n            \"createdAt\": \"2019-12-08T16:13:36.0469451Z\",\n            \"resolvedAt\": \"2019-12-17T15:28:25.1776415Z\",\n            \"updatedAt\": \"2019-12-17T15:28:25.240167Z\",\n            \"paymentLink\": \"\",  \n            \"originalDueDate\": \"2020-01-07T16:13:36.0469451Z\",\n            \"dueDate\": \"2020-01-07T16:13:36.0469451Z\",\n            \"installment\": 1,\n            \"orderId\": \"\",\n            \"transactionId\": \"\",\n            \"numberOfInstallments\": 1,\n            \"creditAccountId\": \"\"\n        },",
      "language": "json"
    }
  ]
}
[/block]
