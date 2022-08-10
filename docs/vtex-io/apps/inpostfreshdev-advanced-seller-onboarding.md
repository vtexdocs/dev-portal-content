---
title: "onboarding-seller"
slug: "inpostfreshdev-advanced-seller-onboarding"
excerpt: "inpostfreshdev.advanced-seller-onboarding@0.0.1"
hidden: true
createdAt: "2022-07-14T10:35:36.787Z"
updatedAt: "2022-07-14T10:35:36.787Z"
---
Extends the default flow for inviting sellers

## Advanced Seller Onboarding Flow

![Onboarding Seller Flow](/docs/Marketplace_Seller_Onboarding.png "Onboarding Seller Flow")

## Configuration

1. Add the app as a theme peerDependency in the `manifest.json` file as vtexromania.advanced-seller-onboarding@1.x
2. Declare 4 new store routes in the `routes.json` file, ex:

```json
{
  "store.custom#seller-form": {
    "path": "/seller-form"
  },
  "store.custom#prelead-form": {
    "path": "/prelead-form/:invitationId"
  },
  "store.custom#vtex-terms": {
    "path": "/vtex-terms"
  },
  "store.custom#seller-terms-and-conditions": {
    "path": "/seller-terms-and-conditions"
  }
}
```

3. Use the `vtexromania.advanced-seller-onboarding` blocks in the new routes, using the `blocks.jsonc` file ex:

```json
{
  "store.custom#seller-form": {
    "blocks": [
      "onboarding-seller-form"
    ]
  },
  "store.custom#prelead-form": {
    "blocks": [
      "onboarding-prelead-form"
    ]
  }
}
```
    The other two pages need to be created in marketplace store-theme /blocks:
 ```json
{
    "store.custom#seller-terms-and-conditions": {
        "blocks": [
            "flex-layout.row#seller-terms-and-conditions"
        ]
      },
      "flex-layout.row#seller-terms-and-conditions": {
        "children": [
            "rich-text#seller-terms-and-conditions"
        ],
        "props": {
            "blockClass": "whiteBackgroundRow"
          }
      },
      "rich-text#seller-terms-and-conditions":{
          "props": {
              "title": "Terms and Conditions"
          }
      }
}
```   

 ```json
{
    "store.custom#vtex-terms": {
        "blocks": [
            "flex-layout.row#vtex-terms"
        ]
      },
      "flex-layout.row#vtex-terms": {
        "children": [
            "rich-text#vtex-terms"
        ],
        "props": {
            "blockClass": "whiteBackgroundRow"
          }
      },
      "rich-text#vtex-terms":{
          "props": {
              "title": "Vtex Conditions"
          }
      }
}   }
}
```   

4. Edit the prelead-form/:invitationId page in CMS as following:
- go to **Prelead-Form References** and add URL to Marketplace Guiding Page in the *Guide link* input

5. Create Terms and Conditions pages: With the page template **/seller-terms-and-conditions** you can create how many pages you need for you **Section of Terms and Conditions**. 
   - first go to Onboarding App Settings and complete the sections with *Page Name* and *Page URL*

![Set Terms and Conditions in App Settings](/docs/terms-and-conditions-1.png "Set Terms and Conditions in App Settings")

   - then go to Storefront -> Pages and Create new Page
   - it is mandatory to choose the template: **{{account}}.store-theme@0.x:store.custom#seller-terms-and-conditions**

![CMS Pages](/docs/terms-and-conditions-2.png "CMS Pages")
![CMS Create new page](/docs/terms-and-conditions-3.png "CMS Create new page")

Edit the terms and conditions pages pages in CMS as following:
- write text in MD format from Rand -> Text imbogatit
- for /vtex-terms page use the file from /docs folder: termeni-VTEX.md

6. Set the upload image link for /prelead-form here:

![Admin Settings](/docs/upload-image-settings.png "Upload Image Link")
You can use whatever link you need, but if left empty, the default image will be the one from the screenshot.

7. Fill in the Guide link for the end of the form /prelead-form  in **Prelead-Form references**

![Admin Settings](/docs/marketplace-guide.png "Upload Image Link")

