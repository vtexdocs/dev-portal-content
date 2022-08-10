---
title: "DECIDIR PPP-PCI Connector"
slug: "vtexarg-decidir-payment-provider"
excerpt: "vtexarg.decidir-payment-provider@0.1.10"
hidden: true
createdAt: "2022-07-15T14:34:18.326Z"
updatedAt: "2022-07-19T18:38:25.651Z"
---
###Based on Payment Provider Example
Implementing a [**Payment-Provider protocol**](https://documenter.getpostman.com/view/487146/7LjCQ6a?version=latest).

## Connector

The connector is located in `node/connector.ts` and it's the only file you need to modify in order to implement a working connector.  
It has 4 mandatory methods that should be implemented, each related to each route. The class has been built so you receive the request body as the parameter and return the response in the function.

## Payment Provider Service

The payment provider service is found at `node/index.ts` and it automatically builds the main routes for your service.  
If your connector requires more routes, make sure to read the [documentation](https://www.notion.so/vtexhandbook/Payment-Provider-Framework-IO-7eb72e77f2c545c7b3b046d0bb43c449) for how to build them.

The `node/flow.ts` is used exclusively for the test suite.  
It detects which test is currently being run and executes the instructions accordingly.

## Builders
The project has 3 builders, each one is responsible for creating the payload for an specific service or method.

`builders/adittionalData.ts`
Creates the payload for storing the payment information in MasterData.

`builders/paymentMethods.ts`
Parses Decidir Payment Method name, for retrieving the ID needed in the payment creation request.

`builders/decidir.ts`
Parses Authorization request information for building the Decidir `/token` and `/payments` request, this two api calls are responsible for creating a payment in decidir.

## Services
The Decidir connector uses different services for consuming the basic informaiton resources:
* `additionalDataClient`  
  Responsible for storing and retrieving data from MasterData  
  
    
* `decidirClient`  
  Responsible for creating tokens and payments request in the decidir REST API  
  
    
* `orderForm`  
  Responsible for retrieving the orderFormId for the current Payment. This value is needed to properly generate the DEVICE FINGERPRINT  
  
  
* `secureClient`  
  Responsible for sending the information using the VTEX Secure Proxy. This proxy receives a VTEX TOKEN as card informaiton, replace it and then sends the request to decidir.
  

## Payment Flow
You can check the payment flow in the following MIRO. If you can't access please refer to [tomas.mehdi@vtex.com.br](mailto:tomas.mehdi@vtex.com.br) or First Party Apps - APUB [Slack Channel](https://slack.com/app_redirect?channel=apub-1st-party-apps)

#### [Miro Board](https://miro.com/app/board/o9J_l4mSBNA=/)

### Device Finger Print
For enabling device fingerprint, [GTM](https://tagmanager.google.com/?hl=es) is mandatory.

A VTEX Public documentation is been developed. [JIRA TASK](https://vtex-dev.atlassian.net/browse/EDU-4406)

## Homologation
Connector homologation is in progress.

- [JIRA task](https://vtex-dev.atlassian.net/browse/PPP-46)
- [Slack Thread](https://vtex.slack.com/archives/CDT0YFXL2/p1622050440039900)

## Full Documentation

You can read the full documentation here: [Payment Provider Framework RFC](https://www.notion.so/vtexhandbook/Payment-Provider-Framework-IO-7eb72e77f2c545c7b3b046d0bb43c449)

## Contributors ✨

Thanks goes to these wonderful people:
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<table>
  <tr>
    <td align="center"><a href="https://github.com/tomymehdi"><img src="https://avatars.githubusercontent.com/u/774112?v=4" width="100px;" alt=""/><br /><sub><b>Tomás Alfredo Mehdi</b></sub></a><br /><a href="https://github.com/vtex-apps/ppp-decidir/commits?author=tomymehdi" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!