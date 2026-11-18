---
title: "Extending My Account"
slug: "vtex-io-extending-my-account"
excerpt: "Learn how to add custom pages, menu links, and profile fields to My Account."
hidden: false
createdAt: "2026-11-12T17:00:00.000Z"
updatedAt: "2026-11-12T17:00:00.000Z"
---

[My Account](https://developers.vtex.com/docs/apps/vtex.my-account) is the page where customers manage their personal information, addresses, orders, and credit cards in a VTEX IO store. It provides extension points to add your own pages, menu links, and profile fields.

This guide shows how to extend My Account by creating your own VTEX IO app. By the end, you'll have a custom page in My Account, reachable from a new link in its menu.

> ⚠️ VTEX doesn't offer support for a customized My Account.

## Before you begin

- [Install the VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-install) to run the commands used in this guide, such as `vtex init`, `vtex link`, and `vtex publish`.
- [Create a development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace) to test your extension without affecting your live store.

## Instructions

### Step 1 - Creating your extension app

1. If you don't have a VTEX IO app yet, create one with the `vtex init` command.
2. Open the `manifest.json` file of your app and add `vtex.my-account` and `vtex.my-account-commons` under the `dependencies` field:

   ```diff
     "dependencies": {
   +   "vtex.my-account": "1.x",
   +   "vtex.my-account-commons": "1.x"
     },
   ```

3. In the same file, add the `store` builder under the `builders` field:

   ```diff
     "builders": {
       "messages": "1.x",
       "react": "3.x",
   +   "store": "0.x"
     },
   ```

### Step 2 - Defining the interfaces and plugins

1. Create the file `store/interfaces.json` and define the interfaces for the page and the menu link:

   ```json
   {
     "my-account-link.my-app-link": {
       "component": "MyAppLink"
     },
     "my-account-page.my-app-page": {
       "component": "MyAppPage"
     }
   }
   ```

   > ⚠️ You can replace `my-app-link`, `my-app-page`, `MyAppLink`, and `MyAppPage` with names that fit your app.

2. Create the file `store/plugins.json` to plug the interfaces into My Account:

   ```json
   {
     "my-account-menu > my-account-link": "my-account-link.my-app-link",
     "my-account-pages > my-account-page": "my-account-page.my-app-page"
   }
   ```

### Step 3 - Creating the `my-account-page` component

First, create the components that your pages render. For this example, create `react/components/UserPoints.js` and `react/components/UserSupport.js` with a minimal placeholder, such as:

```js
import React from 'react'

const UserPoints = () => <div>Your points</div>

export default UserPoints
```

Use the same structure for `UserSupport.js`, changing the component name and the text.

Then, create the `MyAppPage.js` file in the root of the `react` folder with the following content:

```js
import React, { Fragment } from 'react'
import { Route } from 'vtex.my-account-commons/Router'
// Your component pages
import UserSupport from './components/UserSupport'
import UserPoints from './components/UserPoints'

const MyAppPage = () => (
  <Fragment>
    {/* This `path` will be added at the end of the URL */}
    <Route path="/support" exact component={UserSupport} />
    <Route path="/points" exact component={UserPoints} />
  </Fragment>
)

export default MyAppPage
```

This example creates two pages, `/account/#/support` and `/account/#/points`, which render the `UserSupport` and `UserPoints` components, respectively.

### Step 4 - Creating the `my-account-link` component

Create the `MyAppLink.js` file in the root of the `react` folder. This component receives a prop called `render`. Call it with an array of objects containing the `name` and `path` properties. Each object creates a link.

The following example shows a `MyAppLink` implementation:

```jsx
import PropTypes from 'prop-types'
import { intlShape, injectIntl } from 'react-intl'

const MyAppLink = ({ render, intl }) => {
  return render([
    {
      name: intl.formatMessage({ id: 'userPoints.link' }),
      path: '/points',
    },
    {
      name: intl.formatMessage({ id: 'userSupport.link' }),
      path: '/support',
    },
  ])
}

MyAppLink.propTypes = {
  render: PropTypes.func.isRequired,
  intl: intlShape.isRequired,
}

export default injectIntl(MyAppLink)
```

The component uses the `userPoints.link` and `userSupport.link` messages as link names. Add them to the files in the `messages` folder of your app, for example, in `messages/en.json`:

```json
{
  "userPoints.link": "My points",
  "userSupport.link": "Support"
}
```

Add the same keys, with translated values, to the other files in the folder, such as `es.json` and `pt.json`. Otherwise, the builder warns that the keys are missing in those languages.

The following image highlights the **My points** and **Support** links that this example adds to the My Account menu:

![extension-points](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/extension-points.png)

### Step 5 - (Optional) Displaying personal information

The Profile page has an extension point, `profile-display-container`, before the `edit` button. It accepts `profile-display` blocks and is intended for stores that collect custom information from their customers, such as hair color or pet name. This extension point allows your component to display such information without breaking the page layout.

1. Create the `react/BeautyData.js` file. You can use the [example below](#beautydata-component-code) as a starting point. The file must end with `export default BeautyData`.
2. Add the interface to `store/interfaces.json`:

   ```json
   "profile-display.beauty-data": { "component": "BeautyData" }
   ```

3. Add the plugin to `store/plugins.json`:

   ```json
   "profile-display-container > profile-display": "profile-display.beauty-data"
   ```

Your component doesn't render its own markup. Instead, it calls the `render` prop with the appropriate information, and My Account displays it together with the customer's default information. Pass in an array of objects containing the `label` and `value` props:

- `label`: Name of the field you want to display, such as `Hair color`.
- `value`: Value for that field, such as `Red`.

The following image shows the `Hair color` and `Pet name` fields displayed on the Profile page:

![hair-color-pet-name](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/hair-color-pet-name.png)

Preprocess the information before displaying it, for example, by masking or localizing the text. You're also responsible for fetching the information from its source, such as Master Data or your own API, before calling `render`.

#### `BeautyData` component code

The following example shows a component that displays custom information. The values are hardcoded for demonstration purposes only. In a real store, you can fetch them dynamically from your data source instead. For more information, see [Consuming data](https://developers.vtex.com/docs/guides/vtex-io-documentation-7-consuming-data).

```js
const BeautyData = ({ render }) => {
  return render([
    {
      label: 'Hair color',
      value: 'Red',
    },
    {
      label: 'Pet name',
      value: 'Rex',
    },
  ])
}

export default BeautyData
```

### Step 6 - (Optional) Editing personal information

If you display tailored information inside your customer's profile, you can also let them edit it. The `profile-input-container` extension point lets you do that. It accepts `profile-input` blocks, places your content inside the profile editing form, before the `Toggle business fields` button, and uses the functions you provide to validate and submit that content.

1. Add `vtex.styleguide` under the `dependencies` field of your `manifest.json` file, since the example below uses its components.
2. Create the `react/FavColor.js` file with the example below.
3. Add the interface to `store/interfaces.json`:

   ```json
   "profile-input.fav-color": { "component": "FavColor" }
   ```

4. Add the plugin to `store/plugins.json`:

   ```json
   "profile-input-container > profile-input": "profile-input.fav-color"
   ```

Your component can render form components, text, or any other content. We recommend following VTEX Styleguide or your own design guidelines to keep the form style consistent. Your component receives two props, `registerValidator` and `registerSubmitter`, which you use to add your validation and submission functions to the main component. Add them in `componentDidMount`.

When customers click `Submit`, the form works as follows:

1. My Account calls your validation function. It must validate all of your fields and display messages to the user if necessary. If something is invalid, the function must return `false` to halt the submission process. Otherwise, it must return `true`. The function can return the boolean value directly or a `Promise` that resolves to it.
2. After all validations pass, the form enters the submission state. It sends the default profile information to VTEX databases and calls your submission function so you can do the same.

Don't add user interactions to the submission function. My Account returns to the display page as soon as all the submission functions finish, so customers probably won't notice anything you display.

The following example shows a component that adds a favorite color field to the form:

```js
import React, { Component } from 'react'
import { Input } from 'vtex.styleguide'

class FavColor extends Component {
  constructor(props) {
    super(props)
    this.state = {
      color: '',
      error: null,
    }
  }

  componentDidMount() {
    this.props.registerValidator(this.validate)
    this.props.registerSubmitter(this.submit)
  }

  onChange = e => {
    this.setState({ color: e.target.value })
  }

  validate = () => {
    const { color } = this.state
    this.setState({ error: null })
    if (!color.trim()) {
      this.setState({ error: 'This field is required.' })
      return false
    }
    return true
  }

  submit = () => {
    console.log('Success! Your information is saved.')
  }

  render() {
    const { error, color } = this.state
    return (
      <div className="mb8">
        <Input
          name="color"
          label="Favorite Color"
          value={color}
          errorMessage={error}
          onChange={this.onChange}
        />
      </div>
    )
  }
}

export default FavColor
```

The following image shows the field in the profile editing form. If customers click `Submit` with the field empty, the validation function displays an error message and halts the submission:

![favorite-color](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/favorite-color.gif)

### Step 7 - Linking your app and checking the result

1. In a terminal, navigate to the root folder of your app.
2. Run `vtex link` in your development workspace.
3. Open `https://{workspace}--{accountName}.myvtex.com/account/#/points`. Replace `{workspace}` with the name of your development workspace and `{accountName}` with your VTEX account name.

The My Account menu shows the new links, and the page renders the component you defined for the `/points` path.

![your-points](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/your-points.png)

### Step 8 - (Optional) Defining the default page of My Account

You can set your new page as the page that My Account renders when customers open the URL `/account/`. This is a Site Editor setting that points to a page created by your app, so configure it only after the app is linked in Step 7.

> ⚠️ The setting is specific to each workspace. Configure it in the same development workspace where you linked your app, so you can test it there. It doesn't carry over to `master`, so after you install your app in Step 9, repeat the steps below in the `master` workspace to apply it to your live store.

1. In the VTEX Admin, go to **Storefront > Site Editor**.
2. Navigate to the My Account page.
3. Click the **My Account - Home** extension point in the Site Editor menu.
4. In the **My Account's default path** field, enter the path of the new page.
5. Save your changes.

For example, to open the `UserPoints` page from the previous steps, enter `/points`.

![default-path](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/default-path.gif)

### Step 9 - Making your app available

After validating your extension in the development workspace, make it available in your account:

1. In a terminal, navigate to the root folder of your app and run `vtex release` to create a new version of the app. For more information, see [Releasing a new app version](https://developers.vtex.com/docs/guides/vtex-io-documentation-releasing-a-new-app-version).
2. Run `vtex publish` to publish the new version. For more information, see [Publishing an app](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app).
3. Run `vtex deploy` to make the published version stable. For more information, see [Deploying the app stable version](https://developers.vtex.com/docs/guides/vtex-io-documentation-deploying-the-app-stable-version).
4. Run `vtex use master` to switch to the `master` workspace.
5. Run `vtex install {vendor}.{appName}`, replacing `{vendor}` and `{appName}` with the values defined in the `manifest.json` file of your app. For more information, see [Installing an app](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app).

The new pages and menu links are now available in the My Account of your store.
