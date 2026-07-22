---
title: "Installing Activity Flow in Flutter apps"
slug: "installing-activity-flow-in-flutter-apps"
excerpt: "Learn how to install the VTEX Activity Flow SDK in your Flutter app to track navigation, page views, deep links, ads, and customer interactions across Android and iOS."
hidden: false
createdAt: "2025-12-18T16:30:39.842Z"
updatedAt: "2026-07-03T00:00:00.000Z"
seeAlso:
  - "/docs/guides/activity-flow"
---

In this guide, you'll learn how to install and configure the [VTEX Activity Flow SDK](https://developers.vtex.com/docs/guides/activity-flow) in Flutter apps for Android and iOS. By following these steps, you'll be able to track user navigation, handle deep links, and collect ad events and customer interaction events (clicks, views, and impressions) in your app.

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

```dart
import 'package:activity_flow/activity_flow.dart';
```

### Step 2 – Creating an Activity Flow instance

Set the account name to create an instance of the main package class:

```dart
void main() {
  runApp(const MyApp());
}

class App extends StatelessWidget {
  Widget build(BuildContext context) {
    // Call activity flow here
    initActivityFlow(accountName: appAccountName);
    ...
  }
}
```

## Usage

### Tracking page views automatically

To automatically track user navigation between app pages, add the `PageViewObserver` to the `navigatorObservers` list in your app:

```dart
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

For navigation widgets such as `BottomNavigationBar` or `TabBar` that don't trigger route changes, use the `screenViewChange` function to manually track screen views.

For example, using the `onTap` callback within a `BottomNavigationBar` widget allows for capturing a new route each time the user taps on a different tab:

```dart
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

### Tracking deep links

The Activity Flow SDK automatically captures deep link query parameters and includes them in page view events when your app is configured for deep linking. Configure each platform as follows.

#### Android

Add intent filters to `AndroidManifest.xml` for each route that can be accessed via deep link:

```xml android/app/src/main/AndroidManifest.xml
<intent-filter>
  <action android:name="android.intent.action.VIEW" />
  <category android:name="android.intent.category.DEFAULT" />
  <category android:name="android.intent.category.BROWSABLE" />
  <data
    android:scheme="https"
    android:host="example.com"
    android:pathPrefix="{APP_ROUTE}"
  />
</intent-filter>

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

    ```xml ios/{YourApp}/Info.plist
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

    ```swift
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

3. Configure `SceneDelegate`

If your project uses a `SceneDelegate`, also forward deep links there:

    ```swift ios/Runner/SceneDelegate.swift
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

### Tracking ad events

