---
title: "B2B"
slug: "tokstoksponsorio-frontend-api-b2b"
excerpt: "tokstoksponsorio.frontend-api@0.20.2"
hidden: true
createdAt: "2022-07-18T11:36:17.418Z"
updatedAt: "2022-08-01T14:03:46.952Z"
---
## Cria registro das empresas nas entidades CL e AD do masterdata

**POST** `/api/io/b2b/register`

### Body:
```json
{
    "corporateName": "string",
    "tradeName": "string",
    "corporateDocument": "string",
    "stateRegistration": "string",
    "firstName": "string",
    "lastName": "string",
    "document": "string",
    "email": "string",
    "businessPhone": "string",
    "isNewsletterOptIn": false,
    "icmsCorporate": "string",
    "postalCode": "string",
    "street": "string",
    "number": "string",
    "complement": "string",
    "neighborhood": "string",
    "city": "string",
    "state": "string",
    "reference": "string",
    "addressName": "string"
}
```

**Obs.:** somente os campos `email`, `firstName`, `document` e `addressName` são obrigatórios.