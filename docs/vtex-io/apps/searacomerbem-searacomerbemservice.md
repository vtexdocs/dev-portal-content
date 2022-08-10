---
title: "Service Worker Example"
slug: "searacomerbem-searacomerbemservice"
excerpt: "searacomerbem.searacomerbemservice@2.0.1"
hidden: true
createdAt: "2022-08-01T17:24:07.391Z"
updatedAt: "2022-08-02T17:39:00.677Z"
---
Service Workers (SWs) are a poweful tool to handle network requests separate from a web page, as scripts running in the background. They are well known to handle push notifications and background syncronization.

With `service-worker` builder, we can allow an app to expose its own implementation of a Service Worker, enabling VTEX stores to use such Service Worker into their scope.

Service Workers allow us to introduce 6 different event handlers, which can be implemented inside the `service-workers/` folder:

1. [activate](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerGlobalScope/activate_event) → `activate.js`
2. [fetch](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerGlobalScope/onfetch) → `fetch.js`
3. [install](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerGlobalScope/install_event) → `install.js`
4. [message](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerGlobalScope/message_event) → `message.js`
5. [push](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerGlobalScope/push_event) → `push.js`
6. [sync](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerGlobalScope/onsync) → `sync.js`

Whatever is outside those 6 files, should be implemented in `header.js`. The implementation result in the VTEX store DevTools should be as follows:

![image](https://user-images.githubusercontent.com/21017429/114235943-84d14600-9946-11eb-8e1a-4a8f19d3d3d8.png)


Each function can be tested according to the behavior of each event handler. When triggering such event handler, the function body will be executed as follows:

![image](https://user-images.githubusercontent.com/21017429/114235975-8e5aae00-9946-11eb-91f8-b1d7f6d92485.png)


An example is provided in this app for exploration purposes.