---
title: "Current version 0.0.1 - 18/05/2021"
slug: "segurosexito-server-mascotas-integration"
excerpt: "segurosexito.server-mascotas-integration@0.0.7"
hidden: true
createdAt: "2022-07-19T21:04:43.240Z"
updatedAt: "2022-07-28T17:05:01.609Z"
---
# VTEX IO Service bundle  

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
  "name": "service-example",
  "vendor": "vtex",
  "version": "0.0.1",
  "title": "Service Example",
  "description": "Reference app for VTEX IO Services",
  "mustUpdateAt": "2018-01-04",
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
        "host": "httpstat.us",
        "path": "*"
      }
    },
    {
      "name": "colossus-fire-event"
    },
    {
      "name": "colossus-write-logs"
    }
  ],
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