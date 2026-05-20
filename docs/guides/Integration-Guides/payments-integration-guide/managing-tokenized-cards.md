---
title: "Managing tokenized cards"
slug: "managing-tokenized-cards"
hidden: false
createdAt: "2025-12-12T00:00:00.00Z"
updatedAt: "2025-12-12T00:00:00.00Z"
---

Tokenized card management is an essential component in payment integrations that require migration, verification, or synchronization of information between systems. To address these scenarios, VTEX offers the following resources:

   - [Querying tokenized card information](#querying-tokenized-card-information)
   - [Importing external tokens into the Card Token Vault (CTV)](#importing-tokens-into-the-card-token-vault-ctv)

> ⚠️ Card tokenization is in the testing phase (Closed Beta), which means that only specific clients can access it at this time. If you'd like to implement it in the future, contact our [Support](https://support.vtex.com/hc/en-us/) team.

## Querying tokenized card information

The VTEX payment gateway provides an endpoint that allows you to retrieve non-sensitive information from a customer's saved cards. The response to this request includes the card's default information, such as the card network, expiration date, and basic identifiers. If the card already has an associated token, the response also returns the token's metadata.

To query this information, use the [Get card data](https://developers.vtex.com/docs/api-reference/payments-gateway-api#get-/api/payments/pvt/account/-cardId-) endpoint.

## Importing tokens into the Card Token Vault (CTV)

Importing tokens into the CTV is recommended for migration scenarios when tokens generated and stored in an external system need to be replicated in the VTEX environment in a structured and secure manner.

### Prerequisites

Before starting the import process, make sure you have the following:

   - Valid authentication credentials to access the [Card Token Vault API](https://developers.vtex.com/docs/api-reference/card-token-vault-api) endpoints.
   - An `.XLSX` file with a maximum size of 20 MB, containing the necessary information to register the token. The first row of the `.XLSX` file must include the following headers:

| `accountName` | `providerId` | `profileId` | `paymentSystemName` | `cardFirstDigits` | `cardLastDigits` | `cardAddressType` | `cardAddressPostalCode` | `cardAddressStreet` | `cardAddressNeighborhood` | `cardAddressCity` | `cardAddressState` | `cardAddressCountry` | `cardAddressNumber` | `cardAddressComplement` | `cardHolderName` | `tokenType` | `tokenValue` | `tokenExpiration` | `tokenLabel` | `tokenProviderCardTokenId` | `tokenUseCvvForAuthorization` | `tokenHref` | `extraData` | `email` | `shopperId` |

> ℹ️ The `extraData` column must contain information in JSON format or an empty JSON (`{}`).

> ⚠️ Each account can run only one import at a time. If an import is in progress, wait for it to finish before starting a new import.


## Import instructions

Follow the steps below to import tokens into the [Card Token Vault (CTV)](https://developers.vtex.com/docs/api-reference/card-token-vault-api):

1. Save the `.XLSX` file in a local repository.
2. Submit the `.XLSX` file information to the CTV using the [Import card tokens](https://developers.vtex.com/docs/api-reference/card-token-vault-api#post-/api/card-token-vault/tokens/import) endpoint. A returned `id` field and a status code `202 Accepted` in the response body indicate that the file was received successfully.
3. With the `id` from the previous step, use the [Get card token import status](https://developers.vtex.com/docs/api-reference/card-token-vault-api#get-/api/card-token-vault/tokens/import/-importId-) endpoint to query the processing status of the file. Possible status values are:
   - `CREATED`
   - `RUNNING`
   - `FAILED`
   - `DONE`

4. Repeat calls to the [Get card token import status](https://developers.vtex.com/docs/api-reference/card-token-vault-api#get-/api/card-token-vault/tokens/import/-importId-) endpoint until the status returns `DONE` or `FAILED`.
   - If the status returns `FAILED`, get the error report through the [Get card token import report](https://developers.vtex.com/docs/api-reference/card-token-vault-api#get-/api/card-token-vault/tokens/import/-importId-/report) endpoint, and correct the information in the `.XLSX` file. Then restart the import process.
   - If the status returns `DONE`, the import was completed successfully, and no further action is required.