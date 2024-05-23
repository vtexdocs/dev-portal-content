---
title: "Setting up DKIM for transactional emails"
slug: "setting-up-dkim-for-transactional-emails"
hidden: false
createdAt: "2020-12-15T21:20:35.309Z"
updatedAt: "2020-12-28T20:55:49.552Z"
---

To enhance security for outgoing email and improve deliverability, the [DKIM](http://www.dkim.org/) standard adds an encrypted signature to the header of all outgoing messages. Email servers that receive signed messages use DKIM to decrypt the message header and verify the message was not changed after it was sent.

This guide explains how to use the [Message Center API](https://developers.vtex.com/docs/api-reference/message-center-api?endpoint=post-/api/mail-service/pvt/providers/-EmailProvider-/dkim) to generate DKIM keys that can be stored in your DNS provider so that all transactional emails sent by VTEX can be recognized as legitimate.

> ℹ️ These instructions only apply if the [sender](https://help.vtex.com/en/tracks/transactional-emails--6IkJwttMw5T84mlY9RifRP/42LVaxtFb2VHX9xTZU58qC) is set up using VTEX mail servers. If you use your own SMTP provider, you need to enable DKIM in your mail server.

## DKIM endpoint

It is necessary to use the `POST` [Generate DKIM keys](https://developers.vtex.com/docs/api-reference/message-center-api?endpoint=post-/api/mail-service/pvt/providers/-EmailProvider-/dkim) endpoint from Message Center API, as follows:

`POST https://{accountName}.{environment}.com/api/mail-service/pvt/providers/{EmailProvider}/dkim`

- `{accountName}` should be replaced with your store account name (e.g. `apiexamples`).
- `{environment}` should be replaced with the environment you are using (e.g. `vtexcommercestable`).
- `{EmailProvider}` should be replaced with the configured email address (e.g. `help@valdie.co`).

See the [Message Center API](https://developers.vtex.com/docs/api-reference/message-center-api?endpoint=post-/api/mail-service/pvt/providers/-EmailProvider-/dkim) reference for more details.

## Generating a DKIM key for your domain

Follow the steps below to create a DKIM key for your domain:

1. Make a request to the `POST` [Generate DKIM keys](https://developers.vtex.com/docs/api-reference/message-center-api?endpoint=post-/api/mail-service/pvt/providers/-EmailProvider-/dkim) endpoint.

   Before you have [set up a sender in Message Center](https://help.vtex.com/en/tracks/transactional-emails--6IkJwttMw5T84mlY9RifRP) using VTEX mail servers, this is the expected response from the DKIM endpoint:
    
    ```json
    {
        "status": "emailNotFound",
        "dkimKeys": null
    }
    ```
    
2. Follow [this guide](https://help.vtex.com/en/tracks/transactional-emails--6IkJwttMw5T84mlY9RifRP#senders) to set up a sender on Message Center.

    Once the sender has been set up, you should receive an email from Amazon Web Services requesting you to authorize the configured email address to use [Amazon SES](https://aws.amazon.com/ses/), as illustrated below:
    
    ![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-dkim-for-transactional-emails-0.png)

3. Click the confirmation link provided in the email body to verify you are the owner of the configured email address. This is required for the mail server to send mail on your behalf.

   Until this is done, this is the expected response from the DKIM endpoint:
    
    ```json
    {
        "status": "emailNotVerified",
        "dkimKeys": null
    }
    ```

5. Once you have clicked the confirmation link, test your SMTP configuration on VTEX Admin at **Email Templates > Senders** by clicking the ✅**Test** button, as shown in the image below:

    ![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-dkim-for-transactional-emails-1.png)

    You should receive an email from the VTEX mail server using the sender you selected. The email message sent follows the Message Center template `messageservice_teste_email`, which you can customize as in the image below by following the [How to create and edit transactional email templates](https://help.vtex.com/en/tracks/transactional-emails--6IkJwttMw5T84mlY9RifRP/335JZKUYgvYlGOJgvJYxRO) guide.

    ![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-dkim-for-transactional-emails-2.png)

    > ⚠️ If you do not receive any messages, review your sender configuration and try again.
    
6. Once you have correctly set up a sender in Message Center using VTEX mail servers, make a request to `POST` [Generate DKIM keys](https://developers.vtex.com/docs/api-reference/message-center-api?endpoint=post-/api/mail-service/pvt/providers/-EmailProvider-/dkim) endpoint again.
  
   The response should be similar to the one below:
    
    ```json
    {
        "status": "created",
        "dkimKeys": [
            "'n4zbltwizctxpgcmqrars4bmfdd3zlyo._domainkey.valdie.co','CNAME','n4zbltwizctxpgcmqrars4bmfdd3zlyo.dkim.amazonses.com'",
            "'sq3iae4be52fhqq3wm44btttvndeecfv._domainkey.valdie.co','CNAME','sq3iae4be52fhqq3wm44btttvndeecfv.dkim.amazonses.com'",
            "'n4z5g2g7yfy4pnhjklfesxrrkt4o2ha4._domainkey.valdie.co','CNAME','n4z5g2g7yfy4pnhjklfesxrrkt4o2ha4.dkim.amazonses.com'"
        ]
    }
    ```

## Adding the public key to your DNS records

Now that you have generated a DKIM key for your domain, you need to add the values listed in dkimKeys in your DNS records. Read the documentation for your [domain name](https://support.google.com/a/answer/48323) for specific instructions on how to do that, but this is the general flow:

1. Sign in to the management console for your domain host.
2. Locate the page where you update DNS records.
3. Add a CNAME record for each corresponding DKIM key.
4. Save changes.

In up to 72 hours, all settings will be applied automatically, and our servers will start adding a DKIM signature to all outgoing messages.
