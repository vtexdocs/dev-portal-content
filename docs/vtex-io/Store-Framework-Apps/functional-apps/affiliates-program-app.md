---
title: "Affiliates Program"
slug: "affiliates-program-app"
hidden: false
createdAt: "2022-10-14T17:02:14.091Z"
updatedAt: "2022-11-07T22:59:36.234Z"
---

> ℹ️ For the **Affiliates Program app**, an affiliate is different from the standard definition of [affiliate in VTEX](https://help.vtex.com/en/tutorial/o-que-e-afiliado--4bN3e1YarSEammk2yOeMc0). In the app's context, an affiliate is anyone who associates with a VTEX store to promote sales while receiving a commission.

The [Affiliates Program app](https://help.vtex.com/en/tutorial/aplicativo-affiliates-program--7IpHHHcjjWxdmSRMw1FMPQ) creates a specific URL of your VTEX store for each of your affiliates, and every URL is targeted with a parameter that identifies the affiliate. When an affiliate shares their URL with shoppers, and they buy something through that link, the affiliate earns a commission over sales.

The image below is an example of an affiliate’s page to be shared with shoppers:

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/affiliates-program-app-0.png)

The app also creates a profile page for the affiliate to keep track of orders and commissions, as you will see in the next section. Affiliates do not need access to your VTEX store Admin in order to access their profile page, which looks like the following image:

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/affiliates-program-app-1.png)

The **Affiliates Program app’s** main characteristics and behavior are the following:

