---
title: "Sending emails with triggers in Master Data v2"
slug: "sending-emails-with-triggers-in-master-data-v2"
hidden: false
createdAt: "2022-08-03T14:48:49.642Z"
updatedAt: "2022-08-03T14:56:02.147Z"
---
You can use Master Data v2 triggers to automatically send emails to your customers.
[block:callout]
{
  "type": "info",
  "body": "You can find more information about creating triggers in the article [Setting up triggers in Master Data v2](https://developers.vtex.com/vtex-rest-api/docs/setting-up-triggers-in-master-data-v2)."
}
[/block]


## Properties

| Field     | Description     |
| ---------- | ---------- |
| type*       | The action type must be `email` |
| provider*       | Message Center provider name (usually named as `default`) |
| from*       | define name and email of from address |
| to*       | list of emails that email will be sended |
| replyTo*       | list of addresses to reply |
| subject*       | subject line for this e-mail |
| body*       | the message body |
| bcc       | address collection that contains the blind carbon copy (BCC) |

\* Required

## Dynamic expressions

You can use dynamic expressions to deal with document properties in these settings. For more information, look at the [Article on dynamic expressions](https://developers.vtex.com/vtex-rest-api/docs/adding-document-field-values-with-dynamic-expressions).

## JSON Schema example:

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
          "cco": [ "testcco@test.com" ],
          "replyTo": "noreply@email.com",
          "body": "VTEX Master Data Triggers email body"
        } 
      ]
    }
```