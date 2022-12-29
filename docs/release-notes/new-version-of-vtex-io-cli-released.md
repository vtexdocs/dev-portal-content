---
slug: "new-version-of-vtex-io-cli-released"
title: "New version of VTEX IO CLI available"
createdAt: 2021-10-20T12:51:00.000Z
hidden: false
type: "improved"
---

![App Development](https://img.shields.io/badge/-App%20Development-blue)

[block:html]
{
  "html": "<div class=\"badge\" id=\"vtex-io\">VTEX IO</div>\n</br>"
}
[/block]
[VTEX IO CLI](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-installation-and-command-reference) has changed its version 3 to enhance developers' productivity and experience. To allow this evolution, we adapted VTEX IO CLI to a plugin-based architecture, added a new color scheme, and included a more comprehensive command description. Also, VTEX IO CLI is now available on multiple platforms.
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/release-notes/5e85742-vtex-plugins_15.png)

## What has changed?

Unlike previous versions, VTEX IO CLI now has a **plugin-based architecture** that makes it more flexible and extensible to **inject new commands and functionalities.** Now, you can go beyond VTEX IO's CLI default commands and achieve a more comprehensive experience by adding specific plugins. We also updated the CLI with a **complete command reference, a new color scheme, and more informative messages.**

Likewise, it is important to highlight that VTEX IO CLI used to be available only from npm and is now available on **multiple platforms.**

- NPM
- AWS-S3 (Windows, Linux, Mac)
- Homebrew (Mac)
[block:callout]
{
  "type": "warning",
  "body": "**Attention:** Some commands from previous versions of VTEX IO's CLI were detached from its base code and are now available as plugins: `add`, `config`, `debug`, `infra`, `lighthouse`, `logs`, `redirects`, `settings`, `submit`, `support`, `test`, `url`. Hence, you may need to install them manually. For more information, check out our documentation on Managing plugins."
}
[/block]

## Why did we make this change?

These changes aim to enhance developers' productivity by providing faster performance, a user-friendly interface, more transparency on what each command executes, and more visibility over interactions.

## What needs to be done?

You can start using VTEX IO CLI straight away. To update the CLI, run the following command:

```sh
yarn global add vtex
```

For more information, check out the [VTEX IO CLI documentation](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-installation-and-command-reference).
