---
title: "Managing a Customer Credit account"
slug: "managing-a-customer-credit-account"
hidden: false
createdAt: "2024-03-15T00:00:00.000Z"
updatedAt: ""
---
This guide describes how to manage a [Customer Credit account](https://help.vtex.com/en/tutorial/customer-credit-overview--1uIqTjWxIIIEW0COMg4uE0) in your store by performing the following actions through the endpoints of the [Customer Credit API](https://developers.vtex.com/docs/api-reference/customer-credit-api):

- [Create a Customer Credit account](#creating-a-customer-credit-account)
- [Check Customer Credit account details](#checking-customer-credit-account-details)
- [Update personal information and credit settings](#changing-customer-credit-account-information)
- [Check operations statement](#checking-operations-in-a-customer-credit-account)
- [Register dependents for credit sharing](#sharing-credit-with-dependents)
- [Check all Customer Credit accounts of a store](#checking-all-customer-credit-accounts-of-a-store)
- [Close a Customer Credit account](#closing-a-customer-credit-account)

> ℹ️ For more information about Customer Credit functionalities, access [Customer Credit - Overview](https://help.vtex.com/en/tutorial/customer-credit-overview--1uIqTjWxIIIEW0COMg4uE0) and [Customer Credit - Getting Started](https://help.vtex.com/en/tracks/customer-credit-getting-started--1hCRg21lXYy2seOKgqQ2CC/21ok0GBwmcIeaY2IukYMOg).

## Creating a Customer Credit account

To provide exclusive credit to a customer, you can create a Customer Credit account via VTEX Admin or use the [Open an account](https://developers.vtex.com/docs/api-reference/customer-credit-api#post-/api/creditcontrol/accounts) endpoint. In this request, you must send the following customer data and account usage parameters:

- `document`: Customer document.
- `documentType`: Document type (CPF, CNPJ, other).
- `email`: Customer email.
- `creditLimit`: Maximum credit amount on the account.
- `tolerance`: Account credit tolerance (in decimals). This value represents the increase in credit on an account. For example, a value of `0.30` indicates that the customer - can use up to 30% above the account's original maximum credit amount.

__POST - Open an account__

`https://{accountName}.{environment}.com.br/api/creditcontrol/accounts`

Request body

```json
{
    "document": "55555555555",
    "documentType": "CPF",
    "email": "customer@test.com",
    "creditLimit": "3000",
    "tolerance": "0.05"
}
```

The endpoint will return some of the previously sent data and new information about the created account, such as:

- `id`: Client’s Customer Credit account identification.
- `balance`: Account balance value. If this number is negative, the account has a debit instead of a credit to be used.
- `status`: Client’s Customer Credit account status. All accounts are created with the status `Open`.
- `updatedAt`: Date of the last update made to the account (UTC format).
- `createdAt`: Account creation date (UTC format).
- `availableCredit`: Credit amount available on the account.
- `preAuthorizedCredit`: Credit value that can only be used by the account owner after the merchant releases a specific purchase transaction.
- `availableBalance`: Balance available in the account

Response body

```json
{
    "id": "55555555555_CPF",
    "balance": 0.0,
    "document": "55555555555",
    "status": "Open",
    "documentType": "CPF",
    "creditLimit": 3000.00,
    "updatedAt": "2024-02-22T20:43:21.8753045Z",
    "createdAt": "2024-02-22T20:43:21.8287567Z",
    "description": "",
    "availableCredit": 3000.00,
    "preAuthorizedCredit": 0.0,
    "email": "customer@test.com",
    "tolerance": 0.05,
    "availableBalance": 3000.00
}
```

You can also access your VTEX Admin (__Apps > Customer Credit > Accounts__) to confirm that the new Customer Credit account was created.

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Integration-Guides/customer-credit-integration-guide/customer-credit-account_1.png)

> ⚠️ When the Customer Credit account is created using the [Open an account](https://developers.vtex.com/docs/api-reference/customer-credit-api#post-/api/creditcontrol/accounts) endpoint, the account identification (`id`) will be composed of information from the `document` and `documentType` fields, for example, `55555555555_CPF`. If account creation is performed through your VTEX Admin (__Apps > Customer credit > Accounts > New__), an identification code will be randomly created by the system and will be used as account identification, such as `92bccd01-b4ed-15sa-88a4 -175868a0bf42`.

## Checking Customer Credit account details

When you want to check details about a specific Customer Credit account, you can use the [Retrieve an account by ID](https://developers.vtex.com/docs/api-reference/customer-credit-api#get-/api/creditcontrol/accounts/-creditAccountId-) endpoint. In this request, you must send the account identification (`id`) as a path parameter.

See an example below using the account `111111111_CPF`:

__GET - Retrieve an account by ID__

`https://{accountName}.{environment}.com.br/api/creditcontrol/accounts/111111111_CPF`

Response body

```json
{
    "id": "111111111_CPF",
    "balance": 0.0,
    "document": "111111111",
    "status": "Open",
    "documentType": "CPF",
    "creditLimit": 5000.0,
    "updatedAt": "2024-02-22T21:47:37.2832458Z",
    "createdAt": "2024-02-22T21:47:37.2207379Z",
    "description": "",
    "availableCredit": 5000.0,
    "preAuthorizedCredit": 0.0,
    "email": "customer2@test.com",
    "tolerance": 0.0,
    "availableBalance": 5000.0,
}
```

> ℹ️ You can also check a Customer's Credit account details using the VTEX Admin. For more information, go to __Apps > Customer Credit > Accounts__ and click the desired account.

## Changing Customer Credit account information

The Customer Credit API allows you to modify an account settings through the following actions:

- [Update account information](#updating-account-information)
- [Change credit limit](#changing-the-credit-limit-of-an-account)
- [Change tolerance](#changing-a-credit-account-tolerance)

### Updating account information

The [Update account information](https://developers.vtex.com/docs/api-reference/customer-credit-api#put-/api/creditcontrol/accounts/-creditAccountId-) endpoint must be used to update the email address, type, and document number registered to the client.

> ⚠️ You can also use this endpoint to change the credit limit and tolerance information, but it will be mandatory to send the `id`, `document`, and `documentId` fields, even when you do not intend to update this information. If the `id`, `document`, and `documentId` fields are not sent in this request, the information related to them will be removed from the account.

See an example below using the account `fe60ff40-d1cb-11ee-a0ed-87f4fcc03446`:

__PUT - Update account information__

`https://{accountName}.{environment}.com.br/api/creditcontrol/accounts/fe60ff40-d1cb-11ee-a0ed-87f4fcc03446`

Request body

```json
{
  "email": "customer32@test.com",
  "document": "44444444",
  "documentType": "CPF"
}
```

The endpoint will return the account details with updated information.

Response body

```json
{
    "id": "fe60ff40-d1cb-11ee-a0ed-87f4fcc03446",
    "balance": 0.0,
    "document": "44444444",
    "status": "Open",
    "documentType": "CPF",
    "creditLimit": 4500.0,
    "updatedAt": "2024-02-23T17:21:41.6800112Z",
    "createdAt": "2024-02-22T21:47:37.2207379Z",
    "description": "",
    "availableCredit": 4500.0,
    "preAuthorizedCredit": 0.0,
    "email": "customer32@test.com",
    "tolerance": 0.0,
    "availableBalance": 5000.0
}
```

### Changing the credit limit of an account

The [Change credit limit of an account](https://developers.vtex.com/docs/api-reference/customer-credit-api#put-/api/creditcontrol/accounts/-creditAccountId-/creditlimit) endpoint must be used when you want to change the credit limit value available to a customer credit account. In this request, you must send the account identification (`id`) as a path parameter and the `value` field containing the new credit limit, as shown in the example below:

__PUT - Change credit limit of an account__

`https://{accountName}.{environment}.com.br/api/creditcontrol/accounts/fe60ff40-d1cb-11ee-a0ed-87f4fcc03446/creditlimit`

Request body

```json
{
   "value": 5300
}
```

The endpoint will return the account details and the `creditLimit` field already updated.

Response body

```json
{
    "id": "fe60ff40-d1cb-11ee-a0ed-87f4fcc03446",
    "balance": 0.0,
    "document": "44444444",
    "status": "Open",
    "documentType": "CPF",
    "creditLimit": 5300.0,
    "updatedAt": "2024-02-23T17:44:44.7931543Z",
    "createdAt": "2024-02-22T21:47:37.2207379Z",
    "description": "",
    "availableCredit": 5300.0,
    "preAuthorizedCredit": 0.0,
    "email": "customer32@test.com",
    "tolerance": 0.3,
    "availableBalance": 5300.0
}
```

### Changing a credit account tolerance

The [Change tolerance of an account](https://developers.vtex.com/docs/api-reference/customer-credit-api#put-/api/creditcontrol/accounts/-creditAccountId-/tolerance) endpoint must be used when you want to change the credit tolerance amount available on a customer credit account.

In this request, you must send the account identification (`id`) as a path parameter and the `value` field containing the new credit limit. The `value` is represented by a decimal number, where a `value` of `0.30` means 30% of tolerance.

See an example below using the account `fe60ff40-d1cb-11ee-a0ed-87f4fcc03446` and a tolerance of 15%.

__PUT - Change tolerance of an account__

`https://{accountName}.{environment}.com.br/api/creditcontrol/accounts/fe60ff40-d1cb-11ee-a0ed-87f4fcc03446/tolerance`

Request body

```json
{
   "value": 0.15
}
```

The endpoint will return the account details and the `tolerance` field already updated.

Response body

```json
{
    "id": "fe60ff40-d1cb-11ee-a0ed-87f4fcc03446",
    "balance": 0.0,
    "document": "44444444",
    "status": "Open",
    "documentType": "CPF",
    "creditLimit": 5800.00,
    "updatedAt": "2024-02-23T18:03:03.4849783Z",
    "createdAt": "2024-02-22T21:47:37.2207379Z",
    "description": "",
    "availableCredit": 5800.00,
    "preAuthorizedCredit": 0.0,
    "email": "customer32@test.com",
    "tolerance": 0.15,
    "availableBalance": 5800.00
}
```

## Checking operations in a customer credit account

The [Get account statements](https://developers.vtex.com/docs/api-reference/customer-credit-api#get-/api/creditcontrol/accounts/-creditAccountId-/statements) endpoint can be used to track operations performed on a customer credit account, such as:

- [Customer credit limit modification](#tracking-a-credit-limit-change-operation)
- [Tolerance percentage modification](#tracking-a-tolerance-value-change-transaction)
- [Invoice Issuance](#tracking-a-credit-invoice-creation)
- [Invoice payment](#tracking-a-credit-invoice-payment)

In this request, you must send the account identification (`id`) as a path parameter:

__GET - Get account statements__

`https://{accountName}.{environment}.com.br/api/creditcontrol/accounts/fe60ff40-d1cb-11ee-a0ed-87f4fcc03446/statements`

If you send the `id` of a new account or one without an operation type, the response body of the request will not present any value, as shown below:

Response body

```json
{
    "statements": [],
    "currentBalance": 0.0,
    "intervalBalance": 0.0,
    "previousBalance": 0.0
}
```

### Tracking a credit limit change operation

When the credit limit of a customer credit account is modified via VTEX Admin or through the [Change credit limit of an account](https://developers.vtex.com/docs/api-reference/customer-credit-api#put-/api/creditcontrol/accounts/-creditAccountId-/creditlimit) endpoint, it is possible to identify the new value indicated and when the operation was carried out.

See below a scenario where an initial credit limit USD 10.000 is reduced to USD 9.000 and then increased to USD 12.000. The tolerance value configured on this account is 10%.

#### FIRST OPERATION: Decreasing credit limit from USD 10.000 to USD 9.000

__PUT - Change credit limit of an account__

`https://{accountName}.{environment}.com.br/api/creditcontrol/accounts/fe60ff40-d1cb-11ee-a0ed-87f4fcc03446/creditlimit`

Request body

```json
{
  "value": 9.000
}
```

__GET - Get account statements__

`https://{accountName}.{environment}.com.br/api/creditcontrol/accounts/fe60ff40-d1cb-11ee-a0ed-87f4fcc03446/statements`

Response body

```json
{
    "statements": [
        {
            "value": -1100.0,
            "date": "2024-02-26T13:29:08.3978356Z",
            "origin": "Credit"
        }
    ],
    "currentBalance": 0.0,
    "intervalBalance": -1100.0,
    "previousBalance": 0.0
}
```

Note that the value displayed in the `value` field is indicated by a negative sign and 1100.0, instead of 1000.0 which would correspond to how much the credit limit was reduced. This occurs because the endpoint returns the sum of the amount of the reduced credit limit and the percentage of credit tolerance applied to it, in this case, 10% over 1000.0 (100.0).

#### SECOND OPERATION: Increasing credit limit from USD 9.000 to USD 12.000

__PUT - Change credit limit of an account__

`https://{accountName}.{environment}.com.br/api/creditcontrol/accounts/fe60ff40-d1cb-11ee-a0ed-87f4fcc03446/creditlimit`

Request body

```json
{
   "value": 12.000
}
```

__GET - Get account statements__

`https://{accountName}.{environment}.com.br/api/creditcontrol/accounts/fe60ff40-d1cb-11ee-a0ed-87f4fcc03446/statements`

Response body

```json
{
    "statements": [
        {
            "value": -1100.0,
            "date": "2024-02-26T17:08:49.3904874Z",
            "origin": "Credit"
        },
        {
            "value": 3300.0,
            "date": "2024-02-26T17:08:55.3123304Z",
            "origin": "Credit"
        }
    ],
    "currentBalance": 0.0,
    "intervalBalance": 2200.0,
    "previousBalance": 0.0
}
```

As in the credit limit-reducing operation, the value present in the "value" field (3300.0) is indicated by the sum of the value added to the credit limit (3000.0) and the percentage of credit tolerance applied to the operation, 10% on 3000.0 (300.0).

> ℹ️ The "intervalBalance" field is responsible for showing the balance between all amounts reduced and added in operations performed on a customer credit account since its opening. In this case, 2200.0 (3300.0 - 1100.0).

### Tracking a tolerance value change transaction

When the credit tolerance value in a customer credit account is modified via VTEX Admin or through the [Change tolerance of an account](https://developers.vtex.com/docs/api-reference/customer-credit-api#put-/api/creditcontrol/accounts/-creditAccountId-/tolerance) endpoint, it is possible to identify the new value indicated and when the operation was carried out.

See below a scenario where an initial credit tolerance of 10% is reduced to 0%, and then increased to 25%. The credit limit value configured on this account is 5.000.

#### FIRST OPERATION: Decreasing credit tolerance from 10% to 0%

__PUT - Change tolerance of an account__

`https://{accountName}.{environment}.com.br/api/creditcontrol/accounts/fe60ff40-d1cb-11ee-a0ed-87f4fcc03446/tolerance`

Request body

```json
{
  "value": 0
}
```

__GET - Get account statements__

`https://{accountName}.{environment}.com.br/api/creditcontrol/accounts/fe60ff40-d1cb-11ee-a0ed-87f4fcc03446/statements`

Response body

```json
{
    "statements": [
        {
            "value": -500.0,
            "date": "2024-02-26T20:04:27.7754907Z",
            "origin": "Credit"
        }
    ],
    "currentBalance": 0.0,
    "intervalBalance": -500.0,
    "previousBalance": 0.0
}
```

Note that the value displayed in the `value` field is indicated by a negative sign (reduced tolerance percentage) and 500.0, instead of the percentage value 0. This occurs because the endpoint returns the value referring to the percentage reduced in the operation applied to the total amount of credit limit registered on the account. That is, a 10% tolerance reduction over 5000.0 equals 500.0.

#### SECOND OPERATION: Increasing credit tolerance from 0% to 25%

__PUT - Change tolerance of an account__

`https://{accountName}.{environment}.com.br/api/creditcontrol/accounts/fe60ff40-d1cb-11ee-a0ed-87f4fcc03446/tolerance`

Request body

```json
{
  "value": 0.25
}
```

__GET - Get account statements__

`https://{accountName}.{environment}.com.br/api/creditcontrol/accounts/fe60ff40-d1cb-11ee-a0ed-87f4fcc03446/statements`

Response body

```json
{
    "statements": [
        {
            "value": -500.0,
            "date": "2024-02-26T20:04:27.7754907Z",
            "origin": "Credit"
        },
        {
            "value": 1250.0,
            "date": "2024-02-26T22:39:53.8090863Z",
            "origin": "Credit"
        }
    ],
    "currentBalance": 0.0,
    "intervalBalance": 750.0,
    "previousBalance": 0.0
}
```

In the same way, as in the operation in which the tolerance percentage was reduced, the value present in the `value` field (1250.0) represents the added percentage of 25% applied to the credit limit registered in the account (5000.0).

### Tracking a credit invoice creation

After the customer makes a purchase in the store using customer credit as a payment method and the order is [invoiced](https://help.vtex.com/en/tutorial/how-to-invoice-an-order--7p1h852V5t54KyscpgxE2v), it is possible to check the credit operation information on the [Get account statements](https://developers.vtex.com/docs/api-reference/customer-credit-api#get-/api/creditcontrol/accounts/-creditAccountId-/statements) endpoint.

Unlike situations involving credit limit and tolerance changes, in the response body of this type of operation, the `origin` field is indicated as `invoice` and a new object named `metadata` is shown containing the following information:

- `transactionId`: Transaction identification.
- `orderId`: Identification of the order for which the invoice was created.
- `numberOfInstallments`: Number of invoices created to pay for the transaction. invoices created to pay for the order.

See the example below for the response body information related to the operation of a purchase made worth USD 15.

__GET - Get account statements__

`https://{accountName}.{environment}.com.br/api/creditcontrol/accounts/fe60ff40-d1cb-11ee-a0ed-87f4fcc03446/statements`

Response body

```json
{
    "statements": [
        {
        "value": -15.0,
            "date": "2024-02-26T14:39:54.7141907Z",
            "origin": "Invoice",
            "metadata": {
                "transactionId": "ED01C38CD4C949C2BCDFDB2C461C80F1",
                "orderId": "1413590513132-01",
                "numberOfInstallments": 1
            }
        }
    ],
    "currentBalance": 0.0,
    "intervalBalance": -8.01,
    "previousBalance": 0.0
}
```

### Tracking a credit invoice payment

To confirm when a customer credit invoice has been paid by the customer you can also use the [Get account statements](https://developers.vtex.com/docs/api-reference/customer-credit-api#get-/api/creditcontrol/accounts/-creditAccountId-/statements) endpoint.

See below the response body containing the invoice information after order payment.

__GET  - Get account statements__

`https://{accountName}.{environment}.com.br/api/creditcontrol/accounts/fe60ff40-d1cb-11ee-a0ed-87f4fcc03446/statements`

Response body

```json
{
    "statements": [
        {
        "value": 8.01,
            "date": "2024-02-26T14:47:15.9276873Z",
            "origin": "Payment",
            "metadata": {
                "transactionId": "ED01C38CD4C949C2BCDFDB2C461C80F1",
                "installment": 1
            }
        }
    ],
    "currentBalance": 0.0,
    "intervalBalance": 0.0,
    "previousBalance": 0.0
}
```

## Sharing credit with dependents

You can also share the credit available in a customer account with other customers. To do this, you must add a dependent — also known as an account holder — to the account.

> ℹ️ Credit sharing between account holders registered in an account occurs in such a way that the sum of all purchases made by them through Customer Credit cannot exceed the amount of credit available in the account.

### Adding a new account holder

To add the new account holder to the customer credit account, use the VTEX Admin or the [Add an account holder](https://developers.vtex.com/docs/api-reference/customer-credit-api#post-/api/creditcontrol/accounts/-creditAccountId-/holders) endpoint. In this request, you must send the account identification (`id`) as a path parameter.

See an example below using the account `fe60ff40-d1cb-11ee-a0ed-87f4fcc03446`:

__POST - Add an account holder__

`https://{accountName}.{environment}.com.br/api/creditcontrol/accounts/fe60ff40-d1cb-11ee-a0ed-87f4fcc03446/holders`

Request body

```json
{
  "claims": {
    "email": "customertestholder1@test.com"
  }
}
```

The endpoint will return information about the creation of the new holder such as:

- `level`: Holder hierarchy. The value 2 indicates that the holder is a dependent of the account's main holder.
- `email`: Holder email.
- `id`: Holder identification.
- `createdAt`: Date of appointment of the holder.

Response body

```json
{
    "level": 2,
    "claims": {
        "email": "customertestholder1@test.com"
    },
    "id": "78d22849ad844ae5a57ef1715de73467",
    "createdAt": "2024-02-27T14:38:36.0027682Z"
}
```

You can also access your VTEX Admin (__Apps > Customer Credit > Accounts__) and click the desired account to verify that the new holder was added.

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Integration-Guides/customer-credit-integration-guide/customer-credit-account_2.png)

### Removing an account holder

To remove a holder from a customer credit account and prevent them from using the available credit, you can use the VTEX Admin or the [Delete an account holder](https://developers.vtex.com/docs/api-reference/customer-credit-api#delete-/api/creditcontrol/accounts/-creditAccountId-/holders/-holderId-) endpoint. In this request, you must send the account identification (`id`) and the holder identification (`id` obtained in the VTEX Admin or in the response body of the [Add an account holder](https://developers.vtex.com/docs/api-reference/customer-credit-api#post-/api/creditcontrol/accounts/-creditAccountId-/holders) endpoint as path parameters.

See an example below using the account `fe60ff40-d1cb-11ee-a0ed-87f4fcc03446` and the holder `78d22849ad844ae5a57ef1715de73467`:

__DEL - Delete an account holder__

`https://{accountName}.{environment}.com.br/api/creditcontrol/accounts/fe60ff40-d1cb-11ee-a0ed-87f4fcc03446/holders/78d22849ad844ae5a57ef1715de73467`

The endpoint will return the holder's identification, confirming that it was deleted from the account.

Response body

```json
{
    "id": "78d22849ad844ae5a57ef1715de73467"
}
```

You can also access your VTEX Admin (__Apps > Customer Credit > Accounts__) and click on the desired account to verify that the new holder was removed.

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Integration-Guides/customer-credit-integration-guide/customer-credit-account_3.png)

## Checking all customer credit accounts of a store

To check information about all customer credit accounts registered in your store, you can use the VTEX Admin or the [Search all accounts](https://developers.vtex.com/docs/api-reference/customer-credit-api#get-/api/creditcontrol/accounts) endpoint.

__GET - Search all accounts__

`https://{accountName}.{environment}.com.br/api/creditcontrol/accounts/`

Response body

```json
{
    "data": [
        {
            "id": "07D0F8272B6D77F1E68B",
            "balance": 0.0,
            "status": "Open",
            "creditLimit": 1000.0,
            "updatedAt": "2021-06-28T21:33:46.70945Z",
            "createdAt": "2020-04-15T01:23:54.4690229Z",
            "description": "",
            "availableCredit": 1000.0,
            "preAuthorizedCredit": 0.0,
            "email": "isadora.bombonatti@vtex.com.br",
            "tolerance": 0.0,
            "availableBalance": 1000.0
        },
        {
            "id": "E93480BCE84892A336F3",
            "balance": 0.0,
            "status": "Open",
            "creditLimit": 2000.0,
            "updatedAt": "2021-06-28T21:33:46.8344386Z",
            "createdAt": "2020-05-21T22:42:37.8764106Z",
            "description": "",
            "availableCredit": 2000.0,
            "preAuthorizedCredit": 0.0,
            "email": "contato@diasbruno.com",
            "tolerance": 0.0,
            "availableBalance": 2000.0
        },
        {
            "id": "B07403D8311D642477F4",
            "balance": 0.0,
            "status": "Open",
            "creditLimit": 2000.0,
            "updatedAt": "2021-06-28T21:33:47.1156945Z",
            "createdAt": "2020-07-23T20:26:33.894492Z",
            "description": "",
            "availableCredit": 2000.0,
            "preAuthorizedCredit": 0.0,
            "email": "joao.rios@vtex.com.br",
            "tolerance": 0.0,
            "availableBalance": 2000.0
        },
…      
    ],
    "summary": {
        "count": 35
    }
}
```

> ℹ️ The `count` field displays the number of customer credit accounts registered in the store.

## Closing a customer credit account

If you wish to stop offering credit to a specific customer, you must close the account through VTEX Admin or the [Close an account](https://developers.vtex.com/docs/api-reference/customer-credit-api#delete-/api/creditcontrol/accounts/-creditAccountId-) endpoint. In this request, you must send the account identification (`id`) as a path parameter.

Additionally, you can use the queries below (individually or combined) in the URL to refine your account search:

- By the location of the accounts in the list (quantity of accounts): `?from={int}&to={int}`
- By status: `?status={Open, Closed or Cancelled}`
- By email: `?email={string}`

> ⚠️ If your store has more than 20 customer credit accounts and you do not use any queries in the call, only the first 20 account records will appear in the response body.

See an example below using the account `fe60ff40-d1cb-11ee-a0ed-87f4fcc03446`:

__DEL - Close an account__

`https://{accountName}.{environment}.com.br/api/creditcontrol/accounts/c5886660-d598-11ee-ac7f-a50b38956bb7`

The endpoint will return the information for the account that was deleted, displaying the `status` field as `Closed`.

Response body

```json
{
    "id": "c5886660-d598-11ee-ac7f-a50b38956bb7",
    "balance": 0.0,
    "document": "98765432101",
    "status": "Closed",
    "documentType": "CPF",
    "creditLimit": 3000.0,
    "updatedAt": "2024-02-27T17:52:52.842757Z",
    "createdAt": "2024-02-27T17:51:03.5303894Z",
    "description": "",
    "availableCredit": 3000.0,
    "preAuthorizedCredit": 0.0,
    "email": "customerclosed@test.com",
    "tolerance": 0.0,
    "availableBalance": 3000.0
}
```

You can also access your VTEX Admin (__Apps > Customer Credit > Accounts__) to verify that the account was deleted.

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Integration-Guides/customer-credit-integration-guide/customer-credit-account_4.png)

> ⚠️ Once closed, a Customer Credit account cannot be reopened again and all invoices, statements, and additional dependents data will be deleted. However, after completing the account closure, if you wish, you can [open a new account](https://docs.google.com/document/d/10EJmh9ELupEvoIx5ynVahtcl3yYNdXjP6vtgDTyIYyQ/edit#heading=h.yqy2l76230c2](https://developers.vtex.com/docs/api-reference/customer-credit-api#post-/api/creditcontrol/accounts) for the customer using the same email as the closed account.
