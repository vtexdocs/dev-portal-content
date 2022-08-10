---
title: "Retrieve invoice by creditAccountId"
slug: "searchallinvoicesofaaccount"
excerpt: "Returns associated invoices by specified creditAccountId, the param that identifies a client in VTEX's system."
hidden: false
createdAt: "2019-12-24T00:49:31.616Z"
updatedAt: "2020-07-09T20:11:29.816Z"
---
## Paging params 
---
<ul>
<li><strong>By page numbers</strong>:<code>?from={int}&to={int}</code></li>
</ul>

<br>

## Date params
---

You can refine the API response using the two date params that will always be used in ISO8601 format.

<ul>
  <li><strong>By creation date</strong>: <code>?createdDateFrom={dateISO8601}&createDateTo={dateISO8601}</code></li>
  <li><strong>By due date</strong>: <code>?dueDateFrom={dateISO8601}&dueDateTo={dateISO8601}</code></li>
  </ul>

<br>

## Other filters 
---
For proper responses, you can use the filters below:

<ul>
<li><strong>By value</strong>: <code>?value={decimal}</code></li>
<li> <strong>By status</strong>: <code>?status={string}</code></li>
<li><strong>By Id</strong>: <code>?Id={string}</code></li>
<li><strong>By observation</strong>: <code>?observation={string}</code></li>
<li><strong>By checkingAccountId</strong>: <code>?checkingAccountId={checkingaccountId}</code></li>
</ul>

<br>

## Combine filters 
---

You can use the query parameter `op` to specify if filters will be evaluated as `AND` or `OR` for the query. In this case, the default is `AND`.

Let's see how it works? 

For example, if we take the query string `?value=100&status=Paid`, the criteria will build <strong>value=100 AND status=Paid</strong>. 

Now, if we take the same query string and add the `op` parameter, the result will be `?value=100&status=Paid&op=or` and the criteria will build <strong>value=100 OR status=Paid</strong>

<br>