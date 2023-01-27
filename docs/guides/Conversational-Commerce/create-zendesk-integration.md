---
title: 'Create Zendesk integration'
slug: 'create-zendesk-integration'
hidden: false
createdAt: '2022-08-19T17:15:28.422Z'
updatedAt: '2022-08-22T20:30:59.655Z'
---

This guide explains how to create an integration with the Conversational Commerce VTEX and Zendesk. To do so, first you will need to gather some information about the store's Zendesk account:

- **URL:** store's Zendesk account URL, such as `https://{accountName}.zendesk.com`.
- **Tags:** tags that will be added by VTEX when a new ticket is created by the user.
- **Email:** email of a Zendesk account that will be used to create the tickets. This email must have permission to create tickets and add comments to it via API. This email will be used in the `from` field in all support emails.
- **API token**: Zendesk API token that needs to be sent to [VTEX support](https://support.vtex.com/hc/en-us/requests). To generate a token, follow the steps in this [article](https://support.zendesk.com/hc/en-us/articles/4408889192858-Generating-a-new-API-token).

After gathering this information, follow the steps below:

1. [Create a custom field](https://support.zendesk.com/hc/en-us/articles/4408883152794) with the phone number that will be used on WhatsApp Business by the store. You must send its ID to [VTEX support](https://support.vtex.com/hc/en-us/requests).
2. [Create a webhook](https://support.zendesk.com/hc/en-us/articles/4408839108378-Creating-webhooks-in-Admin-Center) with the following information:

- **URL:** `https://live-agent-handler.vtex.com/webhooks/zendesk`
- **Request method:** POST
- **Request format:** JSON
- **Bearer token:** API token
- **Token:** token send by VTEX

3. Once you created the webhook, you must create two triggers to activate the webhook. To create a trigger check this [documentation](https://support.zendesk.com/hc/en-us/articles/4408886797466). Create the first trigger with the following information:

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Conversational%20Commerce/create-zendesk-integration-0_29.png)

- **Trigger name:** VTEX Chatbot - Incoming Live Agent Comment
- **Category:** `Notifications`
- **Conditions**: Meet ALL of the following conditions
  - `Tags` `Contains at least one of the following` `{VTEX tag}`
  - `Update via` `Is not Web service (API)`
  - `Ticket` `Is` `Updated`
  - `Comment` `Is` `Present, and requester can see the comment`

1. On **Actions**, you must select `Notify active webhook` and the previously configurated webhook.

2. Add the following code on the **JSON body** field. Notice that you must replace `{{ticket.ticket_field_6228597897108}}` with the custom field ID previously created.

```json
{
  "conversationId": "{{ticket.external_id}}",
  "userPhoneNumber": "{{ticket.requester.phone}}",
  "accountPhoneNumber": "{{ticket.ticket_field_6228597897108}}",
  "ticket": {
    "id": "{{ticket.id}}",
    "comment": "{{ticket.latest_public_comment}}",
    "author": "{{ticket.latest_public_comment.author.name}}"
  }
}
```

6. [Create another trigger](https://support.zendesk.com/hc/en-us/articles/4408886797466) that will be activated when a support agent resolves a ticket. Fill the trigger form with the following information:

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Conversational%20Commerce/create-zendesk-integration-1_58.png)

- **Conditions:**
  - Meet ALL of the following conditions
    - `Tags` `Contains at least one of the following` `{VTEX tag}`
  - Meet ANY of the following conditions
    - `Status` `Changed to` `Solved`
    - `Status` `Changed to` `Closed`

1. On **Actions**, you must select the `Notify active webhook` and the previously configurated webhook.
2. Add the following code on the **JSON body** field. Notice that you must replace `{{ticket.ticket_field_6228597897108}}` with the custom field ID previously created.

```json
{
  "conversationId": "{{ticket.external_id}}",
  "userPhoneNumber": "{{ticket.requester.phone}}",
  "accountPhoneNumber": "{{ticket.ticket_field_6228597897108}}",
  "event": {
    "type": "enable_bot"
  }
}
```
