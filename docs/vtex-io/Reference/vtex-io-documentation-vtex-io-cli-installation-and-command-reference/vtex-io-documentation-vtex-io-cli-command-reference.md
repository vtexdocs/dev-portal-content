---
title: "Command reference"
slug: "vtex-io-documentation-vtex-io-cli-command-reference"
hidden: false
createdAt: "2021-04-04t22:02:14.325z"
updatedAt: "2022-12-13T20:17:44.857Z"
---

This documentation is a reference for:

- [VTEX IO CLI default commands](#default-commands)
- [VTEX plugins commands](#plugins)
> ⚠️ VTEX IO CLI 3.x now has a plugin-based architecture, which means that certain commands from earlier versions are now implemented as plugins.  These plugins include: `add`, `autoupdate`, `config`, `debug`, `infra`, `lighthouse`, `logs`, `redirects`, `settings`, `submit`, `support`, `test`, and `url`. Access [this link](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-plugins) to learn more about VTEX IO CLI plugins.

## Default commands

Below is a brief description of the default commands available in VTEX IO CLI. For detailed information about each command, you can click on the respective command name.  You can also get this information in your terminal by adding `--help` or `-h` after the command name.

| Command name                                          | Feature                                                                                                                         |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [`autoupdate`](#autoupdate)                           | Automatically updates VTEX IO CLI.                                                                                              |
| [`browse`](#browse)                                   | Opens your current workspace and account URL in a new browser window.                                                           |
| [`deploy`](#deploy)                                   | Publishes an app as a stable version. Only works for apps previously published as a release candidate version.                  |
| [`deprecate`](#deprecate)                             | Deprecates the specified app, uninstalling and downgrading it to the latest stable version on every VTEX account.               |
| [`deps diff`](#deps-diff)                             | Displays the differences between the dependencies of two distinct workspaces.                                                   |
| [`deps list`](#deps-list)                             | Displays the complete dependency tree of the current workspace.                                                                 |
| [`deps update`](#deps-update)                         | Updates a dependency of the current workspace. If not specified which one, it updates all dependencies.                         |
| [`edition get`](#edition-get)                         | Displays the Edition App version installed on the current account.                                                              |
| [`edition set`](#edition-set)                         | Sets the version of the Edition App for the current account.                                                                    |
| [`help`](#help)                                       | Displays help for VTEX CLI commands.                                                                                            |
| [`init`](#init)                                       | Copies starting files and folders from VTEX boilerplates to your local directories.                                             |
| [`install`](#install)                                 | Installs an app on the current workspace. If no app is specified, it defaults to the app in the current directory.              |
| [`link`](#link)                                       | Syncs the app in the current directory with the development workspace being used.                                               |
| [`list`](#list)                                       | Lists the apps installed on the current workspace and account.                                                                  |
| [`local token`](#local-token)                         | Prints the user auth token and copies it to the clipboard.                                                                      |
| [`login`](#login)                                     | Logs into a VTEX account.                                                                                                       |
| [`logout`](#logout)                                   | Logs out from the current VTEX account.                                                                                         |
| [`publish`](#publish)                                 | Publishes the app in the current directory as a release candidate version.                                                      |
| [`release`](#release)                                 | (For git users only.) Bumps the app version, commits, and pushes to the remote repository for the app in the current directory. |
| [`setup`](#setup)                                     | Sets up typing and tools for the current development environment.                                                               |
| [`switch`](#switch)                                   | Switches to another VTEX account.                                                                                               |
| [`undeprecate`](#undeprecate)                         | Reverts a deprecated version of an app to a stable version.                                                                     |
| [`uninstall`](#uninstall)                             | Uninstalls an app from the current account and workspace.                                                                       |
| [`unlink`](#unlink)                                   | Unlinks an app from the current workspace.                                                                                      |
| [`update`](#update)                                   | Updates all installed apps to the latest minor or patch version. Does not upgrade to another major version.                     |
| [`whoami`](#whoami)                                   | Prints details about the current account, workspace, environment, and login information.                                        |
| [`workspace abtest finish`](#workspace-abtest-finish) | Stops all A/B tests on the current account.                                                                                     |
| [`workspace abtest start`](#workspace-abtest-start)   | Starts a new A/B test on the current workspace.                                                                                 |
| [`workspace abtest status`](#workspace-abtest-status) | Displays the results of the active A/B tests.                                                                                   |
| [`workspace delete`](#workspace-delete)               | Deletes one or many workspaces from the current account.                                                                        |
| [`workspace list`](#workspace-list)                   | Lists all workspaces of the current account.                                                                                    |
| [`workspace promote`](#workspace-promote)             | Promotes the current workspace to the master branch. Only applicable for production workspaces.                                 |
| [`workspace reset`](#workspace-reset)                 | Cleans all configurations of the specified workspace and recreates them with the configurations from the master branch.         |
| [`workspace status`](#workspace-status)               | Displays information about the specified workspace.                                                                             |
| [`workspace use`](#workspace-use)                     | Creates and switches to a new workspace or simply switches to an existing one.                                                  |

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### autoupdate

> ℹ️ This command refers to the `@vtex/cli-plugin-autoupdate` plugin. Access [this link](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-plugins) to learn more about VTEX IO CLI plugins.

Automatically updates VTEX IO CLI.

#### Usage

```shell
  vtex autoupdate [CHANNEL]
```

#### Arguments

| Argument               | Description                            |
| ---------------------- | -------------------------------------- |
| **CHANNEL** (optional) | Channel for which to display the logs. |

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### browse

Opens your current workspace and account URL in a new browser window.

#### Usage

```shell
  vtex browse [PATH]
```

#### Arguments

| Argument            | Description                                                      |
| ------------------- | ---------------------------------------------------------------- |
| **PATH** (optional) | Relative path from `https://{workspace}--{account}.myvtex.com/`. |

#### Options

| Option   | Alias | Description                       |
| -------- | ----- | --------------------------------- |
| **--qr** | -q    | Prints a QR Code on the terminal. |

#### Examples

```shell
  vtex browse
  vtex browse admin
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### deploy

> ℹ️ This command refers to the `@vtex/cli-plugin-deploy` plugin. Access [this link](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-plugins) to learn more about VTEX IO CLI plugins.

Publishes an app as a stable version. This command is specifically designed for apps that have been previously published as a release candidate version [see vtex publish --help].

#### Usage

```shell
  vtex deploy [APPID]
```

#### Arguments

| Argument             | Description                                         |
| -------------------- | --------------------------------------------------- |
| **APPID** (optional) | The name and version of the app you want to deploy. |

#### Options

| Option      | Alias | Description                                                                          |
| ----------- | ----- | ------------------------------------------------------------------------------------ |
| **--yes**   | -y    | Answers yes to all prompts.                                                          |
| **--force** | -f    | (Use with caution.) Ignores the testing period of 7 minutes after publishing an app. |

#### Examples

```shell
  vtex deploy
  vtex deploy vtex.service-example@0.0.1
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### deprecate

Deprecates the specified app, uninstalling and downgrading it to the latest stable version on every VTEX account.

#### Usage

```shell
  vtex deprecate [APPID] [ITHAPPID]
```

#### Arguments

| Argument                | Description                                                                                                   |
| ----------------------- | ------------------------------------------------------------------------------------------------------------- |
| **APPID** (optional)    | The name and version of the app to deprecate, specified in the format `{vendor}.{appname}@{x.x.x}`.           |
| **ITHAPPID** (optional) | The names and versions of multiple apps to deprecate, specified in the format (`{vendor}.{appname}@{x.x.x}`). |

#### Options

| Option    | Alias | Description                 |
| --------- | ----- | --------------------------- |
| **--yes** | -y    | Answers yes to all prompts. |

#### Examples

```shell
  vtex deprecate
  vtex deprecate vtex.service-example@0.0.1
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### deps diff

> ℹ️ This command refers to the `@vtex/cli-plugin-deps` plugin. Access [this link](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-plugins) to learn more about VTEX IO CLI plugins.

Displays the differences between the dependencies of two distinct workspaces. If a single parameter is passed, the command compares the dependencies of the specified workspace with those of the master workspace. If no parameter is passed, the command compares the dependencies of the current workspace with those of the master workspace.

#### Usage

```shell
  vtex deps diff [WORKSPACE1] [WORKSPACE2]
```

#### Arguments

| Argument                  | Description                                        |
| ------------------------- | -------------------------------------------------- |
| **WORKSPACE1** (optional) | First workspace for comparison.                    |
| **WORKSPACE2** (optional) | [default: master] Second workspace for comparison. |

#### Example

```shell
  vtex deps diff workspace1 workspace2
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### deps list

> ℹ️ This command refers to the `@vtex/cli-plugin-deps` plugin. Access [this link](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-plugins) to learn more about VTEX IO CLI plugins.

Displays the complete dependency tree of the current workspace.

#### Usage

```shell
  vtex deps list
```

#### Options

| Option     | Alias | Description                                  |
| ---------- | ----- | -------------------------------------------- |
| **--keys** | -k    | Shows only key dependencies.                 |
| **--npm**  | -n    | Includes dependencies from the npm registry. |

#### Alias

```shell
  vtex deps ls
```

#### Examples

```shell
  vtex deps list
  vtex deps ls
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### deps update

> ℹ️ This command refers to the `@vtex/cli-plugin-deps` plugin. Access [this link](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-plugins) to learn more about VTEX IO CLI plugins.

Updates a dependency of the current workspace. If not specified which dependency, the command updates all dependencies of the workspace.

#### Usage

```shell
  vtex deps update [APPID] [ITHAPPID]
```

#### Arguments

| Argument                | Description                                                                                                |
| ----------------------- | ---------------------------------------------------------------------------------------------------------- |
| **APPID** (optional)    | The name and version of the app to update, specified in the format `{vendor}.{appname}@{x.x.x}`.           |
| **ITHAPPID** (optional) | The names and versions of multiple apps to update, specified in the format (`{vendor}.{appname}@{x.x.x}`). |

#### Examples

```shell
  vtex deps update
  vtex deps update vtex.service-example@0.0.1
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### edition get

> ℹ️ This command refers to the `@vtex/cli-plugin-edition` plugin. Access [this link](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-plugins) to learn more about VTEX IO CLI plugins.

Displays the Edition App version installed on the current account.

#### Usage

```shell
  vtex edition get
```

#### Example

```shell
  vtex edition get
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### edition set

> ℹ️ This command refers to the `@vtex/cli-plugin-edition` plugin. Access [this link](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-plugins) to learn more about VTEX IO CLI plugins.

Sets the Edition App version for the current account.

#### Usage

```shell
  vtex edition set EDITION
```

#### Arguments

| Argument    | Description                         |
| ----------- | ----------------------------------- |
| **EDITION** | Name of the Edition App to install. |

#### Example

```shell
  vtex edition set editionName
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### help

Displays help for VTEX CLI commands.

#### Usage

```shell
  vtex help [COMMAND]
```

#### Arguments

| Argument               | Description           |
| ---------------------- | --------------------- |
| **COMMAND** (optional) | Command to show help. |

#### Options

| Option    | Alias | Description                             |
| --------- | ----- | --------------------------------------- |
| **--all** | -     | Displays all commands available in CLI. |

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### init

Copies starting files and folders from VTEX boilerplates to your local directories.

#### Usage

```shell
  vtex init
```

#### Example

```shell
  vtex init
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### install

Installs an app on the current workspace. If no app is specified, it defaults to the app in the current directory.

#### Usage

```shell
  vtex install [APPID] [ITHAPPID]
```

#### Arguments

| Argument                | Description                                                                                               |
| ----------------------- | --------------------------------------------------------------------------------------------------------- |
| **APPID** (optional)    | The name and version of the app to install, specified in the format `{vendor}.{appname}@{x.x.x}`.         |
| **ITHAPPID** (optional) | The names and versions of multiple apps to install, specified in the format `{vendor}.{appname}@{x.x.x}`. |

#### Options

| Option      | Alias | Description                                                      |
| ----------- | ----- | ---------------------------------------------------------------- |
| **--force** | -f    | Installs the specified app without checking for route conflicts. |

#### Examples

```shell
  vtex install
  vtex install vtex.service-example@0.x
  vtex install vtex.service-example@0.0.1
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### link

Syncs the app in the current directory with the development workspace being used.

#### Usage

```shell
  vtex link
```

#### Options

| Option                    | Alias | Description                                                                                                                                                  |
| ------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **--account=account**     | -a    | Starts a development session in the specified account. Must be used together with the '--workspace' flag.                                                    |
| **--clean**               | -c    | Cleans the builder cache.                                                                                                                                    |
| **--setup**               | -s    | Sets up typing definitions before linking the app [see vtex setup --help].                                                                                   |
| **--unsafe**              | -u    | Allows linking the app despite TypeScript errors.                                                                                                            |
| **--workspace=workspace** | -w    | Starts a development session in the specified workspace. It can be used together with the '--account' flag to switch from the current account and workspace. |
| **--no-watch**            | -     | Does not watch for file changes after the initial link.                                                                                                      |

#### Example

```shell
  vtex link -a youraccount -w yourworkspace
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### list

Lists the apps installed on the current workspace and account.

#### Usage

```shell
  vtex list
```

#### Aliases

```shell
  vtex ls

```

#### Examples

```shell
  vtex list
  vtex ls
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### local token

Prints the user auth token and copies it to the clipboard.

#### Usage

```shell
  vtex local token
```

#### Example

```shell
  vtex local token
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### login

Logs into a VTEX account.

#### Usage

```shell
  vtex login [ACCOUNT]
```

#### Arguments

| Argument               | Description             |
| ---------------------- | ----------------------- |
| **ACCOUNT** (optional) | Account name to log in. |

#### Options

| Option                    | Alias | Description                        |
| ------------------------- | ----- | ---------------------------------- |
| **--workspace=workspace** | -w    | Logs into the specified workspace. |

#### Examples

```shell
  vtex login
  vtex login storecomponents
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### logout

Logs out from the current VTEX account.

#### Usage

```shell
  vtex logout
```

#### Example

```shell
  vtex logout
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### publish

Publishes the app in the current directory as a release candidate version.

#### Usage

```shell
  vtex publish
```

#### Options

| Option                    | Alias | Description                                      |
| ------------------------- | ----- | ------------------------------------------------ |
| **--force**               | -f    | Publishes the app independently of SemVer rules. |
| **--tag=tag**             | -t    | Adds the specified tag to the release.           |
| **--workspace=workspace** | -w    | Uses the specified workspace for the app.        |
| **--yes**                 | -y    | Answers yes to all prompts.                      |

#### Example

```shell
  vtex publish
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### release

(For git users only.) Bumps the app version, commits, and pushes to the remote repository for the app in the current directory.

#### Usage

```shell
  vtex release [RELEASETYPE] [TAGNAME]
```

#### Arguments

| Argument                   | Description                            |
| -------------------------- | -------------------------------------- |
| **RELEASETYPE** (optional) | Release type (major, minor, or patch). |
| **TAGNAME** (optional)     | Tag name (e.g., stable, beta).         |

#### Examples

```shell
  vtex release
  vtex release patch
  vtex release patch beta
  vtex release minor stable
  vtex release pre
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### setup

Configures typing definitions and tools for the current development environment.

#### Usage

```shell
  vtex setup
```

#### Options

| Option              | Alias | Description                                                                                        |
| ------------------- | ----- | -------------------------------------------------------------------------------------------------- |
| **--ignore-linked** | -i    | Configures typing definitions from published apps and ignores typing definitions from linked apps. |
| **--all**           | -     | Configures all available typing definitions, configurations, and tools.                            |
| **--tooling**       | -     | Configures Prettier, Husky, and ESLint.                                                            |
| **--tsconfig**      | -     | Configures React and Node TSconfig, if applicable.                                                 |
| **--typings**       | -     | Configures GraphQL and React typing definitions.                                                   |

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### switch

Switches to another VTEX account.

#### Usage

```shell
  vtex switch ACCOUNT
```

#### Arguments

| Argument    | Description                           |
| ----------- | ------------------------------------- |
| **ACCOUNT** | The name of the account to log in to. |

#### Options

| Option                    | Alias | Description                       |
| ------------------------- | ----- | --------------------------------- |
| **--workspace=workspace** | -w    | Moves to the specified workspace. |

#### Examples

```shell
  vtex switch storecomponents
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### undeprecate

Reestablishes a deprecated version of an app as a stable version.

#### Usage

```shell
  vtex undeprecate [APPID] [ITHAPPID]
```

#### Arguments

| Argument                | Description                                                                                                   |
| ----------------------- | ------------------------------------------------------------------------------------------------------------- |
| **APPID** (optional)    | The name and version of the app to undeprecate, specified in the format `{vendor}.{appname}@{x.x.x}`.         |
| **ITHAPPID** (optional) | The names and versions of multiple apps to undeprecate, specified in the format `{vendor}.{appname}@{x.x.x}`. |

#### Options

| Option    | Alias | Description                 |
| --------- | ----- | --------------------------- |
| **--yes** | -y    | Answers yes to all prompts. |

#### Example

```shell
  vtex undeprecate vtex.service-example@0.0.1
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### uninstall

Uninstalls an app from the current workspace. If no app is specified, it defaults to the app in the current directory.

#### Usage

```shell
  vtex uninstall [APPNAME] [ITHAPPNAME]
```

#### Arguments

| Argument                  | Description                                                                                                 |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **APPNAME** (optional)    | The name and version of the app to uninstall, specified in the format `{vendor}.{appname}@{x.x.x}`.         |
| **ITHAPPNAME** (optional) | The names and versions of multiple apps to uninstall, specified in the format `{vendor}.{appname}@{x.x.x}`. |

#### Options

| Option    | Alias | Description                 |
| --------- | ----- | --------------------------- |
| **--yes** | -y    | Answers yes to all prompts. |

#### Examples

```shell
  vtex uninstall
  vtex uninstall vtex.service-example
  vtex uninstall vtex.service-example@0.x
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### unlink

Unlinks an app from the current workspace. If no app is specified, it defaults to the app in the current directory.

#### Usage

```shell
  vtex unlink [APPID] [ITHAPPID]
```

appname Name of the app to unlink.

#### Arguments

| Argument                | Description                                                                                              |
| ----------------------- | -------------------------------------------------------------------------------------------------------- |
| **APPID** (optional)    | The name and version of the app to unlink, specified in the format `{vendor}.{appname}@{x.x.x}`.         |
| **ITHAPPID** (optional) | The names and versions of multiple apps to unlink, specified in the format `{vendor}.{appname}@{x.x.x}`. |

#### Options

| Option    | Alias | Description       |
| --------- | ----- | ----------------- |
| **--all** | -a    | Unlinks all apps. |

#### Examples

```shell
  vtex unlink
  vtex unlink vtex.service-example@0.x
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### update

Updates all installed apps to the latest minor or patch version. Does not upgrade to another major version.

#### Usage

```shell
  vtex update
```

#### Example

```shell
  vtex update
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### whoami

> ℹ️ This command refers to the `@vtex/cli-plugin-whoami` plugin. Access [this link](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-plugins) to learn more about VTEX IO CLI plugins.

Prints details about the current account, workspace, environment, and login information.

#### Usage

```shell
  vtex whoami
```

#### Example

```shell
  vtex whoami
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### workspace abtest finish

> ℹ️ This command refers to the `@vtex/cli-plugin-abtest` plugin. Access [this link](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-plugins) to learn more about VTEX IO CLI plugins.

Stops all A/B tests from running on the current account.

#### Usage

```shell
  vtex workspace abtest finish
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### workspace abtest start

> ℹ️ This command refers to the `@vtex/cli-plugin-abtest` plugin. Access [this link](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-plugins) to learn more about VTEX IO CLI plugins.

Starts a new A/B test on the current workspace.

#### Usage

```shell
  vtex workspace abtest start
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### workspace abtest status

> ℹ️ This command refers to the `@vtex/cli-plugin-abtest` plugin. Access [this link](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-plugins) to learn more about VTEX IO CLI plugins.

Displays the results of active A/B tests.

#### Usage

```shell
  vtex workspace abtest status
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### workspace delete

Deletes one or many workspaces from the current account.

#### Usage

```shell
  vtex workspace delete WORKSPACE1 [ITHWORKSPACE]
```

#### Arguments

| Argument                    | Description                             |
| --------------------------- | --------------------------------------- |
| **WORKSPACE1**              | Name of the workspace to delete.        |
| **ITHWORKSPACE** (optional) | Names of multiple workspaces to delete. |

#### Options

| Option      | Alias | Description                                                |
| ----------- | ----- | ---------------------------------------------------------- |
| **--force** | -f    | Deletes the specified workspace, even if it is being used. |
| **--yes**   | -y    | Answers yes to all prompts.                                |

#### Examples

```shell
  vtex workspace delete workspaceName
  vtex workspace delete workspaceName1 workspaceName2
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### workspace list

Lists all workspaces of the current account.

#### Usage

```shell
  vtex workspace list
```

#### Aliases

```shell
  vtex workspace ls

```

#### Examples

```shell
  vtex workspace list
  vtex workspace ls
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### workspace promote

Promotes the current workspace to the master branch. Only works for production workspaces.

#### Usage

```shell
  vtex workspace promote
```

#### Aliases

```shell
  vtex promote

```

#### Examples

```shell
  vtex workspace promote
  vtex promote
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### workspace reset

Cleans all configurations of the specified workspace and recreates them with the configurations from the master.

#### Usage

```shell
  vtex workspace reset [WORKSPACENAME]
```

#### Arguments

| Argument                     | Description                     |
| ---------------------------- | ------------------------------- |
| **WORKSPACENAME** (optional) | Name of the workspace to reset. |

#### Options

| Option           | Alias | Description                                  |
| ---------------- | ----- | -------------------------------------------- |
| **--production** | -p    | Recreates the workspace as a production one. |
| **--yes**        | -y    | Answers yes to all prompts.                  |

#### Examples

```shell
  vtex workspace reset
  vtex workspace reset workspaceName
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### workspace status

Displays information about the specified workspace.

#### Usage

```shell
  vtex workspace status [WORKSPACENAME]

```

#### Arguments

| Argument                     | Description            |
| ---------------------------- | ---------------------- |
| **WORKSPACENAME** (optional) | Name of the workspace. |

#### Example

```shell
  vtex workspace status
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

### workspace use

Creates and switches to a new workspace or simply switches to an existing one.

#### Usage

```shell
  vtex workspace use WORKSPACE
```

#### Arguments

| Argument      | Description                   |
| ------------- | ----------------------------- |
| **WORKSPACE** | Name of the workspace to use. |

#### Options

| Option           | Alias | Description                                        |
| ---------------- | ----- | -------------------------------------------------- |
| **--production** | -p    | Creates and/or switches to a production workspace. |
| **--reset**      | -r    | Resets the workspace before switching to it.       |

#### Aliases

```shell
  vtex use
```

#### Examples

```shell
  vtex workspace use workspaceName
  vtex use workspaceName
```

<div align="right"> 🔼 <a href="#default-commands">Back</a></div>

## Plugins

Below is a brief description of the commands provided by VTEX plugins. For detailed information about each command, click its respective name. After installing the corresponding plugin, you can also access this information in your terminal by adding `--help` or `-h` after the command name.

> ℹ️ Access [this link](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-plugins) to learn more about VTEX IO CLI plugins.

| Plugin command                            | Feature description                                                                     |
| ----------------------------------------- | --------------------------------------------------------------------------------------- |
| [`add`](#add)                             | Adds the specified app(s) to the manifest dependencies.                                 |
| [`config get`](#-config-get)              | Prints the value of the requested configuration key.                                    |
| [`config reset`](#-config-reset)          | Resets the specified configuration to its default value.                                |
| [`config set`](#-config-set)              | Sets the value of a configuration key.                                                  |
| [`debug dotnet`](#debug-donet)            | Debugs .NET applications (IDEs only).                                                   |
| [`infra install`](#infra-install)         | Installs an infra service.                                                              |
| [`infra list`](#infra-list)               | Lists installed infra services.                                                         |
| [`infra update`](#infra-update)           | Updates all installed infra services.                                                   |
| [`lighthouse audit`](#lighthouse-audit)   | Runs a Lighthouse audit over the specified URL.                                         |
| [`lighthouse show`](#lighthouse-show)     | Shows a previous audit report, filtered by app and/or URL.                              |
| [`logs`](#logs)                           | Shows logs of an app (only apps in production).                                         |
| [`plugins install`](#plugins-install)     | Installs a plugin on CLI.                                                               |
| [`plugins link`](#plugins-link)           | Links a plugin to CLI for development.                                                  |
| [`plugins:list`](#plugins-list)           | Lists all plugins installed on your machine.                                            |
| [`source plugins`](#plugins-source)       | Lists all plugins supported by VTEX.                                                    |
| [`plugins uninstall`](#plugins-uninstall) | Removes a plugin from CLI.                                                              |
| [`plugins:update`](#plugins-update)       | Updates all plugins installed on your machine.                                          |
| [`redirects delete`](#redirects-delete)   | Deletes redirects from the current account and workspace.                               |
| [`redirects export`](#redirects-export)   | Exports all redirects defined in the current account and workspace to a CSV file.       |
| [`redirects import`](#redirects-import)   | Imports redirects from a CSV file to the current account and workspace.                 |
| [`settings get`](#settings-get)           | Prints the settings of the specified app.                                               |
| [`settings set`](#settings-set)           | Sets value to the specified setting of an app.                                          |
| [`settings unset`](#settings-unset)       | Disables the specified setting of an app.                                               |
| [`submit`](#submit)                       | Submits the current app, or a specified one, for validation by the VTEX App Store team. |
| [`support`](#support)                     | Logs in as support to another VTEX account.                                             |
| [`test e2e`](#test-e2e)                   | Runs E2E integration tests for the app in the current directory.                        |
| [`test unit`](#test-unit)                 | Runs unit tests for the app in the current directory.                                   |
| [`url`](#url)                             | Prints the base URL for the current account and workspace.                              |

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### add

Adds the specified app(s) to the manifest dependencies.

#### Usage

```shell
vtex add APPID [ITHAPPID]
```

#### Arguments

| Argument                | Description                                                                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **APPID**               | The name and version of the dependency to include in the manifest.json file, specified in the format `{vendor}.{appname}@{x.x.x}`.          |
| **ITHAPPID** (optional) | The names and versions of multiple dependencies to include in the manifest.json file, specified in the format `{vendor}.{appname}@{x.x.x}`. |

#### Example

```shell
vtex add vtex.service-example@0.x
```

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### autoupdate

Automatically updates VTEX IO CLI.

#### Usage

```shell
  vtex autoupdate [CHANNEL]
```

#### Arguments

| Argument               | Description |
| ---------------------- | ----------- |
| **CHANNEL** (optional) | .           |

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### config get

Prints the value of the requested configuration key.

#### Usage

```shell
vtex config get CONFIGNAME
```

#### Arguments

| Argument       | Description                               |
| -------------- | ----------------------------------------- |
| **CONFIGNAME** | Configuration to retrieve the value from. |

#### Example

```shell
 vtex config get env
 vtex config get cluster
```

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### config reset

Resets the specified configuration to its default value.

#### Usage

```shell
vtex config reset CONFIGNAME
```

#### Arguments

| Argument       | Description                         |
| -------------- | ----------------------------------- |
| **CONFIGNAME** | Name of the configuration to reset. |

#### Example

```shell
 vtex config reset env
 vtex config reset cluster
```

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### config set

Sets the value of a configuration key.

#### Usage

```shell
vtex config set CONFIGNAME VALUE
```

#### Arguments

| Argument       | Description                               |
| -------------- | ----------------------------------------- |
| **CONFIGNAME** | Name of the configuration.                |
| **VALUE**      | New value of the specified configuration. |

#### Example

```shell
  vtex config set env envValue
  vtex config set cluster clusterValue
```

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### debug donet

Debugs .NET applications (IDEs only).

#### Usage

```shell
  vtex debug dotnet DEBUGINST
```

#### Arguments

| Argument      | Description                            |
| ------------- | -------------------------------------- |
| **DEBUGINST** | Name of the .NET application to debug. |

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### infra install

Installs an infra service.

#### Usage

```shell
  vtex infra install SERVICEID
```

#### Arguments

| Argument      | Description                                                                                               |
| ------------- | --------------------------------------------------------------------------------------------------------- |
| **SERVICEID** | The name and version of the service to install, specified in the format `{vendor}.{servicename}@{x.x.x}`. |

#### Examples

```shell
  vtex infra install infra-service
  vtex infra install infra-service@0.0.1
```

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### infra list

Lists installed infra services.

#### Usage

```shell
  vtex infra list [NAME]
```

#### Arguments

| Argument            | Description   |
| ------------------- | ------------- |
| **NAME** (optional) | Service name. |

#### Options

| Option              | Alias | Description                                     |
| ------------------- | ----- | ----------------------------------------------- |
| **--available**     | -a    | Lists services that are available to install.   |
| **--filter=filter** | -f    | Lists services that contain the specified word. |

#### Aliases

```shell
  vtex infra ls
```

#### Examples

```shell
  vtex infra list
  vtex infra ls
```

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### infra update

Updates installed infra services.

#### Usage

```shell
  vtex infra update
```

#### Example

```shell
  vtex infra update
```

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### lighthouse audit

Runs a Lighthouse audit over the specified URL.

#### Usage

```shell
  vtex lighthouse audit URL
```

#### Arguments

| Argument | Description   |
| -------- | ------------- |
| **URL**  | URL to audit. |

#### Options

| Option     | Alias | Description                             |
| ---------- | ----- | --------------------------------------- |
| **--json** | -j    | Returns the report as a JSON on stdout. |

#### Aliases

```shell
  vtex lh audit
```

#### Examples

```shell
  vtex lighthouse audit my.url.com
  vtex lh audit my.url.com
```

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### lighthouse show

Shows a previous audit report, filtering by app and/or URL.

#### Usage

```shell
  vtex lighthouse show
```

#### Options

| Option        | Alias | Description          |
| ------------- | ----- | -------------------- |
| **--app=app** | -a    | Filters by app name. |
| **--url=url** | -u    | Filters by URL.      |

#### Aliases

```shell
  vtex lh show
```

#### Examples

```shell
  vtex lighthouse show --app=vtex.awesome-app
  vtex lighthouse show -u https://awesome.store.com
  vtex lighthouse show -a vtex.awesome-app --url=https://awesome.store.com
  vtex lh show --app=vtex.awesome-app
  vtex lh show -u https://awesome.store.com
  vtex lh show -a vtex.awesome-app --url=https://awesome.store.com
```

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### logs

Shows logs of an app. (Only apps in production.)

#### Usage

```shell
  vtex logs [APP]
```

#### Arguments

| Argument           | Description                   |
| ------------------ | ----------------------------- |
| **APP** (optional) | Name of the app to show logs. |

#### Options

| Option     | Alias | Description                                              |
| ---------- | ----- | -------------------------------------------------------- |
| **--all**  | -a    | Shows logs of all apps installed on the current account. |
| **--past** | -p    | Shows previous logs of the specified app.                |

#### Examples

```shell
  vtex logs
  vtex logs appName
  vtex logs --all
  vtex logs appName --past
```

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### plugins install

Installs a plugin on CLI.

#### Usage

```shell
  vtex plugins install PLUGIN
```

#### Arguments

| Argument   | Description         |
| ---------- | ------------------- |
| **PLUGIN** | Plugins to install. |

#### Options

| Option      | Alias | Description                                                           |
| ----------- | ----- | --------------------------------------------------------------------- |
| **--force** | -f    | Refetches all packages, even the ones that were previously installed. |

#### Aliases

```shell
  vtex plugins:add
```

#### Examples

```shell
  vtex plugins install lighthouse
  vtex plugins install https://github.com/vtex/cli-plugin-someplugin
  vtex plugins install @vtex/cli-plugin-someplugin
```

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### plugins link

Links a plugin to CLI for development.

#### Usage

```shell
  vtex plugins link PLUGIN
```

#### Arguments

| Argument              | Description  |
| --------------------- | ------------ |
| **PATH [default: .]** | Plugin path. |

#### Examples

```shell
   vtex plugins link myplugin
```

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### plugins list

Lists all plugins installed on your machine.

#### Usage

```shell
  vtex plugins:list
```

#### Options

| Option     | Description         |
| ---------- | ------------------- |
| **--core** | Shows core plugins. |

#### Examples

```shell
  vtex plugins list
```

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### plugins source

Lists all plugins supported by VTEX.

#### Usage

```shell
  vtex plugins source PLUGIN
```

#### Arguments

| Argument              | Description  |
| --------------------- | ------------ |
| **PLUGIN**            | Plugin name. |
| **PATH [default: .]** | Plugin path. |

#### Examples

```shell
  vtex plugins source myplugin
```

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### plugins uninstall

Removes a plugin from CLI.

#### Usage

```shell
  vtex plugins uninstall PLUGIN
```

#### Arguments

| Argument   | Description          |
| ---------- | -------------------- |
| **PLUGIN** | Plugin to uninstall. |

#### Aliases

```shell
  vtex plugins unlink
  vtex plugins remove
```

#### Examples

```shell
vtex plugins uninstall lighthouse
vtex plugins remove lighthouse
vtex plugins unlink lighthouse
```

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### plugins update

Updates all plugins installed on your machine.

#### Usage

```shell
  vtex plugins update
```

### redirects delete

Deletes redirects from the current account and workspace.

#### Usage

```shell
  vtex redirects delete CSVPATH
```

#### Arguments

| Argument    | Description                                  |
| ----------- | -------------------------------------------- |
| **CSVPATH** | CSV file containing the URL paths to delete. |

#### Example

```shell
  vtex redirects delete csvPath
```

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### redirects export

Exports all redirects defined in the current account and workspace to a CSV file.

#### Usage

```shell
  vtex redirects export CSVPATH
```

#### Arguments

| Argument    | Description           |
| ----------- | --------------------- |
| **CSVPATH** | Name of the CSV file. |

#### Example

```shell
  vtex redirects export csvPath
```

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### redirects import

Imports redirects from a CSV file to the current account and workspace.

#### Usage

```shell
  vtex redirects import CSVPATH
```

#### Options

| Option      | Alias | Description                               |
| ----------- | ----- | ----------------------------------------- |
| **--reset** | -r    | Removes all previously defined redirects. |

#### Example

```shell
  vtex redirects import csvPath
```

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### settings get

Prints the settings of the specified app.

#### Usage

```shell
  vtex settings get APPNAME [FIELD]
```

#### Arguments

| Argument             | Description                                      |
| -------------------- | ------------------------------------------------ |
| **APNAME**           | Name of the app to check the available settings. |
| **FIELD** (optional) | Name of the setting.                             |

#### Aliases

```shell
  vtex settings
```

#### Example

```shell
  vtex settings get vtex.service-example
```

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### settings set

Sets the value for the specified setting of an app.

#### Usage

```shell
  vtex settings set APPNAME FIELD VALUE 
```

#### Arguments

| Argument    | Description           |
| ----------- | --------------------- |
| **APPNAME** | Name of the app.      |
| **FIELD**   | Name of the setting.  |
| **VALUE**   | Value of the setting. |

#### Example

```shell
  vtex settings set vtex.store enableCriticalCSS true
```

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### settings unset

Disables the specified setting of an app.

#### Usage

```shell
  vtex settings unset APPNAME FIELD
```

#### Arguments

| Argument    | Description          |
| ----------- | -------------------- |
| **APPNAME** | Name of the app.     |
| **FIELD**   | Name of the setting. |

#### Example

```shell
  vtex settings unset vtex.service-example fieldName
```

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### submit

Submits the current app, or a specified one, for validation by the VTEX App Store team.

#### Usage

```shell
  vtex submit [APPID]
```

#### Arguments

| Argument             | Description                      |
| -------------------- | -------------------------------- |
| **APPID** (optional) | The name of the app to validate. |

#### Examples

```shell
  vtex submit
  vtex submit myvendor.myapp@1.2.3
```

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### support

Logs in as support to another VTEX account.

#### Usage

```shell
  vtex support ACCOUNT
```

#### Arguments

| Argument    | Description                          |
| ----------- | ------------------------------------ |
| **ACCOUNT** | Name of the account to give support. |

#### Example

```shell
  vtex support storecomponents
```

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### test e2e

Runs E2E integration tests for the app in the current directory.

#### Usage

```shell
  vtex test e2e
```

#### Options

| Option              | Alias | Description                                                                                                                                                                                                                                                |
| ------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **--report=report** | -r    | Displays the results and status of the specified test ID.                                                                                                                                                                                                  |
| **--token**         | -t    | (Not recommended.) Sends your personal authorization token to your testing session, making it available during the tests. Please note that this action can be potentially dangerous as it exposes your token through the 'authToken' environment variable. |
| **--workspace**     | -w    | Runs tests for the apps installed on the specified workspace.                                                                                                                                                                                              |

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### test unit

Runs unit tests for the app in the current directory.

#### Usage

```shell
  vtex test unit
```

#### Options

| Option       | Alias | Description               |
| ------------ | ----- | ------------------------- |
| **--unsafe** | -u    | Ignores TypeScript errors |

<div align="right"> 🔼 <a href="#plugins">Back</a></div>

### url

Prints the base URL for the current account, workspace, and environment.

#### Usage

```shell
  vtex url
```

#### Example

```shell
  vtex url
```

<div align="right"> 🔼 <a href="#plugins">Back</a></div>
