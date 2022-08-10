---
title: "Opencashback"
slug: "lemoneybr-opencashback-plugin"
excerpt: "lemoneybr.opencashback-plugin@1.3.27"
hidden: true
createdAt: "2022-07-06T17:06:25.436Z"
updatedAt: "2022-07-21T19:33:03.355Z"
---
Opencashback is an application to connect your store with Opencashback easily. It's built on top of VTEX IO and provides components to display cashback values on products, cashback inflow and outflow and it also provides APIs to perform operations on Opencashback API directly from your store.

## Guides

### App configuration

Go to your applications and open Opencashback configuration:

![ocb-app-config](../.github/images/ocb-app-config.png)

You'll need to provide the Opencashback API key and Opencashback integration key. You can contact us to provide the keys.

### Components configuration

#### **Cashback Amount**

Cashback amount is a text description provide customers data on the amount of cashback a product has to offer in your store.

![ocb-cashback-amount](../.github/images/ocb-cashback-amount.png)

1. Import the app to your theme peer dependencies in the `manifest.json` file:

```json
{
  "peerDependencies": {
    "lemoneybr.opencashback-plugin": "1.x"
  }
}
```

2. Add the `ocb-cashback-amount` block to the store product block:

```json
{
  "flex-layout.col#right-col": {
    "props": {
      "preventVerticalStretch": true,
      "rowGap": 0
    },
    "children": [
      "flex-layout.row#product-name",
      "product-rating-summary",
      "flex-layout.row#list-price-savings",
      "flex-layout.row#selling-price",
      "product-installments",
      "ocb-cashback-amount"
    ]
  }
}
```

#### **Digital wallet statement**

1. In your store create the archive `/store/plugins.json` and add:

```json
{
  "my-account-menu > my-account-link": "my-account-link.wallet-link",
  "my-account-pages > my-account-page": "my-account-page.wallet-page"
}
```

2. Create the a `wallet.jsonc` file on `store/blocks`. The final path will be `store/blocks/wallet.jsonc`

```jsonc
{
  "my-account-link.wallet-link": {
    "props": {
      "label": "Minha Carteira"
    }
  },
  "my-account-page.wallet-page": {
    "children": [
      "flex-layout.row#ocb-top",
      "flex-layout.row#ocb-middle",
      "flex-layout.row#ocb-bottom"
    ]
  },
  "flex-layout.row#ocb-top": {
    "children": ["flex-layout.col#expire-wallet-date"],
    "props": {
      "colSizing": "auto",
      "colGap": 5
    }
  },

  "flex-layout.row#ocb-middle": {
    "children": ["flex-layout.col#wallet-status", "flex-layout.col#wallet"],
    "props": {
      "colSizing": "auto",
      "colGap": 0
    }
  },

  "flex-layout.row#ocb-bottom": {
    "children": ["flex-layout.col#statement"],
    "props": {
      "colSizing": "auto",
      "colGap": 5
    }
  },
  "flex-layout.col#wallet": {
    "children": ["ocb-wallet-balance"],
    "props": {
      "blockClass": "walletContainer",
      "width": "grow"
    }
  },
  "flex-layout.col#wallet-status": {
    "children": ["ocb-wallet-status"],
    "props": {
      "blockClass": "walletContainer",
      "width": "40px"
    }
  },
  "flex-layout.col#expire-wallet-date": {
    "children": ["ocb-expire-wallet-date"],
    "props": {
      "blockClass": "expireWalletDateContainer",
      "preventVerticalStretch": true,
      "width": "grow"
    }
  },
  "flex-layout.col#statement": {
    "children": ["ocb-wallet-statement-with-cashback-status"],
    "props": {
      "blockClass": "statementContainer",
      "preventVerticalStretch": true,
      "width": "grow"
    }
  }
}
```

### Styling configuration

For minor changes you can use vtex Site Editor directly. And for colors and other CSS properties use VTEX CSSHandlers.

Create `lemoneybr.opencashback-plugin.css` on your theme under the folder `styles/css`. The final path will be `styles/css/lemoneybr.opencashback-plugin.css`.

| Component                                 |                                                                                                                         CSSHandles                                                                                                                          |
| ----------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| ocb-cashback-amount                       |                                                                                                                      `cashbackColor `                                                                                                                       |
| ocb-cashback-amount-flag-tag              |                                                                                     `tagContainer`<br/>`tagBackground`<br/>`tagFooter`<br/>`tagText`<br/>`tagCashback`                                                                                      |
| ocb-wallet-balance                        |                                                                                                 `walletContainer` <br/> `walletName` <br/> `walletBalance`                                                                                                  |
| ocb-wallet-statement                      |  `statementMessage`<br/>`statementContainer`<br/> `statementCard`<br/>`statementCard_cashback`<br/>`cashbackStatus__fulfilled`<br/>`cashbackStatus__denied` <br/> `cashbackStatus__pending` <br/> `statementCard__cashback` <br/> `statement__description`  |
| ocb-cashback-amount-minimal-tag           |                                                                          `minimalTagContainer`<br/>`minimalTagBackground`<br/>`minimalTagIconColor`<br/>`minimalTagCashback`<br/>                                                                           |
| ocb-wallet-balance-minimal-tag            |                                                                            `balanceContainer`<br />`balance`<br />`balanceText`<br /> `balanceContent`<br />`balanceIcon`<br />                                                                             |
| ocb-wallet-status                         | `walletStatusContainer`<br />`walletStatusText`<br />`walletStatus`<br />`walletStatusTooltipContainer`<br />`walletStatusTooltipColor`<br />`walletStatusBackground__`<br />`walletStatusBackground__active`<br />`walletStatusBackground__inactive`<br /> |
| ocb-wallet-statement-with-cashback-status |                                                                                                 `ocbButton`<br/>`ocbActiveButton`<br/>`ocbButtonContainer`                                                                                                  |
| ocb-expire-wallet-date                    |                                                               `walletDateContainer`<br/>`walletDateText`<br/>`walletDate`<br/>`walletDateTooltipContainer`<br/>`walletDateTooltipColor`<br/>                                                                |
| ocb-wallet-cashback-status                |                                                        `statementMessage`<br/>`statementContainer`<br/>`statementTableContainer`<br/>`statementType`<br/>`overrideTabs`<br/>`statementTypeIcon`<br/>                                                        |