* The app [provides pages and dashboards](https://help.vtex.com/en/tutorial/aplicativo-affiliates-program--7IpHHHcjjWxdmSRMw1FMPQ#vtex-admin-pages) in your VTEX Admin, allowing your store to manage affiliates, orders, and commissions.
* The merchant using a VTEX store can register an affiliate by filling out a form. More information on the next section.
* The merchant using a VTEX store configures a default affiliates’ commission percentage over all products. It is possible to configure a specific commission for an SKU, and that configuration is prioritized over the default value.
* The [affiliates’ URLs can be customized](#affiliates-pages-customization) to show specific products and guide the customer’s user experience.

### Affiliates Program in VTEX Admin

After installing and configuring the app, you will find three pages in your VTEX Admin:

* [Affiliate Management](https://help.vtex.com/en/tutorial/aplicativo-affiliates-program--7IpHHHcjjWxdmSRMw1FMPQ#affiliate-management): allows you to add new affiliates and manage the existing ones. You can add a new affiliate by clicking on the button `Add affiliate` and filling out the form.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/affiliates-program-app-2.png)

* [Orders Management](https://help.vtex.com/en/tutorial/aplicativo-affiliates-program--7IpHHHcjjWxdmSRMw1FMPQ#order-management): provides information about affiliates’ orders. The page enables you to filter data in multiple ways and export it via email.
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/affiliates-program-app-3.png)

* [Commissions Management](https://help.vtex.com/en/tutorial/aplicativo-affiliates-program--7IpHHHcjjWxdmSRMw1FMPQ#commission-management): allows you to manage affiliates’ commissions and import information using files with . CSV or . XLSX extension.
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/affiliates-program-app-4.png)

## Compatibility

The Affiliates Program app is compatible only with stores using [VTEX IO](https://help.vtex.com/en/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/4yB9wSl79cArd68aRBnBZ2), so make sure you fit the criteria. Stores using [Legacy CMS](https://help.vtex.com/en/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/1oN446gRGcR2s70RvBCAmj) or [Headless CMS](https://faststore.dev/tutorials/cms/0#vtex-headless-cms) are not compatible.

## Installation

To install the Affiliates Program app, follow the steps below:

1. In the VTEX App Store, log into your VTEX store’s account.
2. Go to the [Affiliates Program app](https://apps.vtex.com/vtex-affiliates/p) page.
3. Click on `GET APP`.
4. In your cart in the VTEX App Store, click on `PLACE ORDER`.
5. Click on `GO TO INSTALL PAGE`.
6. In the VTEX Admin, click on `INSTALL`.

The app settings will appear in your VTEX Admin under _Other > Affiliates_, and you will see a page like the image below:

> If using the [New VTEX Admin](https://content.vtex.com/join-new-admin-beta-program-en/), you will find the app settings under _Apps > Affiliates_.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/affiliates-program-app-5.png)

In **Settings**, you will define for how long the lead will be valid and set a default commission percentage. To do so, follow the steps below:

1. Fill in the **Lead duration in days** field with the number of days you wish to configure the lead. It is the lead that sets the priority of an affiliate to receive commissions.
[block:callout]
{
  "type": "warning",
  "body": "Every affiliate has its own unique identification code, which is the `Affiliate ID` . When a shopper buys something through the affiliate's URL, the `Affiliate ID` is linked to the shopper for the period configured in this step - 60 days by default. If within the lead duration that shopper makes a second purchase, whether by accessing the store in an organic way, or through another affiliate's URL, the `Affiliate ID` of the first affiliate is prioritized and ensures commission. Note that the `Affiliate ID` for the app's context is not the `Affiliate ID` in the standard definition of [affiliate in VTEX](https://help.vtex.com/en/tutorial/o-que-e-afiliado--4bN3e1YarSEammk2yOeMc0)."
}
[/block]

2. Fill in the **Default value to be used for sku commission** field with the percentual you want to set to determine the affiliates’ commission over sales. Use numbers only, decimals are not allowed.
3. Click on `SAVE`.

  The following message will be displayed:
  > _Your information was submitted successfully._

## Configuration

You will need to access your VTEX store’s code to set up the app and the affiliate’s URL, as shown in the following sections.

### Set up the Affiliates Program app

Open your store's **Store Theme** app directory in your code editor and add the Affiliates Program app to your theme's `manifest.json` file inside `peerDependencies` , as shown below:

[block:code]
{
  "codes": [

    {
      "code": "\"peerDependencies\": {\n  \"vtex.affiliates\": \"1.x\"\n }",
      "language": "json"
    }

  ]
}
[/block]

When you add the Affiliates Program app as a dependency, the app exports theme blocks used to create pages on the storefront: `affiliate` , `affiliate-profile` , and `affiliate-form` . These pages will be available with a default layout:

* **Affiliate’s page:** the page the affiliate sends to shoppers based on your VTEX store storefront. The URL is `{storeName.com}/affiliates/{affiliateSlug}`.
* **Affiliates profile page:** a page where the affiliate can see orders made through their URL and analyze a dashboard with different metrics. The URL is `{storeName.com}/affiliates/{affiliateSlug}/profile`.
* **Affiliate’s form:** a page with a form to be filled by anyone who wants to become an affiliate. The URL is `{storeName.com}/affiliate/form`.

To access the first two pages, you will have to configure an affiliate to be able to replace `{affiliateSlug}` with a valid slug.

### Set up a shareable URL

For the affiliate to be able to share their URL, you will need to add the `affiliate-url-monitoring` block into the header of your theme. That block seeks parameters with a valid affiliate slug to add the affiliate’s information to the purchase.

To do so, check out the example below:

After that, the affiliate will share a URL with the parameter **targeting** with their slug as value so that the affiliate’s information is associated with the sale. See an example in the table below:

[block:parameters]
{
  "data": {

    "h-0": "Example URL",
    "h-1": "Behavior",
    "0-0": " `https://storeName.com/product/p` ",
    "0-1": "URL without the **targeting** parameter, which does not identify the affiliate.",
    "1-0": " `https://storeName/product/p?targeting=affiliateName` ",
    "1-1": "URL with the **targeting** parameter, which links the shopper’s purchase to the affiliate."

  },
  "cols": 2,
  "rows": 2
}
[/block]
<br>

It is possible to change the parameter property used for the affiliate to share the URL by changing the code in [props](#props). You can also change it in VTEX Admin, by accessing _CMS > [Site Editor](https://help.vtex.com/en/tutorial/site-editor-overview--299Dbeb9mFczUTyNQ9xPe1) > Blocks > Affiliate Monitoring_ and editing the `Parameter` field, as shown in the image below:

> If using the [New VTEX Admin](https://content.vtex.com/join-new-admin-beta-program-en/), go to _Storefront > Site Editor > Blocks > Affiliate Monitoring_.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/affiliates-program-app-6.png)

## Advanced configurations

You can customize the appearance and content of the affiliate’s page - `{storeName.com}/affiliates/{affiliateSlug}` , as explained in the next sections:

* [Affiliate’s page customization](#affiliates-pages-customization)
* [Props](#props)
* [CSS customization](#css-customization)

### Affiliate’s pages customization

The default implementation of the affiliate’s page is the following:

[block:parameters]
{
  "data": {

    "h-0": "Block",
    "h-1": "Route",
    "0-0": " `store.affiliates interface` ",
    "1-0": " `store.affiliates-profile` ",
    "2-0": " `store.affiliate-form` ",
    "0-1": " `/affiliates/:slug` ",
    "1-1": " `affiliates/:slug/profile` ",
    "2-1": " `affiliate/form` "

  },
  "cols": 2,
  "rows": 3
}
[/block]

To customize these pages, follow the steps below:

1. Open your store's **Store Theme** app directory in your code editor.
2. Go to `store/blocks`.
3. Create the following files:
    -  `affiliates.jsonc`
    - `affiliates-profile.jsonc`
    - `affiliates-form.jsonc`

4. Copy the respective block’s code – you will find them below.
5. Paste the code in the corresponding file. For example, paste the `store.affiliates` JSON in the `affiliates.jsonc` file.
6. Customize the code as you wish.
7. Repeat steps 4 to 6 for each of the three blocks.
8. Deploy the changes.

**store.affiliates**

**store.affiliates-profile**

**store.affiliate-form**

### Props

You will have to configure two specific component types with props for them to work correctly.

`affiliate-validator` and `affiliate-profile-validator props`

[block:parameters]
{
  "data": {

    "h-0": "Prop name",
    "h-1": "Type",
    "h-2": "Description",
    "h-3": "Default value",
    "0-0": " `valid` ",
    "1-0": " `invalid` ",
    "0-1": "string",
    "1-1": "string",
    "0-2": "Set the block name that will be rendered if the affiliate is valid.",
    "1-2": "Set the block name that will be rendered if the affiliate is invalid.",
    "0-3": " `affiliate-template` ",
    "1-3": " `affiliate-invalid-template` "

  },
  "cols": 4,
  "rows": 2
}
[/block]

`affiliate_url_monitoring` props
[block:parameters]
{
  "data": {

    "h-0": "Prop name",
    "h-1": "Type",
    "h-2": "Description",
    "h-3": "Default value",
    "0-0": " `parameter` ",
    "0-1": "string",
    "0-2": "Parameter name that will be used to validate the URL the affiliate shared.",
    "0-3": " `targeting` "

  },
  "cols": 4,
  "rows": 1
}
[/block]

### CSS customization

If you wish to apply CSS customizations to the Affiliates Program app blocks, check out [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

[block:parameters]
{
  "data": {

    "0-0": " `affiliateStoreName` ",
    "h-0": "CSS Handles",
    "1-0": " `affiliateProfileTitle` ",
    "2-0": " `profileButtonContainer` "

  },
  "cols": 1,
  "rows": 3
}
[/block]

## Email templates

The Affiliates Program app allows your VTEX store to export spreadsheets with information about the affiliates' orders and commissions. Exported spreadsheets will be sent via email to the VTEX Admin [user](https://help.vtex.com/tutorial/managing-users--tutorials_512).

For this configuration, you need to create two email templates on the [Message Center](https://help.vtex.com/tutorial/understanding-the-message-center--tutorials_84):

* Affiliate Orders Export Template
* Commissions By Sku Export Template

To create a new custom email template, follow the steps below:

1. In your VTEX Admin, go to _Customer > Message Center > Templates_.
2. Click on the `New Template` button.
3. Check the `Enable sending emails` flag.
4. Fill in the fields that appear.
    > You can use the image below as a reference, but use your information.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/affiliates-program-app-7.jpg)
5. Copy the **Affiliate Orders Export Template** code - you will find it below.
6. Paste it in the `Html` section.
7. Change it as you wish.
    > You can scroll down the page to check the preview.

8. Click on `Save`.

After creating the _Affiliate Orders Export Template_, repeat the process to create the _Commissions By Sku Export Template_. Use the image below as an example for step 4. On step 5, copy the **Commissions By Sku Export Template** code, which can be found at the end of this section.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/affiliates-program-app-8.jpg)

**Affiliate Orders Export Template**
[block:code]
{
  "codes": [

    {
      "code": "  <!DOCTYPE html>\n<html lang=\"pt-br\">\n\n<head>\n    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n    <meta name=\"viewport\" content=\"initial-scale=1.0\">\n    <!-- So that mobile webkit will display zoomed in -->\n    <meta name=\"format-detection\" content=\"telephone=no\">\n    <!-- disable auto telephone linking in iOS -->\n    <title>{{_accountInfo.TradingName}}</title>\n    <style type=\"text/css\">\n        p {\n            font-family: Fabriga, -apple-system, BlinkMacSystemFont, avenir next, avenir, helvetica neue, helvetica, ubuntu, roboto, noto, segoe ui, arial, sans-serif;\n        };\n        .vtex-button {\n            border-width: .125rem;\n            border-style: solid;\n            font-weight: 500;\n            vertical-align: middle;\n            padding: 0;\n            line-height: 1;\n            border-radius: .25rem;\n            min-height: 2.5rem;\n            box-sizing: border-box;\n            font-family: Fabriga, -apple-system, BlinkMacSystemFont, avenir next, avenir, helvetica neue, helvetica, ubuntu, roboto, noto, segoe ui, arial, sans-serif;\n            font-size: 1rem;\n            text-transform: uppercase;\n            letter-spacing: 0;\n            background-color: #134cd8;\n            border-color: #134cd8;\n            color: #fff;\n            cursor: pointer;\n        };\n    </style>\n</head>\n\n<body marginwidth=\"0\" marginheight=\"0\" bgcolor=\"#fff\" style=\"padding:0px 0px;color:#333;\" leftmargin=\"0\" topmargin=\"0\">\n    <!-- 100% wrapper (grey background) -->\n    <table width=\"100%\" height=\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\" align=\"left\" valign=\"top\">\n        <tbody>\n            <tr>\n                <td align=\"center\" valign=\"top\">\n                    <table width=\"100%\" style=\"max-width: 36rem;\" align=\"center\" cellpadding=\"0\" cellspacing=\"0\"\n                        border=\"0\" valign=\"top\">\n                        <tbody>\n                            <tr>\n                                <td>\n                                    <div\n                                        style=\"border:1px solid #e3e4e6;border-radius:8px;margin-top:1rem;margin-bottom:1rem;padding-top:3rem;padding-right:3rem;padding-bottom:3rem;padding-left:3rem\">\n                                        <img src=\"https://master--qamarketplace.myvtex.com/_v/public/assets/v1/published/vtex.messages-templates@0.1.12/public/react/cdbfb2a8b730a7ee840752d7af7ddc1c.png\"\n                                            width=\"77px\" height=\"28px\"\n                                            style=\"display:block;outline:none;border:none;text-decoration:none\"\n                                            class=\"CToWUd\">\n                                        <p style=\"font-size:24px;color:#25354d;margin-bottom:32px\">\n                                            <strong>Planilha de pedidos de afiliados exportada</strong></p>\n                                        <p style=\"font-size:16px;color:#3f3f40;margin-bottom:32px\">\n                                            Olá,</p>\n                                        <p style=\"font-size:16px;color:#3f3f40\">\n                                            Segue o link para baixar a planilha pedidos de afiliados.\n                                        </p>\n                                        <div style=\"margin-bottom: 24px\">\n                                            <a href=\"{{link}}\" download>\n                                                <button\n                                                    style=\"border-width: .125rem; border-style: solid; font-weight: 500; vertical-align: middle; padding: 0; line-height: 1; border-radius: .25rem; min-height: 2.5rem;  box-sizing: border-box; font-family: Fabriga, -apple-system, BlinkMacSystemFont, avenir next, avenir, helvetica neue, helvetica, ubuntu, roboto, noto, segoe ui, arial, sans-serif;  font-size: 1rem;  text-transform: uppercase;  letter-spacing: 0; background-color: #134cd8; border-color: #134cd8;  color: #fff; cursor: pointer;\"\n                                                    type=\"button\">\n                                                    <div style=\"display: flex; align-items: center; justify-content: center; height: 100%; padding-left: 1.5rem; padding-right: 1.5rem; padding-top: 0.25rem; padding-bottom: 0.25rem;\">\n                                                        Baixar Planilha\n                                                    </div>\n                                                </button>\n                                            </a>\n                                        </div>\n                                        <p style=\"margin-bottom:4px;font-size:16px;color:#3f3f40\">\n                                            Abraços,</p>\n                                        <p style=\"margin-top:0px;font-size:16px;color:#3f3f40\">\n                                            VTEX</p><br>\n                                        <p style=\"font-size:12px;color:#727273;margin-bottom:0px\">\n                                            O link para download é válido por 24 horas. Após esse tempo, será necessário realizar a exportação novamente.\n                                        </p>\n                                        <div\n                                            style=\"color:#e3e4e6;border-top:1px solid #e3e4e6;border-bottom:0px solid #e3e4e6;margin-bottom:2rem;margin-top:1rem\">\n                                        </div>\n                                        <p style=\"font-size:12px;color:#727273;margin-bottom:0px\">\n                                            Esse email é enviado automaticamente e não recebe respostas.\n                                        </p>\n                                        <p style=\"font-size:12px;color:#727273;margin-top:.25rem;margin-bottom:0px\">\n                                            Precisa de ajuda? <a href=\"https://help.vtex.com/?locale=pt\" alt=\"VTEX Help\"\n                                                style=\"font-weight:bold;color:#3F3F40\">Fale Conosco</a>\n                                        </p><br>\n                                        <p style=\"font-size:12px;color:#727273;margin-bottom:0px\">\n                                            © VTEX Praia de Botafogo, 300, 3º Andar, Botafogo, Rio de Janeiro, RJ,\n                                            22250-040\n                                        </p>\n                                    </div>\n                                </td>\n                            </tr>\n                        </tbody>\n                    </table>\n                </td>\n            </tr>\n        </tbody>\n    </table>\n    <!--/600px container -->\n    <!--/100% wrapper-->\n</body>\n</html>",
      "language": "json"
    }

  ]
}
[/block]
<br>

**Commissions By Sku Export Template**
[block:code]
{
  "codes": [

    {
      "code": "<!DOCTYPE html>\n<html lang=\"pt-br\">\n\n<head>\n    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n    <meta name=\"viewport\" content=\"initial-scale=1.0\">\n    <!-- So that mobile webkit will display zoomed in -->\n    <meta name=\"format-detection\" content=\"telephone=no\">\n    <!-- disable auto telephone linking in iOS -->\n    <title>{{_accountInfo.TradingName}}</title>\n    <style type=\"text/css\">\n        p {\n            font-family: Fabriga, -apple-system, BlinkMacSystemFont, avenir next, avenir, helvetica neue, helvetica, ubuntu, roboto, noto, segoe ui, arial, sans-serif;\n        };\n        .vtex-button {\n            border-width: .125rem;\n            border-style: solid;\n            font-weight: 500;\n            vertical-align: middle;\n            padding: 0;\n            line-height: 1;\n            border-radius: .25rem;\n            min-height: 2.5rem;\n            box-sizing: border-box;\n            font-family: Fabriga, -apple-system, BlinkMacSystemFont, avenir next, avenir, helvetica neue, helvetica, ubuntu, roboto, noto, segoe ui, arial, sans-serif;\n            font-size: 1rem;\n            text-transform: uppercase;\n            letter-spacing: 0;\n            background-color: #134cd8;\n            border-color: #134cd8;\n            color: #fff;\n            cursor: pointer;\n        };\n    </style>\n</head>\n\n<body marginwidth=\"0\" marginheight=\"0\" bgcolor=\"#fff\" style=\"padding:0px 0px;color:#333;\" leftmargin=\"0\" topmargin=\"0\">\n    <!-- 100% wrapper (grey background) -->\n    <table width=\"100%\" height=\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\" align=\"left\" valign=\"top\">\n        <tbody>\n            <tr>\n                <td align=\"center\" valign=\"top\">\n                    <table width=\"100%\" style=\"max-width: 36rem;\" align=\"center\" cellpadding=\"0\" cellspacing=\"0\"\n                        border=\"0\" valign=\"top\">\n                        <tbody>\n                            <tr>\n                                <td>\n                                    <div\n                                        style=\"border:1px solid #e3e4e6;border-radius:8px;margin-top:1rem;margin-bottom:1rem;padding-top:3rem;padding-right:3rem;padding-bottom:3rem;padding-left:3rem\">\n                                        <img src=\"https://master--qamarketplace.myvtex.com/_v/public/assets/v1/published/vtex.messages-templates@0.1.12/public/react/cdbfb2a8b730a7ee840752d7af7ddc1c.png\"\n                                            width=\"77px\" height=\"28px\"\n                                            style=\"display:block;outline:none;border:none;text-decoration:none\"\n                                            class=\"CToWUd\">\n                                        <p style=\"font-size:24px;color:#25354d;margin-bottom:32px\">\n                                            <strong>Planilha de comissionamento por SKU exportada</strong></p>\n                                        <p style=\"font-size:16px;color:#3f3f40;margin-bottom:32px\">\n                                            Olá,</p>\n                                        <p style=\"font-size:16px;color:#3f3f40\">\n                                            Segue o link para baixar a planilha de comissionamento por SKU.\n                                        </p>\n                                        <div style=\"margin-bottom: 24px\">\n                                            <a href=\"{{link}}\" download>\n                                                <button\n                                                    style=\"border-width: .125rem; border-style: solid; font-weight: 500; vertical-align: middle; padding: 0; line-height: 1; border-radius: .25rem; min-height: 2.5rem;  box-sizing: border-box; font-family: Fabriga, -apple-system, BlinkMacSystemFont, avenir next, avenir, helvetica neue, helvetica, ubuntu, roboto, noto, segoe ui, arial, sans-serif;  font-size: 1rem;  text-transform: uppercase;  letter-spacing: 0; background-color: #134cd8; border-color: #134cd8;  color: #fff; cursor: pointer;\"\n                                                    type=\"button\">\n                                                    <div style=\"display: flex; align-items: center; justify-content: center; height: 100%; padding-left: 1.5rem; padding-right: 1.5rem; padding-top: 0.25rem; padding-bottom: 0.25rem;\">\n                                                        Baixar Planilha\n                                                    </div>\n                                                </button>\n                                            </a>\n                                        </div>\n                                        <p style=\"margin-bottom:4px;font-size:16px;color:#3f3f40\">\n                                            Abraços,</p>\n                                        <p style=\"margin-top:0px;font-size:16px;color:#3f3f40\">\n                                            VTEX</p><br>\n                                        <p style=\"font-size:12px;color:#727273;margin-bottom:0px\">\n                                            O link para download é válido por 24 horas. Após esse tempo, será necessário realizar a exportação novamente.\n                                        </p>\n                                        <div\n                                            style=\"color:#e3e4e6;border-top:1px solid #e3e4e6;border-bottom:0px solid #e3e4e6;margin-bottom:2rem;margin-top:1rem\">\n                                        </div>\n                                        <p style=\"font-size:12px;color:#727273;margin-bottom:0px\">\n                                            Esse email é enviado automaticamente e não recebe respostas.\n                                        </p>\n                                        <p style=\"font-size:12px;color:#727273;margin-top:.25rem;margin-bottom:0px\">\n                                            Precisa de ajuda? <a href=\"https://help.vtex.com/?locale=pt\" alt=\"VTEX Help\"\n                                                style=\"font-weight:bold;color:#3F3F40\">Fale Conosco</a>\n                                        </p><br>\n                                        <p style=\"font-size:12px;color:#727273;margin-bottom:0px\">\n                                            © VTEX Praia de Botafogo, 300, 3º Andar, Botafogo, Rio de Janeiro, RJ,\n                                            22250-040\n                                        </p>\n                                    </div>\n                                </td>\n                            </tr>\n                        </tbody>\n                    </table>\n                </td>\n            </tr>\n        </tbody>\n    </table>\n    <!--/600px container -->\n    <!--/100% wrapper-->\n</body>\n\n</html>",
      "language": "json"
    }

  ]
}
[/block]
