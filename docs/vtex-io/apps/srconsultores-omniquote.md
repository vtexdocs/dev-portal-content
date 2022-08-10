---
title: "addToQuoteButton"
slug: "srconsultores-omniquote"
excerpt: "srconsultores.omniquote@0.20.11"
hidden: true
createdAt: "2022-07-14T20:36:59.756Z"
updatedAt: "2022-08-09T21:53:58.813Z"
---
This component use a `productContext` that exist on details o `productsummary` components, so this must to be added in this parents components:

![image](https://user-images.githubusercontent.com/14808650/148576501-c1e679f8-1484-4012-adc7-5e5493b41a90.png)

### Looks Like:

![image](https://user-images.githubusercontent.com/14808650/148577638-4444f939-d11b-4e25-9440-1d5371137eb4.png)


## goToQuoteButton
This component can be added everwhere you need, in this case, on header `block.json`:

![image](https://user-images.githubusercontent.com/14808650/148576607-426905f9-fa03-4bd4-8829-2fd569b77510.png)

## addCartQuoteButton
This component can be added everwhere you need, in this case, on header `minicart.jsonc`:

![image](https://user-images.githubusercontent.com/14808650/161395590-d3165f0d-f345-4dea-9c4b-e993a4800bcf.png)
### Looks Like:

![image](https://user-images.githubusercontent.com/14808650/148577713-243a4172-d93e-421f-8f29-2087657eebf5.png)


--------------------------------------------------------------------------------------------------------------------------
| Route                  | Description                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------------  |
| `/omniquote`           | Lists all saved quotes.                                                                        |
| `/omniquote/create`    | Retrieves the current products added information, allowing you to create quotations, add individual products, masive imports and make a copy of cart if is neccesary.  |
| `/omniquote/view/:ID`  | Details page, displayed when you click on a quote from the listing page (`/omniquote`).        |
| `/admin/omniquote/admin`  | List all saved customer's quotes to make administrative changes and approved it.        |
| `admin/omniquote/config` | In this page, you can add a EndPoint to triggers data to a external system.      |
---------------------------------------------------------------------------------------------------------------------------

The new routes already contain a default template with all blocks automatically exported by the `omniquote` app, meaning that the Order Quote pages are ready to be rendered and no further actions are required from you.

## Add or edit products
![image](https://user-images.githubusercontent.com/14808650/148575780-ef9512ce-a439-4bd7-b98f-34e6ed0fe09c.png)

## Approve quotation

![image](https://user-images.githubusercontent.com/14808650/148575390-a2d6951b-bbd0-4e85-9e9d-e26f7c533739.png)

## Adding Trigger EndPoint

![image](https://user-images.githubusercontent.com/14808650/165381117-6546ee7c-fb42-4d73-a93f-89e9eb0c92d0.png)

![image](https://user-images.githubusercontent.com/14808650/165381186-e735e395-a9de-42c0-9318-b418ec6ef981.png)

## Example to import

![image](https://user-images.githubusercontent.com/14808650/152698121-57d36207-dfab-4bfa-ac3a-e04a21439cf8.png)

## Formato importaciones
https://docs.google.com/spreadsheets/d/1c29orZQ1LwOGUjFHWQxMA1LVDbCPk_e8/edit?usp=sharing&ouid=111966310709533495121&rtpof=true&sd=true

This is a simple Excel format whithout formules and type formats. Look the column names and the data format.

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

## MasterData And Data Schema:

This schema can be used to add, update or delete quotations - (Integrates External Systems) - With documents APIs on: [MasterData EndPoints](https://developers.vtex.com/vtex-rest-api/reference/master-data-api-v2-overview).

`Schema and Entity Name: omniquote`

```diff
Format of data:

 ``` "properties": {
        "email": {
            "type": "string",
            "title": "Email"
        },
        "quoteName": {
            "type": "string",
            "title": "Quote Name"
        },
        "status": {
            "type": [
                "null",
                "string"
            ],
            "title": "Status"
        },
        "integratedEndPoint": {
            "type": [
                "null",
                "string"
            ],
            "title": "EndPoint"
        },
        "description": {
            "type": [
                "null",
                "string"
            ],
            "title": "Description"
        },
        "selectDefaultTypeDocument": {
            "type": [
                "null",
                "string"
            ],
            "title": "Document Type"
        },
        "documentCustomer": {
            "type": [
                "null",
                "string"
            ],
            "title": "Document Customer"
        },
        "names": {
            "type": [
                "null",
                "string"
            ],
            "title": "Names"
        },
        "lastNames": {
            "type": [
                "null",
                "string"
            ],
            "title": "LastNames"
        },
        "companyDocument": {
            "type": [
                "null",
                "string"
            ],
            "title": "Company Document"
        },
        "legalName": {
            "type": [
                "null",
                "string"
            ],
            "title": "Legal Name"
        },
        "comercialName": {
            "type": [
                "null",
                "string"
            ],
            "title": "Comercial Name"
        },
        "phone": {
            "type": [
                "null",
                "string"
            ],
            "title": "Phone"
        },
        "invoiceAddress": {
            "type": [
                "null",
                "string"
            ],
            "title": "Invoice Address"
        },
        "giro": {
            "type": [
                "null",
                "string"
            ],
            "title": "Giro"
        },
        "specialBussinesCode": {
            "type": [
                "string",
                "null"
            ],
            "title": "Código especial de Negocio"
        },
        "percentBussiness": {
            "type": [
                "string",
                "null"
            ],
            "title": "Porcentaje"
        },
        "selectSpecialBussiness": {
            "type": [
                "string",
                "No"
            ],
            "title": "Tipo de negocio especial"
        },
        "items": {
            "type": "array",
            "title": "Quote"
        },
        "creationDate": {
            "type": "string",
            "title": "Creation Date"
        },
        "quoteLifeSpan": {
            "type": "string",
            "title": "Quote Life Span"
        },
        "document": {
            "type": "string",
            "title": "Documento"
        },
        "subtotal": {
            "type": "number",
            "title": "Subtotal"
        },
        "discounts": {
            "type": "integer",
            "title": "Discounts"
        },
        "shipping": {
            "type": "integer",
            "title": "Shipping"
        },
        "taxes": {
            "type": [
                "null",
                "integer"
            ],
            "title": "Taxes"
        },
        "customData": {
            "type": [
                "null",
                "object"
            ],
            "title": "Custom Data"
        },
        "total": {
            "type": "number",
            "title": "Total"
        },
        "seller": {
            "type": "string",
            "title": "Seller"
        },
        "emailOperator": {
            "type": [
                "null",
                "string"
            ],
            "title": "Email Operator"
        }
    },
  },
```

## Formato importaciones
https://docs.google.com/spreadsheets/d/1c29orZQ1LwOGUjFHWQxMA1LVDbCPk_e8/edit?usp=sharing&ouid=111966310709533495121&rtpof=true&sd=true

## Usage

This app have some components that help to add products to a Quote and link to create Quote.

So you need to add this components in your store theme.

| CSS Handles               |
| ------------------------- |
| `buttonDelete`            |
| `buttonPrint`             |
| `buttonSave`              |
| `buttonsContainer`        |
| `buttonUse`               |
| `checkboxClear`           |
| `containerCreate`         |
| `containerFields`         |
| `containerList`           |
| `containerView`           |
| `refreshButton`           |
| `refreshLoading`          |
| `field`                   |
| `inputCreate`             |
| `inputCreate`             |
| `listContainer`           |
| `logo`                    |
| `notAuthenticatedMessage` |
| `printingArea`            |
| `totalizerContainer`      |
| `itemNameContainer`       |
| `itemName`                |
| `itemSkuName`             |
| `goToQuoteButton`         |
| `quantityOnQuoteCounter`  |
|---------------------------|
<!-- DOCS-IGNORE:start -->