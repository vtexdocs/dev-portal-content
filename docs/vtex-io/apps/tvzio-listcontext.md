---
title: "VTEX List Context"
slug: "tvzio-listcontext"
excerpt: "tvzio.listcontext@0.0.2"
hidden: true
createdAt: "2022-07-25T18:14:46.617Z"
updatedAt: "2022-07-25T18:14:46.617Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->

This app enables users to create lists of content that can be editable via Site Editor.

The only interface exposed by `vtex.list-context` is `list-context`, which is supposed to be extended by other apps that want to implement this kind of architecture.

It's important to notice that this should **not** be used directly as a block, but should be extended by other apps to create new interfaces that use this context, such as: `list-context.image-list`, implemented by `vtex.store-image` , and `list-context.product-list`, implemented by `vtex.product-summary`.

## Creating a new list-context

To extend `list-context` interface and create a new kind of list, here's what you should do:

- Choose the app you want to implement this interface on, you could create a new one or use an existing one if it's makes more sense.
- Declare a new interface in your `store/interfaces.json` file:

```json
  "list-context.image-list": {
    "component": "ImageList",
    "composition": "children",
    "allowed": "*",
    "content": {
      "properties": {
        "images": {
          "$ref": "app:vtex.store-image#/definitions/Images"
        }
      }
    }
  }
```

We recommend you to use `"composition": "children"` for this new interface so that you can compose it with other `list-context` ones.

- Implement the actual React component to be rendered by this interface:

```typescript
import { useListContext, ListContextProvider } from 'vtex.list-context'

(...)

const ImageList: StorefrontFunctionComponent<Props> = ({
  images,
  height = 420,
  children,
}) => {
  const { isMobile } = useDevice()
  const { list } = useListContext() || []

  const imageListContent = images.map(
    ({ link, image, mobileImage, description }, idx) => (
      <Image
        key={idx}
        src={isMobile && mobileImage ? mobileImage : image}
        alt={description}
        link={link}
        maxHeight={height}
        width="100%"
      />
    )
  )

  const newListContextValue = list.concat(imageListContent)

  return (
    <ListContextProvider list={newListContextValue}>
      {children}
    </ListContextProvider>
  )
}

(...)
```

Notice that this app exports a React hook and a React component: `useListContext` and `<ListContextProvider />`.
Also notice that this component should wrap its `children` a new `<ListContextProvider />` containing the new list which you just appended to.

- No make sure this component is indeed editable via Site Editor, don't forget to add a `schema` to it, such as this one from `ImageList`:

```tsx
ImageList.schema = {
  title: messages.title.id,
  description: messages.description.id,
  type: 'object',
  properties: {
    images: {
      type: 'array',
      title: 'admin/editor.image-list.images.title',
      items: {
        properties: {
          image: {
            $ref: 'app:vtex.native-types#/definitions/url',
            default: '',
            title: 'admin/editor.image-list.images.image.title',
            widget: {
              'ui:widget': 'image-uploader',
            },
          },
          mobileImage: {
            $ref: 'app:vtex.native-types#/definitions/url',
            default: '',
            title: 'admin/editor.image-list.images.mobileImage.title',
            widget: {
              'ui:widget': 'image-uploader',
            },
          },
          description: {
            $ref: 'app:vtex.native-types#/definitions/text',
            default: '',
            title: 'admin/editor.image-list.images.description.title',
          },
          link: {
            default: '',
            title: '',
            $ref: 'app:vtex.native-types#/definitions/link',
          },
        },
      },
    },
    height: {
      default: 420,
      enum: [420, 440],
      isLayout: true,
      title: messages.heightTitle.id,
      type: 'number',
    },
  },
}
```

## `list-context-renderer`

Block that renders the list present in context.

### Configuration

1. Import the `vtex.list-context` app to your theme's dependencies in the `manifest.json`;

```json
  "dependencies": {
    "vtex.list-context": "0.x"
  }
```

2. Add the block `list-context-renderer` as a children of a `list-context` block. For example:

```json
{
  "list-context.product-list#demo1": {
    "blocks": ["product-summary.shelf"],
    "children": ["list-context-renderer#wrapped"],
    "props": {
      "orderBy": "OrderByTopSaleDESC"
    }
  },
  "list-context-renderer#wrapped": {
    "props": {
      "listElement": "ul",
      "itemElement": "li"
    }
  }
}
```

| Prop name     | Type     | Description                                                              | Default value |
| ------------- | -------- | ------------------------------------------------------------------------ | ------------- |
| `listElement` | `String` | HTML element used to render the list (ex: `div`, `ul`, etc)              | `Fragment`    |
| `itemElement` | `String` | HTML element used to render the items of the list (ex: `div`, `li`, etc) | `Fragment`    |

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!