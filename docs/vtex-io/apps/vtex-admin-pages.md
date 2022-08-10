---
title: "VTEX Pages Admin"
slug: "vtex-admin-pages"
excerpt: "vtex.admin-pages@4.49.5"
hidden: true
createdAt: "2022-07-08T17:37:22.936Z"
updatedAt: "2022-08-03T20:03:50.293Z"
---
The Pages Admin is a platform to dynamically edit a VTEX Store, making it possible to select editable components and change its configurations adding or removing content in a straightforward way.

## Continuous Integrations

### Travis CI

[![Build Status](https://travis-ci.org/vtex-apps/pages-editor.svg?branch=master)](https://travis-ci.org/vtex-apps/pages-editor)

## How to make your Component editable

The editor supports two ways of defining an editable component, thought a static schema structure or a dynamic function, that receives data and create the schema to be displayed.

### Static Schema

Add to your component an `schema` constant, a JSON object that with the following structure:

```javascript
const schema = {
  type: 'object',
  title: 'The component title',
  properties: {
    property1: {
      type: 'string'
      title: 'Title of the property'
    },
    ...{n* properties}
  }
}
```

The property type can be: `String`, `Object` or `Number`, if `Object` it will have the same structure as the parent properties.

### Dynamic Schema

Add to your component a function `getSchema`, that will have the logic to dynamically create the schema need to build your component structure. The Page Editor will call that function each time that the page form has a change to its state, which enables to add and remove fields from the schema, like the example below.

```javascript
import { range, map, clone, indexBy, prop } from 'ramda'

const bannerStructure = {
  type: 'object',
  title: 'banner',
  properties: {
    image: {
      type: 'string',
      title: 'Banner image',
    },
    page: {
      type: 'string',
      title: 'Banner link',
    },
    targetParams: {
      type: 'object',
      title: 'Banner target params',
      properties: {
        params: {
          type: 'string',
          title: 'Params',
        },
      },
    },
  },
}

static getSchema = ({numberOfBanners}) => {
  // Do a for loop replicating the banner structure, to create n* banners
  const getRepeatedProperties = (repetition) => indexBy(prop('title'), map((index) => {
    const property = clone(bannerStructure)
    property.title = `${property.title}${index}`
    return property
  }, range(1, repetition+1)))

  // Call's the function if the numberOfBanners its passed
  const generatedSchema = numberOfBanners && getRepeatedProperties(numberOfBanners)

  /**
  * Returns a schema embedding the generated properties and the static property needed
  * to type the number of banners wanted.
  */
  return {
    type: 'object',
    properties: {
      numberOfBanners: {
        type: 'number',
        title: 'Number of banners'
      },
      ...generatedSchema
    }
  }
}
```

## Custom Content Pages

See [docs](https://github.com/vtex-apps/admin-pages/blob/master/docs/CONTENT_PAGE.md)