---
title: "log-export@0.x"
slug: "whirlpoolemea-log-export"
excerpt: "whirlpoolemea.log-export@2.0.0"
hidden: true
createdAt: "2022-07-29T10:12:28.293Z"
updatedAt: "2022-07-29T10:12:28.293Z"
---
Is useful if:
- You need to export your store's logs

### Configuration

| Prop name                     | Type                                                      | Description| Default value |
| ----------------------------- | --------------------------------------------------------- |--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `Vtex - App key`                  | `string`       | Your store's api key. It represents the api key allowed for the delete operations.                                      | `''`        |
| `Vtex - App token`             | `string`       | Your store's api token. It represents the api's token allowed for the delete operations                  | `''`        |


### In which accounts the application is installed

- hotpointit
- frwhirlpool


## How to use it

- Uninstall the account.log-export@x.x in the working account.
- Install the whirlpoolemea.log-export@x.x in the desired account.
- Remember to update the (<b>App Key</b>) and (<b>App Token</b>) to allow any api credentials for the `delete operations`
- Any credentials are allowed to get the Logs. You don't need to set the api key and token inside the appSettings if you simply need to export the logs.
- Remember that the api key and token fields are <b>hashed</b> through the `SHA512 algorithm`. Inside the middlewares (<b>checkCredentials.ts</b>) you can find an example of method to hash the string you want to hide (<b>sha512</b>) following the same approach chosen inside this application.