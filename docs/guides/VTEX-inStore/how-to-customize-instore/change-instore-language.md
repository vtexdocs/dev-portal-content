---
title: "Change inStore language"
slug: "change-instore-language"
hidden: false
createdAt: "2021-08-11T19:15:27.435Z"
updatedAt: "2021-08-24T20:17:18.836Z"
---
Currently, it is possible to use inStore in Portuguese, English, or Spanish.

By default, the application's language is Portuguese, but you can change it by editing the `checkout-instore-custom.js` file. Check out the [How to customize inStore](https://developers.vtex.com/vtex-rest-api/docs/how-to-customize-instore) guide for further information on how to access this file.

## Edit the `checkout-instore-custom.js` file

To change the language used on inStore, first check if the `checkout-instore-custom.js` file contains the following lines of code:
[block:code]
{
  "codes": [
    {
      "code": "window.LOCALE_MESSAGES = {\n  locale: 'pt',\n  messages: {\n    pt: {\n     \n    },\n  },\n};\n\nfunction setNewLocaleMessages() {\n  const localeEvent = new Event('changeLocaleMessages')\n  localeEvent.data = window.LOCALE_MESSAGES\n  document.dispatchEvent(localeEvent)\n}\n\nif (window.inStoreIsLoaded) {\n  setNewLocaleMessages();\n} else {\n  document.addEventListener(\n    'load.instore',\n    function() {\n      setNewLocaleMessages();\n    },\n    false\n  );\n}",
      "language": "javascript"
    }
  ]
}
[/block]
If the code above already exists in your `checkout-instore-custom.js` file, move on to the next step. If only part of it is in your file, replace the current snippet with all the code above.

The language of the application is defined by the `locale` property, which is found in line 3 of the code above (`locale: 'pt'`). Note that, in this case, inStore is set to Portuguese (`pt`).

To change the language, you must replace the locale value with the desired language code.

Check out the possible values for this property:
[block:parameters]
{
  "data": {
    "h-0": "Name",
    "h-1": "Type",
    "h-2": "Description",
    "h-3": "Possible values",
    "0-0": "`locale`",
    "0-1": "string",
    "0-3": "- `pt`\n- `en`\n- `es`",
    "0-2": "Sets the language used on inStore. Use `pt` for Portuguese, `en` for English or `es` for Spanish."
  },
  "cols": 4,
  "rows": 1
}
[/block]

## Example

If you want to change inStore's language to English, for example, replace the `pt` value with `en`. The resulting code snippet should look like this:
[block:code]
{
  "codes": [
    {
      "code": "window.LOCALE_MESSAGES = {\n  locale: 'en',\n  messages: {\n    en: {\n     \n    },\n  },\n};",
      "language": "javascript"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "After making changes in the code, make sure you press the `Save` button."
}
[/block]

## Check out your changes

To see the reflected changes on inStore, enter the menu and click the `Reset app local data` button, as shown in the image below.
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/change-instore-language-0.png)