8. Fill in the app [settings](#settings)

9. Create the schema

`PUT` in Postman

* **URL**
  `https://{{accountName}}.myvtex.com/_v/onboarding-seller/sellerSchema`

* **Method**
  `PUT` 

* **Body**

```json
{
  "token": "the same token as the one set in cron token Admin Settings"
}
```

10. Create the indices

`PUT` in Postman

* **URL**
  `https://{{accountName}}.myvtex.com/_v/onboarding-seller/sellerIndices`

* **Method**
  `PUT` 

* **Body**

```json
{
  "token": "the same token as the one set in cron token Admin Settings"
}
```

11.  Start the cron using the `POST` method. See the [cron section](#cron)

## Settings

The app has the following settings:

| Name                         | Description                                                          | Default     | Optional |
|------------------------------|----------------------------------------------------------------------|-------------|----------|
| Prelead form url             | The URL to use when sending the prelead email                        |     -       | no       |
| Login not found redirect url | The URL to redirect to when a seller login attempt fails             |     -       | no       |
| Seller type                  | White label sellers will not be shown to the users                   | Regular     | no       |
| Store Admin Name                 | The one to who the email is sent                   | -     | no       |
| Store Admin Email                 | The email address to be notificated by the marketplace                   | -     | no       |
| Seller-Info Template in HTML | The name of seller-info HTML template                                | seller-info | yes      |
| Image for uploading files | The seller's prelead-form has an upload image                                 | the image link | yes      |
| Terms and Conditions Pages | Each Page has Page title and Page URL                                 | - | yes      |
| Recaptcha keys               | Google recaptcha public & private key                                 |     -       | no       |
| Ip whitelist                 | List of IPs to allow on the public routes. Will allow all if not set | All IPs     | yes      |
| Cors whitelist               | List of domains for cors. Will allow all if not set                  | All domains | yes      |

## Cron

The cron is responsible with gathering seller data from various vtex services

* **URL**
  `https://{{accountName}}.myvtex.com/_v/onboarding-seller/cron`

* **Method**
  `POST` | `DELETE`

* **Body**

```json
{
  "token": "f1550189-fe9e-478a-a920-7fa446149367"
}
```

* **Success response**
  * `POST`:
    * Code: `201`
    * Content: `'Cron created'`
  * `DELETE`:
    * Code: `200`
    * Content: `'Cron deleted'`

* **Sample call**

```typescript
await axios({
  method: 'post' | 'delete',
  url: 'https://example.myvtex.com/_v/onboarding-seller/cron',
  data: {
    token: "MY_CRON_TOKEN",
  }
});
```
## Seller-Info HTML template
> * URL: `https://{{account}}.myvtex.com/_v/onboarding-seller/seller-html/:sellerAccountName`, where *sellerAccountName* is mandatory
> * GET method using Postman
> * Set up  `Seller-Info Template in HTML` variable from Admin Settings

> ## Create the HTML template with name **seller-info** IN /admin/message-center/

```
<html xmlns="http://www.w3.org/1999/xhtml">
 <center>
     <h1>Despre {{sellerAccount}}</h1>
     <p> {{sellerName}} </p>
     <h2>Informatii companie</h2>
     <p><b>Denumire companie:</b> {{sellerCompanyName}}</p>
     <p><b>Cod unic de înregistrare:</b> {{sellerCUI}}</p>
     <p><b>Nr. Reg. Comerțului:</b> {{sellerNrRegComert}}</p>
     <p><b>Descriere companie:</b> {{sellerDescription}}</p>
     <p><b>Politica de Retur:</b> {{exchangeReturnPolicy}}</p>
     <p><b>Politica de Livrare:</b> {{sellerDeliveryPolicy}}</p>
     <p><b>Politica de Confidentialitate:</b> {{sellerPrivacyPolicy}}</p>
 </center>
 </html>
 
```
## Email templates

The app also needs the following email templates to be set.

> Templates can be set in the admin message center:
> * Url: `{{account}}.myvtex.com/admin/message-center/#/templates`
> * Side menu: `Customer > Message Center > Templates`

The templates can be customized as seen in the [handlebars documentation](https://handlebarsjs.com/)

| Common variables | Type   | Description                 |
|------------------|--------|-----------------------------|
| `to.name`        | string | Name of the email recipient |
| `to.email`       | string | Address of the recipient    |

## **The following templates need to be created in marketplace**
## In admin/messages/templates

1. payu-id-success

| Variables | Description |
|---------- | ------------------------|
| ID  | payu-id-success |
| Nume   | payu_id_success           |
| Subject   | {{to.email}}           |
| CC   | -           |
| BCC   | -         |
| Sender   | Your company address      |

And an example of HTML (you can customize it how you wish):

```handlebars

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Puncte de fidelitate</title>
    <style type="text/css">
        /* ///////// CLIENT-SPECIFIC STYLES ///////// */

        #outlook a {
            padding: 0;
        }
        /* Force Outlook to provide a "view in browser" message */

        .ReadMsgBody {
            width: 100%;
        }

        .ExternalClass {
            width: 100%;
        }
        /* Force Hotmail to display emails at full width */

        .ExternalClass,
        .ExternalClass p,
        .ExternalClass span,
        .ExternalClass font,
        .ExternalClass td,
        .ExternalClass div {
            line-height: 100%;
        }
        /* Force Hotmail to display normal line spacing */

        body,
        table,
        td,
        p,
        a,
        li,
        blockquote {
            -webkit-text-size-adjust: 100%;
            -ms-text-size-adjust: 100%;
        }
        /* Prevent WebKit and Windows mobile changing default text sizes */

        table,
        td {
            mso-table-lspace: 0pt;
            mso-table-rspace: 0pt;
        }
        /* Remove spacing between tables in Outlook 2007 and up */

        img {
            -ms-interpolation-mode: bicubic;
        }
        /* Allow smoother rendering of resized image in Internet Explorer */
        /* ///////// RESET STYLES ///////// */

        body {
            margin: 0;
            padding: 0;
        }

        img {
            border: 0;
            height: auto;
            line-height: 100%;
            outline: none;
            text-decoration: none;
        }

        table {
            border-collapse: collapse;
        }

        body,
        #bodyTable,
        #bodyCell {
            height: 100%;
            margin: 0;
            padding: 0;
            width: 100%;
        }
        /* ///////// TEMPLATE STYLES ///////// */

        body {
            background-color: #e6e6e6;
            font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;
            font-size: 14px;
            color: #666666;
        }
        /* ///////// Gmail hack: ///////// */

        u+#new-gmail-hack {
            display: block !important;
        }
        /* ///////// yahoo hack: ///////// */

        table[align="center"] {
            margin: 0 auto;
        }

        @media only screen and (max-width: 480px) {
            .rwd-align {
                text-align: center !important;
                border-bottom: 1px solid #444444;
            }
            .col-half {
                width: 50% !important;
            }
        }
    </style>
</head>
<center>
    <div style="margin: 0; padding: 0; background-color:#e6e6e6;">
        <table cellpadding="0" cellspacing="0" border="0" style="border-collapse: collapse;padding:0px;margin:0px;width:100%;">
            <tr>
                <td colspan="3" style="padding:0px;margin:0px;font-size:14px;height:20px;" height="20">&nbsp;</td>
            </tr>
            <tr>
                <td style="padding:0px;margin:0px;">&nbsp;</td>
                <td style="padding:0px;margin:0px;" width="600">
                    <!-- DONT EDIT ABOVE THIS LINE -->



                    <!-- EMAIL DESIGN START -->
                    <table align="center" border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" style="border-collapse: collapse;margin: 0 auto; max-width:600px; width: 100%;border: 1px solid #e6e6e6;width:100%;">

                        <!-- CONTENT START -->
                        <tr>
                            <td align="left" valign="top">
                                <table border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse;max-width:600px; width: 100%; background-color: #ffffff; color:#666666;">
                                    <tr>
                                        <td valign="top" align="left" style="padding-top:30px; padding-right:20px; padding-bottom:30px; padding-left:20px;">
                                            <div>
                                                <h2 style="color:#000000; display:block; font-size:18px; font-style:normal; font-weight: bold; text-align:left; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;">
                                                    Salut,
                                                </h2>

                                                <p style="color:#666666; display:block; font-size:14px; font-style:normal; line-height:18px; text-align:left; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-top: 5px; padding-right: 0px; padding-bottom: 5px; padding-left: 0px;">
                                                    Ne bucurăm ca dorești să te alături comunității elefant.ro.

                                                    Pentru a continua procesul de înregistrare este necesară completarea formularului ce poate fi accesat din linkul de mai jos. Mulțumim!
                                                </p>
                                            </div>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                    <!-- EMAIL DESIGN END -->


                    <!-- DONT EDIT BELOW THIS LINE -->
                </td>
                <td style="padding:0px;margin:0px;">&nbsp;</td>
            </tr>
            <tr>
                <td colspan="3" style="padding:0px;margin:0px;font-size:14px;height:20px;" height="20">&nbsp;</td>
            </tr>
        </table>
    </div>
</center>

</html>

```

2. payu-id-error

| Variables | Description |
|---------- | ------------------------|
| ID  | payu-id-error |
| Nume   | payu_id_error           |
| Subject   | {{to.email}}           |
| CC   | -           |
| BCC   | -         |
| Sender   | Your company address      |

And an example of HTML (you can customize it how you wish):

```handlebars

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Puncte de fidelitate</title>
    <style type="text/css">
        /* ///////// CLIENT-SPECIFIC STYLES ///////// */

        #outlook a {
            padding: 0;
        }
        /* Force Outlook to provide a "view in browser" message */

        .ReadMsgBody {
            width: 100%;
        }

        .ExternalClass {
            width: 100%;
        }
        /* Force Hotmail to display emails at full width */

        .ExternalClass,
        .ExternalClass p,
        .ExternalClass span,
        .ExternalClass font,
        .ExternalClass td,
        .ExternalClass div {
            line-height: 100%;
        }
        /* Force Hotmail to display normal line spacing */

        body,
        table,
        td,
        p,
        a,
        li,
        blockquote {
            -webkit-text-size-adjust: 100%;
            -ms-text-size-adjust: 100%;
        }
        /* Prevent WebKit and Windows mobile changing default text sizes */

        table,
        td {
            mso-table-lspace: 0pt;
            mso-table-rspace: 0pt;
        }
        /* Remove spacing between tables in Outlook 2007 and up */

        img {
            -ms-interpolation-mode: bicubic;
        }
        /* Allow smoother rendering of resized image in Internet Explorer */
        /* ///////// RESET STYLES ///////// */

        body {
            margin: 0;
            padding: 0;
        }

        img {
            border: 0;
            height: auto;
            line-height: 100%;
            outline: none;
            text-decoration: none;
        }

        table {
            border-collapse: collapse;
        }

        body,
        #bodyTable,
        #bodyCell {
            height: 100%;
            margin: 0;
            padding: 0;
            width: 100%;
        }
        /* ///////// TEMPLATE STYLES ///////// */

        body {
            background-color: #e6e6e6;
            font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;
            font-size: 14px;
            color: #666666;
        }
        /* ///////// Gmail hack: ///////// */

        u+#new-gmail-hack {
            display: block !important;
        }
        /* ///////// yahoo hack: ///////// */

        table[align="center"] {
            margin: 0 auto;
        }

        @media only screen and (max-width: 480px) {
            .rwd-align {
                text-align: center !important;
                border-bottom: 1px solid #444444;
            }
            .col-half {
                width: 50% !important;
            }
        }
    </style>
</head>
<center>
    <div style="margin: 0; padding: 0; background-color:#e6e6e6;">
        <table cellpadding="0" cellspacing="0" border="0" style="border-collapse: collapse;padding:0px;margin:0px;width:100%;">
            <tr>
                <td colspan="3" style="padding:0px;margin:0px;font-size:14px;height:20px;" height="20">&nbsp;</td>
            </tr>
            <tr>
                <td style="padding:0px;margin:0px;">&nbsp;</td>
                <td style="padding:0px;margin:0px;" width="600">
                    <!-- DONT EDIT ABOVE THIS LINE -->



                    <!-- EMAIL DESIGN START -->
                    <table align="center" border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" style="border-collapse: collapse;margin: 0 auto; max-width:600px; width: 100%;border: 1px solid #e6e6e6;width:100%;">

                        <!-- CONTENT START -->
                        <tr>
                            <td align="left" valign="top">
                                <table border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse;max-width:600px; width: 100%; background-color: #ffffff; color:#666666;">
                                    <tr>
                                        <td valign="top" align="left" style="padding-top:30px; padding-right:20px; padding-bottom:30px; padding-left:20px;">
                                            <div>
                                                <h2 style="color:#000000; display:block; font-size:18px; font-style:normal; font-weight: bold; text-align:left; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;">
                                                    Salut,
                                                </h2>

                                                <p style="color:#666666; display:block; font-size:14px; font-style:normal; line-height:18px; text-align:left; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-top: 5px; padding-right: 0px; padding-bottom: 5px; padding-left: 0px;">
                                                    Ne bucurăm ca dorești să te alături comunității elefant.ro.

                                                    Pentru a continua procesul de înregistrare este necesară completarea formularului ce poate fi accesat din linkul de mai jos. Mulțumim!
                                                </p>
                                            </div>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                    <!-- EMAIL DESIGN END -->


                    <!-- DONT EDIT BELOW THIS LINE -->
                </td>
                <td style="padding:0px;margin:0px;">&nbsp;</td>
            </tr>
            <tr>
                <td colspan="3" style="padding:0px;margin:0px;font-size:14px;height:20px;" height="20">&nbsp;</td>
            </tr>
        </table>
    </div>
</center>

</html>

```

## In /admin/message-center/ create the following:

1. seller-email-in-use

| Variables | Type    | Description                                          |
|-----------|---------|------------------------------------------------------|
| rejected  | boolean | If true, the email address has already been rejected |
| formURL   | string  | Form url to display if rejected is false             |

```handlebars
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Puncte de fidelitate</title>
    <style type="text/css">
        /* /\/\/\/\/\/\/\/\/ CLIENT-SPECIFIC STYLES /\/\/\/\/\/\/\/\/ */

        #outlook a {
            padding: 0;
        }

        /* Force Outlook to provide a "view in browser" message */

        .ReadMsgBody {
            width: 100%;
        }

        .ExternalClass {
            width: 100%;
        }

        /* Force Hotmail to display emails at full width */

        .ExternalClass,
        .ExternalClass p,
        .ExternalClass span,
        .ExternalClass font,
        .ExternalClass td,
        .ExternalClass div {
            line-height: 100%;
        }

        /* Force Hotmail to display normal line spacing */

        body,
        table,
        td,
        p,
        a,
        li,
        blockquote {
            -webkit-text-size-adjust: 100%;
            -ms-text-size-adjust: 100%;
        }

        /* Prevent WebKit and Windows mobile changing default text sizes */

        table,
        td {
            mso-table-lspace: 0pt;
            mso-table-rspace: 0pt;
        }

        /* Remove spacing between tables in Outlook 2007 and up */

        img {
            -ms-interpolation-mode: bicubic;
        }

        /* Allow smoother rendering of resized image in Internet Explorer */
        /* /\/\/\/\/\/\/\/\/ RESET STYLES /\/\/\/\/\/\/\/\/ */

        body {
            margin: 0;
            padding: 0;
        }

        img {
            border: 0;
            height: auto;
            line-height: 100%;
            outline: none;
            text-decoration: none;
        }

        table {
            border-collapse: collapse;
        }

        body,
        #bodyTable,
        #bodyCell {
            height: 100%;
            margin: 0;
            padding: 0;
            width: 100%;
        }

        /* /\/\/\/\/\/\/\/\/ TEMPLATE STYLES /\/\/\/\/\/\/\/\/ */

        body {
            background-color: #e6e6e6;
            font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;
            font-size: 14px;
            color: #666666;
        }

        /* /\/\/\/\/\/\/\/\/ Gmail hack: /\/\/\/\/\/\/\/\/ */

        u + #new-gmail-hack {
            display: block !important;
        }

        /* /\/\/\/\/\/\/\/\/ yahoo hack: /\/\/\/\/\/\/\/\/ */

        table[align="center"] {
            margin: 0 auto;
        }

        @media only screen and (max-width: 480px) {
            .rwd-align {
                text-align: center !important;
                border-bottom: 1px solid #444444;
            }

            .col-half {
                width: 50% !important;
            }
        }
    </style>
</head>
<center>
    <div style="margin: 0; padding: 0; background-color:#e6e6e6;">
        <table cellpadding="0" cellspacing="0" border="0"
               style="border-collapse: collapse;padding:0px;margin:0px;width:100%;">
            <tr>
                <td colspan="3" style="padding:0px;margin:0px;font-size:14px;height:20px;" height="20">&nbsp;</td>
            </tr>
            <tr>
                <td style="padding:0px;margin:0px;">&nbsp;</td>
                <td style="padding:0px;margin:0px;" width="600">
                    <!-- DONT EDIT ABOVE THIS LINE -->


                    <!-- EMAIL DESIGN START -->
                    <table align="center" border="0" cellpadding="0" cellspacing="0" height="100%" width="100%"
                           style="border-collapse: collapse;margin: 0 auto; max-width:600px; width: 100%;border: 1px solid #e6e6e6;width:100%;">

                        <!-- CONTENT START -->
                        <tr>
                            <td align="left" valign="top">
                                <table border="0" cellpadding="0" cellspacing="0"
                                       style="border-collapse: collapse;max-width:600px; width: 100%; background-color: #ffffff; color:#666666;">
                                    <tr>
                                        <td valign="top" align="left"
                                            style="padding-top:30px; padding-right:20px; padding-bottom:30px; padding-left:20px;">
                                            <div>
                                                <h2 style="color:#000000; display:block; font-size:18px; font-style:normal; font-weight: bold; text-align:left; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;">
                                                    Salut,
                                                </h2>

                                                {{#if rejected}}

                                                    <p style="color:#666666; display:block; font-size:14px; font-style:normal; line-height:18px; text-align:left; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-top: 5px; padding-right: 0px; padding-bottom: 5px; padding-left: 0px;">
                                                        Ne pare rau, dar cererea ta de inregistrare a fost refuzata
                                                        anterior! Procesul de inregistrare nu poate fi continuat.
                                                    </p>


                                                {{else}}

                                                    <p style="color:#666666; display:block; font-size:14px; font-style:normal; line-height:18px; text-align:left; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-top: 5px; padding-right: 0px; padding-bottom: 5px; padding-left: 0px;">
                                                        Acest email a mai fost utilizat pentru a porni un proces de
                                                        onboarding. Utilizeaza formularul de mai jos pentru a finaliza
                                                        procesul.
                                                    </p>

                                                    <h3 style="text-align:center;">
                                                        <a href={{formURL}}>Formular</a>
                                                    </h3>

                                                {{/if}}
                                            </div>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                    <!-- EMAIL DESIGN END -->


                    <!-- DONT EDIT BELOW THIS LINE -->
                </td>
                <td style="padding:0px;margin:0px;">&nbsp;</td>
            </tr>
            <tr>
                <td colspan="3" style="padding:0px;margin:0px;font-size:14px;height:20px;" height="20">&nbsp;</td>
            </tr>
        </table>
    </div>
</center>

</html>
```

2. onboarding-seller-response

| Variables | Type                   | Description                                                                                                  |
|-----------|------------------------|--------------------------------------------------------------------------------------------------------------|
| message   | string &#124; optional | Feedback message from the admin operator                                                                     |
| isSoft    | boolean                | If the invitation has been soft rejected this will be set to true. A false value means this is a hard reject |

```handlebars
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Puncte de fidelitate</title>
    <style type="text/css">
        /* /\/\/\/\/\/\/\/\/ CLIENT-SPECIFIC STYLES /\/\/\/\/\/\/\/\/ */

        #outlook a {
            padding: 0;
        }

        /* Force Outlook to provide a "view in browser" message */

        .ReadMsgBody {
            width: 100%;
        }

        .ExternalClass {
            width: 100%;
        }

        /* Force Hotmail to display emails at full width */

        .ExternalClass,
        .ExternalClass p,
        .ExternalClass span,
        .ExternalClass font,
        .ExternalClass td,
        .ExternalClass div {
            line-height: 100%;
        }

        /* Force Hotmail to display normal line spacing */

        body,
        table,
        td,
        p,
        a,
        li,
        blockquote {
            -webkit-text-size-adjust: 100%;
            -ms-text-size-adjust: 100%;
        }

        /* Prevent WebKit and Windows mobile changing default text sizes */

        table,
        td {
            mso-table-lspace: 0pt;
            mso-table-rspace: 0pt;
        }

        /* Remove spacing between tables in Outlook 2007 and up */

        img {
            -ms-interpolation-mode: bicubic;
        }

        /* Allow smoother rendering of resized image in Internet Explorer */
        /* /\/\/\/\/\/\/\/\/ RESET STYLES /\/\/\/\/\/\/\/\/ */

        body {
            margin: 0;
            padding: 0;
        }

        img {
            border: 0;
            height: auto;
            line-height: 100%;
            outline: none;
            text-decoration: none;
        }

        table {
            border-collapse: collapse;
        }

        body,
        #bodyTable,
        #bodyCell {
            height: 100%;
            margin: 0;
            padding: 0;
            width: 100%;
        }

        /* /\/\/\/\/\/\/\/\/ TEMPLATE STYLES /\/\/\/\/\/\/\/\/ */

        body {
            background-color: #e6e6e6;
            font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;
            font-size: 14px;
            color: #666666;
        }

        /* /\/\/\/\/\/\/\/\/ Gmail hack: /\/\/\/\/\/\/\/\/ */

        u + #new-gmail-hack {
            display: block !important;
        }

        /* /\/\/\/\/\/\/\/\/ yahoo hack: /\/\/\/\/\/\/\/\/ */

        table[align="center"] {
            margin: 0 auto;
        }

        @media only screen and (max-width: 480px) {
            .rwd-align {
                text-align: center !important;
                border-bottom: 1px solid #444444;
            }

            .col-half {
                width: 50% !important;
            }
        }
    </style>
</head>
<center>
    <div style="margin: 0; padding: 0; background-color:#e6e6e6;">
        <table cellpadding="0" cellspacing="0" border="0"
               style="border-collapse: collapse;padding:0px;margin:0px;width:100%;">
            <tr>
                <td colspan="3" style="padding:0px;margin:0px;font-size:14px;height:20px;" height="20">&nbsp;</td>
            </tr>
            <tr>
                <td style="padding:0px;margin:0px;">&nbsp;</td>
                <td style="padding:0px;margin:0px;" width="600">
                    <!-- DONT EDIT ABOVE THIS LINE -->


                    <!-- EMAIL DESIGN START -->
                    <table align="center" border="0" cellpadding="0" cellspacing="0" height="100%" width="100%"
                           style="border-collapse: collapse;margin: 0 auto; max-width:600px; width: 100%;border: 1px solid #e6e6e6;width:100%;">

                        <!-- CONTENT START -->
                        <tr>
                            <td align="left" valign="top">
                                <table border="0" cellpadding="0" cellspacing="0"
                                       style="border-collapse: collapse;max-width:600px; width: 100%; background-color: #ffffff; color:#666666;">
                                    <tr>
                                        <td valign="top" align="left"
                                            style="padding-top:30px; padding-right:20px; padding-bottom:30px; padding-left:20px;">
                                            <div>
                                                <h2 style="color:#000000; display:block; font-size:18px; font-style:normal; font-weight: bold; text-align:left; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;">
                                                    Salut,
                                                </h2>

                                                <p style="color:#666666; display:block; font-size:14px; font-style:normal; line-height:18px; text-align:left; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-top: 5px; padding-right: 0px; padding-bottom: 5px; padding-left: 0px;">
                                                    Ne pare rau, dar cererea ta de inregistrare a fost refuzata!
                                                </p>

                                                {{#if message}}

                                                    <h4>
                                                        Motiv:
                                                    </h4>

                                                    <p style="color:#666666; display:block; font-size:14px; font-style:normal; line-height:18px; text-align:left; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-right: 0px; padding-bottom: 5px; padding-left: 0px;">
                                                        {{message}}
                                                    </p>

                                                {{/if}}

                                                {{#if isSoft}}

                                                    <p style="color:#666666; display:block; font-size:14px; font-style:normal; line-height:18px; text-align:left; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-top: 5px; padding-right: 0px; padding-bottom: 5px; padding-left: 0px;">
                                                        Pentru a putea continua procesul de intregistrare recompleteaza
                                                        formularul trimis anterior.
                                                    </p>

                                                    <h3 style="text-align:center;">
                                                        <a href={{formURL}}>Formular</a>
                                                    </h3>

                                                {{else}}

                                                    <p style="color:#666666; display:block; font-size:14px; font-style:normal; line-height:18px; text-align:left; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-top: 5px; padding-right: 0px; padding-bottom: 5px; padding-left: 0px;">
                                                        Refuzul este final si procesul de inregistrare nu mai poate fi
                                                        continuat!
                                                    </p>

                                                {{/if}}
                                            </div>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                    <!-- EMAIL DESIGN END -->


                    <!-- DONT EDIT BELOW THIS LINE -->
                </td>
                <td style="padding:0px;margin:0px;">&nbsp;</td>
            </tr>
            <tr>
                <td colspan="3" style="padding:0px;margin:0px;font-size:14px;height:20px;" height="20">&nbsp;</td>
            </tr>
        </table>
    </div>
</center>

</html>
```

3. seller-prelead

| Variables | Type    | Description                             |
|-----------|---------|-----------------------------------------|
| formURL   | string | Prelead form URL for the user to access |

```handlebars
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Puncte de fidelitate</title>
    <style type="text/css">
        /* /\/\/\/\/\/\/\/\/ CLIENT-SPECIFIC STYLES /\/\/\/\/\/\/\/\/ */

        #outlook a {
            padding: 0;
        }

        /* Force Outlook to provide a "view in browser" message */

        .ReadMsgBody {
            width: 100%;
        }

        .ExternalClass {
            width: 100%;
        }

        /* Force Hotmail to display emails at full width */

        .ExternalClass,
        .ExternalClass p,
        .ExternalClass span,
        .ExternalClass font,
        .ExternalClass td,
        .ExternalClass div {
            line-height: 100%;
        }

        /* Force Hotmail to display normal line spacing */

        body,
        table,
        td,
        p,
        a,
        li,
        blockquote {
            -webkit-text-size-adjust: 100%;
            -ms-text-size-adjust: 100%;
        }

        /* Prevent WebKit and Windows mobile changing default text sizes */

        table,
        td {
            mso-table-lspace: 0pt;
            mso-table-rspace: 0pt;
        }

        /* Remove spacing between tables in Outlook 2007 and up */

        img {
            -ms-interpolation-mode: bicubic;
        }

        /* Allow smoother rendering of resized image in Internet Explorer */
        /* /\/\/\/\/\/\/\/\/ RESET STYLES /\/\/\/\/\/\/\/\/ */

        body {
            margin: 0;
            padding: 0;
        }

        img {
            border: 0;
            height: auto;
            line-height: 100%;
            outline: none;
            text-decoration: none;
        }

        table {
            border-collapse: collapse;
        }

        body,
        #bodyTable,
        #bodyCell {
            height: 100%;
            margin: 0;
            padding: 0;
            width: 100%;
        }

        /* /\/\/\/\/\/\/\/\/ TEMPLATE STYLES /\/\/\/\/\/\/\/\/ */

        body {
            background-color: #e6e6e6;
            font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;
            font-size: 14px;
            color: #666666;
        }

        /* /\/\/\/\/\/\/\/\/ Gmail hack: /\/\/\/\/\/\/\/\/ */

        u + #new-gmail-hack {
            display: block !important;
        }

        /* /\/\/\/\/\/\/\/\/ yahoo hack: /\/\/\/\/\/\/\/\/ */

        table[align="center"] {
            margin: 0 auto;
        }

        @media only screen and (max-width: 480px) {
            .rwd-align {
                text-align: center !important;
                border-bottom: 1px solid #444444;
            }

            .col-half {
                width: 50% !important;
            }
        }
    </style>
</head>
<center>
    <div style="margin: 0; padding: 0; background-color:#e6e6e6;">
        <table cellpadding="0" cellspacing="0" border="0"
               style="border-collapse: collapse;padding:0px;margin:0px;width:100%;">
            <tr>
                <td colspan="3" style="padding:0px;margin:0px;font-size:14px;height:20px;" height="20">&nbsp;</td>
            </tr>
            <tr>
                <td style="padding:0px;margin:0px;">&nbsp;</td>
                <td style="padding:0px;margin:0px;" width="600">
                    <!-- DONT EDIT ABOVE THIS LINE -->


                    <!-- EMAIL DESIGN START -->
                    <table align="center" border="0" cellpadding="0" cellspacing="0" height="100%" width="100%"
                           style="border-collapse: collapse;margin: 0 auto; max-width:600px; width: 100%;border: 1px solid #e6e6e6;width:100%;">

                        <!-- CONTENT START -->
                        <tr>
                            <td align="left" valign="top">
                                <table border="0" cellpadding="0" cellspacing="0"
                                       style="border-collapse: collapse;max-width:600px; width: 100%; background-color: #ffffff; color:#666666;">
                                    <tr>
                                        <td valign="top" align="left"
                                            style="padding-top:30px; padding-right:20px; padding-bottom:30px; padding-left:20px;">
                                            <div>
                                                <h2 style="color:#000000; display:block; font-size:18px; font-style:normal; font-weight: bold; text-align:left; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;">
                                                    Salut,
                                                </h2>

                                                <p style="color:#666666; display:block; font-size:14px; font-style:normal; line-height:18px; text-align:left; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-top: 5px; padding-right: 0px; padding-bottom: 5px; padding-left: 0px;">
                                                    Ne bucurăm ca dorești să te alături comunității noastre.

                                                    Pentru a continua procesul de înregistrare este necesară completarea
                                                    formularului ce poate fi accesat din linkul de mai jos. Mulțumim!
                                                </p>

                                                <h3 style="text-align:center;">
                                                    <a href={{formURL}}>Formular</a>
                                                </h3>
                                            </div>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                    <!-- EMAIL DESIGN END -->


                    <!-- DONT EDIT BELOW THIS LINE -->
                </td>
                <td style="padding:0px;margin:0px;">&nbsp;</td>
            </tr>
            <tr>
                <td colspan="3" style="padding:0px;margin:0px;font-size:14px;height:20px;" height="20">&nbsp;</td>
            </tr>
        </table>
    </div>
</center>

</html>
```

4. seller-invite

| Variables | Type    | Description                             |
|-----------|---------|-----------------------------------------|
| createAccountLink   | string | VTEX redirect link to Account Creation |
| _accountInfo.TradingName   | string | The Marketplace's Name |
| PayU Marketplace Redirect Link  | string | In the 'CREEAZĂ UN CONT PAYU' href section |

```handlebars
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office"
  xmlns:v="urn:schemas-microsoft-com:vml">

<head>
  <!--[if mso]>
    <xml>
      <o:OfficeDocumentSettings>
        <o:AllowPNG/>
        <o:PixelsPerInch>96</o:PixelsPerInch>
      </o:OfficeDocumentSettings>
    </xml>
  <![endif]-->
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="x-apple-disable-message-reformatting" />
  <!-- So that mobile webkit will display zoomed in -->
  <meta name="format-detection" content="telephone=no" />
  <!-- disable auto telephone linking in iOS -->
  <!--[if !mso]><!-->
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <!--<![endif]-->
  <title>{{_accountInfo.TradingName}}</title>
  <style type="text/css">
    /****** Client Specific Styles Start ******/
    /****** Outlook.com / Hotmail
      ******/
    .ExternalClass {
      width: 100%;
    }

    .ExternalClass,
    .ExternalClass p,
    .ExternalClass span,
    .ExternalClass font,
    .ExternalClass td,
    .ExternalClass div {
      line-height: 100%;
    }

    /****** “Read in Browser” Link
      ******/
    #outlook a {
      padding: 0;
    }

    /****** <table> Element Spacing ******/
    table {
      mso-table-lspace: 0pt;
      mso-table-rspace: 0pt;
    }

    /****** Image
      Resizing ******/
    img {
      -ms-interpolation-mode: bicubic;
    }

    /****** Prevent
      WebKit and Windows Mobile changing default text sizes ******/
    body {
      -webkit-text-size-adjust: 100%;
      -ms-text-size-adjust: 100%;
    }

    /******
      Client Specific Styles End ******/
    body {
      -webkit-text-size-adjust: none;
      -ms-text-size-adjust: none;
    }

    body {
      margin: 0;
      padding: 0;
    }

    table td {
      border-collapse: collapse;
    }

    .yshortcuts a {
      border-bottom: none !important;
    }

    .gs li {
      margin-left: 15px;
    }
  </style>
</head>

<body marginwidth="0" marginheight="0" style="padding:0; color: #1a1a1a;" leftmargin="0" topmargin="0">
  <!-- 100% wrapper (grey background) -->
  <table width="100%" cellspacing="0" border="0" bgcolor="#fff">
    <tbody>
      <tr>
        <td valign="top" align="center"
          style="background-color: #ffffff; color:#1a1a1a; font-family: Arial, sans-serif !important; border-spacing: 0;">
          <!-- 600px container (white background) -->
          <table cellspacing="0" cellpadding="0" border="0" width="100%" style="max-width:600px;">
            <tbody>
              <tr>
                <td align="center"
                  style="padding-top: 8%; padding-bottom: 4.75%; padding-left: 16px; padding-right: 16px;
                background-image: url(https://elefant.vteximg.com.br/arquivos/header-wave.png);background-size:100% auto; background-repeat: no-repeat;">
                  <table width="100%" cellspacing="0" cellpadding="0" border="0"
                    style="border-spacing: 0; max-width: 426px;">
                    <tbody>
                      <tr>
                        <td align="left">
                          <a href="https://www.elefant.ro/" target="_blank" title="Elefant Marketplace"
                            style="display: block;">
                            <img src="https://elefant.vteximg.com.br/arquivos/logo.png" alt="Elefant Marketplace"
                              style="display:block" width="150" height="29" />
                          </a>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </td>
              </tr>
              <tr>
                <td align="center"
                  style="padding-top: 32px; padding-bottom: 40px; padding-left: 16px; padding-right: 16px;">
                  <table width="100%" cellspacing="0" cellpadding="0" border="0" align="center"
                    style="border-spacing: 0; max-width: 426px;">
                    <tbody>
                      <tr>
                        <td align="left"
                          style="font-size: 18px; font-weight: bold; line-height: 20px; padding-bottom: 10px;">
                          Felicitări! Cererea ta a fost aprobată!
                        </td>
                      </tr>
                      <tr>
                        <td style="font-size: 14px; line-height: 22px;">
                          Ca să te poți numi oficial Partener Elefant Marketplace, mai trebuie doar să-ți creezi un cont
                          aici:
                        </td>
                      </tr>
                      <tr>
                        <td aria-hidden="true" height="26" style="font-size: 0; line-height: 0;">
                          &nbsp;
                        </td>
                      </tr>
                      <tr>
                        <td>
                          <a href="{{createAccountLink}}" title="CREEAZĂ UN CONT"
                            style="display: inline-block; text-decoration: none; border-radius: 6px;  border-top: 9px solid #7531D6; border-bottom: 9px solid #7531D6; border-left: 48px solid #7531D6; border-right: 48px solid #7531D6;
                              border-style: solid; font-size: 11px; line-height: 15px; color: #ffffff; background-color: #7531D6;">CREEAZĂ UN CONT</a>
                        </td>
                      </tr>
                      <tr>
                        <td aria-hidden="true" height="32" style="font-size: 0; line-height: 0;">
                          &nbsp;
                        </td>
                      </tr>
                      <tr>
                        <td style="font-size: 14px; line-height: 22px; padding-bottom: 10px;">
                          Înscrie-te și dă startul vânzărilor pe markeplace-ul nostru.
                        </td>
                      </tr>
                      <tr>
                        <td>
                          <ul style="font-size: 14px; line-height: 22px; margin:0; margin-left: 16px; padding: 0;">
                            <li>Ai grijă, linkul este valid doar 7 zile.</li>
                            <li>Din motive de securitate, procesul de înregistrare nu poate avea întreruperi.</li>
                            <li>Dacă întâmpini probleme, ne poți cere un alt link spre marketplace.</li>
                          </ul>
                        </td>
                      </tr>
                      <tr>
                        <td aria-hidden="true" height="32" style="font-size: 0; line-height: 0;">
                          &nbsp;
                        </td>
                      </tr>
                      <tr>
                        <td style="font-size: 14px; line-height: 22px;">
                          Pentru a finaliza înscrierea, nu uita să-ți creezi un cont de PayU prin care să poți procesa plățile:
                        </td>
                      </tr>
                      <tr>
                        <td aria-hidden="true" height="26" style="font-size: 0; line-height: 0;">
                          &nbsp;
                        </td>
                      </tr>
                      <tr>
                        <td>  
                          <a title="CREEAZĂ UN CONT PAYU" target="_blank" href="google.com" 
                            style="display: inline-block; text-decoration: none; border-radius: 6px;  border-top: 9px solid #7531D6; border-bottom: 9px solid #7531D6; border-left: 48px solid #7531D6; border-right: 48px solid #7531D6;
                              border-style: solid; font-size: 11px; line-height: 15px; color: #ffffff; background-color: #7531D6;">CREEAZĂ UN CONT</a>
                        </td>
                      </tr>
                      <tr>
                        <td style="font-size: 18px; font-weight: bold; line-height: 20px; padding-top: 16px;">
                          Mulțumim!
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </td>
              </tr>
              <tr>
                <td align="center"
                  style="background-color: #7DD220; padding-top: 12px; padding-bottom: 10px; padding-left: 16px; padding-right: 16px;
                background-image: url(https://elefant.vteximg.com.br/arquivos/footer-wave2.png);background-size: auto 100%; background-repeat: no-repeat; background-position: center bottom;">
                  <table cellspacing="0" cellpadding="0" border="0" align="center"
                    style="border-spacing: 0; max-width: 426px;">
                    <tbody>
                      <tr>
                        <td align="center">
                          <table cellspacing="0" cellpadding="0" border="0" align="center" style="border-spacing: 0;">
                            <tbody>
                              <tr>
                                <td width="31">
                                  <a title="Facebook" target="_blank" href="https://www.facebook.com/elefant.ro"
                                    style="text-decoration: none;">
                                    <img src="https://elefant.vteximg.com.br/arquivos/facebook.png" width="17"
                                      height="17" alt="Elefant" />
                                  </a>
                                </td>
                                <td width="31">
                                  <a title="Instagram" target="_blank" href="https://www.instagram.com/elefantro"
                                    style="text-decoration: none;">
                                    <img src="https://elefant.vteximg.com.br/arquivos/instagram.png" width="17"
                                      height="17" alt="Elefant" />
                                  </a>
                                </td>
                                <td width="31">
                                  <a title="Linkedin" target="_blank" href="https://www.linkedin.com/company/elefantro"
                                    style="text-decoration: none;">
                                    <img src="https://elefant.vteximg.com.br/arquivos/linkedin.png" width="17"
                                      height="17" alt="Elefant" />
                                  </a>
                                </td>
                                <td>
                                  <a title="Telegram" target="_blank" href="https://telegram.org/"
                                    style="text-decoration: none;">
                                    <img src="https://elefant.vteximg.com.br/arquivos/telegram.png" width="17"
                                      height="17" alt="Elefant" />
                                  </a>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                      <tr>
                        <td align="center"
                          style="padding-top: 5px; font-size: 8px !important; line-height: 1.5 !important;">
                          Elefant Online SA. Toate drepturile rezervate.
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
    </tbody>
  </table>
  <!--/600px container -->
  <!--/100% wrapper-->
</body>

</html>
```

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe
on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization)
.

| CSS Handles |
| ----------- |
| `container` |
| `form`      |
| `title`     |


## Public Seller Page

Tha app expose a seller page on url "{basePath}/seller/:slug" where :slug is of format ${sellerId}-${searchSlugify(sellerName)}.
(Ex.: {basePath}/seller/test227-Test where test227 is the id of the seller and Test is the name)

The app expose two possible approaches to retrieve public seller data:

 Graphql: 
  - with the signature existent in schema.graphql (Ex.: getSeller(id: String): Seller)
  - return a body with public info
 REST Endpoint:
  - with path "${basePath}/_v/onboarding-seller/seller/:sellerAccountName" where :sellerAccountName is the sellerId (= account identifier in vtex)
  - return a body with array of matched seller with public info