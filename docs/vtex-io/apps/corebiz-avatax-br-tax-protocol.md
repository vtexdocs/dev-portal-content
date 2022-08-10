---
title: "Avatax-BR-Tax-Protocol"
slug: "corebiz-avatax-br-tax-protocol"
excerpt: "corebiz.avatax-br-tax-protocol@0.1.0"
hidden: true
createdAt: "2022-07-20T17:58:18.201Z"
updatedAt: "2022-07-20T17:58:18.201Z"
---
This app is a dependency for the `vtex.avatax-br` app. Its purpose is to handle tax calculations through the checkout Tax Hub. You **don't** need to install this app separately.

This app depends on `vtex.avatax-br` configuration to work properly.

## Routes

##### /app/tax-provider/checkout/simulation
`taxSimulation`: The route responsible for calculating taxes. It follows the tax protocol specification. Each checkout simulation goes through here when the `vtex.avatax-br` app is turned on.

##### /app/avatax-br-tax-protocol/ping
`ping`: This app pings itself regularly in an attempt to keep itself alive.

##### /app/tax-provider/product
`productTax`: This route allows calculating taxes for a specific product. 

##### /app/avatax-br-tax-protocol/notify-order
`notifyOrder`: This route allows saving order information inside log entries. It's triggered by the orders-broadcaster.