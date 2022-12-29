---
title: "Configure the price history control"
slug: "configure-the-price-history-control"
hidden: false
createdAt: "2022-09-08T14:27:11.386Z"
updatedAt: "2022-09-08T14:27:11.386Z"
---

The past prices control in VTEX is intended to show the lowest price invoiced for an item per month. In other words, it can show the lowest price for which a particular item was sold in your store.

### How to configure it

The control should be included in the product page's template, as follows:

```
<!--Price History Inicio v1-->
<b style="font-family: Inconsolata, monospace;"><vtex.cmc:StockKeepingUnitPriceHistory Months="6" Percentile="100"/>
<!--Price History Fim-->
```

See the complete list of controls for templates [here](http://help.vtex.com/tutorial/lista-de-controles-para-templates/ "here").

### Showing the prices

The default exhibition method for the values looks like the image below. The year, month and lowest amount invoiced this month are shown in sequence.

![HistPrecos](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/configure-the-price-history-control-0.png)

If you want to show these details in another way, you will have to get a layout agency to customize the model.

### The parameters *Months* and *Percentile*

To allow more flexibility in showing values in the product page, you can use the **\_Months \_**parameter to define the number of months to be taken into account by the control.

If the parameter is "6", for example, the control will show the lowest amount invoiced for the item in each of the last six months.

In addition, it can happen that the lowest amount invoiced for the item is below the price usually applied by the store, for example because of a specific promotion. To avoid showing this value, you can use the parameter ***Percentile***.

This allows you to ignore peripheral values. For example: using the parameter with a value of 95 (Percentile="95"), 5% of the amounts are ignored.

Using the parameter with a value of 90 (Percentile="90"), 10% of the amounts are ignored.

In cases like that, prices much below those normally applied will not be shown.

*If there are price variations in a particular month, the control shows the lowest value invoiced for the item during the month.*

*If there were no sales of an item during the month, the control will not show a value for it.*
