---
title: "Understanding ads events"
slug: "understanding-ads-events"
excerpt: "Learn how ad events are tracked, identified, and deduplicated to ensure accurate campaign measurement—covering sessions, user identification, conversion windows, and attribution rules."
hidden: false
createdAt: "2025-05-21T22:18:24.684Z"
updatedAt: "2025-05-21T22:18:24.684Z"
---

## User and session identification

All Beacon requests require specific information to accurately identify and attribute events to users and their corresponding conversions. For this purpose, we use two key concepts:

### `session_id`

The `session_id` is the user's session identifier. It has a limited lifespan and helps us determine when a user transitions from an anonymous to an identified state. It also allows us to understand how many sessions a user goes through before converting.

The `session_id` is **mandatory** in all cases—even for short-lived sessions. For example, in an offline point-of-sale (POS) conversion, you can generate a random value. For web sessions, the value should match the current user session ID. 

### `user_id`

The `user_id` is the unique identifier for a customer within your platform. It must remain consistent across all user touchpoints and sales channels.

This consistency enables us to track users who interact with an ad in one channel (e.g., online) and convert in another (e.g., offline).

The `user_id` can be sent with all events, but it is **required** only for conversion events, as this is the point where the customer must be identified.

## Event count and deduplication

**Impression**, **view**, and **click** events are **deduplicated** per user, per device, per ad. The table below summarizes how each type of event is deduplicated to ensure accurate tracking and prevent double counting:

| Event type | Deduplication window | Explanation |
|-|-|-|
| **Impression** | 1 minute | Multiple impressions of the same ad within 1 minute are counted only once. |
| **Click** | 1 hour | Repeated clicks on the same ad within 1 hour are counted only once. |
| **Conversion** | 30 days (per `order_id`) | Conversion events are always counted regardless of session or device and they don't follow deduplication rules applied to impressions and clicks. Conversion events are deduplicated based on the `order_id` within a 30-day window. <br />If a conversion with the same `order_id` is received again during this period, it will not be counted again. |

### Example 1: Same session

A user clicks on an ad at 12:00 PM on day 1 and clicks on it three more times later that day. Only the first click will be counted.

On day 2, if the same user clicks on the same ad again **before 12:00 PM** (still within the same session), no new click is counted. After 12:00 PM, a new click is counted.

### Example 2: Session change

If the user changes sessions, a new event will always be counted, regardless of the time since the last interaction.

>ℹ️ **Conversion events are always counted**, whether or not the session has changed.

## Conversion window

The conversion window (or attribution window) defines the time frame during which a user's conversion can be attributed to an ad interaction.

We currently use two main attribution models based on ad type:

### Product ads

- **Conversion window**: 7 days
- **Trigger**: User clicks on a product ad

Tracking begins only when the user clicks on a product ad. Views alone do not initiate tracking. From the moment of the click, the ad is monitored for 7 days.

### Display or video ads

- **Conversion window**: 14 days
- **Trigger**: User views the ad

As soon as a user views a display or video ad, tracking begins and continues for 14 days. If the user makes a purchase during this period, the conversion is attributed to the ad.
