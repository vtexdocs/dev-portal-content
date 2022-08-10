---
title: "Payment Provider Homologation"
slug: "payments-integration-payment-provider-homologation"
hidden: false
createdAt: "2020-10-27T15:19:20.313Z"
updatedAt: "2022-02-03T15:13:30.406Z"
---
The last step to complete the implementation process is to check if the integration was done correctly.

To do so, you can simulate the integration functioning with the Payment Provider Test Suite app.

## Install the Test Suite app

There are two ways to download it: accessing the [VTEX App Store] (https://apps.vtex.com/vtex-payment-provider-test-suite/p) or through the Admin.

Considering that you want to download the app through the Admin, proceed as follows:

1. Access the Admin.
2. Go to the **ACCOUNT SETTINGS** module.
3. Click on **Apps** then **App Store**.
4. Now look for **Payment Provider Test Suite** in the search bar.
5. Click **Install**.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c2c9925-Test_suite_1.png",
        "Test_suite_1.png",
        2770,
        1082,
        "#f8f8f9"
      ]
    }
  ]
}
[/block]
6. After that, you will be redirected to the VTEX App Store. Click the **GET APP** button at the top right corner of the page.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7e850d8-Test_suite_2.png",
        "Test_suite_2.png",
        2486,
        1526,
        "#f7f7f8"
      ]
    }
  ]
}
[/block]
7. Then, on the popup screen, type your account's name - with lowercase and no space in between - and click the **CONFIRM** button.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/571bd57-Test_suite_3.png",
        "Test_suite_3.png",
        1602,
        1172,
        "#cccdcf"
      ]
    }
  ]
}
[/block]
8. Click **INSTALL** to complete the installation process.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9191e2b-Test_suite_4.png",
        "Test_suite_4.png",
        2138,
        834,
        "#f2f4f6"
      ]
    }
  ]
}
[/block]
After that, the Test Suite app will be installed in your Admin. 

## Run the tests

After having proceeded with the Homologation process you can start running tests to validate the integration.

### Service information

To start, fulfill each field according to the instructions below:

  - Service URL: The provider’s endpoint. VTEX will use this URL to contact the provider system.
  - Connector Name: How your connector will be named in VTEX. The connector name has necessarily to be related to your brand. Also, the Connector Name is case-sensitive. That means that it considers uppercase and lowercase.
  - X-VTEX-API-AppKey: fulfill it with the value `X-VTEX-API-AppKey`.
  - X-VTEX-API-AppToken: fulfill it with the value `X-VTEX-API-AppToken`.

[block:callout]
{
  "type": "danger",
  "title": "Warning",
  "body": "Once you define the connector name, it can not be changed."
}
[/block]
Then, click the **Check URL** button. This action will call the [GET List Payment Methods](https://developers.vtex.com/vtex-developer-docs/reference/paymentmethods) endpoint. The response will indicate which payment methods will be able to be analyzed in the next step (Tests form).

### Tests

After the call, the payment methods implemented will be exposed in the form and the switches will be activated automatically. 

Check if the right options were activated. Then, click the **Run Tests** button.

### Logs

All of the operations realized in the test phase will be exposed in the Logs box, including the ones that may present some error in the integration. 

If errors happen, make all the adjustments necessary to adapt your connector to the Payment Provider Protocol rules and try to run the test again. 

If everything is ok, you need to [open a ticket to the VTEX support team](https://help.vtex.com/en/tutorial/opening-tickets-to-vtex-support--16yOEqpO32UQYygSmMSSAM?locale=en) informing them that the integration was completed. However, before opening the ticket, make sure you have the following information:

- **Connector Name**: a description of the provider. Use max. 16 alphanumeric characters. This name can not be modified after being published.
- **Partner contact**: partner email address in case we need to communicate changes and new features of our protocol.
- **Production Service Provider Endpoint**: the base path that will be used for API calls to the provider, e.g. *https://vtex.pagadito.com*. It has to respond to at least one of the following routes: `{{serviceUrl}}/manifest` or `{{serviceUrl}}/payment-methods`. This endpoint must be publicly available.
 - **Sandbox Service Provider Endpoint**: the base path that will be used in test mode for API calls to the provider. E.g. *https://sandboxserviceproviderendpoint.com*. 
- **Owner account**: the VTEX account name which will be used in callback requests. This account must be available at *[account].myvtex.com*. 
- **Allowed Accounts**: describe which VTEX accounts from this provider will be available (all accounts or specific accounts).
- **New Payment methods**: inform if this connector supports a payment method that is not yet available in the VTEX Admin.
- **New Payment method purchase flow**: if a "New Payment method" is supported, inform whether it works with Redirect or Payment App. For more information, access  [Purchase Flows] (https://developers.vtex.com/vtex-rest-api/docs/payments-integration-purchase-flows).

The SLA required for the payment team to carry out homologation is 30 days.
[block:callout]
{
  "type": "danger",
  "body": "Do **not** open the ticket for homologation if the Logs box presents any type of error. Redo the operation until the Logs box results are clear. If you need help in this scenario, talk to your Partner Account Manager.",
  "title": "Obey the process"
}
[/block]

[block:callout]
{
  "type": "danger",
  "body": "It is mandatory to open a ticket to VTEX Support. Without that, the implementation will not be recognized by our system.",
  "title": "Contact VTEX Support Team"
}
[/block]
After that, the VTEX support team will inform you if the implementation was done correctly.