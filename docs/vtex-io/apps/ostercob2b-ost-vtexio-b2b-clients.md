---
title: "Current version 0.6.3 - 08/07/2021"
slug: "ostercob2b-ost-vtexio-b2b-clients"
excerpt: "ostercob2b.ost-vtexio-b2b-clients@0.1.4"
hidden: true
createdAt: "2022-07-11T21:16:04.493Z"
updatedAt: "2022-07-11T21:59:50.070Z"
---
# VTEX IO Service bundle  

## Introduction

We use [**KoaJS**](https://koajs.com/) as the web framework, so you might want to get into that
We also use the [**node-vtex-api**](https://github.com/vtex/node-vtex-api), a VTEX set of utilities for Node services. You can import this package using NPM from `@vtex/api` (already imported on this project)

- Start from `node/index.ts` and follow the comments and imports :)

Service package made in VTEX IO that allows managing new users, user approval flow, PQRS, quotes, campaigns and shipment traceability.

## Code Samples

It is necessary to configure some things depending on the environment in which you want to develop:

### Quality Assurance Environment And Production Enviroment

You need to  configure the credentials of the clients to QA (API_KEYS, API_TOKENS, KEYS... ) into admin from QA.

 > manifest.json
```
{
  "name": "pqrs",
  "vendor": "osterco",
  "version": "0.6.0",
  "title": "PQRS app for Óster",
  "description": "",
  "mustUpdateAt": "2021-04-21",
  "categories": [],
  "dependencies": {},
  "builders": {
    "node": "6.x",
    "docs": "0.x"
  },
  "scripts": {
    "prereleasy": "bash lint.sh"
  },
  "credentialType": "absolute",
  "policies": [
    {
      "name": "outbound-access",
      "attrs": {
        "host": "ostercob2b.vtexcommercestable.com.br",
        "path": "*"
      }
    },
    {
      "name": "outbound-access",
      "attrs": {
        "host": "{{account}}.vtexcommercestable.com.br",
        "path": "*"
      }
    },
    {
      "name": "outbound-access",
      "attrs": {
        "host": "api.vtex.com",
        "path": "*"
      }
    },
    {
      "name": "outbound-access",
      "attrs": {
        "host": "clientes.tcc.com.co",
        "path": "/servicios/informacionremesas.asmx?WSDL"
      }
    },
    {
      "name": "outbound-access",
      "attrs": {
        "host": "uat.apigw.newellbrands.com",
        "path": "*"
      }
    },
    {
      "name": "outbound-access",
      "attrs": {
        "host": "apigw.newellbrands.com",
        "path": "*"
      }
    },
    {
      "name": "colossus-fire-event"
    },
    {
      "name": "colossus-write-logs"
    },
    {
      "name": "update-app-settings"
    }
  ],
  "settingsSchema": {
    "title": "App keys",
    "type": "object",
    "properties": {
      "vtexAppKey": {
        "title": "VTEX App Key",
        "type": "string"
      },
      "vtexAppToken": {
        "title": "VTEX App Token",
        "type": "string"
      },
      "endpoint": {
        "title": "endPoint",
        "type": "string"
      }
    }
  },
  "$schema": "https://raw.githubusercontent.com/vtex/node-vtex-api/master/gen/manifest.schema"
}
```


## Installation

> Depending on the environment, the manifest.json and the credentials of the clients must be configured, in addition to being logged into osterco or ostercoqa as the case may be (that is, ostercoqa for tests and oster with to publish to production).

# Installation:

- vtex login (enviroment)
- vtex use (workspace)  or  vtex workspace create (new workspace name)
- vtex link


# Deploy:

The deployment is done to the Osterco environment, be careful and verify the corresponding manifest.json and that the credentials are correct.

- vtex publish

# Annexed

If you do not have the API_KEIS, API_TOKENS or ACCESS KEYS, contact the area in charge to obtain new ones.

# Usage
To use this module, your commit messages have to be in this format:

type(category): description [flags]

Where type is one of the following:
- breaking
- build
- ci
- chore
- docs
- feat
- fix
- other
- perf
- refactor
- revert
- style
- test

Where flags is an optional comma-separated list of one or more of the following (must be surrounded in square brackets):

breaking: alters type to be a breaking change
And category can be anything of your choice. If you use a type not found in the list (but it still follows the same format of the message), it'll be grouped under other.