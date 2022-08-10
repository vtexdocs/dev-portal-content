---
title: "Organizations"
slug: "mpower-organizations"
excerpt: "mpower.organizations@2.0.2"
hidden: true
createdAt: "2022-07-26T20:46:51.439Z"
updatedAt: "2022-07-26T20:46:51.439Z"
---
This application allows you to create organization and manage users under that organization with diffrent roles. 

## Usage

Install this app in your workspace

```js
vtex install vtex.organizations@1.x
```

> ### Link application to development workspace
> - clone the application to your working environment and checkout to the correct branch (i.e: `dev-master`)
> - link this app to your workspace (`vtex link --verbose`)

## Prerequisites

In order to run this application following master data schemas and indices should be created. 
Use `MASTER DATA API - V2` in vtex api documentation to create those schemas (https://developers.vtex.com/reference#master-data-api-v2-overview)

These schemas are shared among several applications `vtex.admin-organizations`, `vtex.auth-challenge` and `vtex.organizations`, therefore if you have already created these schemas and indices you can ignore this step

### Master data schemas

<details><summary>BusinessPermission</summary>

``` 

Data Entity Name: BusinessPermission
Schema Name: business-permission-schema-v1

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

<details><summary>BusinessRole</summary>

``` 

Data Entity Name: BusinessRole
Schema Name: business-role-schema-v1

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

<details><summary>BusinessOrganization</summary>

``` 

Data Entity Name: BusinessOrganization
Schema Name: business-organization-schema-v1

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

<details><summary>UserOrganization</summary>

``` 

Data Entity Name: UserOrganization
Schema Name: user-organization-schema-v1

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

### Changes to existing **CL** table
We need to add two fields to existing **CL** master data table. 
```
isOrgAdmin: Boolean 
organizationId: VarChar 100
```
After creating the fields change settings of that fields with edit field feature.
You can update the field settings as shown in the image below. 

<a href="https://drive.google.com/uc?export=view&id=1IzMTKBpB4A9snERILSQJ-DQd1Zp758wE">View Image</a>

>**_NOTE:_** **isOrgAdmin** field should check following checkboxes 
> **Make readable without credential**, 
> **Is searchable**, 
> **Is filterable**, 

> **organizationId** field should check following checkboxes 
> **Is nullable**, 
> **Make readable without credential**, 
> **Allow editing without credential**, 
> **Allow filter without credential**, 
> **Is searchable**, 
> **Is filterable**, 

Dont forget to `save` and `reindex` `CL` table once you add all the fields. 

### [Deprecated] removed master data collections and schemas
>Data Entity Name: **Persona**, Schema Name: **persona-schema-v1**

>Data Entity Name: **OrgAssignment**, Schema Name: **organization-assignment-schema-v1**

## Important

> **_NOTE:_**  create `Manager` role with required permissions using `vtex.admin-organizations` application (https://github.com/vtex/admin-organizations)