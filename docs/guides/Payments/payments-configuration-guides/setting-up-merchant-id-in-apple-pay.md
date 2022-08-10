---
title: "Setting up Merchant ID in Apple Pay"
slug: "setting-up-merchant-id-in-apple-pay"
hidden: false
createdAt: "2022-01-27T15:02:19.691Z"
updatedAt: "2022-01-27T19:29:46.835Z"
---
In order for your store to begin receiving payments with **Apple Pay**, you will need to set **Merchant ID** in your [Apple developer account](developer.apple.com).

##Creating the Merchand ID

First of all, you need to create the Merchant ID itself - your store's ID on Apple's system.

This account acts as your login to the Apple Pay setup with VTEX. More specifically, this Merchant ID will be entered in the gateway affiliation which will, in turn, process payments.

It's therefore important to choose an ID that's easy to remember. We recommend something similar to `merchant.yourStoreName.vtexpayments.com.br.apple`.

In addition, your Merchant ID will not be the same as that of other stores. Apple's system ensures that each ID is unique.

Let's now turn our attention to the step-by-step process below:

1. Access your Apple **developer account** at `https://developer.apple.com/account/#/overview/`.
2. Select the **Certificates, IDs & Profiles** option.
<br>
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3cfad12-AP1.png",
        "AP1.png",
        208,
        335,
        "#f3f3f3"
      ]
    }
  ]
}
[/block]
<br>

3. Select **Identifiers**.

<br>
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/fd0ce1d-AP2.png",
        "AP2.png",
        194,
        237,
        "#f9f9f9"
      ]
    }
  ]
}
[/block]
<br>

4. Next to Identifiers, click on the blue **+** button.

<br>
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2eb156b-AP3.png",
        "AP3.png",
        418,
        91,
        "#f8f8f9"
      ]
    }
  ]
}
[/block]
<br>

5. Select the **Merchant IDs** option.
6. Click on the blue **Continue** button.

<br>
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d5d7950-AP4.png",
        "AP4.png",
        579,
        397,
        "#f8f8f8"
      ]
    }
  ]
}
[/block]
<br>

7. Fill on the **Description** field.
8. Fill in the **Identifier** field.
9. Click on **Continue**.

<br>
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/fc1ba70-AP5.png",
        "AP5.png",
        619,
        126,
        "#fafafb"
      ]
    }
  ]
}
[/block]
<br>

You will have created your **Merchant ID**.

##Creating the certificate to process payments

Now you've created your Merchant ID, you'll need a certificate to activate it.

This certificate is created by VTEX. Therefore, the retailer needs to [open a ticket](https://help.vtex.com/en/tutorial/open-tickets-to-vtex-support--16yOEqpO32UQYygSmMSSAM) with support for the team responsible for integrations to send you the file.

Thereafter, the retailer can submit the file to Apple Pay's system.

Follow the instructions below to proceed to this step:

1. On the left-hand side, open **Certificates** from the menu.

<br>
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ec990fd-AP6.png",
        "AP6.png",
        611,
        49,
        "#faf9f9"
      ]
    }
  ]
}
[/block]
<br>

2. Type in your newly created **Merchant ID** in the search bar.
3. Select the desired **Merchant ID**.

<br>
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/245d0ac-AP7.png",
        "AP7.png",
        611,
        356,
        "#f7f7f8"
      ]
    }
  ]
}
[/block]
<br>

4. Under **Apple Pay Payment Processing Certificate**, click the **Create Certificate** button.

<br>
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/331b7cc-AP8.png",
        "AP8.png",
        448,
        80,
        "#f5f7f8"
      ]
    }
  ]
}
[/block]
<br>

5. Ensure that the question *"Will payments associated with this Merchant ID be processed exclusively in China?"* is ticked with the **default option (No)**.

<br>
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d698a21-AP9.png",
        "AP9.png",
        623,
        143,
        "#fafafa"
      ]
    }
  ]
}
[/block]
<br>

You'll then be redirected to a screen with instructions on creating the Certificate Signing Request (CSR).

This is the time to open a ticket with the certificate request. The VTEX team will send you a file entitled `{{merchantID}}.csr` and with it saved on your computer, you must click on **Continue**.

After this step, you will be redirected once again, this time to the upload screen.

With the `{{merchantID}}.csr` that you've received, complete the following:

1. Click on **Choose File**.
2. Select the desired **CSR file**.
3. Click on **Continue**.

<br>
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/caafbd7-AP10.png",
        "AP10.png",
        597,
        156,
        "#fafafa"
      ]
    }
  ]
}
[/block]
<br>

4. Click on **Download**.

<br>
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/837b621-AP11.png",
        "AP11.png",
        626,
        165,
        "#f7f7f8"
      ]
    }
  ]
}
[/block]
<br>

5. Click on **Done**.

##Adding domains to Merchant ID

The next step is to link the domains used by your store to the Merchant ID that you've just created.

Firstly, you need to validate each of the desired URLs. Once this step is correctly completed, Apple's own system will create a `.txt` file and point to which domain this document should be linked to.

