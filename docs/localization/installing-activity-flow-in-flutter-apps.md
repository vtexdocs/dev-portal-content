---
title: "Installing Activity Flow in Flutter apps"
slug: "installing-activity-flow-in-flutter-apps"
hidden: false
createdAt: "2025-10-23T17:07:05.899Z"
---

In this guide, you'll learn how to install and configure the [VTEX Activity Flow SDK](https://developers.vtex.com/docs/guides/activity-flow) in Flutter apps for Android and iOS. By following these steps, you'll be able to track user navigation, handle deep links, and collect ad events from your app.

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

## Usage

### Tracking page views automatically

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

### Tracking page views manually (for custom navigation)

For navigation widgets like `BottomNavigationBar` or `TabBar`, which do not trigger route changes, use the `trackPageView` function to manually track screen views.

For example, using the `onTap` callback within a `BottomNavigationBar` widget allows for capturing a new route each time the user taps on a different tab:

```java
BottomNavigationBar(
   items: items,
   currentIndex: _selectedIndex,
   selectedItemColor: Colors.pink,
   onTap: (index) {
      _onItemTapped(index);
      final label = items[index].label ?? 'Tab-$index';

      // Manually calling the `trackPageView` with the label
      trackPageView(label);
   },
)
```

### Tracking deep links

The Activity Flow SDK automatically captures deep link query parameters and includes them in page view events when your app is configured for deep linking. Configure each platform as follows.

#### Android

Add intent filters to `AndroidManifest.xml` for each route that can be accessed via deep link:

``` android/app/src/main/AndroidManifest.xml
<!-- Deep link via HTTPS -->
<intent-filter>
  <action android:name="android.intent.action.VIEW" />
  <category android:name="android.intent.category.DEFAULT" />
  <category android:name="android.intent.category.BROWSABLE" />
  <data
    android:scheme="https"
    android:host="example.com"
    android:pathPrefix="{APP_ROUTE}" />
</intent-filter>
<!-- Deep link via Custom Scheme -->
<intent-filter>
  <action android:name="android.intent.action.VIEW" />
  <category android:name="android.intent.category.DEFAULT" />
  <category android:name="android.intent.category.BROWSABLE" />
  <data android:scheme="YOUR_CUSTOM_SCHEME" />
</intent-filter>
```

The main difference between intent filters for different routes is the `android:pathPrefix` attribute, which specifies the app route.

#### iOS

Configure both `Info.plist` and the app delegate to handle deep links.

1. Register a custom URL scheme in `Info.plist`:

``` ios/{YourApp}/Info.plist
<key>CFBundleURLTypes</key>
<array>
  <dict>
    <key>CFBundleURLSchemes</key>
    <array>
      <string>{YOUR_BUNDLE_URL_SCHEME}</string>
    </array>
    <key>CFBundleURLName</key>
    <string>{YOUR_BUNDLE_URL_NAME}</string>
  </dict>
</array>
```

2. Handle incoming URLs in `AppDelegate.swift` (or `AppDelegate.mm`) for both cold and warm starts:

```typescript
import Flutter
import UIKit
import activity_flow

@main
@objc class AppDelegate: FlutterAppDelegate {
  override func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    GeneratedPluginRegistrant.register(with: self)

    // Capture initial URL if app was launched with a deep link (cold start)
    if let initialURL = launchOptions?[UIApplication.LaunchOptionsKey.url] as? URL {
      DeepLinkManager.shared.handle(url: initialURL)
    }

    return super.application(application, didFinishLaunchingWithOptions: launchOptions)
  }

  // Handles incoming URLs from Custom URL Schemes (e.g., myapp://path)
  override func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    DeepLinkManager.shared.handle(url: url)
    return super.application(app, open: url, options: options)
  }

  // Handles incoming URLs from Universal Links
  override func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
    // Check if the activity is a web browsing activity (Universal Link)
    if userActivity.activityType == NSUserActivityTypeBrowsingWeb {
      if let url = userActivity.webpageURL {
        DeepLinkManager.shared.handle(url: url)
      }
    }
        return super.application(application, continue: userActivity, restorationHandler: restorationHandler)
  }
}
```

