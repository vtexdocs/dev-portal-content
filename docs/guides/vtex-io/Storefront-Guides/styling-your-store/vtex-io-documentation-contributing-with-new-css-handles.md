---
title: "Contributing with new CSS Handles"
slug: "vtex-io-documentation-contributing-with-new-css-handles"
hidden: false
createdAt: "2020-06-03T16:02:44.292Z"
updatedAt: "2022-12-13T20:17:44.236Z"
seeAlso:
  - "/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization"
---

CSS Handles are CSS classes mapped to HTML elements, allowing for flexible customization of store components. The more CSS Handles available, the greater the potential for design customization.

This guide walks you through adding a new CSS Handle, using the customization of a filter on the Search Results page as an example.

## Before you begin

Before you begin, we recommend installing the [React Chrome extension](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi) to inspect the React component tree of any store page.

## Instructions

### Step 1 - Identifying the React component

1. Open the store page you are working on.
2. Right-click on the HTML element you want to customize, then select Inspect. You should see the HTML structure like the following example:

    ```html
    <div tabindex="0" role="link" class="ph5 ph3-ns pv5 pv1-ns lh-copy pointer hover-bg-muted-5 c-muted-1">Hats</div>
    ```

3. In Chrome Dev Tools, go to the `Components` tab and find the React component that wraps this element. For example, `CategoryItem`.

    ![React Component name](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-contributing-with-new-css-handles-0.png)

### Step 2 - Forking the app's repository

1. [Fork the repository](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) of the app that contains the block wrapping the HTML element you are targeting.
2. Clone the forked repository to your local files.
    
    ```
    git clone {repoUrl}
    ```
    
3. Open the project in your preferred code editor and locate the React component identified earlier (e.g., `CategoryItem.jsx`).

### Step 3 - Adding a new CSS Handle

Now, depending on how the component imports its CSS, there are two ways to add a CSS Handle:

- Using the `import {useCssHandles} from 'vtex.css-handles'` function.
- Using the `import styles from './styles.css'` function.

#### Using the `import {useCssHandles} from 'vtex.css-handles'` function

1. Locate the variable passed to the `useCssHandles` hook (e.g., `CSS_HANDLES`).
    
    ```jsx CategoryItem.jsx
    const CSS_HANDLES = ['container', 'element']
    // ...
    const handles = useCssHandles(CSS_HANDLES)
    ```
    
2. Add the new CSS Handle to the array:

    ```diff
     const CSS_HANDLES = [
       'container',
       'element',
    +  'headline',
     ]
    ```
    
    > Note that the `useCssHandles` hook will create an object where each key corresponds to the CSS Handle you defined, and the value is a unique, automatically generated CSS class name. So, `handles.container`, `handles.element`, and `handles.headline` will contain these generated class names. For a component called `foobar`, the generated class names might look like this: `vtex-foobar-1-x-container`, `vtex-foobar-1-x-element`, `vtex-foobar-1-x-headline`.

3. Apply the new CSS Handle to the desired HTML element using the `handles` variable:

    ```diff CategoryItem.jsx
    - <div className="ph0 mr2">
    + <div className={`${handles.headline} ph0 mr2`}>
    ```

4. Save your changes.

#### Using the `import styles from './styles.css'` function

1. Identify and open the CSS file imported in the component (e.g., `searchResult.css`):

    ```jsx CategoryItem.jsx
    import styles from '../searchResult.css'
    ```
    
2. Add a new class to the CSS file with the name of the new CSS Handle:

    ```css searchResult.css
    .headline {} 
    ```

3. Go back to the React component file and add the new CSS Handle to the desired HTML element. Remember to use the name of the function variable (in our example, `styles`) when adding it:

    ```diff CategoryItem.jsx
    - <div className="ph0 mr2">
    + <div className={`${styles.headline} ph0 mr2`}>
    ```

4. Save your changes.

### Step 4 - Checking your changes

1. Using the terminal and the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference), log in to a VTEX account and use a Development workspace to [link](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) the app you are working on.
2. Access the account's website through the development workspace (`{workspaceName}--{accountName}.myvtex.com`) and inspect the modified HTML element to verify if the new CSS class is being applied correctly.

Following our example, we would have something like:

```html
<div class="vtex-foobar-1-x-headline ph0 mr2">
```

### (Optional) Step 5 - Adding modifiers

To customize elements based on user interactions, you can apply modifiers to CSS Handles.

Handle modifiers work as identifiers. They are responsible for overriding the HTML element style according to the behavior assumed by them on the interface, according to user interaction.

Let's suppose you have a handle called `handles.slide` for each slide of a slider and want to customize the currently visible slide via CSS. For this purpose, you should add a modifier to `handles.slide`, allowing customization according to the user's navigation.

1. Import the `applyModifiers` method:

    `import {useCssHandles, applyModifiers} from 'vtex.css-handles'`

2. Instead of directly passing the handle, apply the `applyModifiers` method:

    ```diff
    -<div class={{`${handles.slide}`}}">...</div>
    +<div class={{`${applyModifiers(handles.slide, isCurrentSlide ? 'active' : undefined}`}}">...</div>
    ```
    
    This results in:

    ```html
    <div class="vtex-foobar-1-x-slide vtex-foobar-1-x-slide--active">...</div>
    <div class="vtex-foobar-1-x-slide">...</div>
    <div class="vtex-foobar-1-x-slide">...</div>
    ```

### Step 6 - Committing your changes

After verifying that the new CSS class is correctly rendered, follow these steps to commit and submit your updates:

1. Use Git and GitHub to create a new branch for your changes.
2. Open the `CHANGELOG.md` file and add a new entry under the `[Unreleased]` section to briefly describe your changes. For example:

    ```md
    ## [Unreleased]
    ### Added
    - New CSS Handle `headline`.
    ```
4. In the `docs` folder, update the documentation to include the new CSS Handle. Modify the **Customization** section and the **CSS Handles** table as in the example below:

    ```diff
     | CSS Handles |
     | ----------- |
     | `container` |
     | `element`   |
    +| `headline`  |
    ```
3. Commit your updates with a clear, descriptive message.
4. Push your branch to your forked repository.
5. [Open a Pull Request for the team](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork). In the Pull Request description, include a link to the development workspace where your changes can be tested. For example: `https://john--storecomponents.myvtex.com`.

After your Pull Request is reviewed and approved, your changes will be merged, making the new CSS Handle available to other users and contributing to the app's improvement.

