---
title: "Payment Methods"
slug: "payments-integration-payment-methods"
hidden: false
createdAt: "2020-11-12T18:46:20.596Z"
updatedAt: "2021-12-23T12:14:21.077Z"
---
Payment methods are different ways that a customer can use money to buy a product or a service. In VTEX, the types of payment methods available are: 

- Credit Cards 
- Debit Cards
- Cash
- Custom Payments
  - Promissory
  - Private Labels
  - Co-Branded
- Regional Payments
  - Instant Payments (Pix/Brazil)
  - Bank Invoice (Boleto Bancário/Brazil)

Different countries use different payment methods. There is an extensive list of payment methods worldwide, especially because the payment methods differ from country to country. Before integrating with VTEX platform, it is important to know if the payment methods processed by your system are compatible with ours.

## Credit Cards

Most financial institutions can offer a credit limit to your account holders. This credit can be used as a payment method through a credit card. With that, the customer can make a purchase but pay for it in the near future.

Also, there is one more important thing about credit cards: the corporate flags - networks responsible for managing the credit card operations. MasterCard, Visa, Amex and Diners are examples of credit card networks in the payments industry. For more information, refer to [Credit card payment flow.](https://help.vtex.com/en/tracks/pagamentos--6GAS7ZzGAm7AGoEAwDbwJG/TEYVv2fcVkH7et9n3OnBS#)

## Debit Cards

A card offered by a financial institution to its account holders. Using the debit card as a payment method, the purchases are paid right the way by deducting the money directly from the customer's bank account. 

In the same way as credit cards, debit cards also work together with corporate flags.

## Cash 

Cash payments can be enabled in the inStore app. After having configured and enabled this payment method, a payment made with cash can be received at the brick–and–mortar store or when a product is delivered to the consumer in cases of delivery service. For more information, refer to [Setting up cash payment through inStore.](https://help.vtex.com/en/tracks/instore-payments--43B4Nr7uZva5UdwWEt3PEy/4ye3bIWldaHJxGTgAziBZo)

## Custom Payments

There are some payment methods non-standard according to the payment market patterns - the Custom Payments. This means that these payment methods have a very specific behavior for every scenario that can be applied.

In VTEX, we majorly work with three of them: Promissory, Private Labels and Co-branded.

### Promissory

The seller has to manually approve each payment that is computed in our system. After the approval, the transaction follows normally. The promissory is used mostly to facilitate payments made with cash.   

### Private Labels

It is a credit card made exclusively for a store that functions with its own brand.

### Co-Branded

Also, a credit card made exclusively for a store. The difference between a private label and a co-branded is that the co-branded works with a partnership between a corporate credit card flag - like MasterCard and Visa - and the store’s brand.

## Regional Payments

### Instant Payments (Pix/Brazil)

Pix is the instant payments ecosystem implementation led by the Central Bank of Brazil (BCB) to enable online money transfers with reduced costs, increased safety and 24/7 availability. Transfers occur directly from the payer’s account to the payee’s account, without the need for intermediaries, resulting in lower transaction costs. For more information, refer to [Pix: Instant Payments in Brazil](https://developers.vtex.com/docs/guides/payments-integration-pix-instant-payments-in-brazil). 

### Bank Invoice (Boleto Bancário/Brazil)

The “boleto bancário” is a popular payment method in Brazil. It consists of an official voucher that a customer can pay in cash at more than 200 thousand payment locations such as banks, post offices, and supermarkets. It can also be paid electronically through internet banking. For more information, refer to [Bank Invoice payment flow](https://help.vtex.com/en/tutorial/boleto-bancario-registrado-fluxo-basico-de-um-pagamento--1WlPkeueWQiykUwW8mcM4S#).

Even though the payment facilities, its disbursement can take two commercial days to be computed.

>ℹ️ In VTEX's APIs, this payment method is registered as “bank invoice”.

>ℹ️ For every payment method, there is a payment condition. You can learn how these terms work in VTEX checking our [101 Payments module track](https://help.vtex.com/en/tracks/payments--6GAS7ZzGAm7AGoEAwDbwJG/6bzGxlz4inf8sKmvZ1c7i3).
