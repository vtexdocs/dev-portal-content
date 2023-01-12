---
slug: "cardholder-document-configuration"
title: "Cardholder Document Configuration"
createdAt: 2022-04-20T13:03:27.191Z
hidden: false
type: "improved"
---

![Commerce APIs](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/cardholder-document-configuration-0.png)

VTEX allows anti-fraud providers and merchants to have the autonomy to decide whether an identification document from the cardholder (example: CPF, Social Security) will be required during fraud analysis. This functionality is applied through a field called "cardholder document" that can be shown on the checkout page.

On the [GET Antifraud Manifest](https://developers.vtex.com/vtex-rest-api/reference/manifest) endpoint, the `cardholderDocument` field, which indicates the requirement of card holder document in card transactions has been added. The field has three possible values: `required`, `optional`, or `unused`.

Learn More:

[Cardholder Document Configuration - Dev. Portal](https://developers.vtex.com/vtex-rest-api/docs/cardholder-document-configuration)

[Cardholder Document Configuration - Help Center](https://help.vtex.com/en/tutorial/antifraud-provider--4aZtmdpgFikcsQomWyqAOq#cardholder-document-configuration)
