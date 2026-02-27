---
title: "Content plugin"
slug: "content-plugin"
hidden: "false"
createdAt: "2026-01-12T18:00:00.325z"
updatedAt: "2026-02-27T12:26:00.857Z"
---

The Content plugin is a [VTEX CLI plugin](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-command-reference#plugins) that allows you to manage your store's content and CMS settings from the terminal. Use this plugin to manage CMS schemas, organize components, and define Content Types

## Before you begin

Make sure you have the [VTEX CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference) installed on your machine.

## Installing the plugin

To install the plugin, follow these steps:

1. Open your terminal and log in to your VTEX account:

   ```sh
   vtex login {accountName}
   ```

   > ⚠️ Replace `{accountName}` with your VTEX account name, for example, `vtex login yourstore`.

2. Run the following command to install the plugin:

```shell
vtex plugins install @vtex/cli-plugin-content
```

## Default commands

Below is a description of the default commands available in the Content plugin. To view detailed information about each command, click the respective command name.

| Command name | Description |
| --- | --- |
| [`init`](#init) | Creates the CMS folder structure with sample files. |
| [`generate-schema`](#generate-schema) | Creates a unified schema file from your store components, Content Types, and the FastStore base schema. |
| [`split-components`](#split-components) | Splits `sections.json` into separate files, one per component. |
| [`split-content-types`](#split-content-types) | Splits `content-types.json` into separate files, one per Content Type, for improved Content Type management. |
| [`upload-schema`](#upload-schema) | Uploads the unified schema file created by the [`generate-schema`](#generate-schema) command to the Schema Registry, making it available for use in your store's CMS. |

### `init`

Initializes the CMS folder structure in your project with sample files. This command creates the basic directory and sample files to help you start customizing the CMS.

#### Usage

```shell
vtex content init
```

#### Options

| Option | Alias | Description |
| --- | --- | --- |
| `--help` | `-h` | Displays help information for the command. |

<div align="right">
  🔼 <a href="#default-commands">Back</a>
</div>

### `generate-schema`

Generates a single schema file for the CMS by combining component schemas, Content Type definitions, and the FastStore base schema. This command merges your custom component schemas with the FastStore base schema to create a complete schema ready to upload.

#### Usage

```shell
vtex content generate-schema [COMPONENT_SCHEMAS_PATH] [CONTENT_TYPES_PATH]
```

#### Arguments

| Argument | Default | Description |
| --- | --- | --- |
| `COMPONENT_SCHEMAS_PATH` | `cms/faststore/components` | Specifies the path to the directory containing all custom component schemas. |
| `CONTENT_TYPES_PATH` | `cms/faststore/pages` | Specifies the path to the directory containing all custom Content Type definitions. |

#### Options

| Option | Alias | Description |
| --- | --- | --- |
| `--help` | `-h` | Displays help information for the command. |
| `--out=<path>` | `-o` | Specifies the output file path for the generated schema. This option is required to produce an output, and without it, the command will only display a success message but won't save or output the schema. Default value: `cms_schema.json`. |
| `--local=<path>` | `-l` | Uses a local schema file as the base schema instead of fetching the latest FastStore schema from a remote source. |
| `--base=<schemaId>` | `-b` | Specifies a `schemaId` (`$id` property in a schema) to be used as a custom base schema instead of FastStore's default. |

#### Examples

Generate a schema with default paths and save to a file:

```shell
vtex content generate-schema --out schema.json
```

Generate a schema using custom directories:

```shell
vtex content generate-schema cms/components cms/pages --out custom-schema.json
```

Generate a schema using a local base schema:

```shell
vtex content generate-schema --local ./base-schema.json --out final-schema.json
```

<div align="right">
  🔼 <a href="#default-commands">Back</a>
</div>

### `split-components`

Splits a `sections.json` file into separate component files. Use this command when migrating component definitions from the legacy [Headless CMS](https://developers.vtex.com/docs/guides/faststore/headless-cms-overview) to the new CMS to help organize your store components by creating a separate file for each component.

#### Usage

```shell
vtex content split-components
```

#### Options

| Option | Alias | Description |
| --- | --- | --- |
| `--help` | `-h` | Displays help information for the command. |
| `--input=<path>` | `-i` | Specifies the path to the `sections.json` file to split. Default: `cms/faststore/sections.json` |
| `--output=<path>` | `-o` | Specifies the output directory for component files. Default: `cms/faststore/components` |

#### Examples

Split components using default paths:

```shell
vtex content split-components
```

Split components with custom input and output paths:

```shell
vtex content split-components --input ./cms/sections.json --output ./cms/components
```

<div align="right">
  🔼 <a href="#default-commands">Back</a>
</div>

### `split-content-types`

Splits CMS Content Type definitions from `content-types.json` into separate files, one per Content Type. Use this command when migrating custom Content Types from the legacy [Headless CMS](https://developers.vtex.com/docs/guides/faststore/headless-cms-overview) to the new CMS to organize your Content Types into separate files for easier management.

#### Usage

```shell
vtex content split-content-types
```

#### Options

| Option | Alias | Description |
| --- | --- | --- |
| `--help` | `-h` | Displays help information for the command. |
| `--input=<path>` | `-i` | Specifies the path to the `content-types.json` file to split. Default: `cms/faststore/content-types.json` |
| `--output=<path>` | `-o` | Specifies the output directory for Content Type files. Default: `cms/faststore/pages` |
| `--sections=<path>` | `-s` | Specifies the path to `sections.json` used to filter components by `requiredScopes`. Default: `cms/faststore/sections.json` |

#### Examples

Split Content Types using default paths:

```shell
vtex content split-content-types
```

Split Content Types with custom paths:

```shell
vtex content split-content-types --input ./cms/content-types.json --output ./cms/pages --sections ./cms/sections.json
```

<div align="right">
  🔼 <a href="#default-commands">Back</a>
</div>

### `upload-schema`

Uploads a local schema file to the Schema Registry. This command publishes your consolidated CMS schema to the CMS, making it available for use in your store.

#### Usage

```shell
vtex content upload-schema [SCHEMA_PATH]
```

#### Arguments

| Argument | Default | Description |
| --- | --- | --- |
| `SCHEMA_PATH` | `schema.json` | Specifies the path to the schema file to upload. |

#### Options

| Option | Alias | Description |
| --- | --- | --- |
| `--help` | `-h` | Displays help information for the command. |

#### Examples

Upload a schema file with the default path:

```shell
vtex content upload-schema
```

Upload a custom schema file:

```shell
vtex content upload-schema ./custom-schema.json
```

<div align="right">
  🔼 <a href="#default-commands">Back</a>
</div>
