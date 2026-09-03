---
title: "Setting up Merchant ID in Apple Pay"
slug: "setting-up-merchant-id-in-apple-pay"
excerpt: "Learn how to create a Merchant ID in your Apple Developer account, generate the Apple Pay certificates, and validate your store domains to process Apple Pay payments on VTEX."
hidden: false
createdAt: "2022-01-27T15:02:19.691Z"
updatedAt: "2026-09-03T00:00:00.000Z"
---

To receive payments with Apple Pay, your store needs a Merchant ID, which is the identifier of your store in the Apple system. You create the Merchant ID in your Apple Developer account and then enter it in the gateway affiliation that processes Apple Pay payments.

Setting up the Merchant ID has four stages, described in the following sections:

1. [Create the Merchant ID](#creating-the-merchant-id).
2. [Create the payment processing certificate](#creating-the-payment-processing-certificate).
3. [Validate the domains of your store](#validating-the-domains-of-your-store).
4. [Create the merchant identity certificate](#creating-the-merchant-identity-certificate).

## Before you begin

Check the following requirements:

- An [Apple Developer account](https://developer.apple.com/).
- A computer running macOS, required to create the merchant identity certificate, because you use Keychain Access to generate its certificate signing request and to export the certificate.
- An [API key](https://developers.vtex.com/docs/guides/api-authentication-using-api-keys) of your VTEX account, used to upload the domain validation file.
- A payment provider that processes Apple Pay, as described in [Setting up payments with Apple Pay](https://help.vtex.com/en/docs/tutorials/setting-up-payments-with-apple-pay).

> ⚠️ VTEX generates the certificate signing request (CSR) used to create the payment processing certificate. [Open a ticket to VTEX support](https://supporticket.vtex.com/support) to request this file before you begin, because Apple asks for it in the middle of the certificate creation flow.

## Creating the Merchant ID

The Merchant ID identifies your store in the Apple system. Apple ensures that each Merchant ID is unique, and a Merchant ID never expires. Choose an identifier that is easy to remember, such as `merchant.yourStoreName.vtexpayments.com.br.apple`.

To create the Merchant ID, follow these instructions:

1. Access your [Apple Developer account](https://developer.apple.com/account).
2. Go to **Certificates, IDs & Profiles > Identifiers**.

    ![Program Resources menu of the Apple Developer account, with the Certificates, IDs & Profiles option highlighted.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-0.png)

    ![Sidebar of the Certificates, Identifiers & Profiles section, with the Identifiers option highlighted.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-1.png)

3. Click the add (`+`) button next to **Identifiers**.

    ![Identifiers page with the blue add button next to the page title highlighted.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-2.png)

4. Select **Merchant IDs**.
5. Click `Continue`.

    ![Register a new identifier page, with the Merchant IDs option selected and the Continue button highlighted.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-3.png)

6. Fill in the **Description** and **Identifier** fields.
7. Click `Continue`.

    ![Register Merchant ID page, displaying the Description and Identifier fields.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-4.png)

8. Review the settings.
9. Click `Register`.

## Creating the payment processing certificate

The payment processing certificate is associated with your Merchant ID and encrypts the payment data of the transactions. VTEX creates the CSR of this certificate, so keep the file sent by VTEX support available before you begin.

> ⚠️ The payment processing certificate expires periodically, currently every 25 months, according to the [Apple documentation](https://developer.apple.com/help/account/capabilities/configure-apple-pay). Create a new certificate before the expiration date to avoid interrupting Apple Pay transactions in your store.

To create the certificate, follow these instructions:

1. Go to **Certificates, IDs & Profiles > Identifiers**.
2. In the filter at the top right of the page, select **Merchant IDs**.

    ![Identifiers page with the Merchant IDs filter highlighted at the top right.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-5.png)

3. Select the Merchant ID you created.

    ![List of merchant identifiers, with one Merchant ID selected.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-6.png)

4. Under **Apple Pay Payment Processing Certificate**, click `Create Certificate`.

    ![Merchant ID configuration page, with the Create Certificate button of the Apple Pay Payment Processing Certificate section highlighted.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-7.png)

5. Keep the default option `No` for the question about processing payments exclusively in mainland China.

    ![Question about processing payments exclusively in China, with the default option No selected.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-8.png)

6. On the screen with the instructions to create the CSR, click `Continue`.
7. Click `Choose File`.
8. Select the `{merchantID}.csr` file sent by VTEX support.
9. Click `Continue`.

    ![Upload screen of the certificate signing request, with the Choose File button highlighted.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-9.png)

10. Click `Download`.

    ![Certificate download screen, with the Download button highlighted.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-10.png)

11. Click `Done`.

> ℹ️ Use the CSR sent by VTEX support instead of generating your own. The payment processing certificate requires a CSR created with the key pair that VTEX controls.

## Validating the domains of your store

Apple requires you to register and validate every top-level domain and subdomain that displays the Apple Pay button. In this stage, Apple generates a validation file, and you publish it in your store domain through the VTEX API.

> ⚠️ Plan to complete this stage without interruptions, because VTEX stores the domain validation file for only 60 minutes after the upload.

> ℹ️ Validate one domain at a time. If your store uses 10 domains, repeat this procedure 10 times. According to the [Apple Pay Merchant Integration Guide](https://developer.apple.com/apple-pay/Apple-Pay-Merchant-Integration-Guide.pdf), domains can't be behind a proxy or a redirect, and they must be reachable by the Apple servers.

To validate a domain, follow these instructions:

1. Go to **Certificates, IDs & Profiles > Identifiers**.
2. In the filter at the top right of the page, select **Merchant IDs**.

    ![Identifiers page with the Merchant IDs filter and the search field highlighted.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-11.png)

3. Select the Merchant ID you created.
4. Under **Merchant Domains**, click `Add Domain`.

    ![Merchant ID configuration page, with the Add Domain button of the Merchant Domains section highlighted.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-12.png)

5. Fill in the **Enter the domain you wish to register** field with the fully qualified domain name.
6. Click `Save`.
7. Click `Download` to get the `.txt` validation file.

    ![Domain registration screen, with the Download button of the validation file highlighted.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-13.png)

8. Open the `.txt` validation file.
9. Copy the entire content of the file, respecting the following format:

    - Inside quotation marks
    - In JSON format, as in `"{tokenContent}"`
    - Without line breaks

10. Publish the content in your store domain with the following request, using an API client such as cURL or Postman:

    ```sh
    curl --request POST \
      --url https://{storeDomain}/.well-known/raw/apple-developer-merchantid-domain-association.txt \
      --header 'Content-Type: application/json' \
      --header 'X-VTEX-API-AppKey: {appKey}' \
      --header 'X-VTEX-API-AppToken: {appToken}' \
      --data '"{tokenContent}"'
    ```

    Replace `storeDomain` with the domain you are validating, `appKey` and `appToken` with your API key credentials, and `tokenContent` with the content of the validation file.

    ![API client displaying the POST request to the store domain, with the content of the validation file in the request body.](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Payments/payments-configuration-guides/setting-up-merchant-id-in-apple-pay-20.png)

    The response confirms that VTEX stores the file for 60 minutes. Complete the following steps within this period, or send the request again.

11. In the Apple Developer account, return to the screen where you downloaded the validation file.
12. Click `Verify`.

    ![Domain registration screen, with the Verify button highlighted.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-14.png)

> ⚠️ Don't change the content of the validation file.

When the validation succeeds, the domain appears with the **Verified** status. To add more domains, repeat this procedure using the `Add Domain` button in the **Merchant Domains** section.

## Creating the merchant identity certificate

The merchant identity certificate authenticates the sessions between your store and the Apple Pay servers, and Apple uses it every time the Apple Pay screen is displayed to a customer.

> ⚠️ This stage requires a computer running macOS, because you use Keychain Access to generate the certificate signing request and to export the certificate. During the export, you define a password that protects the exported data. Keep this password, because you enter it in the **Apple Merchant Password** field when you configure the gateway affiliation on VTEX.

To create the certificate, follow these instructions:

1. Go to **Certificates, IDs & Profiles > Identifiers**.
2. In the filter at the top right of the page, select **Merchant IDs**.

    ![Identifiers page with the Merchant IDs filter highlighted at the top right.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-15.png)

3. Select the Merchant ID you created.
4. Under **Apple Pay Merchant Identity Certificate**, click `Create Certificate`.

    ![Merchant ID configuration page, with the Create Certificate button of the Apple Pay Merchant Identity Certificate section highlighted.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-16.png)

5. Follow the instructions displayed on the screen to create the CSR.
6. Click `Continue`.

    ![Screen with the instructions to create a certificate signing request.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-17.png)

7. Click `Download`.

    ![Certificate download screen, with the Download button highlighted.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-18.png)

8. Double-click the downloaded file to install it in Keychain Access.
9. Open **Keychain Access**.
10. Locate the certificate you installed.
11. Right-click the key icon of the certificate.

    ![Keychain Access window, with the key icon of the certificate highlighted.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-merchant-id-in-apple-pay-19.png)

12. Select `Export`.
13. Name the certificate.
14. Select the `.p12` export format.
15. Click `OK`.
16. Define the password that protects the exported data.
17. Save the certificate on your computer.

> ⚠️ The merchant identity certificate requires a CSR generated with an RSA 2048-bit key pair, as described in the [Apple Pay Merchant Integration Guide](https://developer.apple.com/apple-pay/Apple-Pay-Merchant-Integration-Guide.pdf). This CSR is different from the one VTEX sends for the payment processing certificate.

## Next steps

After completing the previous stages, you have a Merchant ID, validated domains, a `.p12` certificate saved on your computer, and the export password. Use this data to configure the payment provider that processes Apple Pay payments in your store, as described in [Registering gateway affiliations](https://help.vtex.com/en/docs/tutorials/registering-gateway-affiliations) and [Setting up payments with Apple Pay](https://help.vtex.com/en/docs/tutorials/setting-up-payments-with-apple-pay).

## Learn more

- [Setting up payments with Apple Pay](https://help.vtex.com/en/docs/tutorials/setting-up-payments-with-apple-pay)
- [Registering gateway affiliations](https://help.vtex.com/en/docs/tutorials/registering-gateway-affiliations)
- [Apple Pay Merchant Integration Guide](https://developer.apple.com/apple-pay/Apple-Pay-Merchant-Integration-Guide.pdf)