>ℹ️ Ads tracking is available only for accounts using [VTEX Ads](https://developers.vtex.com/docs/guides/vtex-ads). If you're interested in this feature, open a ticket with [VTEX Support](https://support.vtex.com/hc/en-us).

When you apply the listener to a widget, the SDK automatically tracks three events:

- **Impressions:** When the widget is first built and rendered.
- **Views:** When at least 50% of the widget is visible on screen for at least 1 continuous second.
- **Clicks:** When the user taps the widget.

To start tracking your ad events, follow these steps:

1. Call the `addAdsListener` method

To enable tracking, call the `addAdsListener` extension method on any Flutter widget that represents an ad:

    ```dart
    yourAdWidget.addAdsListener(Map<String, String> adMetadata);
    ```

    - `yourAdWidget`: The ad widget you want to monitor.
    - `adMetadata`: A map containing specific details about the ad, which will be sent to your analytics service upon a click.

The following example initializes the Activity Flow to track page views automatically and demonstrates ad tracking:

```dart
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

This Flutter screen is constructed as a `StatelessWidget` that lists products and displays an ad banner. The banner's `Container` is wrapped with Activity Flow's `addAdsListener`, which attaches an ad-event listener and sends the provided metadata map with each event.

This instrumentation enables the automatic tracking of impressions, viewability, and clicks, allowing for comprehensive analytics tied to `adId`, `creativeId`, `position`, and `campaignName`.

### Tracking customer interaction events

Beyond page views and ad events, Activity Flow provides individual extension methods for tracking click, view, and impression events on any widget. These methods can be used independently or combined on the same widget.

All methods require `elementSource`, a string that identifies the tracked element. This field is sent as a top-level property in the event payload, separate from the other attributes.

#### Click event

Use `addClickListener` on any widget to capture tap interactions. A click event is fired when the user taps (not drags) on the element. Pass any custom attributes you want to associate with the interaction.

>ℹ️ You must include the `elementSource` key in the method's metadata map.

```dart
ElevatedButton(
  onPressed: () => Navigator.pushNamed(context, '/checkout'),
  child: const Text('Buy Now'),
).addClickListener({
  'elementSource': 'buy-now-button',
  'productId': product.id,
});
```

#### View event

Use `addViewListener` to fire a view event when the widget has been at least 50% visible on screen for at least 1 second (IAB standard). The event fires once per app session — it does not re-fire if the widget scrolls off-screen and back, or if the user navigates away and returns.

>ℹ️ You must include the `elementSource` key in the method's metadata map.

```dart
ProductCard(product: product).addViewListener({
  'elementSource': 'product-card',
  'productId': product.id,
});
```

#### Impression events

Use the `addImpressionListener` method to trigger an impression event immediately upon the widget being built and rendered within the application's widget tree.

>ℹ️ You must include the `elementSource` key in the method's metadata map.

```dart
ProductCard(product: product).addImpressionListener({
  'elementSource': 'product-card',
  'productId': product.id,
});
```

#### Combining multiple listeners

Combine the listeners on a single widget to track the full interaction funnel: whether the element was rendered (impression), actually seen by the user (view), and clicked (click).

The example below chains the impression and view listeners on a single widget to capture both event types simultaneously:

```dart
ProductCard(product: product)
  .addImpressionListener({
    'elementSource': 'product-card',
    'productId': product.id,
  })
  .addViewListener({
    'elementSource': 'product-card',
    'productId': product.id,
  });
```

## Flutter automated tests

To ensure your Flutter test runs work correctly when the Activity Flow is installed, run tests with a test environment flag using a `--dart-define` flag.

The `--dart-define` flag allows you to pass compile-time key=value pairs into your Flutter app as Dart environment declarations. To do so, follow the steps below:

1. In your terminal, run `flutter test --dart-define=ACTIVITY_FLOW_TEST_ENV=true`.
2. In a code editor, open your project.
3. In the code editor settings, search for `dart.flutterTestAdditionalArgs`.
4. Add to it the value `--dart-define=ACTIVITY_FLOW_TEST_ENV=true`.

    >ℹ️ Alternatively, open the `settings.json` file of your project and add `"dart.flutterTestAdditionalArgs": ["--dart-define=ACTIVITY_FLOW_TEST_ENV=true"]`.

## Use case example

Below is an example that contains an app with some pages and navigation through them:

```dart
import 'package:activity_flow/activity_flow.dart';
import 'package:flutter/material.dart';
import 'package:example/screens/favorite.dart';
import 'package:example/screens/products.dart';
import 'package:example/screens/profile.dart';

void main() {
  runApp(const ExampleApp());
}

/// A MaterialApp with a custom theme and routes.
///
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
    );
  }
}

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
///
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

The example demonstrates how to integrate Activity Flow into a Flutter app by importing the necessary package, initializing it with `initActivityFlow(accountName: appAccountName)`, and constructing a `MaterialApp` with named routes and a `PageViewObserver` to automatically capture page-view events.

It outlines a `MyHomePage` that incorporates an `AdBanner` that uses `addAdsListener` to pass ad metadata, such as product name, price, and ID. Additionally, it features navigation buttons sourced from a routes list.

The reusable `ButtonTemplate` facilitates navigation through `Navigator.pushNamed`, showcasing a standard configuration for automatic screen tracking, as well as ad impression and click tracking, in a Flutter application.
