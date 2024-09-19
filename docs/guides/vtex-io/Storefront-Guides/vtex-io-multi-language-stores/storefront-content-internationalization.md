---
title: "Translating storefront content"
slug: "storefront-content-internationalization"
excerpt: "Learn how to translate text messages from a frontend app."
hidden: false
createdAt: "2020-08-31T17:17:21.148Z"
updatedAt: "2020-09-01T16:14:21.366Z"
---

A message is any website text content set as translatable, and Messages is the VTEX IO app responsible for providing message translations for rendering.

As a background, it's important to know that every text set as translatable during the development of a storefront component is automatically translated either by the *storefront app's definitions* (declared in the app's `/messages` folder) or by the *automatic translation service* (when the storefront app doesn't include any specific translation of a message).

However, considering literal translations and cultural factors, some translations might be unsatisfactory.

Hence, you may want to overwrite a translation provided by the automatic translation service or by the app's definitions with a more specific or representative content of your store.

For example, you may want to set a special login message for Spanish-speaking users from Argentina.

Considering this case, in the following step-by-step, we'll teach you how to overwrite a storefront message with exclusive content for your store through the Messages app.

## Instructions

Follow this step-by-step to translate text messages exported from an app (declared in the app's `messages` folder).

1. [Install](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app) the `vtex.admin-graphql-ide@3.x` app using your terminal.
2. Access the Admin and go to **Store Setting > Storefront > GraphQL IDE**.
3. From the dropdown list, choose the `vtex.messages` app.
4. Write the following mutation command in the text box that is displayed:
[block:code]
{
  "codes": [
    {
      "code": "mutation Save($saveArgs: SaveArgsV2!) {\n  saveV2(args: $saveArgs)\n}",
      "language": "text"
    }
  ]
}
[/block]
5. Then, click on  *Query Variables* at the bottom of the page. Now, your screen may look like the following:

![queryvariables](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/storefront-content-internationalization-1.png)

6. To fill in the *Query Variables* box, you must provide the following parameters:

- `to`: target translation locale.
- `messages`: a list of the messages you want to translate, containing the following parameters:
  - `srcLang`: source message locale. This variable must contain the value `en-DV`, no matter which locale is rendered on the app's interface.
  - `srcMessage`: the `id` of your message string declared in the app's `messages` folder.
  - `context`: the name of the storefront app that declared the message being overwritten.
  - `targetMessage`: the desired translation for the message string.

Take the following example:
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"saveArgs\": {\n    \"to\": \"en-US\",\n    \"messages\": [\n      {\n        \"srcLang\": \"en-DV\",\n        \"srcMessage\": \"store/search.placeholder\",\n        \"context\": \"vtex.store-components@3.x\",\n        \"targetMessage\": \"My personalized Search message\"\n      }\n    ]\n  }\n}",
      "language": "json"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "In VTEX IO, translations of storefront components are kept in a `/messages` folder inside the app's root folder. For example, the English translation of the `search.placeholder` message from the `store-components` app is declared [here](https://github.com/vtex-apps/store-components/blob/master/messages/en.json#L2). Hence, in this example, we just overwrote this message with \"My personalized Search message\" through the Messages app."
}
[/block]
7. After adjusting your query, click the play button to run the declared mutation. The expected response is as follows:
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"data\": {\n    \"saveV2\": true\n  }\n}",
      "language": "json"
    }
  ]
}
[/block]
8. (Optional) If you want to check your changes on the GraphQL IDE, check the " Checking your changes" section.

Now, no further actions are needed on your part. Once you receive the expected response, you are ready to check out the desired changes in your store!

To better understand the full process of overwriting an app message translation, check the following gif:

![AppMessageTranslation](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/storefront-content-internationalization-2.gif)

## Checking your changes

If you have already performed the desired mutations, you can check your changes through a query in the GraphQL IDE.

1. In the **GraphQL admin IDE**, after choosing the `vtex.messages` app, write the following query command in the text box that is displayed:
[block:code]
{
  "codes": [
    {
      "code": "query GetTranslation($args: TranslateWithDependenciesArgs!) {\n  translateWithDependencies(args: $args)\n} ",
      "language": "text"
    }
  ]
}
[/block]
2. Then, click on  *Query Variables* at the bottom of the page.

3. To fill in the *Query Variables* box, you must provide the following parameters:

- `from`: source message locale.
- `messages`: a list of the messages you want to check translations, containing the following parameters:
  - `content`: the `id` of your message string declared in the app's `messages` folder.
  - `context`: the name of the storefront app that declared the message being overwritten.
- `to`: target translation locale.
- `depTree`: the dependency tree as in `"[{\"id\": \"{context}\"}]"`.

Take the following example:
[block:code]
{
  "codes": [
    {
      "code": "{\n\"args\": {\n    \"indexedByFrom\": [\n      {\n      \t\"from\": \"en-DV\",\n      \t\"messages\": [\n          {\n            \"content\": \"store/search.placeholder\",\n            \"context\": \"vtex.store-components@3.x\"\n          }\n        ]\n      }\n    ],\n    \"to\": \"en-US\",\n    \"depTree\": \"[{\\\"id\\\": \\\"vtex.store-components@3.x\\\"}]\"\n  }\n}",
      "language": "json"
    }
  ]
}
[/block]
4. After adjusting your query, click the play button to run it. The expected response is the translated message in the target locale.

For the given example, the expected response is as follows:
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"data\": {\n    \"translateWithDependencies\": [\n      \"My personalized Search message\"\n    ]\n  }\n}",
      "language": "json"
    }
  ]
}
[/block]
