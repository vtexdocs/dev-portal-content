---
title: "Session data aggregation: create and transform calls"
slug: "session-data-aggregation-create-and-transform-calls"
hidden: false
createdAt: "2022-08-04T20:56:02.047Z"
updatedAt: "2022-08-04T21:09:23.124Z"
---

Strictly speaking, Session Manager is a backend API system that stores and processes session data in JSON objects. Each VTEX account has settings that indicate which installed apps have a session dependency and how they intend to process this information.

Apps with a session dependency monitor change to their inputs and modify session parameters through their outputs. When a session parameter changes, Session Manager notifies all apps monitoring it and listens to their response, which indicates whether any other parameters must be updated as a result. Session Manager then patches the session data by compiling the responses sent by all apps, if necessary. We refer to this notification / response / update cycle as **transform call** or transform.

Transforms often trigger other transforms, repeating until apps send no further parameter updates. This operation is, naturally, carefully monitored for loop conditions. The diagram below illustrates one such transform cycle:

![Sessions transform diagram, as described in the steps below.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Integration-Guides/session-manager/3442b69-Session_Manager_15.jpg)

1. A change was made to session parameter X
2. App A was monitoring session parameter X, so that triggered Transform 1
3. Transform 1 led App A to change session parameter Y
4. Apps B and C were monitoring session parameter Y, so that triggered Transform 2
5. Transform 2 led App B to change session parameter Z
6. App C was monitoring session parameter Z, so that triggered Transform 3
7. Transform 3 had no side effects on parameters monitored by apps, so the cycle ended, and the session was saved. In the future, other cycles may start if other changes are made.
[block:callout]
{
  "type": "info",
  "body": "Transform calls are made to all apps simultaneously for the sake of performance. That's why App C was affected both by Transform 2 and Transform 3 - it had no way of knowing that the result of Transform 2 on App B would lead to further changes."
}
[/block]
When a new session is created, a simpler version of this cycle is executed, which we call **create call**. All apps that have set their configuration with `RunOnCreate: true` will be notified to run simultaneously with an empty input. If these apps modify any parameters that are monitored by other apps, that triggers a transform cycle that will run until the input dependency is resolved.
