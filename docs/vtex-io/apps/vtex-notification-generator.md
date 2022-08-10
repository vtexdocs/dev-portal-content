---
title: "notification-generator 📚"
slug: "vtex-notification-generator"
excerpt: "vtex.notification-generator@0.6.2"
hidden: true
createdAt: "2022-07-20T13:53:24.535Z"
updatedAt: "2022-07-20T13:53:24.535Z"
---
Event listener to generate notification messages. This app is responsible for generating the notifications when releases happen! There are basically four types of release messages:

### Publish
<img src="../images/appPublished.png" alt="Girl in a jacket" width="400">

### Publish Failed
<img src="../images/appPublishFailed.png" alt="Girl in a jacket" width="300">

### Deploy
<img src="../images/appDeployed.png" alt="Girl in a jacket" width="250">

### Deprecate
<img src="../images/appDeprecated.png" alt="Girl in a jacket" width="300">

### Undeprecate
<img src="../images/appUndeprecated.png" alt="Girl in a jacket" width="300">

All this happens automatically and notifications are sent to `#vtex-io-releases` or `#vtex-io-3p-releases`. This all depends on the vendor of the app. The good news is that this is now configurable. Which means that you can also send this notifications to other channels in Slack! Here's how to do it

## Configurations 🔧
We leverage from [settings builder](https://vtex.io/docs/recipes/development/developing-service-configuration-apps/). Here we assume that you are already familiarized with it. What you need to to is to create a configuration app. The configuration must conform to this interface:

```
interface NotificationSettings {
  allSettings?: MediumSetting[]
}

interface MediumSetting {
  medium: string
  setting: SingleMediumSetting
}

type SingleMediumSetting = SlackSetting

interface SlackSetting {
  bot?: string
  channels: string[]
  filters: {
    includeAppIds: string[]
  }
}
```

For now, we only support Slack notifications (`"medium": "slack"`), but we made this app flexible enough to be easy in the future to add other mediums. One example of `configuration.json` is:

```
{
  "allSettings": [
    {
      "medium": "slack",
      "setting": {
        "bot": "test-app",
        "channels": ["bot-sandbox-test"],
        "filters": {
          "includeAppIds": ["vtex.testing-notification"]
          "releaseType": 'stable'
          "releaseStep": 'deploy'
        }
      }
    }
  ]
}
```

You can add as many `MediumSetting` as you want in this array. Let's go through each one of the keys in `SlackSetting`:
|key|type|Description|
|---|---|---|
|bot|string?|Name of the bot that was configured in settings of `slack-notification`|
|channels|string[]|List of channels that must receive the notification|
|filters|object|Filters on which notifications must be sent to these configured channels|
|includeAppIds|string[]|List of appId's in the format `<vendor>.<appName>` that will be notified in this custom channel|
|releaseType| `'stable' | 'beta' | undefined` |Type of release you want to notify. There are cases you only want notifications about stable versions|
|releaseStep| `'deploy' | 'deprecate' | 'undeprecate' | undefined` |Action that is being performed. You can filter the deploy, deprecate and undeprecate actions, or choose to generate notifications for all actions (publish, deprecate, undeprecate and deploy)|

Feel free to test new configurations for your new channels. We encourage you to also play with [the configurations of `slack-notification`](https://github.com/vtex/slack-notification/blob/master/README.md#-using-a-custom-bot)! So you can create your own bot and receive the release notifications of the apps you care about in the channel of your preference ✨

For issues or more details, please contact the dev tools team! We hope you have an awesome experience! 🚀