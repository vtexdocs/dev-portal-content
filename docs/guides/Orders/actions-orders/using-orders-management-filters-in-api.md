---
title: "Using VTEX Admin filters on orders via API"
slug: "using-orders-management-filters-in-api"
hidden: false
createdAt: "2022-08-30T21:36:16.898Z"
updatedAt: "2022-10-21T00:10:50.805Z"
---
This article explains how to use the VTEX Admin Order Management filters via the [List orders](https://developers.vtex.com/vtex-rest-api/reference/listorders) API:

**GET** - `https://{accountName}.{environment}.com.br/api/oms/pvt/orders`

<br>

To apply VTEX Admin filters via API, follow the steps below:

1. Access your VTEX Admin in **Orders > Order Management > All Orders**.
2. Click on the filters icon.

<br>

![filter_icon_step_2](https://files.readme.io/df54dbf-filter_icon_step_2.jpg)
<br>

3. Select the filter you want to apply and click `Confirm`. You can combine multiple filters.

<br>

![filter_type_step_3](https://files.readme.io/0a13fb3-filter_type_step_3.jpg)

<br>

4. After selecting the filters, copy the URL generated in your browser. 
5. Using an [URL decoder](http://meyerweb.com/eric/tools/dencoder/) tool, decode the URL so that It will look like the following example:

<br>

![decode_print](https://files.readme.io/f9abe45-decode_print.jpg)

<br>

6. Copy only the URL extension after the question mark `?`.

    > For example: `orderBy=creationDate,desc&page=1&f_creationDate=creationDate:[2022-10-01T03:00:00.000Z TO 2022-11-01T02:59:59.999Z]&f_status=$$ALL_VALUES$$`

7. In your browser, insert the API [List orders](https://developers.vtex.com/vtex-rest-api/reference/listorders) path (`https://{accountName}.{environment}.com.br/api/oms/pvt/orders`) followed by the URL excerpt from last step. 
    > For example: `https://{accountName}.{environment}.com.br/api/oms/pvt/orders?orderBy=creationDate,desc&page=1&f_creationDate=creationDate:[2022-10-01T03:00:00.000Z TO 2022-11-01T02:59:59.999Z]&f_status=$$ALL_VALUES$$`

8. Click on `Enter`.

<br>
[block:callout]
{
  "type": "info",
  "body": "You can use pagination and determine the number of orders per page by adding the parameters `_&amp;page=1&amp;per_page=15_` at the end of your URL. The `page=1` means accessing the first page, and `per_page=15` means 15 orders on each page. You can change it as you wish, up to the limit of 30 pages."
}
[/block]