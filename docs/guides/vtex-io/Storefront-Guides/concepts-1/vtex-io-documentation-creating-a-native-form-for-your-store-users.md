---
title: "Creating a native form for your store users"
slug: "vtex-io-documentation-creating-a-native-form-for-your-store-users"
hidden: false
createdAt: "2020-06-03T16:02:44.837Z"
updatedAt: "2022-12-13T20:17:45.509Z"
---
In traditional brick-and-mortar stores, the sales team plays a crucial role in establishing relationships with customers, fostering trust, and providing personalized support. However, online stores lack the in-person interactions that often help reassure customers and create a direct channel for feedback and inquiries.

To bridge this gap, ecommerce stores can leverage forms as essential tools for promoting clear and direct communication with customers. Forms not only enable customers to ask questions and share suggestions but also allow businesses to gather valuable insights into customer satisfaction.

With Store Framework, your store can integrate a native form component with [Master Data v2](https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw), facilitating data collection and storage.
  
## Instructions

### Step 1 - Creating the JSON Schema in Master Data v2

To begin, you must create a [JSON schema](https://json-schema.org/understanding-json-schema) in [Master Data v2](https://help.vtex.com/tutorial/master-data--4otjBnR27u4WUIciQsmkAw#v2-schemas) that defines the fields your form will include and the expected input types. This schema acts as a blueprint for your form, specifying both required data fields and storage structure.

Make a request to the [Save Schema by name](https://developers.vtex.com/docs/api-reference/master-data-api-v2#put-/api/dataentities/-dataEntityName-/schemas/-schemaName-) endpoint to define your schema. Include the JSON example below as the default request body, modifying it to suit your store’s needs:

<details>
  <summary>Schema example</summary>
  ```json
  {
    "title": "Person",
    "type": "object",
    "properties": {
      "firstName": {
        "type": "string",
        "title": "First Name",
        "description": "The person's first name."
      },
      "lastName": {
        "type": "string",
        "title": "Last Name",
        "description": "The person's last name."
      },
      "age": {
        "description": "Age in years which must be equal to or greater than zero.",
        "title": "Age",
        "type": "integer",
        "minimum": 0,
        "maximum": 120
      },
      "height": {
        "type": "number",
        "minimum": 0.3,
        "maximum": 2.9,
        "title": "Your height in meters",
        "multipleOf": 0.01
      },
      "emailAddress": {
        "type": "string",
        "format": "email",
        "title": "Email address"
      },
      "address": {
        "title": "Address",
        "type": "object",
        "properties": {
          "streetType": {
            "type": "string",
            "title": "Street Type",
            "enum": [
              "street",
              "road",
              "avenue",
              "boulevard"
            ]
          },
          "streetAddress": {
            "type": "string",
            "title": "Address"
          },
          "streetNumber": {
            "type": "integer",
            "title": "Street Number"
          }
        },
        "required": [
          "streetType", "streetAddress", "streetNumber"
        ]
      },
      "agreement": {
        "type": "boolean",
        "title": "Do you agree with the terms?"
      }
    },
    "required": [
      "firstName",
      "lastName",
      "agreement"
    ],
    "v-security": {
      "publicJsonSchema": true,
      "allowGetAll": false,
      "publicRead": [ "fieldExample" ],
      "publicWrite": [ "fieldExample" ],
      "publicFilter": [ "fieldExample" ]
    }
  }
  ```
</details>

> ℹ️ Bear in mind that the schema's language will define the form's default language.

When making the request to create the JSON Schema, remember to:

- Replace the `dataEntityName` value with the data entity name in which you want to save the user data fetched from the form.
- Replace the `schemaName` value with a name of your choosing. The value defined will be the form's JSON Schema name.

Once the request is executed successfully, the JSON Schema is ready and you can create the form in your store's theme.

> ℹ️ Master Data v2 doesn't have an interface, so all actions regarding the user form must be done through the [Master Data API v2](https://developers.vtex.com/docs/api-reference/master-data-api-v2#overview).

### Step 2 - Configuring the Store Form app

Lastly, you must configure the Store Form app and the blocks it exports to make your store render the native Store Framework form component.

Access the [Store Form app documentation](https://developers.vtex.com/docs/apps/vtex.store-form) and follow the step-by-step instructions to complete its configuration.

Once the form is configured in your store's theme, users will be able to share their information using the component. Your store will receive this information and automatically save it in Master Data v2, so you can interact with it using the [Master Data API v2](https://developers.vtex.com/docs/api-reference/master-data-api-v2#overview).
