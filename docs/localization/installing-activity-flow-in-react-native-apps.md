---
title: "Installing Activity Flow in React Native apps"
slug: "installing-activity-flow-in-react-native-apps"
excerpt: "Learn how to install Activity Flow in your React Native app."
hidden: false
createdAt: "2025-10-23T17:07:05.899Z"
---

In this guide, you'll learn how to install and use the Activity Flow SDK in React Native apps for Android and iOS.

## Before you begin

<Steps>
  
### Use React Navigation or Expo Router in your project

You must use [React Navigation](https://reactnavigation.org/) or [Expo Router](https://docs.expo.dev/router/introduction/) to manage navigation between different screens of your app, as Activity Flow relies on the useFocusEffect hook from React Navigation to detect page changes. Learn more in the React guide [React Navigation](https://reactnavigation.org/docs/getting-started).

### Install the Activity Flow package

The `@react-native-async-storage/async-storage` library is required because it provides a persistent key-value storage system that is essential for tracking and storing user navigation data locally. This ensures that the Activity Flow plugin can function correctly, even in scenarios where network connectivity is temporarily unavailable. Installing it directly ensures that the native dependencies are correctly linked and available in your app.

To install the library, follow these steps:

1. In your project directory, run:

	<Tabs items={['yarn', 'npm']}>
    	<Tab>```bash yarn add @vtex/activity-flow @react-native-async-storage/async-storage```</Tab>
    	<Tab>```bash npm install @vtex/activity-flow @react-native-async-storage/async-storage```</Tab>
	</Tabs>

2. For iOS, sync native dependencies:

	```bash
	cd ios && pod install && cd ../
	```

This process installs the Activity Flow script in your app by adding a new dependency in the package.json file.

</Steps>

## Instructions

### Step 1 - Importing the Activity Flow plugin

In your app's main file (for example, App.js or App.tsx), import the plugin as follows:

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

### Step 3 - Tracking page views automatically

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

### Step 4 - Tracking ad events

>ℹ️ The ads tracking is available only for accounts that use [VTEX Ads](https://developers.vtex.com/docs/guides/vtex-ads). If you're interested in this feature, open a ticket with [VTEX Support](https://support.vtex.com/hc/en-us).

To configure the ads tracking, follow these steps:

1. Create the ads object

To track events, provide an object containing all information relevant to the ad event. The accountName field is mandatory; if omitted, events are not sent. See the example below.

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

Below is an implementation example of a React Native app using @vtex/activity-flow with React Navigation to track navigation through multiple screens and ad events in a single location.

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
    <View style={styles.screen}>
      <Text style={styles.title}>Home</Text>
      <Button title="Go to Profile" onPress={() => navigation.navigate('Profile')} />
      <View style={styles.spacer} />
      <Button title="Go to Ads" onPress={() => navigation.navigate('Ads')} />
    </View>
  );
};

const ProfileScreen = ({ navigation }: NavProps) => (
  <View style={styles.screen}>
    <Text style={styles.title}>Profile</Text>
    <Button title="Go to Details" onPress={() => navigation.navigate('Details')} />
  </View>
);

const DetailsScreen = ({ navigation }: NavProps) => {
  return (
    <View style={styles.screen}>
      <Text style={styles.title}>Details</Text>
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
    <View style={styles.screen}>
      <Text style={styles.title}>Ads</Text>

      {/* Wrap your ad with AFAdsTracker. The wrapper wires impression/view/click. */}
      <AFAdsTracker params={adParams}>
        <TouchableOpacity
          style={styles.adCard}
          onPress={() => {
            // Your CTA action goes here (e.g., navigate, open link)
            console.log('Ad clicked — navigate or handle CTA');
          }}
        >
          <Text style={styles.adTitle}>Sponsored Ad</Text>
          <Text>Check out our new campaign!</Text>
          <Text style={styles.cta}>Buy now</Text>
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

const styles = StyleSheet.create({
  screen: {
    flex: 1,
    padding: 16,
    gap: 16,
  },
  title: {
    fontSize: 22,
    fontWeight: '700',
  },
  spacer: { height: 16 },
  adCard: {
    padding: 16,
    borderRadius: 8,
    backgroundColor: '#f0f3f7',
  },
  adTitle: { fontWeight: '700', marginBottom: 4 },
  cta: { marginTop: 8, color: '#0a6cff', fontWeight: '600' },
});
```

The app initializes tracking via `initActivityFlow` with your VTEX account name, and enables automatic page view tracking by calling `usePageViewObserver` with a `NavigationContainer` ref.

On the Ads screen, ad parameters (including the mandatory `accountName`) are passed to the AFAdsTracker wrapper, which surrounds a fully clickable child to automatically fire impression, view, and click events without manual handler wiring.

The wrapper detects clicks via `onTouchEndCapture`. If your ad interaction isn’t based on it or cannot be wrapped, [use the `useAdsTracker` hook](#using-the-useadstracker-hook) instead.

>⚠️ To use this example in your project, remember to replace accountName according to your scenario.

#### Using the useAdsTracker hook

The `useAdsTracker` hook provides more control over how events are attached. It returns handlers and a ref that you must apply manually to your components.

Use this method when:

- You cannot use an extra `<View>` to wrap your component.
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

The component's purpose is to render an advertisement within a touchable container and report three key events to the tracking system: **impression**, **view**, and **click**.
