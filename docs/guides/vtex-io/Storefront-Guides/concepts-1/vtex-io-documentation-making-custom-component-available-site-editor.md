---
title: "Making a custom component available in the Site Editor"
slug: "vtex-io-documentation-making-custom-component-available-site-editor"
hidden: false
createdAt: "2024-06-03T14:03:00.000Z"
updatedAt: "2024-06-03T14:03:00.000Z"
excerpt: "Learn how to allow component customization directly in the Site Editor."
seeAlso:
- “/docs/guides/vtex-io-documentation-react-builder”
---

To allow component customization in [Site Editor](https://help.vtex.com/en/tutorial/site-editor-overview--299Dbeb9mFczUTyNQ9xPe1?&utm_source=autocomplete), you need to define the schema for each editable property and reference these definitions in the `interfaces.json` file.

Follow the steps below to configure the schema definitions for your custom components.

## Step by step

### Step 1 - Defining your custom component

For your block to accept user customizations, you need to export the React component responsible for the block. This component includes a schema, which will allow editing directly in the Site Editor.

Follow the steps below:

1. In the `/react` root directory, create a new folder, following the pattern `react/components/{ComponentName}/index.tsx`.

Consider you want to create a component named `CustomComponent`. In this case, the folder structure is as follows:

```txt
react
 ┣ 📂 components
      ┣ 📂 CustomComponent
           ┣ index.tsx
```

2. Open the `index.tsx` file and define your custom component. Ensure you include the schema for the component, as the schema is responsible for creating the interface in the Site Editor.

   ```tsx
   import React from 'react';

   interface CustomComponentProps {
     title: string;
     subtitle: string;
   }

   const CustomComponent = ({ title, subtitle }: CustomComponentProps) => {
      return (
         <>
            <p>{title}</p>
            <p>{subtitle}</p>
         </>
      );
   };

   CustomComponent.defaultProps = {
     title: "VTEX",
     subtitle: "The Composable and Complete Commerce Platform.",
   };

   CustomComponent.schema = {
     title: 'Custom Component',
     type: 'object',
     properties: {
       title: {
         type: 'string',
         title: 'Título',
       },
       subtitle: {
         type: 'string',
         title: 'Subtítulo',
       },
     },
   };

   export default CustomComponent;
   ```

The `defaultProps` object specifies the default values for the props of the `CustomComponent`. If the user does not define props in the Site Editor, it will return the `defaultProps` values.

The `schema` object defines the structure and types of the props, allowing the component to be customized within the Site Editor.

>ℹ️ Ensure that all content schemas adhere to the [JSON Schema](https://json-schema.org/) format and are included under the definitions objects.

The JSON schema definitions provide a structured way to describe the format of data. In this case, it is defined as the expected properties and their types for title and subtitle content. These properties are defined under the `CustomComponent` definition, each with its type and title.

### Step 2 - Exporting the custom component

In the `/react` root directory, create a new file and import the custom component:

```
import CustomComponent from './components/CustomComponent';

export default CustomComponent;
```

>ℹ️ You can define your custom component directly within the `react/components/CustomComponent` folder, by creating a file named `CustomComponent.tsx`, for example. For better organization and management, especially in stores with many custom components, it is recommended to create separate folders for each component within `react/components` and then export them from individual files in the `/react` root directory.


### Step 3 - Referencing definitions within the interfaces file

Now, you need to reference your custom component in the [`interfaces.json` file](https://developers.vtex.com/docs/guides/vtex-io-documentation-interface) within the `/store` folder. This file establishes a relationship between blocks and a React component, allowing the [store builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-builder) to build the store's frontend.

Follow the steps below to declare your definitions in the `interfaces.json` file:

1. In the app's repository where you are developing your custom component, open the `interfaces.json` file within the `/store` folder.

   ```txt
   store
    ┣ 📄 interfaces.json
   ```

The schema definitions might be declared as follows:

```json
{
  "custom-component": {
    "component": "CustomComponent",
    }
}
```

>ℹ️ In the schema above, the block identifier is named `custom-component`, but you can name it anything, as long as it clearly describes the component it references.

### Step 4 - Declaring the component within a block

Consider that this custom component should be available on the store’s main page. In this case, the component must be declared within the `home` block:

```json
{
   “store.home”: {
       “blocks: [“custom-component”]
   }
}
```

After [linking the app](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app), your component will be available to visualize and test in the [development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace)’s Site Editor.

### Step 5 - Making your component available in the live store’s Site Editor

After following the guidelines above, deploy the new version of your app to make it available in the live store’s Site Editor.

Learn how to make it available in the [Deploying a new app version](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available) guide.

When the process is finished, the component will appear as follows in the live account’s Site Editor:

![Default-component](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/vtex-io/Storefront-Guides/images/default-schema.png)

## Schema use cases

You can use the following types of data to configure your schemas:

- [String](#string)
- [Boolean](#boolean)
- [Object](#object)
- [Array](#array)

### String 

Below are examples of content schemas using images and dates as props.

- **Images**

Consider a component that displays different images based on device type (desktop or mobile):

```js
function CustomComponent({ imageDesktop, imageMobile }) {
   return(
      <div>
         <img src={imageDesktop} />
         <img src={imageMobile} />
      </div>
   );
}
```

To enable users to select an image from their computer or paste an image URL link, provide options for both methods in your component’s `schema` object:

```js
CustomComponent.schema = {
   title: 'Custom Component',
   type: 'object',
   properties: {
      imageDesktop: {
         type: 'string',
         title: 'Image Desktop',
         default: '',
         description: 'Paste the URL'
      },
      imageMobile: {
         title: 'Image Mobile',
         default: '',
         type: 'string',
         widget: {//here you can choose a file in your computer
            "ui:widget": "image-uploader"
         }
      }
   }
};
```

In the Site Editor, this custom component will look like this:

![String-images](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/vtex-io/Storefront-Guides/images/string-image-custom-component.png)

- **Dates**

Consider a component that allows users to input an initial and a final date:

```js	
function CustomComponent({ initialDate, finalDate }) {
   return(
      <div>
         <p>{initialDate}</p>
         <p>{finalDate}</p>
      </div>
   );
}
```

In the `schema`, the `initialDate` and `finalDate` props define the configuration for date input fields. 

```js
CustomComponent.schema = {
   title: 'Custom Component',
   type: 'object',
   properties: {
      initialDate: {
         type: 'string',
         title: 'Initial Date',
         default: '',
         description: '{year}/{month}/{day}'
      },
      finalDate: {
         title: 'Final Date', //2022-02-23T02:20:42.074Z
         default: new Date().toISOString(), //Set current date in select input
         type: 'string', //to user select a date.
         format: 'date-time',
         widget: {
            "ui:widget": "datetime"
         }
      }
   }
};
```

The `initialDate` prop has an empty string as its default value and a description indicating the expected date format `'{year}/{month}/{day}'`. The `finalDate` prop has the default value set to the current date and time in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. It includes a custom UI widget for date-time picker, streamlining the selection of both date and time.

In the Site Editor, this component will look like this:

![String-date](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/vtex-io/Storefront-Guides/images/string-date-custom-component.png)

### Boolean

Consider a component that allows users to toggle its active or inactive state:

```js
function CustomComponent({ active }) {
  if(!active) return;

   return(
      <div>
        <h2>Now the component is active!</h2>
      </div>
   );
}
```

To allow users to activate or deactivate the component, define the `schema` as follows:

```js
CustomComponent.schema = {
   title: 'Custom Component',
   type: 'object',
   properties: {
      active: {
         type: 'boolean',
         title: 'Active Component',
         default: true,
      }
   }
};
```

The `active` prop is a boolean, meaning it can be either `true` or `false`. The default value set as `true` ensures that the component starts in an active state unless specified otherwise.

In the Site Editor, this custom component will look like this:

![Boolean](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/vtex-io/Storefront-Guides/images/boolean-custom-component.png)

### Object

Consider a component that renders an image, taking an `image` prop which includes the URL, alt text, and title.

```js
function CustomComponent({ image }) {
   return(
      <div>
        <img
          src={image.url}
          alt={image.alt}
          title={image.title}
        />
      </div>
   );
}
```

In the `schema` below, it is defined the structure of the component, specifying that it expects an `image` prop, which is an object containing `url`, `alt`, and `title` props.

```js
CustomComponent.schema = {
   title: 'Custom Component',
   type: 'object',
   properties: {
      image: {
         title: 'Image Prop',
         type: 'object',
         properties: {
            url: {
               type: 'string',
               title: 'Image URL',
               description: 'URL image'
            },
            alt: {
               type: 'string',
               title: 'Image Text Alternative',
            },
            title: {
               type: 'string',
               title: 'Attribute title',
            },
         }
      }
   }
};
```

In the Site Editor, this component will look like this:

![Object](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/vtex-io/Storefront-Guides/images/object-custom-component.png)

### Array

Consider a component where the displayed images adapt to the screen size: 

```js
function CustomComponent({ images }) {
   const isMobile = window.innerWidth < 768;

   return(
      <div>
        {
           images.map((image, index) => (
              <img
alt={image.alt}
key={index}
src={isMobile ? image.mobileSrc : image.src}
              />
           ))
        }
      </div>
   );
}
```

The component checks if the viewport width is less than 768 pixels to determine if it is a mobile view and selects the appropriate image source. It then renders the images inside a `div`, with each `img` element receiving the correct source and `alt` text based on the viewport size, ensuring each image has a unique key.

In the `schema`, the `images` prop is specified as an array of objects, ensuring it will hold multiple items. Each item within the `images` array is defined as an object with three specific props, `src`, `alt`, and `mobileSrc`.

```js
CustomComponent.schema = {
   title: 'Custom Component',
   type: 'object',
   properties: {
      images: {
         type: 'array',
         title: 'Images',
         default: [
            {
               src: '',
               alt: 'Text alternative',
               mobileSrc: ''
            }
         ],
         items: {//item configuration
            type: 'object',
            title: 'Image',
            properties: {
               src: {
                  type: 'string',
                  title: 'Image SRC',
                  description: 'Image URL [desktop]'
               },
               alt: {
                  type: 'string',
                  title: 'Image Text Alternative',
                  description: 'Image URL'
               },
               mobileSrc: {
                  type: 'string',
                  title: 'Image SRC [mobile]',
                  description: 'Image URL'
               },
            }
         }
      }
   }
};
```

In the Site Editor, this component will look like this:

![Array](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/vtex-io/Storefront-Guides/images/array-custom-component.png)

If you want to allow users to change the name of each item in the `images` array within the Site Editor, add the `__editorItemTitle` prop to the item configuration. 

```js
CustomComponent.schema = {
   title: 'Custom Component',
   type: 'object',
   properties: {
      images: {
         type: 'array',
         title: 'Images',
         default: [
            {
               src: '',
               alt: 'Text alternative',
               mobileSrc: ''
            }
         ],
         items: { //item configuration
            type: 'object',
            title: 'Image',
            properties: {
             __editorItemTitle: { // now change name is available
                  default: 'Image Item',
                  title: 'Change item name',
                  type: 'string'
               },
               src: {
                  type: 'string',
                  title: 'Image SRC',
                  description: 'Image URL [desktop]'
               },
               alt: {
                  type: 'string',
                  title: 'Image Text Alternative',
                  description: 'Image URL'
               },
               mobileSrc: {
                  type: 'string',
                  title: 'Image SRC [mobile]',
                  description: 'Image URL'
               },
            }
         }
      }
   }
};
```

In the Site Editor, this component will look like this:

![Array-item-title](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/vtex-io/Storefront-Guides/images/array-item-custom-component.png)

## `enum` and `enumNames` props

There are some props used to define a set of allowed values for a particular prop, such as `enum` and `enumNames`.

When using `enum`, the value of the prop must be one of the values in the array.

The `enumNames` prop is used in conjunction with `enum` to provide a set of human-readable names for the values specified in the `enum` array. This is particularly useful in UI components dropdowns or radio buttons where you want to display a user-friendly name instead of the actual value.

### `enum` example

Imagine you have a schema with `colors` as prop and the possible values are `red`, `blue`, or `black`.

```js
CustomComponent.schema = {
   title: 'Custom Component',
   type: 'object',
   properties: {
      colors: {
         type: 'string',
         title: 'Color',
         default: 'red',
         enum: ['red', 'blue', 'black'] // allowed values for the `colors` prop
      }
   }
};
```

In the Site Editor, you will see the component like this:

![enum](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/vtex-io/Storefront-Guides/images/enum-example.png)

### `enumNames` example

Imagine you have a schema with `colors` as prop and the possible values are `#0ff102`, `#1038c9` or `#000000`, but for the user you need to show the names `green`, `blue` or `black`, respectively.

```js
CustomComponent.schema = {
   title: 'Custom Component',
   type: 'object',
   properties: {
      colors: {
         type: 'string',
         title: 'Color',
         default: 'red',
         enumNames: ['green', 'blue', 'black'],
         enum: [`#0ff102`,`#1038c9`, `#000000`]
      }
   }
};
```

In the Site Editor, you will see this component like this:

![enumNames](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/vtex-io/Storefront-Guides/images/enum-enumname-example.png)

If the user selects the value `green`, for example, the prop returns `#0ff102`.
