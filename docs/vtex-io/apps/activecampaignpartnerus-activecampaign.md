---
title: "ActiveCampaign"
slug: "activecampaignpartnerus-activecampaign"
excerpt: "activecampaignpartnerus.activecampaign@0.0.11"
hidden: true
createdAt: "2022-07-28T19:36:58.573Z"
updatedAt: "2022-07-29T14:06:25.367Z"
---
How to configure and use ActiveCampaign App with VTEX Store.

This app contains following integrations:

- Create or Update Contacts in ActiveCampaign based on VTEX user login/register
- Send new order to ActiveCampaign when user finishes order.
- Listen to abandoned trigger cart inside VTEX Master Data and sends it to ActiveCampaign

## Configuration

1. Install this app (activecampaignpartnerus.activecampaign@1.x) in the desired account

2. Get following data from your ActiveCampaign account

**Account Name**: Name from ActiveCampaign Account. You can get that info from ActiveCampaign account url yourname.activehosted.com

**Account API Token**: ActiveCampaign App Key. You can get that info into menu -> app -> settings -> developer on ActiveCampaign admin panel.

3. In your admin dashboard, go to **Apps > My Apps > ActiveCampaign**  and input the following settings:

- Account Name: Enter your ActiveCampaign account name.
- Account API Token: Enter your ActiveCampaign integration token.
- Connection ID: Enter your store connection id related with ActiveCampaign [see here how to generate a connection ID](/#creating-connection-id).
- Currency: Enter main store currency.

## Creating Connection ID

You just need to do that action one time.

Make a `POST` request into route `https://youraccountname.api-us1.com/api/3/connections` on your ActiveCampaign account.

Request example:

```json
{
    "connection": {
        "service": "mystorename",
        "externalid": "mystorename",
        "name": "My Store",
        "logoUrl": "https://mystorename.vtexassets.com/assets/vtex.file-manager-graphql/images/7d9a96e7-2e25-4e47-bc49-edc5dd8f7590___809464d8b9be4756fc407c7630b188d9.png",
        "linkUrl": "https://www.mystorename.com"
    }
}
```

[Docs from ActiveCampaign](https://developers.activecampaign.com/reference#create-connection)

From returned success response JSON get the id field and place in your **Connection ID** field inside admin panel on VTEX.

## Creating Abandoned Cart Trigger

1. In your VTEX store panel go to Customer > Master Data
2. On Master Data page access menu "Advanced Settings"
3. Then click on "Estrutura de dados" or "Data Structure" on left menu
4. Click on tab "Triggers"
5. [Add a new trigger](https://help.vtex.com/tutorial/creating-trigger-in-master-data--tutorials_1270) with following config:

### Rules Tab
![Trigger Config](./images/trigger-config-1.jpg)

### Schedule Tab

Choose "Run ASAP" optiom

### If Positive Tab

**Action**: Select action "Send an HTTP Request"

**URL**: fill with endpoint of you app, something with `https://www.yourstore.com/api/io/activeCampaign/abandonedCart`

**Method**: POST

**Headers**: _Name_: Content-Type _Value_:application/json

**Content as JSON**:

```json
{
	"rclastcart": "{!rclastcart}",
	"rclastcartvalue": "{!rclastcartvalue}",
	"rclastsession": "{!rclastsession}",
	"rclastsessiondate": "{!rclastsessiondate}",
	"email": "{!email}",
	"userId": "{!userId}",
	"firstName": "{!firstName}",
	"lastName": "{!lastName}",
	"localeDefault": "{!localeDefault}",
	"id": "{!id}",
	"accountId": "{!accountId}",
	"accountName": "{!accountName}",
	"dataEntityId": "{!dataEntityId}",
	"createdBy": "{!createdBy}",
	"createdIn": "{!createdIn}",
	"updatedBy": "{!updatedBy}",
	"updatedIn": "{!updatedIn}",
	"lastInteractionBy": "{!lastInteractionBy}",
	"lastInteractionIn": "{!lastInteractionIn}"
}
```

7. Enable the trigger and wait. Abandoned cart trigger are triggered following session expire rules from VTEX.

> A page's session expires in 30 minutes. Only after that time do we consider the trigger schedule of the abandoned cart trigger. In other words, the time to be considered is the session's time + the trigger schedule.

ps: abandoned cart trigger only runs on final domain in vtex stores, you can't test with workspace or .myvtex enviroment.