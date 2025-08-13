---
title: "How the integration protocol between VTEX and antifraud companies works"
slug: "how-the-integration-protocol-between-vtex-and-antifraud-companies-works"
hidden: false
createdAt: "2022-12-07T17:09:28.603Z"
updatedAt: "2022-12-07T18:17:43.140Z"
---

The Anti-fraud Provider Protocol is the integration protocol between VTEX and companies that provide anti-fraud services.

Through it, VTEX offers a public contract available to all providers that wish to integrate into our platform. As a result, providers become more autonomous regarding such integration.

The protocol has the following features:

- Processing of synchronous and asynchronous risk analysis.
- Webhook for status notification.

> ⚠️ The Anti-fraud Provider Protocol can be used at VTEX only for payment transactions carried out with credit, [debit](https://developers.vtex.com/docs/guides/implementing-a-pre-analysis-antifraud-flow-for-debit-card-transactions), and gift cards.

## Concepts

**Provider**: system or provider that offers the anti-fraud risk analysis service.

**Anti-fraud Provider Protocol**: integration protocol developed by VTEX.

**Connector**: name of the integration partner provider.

## Implementation prerequisites

### 1. Business partnership agreement

To make your anti-fraud service available at VTEX, you must sign a partnership agreement that is specific to financial services covering the details of this subject and platform regulations. If you do not have a partnership agreement yet but are interested in becoming a payment provider, contact our team through our [website](https://vtex.com/us-en/partner).

### 2. Access to a VTEX environment

After obtaining a business partnership agreement with VTEX, you will receive all information to access the VTEX environment, where you can publish, homologate, update, and have access to our support when developing and maintaining a connector.

If the partner is a SI (Service Implementer) developing integrations for clients or other payment providers, the VTEX account of the main provider must be used and not the account of the contractor agency.

## Integration steps

### 1. Implementing the protocol

Before setting up the VTEX environment, the provider must implement the backend service required to process the anti-fraud services (API). For more information, access the [Anti-fraud Provider Protocol API](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol).

> ⚠️ You can also access our [template on GitHub](https://github.com/vtex-apps/antifraud-provider-example) to help you quickly develop your anti-fraud connector using the Anti-fraud Provider Protocol and VTEX IO.

### 2. Install the Anti-fraud Provider Tester App

After receiving the access data and deploying the backend, the provider can access the approval tool through VTEX Admin. If you still do not have the Anti-fraud Provider Tester App installed in your store, you need to follow these steps:

1. In the VTEX Admin, go to **Apps > Apps Store**.
2. Type **Antifraud Provider** in the search bar at the bottom of the page and click on `Install`.
3. After that, you will be redirected to the VTEX APP Store. Click the `GET APP` button at the top right corner of the page.
4. Then, on the popup screen, type your account's name (with lowercase and no space in between) and click the `CONFIRM` button.
5. Click `INSTALL` to complete the installation process.
   ![Apps Image](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Integration-Guides/payments-integration-guide/how-the-integration-protocol-between-vtex-and-antifraud-companies-works-0_46.png)

With the app installed, go to **Apps > Installed Apps** and click on **Antifraud Provider**, or access `https://{{AccountName}}.myvtex.com/admin/test-suite/antifraud-provider`, replacing `{{AccountName}}` with the name of your platform account.

### 3. Initial settings

In the Anti-fraud Provider Tester app environment, fill in the fields as indicated below:

- **Connector Name**: name you want to give to your connector within VTEX.
- **Service URL**: URL of your provider service. This URL will be the base address of the protocol and must follow the format determined by it. For example, if the service URL is `http://10.10.10.10`, the full URL for the endpoint *transactions* will be `http://10.10.10.10/transactions`.
- **API key**: "X-PROVIDER-API-AppKey" value of your provider's request header for testing purposes.
- **API token**: "X-PROVIDER-API-AppToken" value of your provider's request header for testing purposes.

![Anti-fraud test suite](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Integration-Guides/payments-integration-guide/how-the-integration-protocol-between-vtex-and-antifraud-companies-works-2_53.png)

> ⚠️ It is important to remember that all HTTPS communication should run exclusively on TLS 1.2. Your provider must be prepared to receive two headers (**X-PROVIDER-API-AppKey** and **X-PROVIDER-API-AppToken**), as this combination is used to identify a merchant. All settings that need to be made by the merchant should persist in your provider. The only configuration that VTEX saves about merchants is the combination of X-PROVIDER-API-AppKey and X-PROVIDER-API-AppToken credentials.

After completing the fields correctly, the system will check the approved transactions through a call to the  ***/transactions*** endpoint of your provider. See the API reference [here](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#post-/transactions).

### 4. Testing

To ensure the correct operation of the anti-fraud, a series of tests are necessary. You can choose how many tests you want to run at a time. However, for your integration to be analyzed by the VTEX team, **all tests must have been performed and approved**. See below the description of each test:

- **Authorize**: test performed in two steps.

  - A [Send Anti-fraud Data](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#post-/transactions) request (`{{ServiceURL}}/transactions`) is sent. The expected value for `status` in the response body is `received`.
  - A [Get Anti-fraud Status](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#get-/transactions/-transactions.id-) request (`{{ServiceURL}}/transactions/transactionId`), with the Transaction ID generated in the previous step, is sent. The expected value for `status` in the response body is `approved`.
- **Denied**: test performed in two steps.

  - A [Send Anti-fraud Data](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#post-/transactions) request (`{{ServiceURL}}/transactions`) is sent. The expected value for `status` in the response body is `received`.
  - A [Get Anti-fraud Status](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#get-/transactions/-transactions.id-) request (`{{ServiceURL}}/transactions/transactionId`), with the Transaction ID generated in the previous step, is sent. The expected value for `status` in the response body is `denied`.
- **AsyncApproved**: test performed in three steps.

  - A [Send Anti-fraud Data](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#post-/transactions) request (`{{ServiceURL}}/transactions`) is sent. The expected value for `status` in the response body is `received`.
  - A [Get Anti-fraud Status](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#get-/transactions/-transactions.id-) request (`{{ServiceURL}}/transactions/transactionId`), with the Transaction ID generated in the previous step, is sent. The expected value for `status` in the response body is `undefined`.
  - After 10 seconds, a [Get Anti-fraud Status](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#get-/transactions/-transactions.id-) request (`{{ServiceURL}}/transactions/transactionId`), with the Transaction ID generated in the first step, is sent again. The expected value for `status` in the response body is `approved`.
- **AsyncDenied**: test performed in three steps.

  - A [Send Anti-fraud Data](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#post-/transactions) request (`{{ServiceURL}}/transactions`) is sent. The expected value for `status` in the response body is `received`.
  - A [Get Anti-fraud Status](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#get-/transactions/-transactions.id-) request (`{{ServiceURL}}/transactions/transactionId`), with the Transaction ID generated in the previous step, is sent. The expected value for `status` in the response body is `undefined`.
  - After 10 seconds, a [Get Anti-fraud Status](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#get-/transactions/-transactions.id-) request (`{{ServiceURL}}/transactions/transactionId`), with the Transaction ID generated in the first step, is sent again. The expected value for `status` in the response body is `denied`.
- **HookApproved**: test performed in four steps.

  - A [Send Anti-fraud Data](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#post-/transactions) request (`{{ServiceURL}}/transactions`) is sent. The expected value for `status` in the response body is `received`.
  - A [Get Anti-fraud Status](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#get-/transactions/-transactions.id-) request (`{{ServiceURL}}/transactions/transactionId`), with the Transaction ID generated in the previous step, is sent. The expected value for `status` in the response body is `undefined`.
  - Afterwards, 10 seconds is waited for the anti-fraud provider to POST the URL sent in the *hook* field of the first step (the POST content should contain the response obtained in that same step).
  - A [Get Anti-fraud Status](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#get-/transactions/-transactions.id-) request (`{{ServiceURL}}/transactions/transactionId`), with the Transaction ID generated in the first step, is sent again. The expected value for `status` in the response body is `approved`.
- **HookDenied**: test performed in four steps.

  - A [Send Anti-fraud Data](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#post-/transactions) request (`{{ServiceURL}}/transactions`) is sent. The expected value for `status` in the response body is `received`.
  - A [Get Anti-fraud Status](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#get-/transactions/-transactions.id-) request (`{{ServiceURL}}/transactions/transactionId`), with the Transaction ID generated in the previous step, is sent. The expected value for `status` in the response body is `undefined`.
  - Afterwards, 10 seconds is waited for the anti-fraud provider to POST the URL sent in the *hook* field of the first step (the POST content should contain the response obtained in that same step).
  - A [Get Anti-fraud Status](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#get-/transactions/-transactions.id-) request (`{{ServiceURL}}/transactions/transactionId`), with the Transaction ID generated in the first step, is sent again. The expected value for `status` in the response body is `denied`.

When you click the **RUN TESTS** button, the Anti-fraud Provider Tester App will apply the selected tests in your integration to the different possible scenarios. To run them your service must be in HTTPS.

![Antifraud test suite2](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Integration-Guides/payments-integration-guide/how-the-integration-protocol-between-vtex-and-antifraud-companies-works-3_75.png)

For each Anti-fraud Provider Protocol test, we send a specific ID end to return the expected response. They are:

- **Authorize**: ID with end 1.
- **Denied**: ID with end 2.
- **AsyncApproved**: ID with end 3.
- **AsyncDenied**: ID with end 4.
- **HookApproved**: ID with end 5.
- **HookDenied**: ID with end 6.

### 5. Results

After executing the tests, all results (successes or failures) will be displayed in the app environment.

A list with detailed information about the events that occurred during the tests can be accessed by clicking on **Show logs**. This will allow identifying and correcting possible errors, in case of test failure.
 
![Antifraud test suite3](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Integration-Guides/payments-integration-guide/how-the-integration-protocol-between-vtex-and-antifraud-companies-works-4_107.png)
  
![Antifraud test suite4](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Integration-Guides/payments-integration-guide/how-the-integration-protocol-between-vtex-and-antifraud-companies-works-5_111.png)
 
When your integration has successfully passed all tests, please open a ticket in our [VTEX support](https://help.vtex.com/pt/support). However, before opening the ticket, make sure you have the following information available:

- **Connector Name**: a description of the provider. Use max. 16 alphanumeric characters. This name can not be modified after being published.
- **Partner contact**: partner's email address. We will use this address to communicate changes and new features of our protocol.
- **Production Service Provider Endpoint**: the base path that will be used for API calls to the provider (e.g., `https://vtex.pagseguro.com`). It has to respond to the route `{{serviceUrl}}/manifest`. This endpoint must be publicly available.
- **Sandbox Service Provider Endpoint**: the base path that will be used in test mode for API calls to the provider (e.g., `https://sandboxserviceproviderendpoint.com`).
- **Owner account**: the VTEX account name which will be used in callback requests. This account must be available at *{account}.myvtex.com*.
- **Allowed Accounts**: describe which VTEX accounts from this provider will be available (all accounts or specific accounts).
- **New Payment methods**: inform if this connector supports a payment method that is not yet available in the VTEX Admin.
- **New Payment method purchase flow**: if a “New Payment method” is supported, inform whether it works with Redirect or Payment App. For more information, access [Purchase Flows](https://developers.vtex.com/docs/guides/payments-integration-purchase-flows).

The SLA required for the VTEX payments team to carry out the homologation is 30 days.

> ⚠️ VTEX Antifraud provider protocol supports payment transactions carried out using credit, debit, and gift cards. If you want to allow gift card payment transactions in your anti-fraud provider, set the `allowAntifraudOnGiftCard` field to `true` in the manifest.

## VTEX Credentials

When calling `CallbackURL`, you must specify the authentication headers, which in VTEX are **X-VTEX-API-AppKey** and **X-VTEX-API-AppToken**. You can find these credentials in VTEX License Manager. These credentials are used by the Anti-fraud Provider only.

Use the `https://{{AccountName}}.myvtex.com/admin/license-manager/#/home` URL, replacing `{{AccountName}}` with your account name. Then follow the instructions of [this tutorial](https://help.vtex.com/en/tutorial/api-keys--2iffYzlvvz4BDMr6WGUtet) to learn how to create appKeys and appTokens on our platform.

## Settings in VTEX stores

Once the integration with your anti-fraud is approved, a connector will be made available for VTEX merchants to configure it on their respective stores. To do this, in addition to the contract with your company, the store will need two keys in hand: "X-PROVIDER-API-AppKey" and "X-PROVIDER-API-AppToken".

An example of how the anti-fraud settings screen will look for the VTEX store:
 
![gateway affiliations screen](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Integration-Guides/payments-integration-guide/how-the-integration-protocol-between-vtex-and-antifraud-companies-works-6_138.png)
 
These keys should be made available by you and will serve to identify the store that hired and is using your anti-fraud service.

## Cardholder Document Configuration

During payment transactions analysis, some anti-fraud providers may choose not to use additional information such as the cardholder’s personal identification. In these cases, the merchant has the autonomy to decide whether or not to request this document from his customer during the checkout procedure.

> ⚠️ The configuration option **Cardholder document field** will only be available to the merchant if the anti-fraud provider declares in its [manifest](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#get-/manifest), the cardholder document field (`cardholderDocument`) as `optional`. Learn more at [Cardholder Document Configuration](https://developers.vtex.com/docs/guides/cardholder-document-configuration).

To set up the cardholder document field, follow the steps below:

1. In the VTEX Admin, go to **Store Settings > Payments > Settings**, or type **Settings** in the search bar at the top of the page.
2. In the **Gateway affiliations** tab, click on the `+` button.
3. Select the anti-fraud provider you wish to use.
4. On the anti-fraud configuration screen, fill in the requested information.
5. In **Cardholder document field**, select one of the following options:

   - **Display as a required field**: the field will be displayed at checkout with the information “required”, and the customer must fill in the cardholder information to complete the order.
   - **Display as an optional field**: the field will be displayed at checkout with the information “optional”, and the customer will decide whether or not to fill in it. The order can be completed even if the field is not filled in.
   - **Hide Field**: the field will not be displayed at checkout.
6. Click on **Save**.

After following the steps indicated, the settings made above may take up to 10 minutes to appear at your store's checkout.
