---
title: "Using Policy Engine API on Promotion Alerts"
slug: "using-policy-engine-api-on-promotion-alerts"
hidden: false
createdAt: "2021-05-20T19:03:41.334Z"
updatedAt: "2022-02-03T13:51:02.316Z"
---

The Promotion Alerts is a feature that sets alarms to trigger actions when certain products are sold with undesired prices and promotions. It will allow you to set conditions that check if the prices and the promotions are correct. If not, the system will also generate an alert with information about the product sold at unexpected prices.

This guide will describe all the steps to [create](#creating-a-promotion-alert), [update](#updating-a-promotion-alert), and [delete](#deleting-a-promotion-alert) a Promotion Alert.

## Creating a Promotion Alert

To create a new promotion alert, you should use the [Create Policy](https://developers.vtex.com/vtex-rest-api/reference/policy#policy_createorupdate) endpoint. Let us take a scenario: you want to be alert on Slack if products from the brand *Easy Cosmetics* are sold with a discount greater than 40%. To do so, you should create conditions to check unusual prices or promotions.

### Setting up the `actions`

First, you should define the alert action. This array will define what action it should take when encountering products with the wrong discount or promotion. The alert can have multiple steps. See the code below as an example.
[block:code]
{
  "codes": [
    {
      "code": "\"actions\": [\n                    {\n                        \"id\": \"SendSlackMessage\",\n                        \"metadata\": {\n                            \"channel\": \"C01NJFF35R6\",\n                            \"relatedUsers\": [\n                                \"URUNDC2NB\"\n                            ]\n                        }\n                    }\n                ]",
      "language": "json"
    }
  ]
}
[/block]

#### The `id` parameter

Each object inside it contains an `id` that establishes what the warning will be. Check the table below for its possible values.

| `id` possible values   | Definition                                      |
| ------------------------ | ----------------------------------------------- |
| `SendSlackMessage`     | It sends a Slack message to a specific channel. |
| `SendEmail`            | It sends an email.                              |
| `DeactivatePromotions` | It deactivates the promotions.                  |

In the example case, you should define `id` as `SendSlackMessage`.

#### Other parameters

After setting the `id`, you will determine the `metadata` object that contains the details of the action. Inside it, you should define the `channel` where the alert will notify, and the `alertDescription` displayed when the alert is valid.  You can also inform specific users by including their Slack IDs on the `relatedUsers` field.

#### Other options examples

For sending emails
[block:code]
{
  "codes": [
    {
      "code": "\"actions\": [\n                    {\n                        \"id\": \"SendEmail\",\n                        \"metadata\": {\n                            \"emailList\": [\n                              \"email@email.com\"\n                            ]\n                        }\n                    }\n                ]",
      "language": "json"
    }
  ]
}
[/block]

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Promotions/using-policy-engine-api-on-promotion-alerts-0_60.png)
For deactivating the promotions
[block:code]
{
  "codes": [
    {
      "code": "\"actions\": [\n                    {\n                        \"id\": \"DeactivatePromotions\",\n                    }\n                ]",
      "language": "json"
    }
  ]
}
[/block]
After configuring the `actions`, you should fill the `condition` object with specific information to include the promotion alert context.

### Creating the `conditions`

Every alert will be described by an object that has a `condition` parameter. This will teach the VTEX platform how to know if the action should be executed or not. Conditions usually check a parameter described by the `key` parameter against the`values` by means of the `operation`.

The `condition` object contains a `conditions` array, a `key` string, a `values` array of strings, and an `operation` string. The `condition` parameter allows recursiveness up to a limit of ten object levels inside it.

To create the alert in the example, you should create one condition to define the brand and another to restrict the discount. First, you create the condition for the brand *Easy Cosmetics*. To do so, fill your request body as the example below. You can use the [Get Brand List](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-brand-list) to get the Brand ID of the brand.
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"conditions\": [],\n  \"operation\": \"stringEquals\",\n  \"key\": \"brandId\",\n  \"values\": [\n    \"2000001\"\n  ]\n}",
      "language": "json"
    }
  ]
}
[/block]
After this, you will create the condition to restrict the discount for the brand. Fill your request body as the example below. In this case, `values` contains the percentage discount.
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"conditions\": [],\n  \"operation\": \"numericGreaterThan\",\n  \"key\": \"discountPercentage\",\n  \"values\": [\n    \"40.00\"\n  ]\n}",
      "language": "json"
    }
  ]
}
[/block]
In the table below, you can see other possible values to `key`. It can affect SKUs, brands, and discounts.

#### The `key` parameter

| `key` possible values | Definition                        |
| ----------------------- | --------------------------------- |
| `skuId`               | SKU ID                            |
| `brandId`             | Brand ID                          |
| `discountPercentage`  | Number of the percentage discount |

