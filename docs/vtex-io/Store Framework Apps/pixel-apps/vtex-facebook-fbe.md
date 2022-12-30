---
title: "Facebook Business Extension"
slug: "vtex-facebook-fbe"
excerpt: "vtex.facebook-fbe@1.7.2"
hidden: false
createdAt: "2021-05-27T19:18:44.566Z"
updatedAt: "2022-12-14T20:30:07.485Z"
---
The [Facebook Business Extension and Conversions API app](https://apps.vtex.com/vtex-facebook-fbe/p) is the one-stop shop for merchants to easily connect their stores to Facebook services through the FBE platform. FBE stands for Facebook Business Extension and supports integration with facebook features such as [Catalog](https://developers.facebook.com/docs/marketing-api/catalog), [Facebook Pixel](https://developers.facebook.com/docs/facebook-pixel), Conversions Api, and call-to-action buttons for Facebook and Instagram pages.

## Table of Contents
  1. [Table of Contents](#table-of-contents)
  2. [Compatibility](#compatibility)
  3. [Getting Started](#getting-started)
  4. [Facebook Features](#facebook-features)
  5. [Ads Plugin](#ads-plugin)
  6. [Conversions API Integration](#conversions-api-integration)
  7. [Disconnecting from FBE](#disconnecting-from-fbe)

## Compatibility

This app is fully compatible with IO stores, and partially compatible with Legacy (or headless) stores. 

| Features               	| Legacy    | IO  |
|------------------------	|-----------|-----|
| Facebook Pixel         	| ❌         | ✅	|
| Conversions API        	| ✅        | ✅ |
| Catalog Sync           	| ✅        | ✅ 	|
| Call-To-Action Buttons 	| ✅	       | ✅ 	|

This means legacy stores need to do a few extra steps to optimize their Pixel/Conversions API setup, which is explained in the later topics of this documentation.

This app is fully compatible with the [Facebook Pixel App](https://apps.vtex.com/vtex-facebook-pixel/p). FBE detects if you've selected the same pixel and replaces the Facebook Pixel App with its own Pixel App, that is tailored to work properly with Conversions API.

This app is fully compatible with the [Facebook Connector](https://help.vtex.com/pt/tracks/integracao-com-o-facebook--7h8KvIC4DbRRc8VlyJ8PFc/5OP69kHWKca01wLH0w10jX). When you configure FBE, if you already have the catalog sync configured, the Facebook Connector won't be impacted and will keep working as usual. Otherwise, FBE automatically configures the Facebook Connector to enable Catalog synchronization with Facebook.

This app is available in all countries, as long as the used currency is supported by Facebook Ads. You can check an updated list of all supported currencies in this link: [Accepted Currencies for Facebook Ads](https://www.facebook.com/business/help/151451521590943?id=738655959856647)

## Getting Started

> ℹ️ *To configure the Facebook Business Extension and Conversions API app in the VTEX Admin, check out the documentation [Integration with Facebook Business Extension](https://help.vtex.com/en/tracks/integration-with-facebook-business-extension--2hS3ANSZ7vlHCcba4h7k8D/7JvybNGcBXxGKbVWjadKjt).*

After installing the [Facebook Business Extension and Conversions API app](https://apps.vtex.com/vtex-facebook-fbe/p), you can connect to your Facebook account through the Admin menu, under `Marketplace -> Facebook`.

Region, currency settings and the store URL will be automatically filled in but you can double check these settings and change if needed.

Store URL, region, and currency settings are saved in order to correctly fire store events such as AddToCart and Purchase, and to enable call-to-action buttons on your store's social media pages (Facebook, Instagram, etc)

![FBE Page](https://user-images.githubusercontent.com/1629129/126334878-2405d70a-6d99-4cfc-97b1-8f16973acf1e.png)

Upon clicking the `Connect with Facebook` button, a popup is shown and the user can log in to their business account and select their Facebook assets such as the business page, the Facebook pixel, and the catalog to sync with VTEX products:

![FBE Popup](https://user-images.githubusercontent.com/1629129/122405529-83c82080-cf56-11eb-811b-b3242f121318.png)

After confirming, you can check your integration status and the installed features, such as call-to-action buttons and catalog configuration:

![FBE Connected](https://user-images.githubusercontent.com/1629129/138358151-d323bf60-8da5-4300-8181-bf6d6820aa63.png)

The numbers along the statuses are the ids for your selected assets.

If you need to, you can change the integration settings by clicking on `Integration Settings`:

![Bridge Catalog](https://user-images.githubusercontent.com/1629129/122405675-9fcbc200-cf56-11eb-893e-151533c5f43c.png)

When you connect through FBE, the business manager ID and catalog ID are filled automatically since these fields are already provided by the app, so no extra steps are required here, unless you need to change the Product Display Name, Category Mapping, or the Trade Policy.

## Facebook Features
On the features card, it's possible to configure other Facebook features. Upon clicking on the "Configure Feature" button, a popup on Facebook will guide you through those extra settings:

![Call-to-Action Example](https://user-images.githubusercontent.com/1629129/122405822-beca5400-cf56-11eb-8e6d-cd7a9bc0db11.png)

These features are all provided by a custom Facebook UI and include, but are not limited to:
- **Page Surface Call to Action Button**: Adds a `Buy Now` button to your Facebook Page, which redirects to your store.
- **Instagram Call to Action Button**: Adds a `Buy Now` button to your Instagram Page, which redirects to your store.
- **Messenger Call to Action**: Adds a `Buy Now` button inside Messenger when a user is messaging the business.

### Facebook Pixel for Legacy CMS Portal (Frontend)

A [Pixel](https://developers.facebook.com/docs/meta-pixel/get-started) is a snippet of code placed on the website that allows you to measure the effectiveness of your advertising by understanding the actions people take on the website.
 
This app is fully compatible with the Facebook Pixel App. FBE detects if you've selected the same pixel and replaces the Facebook Pixel App with its own Pixel App, that is tailored to work properly with Conversions API.

Stores using our Legacy CMS need to [manually add the pixel's code](https://www.facebook.com/business/help/952192354843755) to their frontend. Once you've added the Pixel base code to your site, you can set up events to measure actions that interest you, such as making a purchase. 

Pixel code example: 
[block:code]
{
  "codes": [
    {
      "code": "  !function(f,b,e,v,n,t,s)\n  {if(f.fbq)return;n=f.fbq=function(){n.callMethod?\n  n.callMethod.apply(n,arguments):n.queue.push(arguments)};\n  if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';\n  n.queue=[];t=b.createElement(e);t.async=!0;\n  t.src=v;s=b.getElementsByTagName(e)[0];\n  s.parentNode.insertBefore(t,s)}(window, document,'script',\n  'https://connect.facebook.net/en_US/fbevents.js');\n  fbq('init', '{your-pixel-id-goes-here}');\n  fbq('track', 'PageView');",
      "language": "text"
    }
  ]
}
[/block]

After inserting the pixel’s code in the front, is required that you also use the Conversions API. The Conversions API works with the Pixel to help improve the performance and measurement of your ad campaigns.

## Ads Plugin

On the ads plugin cards, it's possible to manage your facebook ads. 

<img alt= "Ads Plugin Cards" src="https://user-images.githubusercontent.com/12246072/176775187-f48636de-8ffa-41c6-b839-18d316b15109.png" width="500px"/>

Upon clicking on the "Open Ads Insights" button, a popup will open with your ads metrics and performance. 

<img alt= "Ads Insights Modal" src="https://user-images.githubusercontent.com/12246072/176775192-a6d9059a-eb9c-46e6-a78a-03ac25298975.png" width="500px"/>

By clicking on the "Open Ads Creation" button, another popup will open with a lightweight interface for ads creation. 

<img alt= "Ads Creation Modal" src="https://user-images.githubusercontent.com/12246072/176775197-7bcbb463-6be0-4259-ad24-55ab97d16ef7.png" width="500px"/>

## Conversions API Integration

Conversions API comes with the FBE App by default. It allows firing certain events directly from VTEX servers, ensuring the relevant data reaches facebook independently from front-end implementations and/or network failures.

These are the supported events in the current version of this App:

| Event              	| Facebook Pixel (Native)  	| Conversions API    	|
|--------------------	|--------------------------	|--------------------	|
| Page View          	| ✅                        | ✅	|
| Content View       	| ✅                        | ✅ 	|
| Search             	| ✅       	               | ✅ 	|
| Add To Cart        	| ✅                        | ✅ 	|
| Initiate Checkout  	| ✅       	               | ✅ 	|
| Purchase           	| ✅                        | ✅ 	|

This integration is configured automatically upon connecting your Facebook account. The CAPI integration works on any store (Legacy/IO), be sure to follow the next steps to ensure an optimal setup for your store.

### Optimizing your Conversions API setup

First off, you may need to do some extra steps depending on your current Facebook Pixel Configuration. 

> ℹ️ **Facebook Pixel** is a piece of code for your ecommerce website that lets you measure, optimize and build audiences for your ad campaigns. When someone visits your website and takes an action (for example, buying something), the Facebook pixel is triggered and reports this action.

The table below shows if any actions are required:

| Store        	| Pixel Setup        	| Actions Required?     	|
|--------------	|--------------------	|-----------------------	|
| Legacy (CMS) 	| None               	| Yes ⚠️         	         |
| Legacy (CMS) 	| Google Tag Manager 	| Yes ⚠️         	         |
| VTEX IO      	| None               	| No ✅                   |
| VTEX IO      	| Facebook Pixel App 	| No ✅ 	                 |
| VTEX IO      	| Google Tag Manager 	| Yes ⚠️            	     |

If no actions are required, you may skip the following subtopic.

### Required actions for stores using VTEX IO

**1** - Browser events need to be fired with the correct parameters in order to promote a correct deduplication between browser and server events. In this case, we need to do this for the Purchase event.

> ℹ️ **What is Event Deduplication?** Facebook tries to deduplicate identical events sent through the Facebook pixel and the Conversions API when we work with a redundant setup. 

> ℹ️ **A redundant setup** is when you send the same events through from both a browser pixel and Conversions API. This is the default setup used by this App.

> ⚠️ **What events will I be able to configure in this step?** For now, the only supported event for this step is the Purchase event. The other 5 (PageView, ViewContent, Search, AddToCart and InitiateCheckout) are just supported by VTEX IO stores. These scripts for Legacy stores are on our implementation roadmap.

This is done through specific parameters that may be used to guarantee the events are the same. The two parameters we'll be configuring in this section are the *Event ID* and the *Event Name*.

- **Event ID**: This ID uniquely identifies an event. In our purchase event, we're going to use orderId as the Event ID.
- **Event Name**: This is the type of the event being triggered. In our purchase event, we're going to go with 'Purchase'.

**2** - Browser events must be initialized with the *external_id* parameter in order to correctly match the actor of the event (the end consumer). We'll use the *userProfileId* as the *external_id*

> ℹ️ **The userProfileId** is a unique id which represents a end consumer of a store in the VTEX platform.

In order to do all that, the following steps need to be done in **Google Tag Manager** (or your tool of choice):

#### Step 1 - Create the Trigger

You may skip this step if you already fire Purchase events through your browser Pixel.

After accessing your Google Tag Manager workspace, ensure you have a trigger for the `orderPlaced` event. This event happens in the checkout confirmation page, whenever a purchase is completed.

In order to do so, click on `Triggers` in the lateral menu:
![](https://user-images.githubusercontent.com/1629129/137395017-fbc748fa-cd86-44c4-bcdc-8c76af6a882f.png)

Create a trigger of type `Custom Event`, and set the event name to `orderPlaced`: 

![](https://user-images.githubusercontent.com/1629129/137395493-d891ebc0-34b1-4216-b95a-c6f4c8841a17.png)

Save the trigger.

#### Step 2 - Create the Tag

With your trigger configured, you need to create a tag to run the custom code required to fire the purchase event to Facebook. You can find an example implementation through the pixel snippets in the FBE App. Go to Marketplace -> Facebook on your VTEX Admin, then click on the `Purchase` button under Pixel Snippets:

![Pixel Snippets](https://user-images.githubusercontent.com/1629129/138329122-56e31139-6008-4a68-91d8-a905709905a0.png)

> ℹ️ It's important to emphasize that Pixel Snippets are only available if the Pixel Toggle is disabled. VTEX IO stores with the toggle enabled have no need for any extra configuration to have an optimal setup.

Then all you need to do for now is click the copy button:

![Code Snippet for Purchase Event](https://user-images.githubusercontent.com/1629129/138329453-b6aeef3d-aacf-4b09-86d1-e28f0c335b90.png)

This snippet contains all required parameters to correctly trigger the purchase event. **However, if you already have other kinds of customizations in your Purchase Tag, please read the next subtopic for more information about how the snippet was created so you can customize it according to your needs.**

Back on Tag Manager, create a new "Custom HTML" tag and paste the currently copied script into the HTML text box.

Click on "Triggering" and set the trigger to your "Order Placed" event:

![Configuring a trigger for the Purchase Tag](https://user-images.githubusercontent.com/1629129/138329789-006ed605-bb60-4ff0-ba48-b95e590aee50.png)

Save your new tag.

#### Step 2b - What if I already have other customizations in my Purchase Tag?

This section is for setups that already have customizations in their Purchase Tag (such as detecting different payment methods, or having additional parameters on the event payload besides `contents`, `contentId`, `contentType`, `currency`, and `value`)

Please be aware that this section is very technical since it explains in details how exactly the Tag gathers all required information to compose and send the purchase event to Facebook.

<details>
  <summary>(Click to Expand) This is the un-minified version of the Purchase Tag Snippet, explained:</summary>

```javascript
const pixelId = 111111111111 // this is your PixelId

// Function to convert an array buffer to its hexadecimal representation.
function buf2hex(buffer) {
  return Array.prototype.map
    .call(new Uint8Array(buffer), function (x) {
      return `00${x.toString(16)}`.slice(-2)
    })
    .join('')
}

// Function that hashes values before sending them to FB.
function hashSHA256(value) {
  const encoder = new TextEncoder()
  const data = value ? encoder.encode(value) : Promise.resolve(undefined)

  const hashedValue = data
    ? window.crypto.subtle.digest('SHA-256', data).then(function (f) {
        return buf2hex(f)
      })
    : Promise.resolve(undefined)

  return hashedValue
}

// This is the main Pixel Code provided by Facebook.
!(function (f, b, e, v, n, t, s) {
  if (f.fbq) return
  n = f.fbq = function () {
    n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments)
  }

  if (!f._fbq) f._fbq = n
  n.push = n
  n.loaded = !0
  n.version = '2.0'
  n.queue = []
  t = b.createElement(e)
  t.async = !0
  t.src = v
  s = b.getElementsByTagName(e)[0]
  s.parentNode.insertBefore(t, s)
})(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js')

// A small timeout of half a second is placed to ensure the fbq function is correctly loaded.
setTimeout(function () {

  // As this tag is self-containing, instead of using variables it peeks into the dataLayer by itself.
  const orderPlaced = dataLayer.find(function (d) {
    return d.event === 'orderPlaced'
  })

  // The UserProfile function retrieves the end consumer email from visitorContactInfo and calls the Checkout API to get the saved userProfile, which contains the userProfileId.
  // The userProfileId is used as the external_id which is an advanced matching parameter as described by Facebook.
  // visitorContactInfo is an array with 3 elements, composed by ['email', 'firstName', 'lastName']. We just need the email for now.
  const userProfile =
    orderPlaced &&
    orderPlaced.visitorContactInfo &&
    orderPlaced.visitorContactInfo.length > 0
      ? fetch(
          `/api/checkout/pub/profiles?email=${orderPlaced.visitorContactInfo[0]}`
        )
          // Retrieve the response text from the API call.
          .then(function (f) {
            return f.text()
          })
          // Parse the response text as an Object.
          .then(function (f) {
            return JSON.parse(f)
          })
          // The e-mail and userProfileId must be hashed before they're sent to Facebook.
          // In no circunstance these parameters can be sent openly before hashing. If that happens, FB automatically discards them.
          .then(function (f) {
            return Promise.all([
              hashSHA256(f.userProfileId),
              hashSHA256(orderPlaced.visitorContactInfo[0].toLowerCase()),
            ])
          })
      : Promise.resolve([])

  // With the userProfile in hands, we're able to compose the advancedMatchingParams
  userProfile.then(function (profileInfo) {
    const advancedMatchingParams =
      profileInfo.length == 2 && profileInfo[0] && profileInfo[1]
        ? {
            external_id: profileInfo[0],
            em: profileInfo[1],
          }
        : {}

    // This condition checks if fbq was already loaded/executed in this page.
    if (!fbq.instance.pixelsByID[pixelId]) {
      // Here we initialize the Pixel with the Advanced Matching Parameters.
      fbq('init', String(pixelId), advancedMatchingParams, { agent: 'vtex' })

      // Then we track the PageView
      fbq('track', 'PageView')
    }

    // The Event ID should always be the orderGroupId without -01, -02, etc, to match the Event ID from Conversions API.
    var substr = orderPlaced.transactionId.indexOf('-');
    var orderId = orderPlaced.transactionId.substring(0, substr > 0 ? substr : orderPlaced.transactionId.length); 

    // After that, we create the PurchaseEvent object based on the order placed.
    const eventObject = {
      value: orderPlaced.transactionTotal,
      content_type: 'product',
      currency: orderPlaced.transactionCurrency,
      content_ids: orderPlaced.transactionProducts.map(function (p) {
        return p.sku
      }),
      contents: orderPlaced.transactionProducts.map(function (p) {
        return { id: p.sku, quantity: p.quantity, price: p.sellingPrice }
      }),
    }

    // In order to ensure deduplication, we send the orderId as the eventID, and the event as 'Purchase'. 
    // This works perfectly for the purchase event since the orderId is unique.
    const eventParams = {
      eventID: orderId,
      event: 'Purchase',
    }

    // We can finally track the Purchase event
    fbq('track', 'Purchase', eventObject, eventParams)
  })
}, 500)

```
</details>


#### Step 3 - Publish your Changes

After saving your tag, you need to submit and publish your new version.

#### Step 4 - Test your Changes

You can then test your events on the Events Manager in the Facebook platform. Open the test events tab and fill in your store URL. Click on the button to open a new browser and finish a purchase in your store. All events should show up in the Test Events Tab:

![Call-to-Action Example](https://user-images.githubusercontent.com/1629129/122405892-cc7fd980-cf56-11eb-96ac-ae304d9f9edd.png)

> ℹ️ Though most of the setups use GTM to fire pixel events, it's possible to configure this using other tools. Just make sure the corresponding parameters are being sent correctly in your tool of choice.

### Configuring Conversions API for stores using our Legacy CMS (Backend)

The Conversions API is configured automatically on any IO stores, but not in Legacy CMS Portal. Therefore, it is mandatory that Legacy CMS Portal do the configuration.

#### Required actions for stores using the Legacy CMS

The event captured by the frontend will start the conversions API in the backend. Create a custom script in your store's backend to call the conversions API, following the example below.

[block:code]
{
  "codes": [
    {
      "code": "var myHeaders = new Headers();\nmyHeaders.append(\"Content-Type\", \"application/json\");\n\nvar raw = JSON.stringify({\n  \"eventName\": \"PageView\",\n  \"eventId\": \"{{eventId}}\",\n  \"eventSourceURL\": \"{{host}}\",\n  \"userAgent\": \"{{User-agent}}\",\n  \"fbpCookie\": \"{{fbpCookie}}\"\n});\n\nvar requestOptions = {\n  method: 'POST',\n  headers: myHeaders,\n  body: raw,\n  redirect: 'follow'\n};\n\nfetch(\"{{host}}/api/io/_v/facebook-fbe/event\", requestOptions)\n  .then(response => response.text())\n  .then(result => console.log(result))\n  .catch(error => console.log('error', error));",
      "language": "text",
      "name": "javacript"
    }
  ]
}
[/block]
Recommendations: 

- Make sure to use `/api/io` in the URL to proxy the app on [VTEX IO](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-what-is-vtex-io).
- The parameter `eventID` sent on the front-end and back-end must be exactly the same to promote a correct deduplication between browser and server events.

## Disconnecting from FBE

At any point in time the user can disconnect from FBE. Please note that while disconnecting revokes access from the system user created for the integration, it does not stop catalog synchronization either. In order to disable it, deactivate catalog sync on bridge (`/admin/bridge/#/settings?openConfig=facebook`) settings.

Be aware that upon disconnecting, the app will stop sending pixel events (pixel and conversions api). It will resume working as expected if you reconnect to FBE.

Previous Facebook Pixel (vtex.facebook-pixel) installations that might have been uninstalled during FBE configuration will also be reinstalled.

![FBE Uninstall](https://user-images.githubusercontent.com/1629129/122410321-3188fe80-cf5a-11eb-8896-a191a326dd11.png)