---
title: "Cardholder document configuration"
slug: "cardholder-document-configuration"
hidden: false
createdAt: "2022-04-19T17:14:08.281Z"
updatedAt: "2022-04-29T12:37:41.520Z"
---

When a customer decides to use a credit or debit card as a payment method for their purchase, in addition to the card data (number, name, expiration date, and CVV code), on some occasions, an identification document from the cardholder may also be requested (example: CPF, Social Security Number). Some payment providers use this information to authorize the transaction and anti-fraud providers to perform fraud analysis.

However, in some countries, there are anti-fraud providers that do not require this type of additional document, and local legislation does not encourage the use of this information. Likewise, some people do not have a personal identification document that can be used to prove that they are the owners of the card used in the purchase.

To allow each anti-fraud provider and merchant to have the autonomy to decide whether or not to request this document, VTEX provides the option to configure the cardholder's document field.

>⚠️ If the anti-fraud provider wants to keep the use of the cardholder document as "mandatory", it is not necessary to perform any of the procedures described in this article.

The procedures below demonstrate how to configure anti-fraud providers via PPP.

## Configuring cardholder document field - Anti-fraud Provider (PPP)

To configure the cardholder document field, follow the steps below:

1. In the anti-fraud provider manifest, add the `cardholderDocument` field with one of the following values:
      - `"required"`: a cardholder document is required for the purpose of fraud analysis. The field must be displayed at checkout and on [my cards](https://help.vtex.com/en/tutorial/como-funciona-a-minha-conta--2BQ3GiqhqGJTXsWVuio3Xh#credit-cards).
      - `"optional"`: a cardholder document can be used to complete the fraud analysis but is not required. The merchant must configure if they want to display the field at checkout and on [my cards](https://help.vtex.com/en/tutorial/como-funciona-a-minha-conta--2BQ3GiqhqGJTXsWVuio3Xh#credit-cards). Learn more at [Cardholder Document Configuration](https://help.vtex.com/en/tutorial/antifraud-provider--4aZtmdpgFikcsQomWyqAOq#cardholder-document-configuration).
      - `"unused"`: a cardholder document is not required to perform fraud analysis. The field will not be displayed at checkout nor on [my cards](https://help.vtex.com/en/tutorial/como-funciona-a-minha-conta--2BQ3GiqhqGJTXsWVuio3Xh#credit-cards).

Anti-Fraud Provider Manifest example:
![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Payments/payments-configuration-guides/cardholder-document-configuration-0.png)

2. Access [VTEX Support](https://help.vtex.com/en/support) to open a ticket, and request that the connector on VTEX be updated.

>⚠️ If the anti-fraud provider wants to keep the use of the cardholder document "mandatory", it is not necessary to add the field `cardholderDocument`.
