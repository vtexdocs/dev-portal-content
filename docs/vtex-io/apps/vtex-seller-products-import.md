---
title: "If the major of version of MasterData-Proxy app has been changed, from vtex.masterdata-proxy@1.0.0 -> @2.0.0, we have to update this in seller-products-import(CustomMasterdata.ts)."
slug: "vtex-seller-products-import"
excerpt: "vtex.seller-products-import@0.6.5"
hidden: true
createdAt: "2022-07-26T10:55:55.166Z"
updatedAt: "2022-07-26T10:55:55.166Z"
---
## `Import session config` schema

#### URL - `https://{{marketplaceAccount}}.{{environment}}.com/api/dataentities/import_session_config_seller/schemas/main`

```json
{
  "properties": {
    "url": {
      "type": "string",
      "title": "URL"
    },
    "cronExpression": {
      "type": "string",
      "title": "Cron Expression"
    },
    "cronSelection": {
      "type": "string",
      "title": "Cron selected option"
    },
    "status": {
      "title": "Import session config status",
      "type": "string",
      "enum": [
        "active",
        "inactive"
      ]
    },
    "importOnlyNew": {
      "type": "boolean",
      "title": "Import only new products",
      "description": "If false, update existing products"
    },
    "templateUsed": {
      "type": "string",
      "description": "FK to Template"
    },
    "categoryMapId": {
      "type": "string",
      "description": "FK to category map"
    },
    "sellerAccountName": {
      "type": "string",
      "title": "Account that created this document"
    }
  },
  "v-indexed": [
    "url",
    "status",
    "sellerAccountName"
  ],
  "v-cache": false,
  "v-immediate-indexing": true
}
```

## `Import session config Emag` schema

#### URL - `https://{{marketplaceAccount}}.{{environment}}.com/api/dataentities/import_session_config_emag_seller/schemas/main`

```json
{
  "properties": {
    "url": {
      "type": "string",
      "title": "URL"
    },
    "cronExpression": {
      "type": "string",
      "title": "Cron Expression"
    },
    "status": {
      "title": "Import session config status",
      "type": "string",
      "enum": [
        "active",
        "inactive"
      ]
    },
    "importOnlyNew": {
      "type": "boolean",
      "title": "Import only new products",
      "description": "If false, update existing products"
    },
    "proxyLink": {
      "type": "string",
      "title": "Emag proxy link"
    },
    "user": {
      "type": "string",
      "title": "User",
      "description": "Credentials for emag marketplace"
    },
    "password": {
      "type": "string",
      "title": "Password",
      "description": "Credentials for emag marketplace"
    },
    "sellerAccountName": {
      "type": "string",
      "title": "Account that created this document"
    }
  },
  "required": [
    "user",
    "password",
    "proxyLink",
    "url",
    "sellerAccountName"
  ],
  "v-indexed": [
    "user",
    "status",
    "url",
    "sellerAccountName"
  ],
  "v-cache": false,
  "v-immediate-indexing": true
}
```

## `Import sessions` schema

#### URL - `https://{{marketplaceAccount}}.{{environment}}.com/api/dataentities/import_session_seller/schemas/main`

> Be sure to replace the accountName variable in the link field!

```json
{
  "properties": {
    "fileSource": {
      "type": "string",
      "title": "File source",
      "description": "File manager file url"
    },
    "numberOfRecords": {
      "type": "number",
      "minimum": 0
    },
    "status": {
      "type": "string",
      "enum": [
        "init",
        "started",
        "finished",
        "notConfigured",
        "error",
        "locked"
      ]
    },
    "concurrencyId": {
      "type": ["string", "null"],
      "title": "Concurrency ID foreign key"
    },
    "errorMessage": {
      "type": ["string", "null"],
      "title": "Error message"
    },
    "importOnlyNew": {
      "type": "boolean",
      "description": "If true it will update existing products"
    },
    "importSessionConfig": {
      "type": "string",
      "link": "http://api.vtex.com/{{accountName}}/dataentities/{{MASTER_DATA.importSessionConfig.dataEntity}}/schemas/{{MASTER_DATA.importSessionConfig.schema}}",
      "description": "FK to ImportSessionConfig"
    },
    "templateUsed": {
      "type": "string",
      "description": "FK to Template"
    },
    "categoryMapId": {
      "type": "string",
      "description": "FK to category map"
    },
    "sellerAccountName": {
      "type": "string",
      "title": "Account that created this document"
    },
    "cancelled": {
      "type": "boolean",
      "title": "Is import session record cancelled",
      "description": "If true, stop an import session record from being processed"
    }
  },
  "required": ["sellerAccountName"],
  "v-indexed": [
    "status",
    "importSessionConfig",
    "templateUsed",
    "cancelled",
    "sellerAccountName"
  ],
  "v-cache": false,
  "v-immediate-indexing": true
}
```

#### URL - `https://{{marketplaceAccount}}.{{environment}}.com/api/dataentities/import_session_record_seller/schemas/main`

```json
{
  "properties": {
    "importSessionId": {
      "type": "string",
      "title": "FK importSessionId"
    },
    "errorMessage": {
      "type": "string",
      "title": "Error message"
    },
    "status": {
      "title": "Import session config status",
      "type": "string",
      "enum": [
        "init",
        "productCreated",
        "productUpdated",
        "incomplete",
        "error",
        "canceled"
      ]
    },
    "importOnlyNew": {
      "type": "boolean",
      "title": "Import only new products",
      "description": "If false, update existing products"
    },
    "record": {
      "type": "object",
      "properties": {
        "product": {
          "type": "string",
          "title": "Product JSON"
        },
        "sku": {
          "type": "string",
          "title": "SKU JSON"
        },
        "specifications": {
          "type": "string",
          "title": "Specification JSON"
        }
      }
    },
    "cancelled": {
      "type": "boolean",
      "title": "Is import session record cancelled",
      "description": "If true, stop an import session record from being processed"
    },
    "sellerAccountName": {
      "type": "string",
      "title": "Account that created this document"
    }
  },
  "required": [
    "importSessionId",
    "status",
    "sellerAccountName"
  ],
  "v-indexed": [
    "importSessionId",
    "status",
    "sellerAccountName"
  ],
  "v-cache": false,
  "v-immediate-indexing": true
}
```

#### URL - `https://{{marketplaceAccount}}.{{environment}}.com/api/dataentities/import_templates_seller/schemas/main`

```json
{
  "properties": {
    "name": {
      "type": "string",
      "title": "Template name",
      "description": "The name of the template"
    },
    "template": {
      "type": "object",
      "title": "Template",
      "description": "Map of vtex field to custom field",
      "additionalProperties": {
        "type": "string"
      }
    },
    "sellerAccountName": {
      "type": "string",
      "title": "Account that created this document"
    }
  },
  "required": [
    "name",
    "sellerAccountName"
  ],
  "v-indexed": [
    "name",
    "sellerAccountName"
  ]
}
```

#### URL - `https://{{marketplaceAccount}}.{{environment}}.com/api/dataentities/import_category_mapping_seller/schemas/main`

```json
{
  "properties": {
    "categories": {
      "type": "object",
      "title": "Categories",
      "description": "Map of file categories to marketplace categories",
      "additionalProperties": {
        "type": "string"
      }
    },
    "sellerAccountName": {
      "type": "string",
      "title": "Account that created this document"
    }
  },
  "required": [
    "sellerAccountName"
  ],
  "v-indexed": [
    "sellerAccountName"
  ]
}
```