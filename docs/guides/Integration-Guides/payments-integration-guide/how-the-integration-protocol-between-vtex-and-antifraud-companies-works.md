---
title: "How the integration protocol between VTEX and antifraud companies works"
slug: "how-the-integration-protocol-between-vtex-and-antifraud-companies-works"
hidden: false
createdAt: "2022-12-07T17:09:28.603Z"
updatedAt: "2022-12-07T18:17:43.140Z"
---

## What is the Antifraud Provider Protocol?

The Antifraud Provider Protocol is the integration protocol between VTEX and companies that provide antifraud services.

Through it, VTEX offers a public contract available to all providers that wish to integrate into our platform. Thus, providers gain more autonomy.

The protocol has the following features:

- Processing of synchronous and asynchronous risk analysis.
- Webhook for status notification.

You can find references to the protocol API [here](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#post-/pre-analysis).

## Concepts

**Provider**: An antifraud system or provider that offers this type of service.

**Antifraud Provider Protocol**: integration protocol developed by VTEX.

**Connector**: name of the integration partner provider.

## First steps

Next, we will present step-by-step information on integrating payments with VTEX.

### 1. Commercial phase

The first step is the commercial contact with VTEX, which should be done through [our site](http://partner.vtex.com). Upon completion of the business agreement, the provider is registered and receives an email with the data needed to access the environment of the antifraud provider, where you can make the necessary settings and tests.

### 2. Implementing the protocol

Before setting up the VTEX environment, the provider must implement the back-end service required to process the antifraud (API). More information about the protocol API [here](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#post-/pre-analysis).

### 3. Antifraud Provider Administration Panel

After receiving the access data and deploying the backend, the provider can access the approval tool through VTEX Admin. To do this, you must install the Antifraud Provider App from the Apps menu:
 
![Apps Image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/how-the-integration-protocol-between-vtex-and-antifraud-companies-works-0.png)

Click on the installed app or access `https://{{AccountName}}.myvtex.com/admin/antifraud-provider`, replacing `{{AccountName}}` with the name of your account on the platform. In this environment, you can register the provider back-end configuration data and perform integration tests.
![gatewayio](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/how-the-integration-protocol-between-vtex-and-antifraud-companies-works-1.png)

### 4. Initial settings

![Antifraud test suite](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/how-the-integration-protocol-between-vtex-and-antifraud-companies-works-2.png)
When you access the environment through the link described in the previous item, you will see a form. Fill in the fields as indicated below:

- **Connector Name**: fill in with the name you want to give to your connector within VTEX. This field can be edited whenever necessary.

- **Service URL**: set the URL of your provider service. This URL will be the base address of the protocol and must follow the format determined by it. For example, if the service URL is `http://10.10.10.10`, the full URL for the endpoint *transactions* will be `http://10.10.10.10/transactions`.

- **Application Key**: Enter the "X-PROVIDER-API-AppKey" value of your provider's request header for testing purposes.

- **Application Token**: Enter the "X-PROVIDER-API-AppToken" value of your provider's request header for testing purposes.

[block:callout]
{
  "type": "warning",
  "body": "It's important to remember that all HTTPS communication should run exclusively on TLS 1.2.\n\nYour provider should expect two headers <strong>X-PROVIDER-API-AppKey</strong> and <strong>X-PROVIDER-API-AppToken</strong>. This combination should identify a merchant. All settings that need to be made by the merchant should persist in your provider. The only configuration that VTEX saves about merchants is the combination of X-PROVIDER-API-AppKey and X-PROVIDER-API-AppToken credentials."
}
[/block]

After completing the fields correctly, the system will check the approved transactions through a call to the ***/transactions*** endpoint of your provider. See the API reference [here](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#post-/pre-analysis).

The tests that should be done in your integration before sending it to VTEX evaluation are displayed in the next module. You can select which tests you want to run, but for your integration to go through the analysis of our team, **all tests need to be done**. Therefore, we recommend that all of them remain selected.
 
![Antifraud test suite2](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/how-the-integration-protocol-between-vtex-and-antifraud-companies-works-3.png)

### 5. Testing

When you click the **Execute tests** button, the Antifraud Provider will apply the tests in your integration to the different possible scenarios. It's important to remember that **all of them are required**. To run them your service must be in HTTPS. The tests are:

- **Authorize**: This test is done in two steps. First, we need the *received* status in response to the *Send Antifraud Data* request for `{{ServiceURL}}/transactions`. We then send a *Get Antifraud Status* request (with the Transaction ID generated in the previous step) to `{{ServiceURL}}/transactions/transactionId`, expecting the *approved* status as response.

- **Denied**: Like the previous one, this test is also done in two steps. First, we need the *received* status in response to the *Send Antifraud Data* request for `{{ServiceURL}}/transactions`. We then send a *Get Antifraud Status* request (with the Transaction ID generated in the previous step) to `{{ServiceURL}}/transactions/transactionId`, waiting the status *denied* as response.

- **AsyncApproved**: This test is divided into three steps. First, we need the *received* status in response to the *Send Antifraud Data* request for `{{ServiceURL}}/transactions`. We then send a *Get Antifraud Status* request (with the Transaction ID generated in the previous step) to `{{ServiceURL}}/transactions/transactionId`, waiting for the status *undefined* as response. Finally, after 10 seconds, we send another *Get Antifraud Status* request (with the same Transaction ID generated in the first step) to `{{ServiceURL}}/transactions/transactionId`, but this time waiting for the *approved* status in response.

- **AsyncDenied**: As in the previous example, this test is also divided into three steps. First, we need the *received* status in response to the *Send Antifraud Data* request for `{{ServiceURL}}/transactions`. We then send a *Get Antifraud Status* request (with the Transaction ID generated in the previous step) to `{{ServiceURL}}/transactions/transactionId`, waiting for the status *undefined* as response. Finally, after 10 seconds, we send another *Get Antifraud Status* request (with the same Transaction ID generated in the first step) to `{{ServiceURL}}/transactions/transactionId`, but this time waiting for the *denied* status in response.

- **HookApproved**: This test is divided into four steps. First, we need the *received* status in response to the *Send Antifraud Data* request for `{{ServiceURL}}/transactions`. Then we send a *Get Antifraud Status* request (with the Transaction ID generated in the previous step) to `{{ServiceURL}}/transactions/transactionId`, waiting for the status *undefined* as response. Then we wait for 10 seconds for the antifraud provider to POST the URL sent in the *hook* field of the first step (the POST content should contain the response obtained in that same step). Finally, we send another *Get Antifraud Status* request (with the same Transaction ID generated in the first step) to `{{ServiceURL}}/transactions/transactionId`, waiting for the *approved* status in response.

- **HookDenied**: Like the previous one, this test is also divided into four steps. First, we need the *received* status in response to the *Send Antifraud Data* request for `{{ServiceURL}}/transactions`. Then we send a *Get Antifraud Status* request (with the Transaction ID generated in the previous step) to `{{ServiceURL}}/transactions/transactionId`, waiting for the status *undefined* as response. Then we wait for 10 seconds for the antifraud provider to POST the URL sent in the *hook* field of the first step (the POST content should contain the response obtained in that same step). Finally, we send a further *Get Antifraud Status* request (with the same Transaction ID generated in the first step) to `{{ServiceURL}}/transactions/transactionId`, waiting for the *denied* status as response.

For each Antifraud Provider Protocol test, we send a specific ID end to return the expected response. They are:

- **Authorize**: ID with end 1.
- **Denied**: ID with end 2.
- **AsyncApproved**: ID with end 3.
- **AsyncDenied**: ID with end 4.
- **HookApproved**: ID with end 5.
- **HookDenied**: ID with end 6.

### 6. Results

After running the tests, the system returns the results, both positive and negative. The system also provides information on the expected results for each test. Thus, you have more visibility of what should be corrected in case of error.
 
![Antifraud test suite3](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/how-the-integration-protocol-between-vtex-and-antifraud-companies-works-4.png)
 
To visualize in detail each action performed by the integration (and thus to identify possible errors), just click on the **Show logs** link. A list of the complete information about the events that happened during the test will be displayed below the results.
 
![Antifraud test suite4](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/how-the-integration-protocol-between-vtex-and-antifraud-companies-works-5.png)
 
When your integration has successfully passed all tests, please open a ticket in our [VTEX support](https://help.vtex.com/pt/support "VTEX Help"). However, before opening the ticket, make sure you have the following information:

- **Connector Name**: a description of the provider. Use max. 16 alphanumeric characters. This name can not be modified after being published.
- **Partner contact**: partner email address in case we need to communicate changes and new features of our protocol.
- **Production Service Provider Endpoint**: the base path that will be used for API calls to the provider, e.g., `https://vtex.pagadito.com`. It has to respond to at least one of the following routes: `{{serviceUrl}}/manifest` or `{{serviceUrl}}/payment-methods`. This endpoint must be publicly available.
- **Sandbox Service Provider Endpoint**: the base path that will be used in test mode for API calls to the provider. E.g., `https://sandboxserviceproviderendpoint.com`.
- **Owner account**: the VTEX account name which will be used in callback requests. This account must be available at *{account}.myvtex.com*.
- **Allowed Accounts**: describe which VTEX accounts from this provider will be available (all accounts or specific accounts).
- **New Payment methods**: inform if this connector supports a payment method that is not yet available in the VTEX Admin.
- **New Payment method purchase flow**: if a “New Payment method” is supported,  inform whether it works with Redirect or Payment App. For more information, access [Purchase Flows](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-purchase-flows).

The SLA required for the payment team to carry out homologation is 30 days.

## VTEX Credentials

When calling `CallbackURL`, you must specify the authentication headers, which in VTEX are *X-VTEX-API-AppKey* and *X-VTEX-API-AppToken*. You can find these credentials in VTEX License Manager. These credentials are used by the Antifraud Provider only.

Use the `https://{{AccountName}}.myvtex.com/admin/license-manager/#/home` URL, replacing `{{AccountName}}` with your account name. Then follow the instructions of [this tutorial](https://help.vtex.com/en/tutorial/application-keys--2iffYzlvvz4BDMr6WGUtet) to learn how to create appKeys and appTokens on our platform.

## Settings in VTEX stores

Once the integration with your antifraud is approved, a connector will be made available for VTEX merchants to configure it on their respective websites. To do this, in addition to the contract with your company, the store will need two keys in hand: "X-PROVIDER-API-AppKey" and "X-PROVIDER-API-AppToken".

An example of how the antifraud settings screen will look for the VTEX store:
 
![gateway affiliations screen](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/how-the-integration-protocol-between-vtex-and-antifraud-companies-works-6.png)
 
These keys should be made available by you and will serve to identify the store that hired and is using your antifraud service.

## Cardholder Document Configuration

During payment transactions analysis, some anti-fraud providers may choose not to use additional information such as the cardholder’s personal identification. In these cases, the merchant has the autonomy to decide whether or not to request this document from his customer during the checkout procedure.
[block:callout]
{
  "type": "warning",
  "body": "The configuration option <strong>Cardholder document field</strong> will only be available to the merchant if the antifraud provider declares in its <a href=\"https://developers.vtex.com/vtex-rest-api/reference/manifest\">manifest</a>, the cardholder document field (<code>cardholderDocument</code>) as <code>optional</code>. Learn more at <a href=\"https://developers.vtex.com/vtex-rest-api/docs/cardholder-document-configuration\">Cardholder Document Configuration</a>."
}
[/block]
To set up the cardholder document field, follow the steps below:

1. Acess **Admin** VTEX.

2. Click on **Payments**.

3. Then, click on **Settings**.

4. On the **Gateway Affiliations** tab, click the **`+`** botton.

5. Select the antifraud provider you wish to use.

6. On the antifraud configuration screen, fill in the requested information.

7. In **Cardholder document field,**, select one of the following options:

   - **Display as a required field**: the field will be displayed at checkout with the information “required”, and the customer must fill in the cardholder information to complete the order.
   - **Display as an optional field**: the field will be displayed at checkout with the information “optional”, and the customer will decide whether or not to fill in it. The order can be completed even if the field is not filled in.
   - **Hide Field**: the field will not be displayed at checkout.

8. Click on **Save**.

After following the steps indicated, the settings made above may take up to 10 minutes to appear at your store’s checkout.
