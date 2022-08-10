---
title: "Modiface Frame"
slug: "ebeauty-store-components-modifaceframe"
excerpt: "ebeauty.store-components@0.0.3"
hidden: true
createdAt: "2022-07-21T13:58:59.930Z"
updatedAt: "2022-07-21T13:58:59.930Z"
---
The `modiface-frame` is the block is responsible for render VTO API in PDP page.

## Configuration

1. Import the `ebeauty.store-components` app to your theme's dependencies in the `manifest.json`, for example:

```json
{
    "dependencies": {
        "ebeauty.store-components": "0.x"
    }
}
```

2. Add the `modiface-frame` block below `store.product`. For example:

```json
{
    "store.product": {
        "blocks": ["modiface-frame"]
    }
}
```

It only works with specifics categories.