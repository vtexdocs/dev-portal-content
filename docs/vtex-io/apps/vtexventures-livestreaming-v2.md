---
title: "Live Shopping"
slug: "vtexventures-livestreaming-v2"
excerpt: "vtexventures.livestreaming@2.12.0"
hidden: true
createdAt: "2022-08-03T21:14:28.444Z"
updatedAt: "2022-08-03T21:14:28.444Z"
---
The Live Shopping app allows businesses to broadcast live on the store website, increasing selling rates, enhancing user experience, and boosting customer interaction simultaneously and in real-time.

The app works on both devices, desktop, and mobile.

![live-streaming-web](https://user-images.githubusercontent.com/52087100/118993914-49ba2d80-b95c-11eb-9720-dc3b35de3a59.png)

![mobile-livestreaming](https://user-images.githubusercontent.com/52087100/118993920-4aeb5a80-b95c-11eb-96c1-4e292f3c8133.png)

## Installation

1. Access the [Live Shopping app page on the VTEX App Store](https://apps.vtex.com/vtexventures-livestreaming/p).
2. Click on the `Get app` button to install the app in your VTEX account.

> ⚠️ Warning
>
> Notice that this is a paid app whose subscription costs will depend on the plan that you have chosen: **Lite**, **Standard**, or **Pro**. All payment details are provided at the moment of installation. Plan pricing refers to the total monthly minutes available for you to make as many transmissions as you like within the plan's available minutes. Each plan includes a set number of minutes for a month. For more details on the plans and pricing check out the [Live Shopping App Store page](https://apps.vtex.com/liveshopping/p).

3. Once the app is successfully installed, open your account's Store Theme app using the code editor of your preference.
4. In the `manifest.json` file, add the app to the theme's peer dependencies list:

```
"peerDependencies": {
    "vtexventures.livestreaming": "0.x"
  }
```

5. Declare the Live Shopping app in the desired template. For example:

```
"store.home": {
    "blocks": [
      "livestreaming",
      "rich-text#shelf-title",
      "flex-layout.row#shelf",
      "rich-text#question",
      "rich-text#link",
      "newsletter"
    ]
  },
```

6. [Deploy your changes](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-making-your-new-app-version-publicly-available#step-6---deploying-the-app-stable-version).

Once you have deployed your changes, check out the [app's overview on VTEX Admin](#apps-overview-on-vtex-admin) and set up the app on your store's by following the instructions on the [Configuration section below.](#configuration)

## App's overview on VTEX Admin

Once you have [installed the VTEX Live Shopping app](#installation), access your store's **Admin** > **Store Setup** > **Live Shopping** > **Events** and you will see an interface as the following:

![app-overview](https://user-images.githubusercontent.com/67270558/142218027-44d00504-900f-47d7-a188-1f7a7be2f41e.png)

- **Events**: section responsible for creating new events, managing them, and tracking events' data. Check out the [Configuration section below.](#configuration) set up the app on your store's.

- **Usage**: helps you track how many Live events minutes are available and were used by your account.

> ⚠️ Warning
>
> The total amount of minutes available will depend on your chosen plan: **Lite**, **Standard**, or **Pro**. All payment details are provided at the moment of installation.


## Configuration

### Creating new events

1. Open your account Admin using your browser.
2. In the Store Setup section, access `**Live Shopping**`.
3. Click on `Events`.
4. Click on the `New` button to schedule a new live shopping on your website.

![creating-events](https://user-images.githubusercontent.com/67270558/142029782-6241d870-ce09-4912-9355-0dd94ed4848e.png)

5. Fill out the fields according to the instructions below:

- `Event Name` - The desired name for the event being created.
- `UTM Source` - The urchin tracking parameters, i.e., identification data for your URL. It enables you to track accesses and check where different traffic comes from.
- `Collection ID` - Optional field. The ID of the desired product collection to be attached to the live stream event. This feature encourages customers to add more products to the store cart.

6. Save your changes.

### Live Shopping events

![admin-events](https://user-images.githubusercontent.com/52087100/118993701-1f687000-b95c-11eb-8fa5-276426c690da.png)

1. In the events list, click on the desired event's arrow button (in the `Action` column).
2. Copy the event's ID in the `Details` section.
3. Change its status to `Live` by toggling the `Status` button.

![details](https://user-images.githubusercontent.com/52087100/119001139-17abca00-b962-11eb-951a-414492949869.png)

> ⚠️ Warning
>
> The event will take approximately 3 minutes to turn on, i.e., be live.

4. Using the admin sidebar, access `CMS` and then `**Site Editor**`.
5. Locate the Live Shopping block in your store, according to the template you have declared it, and click on it.

![site-editor-configs](https://user-images.githubusercontent.com/67270558/142052891-c08256b2-a108-4a41-819c-c780bb3aa570.png)

6. Toggle the `Show component` button to display the Live Shopping component on your store.
7. Click in **Item** and in **Events (In live)** choose the desired event. Then click on `APPLY`.
8. If desired, set a start and end date for the component display.

> ℹ️ Info
>
>  Use the Site Editor module to configure not only the live event but also texts, images, and banners to be displayed alongside it.

9. Save your changes.

#### Choosing the transmission’s Layout type

1. In the events list, click on the desired live event's arrow button (in the `Action` column).
2. In the section, **Layout Type**, choose the type of layout do you want for the Live event:
- Horizontal transmission: Recommended for desktop resolutions.
- Vertical transmission: Recommended for mobile resolutions.

### Accessing the studio to be on the live stream

1. In the events list, click on the desired live event's arrow button (in the `Action` column).
2. In the section, **Streaming Studio**, you have two buttons:
- `COPY INVITATION`: click on it and send the live event’s link to a co-host, for example, and they can enter live with you.
- `ACCESS`: Access the live event studio as the host of it.

When you click on `ACCESS`, a new window will appear redirecting you to the live studio.
	
![access](https://user-images.githubusercontent.com/67270558/142058459-817a0f59-dfec-4187-90b7-be27c355d2cb.png)

In the `Complete my profile` field, type your name and click on `CONTINUE`.
Then, the page will redirect you to the live event studios.

### Managing events' live chat

The Live Shopping app counts with a live chat, enabling your users to engage with the event and share their questions in real-time.

1. In the events list, click on the desired live event's arrow button (in the `Action` column).
2. In the `Live Chat` section, keep up with real-time comments, as well as the number of viewers and likes.

![live-chat](https://user-images.githubusercontent.com/52087100/118993865-3dce6b80-b95c-11eb-8118-74b2986f9a17.png)

3. In the `Questions` section, create questions to be displayed to the audience through the `New question` button. You can choose between quizzes and polls and define the time frame in which they will be displayed. The fetched answers will be stored in the same section.

![new-question](https://user-images.githubusercontent.com/52087100/118993903-46bf3d00-b95c-11eb-8cce-623627abfb48.png)

4. In the admin sidebar, access the `Block list of words` section.
5. Click on the `New` button to define which words will be forbidden to be displayed on the real-time chat.

![block-words](https://user-images.githubusercontent.com/67270558/142054500-692d3f98-4289-4cf5-8d84-96d676ee1dc0.png)

> ℹ️ Info
>
> This feature is helpful to block rude, politician, or non-related comments from your live stream. Notice that the added words will be applied to all events, with no exceptions.

6. Do not forget to save all of your changes during the steps.

### Showing products during the Live event

When you [create a new event](#creating-new-events), you have the option to add the ID of the desired product collection to be attached to the live stream event, and in the section **Products within collection**, you can manage which products will show during the event.

1. In the events list, click on the desired live event's arrow button (in the `Action` column).
2. In the `Products within collection` section, choose the desired products to show during the Live stream and toggle the `Actions` button.

![live-shopping-products](https://user-images.githubusercontent.com/67270558/142084543-4f0245ed-03d4-4c8d-b688-4431c6e72833.png)

### Finalising live-streamed events

1. In the events list, click on the desired live event's arrow button (in the `Action` column).
2. Change its status to `Finalized` by toggling the `Status` button.

> ⚠️ Warning
>
> The live shopping completion process may take a while. Do not close the page until the `Finalized` status is green, as shown in the image below.

![finalized-status](https://user-images.githubusercontent.com/52087100/118993844-3b6c1180-b95c-11eb-9b16-de346d4b7c43.png)

Once finished, you can request the recording of your event in **Recording the event** section and click on the button `REQUEST VIDEO`.

### Tracking events' data

1. In the events list, click on the desired event's graphic button in the `Action` column.
2. Check out the events' analytics data, as shown below:

![analytics-event](https://user-images.githubusercontent.com/52087100/118993713-21323380-b95c-11eb-83e8-a5e3059136f1.png)

## Customization

To apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles                       |
| --------------------------------- |
| `analiticsBlocksContainer`        |
| `answerContent`                   |
| `answerText`                      |
| `answerVotes`                     |
| `backgroundBlue`                  |
| `buttonContenModal`               |
| `chackIconCorner`                 |
| `chatArea`                        |
| `chatBubble`                      |
| `chatMessage`                     |
| `chatText`                        |
| `chatTextContainer`               |
| `chatTime`                        |
| `chatUser`                        |
| `container`                       |
| `graphicContainer`                |
| `graphicsArea`                    |
| `iconCorner`                      |
| `infoTimeLineContainer`           |
| `inputChat`                       |
| `itemWords`                       |
| `lifeChatContainer`               |
| `lifeChatText`                    |
| `likeIcon`                        |
| `likeIconContainer`               |
| `likesCounterContainer`           |
| `likesNumber`                     |
| `liveInfoContainer`               |
| `liveInfoEventName`               |
| `livestreamingIndicator`          |
| `loadingAnimationOne`             |
| `loadingAnimationThree`           |
| `loadingAnimationTwo`             |
| `loadingContainer`                |
| `loadingContent`                  |
| `loadingItem`                     |
| `myWishListProducts`              |
| `myWishListProductsContainer`     |
| `noVideoContainer`                |
| `noVideoText`                     |
| `productsDrawer`                  |
| `profileIcon`                     |
| `shippingTermsSocialNetworks`     |
| `stepper`                         |
| `stepperContainer`                |
| `stepperDescription`              |
| `stepperIcon`                     |
| `stepperStep`                     |
| `subContainer`                    |
| `timeContent`                     |
| `timeLineIndicatorIconCircle`     |
| `timeLineIndicatorIconContainer`  |
| `timeLineIndicatorIconLine`       |
| `timeLineIndicatorIconsContainer` |
| `videoPlayerContainer`            |
| `viewers`                         |
| `viewersContainer`                |
| `wordsContent`                    |

## Contributors ✨

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->