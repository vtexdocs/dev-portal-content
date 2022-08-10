---
title: "Refund the transaction"
slug: "refundthetransaction"
excerpt: "Refunds transaction's value that was previously settled."
hidden: false
createdAt: "2019-12-30T17:11:51.326Z"
updatedAt: "2020-02-27T17:22:01.787Z"
---
After a settled transaction this REST call is allowed, it is possible to refund partially or complete the transaction value. 

Due to acquirer rules it is not possible to execute this step online against the acquirer, and if and error occurrs, we notify the seller company responsible via email to verify manually the transaction status against the acquirer.