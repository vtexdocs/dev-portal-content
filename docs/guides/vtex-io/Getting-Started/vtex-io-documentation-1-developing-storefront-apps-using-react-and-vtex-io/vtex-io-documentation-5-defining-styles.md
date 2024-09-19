---
title: "4. Defining styles"
slug: "vtex-io-documentation-5-defining-styles"
excerpt: "Learn how to define styles for your storefront components, including how to export CSS handles for further customization."
hidden: false
createdAt: "2021-03-25T20:58:44.003Z"
updatedAt: "2022-12-13T20:17:44.865Z"
category: "App Development"
seeAlso:
 - "/docs/guides/vtex-io-documentation-6-structuring-documentation"
---

Once you have defined the blocks for your theme, the next step is to consider the style you want to apply to them. This includes defining the color scheme, typography, and other design elements that will establish the visual identity of your app when it is rendered.

## Before you begin

Customizing the style in a component requires basic CSS knowledge. If you're new to CSS, we recommended checking the [documentation](https://www.w3schools.com/css/default.asp) for this language before following the instructions detailed in this article.

## Instructions

Store Framework provides three different tools for applying CSS to a storefront:

- **Tachyons** - Main option for styling components from CSS classes. It offers a wide range of pre-defined styles and enables you to customize them as needed.
- **CSS Modules** - Secondary option for styling components from CSS classes. It should only be used when the desired style cannot be achieved with Tachyons.
- **CSS handles** - This option exports generic CSS classes that allow users that work with your component to customize it according to their individual needs.

Now that you know the various styling option available on the platform, it is time to delve deeper into each of them and explore their features and functionalities. Below you will find detailed instructions on how to work with each of them.

### Using Tachyons

