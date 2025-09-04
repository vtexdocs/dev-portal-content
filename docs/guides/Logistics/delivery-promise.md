---
title: "Delivery Promise"
slug: "delivery-promise"
hidden: false
createdAt: "2025-09-01T16:53:51.8Z"
updatedAt: ""
excerpt: "Delivery Promise helps your store show only products that can be delivered or picked up based on the customer’s location. It improves shopping experience, reduces cart abandonment, and increases product assortment visibility."
seeAlso: 
    - "https://help.vtex.com/en/tutorial/delivery-promise-faq--2frHHK5uPsQrLK5XbYHALN"
---

>ℹ️ This feature is in beta, and we are actively working to improve it. If you have any questions, please contact [our Support](https://help.vtex.com/en/support).  

**Delivery Promise** a VTEX solution that provides accurate and reliable delivery estimates for available products based on the customer's location. It ensures that customers only see products that are in stock and can be delivered to their address or picked up at a nearby location. Using this solution, your store can guarantee delivery for every product a customer sees.

The content is organized as follows:

- [Available features](#available-features)
- [Advantages](#advantages)
- [Requirements and restrictions](#requirements-and-restrictions)
- [Delivery Promise for Store Framework](#delivery-promise-for-store-framework)
- [Delivery Promise for headless stores](#delivery-promise-for-headless-stores)
- [Delivery Promise for FastStore](#delivery-promise-for-faststore)

## Available features

When the customer provides their address, an initial selection of products is made, displaying only products that can be delivered to that location or picked up at pickup points within a radius of up to 50 km from the provided address — a limit determined by Checkout.

- Products available for the desired postal code.
- Product delivery deadlines.
- Products available in stores near the customer's location.
- Faster shipping methods for order delivery.
- [Pickup point](https://help.vtex.com/en/tutorial/pickup-points--2fljn6wLjn8M4lJHA6HP3R) where the customer wants to pick up the order.

At this stage, **Delivery Promise** allows your store's customers to filter the products displayed during navigation by using these filters:

| Filter | Description | Availability |
| ----------- | ----------- | ------------- |
| **Deliver to** | Products available for delivery to the specified address. | Store Framework and FastStore (only on PLPs and search results) |
| **Pickup** | Products available for pickup at locations within up to 50 km of the specified address. | Store Framework and FastStore (only on PLPs and search results) |
| **Pickup nearby** | Products available for pickup at locations within up to 10 km of the specified address. | Store Framework and FastStore (only on PLPs and search results) |
| **Pickup at {{name}}** | Products available for pickup at a specific pickup point. | Store Framework and FastStore (only on PLPs and search results) |
| **Global filters** | All products available in the store’s navigation. | FastStore |

> The filters mentioned above are native components of Intelligent Search. If you want to develop custom components for your store, please contact your development team or an [implementation partner](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4yPqZQyj0t675QpcG7H6yl#implementation-partners).

## Advantages

**Delivery Promise** is suitable for all types of operations, as the solution provides many advantages for any business model. Learn about the store architecture requirements for participating in the current beta phase in the [Requirements and restrictions](#requirements-and-restrictions) section.

For [omnichannel](https://help.vtex.com/en/tracks/unified-commerce-strategies--3WGDRRhc3vf1MJb9zGncnv/2LGAiUnHES1enjHsfi8fI3) operations, the greater the coverage of the logistics network and the greater the number of sellers and [franchise accounts](https://help.vtex.com/en/tutorial/what-is-a-franchise-account--kWQC6RkFSCUFGgY5gSjdl) associated with the operation, the greater the benefits. The table below shows the main advantages:  

| **Advantage** | **Details** |
| :---: | :--- |
| Fewer abandoned carts | <p>Customers often abandon an order after entering their location at the cart step when they find out that the products can't be shipped to their location or that the shipping time doesn't meet their expectations.</p><p>With <b>Delivery Promise</b>, the availability and delivery feasibility of each product the customer sees on the product listing page are considered based on the customer's location. In addition, shipping information is displayed from the beginning of the customer's buying journey.</p> |
| Increased product assortment on the product listing page | <p>Without <b>Delivery Promise</b>, the product assortment displayed on the product listing page may not reflect all available products from sellers due to limitations in features such as <a href="https://help.vtex.com/en/tutorial/configure-seller-regionalization--32t6wLpQCEnumoh8TjT5fw">seller regionalization</a>, <a href="https://help.vtex.com/en/tutorial/comprehensive-seller--5Qn4O2GpjUIzWTPpvLUfkI">Comprehensive Seller</a> and the <a href="https://help.vtex.com/en/tutorial/white-label-sellers-selection--3MemNQ4pKkWCpMdzI27AHa">seller selection algorithm</a>.</p><p>With <b>Delivery Promise</b>, the customer can view the complete product assortment of all sellers, provided that:<ul><li>Sellers are correctly configured..</li><li>Products are available in stock..</li><li>Products have a valid shipping method to the address entered by the customer.</li></ul></p> |
| Improved shopping experience | <p><b>Delivery Promise</b> promotes a better shopping experience for the customer as a whole:<ul><li>It eliminates any frustration at checkout when they find it impossible to place an order.</li><li>It allows customers to view more products.</li><li>It allows customers to browse the storefront in a way that meets their needs, whether they prioritize the type of shipment or choose to place an order in a physical store.</li></ul></p> |
| Promotion of physical store sales | <b>Delivery Promise</b> gives customers confidence in finding certain products in physical stores, which encourages them to go to the stores and increases sales opportunities. |

## Requirements and restrictions

**Delivery Promise** requires the customer's location from the beginning of the buying journey, ensuring that only products with valid shipping methods are displayed on the product listing page. To join the current phase of **Delivery Promise**, you must meet the following conditions:

| Requirement | Description |  
| -------------- | ------------ |  
| Install Intelligent Search | Install the [Intelligent Search](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/3qgT47zY08biLP3d5os3DG) app in your VTEX account. This app provides advanced search capabilities for your store. |
| Install Session Manager | Install the [Session Manager](https://developers.vtex.com/docs/guides/vtex-io-documentation-collecting-user-session-data) app in your VTEX account. This app enables your store to collect user session data. |
| Build the storefront | Build your store's frontend using [Store Framework](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/67SCtUreXxKYWhZh8n0zvZ#store-framework) or [FastStore](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/67SCtUreXxKYWhZh8n0zvZ#faststore). |  

>ℹ️ Check the [Delivery Promise visual library](https://www.figma.com/design/PDiXfXZOhcUrUQudSa56fz/-Public--Delivery-Promise?node-id=8001-14744&p=f&t=wbvHJWUyiGar68ag-0) with [use cases](https://www.figma.com/design/PDiXfXZOhcUrUQudSa56fz/-Public--Delivery-Promise?node-id=8001-14743&p=f&t=wbvHJWUyiGar68ag-0), [behavior specifications](https://www.figma.com/design/PDiXfXZOhcUrUQudSa56fz/-Public--Delivery-Promise?node-id=8002-48329&p=f&t=wbvHJWUyiGar68ag-0) and [components](https://www.figma.com/design/PDiXfXZOhcUrUQudSa56fz/-Public--Delivery-Promise?node-id=8001-14732&p=f&t=wbvHJWUyiGar68ag-0) to better understand how to apply it to your store.  

## Delivery Promise for Store Framework

When building your storefront with Store Framework, you can enable Delivery Promise components using the [Shipping Option Components](https://developers.vtex.com/docs/apps/vtex.shipping-option-components) and [Search Result](https://developers.vtex.com/docs/apps/vtex.search-result) apps.

Learn how to configure these components in the [Setting up Delivery Promise components (Beta)](https://developers.vtex.com/docs/guides/setting-up-delivery-promise-components) guide.

## Delivery Promise for headless stores

When using a headless approach in your store, you can use the [Intelligent Search API](https://developers.vtex.com/docs/api-reference/intelligent-search-api) to enable Delivery Promise. To learn how to apply it to your store, read the [Delivery Promise for headless stores (Beta)](https://developers.vtex.com/docs/guides/delivery-promise-for-headless-stores) guide.

## Delivery Promise for FastStore

When building your storefront with FastStore, you can enable Delivery Promise using hooks, filter options, and location priority. Learn how to apply it in the [Delivery Promise](https://developers.vtex.com/docs/guides/faststore/features-delivery-promise) guide.
