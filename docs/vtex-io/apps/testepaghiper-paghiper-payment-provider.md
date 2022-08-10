---
title: "VTEX Payment Provider Template"
slug: "testepaghiper-paghiper-payment-provider"
excerpt: "testepaghiper.paghiper-payment-provider@3.5.4"
hidden: true
createdAt: "2022-07-27T20:02:40.067Z"
updatedAt: "2022-07-27T22:15:32.443Z"
---
This repo is based on the [VTEX repo](https://github.com/vtex-apps/payment-provider-example)

A reference app implementing a payment connector.

## Connector

The connector is located in `node/connector.ts` and it's the only file you need to modify in order to implement a working connector.  
It has 4 mandatory methods that should be implemented, each related to each route. The class has been built so you receive the request body as the parameter and return the response in the function.

## Service

The payment provider service is found at `node/index.ts` and it automatically builds the main routes for your service.  
If your connector requires more routes, make sure to read the [documentation](https://www.notion.so/vtexhandbook/Payment-Provider-Framework-IO-7eb72e77f2c545c7b3b046d0bb43c449) for how to build them.

## Test Suite Flow

The `node/flow.ts` is used exclusively for the test suite.  
It detects which test is currently being run and executes the instructions accordingly.

## Full Documentation

You can read the full documentation here: [Payment Provider Framework RFC](https://www.notion.so/vtexhandbook/Payment-Provider-Framework-IO-7eb72e77f2c545c7b3b046d0bb43c449)