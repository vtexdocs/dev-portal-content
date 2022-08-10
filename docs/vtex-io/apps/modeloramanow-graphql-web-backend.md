---
title: "graphql-web-backend"
slug: "modeloramanow-graphql-web-backend"
excerpt: "modeloramanow.graphql-web-backend@1.6.0"
hidden: true
createdAt: "2022-07-12T19:20:21.791Z"
updatedAt: "2022-08-08T16:37:56.859Z"
---
## ​

To run this application and test your changes in real time, cloning this repo, open a new terminal on the root folder for the project and run the following commands:
​

```
vtex login <account name>
vtex use <workspace name>
vtex link
```

## Features

- Generate an `appToken` to be used to consume resources from ABI Graphql server

---

## Testing

Currently, this repo doesn't offer unit testing

---

## Dependencies & Versions

​
VTEX handles dependencies through its `manifest.json` file and uses yarn as its dependency manager. Make sure you have both Yarn and `vtex` installed.
​
To install the VTEX CLI use `yarn global add vtex`

## Installation

​
The application is used as dependency for other apps and needs to be declared on manifest.json to be installed.
​

---

## Configuration

### manifest.json

- For security reasons, the endpoint url needs to be included on `outbound-access` on manifest.json file at `root` folder

### VTEX admin

You should configure the following variables in https://{account-name}myvtex.com/admin/apps/modeloramanow.graphql-web-backend@{app-version}/setup/:

- modeloramaGatewayAppKey
- modeloramaGatewayUrl