---
title: "SBD-Impersonation"
slug: "smartinqa-sbd-impersonation"
excerpt: "smartinqa.sbd-impersonation@0.0.0"
hidden: true
createdAt: "2022-07-28T17:29:20.271Z"
updatedAt: "2022-07-28T17:29:20.271Z"
---
This is an app that manages the impersionation processes in **Black&Decker** sites.

## 🚀 Getting Started

These instructions will allow you to get a copy of the project running on your local machine for the purposes of using the authentication apps from the **Black&Decker** store.

### 🔧 Installation

To start the **installation**, you need to **install the app in the vtex store**:

```bash
    vtex install smartinqa.sbd-impersonation
```

### 🏗️ Blocks

#### `select-client-button`
This block contains the "Select Client" button and the "Client List" dropdown.
It doesn't receive any props.

## 📋 Modus Operandi

The default behavior of the app is to manage the impersonation process.

The block "select-client-button" shows a blue button that opens a dropdown list when clicked.
The dropdown list has an input with a magnifying glass on the right side of it and a list of the representative Clients there, unfiltered.
The user can filter by client name in the input.

## 🛠️ Customization

### Clone Project

To customize this app first you need to **clone the project**

```bash
    cd "directory of your choice"
```

SSH clone

```bash
    git clone git@gitlab.com:acct.global/code-witchers/acct.sbd/vtex-io/india/general-apps/sbd-impersonation.git
```

or

clone HTTPS

```bash
    git clone https://gitlab.com/acct.global/code-witchers/acct.sbd/vtex-io/india/general-apps/sbd-impersonation.git
```

### Login in the vtex account

```bash
    vtex login [account-name]
    ex. vtex login smartinqa
```

### Create a workspace

```bash
    vtex use [workspace-name]
    ex. vtex use myworkspace
```

### Link the workspace

```bash
    vtex link
```

### Start your in-store workspace

The server will start in your WS environment just login

```
https://[woskspace-name]--[account-name].myvtex.com
ex. https://myworkspace--smartinqa.myvtex.com
```

## Contributors ✨

Thanks goes to these wonderful people:

- **João Castro** - _Documentation / Developer_ - [João Castro](https://github.com/JooLuiz)
- **Felipe Felix** - _Developer_ - [Felipe Felix](https://gitlab.com/felipe.felix1)
- **Carlos Pellizzari** - _Solutions Architect_ - [Carlos Pellizzari](https://gitlab.com/carlos.pellizzari)

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!