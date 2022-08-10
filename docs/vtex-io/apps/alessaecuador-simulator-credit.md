---
title: "Credit Simulator"
slug: "alessaecuador-simulator-credit"
excerpt: "alessaecuador.simulator-credit@0.0.7"
hidden: true
createdAt: "2022-07-11T18:29:39.008Z"
updatedAt: "2022-07-11T18:29:39.008Z"
---
## Description

Credit simulator is an application which has two options.

-   Calculate the value of the installments according to the amount and the assigned term.
-   Calculate a credit amount according to how much you can contribute monthly and term. Later gives the value of the fee.

## Table of Contents

-   [Usage](#usage)
-   [Components Specs](#components-specs)

## Usage

This app uses our store builder with the blocks architecture. To know more about Store Builder [click here.](https://help.vtex.com/en/tutorial/understanding-storebuilder-and-stylesbuilder#structuring-and-configuring-our-store-with-object-object)

To use this app, you need to import in your dependencies on `manifest.json`.

```json
  "dependencies": {
    "blacksipqa.simulator-credit": "0.x"
  }
```

Previously mentioned `credit simulator` consists of two sections, which should be added two blocks. For instance.
See an example of how to configure:

```json
{
    "store.home": {
        "blocks": ["simulator-credit", "simulator-credit.v2"]
    }
}
```

## Components Specs

Below we have a README for each component of this project that explains how to use them.

-   [Simulator Credit](CreditSimulator.md)
-   [Simulator Credit V2](CreditSimulatorV2.md)