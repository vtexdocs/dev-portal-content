---
title: "Tracking"
slug: "tracking-1"
hidden: false
createdAt: "2021-04-29T19:54:42.684Z"
updatedAt: "2021-04-29T21:34:34.573Z"
---
Access the [boilerplate repository for the tracking app](https://github.com/vtex-apps/carrier-hubs-examples/tree/main/carrier-tracking-example) to clone it and begin development.

A tracking app published by a carrier will include an endpoint like this one:
`https://app.io.vtex.com/{app_name}/{app_version}/{account}/{workspace}/tracking`

Once every hour, the VTEX tracking hub makes a `POST` request to this endpoint containing a list of packages’ tracking numbers. The app should respond with the updated tracking information for each package.

Below are some examples, but you can learn more about this request on the [tracking API request documentation](https://developers.vtex.com/vtex-developer-docs/reference/vtex-log-tracking-app).

Request body example:
```json
[
  {
    "trackingNumber": "BR000000000"
  }
]
```

Response body example:

```json
{
  &lt;trackingNumber>: {
    "deliveredDate": Date,
    "events": [
      {
        "city": string,
        "date": Date,
        "description": string,
        "state": string
      }
    ],
    "hasReturnedToSender": bool,
    "isDelivered": bool
  }
}
```

>⚠️ Be aware that this call may contain several package's tracking numbers, and the app should respond with tracking information for each of them.

## Learn more

See this guide on [how to develop carrier apps on VTEX IO](https://developers.vtex.com/vtex-rest-api/docs/getting-started-with-vtex-io-for-carriers). You can also learn more about the [integration flow](https://developers.vtex.com/vtex-rest-api/docs/integration-flow) and [notification](https://developers.vtex.com/vtex-rest-api/docs/notification-1) for carrier apps.