3. Configure `SceneDelegate`.

If your project uses a `SceneDelegate`, also forward deep links there:

```typescript ios/Runner/SceneDelegate.swift
import UIKit
import Flutter
import activity_flow

class SceneDelegate: FlutterSceneDelegate {
  override func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
    // Capture deep links on cold start
    var hasDeepLink = false

    if let userActivity = connectionOptions.userActivities.first(where: { $0.activityType == NSUserActivityTypeBrowsingWeb }) {
    if let url = userActivity.webpageURL {
      DeepLinkManager.shared.handle(url: url)
      hasDeepLink = true
      }
    } else if let url = connectionOptions.urlContexts.first?.url {
      DeepLinkManager.shared.handle(url: url)
      hasDeepLink = true
    }

    // Call super with empty options if a deep link was handled
    if hasDeepLink {
      super.scene(scene, willConnectTo: session, options: UIScene.ConnectionOptions())
    } else {
      super.scene(scene, willConnectTo: session, options: connectionOptions)
    }
  }

  override func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
    if let url = URLContexts.first?.url {
      DeepLinkManager.shared.handle(url: url)
    }
  }

  override func scene(_ scene: UIScene, continue userActivity: NSUserActivity) {
    if userActivity.activityType == NSUserActivityTypeBrowsingWeb {
      if let url = userActivity.webpageURL {
        DeepLinkManager.shared.handle(url: url)
      }
    }
  }
}
```

### (Optional) Tracking ad events

