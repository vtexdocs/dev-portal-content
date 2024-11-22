---
title: "Using dynamic expressions in Master Data v2"
slug: "adding-document-field-values-with-dynamic-expressions"
hidden: false
createdAt: "2022-08-03T14:54:11.873Z"
updatedAt: "2022-08-03T14:57:56.514Z"
excerpt: Learn how to automate processes based on Document updates using dynamic expressions.
seeAlso:
    - /docs/guides/setting-up-triggers-in-master-data-v2
---

Dynamic expressions in Master Data v2 enable you to populate document fields dynamically, making it easier to automate tasks like sending personalized marketing emails or processing document updates. This guide explains how to configure and use dynamic expressions with JSON schemas.

## Syntax

Dynamic expressions use placeholders to reference and retrieve values from Document fields, including nested fields. These expressions enable dynamic data usage in actions like sending emails or saving data to another entity.

- **Basic syntax:** Use `{!fieldName}` to reference a top-level field. For example:  
    ```
    {!email}
    ```
- **Nested fields:** Use dot notation to reference fields within nested objects. For example:
    ```
    {!order.clientProfileData.email}
    ```
    
## Before you begin

Before using dynamic expressions, ensure you have a [JSON schema](https://json-schema.org/) configured for your Data Entity in Master Data v2. For more information, refer to [Creating JSON Schemas for a Data Entity](https://developers.vtex.com/docs/guides/starting-to-work-on-master-data-with-json-schema).

## Instructions

### Step 1: Creating a trigger

Follow the instructions in the [Setting up triggers](https://developers.vtex.com/docs/guides/setting-up-triggers-in-master-data-v2) guide to create a trigger in Master Data v2. This defines when the action will be triggered (e.g., Document creation) and what action will be taken.

### Step 2: Configuring a trigger to use dynamic expressions

In the trigger's `action` object, use dynamic expressions to populate the desired fields. For example:

```json
{
  "v-triggers": [
    {
      "name": "email-notification",
      "active": true,
      "action": {
        "type": "email",
        "provider": "default",
        "to": "{!email}",
        "subject": "Welcome, {!name}!",
        "body": "Hello, {!name}. Your order ID is {!order.id}."
      }
    }
  ]
}
```

In this example, the `to` field dynamically retrieves the value of the `email` field from the Document, while the `subject` and `body` incorporate values from `name` and `order.id`.

> ⚠️ Ensure all fields referenced in your dynamic expressions exist in the JSON schema of your Data Entity.

### Step 3: Testing the trigger

Test the configuration using a sample document to validate your trigger configuration and the dynamic expressions. Here’s an example document:

```json
{
  "email": "customer@example.com",
  "name": "Alice",
  "order": {
    "id": "98765"
  }
}
```

The expected output in the triggered email would be:

```
To: customer@example.com
Subject: Welcome to Our Store, Alice!
Body: Hi Alice, thank you for your order #98765.
```
