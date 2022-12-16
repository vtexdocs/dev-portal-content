---
title: "Installing the VTEX IO CLI"
slug: "vtex-io-documentation-vtex-io-cli-install"
excerpt: "vtex.io-documentation@0.88.5"
hidden: false
createdAt: "2021-04-04T22:02:14.003Z"
updatedAt: "2022-08-02T00:03:06.608Z"
---

According to your operating system, take the respective steps to install VTEX IO’s CLI on your machine.

<details>
  <summary><span class="fa fa-apple">&nbsp;</span>MacOS</summary>

- **Brew**

  > ⚠️ Warning
  >
  > For machines running on Apple M1 chip, before installing VTEX IO CLI, install [Rosetta](https://support.apple.com/en-us/HT211861) and enable the machine to use the command-line interface for a Mac with an Intel processor.  To install Rosetta, run the following in your terminal: `/usr/sbin/softwareupdate --install-rosetta --agree-to-license`.
  
  1. Install **Homebrew** by following the instructions on [**Homebrew website**](https://brew.sh/index).

  ![brew](https://files.readme.io/7a812a5-Screen_Shot_2021-04-20_at_19.49.25.png)

  2. Then, install **VTEX IO'S CLI** by running the following command.

  ```sh
  brew tap vtex/vtex
  brew install vtex
  ```

</details>

<details>
  <summary><span class="fa fa-linux">&nbsp;</span>Linux</summary>
<br>

- **Tarball**
  
  >⚠️ Caution
  >
  > Before the installation, check if you have the [curl](https://curl.se/) command-line tool and library installed on your machine.

  Open the terminal and run the following command to install the VTEX IO CLI.

  ```sh
  curl -L https://vtex.io/vtexcli/install | sh
  ```

</details>

<details>
  <summary><span class="fa fa-windows">&nbsp;</span>Windows</summary>

- **Installer for Windows**
  
1. Download the appropriate installer for your Windows system ([64-bit installer](https://vtex.io/vtexcli/install/win-x64); [32-bit installer](https://vtex.io/vtexcli/install/win-x32)).
2. Open the downloaded file and follow the instructions to finish the installation process.

</details>

## Installing the CLI via NPM

Since VTEX IO's CLI is built with [Node.js](https://nodejs.org/en/), you can manually install it via [npm](https://www.npmjs.com/package/vtex). This method is recommended only for environments in which auto-updating VTEX IO's CLI is not ideal.

>❗️Danger
>
> We strongly recommend using an alternative installation method. If you opt to use npm to install the VTEX IO CLI, keep in mind that the CLI won't be automatically updated, and the Node version on your machine might conflict with the one used by the CLI developers. Preferably, if you opt for any other installation method, VTEX IO's CLI will always be up-to-date, and you will avoid installation issues.

<details>
  <summary><span class="fa fa-apple">&nbsp;</span>MacOS</summary>

  1. Install **Homebrew** by following the instructions on [**Homebrew website**](https://brew.sh/index).

  ![brew](https://files.readme.io/7a812a5-Screen_Shot_2021-04-20_at_19.49.25.png)

  2. Install **Node.js** via Homebrew by running the following command.

  ```sh
  brew install node
  ```

  3. Then, install **Yarn**.
  
  ```sh
  brew install yarn
  ```

  4. Finally, install the **VTEX IO CLI**.

  ```sh
  yarn global add vtex
  ```
  
</details>

<details>
  <summary><span class="fa fa-linux">&nbsp;</span>Linux</summary>

  1. Install **Node.js** by running the following command.

  ```sh
  sudo apt install nodejs
  ```

  2. Install **Yarn** by following the [Yarn installation](https://classic.yarnpkg.com/en/docs/install#gentoo-stable) for Linux.
  3. Install the **VTEX IO CLI** by running the following command.

  ```sh
  sudo yarn global add vtex
  ```

</details>

<details>
  <summary><span class="fa fa-windows">&nbsp;</span>Windows</summary>

  1. Download and install [**Node.js**](https://nodejs.org/pt-br/download/).
  2. Download and install [**Yarn**](https://classic.yarnpkg.com/en/docs/getting-started).
  3. Open the terminal.
  4. Install the **VTEX IO CLI** by running the following command.

  ```sh
  yarn global add vtex
  ```

</details>

## Verifying the installation

To confirm that the installation occurred as expected, run the following command to check all default commands available in VTEX IO's CLI.

```sh
vtex
```

![vtex](https://raw.githubusercontent.com/vtex-apps/io-documentation/master/docs/en/Recipes/development/Media/vtex-command.png)

### Troubleshooting

If VTEX IO's CLI is not behaving as expected, run `vtex --version` to make sure you're using the [latest version](https://github.com/vtex/toolbelt/blob/3.x/CHANGELOG.md) available. If not, consider [updating](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-update) it.

If the problem persists, check the following instructions.

<details>
  <summary><code>Error: Cannot find module 'vtex'</code></summary>

This error is related to [plugins](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-vtex-io-cli-plugins) detached from the VTEX IO's CLI base code.

Even though plugins are decoupled from VTEX IO's CLI, they rely on the CLI functionalities. Therefore, this error signalizes that these plugins are failing to access VTEX IO's CLI functionalities.

To solve this problem, you will need to create a [symlink](https://en.wikipedia.org/wiki/Symbolic_link) from `{vtex-folder}/node_modules/vtex` to `{vtex-folder}/`.

According to your operating system, run the following command in the terminal to create a symlink:

- <span class="fa fa-apple">&nbsp;</span> MacOS

  ```sh
  ln -s /usr/local/Cellar/vtex/2.119.2/libexec /usr/local/Cellar/vtex/2.119.2/libexec/node_modules/vtex
  ```

- <span class="fa fa-linux">&nbsp;</span>Linux
  
  ```sh
  ln -s /usr/local/lib/vtex /usr/local/lib/vtex/node_modules/vtex
  ```

If the error persists, don't hesitate to [open a support ticket](https://help-tickets.vtex.com/smartlink/sso/login/zendesk).

</details>
