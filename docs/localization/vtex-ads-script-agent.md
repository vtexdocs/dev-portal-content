---
title: "VTEX Ads Script Agent"
slug: "vtex-ads-script-agent"
excerpt: "Learn how to implement the VTEX Ads tracking script across your site using Google Tag Manager for optimal campaign performance and audience segmentation."
hidden: false
createdAt: "2025-10-13T00:00:00.000Z"
updatedAt: "2025-10-13T00:00:00.000Z"
---

This document details the procedure for installing the **VTEX Ads** tracking script on all site pages (except checkout pages) through Google Tag Manager (GTM). Proper implementation of this script is essential for collecting navigation data that enables optimization and targeting of Retail Media campaigns.

## Data collection

The VTEX Ads script is designed to collect exclusively non-sensitive navigation data, with the objective of personalizing user experience and optimizing campaigns.

Learn more about the collected data below:

- **For off-site campaigns:**

  - `session_id`: Anonymous navigation session identifier.
  - `ad_id`: Identifier of the ad that originated the traffic.

- **For audience segmentation (Page View):**

  - `session_id`: Anonymous navigation session identifier.
  - **Page information:** URL, title (`<title>`), and description (`<meta name="description">`).

>⚠️ The script **does not collect** any personally identifiable information (PII), such as name, email, CPF, phone, address, or payment data. Data collection complies with major data protection laws.

## Script details

The script must be loaded asynchronously to avoid impacting page loading time.

**Script URL:**

```http
https://cdn.newtail.com.br/retail-media/scripts/vtexads-agent.1.0.0.js
```

## Implementation via Google Tag Manager (GTM)

To ensure the script executes as early as possible during page loading, we recommend using the **Initialization** trigger.

### Step 1: Create the custom HTML tag

1. Access your GTM container and go to the **Tags** section.
2. Click **New** to create a new tag.
3. Give the tag a recognizable name, for example: **Custom HTML - VTEX Ads Agent**.
4. Click **Tag Configuration** and select the **Custom HTML** tag type.
5. In the HTML field, insert the following code:

   ```html
   <script type="text/javascript" async src="https://cdn.newtail.com.br/retail-media/scripts/vtexads-agent.1.0.0.js"></script>
   ```

### Step 2: Configure the main trigger

1. Below the tag configuration, click **"Triggering"**.
2. Select the **"Initialization - All Pages"** trigger. This trigger ensures the script fires before most other tags, on all pages.

### Step 3: Create and add a trigger exception

To prevent the script from executing on checkout pages, we'll create an exception.

1. Still in the tag configuration, in the **"Triggering"** section, click **"Add Exception"**.
2. Click the **"+"** icon in the upper right corner to create a new exception trigger.
3. Name the trigger, for example: **"Trigger Exception - Checkout Pages"**.
4. Click **"Trigger Configuration"** and choose the **"Initialization"** type.
5. Under **"This trigger fires on"**, select **"Some Initialization Events"**.
6. Configure the condition to identify checkout pages. The condition may vary depending on your site's URL structure. Common examples:
   - `Page Path` | `contains` | `/checkout`
   - `Page URL` | `matches RegEx (ignore case)` | `/checkout/|/orderPlaced/`
7. Save the new exception trigger. It will be automatically added to your tag.

### Step 4: Save and publish

1. Save the newly created tag.
2. Submit and publish the changes in your GTM container.

## User session configuration

For the VTEX Ads platform to correctly correlate user interactions, you must specify which session identifier is used by your ecommerce.

>⚠️ **Required action:** The ecommerce team must inform the VTEX Ads team about the **name of the attribute in the `cookie` or `sessionStorage`** that stores the user's session ID.
> 
> For example: If the session ID is stored in a cookie called `vtex_session`, this information must be provided.
>
> This configuration allows the script to read the correct identifier and associate it with navigation events.
