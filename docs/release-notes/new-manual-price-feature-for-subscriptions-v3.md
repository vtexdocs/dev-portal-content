---
slug: "new-manual-price-feature-for-subscriptions-v3"
title: "New Manual Price feature for Subscriptions v3"
createdAt: 2022-05-10T20:00:04.576Z
hidden: false
type: "added"
---

You can now enable the Manual Price feature for [Subscriptions v3](https://developers.vtex.com/vtex-rest-api/docs/subscriptions-v3-migration-guide), which allows you to:

* Apply a manual price to each subscription item, instead of the current price applied.
* Maintain the same manual price for every future recurrent order from that subscription, if desired.

To make this possible, we have added an endpoint to the Subscriptions API v3:

* <span class="APIMethod APIMethod_fixedWidth APIMethod_post">post</span> [Edit Subscription Settings](https://developers.vtex.com/vtex-rest-api/reference/editsettings-1)

We also added these properties to the following endpoints:

<table>
    <thead>
        <tr>
            <th>Property name</th>
            <th>Endpoints to which the property was added</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code class="rdmd-code lang- theme-light">manualPriceAllowed</code></td>
            <td rowspan="2"><span class="APIMethod APIMethod_fixedWidth APIMethod_get">get</span>
                <a href="https: //developers.vtex.com/vtex-rest-api/reference/getsettings-1" target="_blank"
                    rel="noopener noreferrer">Get Subscription Settings</a> <br><br><span
                        class="APIMethod APIMethod_fixedWidth APIMethod_post">post</span>
                    <a href="https: //developers.vtex.com/vtex-rest-api/reference/editsettings-1" target="_blank"
                        rel="noopener noreferrer">Edit Subscription Settings</a>
            </td>
        </tr>
        <tr>
            <td><code class="rdmd-code lang- theme-light">useItemPriceFromOriginalOrder</code></td>
        </tr>
        <tr>
            <td><code class="rdmd-code lang- theme-light">manualPrice</code></td>
            <td><span class="APIMethod APIMethod_fixedWidth APIMethod_post">post</span>
                <a href="https://developers.vtex.com/vtex-rest-api/reference/post_api-rns-pub-subscriptions-id-items" target="_blank"
                    rel="noopener noreferrer">Add item to subscription</a> <br><span
                        class="APIMethod APIMethod_fixedWidth APIMethod_patch">patch</span>
                    <a href="https://developers.vtex.com/vtex-rest-api/reference/patch_api-rns-pub-subscriptions-id-items-itemid" target="_blank"
                        rel="noopener noreferrer">Edit item on subscription</a>
            </td>
        </tr>
    </tbody>
</table>

To learn more about the feature and how to enable it, please refer to the documentation below.

* [Enabling Manual Prices for Subscriptions v3](https://developers.vtex.com/vtex-rest-api/docs/enabling-manual-prices-for-subscriptions-v3) guide.
* [Subscriptions API v3 reference](https://developers.vtex.com/vtex-rest-api/reference/subscriptions-api-v3-overview).---
slug: "new-manual-price-feature-for-subscriptions-v3"
title: "New Manual Price feature for Subscriptions v3"
createdAt: 2022-05-10T17:56:31.473Z
hidden: true
type: "added"

---

You can now enable the Manual Price feature for [Subscriptions v3](https://developers.vtex.com/vtex-rest-api/docs/subscriptions-v3-migration-guide), which allows you to:

* Apply a manual price to each subscription item, instead of the current price applied.
* Maintain the same manual price for every future recurrent order from that subscription, if desired.

To make this possible, we have added an endpoint to the Subscriptions API v3:

* <span class="APIMethod APIMethod_fixedWidth APIMethod_post">post</span> [Edit Subscription Settings](https://developers.vtex.com/vtex-rest-api/reference/editsettings-1)

We also added these properties to the following endpoints:

<table>
    <thead>
        <tr>
            <th>Property name</th>
            <th>Endpoints to which the property was added</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code class="rdmd-code lang- theme-light" data-lang=""
                    name="">manualPriceAllowed</code>
            </td>
            <td rowspan="2">
                <span class="APIMethod APIMethod_fixedWidth APIMethod_get">get</span> <a
                    href="https://developers.vtex.com/vtex-rest-api/reference/getsettings-1" target="_blank"
                    rel="noopener noreferrer">Get Subscription Settings</a> <br><br>
                <span class="APIMethod APIMethod_fixedWidth APIMethod_post">post</span> <a
                    href="https://developers.vtex.com/vtex-rest-api/reference/editsettings-1" target="_blank"
                    rel="noopener noreferrer">Edit Subscription Settings</a>
            </td>
        </tr>
        <tr>
            <td><code class="rdmd-code lang- theme-light" data-lang=""
                    name="">useItemPriceFromOriginalOrder</code>
            </td>
        </tr>
        <tr>
            <td><code class="rdmd-code lang- theme-light" data-lang=""
                    name="">manualPrice</code>
            </td>
            <td>
                <span class="APIMethod APIMethod_fixedWidth APIMethod_post">post</span> <a
                    href="https://developers.vtex.com/vtex-rest-api/reference/post_api-rns-pub-subscriptions-id-items"
                    target="_blank" rel="noopener noreferrer">Add item to subscription</a> <br>
                <span class="APIMethod APIMethod_fixedWidth APIMethod_patch">patch</span> <a
                    href="https://developers.vtex.com/vtex-rest-api/reference/patch_api-rns-pub-subscriptions-id-items-itemid"
                    target="_blank" rel="noopener noreferrer">Edit item on subscription</a>
            </td>
        </tr>
    </tbody>
</table>

To learn more about the feature and how to enable it, please refer to the documentation below.

* [Enabling Manual Prices for Subscriptions v3](https://developers.vtex.com/vtex-rest-api/docs/enabling-manual-prices-for-subscriptions-v3) guide.
* [Subscriptions API v3 reference](https://developers.vtex.com/vtex-rest-api/reference/subscriptions-api-v3-overview).
