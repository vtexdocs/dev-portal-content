---
title: "SBD Authentication"
slug: "smartinqa-sbd-auth"
excerpt: "smartinqa.sbd-auth@0.0.0"
hidden: true
createdAt: "2022-07-28T17:25:32.241Z"
updatedAt: "2022-07-28T17:25:32.241Z"
---
This repository contains app for store authentication **Black&Dacker**

## 🚀 Getting Started

These instructions will allow you to get a copy of the project running on your local machine for the purposes of using the authentication apps from the **Black&Dacker** store.

## 📋 Prerequisites

When linking the sbd-auth app in the store, there is an order to link each app and this order must be respected to avoid possible conflicts.

1.  sbd-auth
2.  store-theme-general

## 🔧 Installation

To start the installation, you need to clone the GitLab project to a directory of your choice:

```
 cd "directory of your choice"
```

SSH clone

```
 git clone git@gitlab.com:acct.global/code-witchers/acct.sbd/vtex-io/india/general-apps/sbd-auth.git
```

or

clone HTTPS

```
  git clone https://gitlab.com/acct.global/code-witchers/acct.sbd/vtex-io/india/general-apps/sbd-auth.git
```

Once the clone is done, now let's login, create the workspace and put it to run in the store.
Tip whenever you login, always check the 'manifest.json' file to get the store name correctly.

### Login and access to the store

Access the project folder in terminal / cmd

```
  cd "saved directory"
  vtex login smartinqa
```

### Check VTEX account and workspace

To verify the VTEX account and workspace in use, simply type

```
  vtex whoami
```

### Creating your shop workspace

```
  vtex use 'smvi000'
  (by default, we use jira task number smvi000 without spaces and hyphen).
```

### Link your in-store workspace

```
  vtex link smvi000
  (which would be your ws id)
```

### Start your in-store workspace

The server will start in your WS environment just login

```
https://smvi000--smartinqa.myvtex.com
```

## 🛠️ Built with

Mention the tools you used to create your project

- [Node](https://nodejs.org/en/docs/)
- [Typescript](https://www.typescriptlang.org/docs/)

## 📌 Version

We use [SemVer](http://semver.org/) for version control. For available versions, note the [tags in this repository](https://github.com/your/tags/do/project).

## ✒️ Authors

Mention all those who helped lift the project from its inception

- **João Castro** - _Developer_ - [João Castro](https://gitlab.com/@joo.castro)
- **Felipe Felix** - _Documentation / \_Developer_ - [Felipe Felix](https://gitlab.com/felipe.felix1)

---

⌨️ By [Felipe Felix](https://gitlab.com/felipe.felix1) 😊