---
title: "B2B Store Theme"
slug: "installing-the-b2b-store-theme"
excerpt: "vtex.b2b-store-theme@2.13.1"
hidden: false
createdAt: "2022-07-18T20:12:55.205Z"
updatedAt: "2022-07-18T20:12:55.205Z"
---
B2B Store Theme is a front-end template to help your store get started with VTEX’s core features for businesses selling to other businesses.

> ⚠️ The B2B Store Theme is not compatible with the [B2B Suite](https://developers.vtex.com/vtex-developer-docs/docs/vtex-b2b-suite) solution. Therefore, these instructions do not apply to stores using the B2B Suite. If you are using the B2B Suite, refer to the [B2B New Store Theme](https://github.com/vtex-apps/b2b-newstore-theme) documentation.

## Prerequisites

### Set up your development environment

Before starting with the B2B Store Theme setup itself, you must:

1. [Set up a workspace to develop in VTEX IO](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-2-basicsetuptodevelopinvtexio) on your machine.
2. Follow [these instructions](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-2-prerequesites) to make sure you meet all the prerequisites to develop using Store Framework.
3. Make sure your store’s catalog is integrated with VTEX Intelligent Search, as described in [this article](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/6wKQgKmu2FT6084BJT7z5V).


### Install required B2B apps

Now you must install the required apps listed below. They are mandatory for the B2B Store Theme to work properly.

* [Wishlist](https://developers.vtex.com/vtex-developer-docs/docs/installing-the-b2b-store-theme#wishlist)
* [Reviews and Ratings](https://developers.vtex.com/vtex-developer-docs/docs/installing-the-b2b-store-theme#reviews-and-ratings)
* [Quick Order](https://developers.vtex.com/vtex-developer-docs/docs/installing-the-b2b-store-theme#quick-order)
* [Location Availability](https://developers.vtex.com/vtex-developer-docs/docs/installing-the-b2b-store-theme#location-availability)
* [Shopper Location](https://developers.vtex.com/vtex-developer-docs/docs/installing-the-b2b-store-theme#shopper-location)
* [Order Quote](https://developers.vtex.com/vtex-developer-docs/docs/installing-the-b2b-store-theme#order-quote)
* [Wordpress Integration](https://developers.vtex.com/vtex-developer-docs/docs/installing-the-b2b-store-theme#wordpress-integration)
* [Admin Organizations](https://developers.vtex.com/vtex-developer-docs/docs/installing-the-b2b-store-theme#admin-organizations)
* [Organizations](https://developers.vtex.com/vtex-developer-docs/docs/installing-the-b2b-store-theme#organizations)

#### Wishlist

[Wishlist](https://github.com/vtex-apps/wish-list) is an app that allows your store’s customers to bookmark their favorite products by clicking on a heart icon.

To install this app on your store, run the following command on the CLI:

```
vtex install vtex.wish-list@1.x
```

#### Reviews and Ratings

The [Reviews and ratings](https://github.com/vtex-apps/reviews-and-ratings) app enables your clients to submit reviews and ratings — using a star rating system — to your store’s products.

Install it using the command: 

```
vtex install vtex.reviews-and-ratings@2.x
```

After that, go to your store's Admin to proceed with the installation. 

Once you are logged in, follow these steps:

1. Go to the **Account Settings** module.
2. Click on `Apps`.
3. Then, click on `My apps`. 
4. Then, find the **Reviews and Ratings** app card and click on `Settings`. 
5. It is recommended that you check the **Display stars in product-rating-summary if there are no reviews** option and uncheck the **Display total reviews number on product-rating-summary block** option, as illustrated below.
6. Click on the `Save` button.

![e683a71-image2](https://user-images.githubusercontent.com/77292838/178748970-44054726-dbc7-4330-971a-291c4acc5340.png)

#### Quick Order

[Quick Order](https://github.com/vtex-apps/quickorder) is an app that enables customers to make bulk orders.

To install it, use the following command: 

```
 vtex install vtex.quickorder@3.x
```

#### Location Availability

The [Location Availability](https://github.com/vtex-apps/location-availability) app shows product availability and shipping information in the storefront based on the customer’s location, providing a personalized shopping experience.

Install this app on your store using the `vtex.location-availability@0.x ` command.


#### Shopper Location

[Shopper Location](https://github.com/vtex-apps/shopper-location) is a geolocation app. Once it is installed, the app tracks the customer’s location, after permission is granted.

To install it, use the following command: 


```
vtex install vtex.shopper-location@0.x
```

#### Order Quote

[Order Quote](https://github.com/vtex-apps/order-quote) is an app that allows the B2B customer to save a cart’s information and use it later for any order. 

To install it, use the following command: 

```
vtex install vtex.orderquote@1.x
```

#### Wordpress integration 

The [Wordpress integration](https://github.com/vtex-apps/wordpress-integration) app enables the account admin to create content on your store’s front through Wordpress’ API.

To install this app, run the following command on the CLI:

```
vtex install vtex.wordpress-integration@2.x
```

#### Admin Organizations

In brief, the [Admin Organizations](https://github.com/vtex-apps/admin-organizations) app is responsible for managing the **Roles** and **Permissions** modules on your store’s Admin.

To install it, run `vtex install vtex.admin-organizations@1.x `on the CLI.

#### Organizations

The [Organizations](https://github.com/vtex-apps/organizations) app allows you to create an organization — a business store — and manage users under that organization with different roles.

Run the command `vtex install vtex.organizations@1.x ` to install it on your store.


### Create fields in Master Data 

After installing all the required apps, you need to create two new fields in Master Data: `isOrgAdmin` and `organizationId`. You must create these fields on the **Client** entity. To do so, check our step-by-step tutorial on [how to create a field on Master Data](https://help.vtex.com/en/tutorial/how-can-i-create-a-field-in-master-data--frequentlyAskedQuestions_1829).

| **Field name** | **Type** |
|---|---|
| `isOrgAdmin` | Boolean |
| `organizationId` | VarChar 100 |

When creating the `isOrgAdmin` field, you should check the following checkboxes:

* **Make readable without credential**
* **Is searchable**
* **Is filterable**

When creating the `organizationId` field, you should check the following checkboxes:

* **Is nullable**
* **Make readable without credential**
* **Allow editing without credential**
* **Allow filter without credential**
* **Is searchable**
* **Is filterable**

> ⚠️ After creating the new fields, it is mandatory to Publish the CL entity and to Reindex it by clicking the buttons illustrated below. Otherwise, the B2B Store Theme will not be applied correctly.
> 
> ![0e71b5a-Group_1_6](https://user-images.githubusercontent.com/77292838/178752430-9ca0e99a-3224-4a89-bbdc-76b9468b98b6.png)


### Install B2B Easy Setup (optional) 

If you are setting up a new store, you can follow the instructions in [this guide](https://developers.vtex.com/vtex-rest-api/docs/installing-b2b-easy-set-up) to quickly set up a test store with sample data using the B2B Easy Setup app.

> ⚠️ We strongly advise that you do not run Easy Setup on a production environment. It will make irreversible changes and may delete some previous configurations on your store.


### Create Master Data schemas

If you have [installed B2B Easy Setup](https://developers.vtex.com/vtex-rest-api/docs/installing-b2b-easy-set-up) and selected **Organizations** resources, you can skip this step, because the required Master Data schemas will already have been created and you should have all **Permissions** and **Roles** ready.

If you have opted not to install B2B Easy Setup, you need to use the **[Save schema by name](https://developers.vtex.com/vtex-rest-api/reference/schemas#saveschemabyname)** endpoint of the **Master Data API - V2 **to create the following schemas.

* [`BusinessPermission schema`](https://developers.vtex.com/vtex-developer-docs/docs/installing-the-b2b-store-theme#businesspermission-schema)
* [`BusinessRole schema`](https://developers.vtex.com/vtex-developer-docs/docs/installing-the-b2b-store-theme#businessrole-schema)
* [`BusinessOrganization schema`](https://developers.vtex.com/vtex-developer-docs/docs/installing-the-b2b-store-theme#businessorganization-schema)
* [`UserOrganization schema`](https://developers.vtex.com/vtex-developer-docs/docs/installing-the-b2b-store-theme#userorganization-schema)


#### `BusinessPermission` schema

| **Path param** | **Value** |
|---|---|
| `data_entity_name` | `BusinessPermission` |
| `schema_name` | `business-permission-schema-v1` |

Request body:

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

#### `BusinessRole` schema

| **Path param** | **Value** |
|---|---|
| `data_entity_name` | `BusinessRole` |
| `schema_name` | `business-role-schema-v1` |

Request body:

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

#### `BusinessOrganization` schema

| **Path param** | **Value** |
|---|---|
| `data_entity_name` | `BusinessOrganization` |
| `schema_name` | `business-organization-schema-v1` |

Request body:

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

#### `UserOrganization` schema

| **Path param** | **Value** |
|---|---|
| `data_entity_name` | `UserOrganization` |
| `schema_name` | `user-organization-schema-v1` |

Request body:

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

## Installation

After following the steps above, you are ready to install the B2B Store Theme. You must:

1. Run the `vtex install vtex.b2bstore@1.x `command on the CLI.
2. Run the `vtex browse` command to see the B2B Store Theme on your browser.

Finally, your storefront should look like this:

![d6eeb9f-image3](https://user-images.githubusercontent.com/77292838/178750578-aac35d1f-4c2b-4053-998e-651242e36900.png)


## Customization

After installing the B2B Store Theme, you can customize it according to your store’s business needs. Check our guide on [Customizing the B2B Store Theme](https://developers.vtex.com/vtex-developer-docs/docs/customizing-the-b2b-store-theme) for more information.