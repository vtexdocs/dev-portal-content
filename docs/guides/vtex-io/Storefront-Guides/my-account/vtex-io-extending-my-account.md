---
title: "Extending My Account"
slug: "vtex-io-extending-my-account"
hidden: false
createdAt: "2026-11-12T17:00:00.000Z"
updatedAt: "2026-11-12T17:00:00.000Z"
---

[My Account](https://developers.vtex.com/docs/apps/vtex.my-account) is the page where customers manage their personal information, addresses, orders, and credit cards in a VTEX IO store. It provides extension points that allow you to add your own pages, menu links, and profile fields.

This guide shows how to extend My Account by creating your own VTEX IO app. By the end, you'll have a custom page in My Account, reachable from a new link in its menu.

> ⚠️ VTEX doesn't offer support for a customized My Account.

## Before you begin

- [Install the VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-install)
- [Create a development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace)

## Instructions

### Step 1 - Create your extension app

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

### Step 2 - Define the interfaces and plugins

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

   > ⚠️ You can use any names that make sense for your app instead of `my-app-link`, `my-app-page`, `MyAppLink`, and `MyAppPage`.

2. Create the file `store/plugins.json` to plug the interfaces into My Account:

   ```json
   {
     "my-account-menu > my-account-link": "my-account-link.my-app-link",
     "my-account-pages > my-account-page": "my-account-page.my-app-page"
   }
   ```

### Step 3 - Create the `my-account-page` component

Create a new file in the root of the `react` folder named `MyAppPage.js`, with the following content:

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

In this example, you have two new pages, `/account/#/support` and `/account/#/points`, which render the `UserSupport` and `UserPoints` components, respectively.

### Step 4 - Create the `my-account-link` component

Create a new file in the root of the `react` folder named `MyAppLink.js`. This component receives a prop called `render`. You must call it with an array of objects with the `name` and `path` properties, which creates a link for each object.

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

### Step 5 - (Optional) Define the default page of My Account

You can set your new page as the page that My Account renders when customers open the URL `/account/`. To do so, follow these steps:

1. In the VTEX Admin, open the Site Editor (`/admin/cms/site-editor`).
2. Navigate to the My Account page.
3. Click the **My Account - Home** extension point in the Site Editor menu.
4. In the **My Account's default path** field, enter the path of the new page.

For example, to open the `UserPoints` page from the previous steps, enter `/points`.

### Step 6 - (Optional) Display personal info

Inside the Profile page, right above the `edit` button, there is another extension point. It is intended for stores that collect custom data from their customers, such as their hair color or their pet's name. This extension point allows your component to display such information without breaking the page layout.

Your component must not render anything. Call the `render` prop with the appropriate data, and My Account displays it together with the customer's default information. Pass in an array of objects containing the `label` and `value` props:

- `label`: Name of the field you want to display, such as `Hair color`.
- `value`: Value for that field, such as `brown`.

You must preprocess your data before displaying it, such as masking or localizing your texts. You are also responsible for fetching the data from wherever it is.

The following example shows a component that displays custom data:

```js
const BeautyData = ({ render }) => {
  return render([
    {
      label: 'Hair color',
      value: 'Red',
    },
    {
      label: 'Skin color',
      value: 'White',
    },
  ])
}
```

### Step 7 - (Optional) Edit personal info

If you display tailored data inside your customer's profile, you probably want to edit that information too. The `my-account/profile/input` extension point lets you do that. It places your content inside the profile editing form, right above the **Toggle business fields** button, and uses the functions you provide to validate and submit that content.

Your component may render form components, texts, or anything else you need. We recommend following VTEX Styleguide or your own design guidelines to avoid breaking the style of the rest of the form. Your component receives two props, `registerValidator` and `registerSubmitter`, which you use to register your validation and submission functions with the main component. Register them in `componentDidMount`.

When customers click **Submit**, the form works as follows:

1. My Account calls your validation function. It must validate all of your fields and display messages to the user if necessary. If something is invalid, the function must return `false` to halt the submission process. Otherwise, it must return `true`. The function can return the boolean value directly or a `Promise` that resolves to it.
2. After all validations pass, the form enters the submission state. It sends the default profile information to VTEX databases and calls your submission function so you can do the same.

Don't place user interaction or anything related inside the submission function, besides submitting. My Account returns to the display page as soon as all the submission functions finish, and customers probably won't notice anything you display.

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
    if (color !== 'yellow') {
      this.setState({ error: 'Your favorite color must be yellow.' })
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

### Step 8 - Link your app and check the result

1. In a terminal, navigate to the root folder of your app.
2. Run `vtex link` in your development workspace.
3. Open `https://{workspace}--{accountName}.myvtex.com/account/#/points`. Replace `{workspace}` with the name of your development workspace and `{accountName}` with your VTEX account name.

The My Account menu shows the new links, and the page renders the component you defined for the `/points` path.

### Step 9 - Make your app available

After validating your extension in the development workspace, make it available in your account:

1. In a terminal, navigate to the root folder of your app and run `vtex release` to create a new version of the app. For more information, see [Releasing a new app version](https://developers.vtex.com/docs/guides/vtex-io-documentation-releasing-a-new-app-version).
2. Run `vtex publish` to publish the new version. For more information, see [Publishing an app](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app).
3. Run `vtex deploy` to make the published version stable. For more information, see [Deploying the app stable version](https://developers.vtex.com/docs/guides/vtex-io-documentation-deploying-the-app-stable-version).
4. Run `vtex use master` to switch to the `master` workspace.
5. Run `vtex install {vendor}.{appName}`, replacing `{vendor}` and `{appName}` with the values defined in the `manifest.json` file of your app. For more information, see [Installing an app](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app).

The new pages and menu links are now available in the My Account of your store.
