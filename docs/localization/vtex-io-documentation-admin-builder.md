---
title: "Messages builder"
slug: "vtex-io-documentation-messages-builder"
hidden: false
createdAt: "2024-08-13T17:00:00.000Z"
updatedAt: ""
excerpt: "Learn how to use the VTEX IO Messages builder."
---

The `messages` builder handles the internationalization (i18n) of strings in VTEX IO apps using [React](https://react.dev/). Instead of declaring static strings in frontend components, this builder allows you to use an ID for each message, which will be dynamically replaced by the corresponding string in the user's language.

For details about creating apps that support multiple languages, see [7. Translating the component in the Storefront apps tutorial](https://developers.vtex.com/docs/guides/vtex-io-documentation-8-translating-the-component).

## Folder structure

The `messages` builder uses a folder named `messages` located in the app’s root folder. This folder contains one JSON file for each language used in the app. Each file is named with the corresponding two lower case letters of the language in [ISO 639-1 code](https://www.loc.gov/standards/iso639-2/php/code_list.php). For instance, English is represented by the code `en`, Spanish by `es`, and Portuguese by `pt`.

  ```txt
  messages
  ┣ 📄en.json
  ┣ 📄es.json
  ┗ 📄pt.json
  ```

- `{language-code}.json`: JSON file of the language containing the message IDs with their corresponding strings in the language. See below examples of file names:

    - `en.json`: JSON file for English messages.
    - `es.json`: JSON file for Spanish messages.
    - `pt.json`: JSON file for Portuguese messages.

## Usage

To develop an app using the `messages` builder, refer to the following steps:

1. **Start with a React app**: First, you need an app that uses the [`react` builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-react-builder). If you are starting from scratch, you can download the [React app boilerplate](https://github.com/vtex-apps/react-app-template/tree/master/react).
2. **Add the react i18n libraries**: Open a terminal in the `react` folder of your app and run the command `yarn add react-intl@3 && yarn add @types/react-intl@3 --dev`.
3. **Configure the manifest**: Access the `manifest.json` file and add the `messages` builder to the builders list.

```diff manifest.json
{
  ...
  "builders": {
  "react": "3.x",
  "docs": "0.x",
+ "messages": "1.x"
  },
  ...
}
```

4. **Add the message identifiers:** Use the string identifiers in your React code. In the example below, `"store/my-app.hello"` is a string identifier for the `<Formatted Message>` component.

```typescript
import React from 'react'
import { FormattedMessage } from 'react-intl'

const HelloWorld = () => {
  return (
   <div>
     <FormattedMessage id="store/my-app.hello"/>
   </div>
  )
}

export default HelloWorld
```

5. **Add the messages files with the strings:** Create a separate JSON file for each language in the `messages` folder. In each file, define an object where the keys are the message IDs and the values are  the corresponding strings in the target language. See the examples below for English, Spanish, and Portuguese.

```json en.json
{
  "store/my-app.hello": "Hello World!"
}
```

```json es.json
{
  "store/my-app.hello": "Hola Mundo!"
}
```

```json pt.json
{
  "store/my-app.hello": "Olá Mundo!"
}
```
