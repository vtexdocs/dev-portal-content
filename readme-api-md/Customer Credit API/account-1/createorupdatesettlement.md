---
title: "Create or Update Settlement"
slug: "createorupdatesettlement"
excerpt: "Debit a value from checking account."
hidden: false
createdAt: "2019-12-24T00:49:31.616Z"
updatedAt: "2020-02-13T14:24:25.588Z"
---
This operation causes the creation of N invoices, where N is the number of installments.
The first invoice will have a due date with 30 days and the next invoices will have a due date 30 days away from previous invoice.

You can specify a Pre-Authorization Id that will be used to create N invoices.