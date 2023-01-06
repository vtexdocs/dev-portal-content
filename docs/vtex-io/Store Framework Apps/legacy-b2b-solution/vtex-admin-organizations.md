---
title: "Admin Organizations"
slug: "vtex-admin-organizations"
excerpt: "vtex.admin-organizations@1.1.0"
hidden: false
createdAt: "2020-06-03T15:19:29.881Z"
updatedAt: "2020-12-11T11:57:26.752Z"
---

This is an Admin application for managing `Roles` and `Permissions` for organizations on a B2B Store.

## Usage

Install the app, then you can see the features in Admin view.

```sh
vtex install vtex.admin-organizations@1.x
```

### Prerequisites

In order to run this application, you must create the following Master Data schemas.
Use `MASTER DATA API - V2` in [VTEX API documentation](https://developers.vtex.com/reference#master-data-api-v2-overview) to create those schemas.

These schemas are shared among several applications `admin-organizations`, `organizations-challenge` and `organizations`. Therefore, if you have already created these schemas before, you can ignore this step.

<details>

<summary>Permissions</summary>

Data Entity Name: BusinessPermission
Schema Name: business-permission-schema-v1

``` json
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

<summary>Roles</summary>

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

### Add Required roles

You will need to create the Manager role to make other related applications work properly.
Use `label` as `Manager` and `name` as `manager` to create this role.
