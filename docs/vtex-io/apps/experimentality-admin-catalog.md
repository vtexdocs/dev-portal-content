---
title: "Current version 0.0.1 - 17/09/2021"
slug: "experimentality-admin-catalog"
excerpt: "experimentality.admin-catalog@0.1.1"
hidden: true
createdAt: "2022-07-07T02:57:01.602Z"
updatedAt: "2022-07-07T02:57:01.602Z"
---
# VTEX IO Catalog Integration

### Catalog Integration
Link to install: 
````
https://{account}.myvtex.com/admin/apps/experimentality.admin-catalog@0.1.1/install
````
## Introduction 

We use [**KoaJS**](https://koajs.com/) as the web framework, so you might want to get into that
We also use the [**node-vtex-api**](https://github.com/vtex/node-vtex-api), a VTEX set of utilities for Node services. You can import this package using NPM from `@vtex/api` (already imported on this project)
 
- Start from `node/index.ts` and follow the comments and imports :)

Example of service done in VTEX IO with the basic configurations to start the development of a new service, it has several pre-configured clients

## Code Samples

It is necessary to configure some things depending on the environment in which you want to develop:

### Quality Assurance Environment And Production Enviroment

You need to configure the credentials of the clients to QA (API_KEYS, API_TOKENS, KEYS... ) into admin from QA.

 > manifest.json
```
{
  "name": "admin-catalog",
  "vendor": "experimentality",
  "version": "0.0.1",
  "title": "Catalog Categories Integration",
  "description": "Application that allows the creation of categories in the category tree through an .xlsx document. To use it it is necessary to have permissions in VTEX",
  "mustUpdateAt": "2021-09-17",
  "categories": [],
  "dependencies": {
    "vtex.styleguide": "9.x"
  },
  "builders": {
    "node": "6.x",
    "react": "3.x",
    "admin": "0.x",
    "messages": "1.x",
    "docs": "0.x"
  },
  "credentialType": "absolute",
  "billingOptions": {
    "termsURL": "https://compliance.vtex.com/gdpr/policies/vtex-privacy-policy",
    "support": {
      "url": "https://support.vtex.com/hc/requests"
    },
    "free": true,
    "type": "free",
    "availableCountries": [
      "*"
    ]
  },
  "policies": [
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
      "VTEX_API_KEY": {
        "title": "VTEX APP KEY",
        "type": "string",
        "description": "Enter X-VTEX-API-AppKey as key. The value of this header must be the appKey created in VTEX admin."
      },
      "VTEX_API_TOKEN": {
        "title": "VTEX APP TOKEN",
        "type": "string",
        "description": "Enter X-VTEX-API-AppToken as key. The value of this header must be the appToken created in VTEX admin."
      }
    }
  },
  "$schema": "https://raw.githubusercontent.com/vtex/node-vtex-api/master/gen/manifest.schema"
}

```


## Installation

> Depending on the environment, the manifest.json and the credentials of the clients must be configured, in addition to being logged into production or QA as the case may be (that is, QA for tests and prod with to publish to production).

# Installation:

- vtex login (enviroment)
- vtex use (workspace)  or  vtex workspace create (new workspace name)
- vtex link


# Deploy:

The deployment is done to the Osterco environment, be careful and verify the corresponding manifest.json and that the credentials are correct.

- vtex publish

# Annexed

If you do not have the API_KEIS, API_TOKENS or ACCESS KEYS, contact the area in charge to obtain new ones.

## Changelog

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

# Logs

logger.warn('Warning the world!')
logger.error('Error!!!')  
logger.debug('Verbose debug message!')

# Execute logs

vtex logs --all