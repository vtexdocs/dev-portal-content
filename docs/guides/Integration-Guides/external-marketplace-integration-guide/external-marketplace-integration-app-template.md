---
title: "Creating an integration app from a Template"
slug: "external-marketplace-integration-app-template"
excerpt: "Create an app to integrate with external marketplaces."
hidden: false
createdAt: "2021-09-27T16:02:23.338Z"
updatedAt: "2022-06-23T20:26:15.880Z"
---

The integration Template App is a pre-built app developed by VTEX for our partners to reduce development and implementation time when integrating with external marketplaces. By using the template to build your integration app, connectors will also have the app displayed in the [VTEX App Store](https://apps.vtex.com/).

## What the App Template includes for the VTEX Admin

An integration app created from our App Template already includes:

- **Standard set up page** containing:
  - Activate/deactivate the integration button
  - Field identifying the affiliate ID
  - Field to inform the email that will receive notifications about changes in the affiliate
  - Callback URL used by the VTEX notification system
  - Field for the [sales channel](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV) ID
  - Fields included in the [sales channel form](https://help.vtex.com/en/tutorial/creating-a-trade-policy--563tbcL0TYKEKeOY4IAgAE#filling-in-the-fields)
  - Save Settings button
- **Custom settings page** containing:
  - Button to activate/deactivate [franchise accounts](https://help.vtex.com/en/tutorial/what-is-a-franchise-account--kWQC6RkFSCUFGgY5gSjdl)
- Complete **search endpoint** to retrieve seller configurations using [AppKey and AppToken](https://help.vtex.com/en/tutorial/api-keys--4bFEmcHXgpNksoePchZyy6) generated in the seller’s account, defined by the appVendor.
- **Link to [VTEX Mapper Registration](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-mapper#post-/api/mkp-category-mapper/connector/register)**, allowing sellers to map their catalog according to the marketplace’s definitions.

## Before you begin

The Template App runs in [VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io). Before you begin creating your app from our template, make sure to:

- [Set up your development environment](https://developers.vtex.com/docs/guides/vtex-io-documentation-2-basicsetuptodevelopinvtexio).
- [Install VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-install).
- Have your VTEX Partner account in hand for step 2.

> If you do not have access to a VTEX Account, join our [Partner Program](https://vtex.com/us-en/partner), to become a certified partner.

## Step 1 - Creating your repository from the template

1. Access the [Template App’s repository](https://github.com/vtex/mkp-app-template).
2. Don't forget to request the use of the builders necessary for the development of the app. Read the article [Filling the Application form for development](https://developers.vtex.com/docs/guides/vtex-io-documentation-filling-the-application-form-for-development) and request the builders: admin, docs, graphql, messages, node and react.
3. Click on `Use this template`.
4. Add a **name** to your repository.
5. Select the `Private` option.
6. Do not check the **Include all branches** option.
7. Click on `Create repository from template`.

## Step 2 - App configurations

Once your repository is created from the template, you must configure your app by substituting placeholders and setting up the necessary Template App Configurations.

### Substituting placeholders

Follow the list below to substitute placeholders properly. Once placeholders are replaced, the App’s foundation will include the fields needed to set up the seller and the integration on VTEX's side.

> Placeholders within the `manifest.json` file must follow the rules described in [Manifest Fields Summary](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest).

| Placeholder | Description | Files where it can be found |
|---|---|---|
| appName | Name of the app. This value must follow the kebab case (only minor case letters and the - character). | manifest.json, navigation.json, routes.json, node/service.json, node/constants/variables.ts, react/package.json |
| appVendor | Name of the app’s owner, responsible for its distribution and maintenance. It must be the Partner’s VTEX accountName. | manifest.json, navigation.json, node/routes.json, node/service.json, node/constants/variables.json |
| appTitle | Title of the app that will appear in the VTEX Admin’s screen and left navigation, once the seller accesses it. | messages/context.json, messages/en.json, messages/pt.json, messages/es.json, node/constants/variables.ts |
| connectorEndpoint | Base URL of the backend connector to which notifications coming from VTEX will be sent. Examples: [https://externalconnector.com](https://externalconnector.com) or relative URL; [https://externalconnector.com/api/vtex](https://externalconnector.com/api/vtex). | node/constants/variables.ts, react/areas/ConfigArea/DefaultConfigs/endpoint.tsx |
| connectorEndpointHost | Endpoint host informed in the connectorEndpoint placeholder. Example: externalconnector.com. | manifest.json |
| affiliateId | Affiliate identifier code, which consists of three consonants, whether they are repeated or not. | react/areas/ConfigArea/index.tsx |
| manifestTitle | App’s title in the VTEX App Store. | manifest.json |
| manifestDescription | App’s description in the VTEX App Store. | manifest.json |
| mapperId | Connector’s ID in VTEX Mapper. | admin/navigation.json |
| connectorId | Connector's ID registered in Channel Manager. | node/constants/variables.json |

The fields listed above come with the App Template as default. However, it is possible to remove fields that represent features not used by your integration, like the VTEX Mapper. They are listed ahead in the section [CustomConfigs](#customconfigs).

#### Receiving notifications

To receive notifications from VTEX, the seller needs to implement specific API routes in the endpoint informed in connectorEndpoint. These endpoints are described in the following sections:

- [Catalog notification](#catalog-notification)
- [Store configuration notification](#store-configuration-notification)

##### Catalog notification

To receive product update notifications and product variations (including stock, price and trade policy), you must implement the POST `{{connectorEndpoint}}/catalog/notification` route.

This notification follows the format of our VTEX [Broadcaster Adapter](https://developers.vtex.com/docs/guides/vtex-broadcaster#sku-data).

##### Store configuration notification

To receive notifications of updates to store or seller settings, you must implement the POST `{{connectorEndpoint}}/store-config/notification` route.

The store configuration notification format will vary according to the configuration you implement in your app. The default fields are:

| **Field name** | **Description** | **Type** |
| ---------- | ---------- | -------- |
| `accountName` | Name of the seller’s account in VTEX. | string |
| `active` | Flag that indicates if the seller wants to be active in the marketplace. If false, the connector should deactivate the seller’s products on the marketplace. | boolean |
| `affiliateId` | Unique affiliate ID configured in the seller that identifies its connection with the marketplace. | string |
| `salesChannel` | Sales channel/trade policy ID configured in the seller and being used for this marketplace. | string |
| `email` | Email that’ll be notified about changes related to the affiliate. | string |
| `cookie` | App’s auth cookie. This token can be used when making requests to VTEX APIs with the seller’s account. | string |
| `allowFranchiseAccounts` | Flag indicates if the seller also wants to synchronize their franchise accounts catalog/orders with the marketplace, through the Multilevel Omnichannel Inventory feature. | boolean |

### Template App Configurations

The Template App is divided into two areas:

- **TitleArea:** where the app's title goes, defined by the `{{appTitle}}` field.
- **ConfigArea:** where the app's set up fields go. The ConfigArea has two types of configurations: Default Configurations and Custom Configurations.

#### DefaultConfigs

DefaultConfigs is where the mandatory fields for all apps are included. This section does not need to be changed, regardless of the marketplace's needs, since they are internal configurations used by VTEX. This section already includes:

- Toggle indicating if the integration is activated or inactivated.
- Input field showing the marketplace's affiliateId.
- Input field showing the connector's endpoint, for notifying product and order updates occurred in VTEX.
- Input field for sellers to fill in the email registered as the affiliate.
- Button leading to the account's Affiliate page.
- Selection box showing a list of countries, currencies, time zones and other [information](https://help.vtex.com/en/tutorial/creating-a-trade-policy--563tbcL0TYKEKeOY4IAgAE) registered in the [sales channels](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV) that the seller has set up in their account. This way, sellers can create or edit their sales channel information directly through the Default Configs page.
- Field showing the sales channel's name used for the marketplace, with a button leading to the VTEX account's Sales channels page. This becomes available after the initial set up of the fields listed above.

#### CustomConfigs

The CustomConfigs section is where you find configurations that come as default but are optional, like VTEX Mapper and AllowFranchiseAccounts.

##### Removing VTEX Mapper

You can remove [VTEX Mapper Registration](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-mapper#post-/api/mkp-category-mapper/connector/register) from the app, if the integration does not require mapping categories, or the partner already has a solution for mapping catalog architecture. To remove VTEX Mapper, on the `admin/navigation.json`, remove file the object that defines the Mapper endpoint in the Admin:

```json
{
  "labelId": "admin/app.mapper.tile",
  "path": "/admin/mkp-category-mapper/{{mapperId}}"
}
```

##### Removing _AllowFranchiseAccounts_

When the configuration _AllowFranchiseAccounts_ is configured, the component becomes a toggle indicating whether [franchise accounts](https://help.vtex.com/en/tutorial/what-is-a-franchise-account--kWQC6RkFSCUFGgY5gSjdl) are permitted.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/external-marketplace-integration-app-template-0.png)

You can remove the configuration by performing the following actions:

[block:parameters]
{
  "data": {
    "h-0": "Instruction",
    "h-1": "Files where it can be found",
    "0-0": "Remove component `AllowFranchiseAccounts`",
    "1-0": "Remove field `allowFranchiseAccounts`",
    "2-0": "Set the atribution `allowFranchiseAccounts` as `false`",
    "0-1": "react/areas/ConfigArea/CustomConfigs/index.tsx",
    "1-1": "react/graphql/getConfig.gql\ngraphql/schema.graphql\ngraphql/types.graphql\nnode/typings/configuration.d.ts\nreact/typings/config.d.ts",
    "2-1": "react/areas/ConfigArea/index.tsx:"
  },
  "cols": 2,
  "rows": 3
}
[/block]

#### Adding your own CustomConfigs

CustomConfigs is also where connectors can add their custom fields and most of the app’s development will be made, in case it is necessary to add extra fields like input field for the marketplace’s token, or a button to activate a connector’s new feature, for example. To add custom fields in the App:

1. In the folder `react/areas/configArea/customConfigs`, create a file with the field’s **name** and **.tsx** extension.
   Ex. *email.tsx*, *token.tsx*.

2. In the file, add the following **code**, replacing the `ExampleComponent` field with the name you wish to give it.

```ts
import React from "react"
import { DefaultProps } from '../../../typings/props'

const ExampleComponent: React.FC<DefaultProps> = ({ intl, config }) => {
    return (
    )
}

export default ExampleComponent
```

<table>
    <tr>
        <td><strong>Field</strong></td>
        <td><strong>Description</strong></td>
        <td><strong>Files where it can be found</strong></td>
    </tr>
    <tr>
        <td>DefaultProps</td>
        <td>Defines attributes used by all components present in the integration. The attributes include `intl` (used for field internationalization) and `config` (represents the seller’s current configuration).</td>
        <td>react/typings/props.tsx</td>
    </tr>
</table>

3. To add more properties to the `DefaultProps` for a specific field, **extend the `DefaultProps` interface**, adding the extra properties. This step is optional.

```ts
import React from "react"

export interface CustomProps extends DefaultProps {
 newProp: string
}

const FieldName: React.FC<CustomProps > = ({ intl, config, newProp}) => {
    return (
    )
}

export default FieldName
```

In the example above, a new interface called `CustomProps` was created, that can `extend` the `DefaultProps`, by adding a `newProp` string property. Thus, it is possible to use `CustomProps` in place of `DefaultProps`, and the component can now accept the extra `newProp` property.

4. To use other properties that are not listed in `DefaultProps`, define a **new interface** with the needed properties.

In the example below, a new interface called `CustomProps` is created, with only two properties: `prop1` (string) and `prop2` (number).

```ts
import React from "react"

export interface CustomProps {
 prop1: string.
 prop2: number
}

const FieldName: React.FC<CustomProps > = ({ prop1, prop2 }) => {
    return (
    )
}

export default FieldName
```

5. Add **components developed** to the app’s template.

Here’s an example code for adding an input field:

```ts
import React from "react"
import InputComponent from "../../../components/InputComponent"
import { DefaultProps } from "../../../typings/props"

export interface ExampleProps extends DefaultProps {
  setConfig: React.Dispatch<React.SetStateAction<Configuration>>
}

const ExampleComponent: React.FC<ExampleProps> = ({ intl, config, setConfig }) => {
    return (
   <InputComponent
       id={example}
       label={example}
       canEdit={true}
       initValue={config.email}
       type={'text'}
       required={false}
       tooltip={intl.formatMessage({ id: "admin/app.example" })}
       onChange={value => {
           if(value !== undefined){
             setConfig(oldConfig => ({ ...oldConfig, email: value }))
           }
         }
       }
     />
    )
}

export default ExampleComponent
```

The example above creates an input field called `ExampleComponent`. It uses an extra property, or the `setConfig`, used in this case within the `onChange` property of the Input component. This updates the `email` field in the config, whenever the seller types something within the field. This is how it is rendered in the UI:

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/external-marketplace-integration-app-template-1.png)

6. To finalize the new field’s inclusion, add the new field within the **CustomConfigsArea**. To do that:

- In the `react/areas/configArea/customConfigs/index.tsx` field, add an **import** to the new component developed.
  Following the example above: *import ExampleComponent from './example'*
- Add the component within the ` ` of `CustomConfigArea`.

```ts
const CustomConfigsArea: React.FC<CustomConfigsProps> = ({ intl, config, setConfig }) => {
  return (
    <div>
      <ExemploComponent
        config={config}
        intl={intl}
        setConfig={setConfig}
      />
    </div>
  )
}
```

Note that the `CustomConfigArea` in the template does not include `intl`, `config` and `setConfig`. They must be added, like in the example above, depending on which properties are needed. To add more properties, repeat step 3.

7. If other components are necessary, add them in the `return` object.

The order of components within the `return` affects the order in which components are rendered in the app.

## Step 3 - Translating a component

The app’s internationalization is made using the `intl` library in the `messages` builder, declared in the `manifest.json`. This builder’s addition comes in the Template App as default and does not need to be altered. It is only necessary to add translations for new inserted fields. Check out [Translating the component](https://developers.vtex.com/docs/guides/vtex-io-documentation-8-translating-the-component) to know more.

The `intl` library gets what locale is being used in the VTEX Admin’s context and searches in the `messages` file the corresponding translated text in the `{messageId}`. In case the VTEX Admin is using a language that is not translated in the app, the library will search the id of a language mapped in the app, and automatically translate it to the Admin’s locale.

To add translations to the app:

1. Add the translations in the `messages` folder. The Template app already includes the files:

- **en.json:** english
- **es.json:** spanish
- **pt.json:** portuguese

The following languages are also available in the VTEX Admin: italian (it), japanese (ja), korean (ko), dutch (nl) and romanian (ro).

2. Add the translations in the `{messageId}` to the corresponding locale’s file in the format `"admin/{messageId}": "translation"`.
3. In the selected property that needs translation, substitute the text for the code `intl.formatMessage({ id: 'admin/{messageId}' })`.

- **admin/:** used to identify a translation of a component installed in the VTEX Admin. It must be every Id’s prefix.
- **messageId:** can be substituted for any text. It only accepts letters and `-` to define the text.

To illustrate with an example, let’s suppose we have the following component:

```ts
import React from "react"
import InputComponent from "../../../components/InputComponent"
import { DefaultProps } from '../../../typings/props'

const ExemploComponent: React.FC<DefaultProps> = ({ intl }) => {
    return (
      <InputComponent
        canEdit={true}
        id={'test'}
        initValue={""}
        label={intl.formatMessage({ id: 'admin/app.test.title' })}
        type={'text'}
      />
    )
}

export default ExemploComponent
```

In this case, we have an Input component, type “text”, and its label will be translated according to the VTEX Admin’s locale. If we do not add the id `"admin/app.test.title"` in the `messages` folder, this is what is rendered in the UI:

![Template App 2](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/external-marketplace-integration-app-template-2.png)

Since the id does not exist in any `messages` file, it renders the id itself as a response.

To add the id to the file, we add the code: `“admin/app.test.title”: “Teste no en.json”`. Once the id is rendered in all files, the component will then render:

![Template App 3](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/external-marketplace-integration-app-template-3.png)

## Step 4 - Testing the app locally

1. With the app already configured, open a CLI in the project’s **root**.
2. Login into a test account using the command: `vtex login {{account}}`. Substitute {{account}} by the test account’s *accountName*.
3. Once logged into the account, use the command `vtex use {{workspace}}` to access a development workspace to link the app. Substitute  *{{workspace}}* by any name you choose.
4. Use the command `vtex setup` to adjust IO types and variables based on the values set in the app’s configuration.
5. Use the command `vtex link` to link the app so it operates on VTEX IO’s infrastructure.
6. Access the following address:
   `https://{{workspace}}--{{account}}.myvtex.com/admin/{{appVendor}}/{{appName}}` substituting the placeholders for the chosen values in the previous steps.

### Collecting the app’s configurations

Once the app is configured, it is possible to recover the seller’s configuration through the app. To search a seller’s configuration:

1. Call the following API: `https://{{workspace}}--{(account}}.myvtex.com/_v/{{appVendor}}/{{appName}}/config`

<table>
    <tr>
        <td><strong>Field</strong></td>
        <td><strong>Description</strong></td>
    </tr>
    <tr>
        <td>workspace</td>
        <td>Environment where the app was linked. In production, the workspace is not included in the call, so the endpoint is as follows: <code>https://{(account}}.myvtex.com/_v/{{appVendor}}/{{appName}}/config</code></td>
    </tr>
    <tr>
        <td>account</td>
        <td>Seller’s VTEX account you wish to recover configuration information from.</td>
    </tr>
    <tr>
        <td>appVendor</td>
        <td>Name of the app’s owner, responsible for its distribution and maintenance. It must be the Partner’s VTEX <code>accountName</code>.</td>
    </tr>
    <tr>
        <td>appName</td>
        <td>Name of the app. This value must follow the kebab case (only minor case letters and the `-` character).</td>
    </tr>
</table>

2. Generate the account’s [AppKey and AppToken](https://help.vtex.com/en/tutorial/api-keys--4bFEmcHXgpNksoePchZyy6) to authenticate it.

#### Request’s curl in a workspace

[block:code]
{
  "codes": [
    {
      "code": "curl --location -g --request GET 'https://{{workspace}}--{{account}}.myvtex.com/_v/{{appVendor}}/{{appName}}/config' \\ --header 'appkey: {{appkey}}' \\ --header 'apptoken: {{apptoken}}'",
      "language": "json",
      "name": "Curl example"
    }
  ]
}
[/block]

#### Request’s curl in production

[block:code]
{
  "codes": [
    {
      "code": "curl --location -g --request GET 'https://{{account}}.myvtex.com/_v/{{appVendor}}/{{appName}}/config' \\ --header 'appkey: {{appkey}}' \\ --header 'apptoken: {{apptoken}}'",
      "language": "json",
      "name": "Curl example"
    }
  ]
}
[/block]

## Step 5 - Publishing the app in the VTEX App Store

Once all steps are completed, you must publish the app in VTEX’s App Store, so it is available for clients to install it in their accounts. Follow the instructions on [Submitting your app in the VTEX App Store](https://developers.vtex.com/docs/guides/vtex-io-documentation-submitting-your-app-in-the-vtex-app-store) for this step.