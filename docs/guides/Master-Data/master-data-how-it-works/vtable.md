---
title: "VTable"
slug: "vtable"
hidden: false
createdAt: "2022-07-28T20:39:04.566Z"
updatedAt: "2022-07-28T21:27:21.269Z"
---

 VTable is a flexible and dynamic user interface designed to handle data from Master Data v2 directly from VTEX Admin. It allows you to create custom applications for managing and visualizing data efficiently, using [JSON schemas](https://developers.vtex.com/vtex-rest-api/docs/starting-to-work-on-master-data-with-json-schema).

To render an app in VTable you must follow these steps:

1. [Create a JSON schema](#1-creating-a-json-schema)
2. [Build the app schema](#2-building-the-app-schema)
3. [Validate the app schema](#3-validating-the-app-schema)
4. [Save the app schema to Master Data](#4-saving-the-app-schema-to-master-data)

Below you can also learn more about all necessary [JSON schema configurations](#json-schema-configurations).

## 1. Creating a JSON schema

First, make sure you have a [data entity](https://developers.vtex.com/docs/guides/master-data-components#data-entity) and a [JSON schema](https://developers.vtex.com/vtex-rest-api/docs/starting-to-work-on-master-data-with-json-schema) associated with it to store data in a specific format.

You can create it with the [Save schema by name](https://developers.vtex.com/docs/api-reference/master-data-api-v2#put-/api/dataentities/-dataEntityName-/schemas/-schemaName-) endpoint. Use your JSON schema as a request body, as exemplified below.

Check the [JSON schema configurations](#json-schema-configurations) section to learn how to configure each field for your specific needs.

### Example JSON schema (request body)

```json
[
    {
        "name": "v1",
        "schema": {
            "properties": {
                "email": {
                    "type": "string"
                },
                "firstName": {
                    "type": "string"
                },
                "lastName": {
                    "type": "string"
                }
            },
            "v-indexed": [
                "email",
                "firstName",
                "lastName"
            ],
            "v-default-fields": [
                "id",
                "email",
                "firstName",
                "lastName"
            ],
            "v-cache": false,
            "required": [
                "email",
                "firstName",
                "lastName"
            ]
        }
    }
]
```

## 2. Building the app schema

To create a VTable app, you must define a schema that specifies the data VTable will use to render a table.

The app schema you create must follow the structure indicated by the [VTable app objects schema](#vtable-app-objects-schema).

For now, start with the [Example app schema](#example-app-schema) and edit it according to your data.

You will validate your app schema's structure in the following step.

### VTable app objects schema

```json
{
   "properties": {
      "name": {
         "type": "string",
         "minLength": 1,
         "maxLenght": 50
      },
      "title": {
         "type": "string",
         "minLength": 1,
         "maxLenght": 50
      },
      "tables": {
         "type": "array",
         "minItems": 1,
         "items": {
            "type": "object",
            "properties": {
               "id": {
                  "type": "string",
                  "minLength": 1
               },
               "title": {
                  "type": "string",
                  "minLength": 1
               },
               "entity": {
                  "type": "string",
                  "minLength": 1
               },
               "model": {
                  "type": "string",
                  "minLength": 1
               },
               "list": {
                  "type": "array",
                  "minItems": 1,
                  "uniqueItems": true,
                  "items": {
                     "type": "string",
                     "minLength": 1
                  }
               },
               "editor": {
                  "type": "object",
                  "properties": {
                     "settings": {
                        "type": "object",
                        "properties": {
                           "sections": {
                              "type": "array",
                              "minItems": 1,
                              "items": {
                                 "type": "object",
                                 "properties": {
                                    "name": {
                                       "type": "string",
                                       "minLength": 1
                                    },
                                    "fields": {
                                       "type": "array",
                                       "minItems": 1,
                                       "uniqueItems": true,
                                       "items": {
                                          "type": "string",
                                          "minLength": 1
                                       }
                                    }
                                 },
                                 "required": [
                                    "name",
                                    "fields"
                                 ]
                              }
                           }
                        },
                        "required": [
                           "sections"
                        ]
                     }
                  },
                  "required": [
                     "settings"
                  ]
               },
               "fields": {
                  "type": "object",
                  "properties": {
                     "id": {
                        "type": "object",
                        "properties": {
                           "width": {
                              "type": "integer"
                           }
                        },
                        "required": [
                           "width"
                        ]
                     }
                  },
                  "required": [
                     "id"
                  ],
                  "additionalProperties": {
                     "type": "object",
                     "properties": {
                        "width": {
                           "type": "integer"
                        }
                     },
                     "required": [
                        "width"
                     ]
                  }
               }
            },
            "required": [
               "fields",
               "entity",
               "model",
               "id",
               "title",
               "list",
               "editor"
            ]
         }
      }
   },
   "required": [
      "name",
      "title",
      "tables"
   ]
}
```

### Example app schema

```json
{
   "name":"users",
   "title":"Users Admin",
   "tables":[
      {
         "id":"main",
         "title":"Users",
         "entity":"users",
         "model":"user-v1",
         "fields":{
            "id":{
               "width":200
            },
            "email":{
               "width":200
            },
            "firstName":{
               "width":300
            }
         },
         "list":[
            "email",
            "firstName",
            "lastName"
         ],
         "editor":{
            "settings":{
               "sections":[
                  {
                     "name":"Personal Data",
                     "fields":[
                        "firstName",
                        "email",
                        "lastName"
                     ]
                  }
               ]
            }
         }
      }
   ]
}
```

You can use this example app schema as a foundation to create your own app. Check the meaning of fields in the example app schema:

| Field | Type | Description |
|---|---|---|
| `name` | string | Name of the schema in Master Data v2. |
| `title` | string | App title. |
| `tables` | array of objects | List of objects containing information about the tables. |
| `tables[i].id` | string | Table ID. |
| `tables[i].title` | string | Table title. |
| `tables[i].entity` | string | Corresponds to the data entity in Master Data, which must exist before creating the app. |
| `tables[i].model` | string |  Relates to the schema associated with the data entity in Master Data. |
| `tables[i].fields` | object | Lists the fields to be displayed. Each field specifies the width it occupies in the table. |
| `tables[i].fields.id` | object | Field name. |
| `tables[i].fields.id.width` | integer | Width of the `id` field. |
| `tables[i].fields.email` | object | Field name. |
| `tables[i].fields.email.width` | integer | Width of the `email` field. |
|`tables[i].fields.firstName` | object | Field name. |
| `tables[i].fields.firstName.width` | integer | Width of the `firstName` field. |
| `tables[i].list` | array of strings | Defines the fields to be rendered in the table. |
| `tables[i].editor` | object | Configures the form's rendering. |
| `tables[i].editor.settings` | object | Form settings. |
| `tables[i].editor.settings.sections` | array of objects | List of form sections and their respective settings. |
| `tables[i].editor.settings.sections[j].name` | string | Setting name. |
| `tables[i].editor.settings.sections[j].fields` | array of strings | List of fields shown in the form. |

Read the [JSON schema configurations](#json-schema-configurations) section to learn how to configure each field for your specific needs.

## 3. Validating the app schema

To validate your app schema, use a tool such as [JSON Schema Validator](https://www.jsonschemavalidator.net/), which allows you to paste the code from [VTable app objects schema](#vtable-app-objects-schema) and the code from your app schema created in [step 2](#2-building-the-app-schema) to check if the structure of your app schema is valid.

## 4. Saving the app schema to Master Data

To save the app schema to Master Data, you must use the [Create document with custom ID](https://developers.vtex.com/docs/api-reference/master-data-api-v2#put-/api/dataentities/-dataEntityName-/documents/-id-) endpoint, adding your app schema as the request body and filling the URL with the information below:

`PUT` `https://{accountName}.{environment}.com.br/api/dataentities/vtable/documents/{appName}?_schema=app`

Your app schema will be saved as a document in the VTable data entity.

After that, you will be able to access the app data in VTable at `https://{accountName}.myvtex.com/admin/vtable/`, replacing `{accountName}` with your VTEX account name.

## JSON schema configurations

VTable parses the JSON Schema configuration and each field to a corresponding UI component. These are some examples of possible configurations:

### Checkbox

To render a checkbox the field must have type **boolean**.

```json
"approved": {
  "type": "boolean",
  "title": "Approved"
}
```

### DropDown

To render a DropDown the field must have the **enum** keyword.

```json
"gender": {
  "type": "string",
  "enum": [
    "Male",
    "Female"
  ]
}
```

### DatePicker

To render a `DatePicker` the field must have the property `format` with the value `date-time`.

```json
"birthdate":{
   "type":"string",
   "format":"date-time"
}
```

### TextArea

To render a `TextArea` the field must have the type `string` and the property `multiline` with the value `true` in the app configuration.

```json
// JSON Schema configuration
"lastName":{
   "type":"string",
   "title":"LastName",
   "maxLenght":250
},
// APP configuration
"lastName":{
   "width":300,
   "multiLine":true
}
```

### Link

The `LinkControl` represents the reference of one data entity to another data entity. To render the `LinkControl` set the properties `link` and `linked_field` where the value of `link` is the link to the referenced schema and the value of `linked_field` is the field that will be referenced.

The `LinkControl` lets you navigate between the related tables. For that, you need to set the properties `relatedApp` and `relatedTable` in the app configuration.

```json
// JSON Schema Configuration
"user":{
   "type":"string",
   "link":"http://api.vtex.com/{accountName}/dataentities/users/schemas/user-v1",
   "linked_field":"email"
}
// APP Configuration
"user":{
   "width":300,
   "relatedApp":"users",
   "relatedTable":"main"
}
```

### TextBox

To render a TextBox the field must be a `string`, `number`, or `integer`. All properties of the JSON Schema that are used to validate the field (e.g., `pattern`, `minLength`, `maxLength`) will be used by VTable to validate the value of the field.

You can add a **mask** to the field in the APP configuration.

```json
// JSON Schema
"phone":{
   "type":"string",
   "maxLenght":100,
   "title":"Phone",
   "pattern":"[0-9]{10,11}"
}

// APP Configuration
"phone":{
   "width":200,
   "mask":"(99) 99999-9999"
},
```

### MultiOptions

To render a `MultiOptions` control, set the field type to `array` and each item must be a `string`. Also, each item must contain the `enum` property, which is an array with the possible strings for that field.

```json
"nationality":{
   "type":"array",
   "items":{
      "type":"string",
      "enum":[
         "Brasil",
         "Argentina",
         "Colombia",
         "Uruguai",
         "Chile",
         "Paraguai"
      ]
   }
},
```

### ArrayControl

If the field type is `array` and the field schema does not match a special case, VTable will use `ArrayControl`.

```json
"list":{
   "type":"array",
   "title":"List",
   "items":{
      "type":"object",
      "properties":{
         "productId":{
            "type":"string",
            "title":"ProductId"
         },
         "quantity":{
            "type":"integer",
            "title":"Qty"
         },
         "name":{
            "type":"string",
            "title":"Name"
         }
      }
   }
}
```

### ObjectControl

To render an `ObjectControl`, set the field type to **object**. The `ObjectControl` is recursive, so it can hold another object as a property.

```json
"complex":{
   "type":"object",
   "title":"Complex",
   "properties":{
      "name":{
         "type":"string",
         "title":"Name"
      },
      "age":{
         "type":"number",
         "title":"Age",
         "minimum":0,
         "maximum":100
      },
      "birthdate":{
         "type":"string",
         "title":"BirthDate",
         "format":"date-time"
      },
      "innerObject":{
         "type":"object",
         "properties":{
            "innerName":{
               "type":"string",
               "title":"InnerName"
            },
            "innerAge":{
               "type":"number",
               "title":"Idade 3",
               "minimum":0,
               "maximum":100
            }
         }
      }
   }
}
```

> To learn more, check the [Master Data v2 API documentation](https://developers.vtex.com/docs/api-reference/master-data-api-v2#overview).