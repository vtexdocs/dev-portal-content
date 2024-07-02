---
title: "Implementing a pre-analysis anti-fraud flow for debit card transactions"
slug: "implementing-a-pre-analysis-antifraud-flow-for-debit-card-transactions"
hidden: false
createdAt: "2023-07-04T00:00:00.691Z"
updatedAt: ""
---

To provide more protection in transactions processed by debit cards, an initial pre-analysis anti-fraud step can be added to the standard payment transaction flow.

See below an example of a debit card transaction using the anti-fraud system:

1. **Analyzing initial risk (pre-analysis)**: This flow starts with a pre-analysis carried out by the anti-fraud system using the data forwarded by the payment gateway.
2. **Authorizing**: If no initial inconsistencies are found, the transaction information is forwarded to the acquirer or another gateway (when applicable).
3. **Authorized**: Upon initiating the authorization process, the acquirer or other gateway sends the transaction information to the issuing bank. The bank responds whether or not the transaction should be authorized. If it denies the transaction, the payment is **canceled**. If it authorizes, the transaction status changes to **Authorized**.
4. **Approved**: This status indicates that the transaction was authorized by the issuing bank.
5. **Analyzing Risk**: After approval of the transaction by the issuing bank, the anti-fraud system works by analyzing the risk of the operation.
6. **Risk Approved**: If the anti-fraud responds positively, the transaction goes to the **risk approved** status. If the anti-fraud identifies any evidence of fraud, the transaction is **canceled**.
7. **Settlement of $**: This status indicates that the **settlement** process of a specific amount will be started. It's important to note that, at this stage, the value **has not yet been settled**. What exists is a warning that the process of settling this value will be carried out in the next status.
8. **Settling**: In this status, the **settlement** attempt actually starts. The systems responsible for that begin the process by which the transaction amount is settled.
9. **Settled**: When the transaction reaches this status, it means that **the amount was successfully settled**. Now, the payment has already been sent to the store's account.
10. **Finished**: The transaction reaches the **finished** status when the invoice with the payment amount is issued and linked to the order in the OMS. You should note that even after the settlement finishes successfully, [it is necessary to include the invoice in the order](https://help.vtex.com/en/faq/why-has-a-transaction-been-successfully-captured-but-not-finalized-in-the-pci-gateway).

<p align="center">
<img src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/a6366f253c5abb8a1fc21552bfbdd3c53314146c/docs/guides/Payments/payments-configuration-guides/antifraud-debit-card-transactions.png"></img>
</p>

## How to activate the anti-fraud flow for debit card transactions

To implement the debit card anti-fraud provider flow in your system, during the homologation process, you should contact the [Support VTEX](https://help.vtex.com/support) and request its activation.

Upon your request, our team will add the parameter `shouldUseAntifraudOnDebit` to your provider settings. This is a boolean field, with the default value being `false`.

When you set this value to `true`, and a debit card transaction occurs using a payment rule containing an anti-fraud, the anti-fraud provider will be triggered, and the payment flow will be carried out as mentioned in this article.
