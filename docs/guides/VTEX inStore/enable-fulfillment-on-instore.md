---
title: "Enable Fulfillment on inStore"
slug: "enable-fulfillment-on-instore"
hidden: true
createdAt: "2021-09-16T17:23:14.801Z"
updatedAt: "2022-02-24T20:45:25.026Z"
---
**Fulfillment** is an inStore module where the physical store fulfillment operators or sales associates can see orders to be picked up and to be shipped from the store. It allows picking, packing, invoicing and preparation for shipping or pick up and enables staff to check every order and their respective changes in status.

Follow the instructions below to enable **Fulfillment** on inStore.

## Prerequisites

Before you start the **Fulfillment** setup itself, you must:

1. [Install VTEX IO’s CLI in your machine.](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-installation-and-command-reference)
2. [Set up a development environment.](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-2-basicsetuptodevelopinvtexio)
3. [Install inStore in your VTEX account.](https://help.vtex.com/tracks/instore-getting-started-and-setting-up--zav76TFEZlAjnyBVL5tRc/4L5SoLxE8O3YkxF7FKymrO)
4. [Have at least one enabled seller.](https://help.vtex.com/en/tutorial/adding-a-seller--tutorials_392)

Make sure you meet all the requirements above before you proceed with the installation.

## Installation

### Step 1 - Enable the **Fulfillment** tab

The first step in the installation process is to enable the **Fulfillment** tab on the inStore menu. Follow the instructions below to do so.

1. Open the `checkout-instore-custom.js` file. To learn where to find this file, read our guide [How to customize inStore](https://developers.vtex.com/vtex-rest-api/docs/how-to-customize-instore#javascript-customizations).
2. Inside the `window.INSTORE_CONFIG` object, you must insert the following properties:
[block:parameters]
{
  "data": {
    "0-0": "`fulfillment`",
    "1-0": "↳ `enabled`",
    "2-0": "↳ `features`",
    "3-0": "↳↳ `shipFromStore`",
    "4-0": "↳↳↳ `enabled`",
    "5-0": "↳↳ `pickupInStore`",
    "6-0": "↳↳↳ `enabled`",
    "0-1": "object",
    "1-1": "boolean",
    "2-1": "object",
    "3-1": "object",
    "4-1": "boolean",
    "6-1": "boolean",
    "5-1": "object",
    "0-2": "Object that represents inStore’s **Fulfillment** module.",
    "1-2": "Set the value to `true` to show the **Fulfillment** tab on the inStore menu or `false` not to show it.\n\n",
    "2-2": "Object that contains features of inStore’s Fulfillment module.",
    "4-2": "Set the value to `true` to enable Ship From Store orders on **Fulfillment** or `false` not to enable them.\n\n",
    "3-2": "Object that represents the Ship From Store feature.",
    "5-2": "Object that represents the Pick up in Store feature.",
    "6-2": "Set the value to `true` to enable Pick up in Store orders on **Fulfillment** or `false` not to enable them.",
    "h-1": "Type",
    "h-2": "Description",
    "h-0": "Field",
    "7-0": "↳↳ `partialPicking`",
    "8-0": "↳↳↳ `enabled`",
    "10-0": "↳↳↳ `enabled`",
    "9-0": "↳↳ `reverseOrder`",
    "7-1": "object",
    "9-1": "object",
    "8-1": "boolean",
    "10-1": "boolean",
    "7-2": "Object that represents the partial picking feature.",
    "8-2": "Set the value to `true` to enable partial picking or `false` to disable it. The default behavior is set to `true`.",
    "10-2": "Set the value to `true` to enable reverse logistics or `false` to disable it. The default behavior is set to `false`.",
    "9-2": "Object that represents the reverse logistics feature, to be used when an order is returned."
  },
  "cols": 3,
  "rows": 11
}
[/block]

#### Example code

[block:code]
{
  "codes": [
    {
      "code": "window.INSTORE_CONFIG = {\n   fulfillment: {\n    enabled: true,\n    features: {\n      shipFromStore: {\n         enabled: true,\n      },\n      pickupInStore: {\n         enabled: true,\n      },\n      partialPicking: {\n       \t enabled: true,\n      },\n      reverseOrder: {\n       \t enabled: true,\n      },  \n    },\n  },\n}",
      "language": "javascript"
    }
  ]
}
[/block]

### Step 2 - Install the Picking app

In both the main account (marketplace) and franchise account (seller), you must install the Picking app via CLI. Use the following command:

```
vtex install vtex.picking-app@2.x
```

[block:callout]
{
  "type": "info",
  "body": "If you need to list the franchise accounts associated with the main account, use the following License Manager API request: `GET https://licensemanager.vtex.com.br/api/license-manager/pvt/accounts/{{accountName}}?childAccounts=true`\n\nThe franchise accounts will be listed in the `childAccounts` object."
}
[/block]

### Step 3 - Install the Invoice Notifier app

Follow the instructions below to install the Invoice Notifier app, which allows you to notify an external endpoint automatically when an order is ready to be invoiced.

1. In both the main account (marketplace) and franchise account (seller), you must install the Invoice Notifier app via CLI. Use the following command:

```
vtex install vtex.invoice-notifier
```

2. After the installation, you must configure the Invoice Notifier app. Access `https://{accountName}.myvtex.com/admin/apps` on your browser, replacing `{accountName}` with your account name.

3. Click on **Invoice Notifier**.

4. Fill in the following information:

   - **URL to notify**: insert the external endpoint URL that will be notified when an order is ready to be invoiced.

   - **Provide a token that will be passed in the request**: insert a token to be used in the request to the external endpoint. This field is optional. Keep in mind this token must be previously set in the external infrastructure you want to notify, if you opt to use it.

5. Click on `Save`.
[block:callout]
{
  "type": "info",
  "body": "If you do not have an ERP system and you want to test the invoicing process, you can install the **Invoicer Mock** app in the franchise account to simulate an ERP invoicer.\n\nRun the `vtex install vtex.invoicer-mock` command via CLI to install **Invoicer Mock** and follow the other instructions listed in this section.\n\nKeep in mind that in this case you must set `https://{accountName}.myvtex.com/_v/mock/invoice` as the **URL to notify**. It is not necessary to provide a token.",
  "title": "Testing the invoicing process without an ERP system"
}
[/block]

### Step 4 - Set a **Message Center** template for pick up orders [optional]

[block:callout]
{
  "type": "info",
  "body": "This is a mandatory step only if you want to allow pick up orders."
}
[/block]

In the main account (marketplace), make sure you configure the **Message Center** email template to notify clients when their orders are ready to be picked up at the selected store. Follow the instructions below to do so.

1. On the main account’s Admin (marketplace), click on **Message Center** in the **Customer** module.
2. Click on **Templates** to view all existing email templates.
3. Click on `New template` to create a new email template.
4. Name your template `Order ready for pickup in store` or `order-ready-for-pickup-in-store`, as illustrated below. It is important to use one of these exact names for the email to be sent automatically when orders are ready to be picked up.
   ![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/enable-fulfillment-on-instore-0.gif)
5. Enable the **Enable e-mail sending?** option, as shown above.
6. Fill in the template fields and write the HTML code for your template. To learn more about how to do this, read [our articles in the Templates category](https://help.vtex.com/en/subcategory/templates--4D5LrWwlHGmOWMomOaaGee). Make sure you use the `{{clientProfileData.email}}` tag in the **To** field, to indicate clients’ respective emails.
7. Click `Save` when you are done.

#### Example template

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/enable-fulfillment-on-instore-1.png)

### Step 5 - Set the seller’s origin address [optional]

[block:callout]
{
  "type": "info",
  "body": "This is a mandatory step only if you want to enable the [Ship from Store](https://help.vtex.com/en/tracks/unified-commerce-strategies--3WGDRRhc3vf1MJb9zGncnv/50GAmxxFsJoLWqcnMysWdl) strategy using VTEX Log."
}
[/block]

In this step, you must register the physical store’s origin address using the Logistics API. To do so, you can make a `POST` call to this endpoint: `https://portal.vtexcommercestable.com.br/api/logistics/pvt/configuration/originaddress?an={accountName}` .

Below you can find an example of what the body of this request should look like. Make sure you replace `{accountName}` with the franchise account name and the `null` values with the respective store address information.

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"postalCode\": null,\n    \"country\": null,\n    \"city\": null,\n    \"state\": null,\n    \"neighborhood\": null,\n    \"street\": null,\n    \"number\": null,\n    \"complement\": null,\n    \"reference\": null,\n    \"location\": null\n}'",
      "language": "json"
    }
  ]
}
[/block]

