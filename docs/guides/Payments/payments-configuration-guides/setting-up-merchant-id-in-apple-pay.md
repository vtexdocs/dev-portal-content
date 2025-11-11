---
title: "Setting up Merchant ID in Apple Pay"
slug: "setting-up-merchant-id-in-apple-pay"
hidden: false
createdAt: "2022-01-27T15:02:19.691Z"
updatedAt: "2022-01-27T19:29:46.835Z"
---

In order for your store to begin receiving payments with **Apple Pay**, you will need to set **Merchant ID** in your [Apple developer account](https://developer.apple.com/).

## Creating the Merchant ID

First of all, you need to create the Merchant ID itself - your store's ID on Apple's system.

This account acts as your login to the Apple Pay setup with VTEX. More specifically, this Merchant ID will be entered in the gateway affiliation which will, in turn, process payments.

It's therefore important to choose an ID that's easy to remember. We recommend something similar to `merchant.yourStoreName.vtexpayments.com.br.apple`.

In addition, your Merchant ID will not be the same as that of other stores. Apple's system ensures that each ID is unique.

Let's now turn our attention to the step-by-step process below:

1. Access your Apple **developer account** at `https://developer.apple.com/account/#/overview/`.
2. Select the **Certificates, IDs & Profiles** option.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-0.png)

3. Select **Identifiers**.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-1.png)

4. Next to Identifiers, click on the blue **+** button.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-2.png)

5. Select the **Merchant IDs** option.
6. Click on the blue **Continue** button.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-3.png)

7. Fill on the **Description** field.
8. Fill in the **Identifier** field.
9. Click on **Continue**.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-4.png)

You will have created your **Merchant ID**.

## Creating the certificate to process payments

Now you've created your Merchant ID, you'll need a certificate to activate it.

This certificate is created by VTEX. Therefore, the retailer needs to [open a ticket](https://help.vtex.com/en/tutorial/open-tickets-to-vtex-support--16yOEqpO32UQYygSmMSSAM) with support for the team responsible for integrations to send you the file.

Thereafter, the retailer can submit the file to Apple Pay's system.

Follow the instructions below to proceed to this step:

1. On the left-hand side, open **Certificates** from the menu.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-5.png)

2. Type in your newly created **Merchant ID** in the search bar.
3. Select the desired **Merchant ID**.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-6.png)

4. Under **Apple Pay Payment Processing Certificate**, click the **Create Certificate** button.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-7.png)

5. Ensure that the question *"Will payments associated with this Merchant ID be processed exclusively in China?"* is ticked with the **default option (No)**.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-8.png)

You'll then be redirected to a screen with instructions on creating the Certificate Signing Request (CSR).

This is the time to open a ticket with the certificate request. The VTEX team will send you a file entitled `{{merchantID}}.csr` and with it saved on your computer, you must click on **Continue**.

After this step, you will be redirected once again, this time to the upload screen.

With the `{{merchantID}}.csr` that you've received, complete the following:

1. Click on **Choose File**.
2. Select the desired **CSR file**.
3. Click on **Continue**.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-9.png)

4. Click on **Download**.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-10.png)

5. Click on **Done**.

## Adding domains to Merchant ID

The next step is to link the domains used by your store to the Merchant ID that you've just created.

Firstly, you need to validate each of the desired URLs. Once this step is correctly completed, Apple's own system will create a `.txt` file and point to which domain this document should be linked to.

Lastly, you need to import this file to VTEX's system through Postman - an [API](https://developers.vtex.com/docs/guides/getting-started-list-of-rest-apis) management tool.

>⚠️ This validation can only be done one domain at a time. This means that if your store uses 10 different domains, the process will have to be repeated 10 times.

Follow these steps:

1. Search for the recently created **MerchantID** in the search bar.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-11.png)

2. Click on the desired **MerchantID**.
3. In the **Merchant Domain** module, click on **Add Domain**.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-12.png)

4. Add the domain in the **Enter the domain you wish to register** field.
5. Click on **Save**.

Thereafter, to upload the`.txt` file by API, follow these instructions:

1. Click on **Download** and make no changes to the file.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-13.png)

2. Open the `.txt` file and **copy** all the content.

Then, start a Postman session. You perform a call to VTEX's CDN using the POST method:

1. Configure the route **POST** `https://{{yourdomainhere}}/.well-known/raw/apple-developer-merchantid-domain-association.txt`.
2. Paste the content of the .txt file in the request body. Ensure that all contents of the file are:
   - Inside quotations marks.
   - In JSON format, as in `"{token_content}"`.
   - Without any line breaks.

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Payments/payments-configuration-guides/setting-up-merchant-id-in-apple-pay-20.png)

3. Add the **X-VTEX-API-AppKey** and the **X-VTEX-API-AppToken** to the header.

Now, when making the **POST** call, the response will inform you that your certificate will be saved for 60 minutes. During this time, you should complete the domain validation.

Head back to the Apple's website. On the same screen where you downloaded the `.txt` file, click on **Verify**.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-14.png)

If you've followed the step-by-step correctly, your domain will be registered with the **verified** status. If you want, you can repeat the process to add more domains by using the **Add Domain** button in the **Merchant Domains** section.

## Creating a Merchant Identity Certificate

Lastly, you must generate a Merchant ID certificate, which will be used every time Apple shows the Apple Pay screen to your customers. To complete the steps of this process, it's important that to have a Mac computer available.

To complete the action, you'll need to create a password to protect the exported data.

> ℹ️️ We recommend an easy to remember password, since it will be filled into the Apple Merchant Password field upon configuring the gateway affiliation on VTEX's platform.

1. Access the **Certificate**, **Identifiers & Profilers** module.
2. From the left side menu, choose **Identifiers**.
3. In the upper right corner, filter by **Merchant IDs**.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-15.png)

4. Select the desired **Merchant Identifier**.
5. Click on **Create Certificate**.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-16.png)

6. Follow the **instructions** displayed on the screen to create a certificate.
7. Click on **Continue**.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-17.png)

8. Click on **Download**.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-18.png)
After the file has been downloaded, double-click it to install it in Keychain Access.

Afterwards, proceed to the following steps:

1. Open **Keychain Access**.
2. Locate the **certificate** created in step 4 above.
3. Right click on the **key** icon.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-19.png)

4. Click on **Export**.
5. Give the **certificate** a name.
6. Select the **.p12** export format.
7. Click on **OK**.
8. Save the certificate on your computer.

After completing all the steps above, you will have a Merchant ID set up for Apple Pay, a `.p12` certificate saved on your computer, and an access password. All this data will be requested during the process of setting up the [payment provider](https://help.vtex.com/en/tutorial/registering-gateway-affiliations--tutorials_444) that will process payments with Apple Pay in your store.