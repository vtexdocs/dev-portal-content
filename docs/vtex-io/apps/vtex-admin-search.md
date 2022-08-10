---
title: "Admin Search"
slug: "vtex-admin-search"
excerpt: "vtex.admin-search@1.62.0"
hidden: true
createdAt: "2022-07-06T04:15:18.056Z"
updatedAt: "2022-08-04T13:30:58.412Z"
---
Admin Search is the app used to configure the [vtex-search](https://github.com/vtex-apps/search) app.


## Table of Contents

- [Installation](#installation)
- [Git Secret](#git-secret)
- [Usage](#usage)
    - [Integration Settings](#integration-settings)

## Installation

`vtex install vtex.admin-search@1.x`

## Git Secret

This repository uses [git secret](#https://git-secret.io/).
To get access to the encrypted code:

1. Generate a gpg key: `gpg --gen-key`
2. Get your public key : `gpg --armor --export you@example.com > mykey.asc`
3. Send your key to an admin

## Usage

### Integration Settings

The search integration needs to authenticate through `appKey` and `appToken`. This screen allows the user to inform these tokens.

### Reports

The search reports. Informations like sales and searches

### Synonyms

Create word synonyms in search