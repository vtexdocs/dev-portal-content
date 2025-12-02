---
title: "Installing Activity Flow in React Native apps"
---

In this guide, you'll learn how to install and use the Activity Flow SDK in React Native apps for Android and iOS. By following these steps, you'll be able to track user navigation, order events, deep links, and ad events in your app.

## Before you begin

<Steps>
  
### Use React Navigation or Expo Router in your project

To manage navigation between different screens of your app, you must use either [React Navigation](https://reactnavigation.org/) or [Expo Router](https://docs.expo.dev/router/introduction/). This is important because Activity Flow relies on the `useFocusEffect` hook from React Navigation to detect changes in pages. For more information, refer to the [React Navigation guide](https://reactnavigation.org/docs/getting-started).

### Install the Activity Flow package

Activity Flow depends on [`@react-native-async-storage/async-storage`](https://github.com/react-native-async-storage/async-storage) to store navigation data locally. This ensures events are captured even when the device is offline.

To install the library, follow these steps:

1. In your project directory, run:

    <Tabs items={['yarn', 'npm']}>
        <Tab>
            ```bash
            yarn add @vtex/activity-flow @react-native-async-storage/async-storage
            ```
        </Tab>
        <Tab>
            ```bash
            npm install @vtex/activity-flow @react-native-async-storage/async-storage
            ```
        </Tab>
    </Tabs>

2. For iOS, sync native dependencies:

```bash
 cd ios && pod install && cd ../
```

This process installs the Activity Flow script in your app by adding a new dependency in the `package.json` file.

</Steps>

## Instructions

### Step 1 - Importing the Activity Flow plugin

In your app's main file (for example, `App.js` or `App.tsx`), import the plugin as follows:

```js
import { initActivityFlow } from '@vtex/activity-flow';
```

### Step 2 - Creating an Activity Flow instance

Set the account name to create an instance of the main package class:

```js
function App() {
  // Initialize the Activity Flow plugin with your VTEX account name
  initActivityFlow({
    accountName: 'your-account-name', // Replace with your VTEX account name
  });
  // ...rest of your app
}
```

## Usage

### Tracking page views automatically

To track navigation state changes, integrate the `usePageViewObserver` hook with the `NavigationContainer`, the root component of React Navigation, in your app's main file. To do so, follow these steps:

1. Import the observer hook:

    ```js
    import { usePageViewObserver } from '@vtex/activity-flow';
    ```

2. Create a reference for the `NavigationContainer`:

    ```js
    const navigationRef = useRef(null);
    ```

3. Pass the reference to `NavigationContainer`:

    ```js
    <NavigationContainer ref={navigationRef}>
      {/* Stack configurations */}
    </NavigationContainer>
    ```

4. Use the observer hook to track page views:

```js
usePageViewObserver({ navigationRef });
```

Activity Flow now automatically tracks page transitions. When you navigate between screens, it records each page view and sends event data.

### Tracking order group

The Activity Flow SDK can automatically capture order details from navigation parameters, such as `orderGroup` or `orderPlaced`, and any query parameters from the navigator stack. These parameters help validate checkout events and confirm successful purchases.

To enable this feature, include the required parameter in your page redirect configuration. See the example below:

```ts //checkout_screen.tsx
<TouchableOpacity
  onPress={() =>
    navigation.navigate('/purchase_success', {
      orderGroup: '1234567890',
      orderId: '1234',
      // ...other params
    })
  }
>
  <Text>Confirm Purchase</Text>
</TouchableOpacity>
```

When a user completes a purchase, Activity Flow automatically captures orderGroup and other query parameters during the screen transition.

### Tracking deep links

The Activity Flow SDK automatically captures deep-link query parameters from the `usePageViewObserver` hook and includes them in page view events. To enable this feature, configure deep linking in your app according to its platform: [Android](#android) or [iOS](#ios).

#### Android

To enable deep-link handling in your Android app, add intent filters to the `AndroidManifest.xml` file for each route that can be accessed via a deep link. See the example below:

```xml AndroidManifest.xml
<!-- Deep link via HTTPS -->
<intent-filter>
  <action android:name="android.intent.action.VIEW" />
  <category android:name="android.intent.category.DEFAULT" />
  <category android:name="android.intent.category.BROWSABLE" />
  <data
    android:scheme="https"
    android:host="mystore.com"
    android:pathPrefix="{APP_ROUTE}"
  />
</intent-filter>
<!-- Deep link via custom scheme -->
<intent-filter>
  <action android:name="android.intent.action.VIEW" />
  <category android:name="android.intent.category.DEFAULT" />
  <category android:name="android.intent.category.BROWSABLE" />
  <data android:scheme="{YOUR_CUSTOM_SCHEME}" />
</intent-filter>
```

This `AndroidManifest` adds two intent filters for deep linking:

- One for HTTPS URLs starting with `"https://example.com/{APP_ROUTE}"`.
- One for a custom scheme `"{YOUR_CUSTOM_SCHEME}"`. Both use `action.VIEW`, `category_DEFAULT`, and `category_BROWSABLE`, allowing the Activity Flow to launch from browsers or other apps.
The data tag for deep link via HTTP specifies the `scheme`, `host`, and an optional `pathPrefix`, matching any path that begins with that prefix (for example, **"/products/42"** if `{APP_ROUTE}` is **"/products"**). The main difference between intent filters for different routes is the `android:pathPrefix` attribute, which specifies the app route.
For a deep link via a custom scheme, the data tag sets the scheme, matching any URL that starts with that scheme (for example, **myapp://...** if `{YOUR_CUSTOM_SCHEME}` is **myapp**).

#### iOS

To enable deep-link handling in your iOS app, add your URL scheme to the `Info.plist` file and handle incoming URLs in the `AppDelegate` file:

1. Register your custom URL scheme by adding the following configuration to your `Info.plist` file:

```ts info.plist
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

In the `info.plist` configuration, `{YOUR_BUNDLE_URL_SCHEME}` is the custom URL scheme your app will handle, that is, the prefix before `://` in deep links. For example, setting it to `myapp` makes links like `myapp://path` open your app. Enter only the scheme name, without `://`. The `{YOUR_BUNDLE_URL_NAME}` label is a unique identifier for this URL type entry, typically in reverse-DNS format, used to distinguish the configuration and doesn't affect routing. For example, `com.example.appname`.

2. Handle incoming deep links by modifying your `AppDelegate.swift` (or `AppDelegate.mm`) file. The following example handles deep links for cold starts, when the app isn't running, and warm starts, when the app is already running.

```ts AppDelegate.swift
import UIKit
import React

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {
  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
  ) -> Bool {
    // ... your existing setup code ...
    // Capture initial URL if app was launched with a deep link (cold start)
    if let initialURL = launchOptions?[UIApplication.LaunchOptionsKey.url] as? URL {
      NotificationCenter.default.post(
        name: NSNotification.Name("RCTOpenURLNotification"),
        object: nil,
        userInfo: ["url": initialURL]
      )
    }
    return true
  }

  * Handles incoming URLs from Custom URL Schemes (e.g., myapp://path)
  func application(
    _ app: UIApplication,
    open url: URL,
    options: [UIApplication.OpenURLOptionsKey : Any] = [:]
  ) -> Bool {
    // Post notification for Activity Flow's CaptureDeepLinkModule
    NotificationCenter.default.post(
      name: NSNotification.Name("RCTOpenURLNotification"),
      object: nil,
      userInfo: ["url": url]
    )
    // Pass the URL to React Native's standard linking manager
    return RCTLinkingManager.application(app, open: url, options: options)
  }

  * Handles incoming URLs from Universal Links (e.g., https://mystore.com/product)
  func application(
    _ application: UIApplication,
    continue userActivity: NSUserActivity,
    restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void
  ) -> Bool {
    // Check if the activity is a web browsing activity (Universal Link)
    if userActivity.activityType == NSUserActivityTypeBrowsingWeb {
      // Post notification for Activity Flow's CaptureDeepLinkModule
      if let url = userActivity.webpageURL {
        NotificationCenter.default.post(
          name: NSNotification.Name("RCTOpenURLNotification"),
          object: nil,
          userInfo: ["url": url]
        )
      }
    }
    // Pass the user activity to React Native's standard linking manager
    return RCTLinkingManager.application(
      application,
      continue: userActivity,
      restorationHandler: restorationHandler
    )
  }

  return false
}
```

Your Android app can now be launched from both web links (`https://mystore.com/products/42`) and custom scheme links: (`myapp://products/42`).

### Tracking ad events

>ℹ️ Ad tracking is available only for accounts that use [VTEX Ads](https://developers.vtex.com/docs/guides/vtex-ads). If you're interested in this feature, open a ticket with [VTEX Support](https://support.vtex.com/hc/en-us).

To configure ad tracking, follow these steps:

1. Create the ad object

To track events, provide an object containing all information relevant to the ad event. The accountName field is mandatory.

```ts
const adParams = {
  accountName: 'your-account-name',
  adId: 'main-banner-01',
  // ...other parameters
};
```

2. Integrate the ad tracker into your components

There are two methods to integrate the ad tracker into your components: Using the AFAdsTracker Wrapper component or using the useAdsTracker hook.

#### Using the AFAdsTracker wrapper component

To track ad events with the AFAdsTracker, wrap your ad component with it and provide the necessary tracking parameters. The wrapper will automatically manage all required event handlers.

Use this method when your entire child component represents a clickable ad. See the example below:

```ts
<AFAdsTracker params={adParams}>
  <TouchableOpacity
    style={styles.button}
    onPress={() => {
      navigation.navigate('/checkout');
    }}
  >
    <Text style={styles.buttonText}>Buy</Text>
  </TouchableOpacity>
</AFAdsTracker>
```

The example below shows a React Native app that uses @vtex/activity-flow with React Navigation to track navigation across multiple screens and ad events from a single location.

```ts
// App.tsx
import React, { useRef, useEffect } from 'react';
import { View, Text, Button, TouchableOpacity, StyleSheet } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import {
  initActivityFlow,
  usePageViewObserver,
  AFAdsTracker,
} from '@vtex/activity-flow';

type NavProps = { navigation: any };

const HomeScreen = ({ navigation }: NavProps) => {
  return (
    <View>
      <Text>Home</Text>
      <Button title="Go to Profile" onPress={() => navigation.navigate('Profile')} />
      <View />
      <Button title="Go to Ads" onPress={() => navigation.navigate('Ads')} />
    </View>
  );
};

const ProfileScreen = ({ navigation }: NavProps) => (
  <View>
    <Text>Profile</Text>
    <Button title="Go to Details" onPress={() => navigation.navigate('Details')} />
  </View>
);

const DetailsScreen = ({ navigation }: NavProps) => {
  return (
    <View>
      <Text>Details</Text>
      <Button title="Go Back" onPress={() => navigation.goBack()} />
    </View>
  );
};

const AdsScreen = () => {
  // Include your VTEX accountName here (required for sending ad events)
  const adParams = {
    accountName: 'your-account-name',
    adId: '12345',
    campaign: 'summer_campaign',
  };

  return (
    <View>
      <Text>Ads</Text>
      {/* Wrap your ad with AFAdsTracker. The wrapper wires impression/view/click. */}
      <AFAdsTracker params={adParams}>
        <TouchableOpacity
          onPress={() => {
            // Your CTA action goes here (e.g., navigate, open link)
            console.log('Ad clicked — navigate or handle CTA');
          }}
        >
          <Text>Sponsored Ad</Text>
          <Text>Check out our new campaign!</Text>
          <Text>Buy now</Text>
        </TouchableOpacity>
      </AFAdsTracker>
    </View>
  );
};

const Stack = createNativeStackNavigator();

export default function App() {
  const navigationRef = useRef(null);

  // Initialize Activity Flow once with your VTEX account name
  useEffect(() => {
    initActivityFlow({
      accountName: 'your-account-name',
    });
  }, []);

  // Track page views automatically (attach to the navigation ref)
  usePageViewObserver({ navigationRef });

  return (
    <NavigationContainer ref={navigationRef as any}>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} />

        <Stack.Screen name="Profile" component={ProfileScreen} />

        <Stack.Screen name="Details" component={DetailsScreen} />

        <Stack.Screen name="Ads" component={AdsScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
```

The app initializes tracking via `initActivityFlow` with your VTEX account name, and enables automatic page view tracking by calling `usePageViewObserver` with a `NavigationContainer` ref.

On the Ads screen, ad parameters (including the required `accountName`) are passed to the AFAdsTracker wrapper, which wraps a fully clickable child to automatically fire impression, view, and click events without manual handler wiring.

The wrapper detects clicks via `onTouchEndCapture`. If your ad interaction isn't based on it or can't be wrapped, [use the `useAdsTracker` hook](#using-the-useadstracker-hook) instead.

>⚠️ To use this example in your project, remember to replace `accountName` based on your scenario.

#### Using the `useAdsTracker` hook

The `useAdsTracker` hook provides more control over how events are attached. It returns handlers and a ref that you must apply manually to your components.

Use this method when:

- You can't use an extra `<View>` to wrap your component.
- The component that receives events (for example, a `TouchableOpacity`) is different from the component that defines the visibility area.
- You integrate with third-party component libraries that don’t allow a generic wrapper.
- The click property isn't `onTouchEnd`, since the **AFAdsTracker** wrapper uses `onTouchEndCapture`.

Follow the steps below to use this hook:

1. Import and call the hook:

```js
import { useAdsTracker } from '@vtex/activity-flow';

const { handleLayout, handlePress, viewRef } = useAdsTracker(adParams);
```

2. Attach the handlers and ref to your component. See the example below:

```js
<TouchableOpacity
  ref={viewRef} // Attach the ref to track visibility (view)
  onLayout={handleLayout} // Attach the layout handler (impression)
  onPress={handlePress} // Attach the click handler (click)
>
  <Image source={{}} />
</TouchableOpacity>
```

The hook returns an object with three properties:

- `handleLayout`: A function to be passed to your component's `onLayout` prop. It fires the impression event.
- `handlePress`: A function to be passed to a touch prop, like `onPress` or `onTouchEndCapture`. It fires the click event.
- `viewRef`: A `ref` that must be attached to the `ref` prop of the ad's main component. It monitors visibility and fires the view event.

Below is an implementation example of a React Native code that defines a `CustomAd` component. This component uses the `useAdsTracker` hook from the `@vtex/activity-flow` library to integrate with an ad tracking system for visibility and interaction.

```ts
import { useAdsTracker } from "@vtex/activity-flow";
import { Image, TouchableOpacity } from "react-native";

export const CustomAd = () => {
   // 1. Define the parameters
   const adParams = {
accountName: 'my-company-x',
adId: 'sidebar-banner-02',
   };

// 2. Call the hook to get the handlers and the ref
const { handleLayout, handlePress, viewRef } = useAdsTracker(adParams);

return (
   // 3. Attach the handlers and ref to your component
   <TouchableOpacity
ref={viewRef} // Attach the ref to track visibility (view)
onLayout={handleLayout} // Attach the layout handler (impression)
onPress={handlePress} // Attach the click handler (click)
   >
<Image source={{}} />
   </TouchableOpacity>
  );
};
```

The component's purpose is to render an ad inside a touchable container and report three key events to the tracking system: **impression**, **view**, and **click**.
