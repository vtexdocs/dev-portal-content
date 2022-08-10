---
title: "Fishbowl Integration"
slug: "rmoils-fishbowl-integration"
excerpt: "rmoils.fishbowl-integration@0.0.26"
hidden: true
createdAt: "2022-07-21T02:01:52.894Z"
updatedAt: "2022-07-21T02:01:52.894Z"
---
The Fishbowl Integration app is to export the Orders, Shipping, and Payment data to the fishbowl. This app will export the data whenever order is shipped.

## Configuration

  1. Install this app (`rmoils.fishbowl-integration`) in the desired account
  2. In your admin dashboard, go to **Apps** > **Fishbowl Integration** and input the following settings:

  - `Access Key`: Enter your AWS S3 Access Key.
  - `Secret Key`: Enter your AWS S3 Secret Key.
  - `Bucket Name`: Enter your AWS S3 Bucket Name.
  - `Folder Name`: Enter your AWS S3 Folder Name.
  - `Region`: Enter your AWS S3 Region.
  3. To use this app, you need to import it in your dependencies on `manifest.json` file:

  ```json
    "peerDependencies": {
      "rmoils.fishbowl-integration": "0.x"
    }
  ```