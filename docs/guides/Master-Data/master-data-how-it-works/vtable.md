---
title: "VTable"
slug: "vtable"
hidden: false
createdAt: "2022-07-28T20:39:04.566Z"
updatedAt: "2022-07-28T21:27:21.269Z"
---
VTable is a flexible and dynamic user interface you can set up using [JSON schemas](https://developers.vtex.com/vtex-rest-api/docs/starting-to-work-on-master-data-with-json-schema) to manage data from Master Data v2.

To have an app rendered in VTable you must:
1. Make sure you have a data entity with an existing [JSON schema](https://developers.vtex.com/vtex-rest-api/docs/starting-to-work-on-master-data-with-json-schema) associated.
2. [Build the app schema](#build-the-app-schema)
3. [Validate the app schema](#validate-the-app-schema)
4. [Saving to Master Data](#saving-to-master-data)

Below you can also learn more about all necessary [JSON schema configurations](#json-schema-configurations).

## Build the app schema

To create an app we need to build a schema that contains the data VTable will use to render a specific table. A common app looks like the example below.

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

You can use this JSON as a base to create your own apps. 

Learn more about some important fields in the app schema:
- The `entity` field is the data entity in Master Data and must exist before creating the app.
- The `model` field is the schema related to the data entity in Master Data
- The `fields` field contains the list of fields to be rendered. Each field contains a simple configuration defining the appropriate width each field will take when rendered in the table.
- The `list` field contains the list of fields that will be rendered in the table.
- The `editor` field contains the configuration for rendering the form.

Also, check the [JSON schema configurations](#json-schema-configurations) to learn how to configure each field in your app.

## Validate the app schema

The following JSON Schema contains the structure and validation of the VTable app objects. You can validate the app using [JSON Schema Validator](https://www.jsonschemavalidator.net/).

```json
{
   "properties":{
      "name":{
         "type":"string",
         "minLength":1,
         "maxLenght":50
      },
      "title":{
         "type":"string",
         "minLength":1,
         "maxLenght":50
      },
      "tables":{
         "type":"array",
         "minItems":1,
         "items":{
            "type":"object",
            "properties":{
               "id":{
                  "type":"string",
                  "minLength":1
               },
               "title":{
                  "type":"string",
                  "minLength":1
               },
               "entity":{
                  "type":"string",
                  "minLength":1
               },
               "model":{
                  "type":"string",
                  "minLength":1
               },
               "list":{
                  "type":"array",
                  "minItems":1,
                  "uniqueItems":true,
                  "items":{
                     "type":"string",
                     "minLength":1
                  }
               },
               "editor":{
                  "type":"object",
                  "properties":{
                     "settings":{
                        "type":"object",
                        "properties":{
                           "sections":{
                              "type":"array",
                              "minItems":1,
                              "items":{
                                 "type":"object",
                                 "properties":{
                                    "name":{
                                       "type":"string",
                                       "minLength":1
                                    },
                                    "fields":{
                                       "type":"array",
                                       "minItems":1,
                                       "uniqueItems":true,
                                       "items":{
                                          "type":"string",
                                          "minLength":1
                                       }
                                    }
                                 },
                                 "required":[
                                    "name",
                                    "fields"
                                 ]
                              }
                           }
                        },
                        "required":[
                           "sections"
                        ]
                     }
                  },
                  "required":[
                     "settings"
                  ]
               },
               "fields":{
                  "type":"object",
                  "properties":{
                     "id":{
                        "type":"object",
                        "properties":{
                           "width":{
                              "type":"integer"
                           }
                        },
                        "required":[
                           "width"
                        ]
                     }
                  },
                  "required":[
                     "id"
                  ],
                  "additionalProperties":{
                     "type":"object",
                     "properties":{
                        "width":{
                           "type":"integer"
                        }
                     },
                     "required":[
                        "width"
                     ]
                  }
               }
            },
            "required":[
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
   "required":[
      "name",
      "title",
      "tables"
   ]
}
```

## Saving to Master Data

To save the app JSON Object to Master Data, you must add the document to the VTable data entity. An example of that request's path is:

```
https://{accountName}.{environment}.com.br/api/dataentities/vtable/documents/{appName}?_schema=app
```

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

To render a TextBox the field must be a `string`, `number`, or `integer`. All properties of the JSON Schema that are used to validate the field (e.g., `pattern`, `minLength`, `maxLength` will be used by VTable to validate the value of the field.

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
[block:callout]
{
  "type": "info",
  "body": "To learn more, check the [Master Data v2 API documentation](https://developers.vtex.com/docs/api-reference/master-data-api-v2#overview)."
}
[/block]