Lastly, you need to import this file to VTEX's system through Postman - an [API](https://help.vtex.com/en/tutorial/introduction-to-vtex-apis--3SjAqQ0BeUqu2ge8AiIkmW) management tool.

[block:callout]
{
  "type": "warning",
  "body": "This validation can only be done one domain at a time. This means that if your store uses 10 different domains, the process will have to be repeated 10 times."
}
[/block]
Follow these steps:

1. Search for the recently created **MerchantID** in the search bar.

<br>
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d16da6a-AP12.png",
        "AP12.png",
        615,
        55,
        "#fbfafa"
      ]
    }
  ]
}
[/block]
<br>

2. Click on the desired **MerchantID**. 
3. In the **Merchant Domain** module, click on **Add Domain**.

<br>
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2d7e546-AP13.png",
        "AP13.png",
        602,
        238,
        "#f4f4f4"
      ]
    }
  ]
}
[/block]
<br>

4.  Add the domain in the **Enter the domain you wish to register** field.
5.  Click on **Save**.

Thereafter, to upload the`.txt` file by API, follow these instructions:

1.  Click on **Download** and make no changes to the file.

<br>
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/aafb5cc-AP14.png",
        "AP14.png",
        599,
        267,
        "#f4f5f7"
      ]
    }
  ]
}
[/block]
<br>

2.  Open the `.txt` file and **copy** all the content.

Then, start a Postman session. You perform a call to VTEX's CDN using the POST method:

1.  Configure the route **POST** `https://{{yourdomain}}/.well-known/raw/{token}`.
2. Ensure that **all the contents** of the `.txt` file is in **quotation marks** and without any **line breaks**.
3. Add the **X-VTEX-API-AppKey** and the **X-VTEX-API-AppToken** to the header.

Now, when making the **POST** call, the response will inform you that your certificate will be saved for 60 minutes. During this time, you should complete the domain validation.

Head back to the Apple's website. On the same screen where you downloaded the `.txt` file, click on **Verify**.

<br>
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8d2c64f-AP15.png",
        "AP15.png",
        596,
        354,
        "#f6f7f8"
      ]
    }
  ]
}
[/block]
<br>

If you've followed the step-by-step correctly, your domain will be registered with the **verified** status. If you want, you can repeat the process to add more domains by using the **Add Domain** button in the **Merchant Domains** section.

##Creating a Merchant Identity Certificate

Lastly, you must generate a Merchant ID certificate, which will be used every time Apple shows the Apple Pay screen to your customers. To complete the steps of this process, it's important that to have a Mac computer available.

To complete the action, you'll need to create a password to protect the exported data.

<br>
[block:callout]
{
  "type": "info",
  "body": "We recommend an easy to remember password, since it will be filled into the Apple Merchant Password field upon configuring the gateway affiliation on VTEX's platform."
}
[/block]
1.  Access the **Certificate**, **Identifiers & Profilers** module.
2.  From the left side menu, choose **Identifiers**.
3.  In the upper right corner, filter by **Merchant IDs**.

<br>
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4e48e0c-AP16.png",
        "AP16.png",
        617,
        56,
        "#fbfafa"
      ]
    }
  ]
}
[/block]
<br>

4. Select the desired **Merchant Identifier**.
5. Click on **Create Certificate**.

<br>
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4cf8941-AP17.png",
        "AP17.png",
        397,
        107,
        "#ededed"
      ]
    }
  ]
}
[/block]
<br>

6. Follow the **instructions** displayed on the screen to create a certificate.
7. Click on **Continue**.

<br>
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/109d91f-AP18.png",
        "AP18.png",
        605,
        682,
        "#f7f7f8"
      ]
    }
  ]
}
[/block]
<br>

8. Click on **Download**.

<br>
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e05a913-AP19.png",
        "AP19.png",
        588,
        377,
        "#f4f6f7"
      ]
    }
  ]
}
[/block]
After the file has been downloaded, double-click it to install it in Keychain Access.

Afterwards, proceed to the following steps:

1. Open **Keychain Access**.
2. Locate the **certificate** created in step 4 above.
3. Right click on the **key** icon.

<br>
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4a93846-AP20.png",
        "AP20.png",
        582,
        109,
        "#c9d8ea"
      ]
    }
  ]
}
[/block]
<br>

4. Click on **Export**.
5. Give the **certificate** a name.
6. Select the **.p12** export format.
7. Click on **OK**.

As a final step, save the certificate on your computer. This file should be loaded in the gateway affiliation setting's **Apple Merchant Certificate (.p12)** field, affiliation that will process Apple Pay in your VTEX store.

After completing all the steps above, you will have a Merchant ID set up for Apple Pay, a `.p12` certificate saved on your computer, and an access password. All this data will be requested during the process of setting up the gateway affiliation that will process payments with Apple Pay.

To learn how to do this, access this [Help article](https://help.vtex.com/en/tutorial/setting-up-rede-acquirer-with-erederest).