VTEX Tachyons is a functional CSS structure built on [Tachyons](https://tachyons.io/). VTEX Tachyons offers single-purpose CSS classes that can be combined to create complex layouts and responsive components for your storefront app.

> ℹ️ To better understand VTEX Tachyons tokens for CSS classes, it is important to familiarize yourself with the underlying Tachyons framework. We highly recommend carefully reading through Tachyons [documentation](https://tachyons.io/#getting-started) to learn more about this solution.

1. Open your app code in your code editor.
2. In the `react` folder, access the file created for the component you want to style.
3. Check the [VTEX Tachyons documentation](https://vtex.github.io/vtex-tachyons/) and look for the most appropriate CSS classes for the customization you want to apply.
4. In the React component code, declare the desired CSS classes. For example:

  ```tsx
  const Example = () => (
    <div className="flex justify-center pv4 ph3 bg-base--inverted">
      <p>Hello, World!</p>
    </div>
  )
  ```

5. Save your changes.

### Using CSS Modules

CSS Modules is a tool for defining CSS classes within a separate CSS file that is scoped to the storefront app exporting the component. In this regard, the use of CSS Modules may be limiting when it comes to importing and exporting components between different apps. Thus, it is recommended to use VTEX Tachyons as the primary CSS styling tool in your project. CSS Modules should only be used when the desired style cannot be achieved using Tachyons.

>⚠️ Keep in mind that using CSS Modules should be avoided whenever possible in favor of VTEX Tachyons. This will ensure greater compatibility and flexibility when importing and exporting components between different storefront apps.

1. In your app's `react` folder, create the `styles.css` file.
2. In this file, create the desired CSS classes (the ones not understood by Tachyons tokens). For example:

 ```css
 .myButton {
    background-color: red;
 }
 ```

3. In the `react` folder, access the component file being customized and import the `styles` file created in step 1. For example:

  ```tsx
  import styles from './styles.css'
  ```

4. You can also import the `styles` file so that the generated CSS classes are private; that is, they are generated with a unique identifier (*hash*) instead of the traditional `vendor-app-major-x-format-classname`. For this, you need to do an import following the model below:

  ```tsx
  import styleModule from './style.module.css'
  ```

5. After this, the `styles` imported for your component will be an object whose keys will be the names of the classes you created (`className`). For example:

  ```tsx
  /* /react/MyButton.tsx */
  import styles from './styles.css'

  export default function MyButton() {
    return (
      <button className={styles.myButton}>
        My button
      </button>
    )
  }
  ```

> ℹ️ Remember that the name of the created classes will depend on the *import* model you used (step 3 or step 4 in this section).

6. Save your changes and [link](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app/) the app.

When rendered and inspected, the component will now have the following HTML structure if you chose to follow the *import* model shown in step 3:

```tsx
<button class="vtex-my-app-name-0-x-myButton">My button</button>
```

### Using CSS handles

A CSS handle is an **HTML element identifier**. Handles are useful when creating store themes, allowing your app users to apply CSS classes based on the visual identity they want.

To make handles available for future app users, add `vtex.css-handles` to the `dependencies` list in the `manifest.json` file:

```diff
  "dependencies": {
+   "vtex.css-handles": "0.x"  
  }
```

Once `vtex.css-handles` is added as a dependency, your app is ready to generate CSS handles.

However, when generating them, you will need to pay attention to how your app's React component(s) are imported and defined.

There are two possible scenarios:

- **Function components** - React components are defined in your app using a function.
- **Class components** - React components are defined in your app using a class.

#### Creating CSS handles for function components

1. In your app's `react` folder, go to the file of the React component you want.
2. Copy and paste the following code example in the file:

  ```tsx
  import { useCssHandles } from 'vtex.css-handles'

  const CSS_HANDLES = ['container', 'background', 'text', 'item'] as const
  /* Using `as const` at the end hints to Typescript that this array
  * won't change, thus allowing autocomplete and other goodies. */

  const Component: FC = () => {
    const handles = useCssHandles(CSS_HANDLES)
  ```

3. In the `CSS_HANDLES` array, replace the exemple strings with the names of the CSS handles you want. You can choose any name for the CSS handle; but, remember, your app users will use it with CSS classes to personalize HTML elements in stores. We recommend choosing intuitive names. Following the above example, the variable `(CSS_HANDLES)` will be an object using the following format:

  ```tsx
  {
    container: 'vtex-foobar-1-x-container',
    background: 'vtex-foobar-1-x-background',
    text: 'vtex-foobar-1-x-text',
    item: 'vtex-foobar-1-x-item',
  }
  ```

 > ℹ️ Note that the CSS handles generated and stored in the object follow this pattern: `vtex-{appName}-{majorVersion}-x-{handleName}`.

4. Add the new CSS handle to the desired CSS class–according to the HTML element to be customized by app users. Remember to use the `handle` variable when adding it and also the CSS handle name defined in the `CSS_HANDLES` array (like `container`). For example:

  ```tsx
      <div className={handles.container}>
        <div className={`${handles.background} bg-red`}>
          <h1 className={`${handles.text} f1 c-white`}>Hello world</h1>
          <ul>
            {['blue', 'yellow', 'green'].map(color => (
              <li
                className={`${handles.item} bg-${color}`}>
                Color {color}
              </li>
            ))}
          </ul>
        </div>
      </div>
  ```

#### Creating CSS handles for class components

1. In your app's `react` folder, go to the file of the React component you want.
2. Copy and paste the following code example in the file:

  ```tsx
  import { withCssHandles } from 'vtex.css-handles'

  const CSS_HANDLES = ['text'] as const

  class ExampleComponent extends Component {
    render() {
      const { cssHandles } = this.props
  ```

 > ℹ️ Since components defined as classes cannot use *hooks*, we will use an HOC called `withCssHandles`.

3. In the `CSS_HANDLES` array, replace the example strings with the names of the CSS handles you want. You can choose any name for the CSS handle; but, remember, your app users will use it with CSS classes to personalize HTML elements. We recommend using intuitive names.

Following the above example, the variable `{ cssHandles }` will be an object using the following format:

  ```tsx
  {
    text: 'vtex-foobar-1-x-text',
  }
  ```

  > ℹ️ Note that the CSS handles generated and stored in the object follow this pattern: `vtex-{appName}-{majorVersion}-x-{handleName}`.

4. Add the new CSS handle to the desired CSS class–according to the HTML element to be customized by app users. Remember to use the `handle` variable when adding it, as well as the CSS handle name defined in the `CSS_HANDLES` array (like `text`). For example:

  ```tsx
  <div className={`${cssHandles.text} f1 c-white`}>Hello world</div>
  ```

After saving your changes, your app will be able to not only export a predefined style based on the CSS classes you set up but also export CSS handles, giving your users more customization flexibility.

> ℹ️ Learn more about how CSS handles can be used to define styles in [Using CSS handles for store customization](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization).