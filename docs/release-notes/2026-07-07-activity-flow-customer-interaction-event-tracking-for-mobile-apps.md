---
title: "Activity Flow: Customer interaction event tracking for mobile apps"
slug: "2026-07-07-activity-flow-customer-interaction-event-tracking-for-mobile-apps"
type: "added"
excerpt: "The Activity Flow SDK for React Native and Flutter now tracks click, view, and impression events."
createdAt: "2026-07-07T00:00:00.000Z"
tags:
  - Activity Flow
---

The [Activity Flow](https://developers.vtex.com/docs/guides/activity-flow) SDK for mobile now supports customer interaction event tracking (click, view, and impression) in React Native and Flutter apps. This aligns the mobile SDKs with the web script, so you can measure the full engagement funnel (rendered → seen → clicked) for any component in your app, not just page views and ad events.

## What has changed?

Previously, mobile apps supported only page views and ad events. Customer interaction tracking was available on the web via the Activity Flow script.

Now, React Native and Flutter apps support click, view, and impression tracking.

### React Native

- **Click tracking:** Use the new `useClickObserver` hook to capture tap interactions. It returns an `afHandlePress` callback to call in your press handler.
- **View tracking:** Use the new `useViewObserver` hook to detect when a component is at least 50% visible for 1 second. It returns an `afViewRef` that can be attached to the target view.
- **Impression tracking:** Use the new `useImpressionObserver` hook to record when a component is rendered, regardless of viewport visibility. It re-fires only when the tracked attributes change.

### Flutter

- **Click tracking:** Use the new `addClickListener` extension method on any widget to capture tap interactions.
- **View tracking:** Use the new `addViewListener` extension method to fire a view event when the widget is at least 50% visible for 1 second (per IAB standards). It fires once per app session.
- **Impression tracking:** Use the new `addImpressionListener` extension method to record when a widget is built and rendered in the widget tree.

## What needs to be done?

To implement interaction event tracking in your app, see the related guides:

- [Installing Activity Flow in React Native apps](https://developers.vtex.com/docs/guides/installing-activity-flow-in-react-native-apps)
- [Installing Activity Flow in Flutter apps](https://developers.vtex.com/docs/guides/installing-activity-flow-in-flutter-apps)
