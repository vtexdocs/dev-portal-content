---
title: "Sending emails with triggers in Master Data v2"
slug: "sending-emails-with-triggers-in-master-data-v2"
hidden: false
createdAt: "2022-08-03T14:48:49.642Z"
updatedAt: "2022-08-03T14:56:02.147Z"
---

There are two ways of sending emails automatically with Master Data v2 triggers:

- [Sending emails](#sending-emails)
- [Sending emails using Message Center templates](#sending-emails-using-message-center-templates)

>ℹ️ Learn more about triggers in the article [Setting up triggers in Master Data v2](https://developers.vtex.com/docs/guides/setting-up-triggers-in-master-data-v2).

## Sending emails

This is the more direct method of sending emails with Master Data v2 triggers, but without the standardization provided by [Message Center templates](#sending-emails-using-message-center-templates).

### Properties

| Field | Type | Description | Required |
| ---------- | ---------- | ---------- | ---------- |
| type | String | Action type, which must be `email`. | True |
| provider | String | Message Center provider name (usually named as `default`). | True |
| from | Object | Information about the sender. | True |
| ↪ email | String | Sender email. | True |
| ↪ name | String | Sender name. | True |
| to | Array of strings | List of recipient email addresses, separated by comma. | True |
| replyTo | Array | Email address for replies. | True |
| subject | String | Email subject. | True |
| body | String | Email message body. | True |
| bcc | Array of strings | List of email addresses that will receive a blind carbon copy (BCC) of the message. | False |

### Dynamic expressions

You can use dynamic expressions to deal with document properties in these settings. For more information, look at the [Article on dynamic expressions](https://developers.vtex.com/vtex-rest-api/docs/adding-document-field-values-with-dynamic-expressions).

### JSON schema example

```json
    {
      "properties": { ... },
      "v-triggers": [
        {
          "type": "email",
          "provider": "default",
          "subject": "Sending email with VTEX Master Data",
          "from": {
            "email": "mailfrom@email.com",
            "name": "My custom name"
          },
          "to": [ "test@test.com" ],
          "bcc": [ "testbcc@test.com" ],
          "replyTo": "noreply@email.com",
          "body": "VTEX Master Data Triggers email body"
        } 
      ]
    }
```

## Sending emails using Message Center templates

See below how to set up a trigger to send emails using a [Message Center](https://help.vtex.com/en/tutorial/understanding-the-message-center--tutorials_84) template.

### Properties

| Field | Type | Description | Required |
| ---------- | ---------- | ---------- | ---------- |
| type | String | Action type, which must be `t-email`. | True |
| template | String | Name of the Message Center template. | True |
| provider | String | Message Center provider name (usually named as `default`). | True |
| from | Object | Information about the sender. | True |
| ↪ email | String | Sender email. | True |
| ↪ name | String | Sender name. | True |
| to | Array of strings | List of recipient email addresses, separated by comma. | True |
| replyTo | String | Email address for replies. | True |
| subject | String | Email subjec.t | True |
| body | String | Email message body. | True |
| bcc | Array of strings | List of email addresses that will receive a blind carbon copy (BCC) of the message. | False |

### JSON schema example

```json
    {
      "properties": { ... },
      "v-triggers" [
            {
            "type": "t-email",
            "template": "template-name",
            "provider": "default",
            "subject": "My template email with VTEX Master Data",
            "to": [
                "{!email}",
                "test@email.com"
            ],
            "bcc": [
                "myemail@test.com"
            ],
            "replyTo": "noreply@company.com",
            "body": {
                        "firstName": "{firstName}",
                        "email": "{email}",
                        "id": "{!id}",
                        "clientName": "{!clientProfileData.firstName{!clientProfileData.lastName}",
                        "ownerListName": "{!customData.customApps[0fields.ownerListName}",
                        "ownerListEmail": "{!customData.customApps[0fields.ownerListEmail}",
                        "items": "{!items}",
                        "openTextField": "{!openTextField.value}"
                    }
        }
      ]
    }
```
