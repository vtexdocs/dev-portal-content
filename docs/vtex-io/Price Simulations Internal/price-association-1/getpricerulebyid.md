---
title: "Get price association by ID"
slug: "getpricerulebyid"
excerpt: "Retrieves price association for a shopping scenario by its ID"
hidden: true
createdAt: "2021-02-02T13:50:02.022Z"
updatedAt: "2021-02-03T20:48:37.681Z"
---
## Request Headers 
---
<table>
  <tr>
        <td><b>Header</b></td>
        <td><b>Value</b></td>
    </tr>
    <tr>
        <td><code>Content-Type</code></td>
        <td><b>application/json</b></td>
    </tr>
  <tr>
        <td><code>Accept</code></td>
        <td><b>application/json</b></td>
    </tr>
</table>

<br>

## Response Body 
---

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
        <td>Price Association unique identifier</td>
    </tr>
    <tr>
        <td><code>resell</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Order type</td>
    </tr>
     <tr>
        <td><code>pricetable</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Name of the Price Table associated with the scenario</td>
    </tr>
         <tr>
        <td><code>email</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>User's email</td>
    </tr>
         <tr>
        <td><code>state</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Delivery location</td>
    </tr>
     <tr>
</table>
<br>

## Request examples and their responses 
---
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"id\": \"25cacc61-a66e-11ea-8343-0a541e315519\",\n    \"orderType\": \"res\",\n    \"state\": \"RJ\",\n    \"pricetable\": \"ale2\",\n    \"email\": null\n}",
      "language": "curl",
      "name": "200 - OK"
    },
    {
      "code": "<!doctype html>\n<html>\n\n<head>\n\t<script>\n\t\t(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start': new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0], j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src= '//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f); })(window,document,'script','dataLayer','GTM-MB9QMPT');\n\t</script>\n\t<title>VTEX ID Authentication</title>\n\t<meta charset=\"utf-8\">\n\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, maximum-scale=1.0\">\n\t<link rel=\"stylesheet\" href=\"//io.vtex.com.br/front-libs/intlTelInput/intlTelInput.css?x=1\">\n</head>\n\n<body>\n\t<script src=\"//io.vtex.com.br/front-libs/jquery/2.1.3/jquery.min.js\"></script>\n\t<script src=\"//io.vtex.com.br/front-libs/intlTelInput/intlTelInput.js\"></script>\n\t<script>\n\t\twindow.vtex = {};window.vtex.conciergeData = {\"accountName\":\"b2bstore\",\"environment\":\"stable\"};\n\t</script>\n\t<script src=\"//io.vtex.com.br/vtex-id-ui/3.20.1/vtexid.min.js\"></script>\n\t<script>\n\t\t$(function(){vtexid.start({returnUrl: vtexid.getReturnUrl()|| vtexid.getRedirectUrl() || \"/\",canClose: false});});\n\t</script>\n</body>\n\n</html>",
      "language": "curl",
      "name": "200 - OK"
    }
  ]
}
[/block]