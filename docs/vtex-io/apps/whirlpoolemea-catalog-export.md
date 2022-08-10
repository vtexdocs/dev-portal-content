---
title: "catalog-export@0.x"
slug: "whirlpoolemea-catalog-export"
excerpt: "whirlpoolemea.catalog-export@1.0.0"
hidden: true
createdAt: "2022-07-29T10:27:12.946Z"
updatedAt: "2022-07-29T10:27:12.946Z"
---
Is useful if:
- You need to export your store's catalog into an <b>xls file</b>.

### Configuration

| Prop name                     | Type                                                      | Description| Default value |
| ----------------------------- | --------------------------------------------------------- |--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `Marketplace Hostname`                  | `string`       | Your store hostname. For example: whirlpool.fr                                      | `''`        |
| `Marketplace Api Key`             | `string`       | AES256 encrypted store api key. Read this documentation for more details                  | `''`        |
| `Marketplace Api Token`                 | `string`       | AES256 encrypted store api key. Read this documentation for more details   nvalues.                                            | `''`        |
| `Marketplace Sales channels ids (comma separated)`       | `string`       | The list of sales channels ids separated by comma. For example: 1,2,3                                                               | `''`        |
| `Marketplace Services ids ids (comma separated)`                      | `boolean`      | The list of additional services ids separated by comma. For example: 1,2,3            | `''`        |
| `CC project`              | `Boolean`       | Flag to be filled if the project is a Closed Community project                                 | `false`        |


| Prop name           | Type                                                      | Description| Default value |
| ------------------- | --------------------------------------------------------- |----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `Seller Account Name`                  | `string`       | Seller account name, from which retrieve the commercial offers.                                      | `''`        |
| `Seller Api Key`             | `string`       | AES256 encrypted seller api key. Read this documentation for more details                  | `''`        |
| `Seller Api Token`                 | `string`       | AES256 encrypted seller api key. Read this documentation for more details   nvalues.                                            | `''`        |

| Prop name           | Type                                                      | Description| Default value |
| ------------------- | --------------------------------------------------------- |----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `Catalog Export Fields Checklist`                  | `[boolean]`       | A list of XLS columns name that the user want to export through the file                                     | `[true, true, ...]`        |
| `Sellable Map`             | `[object]`       | A list of Sellables in which each object is composed by a <b>key</b> and <b>value</b> fields.| `[{"key": "EPP","value": "sellableEPP"},{"key": "FF","value": "sellableFF"},{"key": "VIP","value": "sellableVIP"}]`       |

### In which accounts the application is installed

- hotpointit
- itwhirlpool
- frwhirlpool


## How to use it

- Uninstall the account.catalog-export@x.x in the working account.
- Install the whirlpoolemea.catalog-export@x.x in the desired account.
- Each time a new column should be added into the xls file, remember to extend the logic (<b>exportCatalog.ts</b>) and create a new appSettings (<b>manifest.json</b>)
- Remember that the api key and token fields are encrypted through the `AES256 algorithm`. Inside the utils (<b>cryptography.ts</b>) you can find an example of method to encrypt the string you want to hide (<b>AES256Encode</b>). Remember to use the same <b>cypherKey</b> and <b>cipherIV</b> parameters expected by the decrypt method!