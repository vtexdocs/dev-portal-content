---
title: "VTEX SmartBill"
slug: "vtex-smartbill"
excerpt: "vtex.smartbill@2.2.10"
hidden: true
createdAt: "2022-08-08T10:57:42.573Z"
updatedAt: "2022-08-08T11:22:10.275Z"
---
This application allows you to generate invoices using the SmartBill API.

## Installation & Configuration

- Use the vtex toolbelt to install.

```bash
vtex install vtex.smartbill
```

- Import the vtex.smartbill app to your theme's dependencies in the manifest.json

```json
"dependencies": {
    ....
    "vtex.smartbill" : "1.x"
}
```

Open the app settings on your admin - "https://your-store-name.myvtex.com/admin/apps" - click on the SmartBill app and fill in the the following fields:

- SmartBill Username
- SmartBill API TOKEN
- SmartBill Vat Code
- SmartBill Series Name
- Invoice shipping cost (optional)
- Shipping cost product name (optional)
- Shipping cost product code (optional)
- Use VTEX priceTags (optional)
- Smartbill default VAT percentage

## Exposed endpoints

POST - /smartbill/generate-invoice (https://ws.smartbill.ro/SBORO/api/invoice)

- [DOCS](https://api.smartbill.ro/#!/Facturi/addInvoicePublicApi)

Request Example:

```json
{ "order": "Response from /api/oms/pvt/orders/{orderId}" }
```

Response Example:

```json
{
  "errorText": "",
  "message": "",
  "number": "1111",
  "series": "ASD",
  "url": "",
  "encryptedNumber": "YWZjMjk2MjM2NDkwY2JjMTVjZWQ2XDI3ODdkOTI4ODQyYWZlZTI4OTE3NmQ1MWI5NTNiZDVjMDQxMzkzOTdhZjQrQ2NyWjd4cnFqTVhOY1RPWUV6T3c9PTYyZDBlMmQ4ZDY1YjMzNGViNWM3MDFhNmM3ZjM2OTZiNWU5N@YU2YzYyZDg5MDRkMGQwNmFmN2E0ZWM1MTM2Yjg="
}
```

GET - /smartbill/show-invoice/:encryptedInvoiceNumber (https://ws.smartbill.ro/SBORO/api/invoice/pdf)

- [DOCS](https://api.smartbill.ro/#!/Facturi/getFile)

## Important

> **_NOTE:_** The secret key used to encrypt the invoice number is the Smartbill Token, if the token is changed the previously generated invoices will not be able to decrypt the invoice number. All invoice urls will not show the pdf.