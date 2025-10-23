---
title: "Installing Activity Flow in Flutter apps"
slug: "installing-activity-flow-in-flutter-apps"
hidden: false
createdAt: "2025-10-23T17:07:05.899Z"
---

This guide explains how to install and configure the VTEX Activity Flow SDK in Flutter apps for Android and iOS.

## Before you begin

### Install the Activity Flow package

The Activity Flow SDK captures user navigation and sends events from your mobile app. To install the package, run the following command in your project directory:

```bash
flutter pub add activity_flow
```

This installs the SDK and updates your `pubspec.yaml` file with the `activity_flow` dependency.

## Instructions

### Step 1 – Importing the Activity Flow package

In your app's main file, import the Activity Flow package as follows:

```javascript
import 'package:activity_flow/activity_flow.dart';
```

### Step 2 – Creating an Activity Flow instance

Set the account name to create an instance of the main package class:

```java
void main() {
runApp(const MyApp());
}

class App extends StatelessWidget {

  Widget build(BuildContext context) {

// Call activity flow here
    initActivityFlow(accountName: appAccountName);
...

}
```

### Step 3 – Tracking page views automatically

To automatically track user navigation between app pages, add the `PageViewObserver` to the `navigatorObservers` list in your app:

```java
MyApp(
   // Add the PageViewObserver to the navigatorObservers list.
   navigatorObservers: [PageViewObserver()],
   routes: {
     // Define your named routes here
   },

),
```

This setup enables automatic screen view tracking for standard route navigation.

### Step 4 – Tracking page views manually (for custom navigation)

For navigation widgets like **Bottom Navigation** or **Tab Navigation**, which do not trigger route changes, use the `screenViewChange` function to track screen views manually.

For example, using the `onTap` callback within a Bottom Navigation bar widget allows for capturing a new route each time the user taps on a different tab:

```java
BottomNavigationBar(
   items: items,
   currentIndex: _selectedIndex,
   selectedItemColor: Colors.pink,
   onTap: (index) {
      _onItemTapped(index);
      final label = items[index].label ?? 'Tab-$index';

      // Manually calling the `screenViewChange` with the label
      screenViewChange(label);
   },
)
```

### Step 5 – (Optional) Tracking ad events

>ℹ️ The ads tracking is available only for accounts that use [VTEX Ads](https://developers.vtex.com/docs/guides/vtex-ads). If you're interested in this feature, open a ticket with [VTEX Support](https://support.vtex.com/hc/en-us).

To start tracking your ad events, follow these steps:

1. Call the `addAdsListener`

To track ad impressions, views, and clicks, use the `addAdsListener` extension method by attaching it to any widget that displays ads:

```java
yourAdWidget.addAdsListener({Map<String, String> adMetadata);
```

- `yourAdWidget`: The ad widget you want to monitor.
- `adMetadata`: A Map containing specific details about the ad, which will be sent to your analytics service upon a click.