Now you should establish a relation between the two created conditions. In this case, both conditions should be valid to the alert active, so you should set the `operation` direct from the `condition` object to `and`. Check the example below.
[block:code]
{
  "codes": [
    {
      "code": "\"condition\": {\n                    \"conditions\": [\n                        {\n                            \"conditions\": [],\n                            \"operation\": \"stringEquals\",\n                            \"key\": \"brandId\",\n                            \"values\": [\n                                \"2000001\"\n                            ]\n                        },\n                        {\n                            \"conditions\": [],\n                            \"operation\": \"numericGreaterThan\",\n                            \"key\": \"discountPercentage\",\n                            \"values\": [\n                                \"40.00\"\n                            ]\n                        }\n                    ],\n                    \"operation\": \"and\"\n                }",
      "language": "json"
    }
  ]
}
[/block]
In the table below, you can see other possible values to `operation`. There are numerous ways to relate the conditions you create to the alarm.

#### The `operation` parameter

| `operation` possible values | Definition                                                                                                                                                                                               |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `stringEquals`              | It will check the first string inside `values`, being case sensitive, with the corresponding attribute within the context, when evaluating this policy.                             |
| `stringEqualsIgnoreCase`    | It will check the first string inside `values`, not being case sensitive, with the corresponding attribute within the context, when evaluating this policy.                                            |
| `numericEquals`             | It will consist of the exact number inside `values.`                                                                                                                                                   |
| `numericLessThan`           | It will check if the first number is smaller than the one inside `values` with the corresponding attribute within the context when evaluating this policy. This is a string type.                      |
| `numericLessThanEquals`     | It will check if the first number is smaller than or equals the one inside `values` with the corresponding attribute within the context when evaluating this policy. This is a string type.            |
| `numericGreaterThan`        | It will check if the first number is greater than the one inside `values` with the corresponding attribute within the context when evaluating this policy. This is a string type.                      |
| `numericGreaterThanEquals`  | It will check if the first number is greater than or equals to the one inside `value` with the corresponding attribute within the context when evaluating this policy. This is a string type.          |
| `bool`                      | It will determine if the condition is `true` or `false`, considering what is inside `values.`                                                                                                      |
| `not`                       | It will negate a list of conditions inside the `conditions` array.                                                                                                                                     |
| `or`                        | For the alert to be valid, at least one of the `conditions` should be satisfied.                                                                                                                       |
| `and`                       | For the alert to be valid, all of the `conditions` should be satisfied.                                                                                                                                |
| `dateTimeUtcGreaterThan`    | The date should be greater than the one inside `values`.                                                                                                                                               |
| `dateTimeUtcLessThan`       | The date should be smaller than the one inside `values`.                                                                                                                                               |
| `between`                   | It will check if the corresponding attribute within the context when evaluating this policy is between the other values inside `values`. The `values` array must have exactly two strings inside it. |
[block:callout]
{
  "type": "warning",
  "body": "The values `and`, `or`, and  `not` are the most common ones to use when the `operation` parameter refers to a `conditions` array."
}
[/block]
Check the request body below as an example of the scenario.
[block:code]
{
  "codes": [
    {
      "code": "{\n        \"name\": \"alert-test\",\n        \"description\": \"Alert Test\",\n        \"statements\": [\n            {\n                \"actions\": [\n                    {\n                        \"id\": \"SendSlackMessage\",\n                        \"metadata\": {\n                            \"channel\": \"C01NJFF35R6\",\n                       \"relatedUsers\": [\n                                \"URUNDC2NB\"\n                            ],\n                            \"alertDescription\": \"Avoid selling products from Easy Cosmetics with a discount greater than 40%.\"\n                        }\n                    }\n                ],\n                \"resource\": \"vrn:vtex.promotions-alert:aws-us-east-1:kamila:master:/_v/promotions_alert\",\n                \"condition\": {\n                    \"conditions\": [\n                        {\n                            \"conditions\": [],\n                            \"operation\": \"stringEquals\",\n                            \"key\": \"brandId\",\n                            \"values\": [\n                                \"2000001\"\n                            ]\n                        },\n                        {\n                            \"conditions\": [],\n                            \"operation\": \"numericGreaterThan\",\n                            \"key\": \"discountPercentage\",\n                            \"values\": [\n                                \"40.00\"\n                            ]\n                        }\n                    ],\n                    \"operation\": \"and\"\n                }\n            }\n        ]\n    }\n }",
      "language": "json"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "To fill the `resource` of your account, just use the following code `vrn:vtex.promotions-alert:aws-us-east-1:{accountName}:master:/_v/promotions_alert`, replacing `{accountName}` with the name of your account."
}
[/block]
If your request is successful, it will return `200 OK`.

## Updating a Promotion Alert

To update an existing promotion alert, you should use the [Update Policy](https://developers.vtex.com/vtex-rest-api/reference/put_api-policy-engine-policies-id) endpoint. Follow the steps below to update a promotion alert.

1. Enter the Policy ID in the path.
2. Change the desired information on the request body.
3. Send the request.
4. If the response to the request is `200 OK`, the promotion alert was updated.

## Deleting a Promotion Alert

To delete an existing promotion alert, you should use the [Delete Policy](https://developers.vtex.com/vtex-rest-api/reference/policy_delete) endpoint. Follow the steps below to delete a promotion alert.

1. Enter the Policy ID in the path.
2. If the response to the request is `200 OK`, the promotion alert was deleted.
