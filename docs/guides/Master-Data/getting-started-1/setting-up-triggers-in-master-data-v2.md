---
title: "Setting up triggers in Master Data v2"
slug: "setting-up-triggers-in-master-data-v2"
hidden: false
createdAt: "2022-07-05T16:11:49.082Z"
updatedAt: "2022-10-28T14:34:21.479Z"
---
A Master Data trigger is an [action](#action) executed after the insert or update of a given document. Actions can be of three types:
- Send an HTTP request.
- Send an email.
- Send email using [Message Center](https://help.vtex.com/pt/tutorial/conhecendo-o-message-center--tutorials_84) template.
- Save data to another data entity.

In this guide, you will learn how to set up Master Data v2 triggers and see some code examples of different use cases.
[block:callout]
{
  "type": "info",
  "body": "- This article is about Master Data v2 triggers. If you want to use Master Data v1, check out the steps described in [How to create a trigger in Master Data v1](https://help.vtex.com/pt/tutorial/creating-trigger-in-master-data--tutorials_1270).\n- You may use Master Data triggers to create add hooks to VTEX first party apps. To do that, [Create a new JSON schema](ref:saveschemabyname) for the data entity used by the app and then follow the instructions below.",
  "title": "Note that:"
}
[/block]
## Creating triggers

Each trigger is described as an item of the array `v-triggers` of a [JSON schema](https://developers.vtex.com/vtex-rest-api/docs/master-data-schema-lifecycle). If you want to create a trigger for a data entity with no associated schema, you may [create a new schema](ref:saveschemabyname) with the trigger settings according to what is described below. To create a new trigger in an existing schema, follow these steps:
1. [Get the schema](https://developers.vtex.com/vtex-rest-api/reference/getschemabyname) to which you wish to add a trigger.
2. Copy the JSON schema from the response and create a new item in the `v-triggers` array, configuring the properties according to your desired behavior. See the [properties](#json-properties) and [example](#complete-example) below.
3. Send your edited schema as the body in the [Save schema by name](ref:saveschemabyname) endpoint.
[block:callout]
{
  "type": "info",
  "title": "Edit triggers",
  "body": "To edit Master Data v2 triggers, follow the same steps described above, just editing the properties you wish instead of creating a new array item."
}
[/block]
### JSON Properties:

| Property  | Description                                        |
|-----------|----------------------------------------------------|
| `name`      | trigger name                                       |
| `active`    | boolean to enable or disable the trigger           |
| `condition` | rule that validates the document before execution  |
| `runAt`     | schedule the action to some time in the future     |
| `weight`    | percentage value used for A/B test                 |
| `retry`     | customize the retry policy                         |
| `action`    | the action that will be executed                   |

#### `name`
It is the trigger name and must be a string value with limit of 100 characters.

#### `active`

Boolean value that indicates if the trigger is either enabled or disabled.

#### `condition`
The rule is the same as Master Data API v2's [Search documents](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/search) route. Example: `status=ready-for-handling`
To get futher information, check the [Search documents](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/search) endpoint reference.

#### `runAt`

In case of scheduling an action in the future you can use the `runAt` property. See the examples below:

- Schedule the execution 10 minutes after.
```json
    {
    	"dateTime": "now",
    	"increment": {
    		"addMinutes": 10
    	}
    }
```

- Schedule the execution six months after the field value `createdIn`.

```json
    {
    	"dateTime": "{!createdIn}",
    	"increment": {
    		"addMonths": 6
    	}
    }
```

#### `weight`
An integer field used to distribute actions. See more information in the article [Setting up an A/B test with Master Data trigger](https://help.vtex.com/en/tutorial/setting-up-a-b-test--4xFzBMHYty6gmEosWGWMC0#).

#### `retry`
By default, VTEX Master Data makes 3 attempts in an interval of 10 minutes. Use this property to override such behavior. See the example below.

Attempt five times in an interval of 30 minutes.
```json
    {
    	"times": 5,
    	"delay": {
    		"addMinutes": 30
    	}
    }
```

#### `action`
There are 3 types of actions: `Call an HTTP Request`, `send an email` and `save in other data entity`. See the examples below.

- Setting up an HTTP Request action.
```json
    {
    	"type": "http",
    	"uri": "http://mydomain.com/api/test",
    	"method": "POST",
    	"headers": {
    		"content-type": "application/json"
    	},
    	"body": {
    		"id": "{!id}",
    		"test": "TestValue",
    		"count": 25
    	}
    }
```

- Setting up an email action.
```json
    {
    	"type": "email",
    	"provider": "default",
    	"subject": "My email with VTEX Master Data",
    	"to": [
    		"{!email}",
    		"test@email.com"
    	],
    	"bcc": [
    		"myemail@test.com"
    	],
    	"replyTo": "noreply@company.com",
    	"body": "My email with document {!id}."
    }
```

- Setting up an email action using a [Message Center](https://help.vtex.com/pt/tutorial/conhecendo-o-message-center--tutorials_84) template.
```json
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
                        "clientName": "{!clientProfileData.firstName} {!clientProfileData.lastName}",
                        "ownerListName": "{!customData.customApps[0].fields.ownerListName}",
                        "ownerListEmail": "{!customData.customApps[0].fields.ownerListEmail}",
                        "items": "{!items}",
                        "openTextField": "{!openTextField.value}"
                    }
    }
```

- Setting up an action saving a document to another data entity.
```json
    {
    	"type": "save",
    	"dataEntity": "copy",
    	"json": {
    		"id": "{!id}",
    		"message": "{!message}",
    		"custom": "created/updated by VTEX Master Data triggers"
    	}
    }
```

### Complete example

```json
    {
    	"properties": {},
    	"v-triggers": [
    		{
    			"name": "copy-document",
    			"active": true,
    			"condition": "status=window-to-cancel",
    			"action": {
    				"type": "save",
    				"dataEntity": "copy",
    				"json": {
    					"id": "{!id}",
    					"message": "{!message}",
    					"custom": "created/updated by VTEX triggers"
    				}
    			},
    			"retry": {
    				"times": 5,
    				"delay": {
    					"addMinutes": 30
    				}
    			}
    		}
    	]
    }
```
