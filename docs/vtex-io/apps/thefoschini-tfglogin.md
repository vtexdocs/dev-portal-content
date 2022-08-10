---
title: "Mobile Auth Service"
slug: "thefoschini-tfglogin"
excerpt: "thefoschini.tfglogin@0.0.23"
hidden: true
createdAt: "2022-07-05T13:03:29.419Z"
updatedAt: "2022-07-14T07:50:07.627Z"
---
This service for mobile app to redirect the user back into the app after authentication. This service will have the same domain as the VTEX store - which will pass the first security check on the callbackURL on /startLogin.

The Service app name is `tfglogin`. This name had to be whitelisted on VTEX before we could deploy into any workspace. 

Use this guide as a reference →  

## Install the VTEX CLI

https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-installation-and-command-reference


#### Routes
- /status
- /mobileAuth
- BaseUrl - `https://{workspace}--thefoschini.myvtex.com/_v/`

Testing workspace - `testing`


Note:: When deployed to prod the `{workspace}--` part of the url falls away.

The mobile app will use the above URL as the callbackURL when calling /startlogin when starting the login flow.
The provided endpoint will receive a GET request with headers from the authentication flow. Then this request will be handled through the following steps: 

1. Extract the following paramaters from the “set-cookie” or "cookie" headers
    ```
      VtexIdclientAutCookie_thefoschini
      vid_rt
      VtexIdclientAutCookie_ca638f38-ed20-42e4-97fe-8a3a3b0a683c
    ```
2. Construct a redirectUrl by injecting the headers extracted above
  `com.tfglabs.manhattan.app.dev://auth?VtexIdclientAutCookie_thefoschini={value}&vid_rt={value}&VtexIdclientAutCookie_ca638f38-ed20-42e4-97fe-8a3a3b0a683c={value}`
3. Do a 302 edirect to the url constructed above