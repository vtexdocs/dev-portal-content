---
title: "DPL"
slug: "caehealthcareqa-pvt-dplcheck-cae"
excerpt: "caehealthcareqa.pvt-dplcheck-cae@3.0.4"
hidden: true
createdAt: "2022-07-20T20:27:17.429Z"
updatedAt: "2022-08-09T21:55:37.905Z"
---
DPL is a Typescript microservice for dealing with the CAE's export control system.

## Requiriments

- jest
- vtex CLI
- prettier

## Installation

step 01: create masterdata schemas

```
to create the required data tables, you must edit the PROGRAM.LEVEL.APPS/apps/pvt-dplcheck-cae/node/scripts/entity.js file with your account, appKey and appToken.

then under the PROGRAM.LEVEL.APPS/apps/pvt-dplcheck-cae/node/scripts folder run the script:

yarn run deploy:entity --key="" --token="" --account=""
```

step 02: save your emails templates

```
open store's message center

https://{{ACCOUNT}}.myvtex.com/admin/message-center/#/templates

and create these templates, using PROGRAM.LEVEL.APPS/apps/pvt-dplcheck-cae/mail-templates

- dpl-cancel
- dpl-oldmailsent
- dpl-on-hold-order
- dpl-wrongly-moved-order

edit these templates, according to your store brand and requiriments.
```

step 03: create some fields on CL table from master data v1.

```
on the admin: https://{{ACCOUNT}}.ds.vtexcrm.com.br/ open the CL's table and add these fields:

| Name                          | Display Name                                            | Type        | isNullAble | defaultValue      |
| ----------------------------- | ------------------------------------------------------- | ----------- | ---------- | ----------------- |
| birthdate                     | Date of Birth                                           | Varchar 100 | true       |                   |
| currentCitizenshipISO2        | Citizenship (most recent if you have more than one)     | Varchar 10  | false      | defaultValue: --- |
| currentPermanentResidenceISO2 | Country of residence (country where you currently live) | Varchar 10  | true       |                   |
| middleName                    | Middle Name                                             | Varchar 750 | true       |                   |

```

step 04: intall pvt-dplcheck-cae.

```
- submit this [form](https://docs.google.com/forms/d/e/1FAIpQLSfhuhFxvezMhPEoFlN9yFEkUifGQlGP4HmJQgx6GP32WZchBw/viewform) to VTEX requesting the node build to your vendor.

- after the approval, put your vendor on the PROGRAM.LEVEL.APPS/apps/pvt-dplcheck-cae/manifest.json.

- login in your account and run the deployment of the app. vtex login {{ACCOUNT}} -> vtex publish -> vtex deploy -> vtex install
```

step 05: enviroment keys.

```
  - to the pvt-dplcheck-cae works properly you must save your environments keys in the admin panel.
  - open the [admin](https://{{ACCOUNT}}.myvtex.com/admin/apps/) , then procced to the applications list, select the `DPL CHECK OF CAE - PVT` app and save your environments keys.

  to retrieve the full list of environments, go to the PROGRAM.LEVEL.APPS/apps/pvt-dplcheck-cae/manifest.json. file.
```

step 06: checkout UI:

```
this app requires checkout UI in your store.

TODO: document how to use checkout UI for dpl app.

```

step 07: cron function:

```
to process orders, we use a cron function that call the api each period.
to set the cron function check the PROGRAM.LEVEL.APPS/lambdas/cron-dpl-check/README.md

```

## Core Functionalities

1. Check export control status (approved/disapproved)
2. Get export control details
3. Process orders based on user export control status (if user is approved move order to start handling, if user is not approved cancel the order, if the user is under investigation skip the order)
4. Integrated with VTEX order create trigger (if order's user has the DPL control status approved move the order to the start handling, otherwise insert the order into the process queue)
5. Integrated with VTEX order delete trigger (if order's is on the process queue and someone cancel the order in the admin panel, remove the order from the queue and send an email warning about this status change)
6. Integrated with VTEX order update trigger (if order's is on the process queue and someone update the order status in the admin panel, remove the order from the queue and send an email warning about this status change)
7. Send emails when a order has not been processed yet (if order is on the process queue for a configured time period, send an email warning about the order being on the queue)

## APIs

Documentation under the PROGRAM.LEVEL.APPS/apps/pvt-dplcheck-cae/docs/api-docs.md file.

## Schemas

All schemas used in this app can be found on PROGRAM.LEVEL.APPS/apps/pvt-dplcheck-cae/docs/schemas.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.