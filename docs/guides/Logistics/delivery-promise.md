---
title: "Delivery Promise"
slug: "delivery-promise"
hidden: false
createdAt: "2025-09-01T16:53:51.8Z"
updatedAt: ""
excerpt: ""
---

>ℹ️ This feature is in beta, which means we are working to improve it. If you have any questions, please contact [our Support](https://help.vtex.com/en/support).

**Delivery Promise** a VTEX solution that provides accurate and reliable delivery estimates for available products based on the customer's location. It ensures that customers only see products that are in stock and can be delivered to their address or picked up at a nearby location. Using this solution, your store can make a “delivery promise” to customers for all products they view.

>ℹ️ Currently, **Delivery Promise** does not yet allow you to filter the product listing page by shipping time. To learn more about filters, see the [Available features](#available-features) section.

The content is organized as follows:

- [Available features](#available-features)
- [Advantages](#advantages)
- [Requirements and restrictions](#requirements-and-restrictions)
- [Delivery Promise for Store Framework](#delivery-promise-for-store-framework)
- [Delivery Promise for headless stores](#delivery-promise-for-headless-stores)
- [Delivery Promise for FastStore](#delivery-promise-for-faststore)
- [Learn more](#learn-more)

## Available features

When the customer provides their address, an initial selection of products is made, displaying only products that can be delivered to that location or picked up at pickup points within a radius of up to 50 km from the provided address—a limit determined by Checkout.

In addition to being able to buy all the products viewed, customers can filter the products on the product listing page to view only the results that meet certain criteria, as shown below. This allows customers to tailor their navigation experience to meet their needs:

- Products available for the desired postal code.
- Product delivery deadlines.
- Products available in stores near the customer's location.
- Faster shipping methods to deliver the order.
- [Pickup point](https://help.vtex.com/en/tutorial/pontos-de-retirada--2fljn6wLjn8M4lJHA6HP3R) where the customer wants to pick up the order.

At this stage, **Delivery Promise** allows your store's customers to filter the products displayed in the navigation by using these filters:

- **Deliver to**: Products available for delivery to the provided address.
- **Pickup**: Products available for pickup at pickup points within a radius of up to 50 km from the provided address.
- **Pickup nearby:** Products available for pickup at pickup points within a radius of up to 10 km from the provided address.
- **Pickup at {{name}}:** Products available for pickup at a given pickup point.

> The filters mentioned above are native components of Intelligent Search. If you want to develop custom components for your store, please contact your development team or an [implementation partner](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4yPqZQyj0t675QpcG7H6yl#implementation-partners).

## Advantages

**Delivery Promise** is suitable for all types of operations, as the solution provides many advantages for any business model. Learn about the store architecture requirements for participating in the current beta phase in the [Requirements and restrictions](#requirements-and-restrictions) section.

For [omnichannel](https://help.vtex.com/en/tracks/estrategias-de-comercio-unificado--3WGDRRhc3vf1MJb9zGncnv) operations, the greater the coverage of the logistics network and the number of sellers and [franchise accounts](https://help.vtex.com/en/tutorial/o-que-e-conta-franquia--kWQC6RkFSCUFGgY5gSjdl) associated with the operation, the greater the benefits. The table below shows the main advantages:

| **Advantage** | **Details** |
| :---: | :--- |
| Fewer abandoned carts | <p>Customers often abandon an order after entering their location in the cart step when they find out the products can't be shipped to their location or that the shipping time doesn't meet their expectations.</p><p>With <b>Delivery Promise</b>, the availability and delivery feasibility of each product the customer sees on the product listing page are considered based on the customer's location. In addition, shipping information is displayed from the beginning of the customer's buying journey.</p> |
| Increased product assortment on the product listing page | <p>Without <b>Delivery Promise</b>, the product assortment displayed on the product listing page may not reflect all available products from sellers due to limitations in features such as <a href="https://help.vtex.com/en/tutorial/configure-seller-regionalization--32t6wLpQCEnumoh8TjT5fw">seller regionalization</a>, <a href="https://help.vtex.com/en/tutorial/comprehensive-seller--5Qn4O2GpjUIzWTPpvLUfkI">comprehensive seller</a> and the <a href="https://help.vtex.com/en/tutorial/white-label-sellers-selection--3MemNQ4pKkWCpMdzI27AHa">seller selection algorithm</a>.</p><p>With <b>Delivery Promise</b>, the customer can view the complete product assortment of all sellers, provided that:<ul><li>Sellers are correctly configured.</li><li>Products are available in stock.</li><li>Products have a valid shipping method to the address entered by the customer.</li></ul></p> |
| Improved shopping experience | <p><b>Delivery Promise</b> promotes a better shopping experience for the customer as a whole:<ul><li>It eliminates any frustration at checkout when they find it impossible to place an order.</li><li>It allows customers to view more products.</li><li>It allows customers to browse the storefront in a way that meets their needs, whether they prioritize the type of shipment or choose to place an order in a physical store.</li></ul></p> |
| Promotion of physical stores sales | <b>Delivery Promise</b> gives customers confidence in finding certain products in physical stores, which encourages them to go to the stores and increases sales opportunities. |

## Requirements and restrictions

**Delivery Promise** requires the customer's location from the beginning of the buying journey, ensuring that only products with valid shipping methods are displayed on the product listing page. To do this, you must install [Intelligent Search](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/3qgT47zY08biLP3d5os3DG), which requires the customer's location.

To join the current phase of **Delivery Promise**, you must meet the following conditions:

- **Requirement:** Use [Intelligent Search](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/3qgT47zY08biLP3d5os3DG).
- **Requirement:** Have implemented the [Store Framework](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/67SCtUreXxKYWhZh8n0zvZ#store-framework) frontend.

>ℹ️ Check the [Delivery Promise visual library](https://www.figma.com/design/PDiXfXZOhcUrUQudSa56fz/-Public--Delivery-Promise?node-id=8001-14744&p=f&t=wbvHJWUyiGar68ag-0) with [use cases](https://www.figma.com/design/PDiXfXZOhcUrUQudSa56fz/-Public--Delivery-Promise?node-id=8001-14743&p=f&t=wbvHJWUyiGar68ag-0), [behavior specs](https://www.figma.com/design/PDiXfXZOhcUrUQudSa56fz/-Public--Delivery-Promise?node-id=8002-48329&p=f&t=wbvHJWUyiGar68ag-0) and [components](https://www.figma.com/design/PDiXfXZOhcUrUQudSa56fz/-Public--Delivery-Promise?node-id=8001-14732&p=f&t=wbvHJWUyiGar68ag-0) to better understand how to apply it to your store.

## Delivery Promise for Store Framework

When building your storefront with Store Framework, you can enable Delivery Promise components using the [Shipping Option Components](https://developers.vtex.com/docs/apps/vtex.shipping-option-components) and [Search Result](https://developers.vtex.com/docs/apps/vtex.search-result) apps.

Learn how to configure these components in the [Setting up Delivery Promise components (Beta)](https://developers.vtex.com/docs/guides/setting-up-delivery-promise-components) guide.

## Delivery Promise for headless stores

When using a headless approach in your store, you can use the [Intelligent Search API](https://developers.vtex.com/docs/api-reference/intelligent-search-api) to enable Delivery Promise. To learn how to apply it to your store, read the [Delivery Promise for headless stores (Beta)](https://developers.vtex.com/docs/guides/delivery-promise-for-headless-stores) guide.

## Delivery Promise for FastStore

When building your storefront with FastStore, you can enable Delivery Promise using hooks, filter options, and location priority. Learn how to apply it in the [Delivery Promise](https://developers.vtex.com/docs/guides/faststore/features-delivery-promise) guide.

## Learn more

- [Delivery Promise: FAQ](https://help.vtex.com/en/tutorial/delivery-promise-faq--2frHHK5uPsQrLK5XbYHALN)
