---
title: "Partytown"
slug: "vtex-partytown"
excerpt: "vtex.partytown@0.0.1-alpha.17"
hidden: true
createdAt: "2022-07-06T17:13:25.848Z"
updatedAt: "2022-07-07T06:42:46.003Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

Partytown is app to manage your third party scripts.

> ℹ️ **Partytown is currently in Alpha**. Which means it's still not a final version and may have flaws. We recommend always testing all scripts while implementing this guide.

## Usage
### Installing partytown

Install the `vtex.partytown` on your new workspace by running `vtex install vtex.partytown@0.0.1-alpha.17`

### Migrating your pixel app to the partytown format

1. Open the `pixel/head.html` file

2. Add the `type="text/partytown"` attribute to each individual `<script>` tag
```diff
- <script>...</script>
+ <script type="text/partytown">...</script>
```

3. (Optional) If you want to access some global variables added to the `window` by the pixel apps, you need to declare it. Go to the `https://{{myworkspace}}--{{myaccount}}.myvtex.com/admin/apps` URL, select the `partytown` app and then add the name of the variables you want to access in the `Forward` field.

![image](https://user-images.githubusercontent.com/40380674/169821502-4148db94-4a1a-493f-95ee-aaf5e243ebec.png)

## Development

Modify the `src/head.html` file and run the `yar run build` command.

<!-- TODO: Documentation -->