### Step 6 - Install the carrier apps [optional]

[block:callout]
{
  "type": "info",
  "body": "This is a mandatory step only if you want to enable the Ship from Store strategy with an integrated carrier."
}
[/block]
In both the main account (marketplace) and franchise account (seller), you must install the carrier apps via CLI, using the following commands.

```
vtex install vtex.carrier-notifier
vtex install vtexlog.labels-emitter
```

If your carrier is integrated to **VTEX Log**, you must also install the Carrier Tracking app by using the following command:

```
vtex install vtex.carrier-tracking
```

[block:callout]
{
  "type": "info",
  "body": "In case you have previously installed the apps, make sure they are updated by running the `vtex update` command on the CLI."
}
[/block]

### Step 7 - Configure a printer

Follow the steps detailed in the [Set up the order summary printing](https://developers.vtex.com/vtex-rest-api/docs/set-up-the-order-summary-printing) guide to configure a printer.

## Testing the module

Follow the instructions below to test the correct functioning of the **Fulfillment** module on inStore.

1. Open the inStore app using your device.
2. Log in as one of the sales associates you registered for the store where you have enabled **Fulfillment** following the steps above.
3. Place a test order using inStore. Make sure you select pickup in store as the delivery method, if enabled.
4. Then, in the inStore menu, click on the **Fulfillment** module. If you see the test order you placed, you are all set and the **Fulfillment** module has been installed correctly. If the test order does not show up, wait 5 minutes and try again.
