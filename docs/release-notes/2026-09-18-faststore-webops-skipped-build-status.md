---
title: "FastStore WebOps: Skipped status for superseded builds"
slug: "2026-09-18-faststore-webops-skipped-build-status"
type: "improved"
createdAt: "2026-09-18T00:00:00.000Z"
updatedAt: "2026-09-18T00:00:00.000Z"
excerpt: "WebOps now marks superseded queued deploys as Skipped, so builds that would be immediately replaced by a newer commit on the same branch are no longer executed."
tags:
    - FastStore
    - WebOps
---

[FastStore WebOps](https://developers.vtex.com/docs/guides/faststore/webops-dashboard) now avoids building commits that would be immediately replaced by a newer one. When multiple commits are pushed to the same branch while a build is already running, only the most recent queued commit is built next, and older queued commits are marked **Skipped**.

## What has changed?

Previously, every commit pushed to a branch eventually triggered its own build, even if a newer commit had already been pushed to the same branch before that build started.

Now, WebOps runs only one build at a time per branch. Consider the following scenario:

1. Deploy `A` arrives while nothing is running, so it starts immediately (**In progress**).
2. Deploy `B` arrives while `A` is still running, so it becomes **Queued**.
3. Deploy `C` arrives while `A` is still running. `B` becomes **Skipped**, and `C` becomes **Queued** instead.
4. `A` finishes, and `C` starts. `B` is never built, since `C` would have replaced it anyway.

A deploy already **In progress** is never interrupted; only deploys still **Queued** for that branch can become **Skipped**.

For more information, see [Skipped deploys](https://developers.vtex.com/docs/guides/faststore/webops-dashboard#skipped-deploys) in the FastStore WebOps - Dashboard guide.

## Why did we make this change?

Teams that push multiple commits in quick succession to the same branch no longer wait for builds that would be discarded as soon as they finished. This reduces unnecessary build time and keeps the Deploys list focused on the builds that actually reach production or preview.

## What needs to be done?

This behavior is automatic and requires no configuration.

> ℹ️ A deploy marked **Skipped** isn't an error and doesn't require any action.
