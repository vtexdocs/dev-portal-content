---
title: "Do authorization"
slug: "4doauthorization"
excerpt: "The fouth and last step to create a new transaction. It will authorized the new transction creation acorrdint to the data previously informed in the latests requests."
hidden: false
createdAt: "2019-12-30T17:11:51.326Z"
updatedAt: "2020-02-27T17:22:01.124Z"
---
This step is the trigger to process each of payments that were received in step 2.

Each payment will be sent to acquirer. If all payments are authorized, the transaction will be authorized. If one of the payments is denied, all payments in transaction will be cancelled.