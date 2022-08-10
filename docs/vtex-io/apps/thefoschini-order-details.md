---
title: "OrderDetails"
slug: "thefoschini-order-details"
excerpt: "thefoschini.order-details@1.9.6"
hidden: true
createdAt: "2022-07-15T11:09:44.197Z"
updatedAt: "2022-07-15T13:30:38.969Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

This repository constains a few React components that are mainly used by
OrderPlaced and MyOrders to display information about orders.

In order to use the components exported by OrderDetails, you must include in your `manifest.json` file:

```json
"dependencies": {
  "vtex.order-details": "1.x",
},
```

## App customized to TFG
### Features added
- release 1.9.0 ([019e56c](https://github.com/TFG-Labs/order-details/commit/019e56cd476c7b37bc40f23d6ddec07a90449b7d))

## Exported components

### Address

This a wrapper for the `<AddressRules/>` component from `vtex.address-form` that renders a formated address. It's props are defined by the interface:

```typescript
interface Props {
  address: Address;
  pickup?: Parcel;
}
```

The `Parcel` type comes from `vtex.delivery-packages`, and the `Address` component uses the attribute:

```typescript
interface Parcel {
  ...
  pickupFriendlyName: string | null;
  ...
}
```

### Attachment and Subscription

This `Attachment` component is used for rendering attachments to `OrderItems`. It's props are defined by:

```typescript
interface Props {
  attachmentsInfo: Attachment[];
  bundleInfo: Bundle[];
  currency: string;
}

interface Bundle {
  id: string;
  attachments: Attachment[];
  name: string;
  price: number;
  quantity: number;
  imageUrl: string | null;
  measurementUnit: string;
  unitMultiplier: number;
}

interface Attachment {
  content: any;
  name: string;
}
```

The `Subscription` component is just a customized version to use when the `OrderItem` has an `Attachment` that is a subscription. It's props are different and defined by:

```typescript
interface Props {
  attachmentItem: Attachment;
}
```

### ButtonLink

This component renders a `Button` or a `ButtonWithIcon` component from `vtex.styleguide` wrapped by a `Link` component from `render-runtime`. It's props are:

```typescript
interface Props {
  to: string;
  icon?: ReactNode;
  fullWidth?: boolean;
  openNewWindow?: boolean;
  variation: string;
  children: ReactChild;
}
```

### CustomerInfo

This a wrapper for the `<ProfileRules />` component from `vtex.profile-form` that renders a formated profile. It's props are defined by the interface:

```typescript
interface Props {
  profile: ClientProfile;
}

interface ClientProfile {
  email: string;
  firstName: string | null;
  lastName: string | null;
  document: string | null;
  documentType: string | null;
  phone: string | null;
}
```

### FormattedDate and FormattedPrice

Simple components for rendering formatted dates and prices using `react-intl`. Props for `FormattedDate`:

```typescript
interface Props {
  date: string;
  style: string;
}
```

For `FormattedPrice`:

```typescript
interface Props {
  value: number;
  currency: string;
}
```

### OrderHeader

Component for rendering basic information on an order visualization, along with `OrderOptions`. It's props are defined by:

```typescript
interface Props {
  orderInfo: Order;
  takeaway?: boolean;
}
```

Notice that the `takeaway` prop is a `boolean`, and should be set to true if this order has takeaway items (from InStore).

### OrderOptions

Renders `ButtonLink`s for actions to perform on an order. It's props are defined by:

```typescript
interface Props {
  allowCancellation: boolean;
  takeaway?: boolean;
  className?: string;
  fullWidth?: boolean;
  orderId?: string;
  myAccountPath?: string;
}
```

### OrderSplitNotice

Renders a `Alert` component from `vtex.styleguide` with custom text to warn a customer that his/her order was split into multiple deliveries, pickups and takeaways. Props defined by:

```typescript
interface Props {
  deliveries: number;
  pickups: number;
  takeaways: number;
}
```

### OrderTotal

Component for rendering the total prices from an order. Props defined by:

```typescript
interface Props {
  items: OrderItem[];
  totals: OrderItemTotal[];
  orderValue: number;
  currency: string;
}

interface OrderItem {
  id: string;
  attachments: Attachment[];
  skuName: string;
  name: string;
  price: number;
  listPrice: number;
  bundleItems: Bundle[];
  isGift: boolean;
  quantity: number;
  seller: string;
  imageUrl: string;
  detailUrl: string;
  measurementUnit: string;
  unitMultiplier: number;
}

interface OrderItemTotal {
  id: string;
  name: string;
  value: number;
}

interface Bundle {
  id: string;
  attachments: Attachment[];
  name: string;
  price: number;
  quantity: number;
  imageUrl: string | null;
  measurementUnit: string;
  unitMultiplier: number;
}

interface Attachment {
  content: any;
  name: string;
}
```

### PaymentMethod

Component used to render a payment's information. Props defined by:

```typescript
interface Props {
  payment: Payment;
  transactionId: string;
  currency: string;
}

interface Payment {
  id: string;
  paymentSystem: string;
  paymentSystemName: string;
  value: number;
  lastDigits: string | null;
  group: string;
  installments: number;
  dueDate: string | null;
  url: string | null;
  bankIssuedInvoiceIdentificationNumberFormatted: string | null;
  bankIssuedInvoiceBarCodeNumber: string | null;
  bankIssuedInvoiceBarCodePNG: string | null;
}
```

### Product

Component for rendering information about a product in product list. Props defined by:

```typescript
interface Props {
  productInfo: OrderItem;
  currency: string;
}
```

### ProductImage

Component for rendering product images. Props defined by:

```typescript
interface Props {
  url: string;
  alt: string;
  ...props: any;
}
```

### ShippingHeader

Component to render basic information on shipping items, such as address to ship and receiver's name. Props defined by:

```typescript
interface Props {
  shippingData: Parcel;
  index: number;
  numPackages: number;
  giftRegistry?: GiftRegistry | null;
}

interface GiftRegistry {
  attachmentId: string;
  giftRegistryId: string;
  giftRegistryType: string;
  giftRegistryTypeName: string;
  addressId: string;
  description: string;
}
```

### StorePickUpHeader

Component to render basic information on store pickup items, such as pickup point address, receiver's name and pickup friendly name. Props defined by:

```typescript
interface Props {
  shippingData: Parcel;
  index: number;
  numPackages: number;
}
```

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles      |
| ---------------- |
| `customerInfoListContainer`   |
| `customerInfoListName`   |
| `customerInfoListEmail`   |
| `customerInfoListDocument`   |
| `customerInfoListPhone`   |
| `paymentGroup`   |
| `paymentValue`   |
| `addressContainer`   |
| `pickupFriendlyName`   |
| `updateOrderButton` |
| `myOrdersButton` |
| `cancelOrderButton` |

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/LucasCastroAcctGlobal"><img src="https://avatars0.githubusercontent.com/u/55210107?v=4" width="100px;" alt=""/><br /><sub><b>LucasCastroAcctGlobal</b></sub></a><br /><a href="https://github.com/vtex-apps/order-details/commits?author=LucasCastroAcctGlobal" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!