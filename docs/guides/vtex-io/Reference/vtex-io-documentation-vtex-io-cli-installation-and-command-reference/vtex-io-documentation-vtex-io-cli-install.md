---
title: "Installing VTEX IO CLI"
slug: "vtex-io-documentation-vtex-io-cli-install"
hidden: false
createdAt: "2021-04-04t22:02:14.003z"
updatedAt: "2022-12-13T20:17:44.621Z"
---

According to your operating system, follow the respective steps to install VTEX IO CLI on your computer.

## MacOS

- **Brew**

  > ⚠️ For computers running on an Apple M1 chip, before installing VTEX IO CLI, install [Rosetta](https://support.apple.com/en-us/HT211861) and enable your computer to use the command-line interface for a Mac with an Intel processor.  To install Rosetta, run the following in your terminal: `/usr/sbin/softwareupdate --install-rosetta --agree-to-license`.


  1. Install Xcode by running the following command.
 
  ```sh
  xcode-select --install
  ```
  
  2. Install **Homebrew** by following the instructions on the [**Homebrew website**](https://brew.sh/index).

  ![brew](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-vtex-io-cli-install-0.png)

  3. Then, install **VTEX IO CLI** by running the following command.

  ```sh
  brew tap vtex/vtex
  brew install vtex
  ```

## Linux

- **Tarball**

  > ⚠️ Before the installation, check if you have the [curl](https://curl.se/) command-line tool and library installed on your computer.

  Open the terminal and run the following command to install VTEX IO CLI.

  ```sh
  curl -L https://vtex.io/vtexcli/install | sh
  ```

## Windows

- **Installer for Windows**

1. Download the appropriate installer for your Windows system ([64-bit installer](https://vtex.io/vtexcli/install/win-x64); [32-bit installer](https://vtex.io/vtexcli/install/win-x32)).
2. Open the downloaded file and follow the instructions to finish the installation process.
3. Run the Windows Terminal with elevated administrator permission by right-clicking the Windows Terminal icon and selecting "Run as administrator."
4. Run the following command to finish the installation.

  ```sh
  vtex
  ```

  After following the steps, this message will appear.

  ![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-vtex-io-cli-install-1.png)

  You don't have to be in your admin role for the next step.

## Installing CLI via NPM

Since VTEX IO CLI is built with [Node.js](https://nodejs.org/en/), you can manually install it via [npm](https://www.npmjs.com/package/vtex). This method is recommended only for environments where auto-updating VTEX IO CLI is not ideal.

> ❗️ We highly recommend using an alternative installation method. If you opt to use npm to install the VTEX IO CLI, remember that CLI won't be automatically updated, and the Node version on your computer might conflict with the one used by CLI developers. If you opt for any other installation method, VTEX IO CLI will always be up-to-date, and you will avoid installation issues.

<details>
  <summary><span class="fa fa-apple">&nbsp;</span>MacOS</summary>

  <br>

  1. Install **Homebrew** by following the instructions on the [**Homebrew website**](https://brew.sh/index).

  ![brew](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-vtex-io-cli-install-2.png)

  2. Install **Node.js** via Homebrew by running the following command.

  ```sh
  brew install node
  ```

  3. Then, install **Yarn**.

  ```sh
  brew install yarn
  ```

4. Finally, install **VTEX IO CLI**.

  ```sh
  yarn global add vtex
  ```

<br>
</details>

<details>
  <summary><span class="fa fa-linux">&nbsp;</span>Linux</summary>

<br>

  1. Install **Node.js** by running the following command.

  ```sh
  sudo apt install nodejs
  ```

  2. Install **Yarn** by following the [Yarn installation](https://classic.yarnpkg.com/en/docs/install#gentoo-stable) for Linux.
  3. Install **VTEX IO CLI** by running the following command.

  ```sh
  sudo yarn global add vtex
  ```

<br>
</details>

<details>
  <summary><span class="fa fa-windows">&nbsp;</span>Windows</summary>

<br>

  1. Download and install [**Node.js**](https://nodejs.org/pt-br/download/).
  2. Download and install [**Yarn**](https://classic.yarnpkg.com/en/docs/getting-started).
  3. Run the Windows Terminal with elevated administrator permission by right-clicking the Windows Terminal icon and selecting "Run as administrator."
  4. Install **VTEX IO CLI** by running the following command.

  ```sh
  yarn global add vtex
  ```

  5. Run the following command to finish the installation.

  ```sh
  vtex
  ```

  After following the steps, this message will appear.

  ![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-vtex-io-cli-install-3.png)

  You don't have to be in your admin role for the next step.

<br>
</details>

## Verifying the installation

To confirm that the installation went as expected, run the following command to check all default commands available in VTEX IO CLI.

```sh
vtex
```

![vtex](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-vtex-io-cli-install-4.png)

### Troubleshooting

If VTEX IO CLI is not behaving as expected, run `vtex --version` to make sure you're using the [latest version](https://github.com/vtex/toolbelt/blob/3.x/CHANGELOG.md) available. If not, consider [updating](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-update) it.

If the problem persists, please check the following instructions.

<details>
  <summary><code>Error: Cannot find 'vtex' module</code></summary>

  <br>

This error is related to [plugins](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-plugins) detached from the VTEX IO CLI base code.

Even though plugins are decoupled from VTEX IO CLI, they rely on the CLI features. Therefore, this error indicates that these plugins are failing to access VTEX IO CLI features.

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

If the error persists, [open a support ticket](https://help-tickets.vtex.com/smartlink/sso/login/zendesk).

<br>
</details>
