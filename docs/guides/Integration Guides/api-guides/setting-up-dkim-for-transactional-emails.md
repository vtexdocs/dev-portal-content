---
title: "Setting up DKIM for transactional emails"
slug: "setting-up-dkim-for-transactional-emails"
hidden: false
createdAt: "2020-12-15T21:20:35.309Z"
updatedAt: "2020-12-28T20:55:49.552Z"
---
To enhance security for outgoing email and improve deliverability, the [DKIM](http://www.dkim.org/) standard adds an encrypted signature to the header of all outgoing messages. Email servers that get signed messages use DKIM to decrypt the message header, and verify the message was not changed after it was sent.

This article explains how to use the Message Center API to generate DKIM keys that can be stored in your DNS provider, so that all transactional emails sent by VTEX can be recognized as legitimate.

> 📘
>
> These instructions only apply if the [sender](https://help.vtex.com/en/tracks/transactional-emails--6IkJwttMw5T84mlY9RifRP/42LVaxtFb2VHX9xTZU58qC) is set up using VTEX mail servers. If you are using your own SMTP provider, you need to configure DKIM in your mail server.

## DKIM endpoint

<span class="pg-type type-post">post</span> `https://{accountName}.{environment}.com/api/mail-service/pvt/providers/:EmailProvider/dkim`

- `{accountName}` should be replaced with your store's account name (e.g. _cosmetics2_)
- `{environment}` should be replaced with the environment you are using (e.g. _vtexcommercestable_)
- `:EmailProvider` should be replaced with the configured e-mail address (e.g. _help@valdie.co_)

Check out the [Message Center API](https://developers.vtex.com/vtex-developer-docs/reference/dkim-configuration#createdkim) reference for more details.

## Generate DKIM key for your domain

Before you have setup a sender in [Message Center](https://help.vtex.com/en/tracks/transactional-emails--6IkJwttMw5T84mlY9RifRP) using VTEX mail servers, this is the expected response from the DKIM endpoint:

```json
{
    "status": "emailNotFound",
    "dkimKeys": null
}
```

Once the sender has been set up, you should receive an e-mail from Amazon Web Services requesting you to authorize the configured e-mail address for use with [Amazon SES](https://aws.amazon.com/ses/).

![](https://files.readme.io/9070bed-image1.png)

Clicking on the confirmation link provided in the e-mail body verifies you are the owner of the configured e-mail address. This is required for the mail server to send mail on your behalf. Until this is done, this is the expected response from the DKIM endpoint:

```json
{
    "status": "emailNotVerified",
    "dkimKeys": null
}
```

Once you have clicked on the confirmation link, you may test your SMTP configuration by clicking on the ✅**Test** button, as shown in the image below.

![](https://files.readme.io/33c85ef-image3.png)
After clicking on ✅**Test** button, you should receive an e-mail from the VTEX mail server using the sender you selected. The e-mail message sent follows the [Message Center template](https://help.vtex.com/en/tracks/transactional-emails--6IkJwttMw5T84mlY9RifRP/335JZKUYgvYlGOJgvJYxRO) `messageservice_teste_email`, which can be customized as seen in the image below.

![](https://files.readme.io/705e4dc-image2.png)

> 🚧
>
> If you don't receive any messages, review your sender configuration and try again.

Once you have correctly set up a sender in Message Center using VTEX mail servers, you should get a response similar to the one below from the DKIM endpoint:

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

## Add the public key to your DNS records

Now that you have generated a DKIM key for your domain, you need to add the values listed in dkimKeys in your DNS records. You should check the documentation for your [domain name registrar](https://support.google.com/a/answer/48323) for specific instructions on how to do that, but this is the general flow:

1. Sign in to the management console for your domain host
2. Locate the page where you update DNS records.
3. Add a TXT record corresponding to your DKIM keys
4. Save your changes

In up to 72 hours, all settings will propagate automatically and our servers will start adding a DKIM signature to all outgoing messages.
