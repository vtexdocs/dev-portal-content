---
title: 'Import customer data'
slug: 'import-customer-data'
hidden: false
createdAt: '2022-05-16T23:39:31.746Z'
updatedAt: '2022-06-01T21:27:30.468Z'
---

When implementing an ecommerce project, it may be necessary to import customer data from other systems, such as Customer Relationship Management (CRM) applications.

You can use [Master Data v2](https://help.vtex.com/en/tutorial/master-data-v2--3JJ1mlzuo88w22gO0gy0QS#) to manage many types of data and it provides the best way of integrating your customer data base to VTEX.

In this guide, you can learn how to import customer data to VTEX. Learn more about Master Data and its features in the [Master Data developers guide](https://developers.vtex.com/vtex-rest-api/docs/master-data-how-it-works).

> ℹ️ Importing your customers' data will also enable automatic fill-in at checkout for those customers. Learn more about [SmartCheckout - Customer information automatic fill-in](https://help.vtex.com/en/tutorial/smartcheckout-preenchimento-automatico-de-dados-do-cliente--2Nuu3xAFzdhIzJIldAdtan#)

## Data entities

Master Data v2 leveradges the concept of [data entities](https://developers.vtex.com/vtex-rest-api/docs/master-data-components#data-entity) to allow for highly customizable data bases. These work as tables, where each document (profile or address) is saved as a row.

There are two native data entities you must use for this integration:

- `CL`: stores customer profiles.
- `AD`: stores addresses.

## Schemas

It is not strictly necessary, but you can use [JSON schemas](https://json-schema.org/), to specify the format of the data you expect to store. By using them you enable some handy features such as:

- Indicating which fields are searchable.
- Having Master Data validate documents as they are sent.
- [Master Data triggers](https://help.vtex.com/en/tutorial/setting-up-triggers--54eVOFGhS0EWyAUieoqKWo#).
  > ℹ️ A single data entity may be associated with more than one schema and will store documents that comply with multiple schemas or none.

To implement schemas check:

- [Get schemas API endpoint](https://developers.vtex.com/vtex-rest-api/reference/getschemas): to check the schemas that are set up in your store for a given data entity.
- [Save schema by name API endpoint](https://developers.vtex.com/vtex-rest-api/reference/saveschemabyname): if you wish to create a schema for a given data entity.
- [Schema lifecycle guide](https://developers.vtex.com/vtex-rest-api/docs/master-data-schema-lifecycle): to learn more.

## Integration

The basic operations you will need to import customer data are:

- [creating new customer profiles](#create-new-customer-profile).
- [creating addresses](#create-new-address).

Depending on your project’s architecture, it may also be important to:

- [Retrieve customer data](#retrieve-customer-data).
- [Edit customer data](#edit-customer-data).

### Create new customer profile

To register a new customer profile, use the [Create new document](https://developers.vtex.com/vtex-rest-api/reference/createnewdocument) for the `CL` data entity.

> ❗ When creating a new document, you will receive an `Id` in the response. This identifies the customer in Master Data and will be used later to register addresses associated with that customer. Make sure you save this ID and associate it with the customer’s ID in your source database.

#### Creating customer profile request example

POST

```
https://{accountName}.{envirnoment}.com.br/api/dataentities/CL/documents
```

Request body

```json
{
  "email": "clark.kent@examplemail.com",
  "firstName": "Clark",
  "lastName": "Kent",
  "phone": "+12025550195",
  "documentType": "CPF",
  "document": "12345678900",
  "isCorporate": false,
  "isNewsletterOptIn": false,
  "localeDefault": "en-US"
}
```

Response

```json
{
  "Id": "CL-b345cbda-e489-11e6-94f4-0ac138d2d42e",
  "Href": "http://api.vtex.com/my-store-name/dataentities/CL/documents/b345cbda-e489-11e6-94f4-0ac138d2d42e"
}
```

### Create new address

To register a new customer address, use the [Create new document](https://developers.vtex.com/vtex-rest-api/reference/createnewdocument) for the `AD` data entity.

[block:callout]
{
"type": "warning",
"body": "Note that the `userId` in the request body is the `Id` returned by the API when [creating a customer profile](#create-new-customer-profile). Make sure to send it to associate the address with the corresponding customer."
}
[/block]

#### Creating new address request example

POST

```
https://{accountName}.{envirnoment}.com.br/api/dataentities/AD/documents
```

Request body

```json
{
  "addressName": "My House",
  "addressType": "residential",
  "city": "Metropolis",
  "complement": "",
  "country": "USA",
  "postalCode": "11375",
  "receiverName": "Clark Kent",
  "reference": null,
  "state": "MP",
  "street": "Baker Street",
  "neighborhood": "Upper east side",
  "number": "21",
  "userId": "7e03m794-a33a-11e9-84rt6-0adfa64s5a8e"
}
```

### Retrieve customer data

If you need to retrieve customer information after you have imported it to VTEX, you can use one of these endpoints:

- [Search documents](https://developers.vtex.com/vtex-rest-api/reference/searchdocuments): more direct solution for fetching a single document, while also being able to return multiple results.
- [Scroll documents](https://developers.vtex.com/vtex-rest-api/reference/scrolldocuments): useful if you want to fetch multiple documents spread across multiple requests.

> ℹ️ These requests allow you to filter and sort data by any of the documents’ fields. You can also request that only certain pieces of information be returned, instead of the complete documents. See their detailed documentation to learn more:
>
> - [Search documents](https://developers.vtex.com/vtex-rest-api/reference/searchdocuments)
> - [Scroll documents](https://developers.vtex.com/vtex-rest-api/reference/scrolldocuments)

## Edit customer data

Once your store is up and running, your customers can update their profile information in the [My Account](https://help.vtex.com/en/tutorial/how-does-my-account-work--2BQ3GiqhqGJTXsWVuio3Xh#) section and it will be automattically updated in the documents you have created with the Master Data v2 API. So many integrations will not have to deal with customer data maintenance.

However, if you need to implement such an integration, you can use the [Update partial document API endpoint](https://developers.vtex.com/vtex-rest-api/reference/updatepartialdocument).

#### Updating customer profile request example

PATCH

```
https://{accountName}.{envirnoment}.com.br/api/dataentities/CL/documents/{id}
```

Request body

```json
{
  "phone": "+12025550195",
  "isNewsletterOptIn": false
}
```

#### Updating address request example

PATCH

```
https://{accountName}.{envirnoment}.com.br/api/dataentities/CL/documents/{id}
```

Request body

```json
{
  "phone": "+12025550195",
  "isNewsletterOptIn": false
}
```
