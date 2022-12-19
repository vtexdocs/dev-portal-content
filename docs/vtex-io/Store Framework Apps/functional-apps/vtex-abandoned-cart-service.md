---
title: "Abandoned Cart Service"
slug: "vtex-abandoned-cart-service"
excerpt: "vtex.abandoned-cart-service@3.1.4"
hidden: false
createdAt: "2022-08-05T15:20:02.558Z"
updatedAt: "2022-08-10T21:32:18.857Z"
---
The Abandoned Cart Service app can be used to trigger abandoned cart emails.

### Usage

To use it in your account, run the `vtex install vtex.abandoned-cart-service` command.

You should follow the documentation to [Setting up Cart Abandonment (Trigger)](https://help.vtex.com/tutorial/setting-up-abandoned-carts--tutorials_740) but in the Action tab you should select Send an HTTP Request with the follow configuration:

- The URL field is https://{{account}}.myvtex.com/_v/abandoned-cart.
- Method field is POST.
- Header fields:
  ```html
  content-type: application/json
  accept: application/json
  ```
- Content as JSON field:

```json
{
  "email": "{!email}",
  "skuURL": "{!rclastcart}",
  "template": "vtexcommerce-abandoned-cart",
  "additionalFields": {
    // In object you can add any additional field to send in the mail
    "firstName": "{!firstName}"
  }
}
```
Like the example bellow:
<img width="1440" alt="Captura de Tela 2022-08-03 às 17 51 51" src="https://user-images.githubusercontent.com/67066494/184005464-d06e1cda-3b21-42ec-b020-d85d684e6b7c.png"/>


_The template field in the JSON above depends on the template id configured in the message center_

The app installation should automatically generate a new template in the message center with the id vtexcommerce-abandoned-cart and this can be edited to create the desired template. To style the email the following json can be used as an example of JSON Data:

```json
{
	"email": "teste@vtex.com.br",
	"items": [
		{
			"id": "880010",
			"productName": "adidas Men's Performance Polo - Blast Blue S",
			"image": "https://bibi.vteximg.com.br/arquivos/ids/155405/adidas-mens-performance-polo-blast-blue.jpg?v=637947886549170000",
			"sellingPrice": "455.00",
			"quantity": "1",
			"link": "adidas-mens-performance-polo-blast-blue",
			"availabilityQuantity": 1000000
		}
	],
	"addToCartURL": "add?sku=880010&qty=1&seller=1&sc=1",
	"additionalFields": {
		"firstName": "Teste VTEX"
	},
	"_accountInfo": {
		"MainAccountName": "teste",
		"AccountName": "teste",
		"Cnpj": null,
		"Id": "278fe15c-f0eb-4c30-81a2-f42b29113f1a",
		"AppId": null,
		"IsActive": true,
		"IsOperating": false,
		"CreationDate": "2022-06-21T19:58:01.3387095Z",
		"OperationDate": null,
		"CompanyName": "Companhia Brasileira de Tecnologia para ecommerce",
		"TradingName": "VTEX",
		"City": null,
		"Complement": null,
		"Country": null,
		"State": null,
		"Address": null,
		"District": null,
		"Number": null,
		"PostalCode": null,
		"Licenses": [
			7
		],
		"ParentAccountId": null,
		"ParentAccountName": null,
		"InactivationDate": null,
		"Platform": "vtex",
		"Privacy": null,
		"HasPiiRestriction": false,
		"Infra": null
	}
}
```

You can use the following template as an example:

```html
<!DOCTYPE html
PUBLIC"-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:v="urn:schemas-microsoft-com:vml"
style="-webkit-text-size-adjust:100%; -ms-text-size-adjust: 100%; -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; box-sizing: border-box; width: 100%;height:100%; margin: 0; padding: 0; background: #f1f1f1!important;">

<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{{_accountInfo.TradingName}}</title>
<!--[if gte mso 9]>
<xml>
<o:OfficeDocumentSettings>
<o:AllowPNG/>
<o:PixelsPerInch>96</o:PixelsPerInch>
</o:OfficeDocumentSettings>
</xml>
<![endif]-->
<style>
a[x-apple-data-detectors] {
color: inherit !important;
text-decoration: none!important;
font-size:inherit!important;
font-family:inherit!important;
font-weight:inherit!important;
line-height:inherit!important;
}
</style>
<style>
@media(max-width:600px){

img{
max-width:100%!important;
height: auto!important;
}
}
</style>
<style>
@media screen and (min-width:30em){

.w-50-ns{
width:50%!important;
}

.pr4-ns{
padding-right:2rem!important;
}

.ph4-ns{
padding-left:2rem!important;
padding-right:2rem!important;
}

.mv1-ns{
margin-top:.25rem!important;
margin-bottom:.25rem!important;
}

.mv4-ns{
margin-top:2rem!important;
margin-bottom:2rem!important;
}
}
</style>
</head>

<body
style="-webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; box-sizing: border-box; width: 100%; height: 100%; margin: 0; padding: 0; background: #f1f1f1 !important; font-family: -apple-system, BlinkMacSystemFont, '''Segoe UI''', Roboto, Helvetica, Arial, sans-serif;">
<table width="100%" border="0" cellpadding="0" cellspacing="0"
style="box-sizing: border-box; margin: 0; padding: 0; background: #f1f1f1; border-collapse: collapse; border-spacing: 0; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-family: -apple-system, BlinkMacSystemFont, '''Segoe UI''', Roboto, Helvetica, Arial, sans-serif; width: 100%; height: 100%; line-height: 100% !important;">
<tr style="box-sizing: border-box !important;">
<td align="left" valign="top"
style="font-size: 14px; line-height: 20px; box-sizing: border-box; border-collapse: collapse; text-align: left !important; font-family: -apple-system, BlinkMacSystemFont, '''Segoe UI''', Roboto, Helvetica, Arial, sans-serif;">
<table class="mv4-ns" width="100%" align="center" border="0" cellpadding="0" cellspacing="0"
style="box-sizing: border-box; max-width: 40rem; width: 100%; background-color: #fff; border-collapse: collapse; border-spacing: 0; mso-table-lspace: 0pt; mso-table-rspace: 0pt !important; font-family: -apple-system, BlinkMacSystemFont, '''Segoe UI''', Roboto, Helvetica, Arial, sans-serif;"
bgcolor="#fff">

<tr style="box-sizing: border-box !important;">
<td class="ph4-ns"
style="font-size: 14px; line-height: 20px; box-sizing: border-box; border-collapse: collapse; border-bottom-style: solid; border-bottom-width: 1px; border-color: #eee; width: 100%; padding-bottom: 2rem; text-align: center !important; font-family: -apple-system, BlinkMacSystemFont, '''Segoe UI''', Roboto, Helvetica, Arial, sans-serif;"
align="center">
<div
style="box-sizing: border-box; width: 8rem; margin-bottom: 1rem; margin-top: 2rem; margin-right: auto; margin-left: auto !important;">
<a href="http://{{_accountInfo.HostName}}.com.br" style="box-sizing: border-box !important;">
<img alt="" border="0" width="auto"
src="http://licensemanager.vtex.com.br/api/site/pub/accounts/{{_accountInfo.Id}}/logos/show"
style="vertical-align: top; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; max-width: 100%; border: none; max-height: 80px !important;">
</></a>
</div>
<h1 style="margin: 0; font-size: 50px; line-height: 58px; box-sizing: border-box !important;">Abandoned Cart</h1>
</td>
</tr>

<tr style="box-sizing: border-box !important;">
<td class="ph4-ns"
style="font-size: 14px; line-height: 20px; box-sizing: border-box; border-collapse: collapse; text-align: left; border-top-style: solid; border-top-width: 1px; border-color: #eee; width: 100%; padding-top: 2rem; padding-bottom: 2rem !important; font-family: -apple-system, BlinkMacSystemFont, '''Segoe UI''', Roboto, Helvetica, Arial, sans-serif;"
align="left">
<div style="box-sizing: border-box; clear: both; float: none; padding-top: 1rem !important;">

<table width="100%" border="0" cellpadding="0" cellspacing="0"
style="box-sizing: border-box; border-collapse: collapse; border-spacing: 0; mso-table-lspace: 0pt; mso-table-rspace: 0pt !important; font-family: -apple-system, BlinkMacSystemFont, '''Segoe UI''', Roboto, Helvetica, Arial, sans-serif;">
<thead>
</thead>
<tbody>
{{#each items}}
<tr style="box-sizing: border-box !important;">
<td
style="font-size: 14px; line-height: 20px; box-sizing: border-box; border-collapse: collapse; text-align: left; width: 4rem; padding-right: .5rem; padding-top: .5rem; padding-bottom: .5rem; vertical-align: top; font-family: -apple-system, BlinkMacSystemFont, '''Segoe UI''', Roboto, Helvetica, Arial, sans-serif;"
align="left" valign="top"><img alt="" src="{{image}}"
style="vertical-align: top; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; max-width: 100% !important;" />
</td>
<td
style="font-size: 14px; line-height: 20px; box-sizing: border-box; border-collapse: collapse; text-align: left; padding-top: .5rem; padding-bottom: .5rem; vertical-align: top !important; font-family: -apple-system, BlinkMacSystemFont, '''Segoe UI''', Roboto, Helvetica, Arial, sans-serif;"
align="left" valign="top">
<div class="mv1-ns"
style="box-sizing: border-box; line-height: 1.25; font-size: 1rem!important;">{{productName}}</div>
<div style="box-sizing: border-box; color: #777 !important;">
{{quantity}} un.
{{#if sellingPrice}}
${{formatCurrency sellingPrice}}
{{else}}
Grátis
{{/if}}
</div>
</td>
</tr>
{{/each}}
</tbody>
</table>
</div>
</td>
</tr>

<tr style="box-sizing: border-box!important;">
<td class="ph4-ns"
style="font-size: 14px; line-height: 20px; box-sizing: border-box; border-collapse: collapse; text-align: left; border-top-style: solid; border-top-width: 1px; border-color:#eee; width: 100%; padding-top: 2rem; padding-bottom: 2rem !important; font-family: -apple-system, BlinkMacSystemFont, '''Segoe UI''', Roboto, Helvetica, Arial, sans-serif;"
align="left">
<a style="color: black" href="http://www.FINALURL.com/checkout/cart/{{addToCartURL}}">Link to the cart</a>
</td>
</tr>

</table>
</td>
</tr>
</table>
</body>

</html>
```

The `addToCartURL` variable is formatted to work with the [cart URL](https://help.vtex.com/tutorial/how-to-assemble-the-cart-url--u3Tj5wagnukYwG84IQU06). Its purpose is to send the user back to the checkout with the items in the abandoned cart.