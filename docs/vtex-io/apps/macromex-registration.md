---
title: "Macromex registration"
slug: "macromex-registration"
excerpt: "macromex.registration@1.0.50"
hidden: true
createdAt: "2022-08-09T13:30:35.818Z"
updatedAt: "2022-08-09T13:30:35.818Z"
---
### Installation
> vtex install macromex.registration@0.x


### Settings
* Go to `Admin > Apps > Macromex Registration` and fill up the form.

### Email Templates
* Go to `Admin > Message Center > Templates` and create 2 new email templates with the following names `Inregistrare noua` and `Inregistrare noua  admin companie`.
* Check `enable email sending?`
* Add `{{data.targetEmail}}` at "To:" field

#### JsonData Example for email
```
{
	"data": {
		"targetEmail": "email@domain.com",
		"name": "Fullname here",
		"phone": "0720000000",
		"email": "user@domain.com",
		"companyCui": "COMPANY VAT CODE",
		"companyName": "COMPANY NAME",
		"companyAddress": "COMPANY ADDRESS",
		"companyLocality": "CITY",
		"companyCounty": "COUNTY"
	},
	"_accountInfo": {
		"MainAccountName": "VTEX ACCOUNT NAME",
		"AccountName": "VTEX ACCOUNT NAME",
		"Cnpj": "12312312",
		"Id": "VTEX ACCOUNT ID",
		"IsActive": true,
		"IsOperating": false,
		"CreationDate": "2021-02-04T18:59:56",
		"OperationDate": null,
		"CompanyName": "VENDOR COMPANY NAME",
		"TradingName": "VENDOR TRADING NAME",
		"City": null,
		"Complement": null,
		"Country": null,
		"State": null,
		"Address": null,
		"District": null,
		"Number": null,
		"PostalCode": null,
		"Licences": null,
		"ParentAccountName": null,
		"InactivationDate": null,
		"Platform": "vtex"
	}
}
```