>ℹ️ Ads tracking is available only for accounts using [VTEX Ads](https://developers.vtex.com/docs/guides/vtex-ads). If you're interested in this feature, open a ticket with [VTEX Support](https://support.vtex.com/hc/en-us).

When you apply the listener to a widget, the SDK automatically tracks three events:

- **Impression:** When the widget is first built and rendered.
- **View:** When at least 50% of the widget is visible on screen for at least 1 continuous second.
- **Click:** When the user taps the widget.

To start tracking your ad events, follow these steps:

1. Call the `addAdsListener`

To enable tracking, call the `addAdsListener` extension method on any Flutter widget that represents an ad:

```java
yourAdWidget.addAdsListener({Map<String, String> adMetadata);
```

- `yourAdWidget`: The ad widget you want to monitor.
- `adMetadata`: A map containing specific details about the ad, which will be sent to your analytics service upon a click.

The following example initializes the Activity Flow to track page views automatically and demonstrates manual tracking for tab changes:

```
import 'package:activity_flow/activity_flow.dart';
import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Home')),
      body: ListView(
        children: [
          const Padding(
            padding: EdgeInsets.all(16.0),
            child: Text('Featured Products'),
          ),

          // Standard content
          const ProductTile(name: 'Product A'),
          const ProductTile(name: 'Product B'),

          // Ad Widget with Activity Flow tracking
          // We wrap the visual component (e.g., Image, Container) with the listener
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 10.0),
            child: Container(
              height: 150,
              width: double.infinity,
              color: Colors.grey[200],
              child: Image.asset(
                'assets/promo_banner.jpg',
                fit: BoxFit.cover,
              ),
            ).addAdsListener({
              'adId': 'summer_campaign_123',
              'creativeId': 'banner_v1',
              'position': 'list_middle',
              'campaignName': 'Summer Sale 2024',
            }),
          ),
          // More content
          const ProductTile(name: 'Product C'),
        ],
      ),
    );
  }
}
```

This Flutter screen, constructed as a `StatelessWidget` that lists products and displays an ad banner. The banner's Container is wrapped with Activity Flow's `addAdsListener`, which attaches an ad-event listener and sends the provided metadata map with each event.

This instrumentation enables the automatic tracking of impressions, viewability, and clicks, allowing for comprehensive analytics tied to `adId`, `creativeId`, `position`, and `campaignName`.

## Flutter automated tests

To ensure your Flutter test runs work correctly when the Activity Flow is installed, run tests with a test environment flag using a `--dart-define` flag.

The `--dart-define` flag allows you to pass compile-time key=value pairs into your Flutter app as Dart environment declarations. To do so, follow the steps below:

1. In your terminal, run `flutter test --dart-define=ACTIVITY_FLOW_TEST_ENV=true`.
2. In a code editor, open your project.
3. In the code editor settings, search for `dart.flutterTestAdditionalArgs`.
4. Add to it the value `--dart-define=ACTIVITY_FLOW_TEST_ENV=true`.
5. Open the `settings.json` file of your project.
6. Add the following: `"dart.flutterTestAdditionalArgs": ["--dart-define=ACTIVITY_FLOW_TEST_ENV=true"]`

## Use case example

Below is an example that contains an app with some pages and navigation through them:

```java
import 'package:activity_flow/activity_flow.dart';
import 'package:flutter/material.dart';
import 'package:example/screens/favorite.dart';
import 'package:example/screens/products.dart';
import 'package:example/screens/profile.dart';

void main() {
   runApp(const ExampleApp());
}
/// A MaterialApp with a custom theme and routes.
/// The routes are defined in the [routes] property.
/// The theme is defined in the [theme] property.
class ExampleApp extends StatelessWidget {
   const ExampleApp({super.key});

   @override
   Widget build(BuildContext context) {
      initActivityFlow(accountName: appAccountName);

      return MaterialApp(
         title: 'Example App',
         theme: ThemeData(
           colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
           useMaterial3: true,
         ),
         routes: {
           '/': (context) => const MyHomePage(),
           '/products': (context) => const ProductsScreen(),
           '/profile': (context) => const ProfileScreen(),
           '/favorites': (context) => const FavoriteScreen(),
         },
         initialRoute: '/',
         navigatorObservers: [PageViewObserver()],

/// A home screen with buttons to navigate to other screens.
class MyHomePage extends StatelessWidget {
   const MyHomePage({super.key});

   final List<Map> _routes = const [
      {
        'name': 'Products',
        'route': '/products',
      },
      {
        'name': 'Profile',
        'route': '/profile',
      }
    ];

   @override
   Widget build(BuildContext context) {
      return Scaffold(
        appBar: AppBar(
          backgroundColor: Theme.of(context).colorScheme.inversePrimary,
          title: const Text('Home Screen'),
        ),
        body: Center(
          child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
            const AdBanner().addAdsListener({
              'productName': 'Sneakers',
              'productPrice': '59.99',
              'adID': '1123',
            }),
            ..._routes.map((route) => ButtonTemplate(
                  title: route['name'],
                  route: route['route'],
               )),
        ])),
      );
   }
}

/// A template for creating buttons.
/// Receives a [title], [icon], and [route] to navigate to.
/// Returns an [ElevatedButton.icon] with the given parameters.
class ButtonTemplate extends StatelessWidget {
   const ButtonTemplate({
      super.key,
      required this.title,
      required this.route,
   });

   final String title;
   final String route;

   @override
   Widget build(BuildContext context) {
      return ElevatedButton(
        onPressed: () => Navigator.pushNamed(context, route),
        child: Text(title),
      );
   }
}
```

The example demonstrates the integration of Activity Flow into a Flutter app by importing the necessary package, initializing it with `initActivityFlow(accountName: appAccountName)`, and constructing a `MaterialApp` with named routes and a `PageViewObserver` to automatically capture page-view events.

It outlines a `MyHomePage` that incorporates an `AdBanner`, which uses `addAdsListener` to pass ad metadata such as product name, price, and ID. Additionally, it features navigation buttons sourced from a routes list.

The reusable `ButtonTemplate` facilitates navigation through `Navigator.pushNamed`, showcasing a standard configuration for automatic screen tracking, as well as ad impression and click tracking, in a Flutter application.
