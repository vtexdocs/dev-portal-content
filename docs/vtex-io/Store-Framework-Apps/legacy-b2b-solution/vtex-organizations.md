---
title: "Organizations"
slug: "vtex-organizations"
hidden: false
createdAt: "2020-06-03T15:19:18.888Z"
updatedAt: "2022-03-17T16:38:51.319Z"
---
This application allows you to create organization and manage users under that organization with diffrent roles. 

## Usage

1. Install this app in your workspace by running this CLI command:

	```js
	vtex install vtex.organizations@1.x
	```

2. Link the application to your development workspace, as follows:

   Clone the application to your working environment and checkout to the correct branch (i.e: `dev-master`).

   Link this app to your workspace (`vtex link --verbose`).

## Prerequisites

In order to run this application, you must create the following Master Data schemas and indices using [MASTER DATA API - V2](https://developers.vtex.com/api-reference/master-data-api-v2#overview).

These schemas are shared among several applications: `vtex.admin-organizations`, `vtex.auth-challenge` and `vtex.organizations`. Therefore, if you have already created these schemas and indices you can ignore this step.

### Master data schemas

<details>
	<summary>BusinessPermission</summary>

	Data Entity Name: BusinessPermission
	Schema Name: business-permission-schema-v1

```json
{
	"properties": {
		"name": {
			"type": "string"
		},
		"label": {
			"type": "string"
		}
	},
	"v-default-fields": [
		"name",
		"label",
		"id"
	],
	"required": [
		"name"
	],
	"v-indexed": [
		"name"
	],
	"v-security": {
		"allowGetAll": true,
		"publicRead": [
			"name",
			"label",
			"id"
		],
		"publicWrite": [
			"name",
			"label"
		],
		"publicFilter": [
			"name",
			"id"
		]
	}
}

```
</details>

<details>

<summary>BusinessRole</summary>

Data Entity Name: BusinessRole
Schema Name: business-role-schema-v1

```json
{
	"properties": {
		"name": {
			"type": "string"
		},
		"label": {
			"type": "string"
		},
		"permissions": {
			"type": "string"
		}
	},
	"definitions": {
		"permission": {
			"type": "string"
		}
	},
	"v-default-fields": [
		"name",
		"label",
		"id",
		"permissions"
	],
	"required": [
		"name"
	],
	"v-indexed": [
		"name"
	],
	"v-security": {
		"allowGetAll": true,
		"publicRead": [
			"name",
			"label",
			"permissions",
			"id"
		],
		"publicWrite": [
			"name",
			"label",
			"permissions"
		],
		"publicFilter": [
			"name",
			"id"
		]
	}
}
```
</details>

<details>

<summary>BusinessOrganization</summary>

Data Entity Name: BusinessOrganization
Schema Name: business-organization-schema-v1

```json
{
	"properties": {
		"name": {
			"type": "string"
		},
		"telephone": {
			"type": "string"
		},
		"address": {
			"type": "string"
		},
		"email": {
			"type": "string"
		}
	},
	"v-default-fields": [
		"name",
		"telephone",
		"id",
		"address",
		"email"
	],
	"required": [
		"name",
		"telephone"
	],
	"v-indexed": [
		"name",
		"telephone",
		"email"
	],
	"v-security": {
		"allowGetAll": true,
		"publicRead": [
			"name",
			"telephone",
			"id",
			"address",
			"email"
		],
		"publicWrite": [
			"name",
			"telephone",
			"address",
			"email"
		],
		"publicFilter": [
			"name",
			"telephone",
			"id",
			"email"
		]
	}
}
```

</details>

<details>

<summary>UserOrganization</summary>

Data Entity Name: UserOrganization
Schema Name: user-organization-schema-v1

```json
{
	"properties": {
		"email": {
			"type": "string"
		},
		"businessOrganizationId": {
			"type": "string",
			"link": "http://api.vtex.com/{{accountName}}/dataentities/BusinessOrganization/schemas/business-organization-schema-v1"
		},
		"roleId": {
			"type": "string",
			"link": "http://api.vtex.com/{{accountName}}/dataentities/BusinessRole/schemas/business-role-schema-v1"
		},
		"status": {
			"type": "string"
		}
	},
	"v-default-fields": [
		"email",
		"id",
		"businessOrganizationId",
		"roleId",
		"status"
	],
	"required": [
		"email",
		"businessOrganizationId",
		"roleId",
		"status"
	],
	"v-indexed": [
		"email",
		"businessOrganizationId",
		"roleId",
		"status"
	],
	"v-security": {
		"allowGetAll": true,
		"publicRead": [
			"email",
			"id",
			"businessOrganizationId",
			"businessOrganizationId_linked",
			"roleId",
			"roleId_linked",
			"status"
		],
		"publicWrite": [
			"id",
			"email",
			"businessOrganizationId",
			"roleId",
			"status"
		],
		"publicFilter": [
			"email",
			"id",
			"businessOrganizationId",
			"roleId",
			"status"
		]
	},
	"v-triggers": [
		{
			"name": "organization-assignment-accept-email",
			"active": true,
			"condition": "status=APPROVED",
			"action": {
				"type": "email",
				"provider": "default",
				"subject": "Organization Assignment Acceptance",
				"to": [
					"{!email}"
				],
				"replyTo": "noreply@company.com",
				"body": "You have been assigned to {!businessOrganizationId_linked.name}."
			}
		},
		{
			"name": "organization-assignment-decline-email",
			"active": true,
			"condition": "status=DECLINED",
			"action": {
				"type": "email",
				"provider": "default",
				"subject": "Organization Assignment Decline",
				"to": [
					"{!email}"
				],
				"replyTo": "noreply@company.com",
				"body": "You have left the organization {!businessOrganizationId_linked.name}."
			}
		}
	]
}
```

</details>

### Changes to existing CL table

You must add two fields to existing **CL** Master Data table:

|Field name|Type|Settings|
|-|-|-|
|`isOrgAdmin`|Boolean|Make readable without credential, Is searchable, Is filterable |
|`organizationId`|VarChar 100|Is nullable, Make readable without credential, Allow editing without credential, Allow filter without credential, Is searchable, Is filterable |

After creating the fields, change their settings by using the `Edit field` option.
You can update the field settings as shown in the image below. 

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/vtex-io/Store%20Framework/legacy-b2b-solution/vtex-organizations-1.png)

Dont forget to `save` and `reindex` `CL` table once you add all the fields. 

### Deprecated Master Data collections and schemas

| Data Entity Name | Schema Name |
|-|-|
|Persona|persona-schema-v1|
|OrgAssignment|organization-assignment-schema-v1|


## Add Required roles

It is necessary to create the Manager role with required permissions using the [Admin Organizations](https://github.com/vtex/admin-organizations) app.