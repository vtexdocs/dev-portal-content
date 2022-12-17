---
title: "Store Configuration"
slug: "store-configuration"
hidden: false
createdAt: "2019-12-24T00:49:31.616Z"
updatedAt: "2020-05-19T23:09:39.823Z"
---
## notificationsSettings

Customer Credit sends invoice payment reminders by e-mail to customers. By default, this e-mail is sent on the invoice due date at 12:00 PM UTC. However, a different notification timeline can be set using the optional `notificationsSettings` field.

The `notificationsSettings` object can set up to three e-mail notification triggers each for the pre-payment (`daysPrior`) and post-payment (`daysAfter`) timelines. These triggers can be set in a range of 10 days before or after the payment day.

![Prepayment-PostPayment-Timeline](https://files.readme.io/05c7e7d-Prepayment-PostPayment-Timeline.png)

In the example above, this is what the `notificationsSettings` object would look like:
[block:code]
{
  "codes": [
    {
      "code": "{\n  ...\n  \n  \"notificationsSettings\": {\n        \"daysPrior\": [\n            {\n                \"days\": 9,\n                \"timeOfDay\": \"12:00:00\"\n            },\n            {\n                \"days\": 5,\n                \"timeOfDay\": \"12:00:00\"\n            },\n            {\n                \"days\": 1,\n                \"timeOfDay\": \"12:00:00\"\n            }\n        ],\n        \"daysAfter\": [\n            {\n                \"days\": 4,\n                \"timeOfDay\": \"12:00:00\"\n            },\n            {\n                \"days\": 6,\n                \"timeOfDay\": \"12:00:00\"\n            },\n            {\n                \"days\": 8,\n                \"timeOfDay\": \"12:00:00\"\n            }\n        ]\n    }\n  \n  ...\n}\n",
      "language": "json"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "As mentioned before, the `notificationSettings` field is optional. If you do not wish to set any e-mail notification triggers for either `daysPrior` or `daysAfter`, just fill in the corresponding parameter with an empty array (`[]`).",
  "title": "You do not need to set triggers in both timelines"
}
[/block]