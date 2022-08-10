---
title: "Linx Integration"
slug: "usaflextatix-linx-search"
excerpt: "usaflextatix.linx-search@0.5.13"
hidden: true
createdAt: "2022-07-11T16:44:35.891Z"
updatedAt: "2022-08-01T21:33:15.654Z"
---
Vtex resolvers implementation reference: [link](https://github.com/vtex-apps/chaordic-graphql)

### Configuration
/node/api/config.ts 
``` json
{ 
  apiKey: "", 
  secretKey: ""
}
```

### JSON block to show a shelf
#### List with all features [link](https://docs.linximpulse.com/v0-api-vitrines/docs/layouts)

```json
  "list-context.linx-product-list#home-novidades": {
    "blocks": [
      "product-summary.shelf"
    ],
    "props": {
      "feature": "MostPopular",
      "position": "top", //dont use capital letters at the beginning
      "page": "home"
    },
    "children": [
      "slider-layout#linx-shelves"
    ]
  }
```

### Quantity variant component
```json
  "product-summary.shelf": {
    "children": [
      "flex-layout.row#search-product-summary-header",
      "product-summary-image",
      "quantity-variants",
      "product-summary-name",
      "product-summary-price"
    ]
  }
```

### Shelf flags
```json
  "flex-layout.row#product-summary-header": {
    "children": [
      "linx-summary-tag#small",
      "add-to-list-btn"
    ],
    "props": {
      "preserveLayoutOnMobile": true,
      "preventVerticalStretch": true
    }
  },
  "linx-summary-tag#small": {
    "props": {
      "width": 80,
      "size": 11
    }
  }
```


### Search Result
```json
  "linx-search-content": {
      "children" : [
        "search-breadcrumb",
        "linx-search-title",
        "linx-search-suggestions",
        "linx-did-you-mean",
        "linx-search-filter", 
        "linx-search-orderby"
        "linx-search-result",
        "linx-pagination",
        "not-found-content"
      ],
      "props" : {
        "maxItemsPerPage": 12,
        "context": "search"
      },
      "title": "Linx - Search Content"
  },
  "linx-search-result" : {
    "blocks": [
      "gallery"
    ]
  },
  "search-result-layout": {
    "blocks": [
      "search-result-layout.mobile"
    ],
    "props": {
      "defaultGalleryLayout": "grid"
    }
  },

  "search-result-layout.mobile": {
    "children": [
      "linx-search-content"
    ],
    "props": {
      "preventRouteChange": true
    }
  }
```

### Conditional
```json
  "conditional": {
    "children": ["rich-text"]
  },
  "rich-text": {
    "props": {
      "text": "Text that should be rendered only if not empty search"
    }
  }
```