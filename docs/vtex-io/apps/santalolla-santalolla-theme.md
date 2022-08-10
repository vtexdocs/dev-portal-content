---
title: "Table of Contents"
slug: "santalolla-santalolla-theme"
excerpt: "santalolla.santalolla-theme@0.1.90"
hidden: true
createdAt: "2022-07-07T18:29:49.949Z"
updatedAt: "2022-08-09T18:00:26.581Z"
---
- [Table of Contents](#table-of-contents)
- [About <a name = "about"></a>](#about-)
- [Prerequisites](#prerequisites)
- [Getting Started <a name = "getting_started"></a>](#getting-started-)
- [Usage <a name="usage"></a>](#usage-)
- [Deployment <a name = "deployment"></a>](#deployment-)
- [Built Using <a name = "built_using"></a>](#built-using-)
- [Authors <a name = "authors"></a>](#authors-)

## About <a name = "about"></a>

This VTEX IO project was developed to replace the old VTEX CMS project. Most of the code was developed from scratch, but code from the old project still exists.

Maintain project best practices, follow development standards, and try not to break Eslint and Prettier rules

## Prerequisites

Make sure you meet all project requirements before trying to run it

| Package           | Version          |
------------------- | ------------------
|Node.Js            | V.16.14.0        |
|Npm                | V.8.3.1          |
|Vtex Toolbet       | V.3.0.0          |


## Getting Started <a name = "getting_started"></a>

1. Clone this repository to your local development environment

```
$ git clone https://github.com/codeby-global/santalolla.theme-io.git
```

2. Add node packages

```
$ yarn install
```

3. Login to your vtex account:

```
$ vtex login {Account Name (Same as vendor at manifest.json)}
```

4. Change to your workspace

```
$ vtex use {Workspace Name (Any name you like)}
```

5. Link with your workspace

```
$ vtex link
```

## Usage <a name="usage"></a>

Always document your code, explaining what each function accomplishes. Make the next developer's job easier (:

Command to fix prettier:
```
$ yarn format
```

Command to view Eslint:
```
$ yarn lint
```

Command to fix some Eslint:
```
$ yarn lint-fix
```

## Deployment <a name = "deployment"></a>

The husky was configured to not allow commits if the code is not in the Eslint and Prettier standards. Pay attention to scripts to run and fix both (Eslint and Prettier)

Make sure that your updates have been validate by QA TEAM and by customers and follow the next steps:

1. vtex release patch stable
2. vtex use staging -p -r
3. vtex install {vendor}.{name}@{version}
4. Validate if everything is ok at workspace staging
5. vtex promote

## Built Using <a name = "built_using"></a>


## Authors <a name = "authors"></a>

- [@Team CodeBy](https://github.com/codeby-global) - Repository architecture, support and maintenance