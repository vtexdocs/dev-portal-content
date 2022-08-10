---
title: "MyAccount - Portal version"
slug: "vtex-my-account-v0"
excerpt: "vtex.my-account@0.41.0"
hidden: true
createdAt: "2022-07-12T18:26:31.498Z"
updatedAt: "2022-07-12T18:26:31.498Z"
---
> Notice: React: 2.x | Pages: 0.x

[Store v2](https://github.com/vtex-apps/my-account/tree/1.x 'StoreV2 version')

## Intro

MyAccount is a canonical app built in all VTEX stores. This app serves as a hub of apps, meaning that it is the entry point for all apps that want to be available for the store's customers.

The app is responsible for handling customer's personal data such as: profile info, passwords, addresses, orders and credit cards. Orders and credit cards are responsibilities of other two apps that come per default with the MyAccount, respectively, these apps are: `vtex.my-orders-app` and `vtex.my-cards`.

## Features

This app provides a few extension points in order to allow apps to customize stores' experience as needed.

### Adding a new page to My Account

To add new pages to My Account, your app must define in it `pages.json` file the following extension points:

```json
{
  "extensions": {
    "my-account-portal/routes/{YOUR_APP}": {
      "component": "ExtensionRouter"
    }
  }
}
```

#### Creating the ExtensionRouter component

Now create a new file in the root of the "react" folder with the name "ExtensionRouter.js".

```js
import React, { Fragment } from 'react'
import { Route } from 'vtex.my-account-commons/Router'
// Your component pages
import UserSupport from './components/UserSupport'
import UserPoints from './components/UserPoints'

const ExtensionRouter = () => (
  <Fragment>
    {/* This `path` will be added at the end of the URL */}
    <Route path="/support" exact component={UserSupport} />
    <Route path="/points" exact component={UserPoints} />
  </Fragment>
)

export default ExtensionRouter
```

In this example you will have two new pages `/account/#/support` and `/account/#/points`, rendering the UserSupport and UserPoints components respectively.

### Menu

There are two ways to customize the menu of My Account:

1. Adding links to the top or bottom of the list
2. Opting-out of the menu entirely (DEPRECATED)

It's **highly recommended** that you follow the first option. The second option will make your menu out of future updates and will not create links automatically with other apps that extends My Account, like My Subscriptions, My Cards and [Customer Credit](https://github.com/vtex/customer-credit). Also this method is not supported in v1 of My Account, so don't do anything crazy here, this is not a future proof solution!

#### Adding links to the top or bottom of the list

To add links to the bottom of the menu add to your `pages.json`:

```json
{
  "extensions": {
    "my-account-portal/menu-links-after/{YOUR_APP}": {
      "component": "ExtensionLinks"
    }
  }
}
```

To add links to the top:

```json
{
  "extensions": {
    "my-account-portal/menu-links-before/{YOUR_APP}": {
      "component": "ExtensionLinks"
    }
  }
}
```

##### Creating the ExtensionLinks component

This extension point will receive a prop called `render`. You **must** call it with an array of objects with the properties `name` and `path`. This will create the link given the `name` and the `path` provided.

Example of an ExtensionLinks implementation:

```jsx
import PropTypes from 'prop-types'
import { intlShape, injectIntl } from 'react-intl'

const ExtensionLinks = ({ render, intl }) => {
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

ExtensionLinks.propTypes = {
  render: PropTypes.func.isRequired,
  intl: intlShape.isRequired,
}

export default injectIntl(ExtensionLinks)
```

#### Optin-out of the default navigation (DEPRECATED)

You can also opt-out from the default sidebar Menu implemented by this app. To do so, there are three steps: implementing your own Menu, adding your Menu to `pages.json`, and changing the settings of the "My Account - Menu" extension point.

##### Implementing your own Menu

First, make sure you use the `react-router-dom` that we export in `vtex.my-account-commons`.

Use the `Link` component from `react-router-dom` (check [React Router `Link` docs](https://reacttraining.com/react-router/web/api/Link)) to link to other pages.

You can also wrap your component with `withRouter` (check [React Router `withRouter` docs](https://reacttraining.com/react-router/web/api/withRouter)), so you can mark a link as active.

Check the example of an implementation of a custom menu:

```js
import React from 'react'
import PropTypes from 'prop-types'
import { Link, withRouter } from 'vtex.my-account-commons/Router'

function CustomMenu(props) {
  return (
    <div>
      <h4>Custom Menu</h4>
      <Link to="/profile">
        <span
          className={`bl bw2 ${
            props.location.pathname.indexOf('profile') === -1
              ? 'c-muted-1 b--transparent'
              : 'c-on-base b b--action-primary'
          }`}>
          Personal data
        </span>
      </Link>
      <br />
      <Link to="/address">
        <span
          className={`bl bw2 ${
            props.location.pathname.indexOf('address') === -1
              ? 'c-muted-1 b--transparent'
              : 'c-on-base b b--action-primary'
          }`}>
          Address
        </span>
      </Link>
    </div>
  )
}

CustomMenu.propTypes = {
  history: PropTypes.object.isRequired,
  location: PropTypes.object.isRequired,
  match: PropTypes.object.isRequired,
}

export default withRouter(CustomMenu)
```

##### Add an extension to `pages.json`

Now add this React component to the root directory of your app and reference it in the `pages.json` of your app, like so:

```json
{
  "extensions": {
    "my-account-portal/menu/customMenu": {
      "component": "CustomMenu"
    }
  }
}
```

Note that the name `CustomMenu` is the name of the React component filename.

##### Changing the extension point settings

1. Open the Storefront admin (`/admin/cms/storefront`).
2. Navigate to the My Account page
3. Click on the "My Account - Menu" extension point on the Storefront's Components menu
4. The field "Menu's Extension Point" will make My Account load the following extension point: "my-account-portal/menu/<VALUE>". So add the value `customMenu`, this will make it load the extension "my-account-portal/menu/customMenu" defined in `pages.json`.
5. Save the settings.

Now, your store will render the custom menu instead of the default menu of My Account. It's important to acknowledge that this makes your menu completely indenpendent and out of future updates.

##### Defining the default home page of My Account

After [creating a new page](#adding-a-new-page-to-my-acccount), you can define the default path that will be rendered when the user opens the URL `/account/`.

1. Open the Storefront admin (`/admin/cms/storefront`).
2. Navigate to the My Account page
3. Click on the "My Account - Home" extension point on the Storefront's Components menu
4. Fill the field "My Account's default path" to the new path

Following the previous examples, we could fill it with "/points", to open the UserPoints page.

### Display personal info

Inside the Profile page, right above the `edit` button, there is another extension point, with ID `my-account-portal/profile/display`. This one is intended for stores that collect custom data from their customers (such as their hair color or their pet's name). This extension point allows your component to display such information without breaking the page layout.

**Usage:** Your component shall not render anything: you will simply call the `render` prop with the appropriate data and it will be displayed together with the user's default information. You should pass in an array of objects containing `label` and `value` props. `label` is the name of the field you which to display (such as `Hair color`) and `value` is the value for such field (such as `brown`). Keep in mind that you must run any necessary preprocessing in your data by yourself before displaying, such as masking or localizing your texts. Also, it is up to you to fetch the data from wherever it is.

**Example**

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

### Edit personal info

If you are going to display tailored data inside your customer's profile, you probably want to edit that info too. The last extension point, `my-account/profile/input`, lets you do that. It will place whatever content you want inside the profile editing form, right above the 'toggle business fields' button, and also use functions provided by you to validate and submit that content.

**Usage:** Your component may render form components, texts or anything else as desired. We recommend sticking to VTEX's Styleguide or your own design guidelines to avoid breaking the style from the rest of the form. You also receive two props, `registerValidator` and `registerSubmitter`. As their names suggest, you must use them to register your validation and submission functions with the main component. You should use `componentDidMount` to do that. This way, when the user hits 'Submit', your validation function will be called. We then expect you to validate all of your fields and display messages to the user if necessary. If something is invalid, your function should return `false` in order to halt the submission process, and return `true` otherwise. The function may either return the boolean value directly or a `Promise` which will resolve to the appropriate boolean value. When all validation is passed, the form enters submission state. It will now send the default profile information to VTEX's databases and call your submit function so you can do the same. Do not place user interaction or anything related inside that function besides submitting, since the app will return to the display page as soon as all the submitter functions finish executing and anything you display will probably not be noticed by the user.

**Example**

```js
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
```

### Example

You can see these features in action by running `vtex link` on the `my-account-extension-example` folder.

## Author

Gustavo Silva (@akafts) during a Winter Internship at VTEX :)

Ft: Felipe Sales (@salesfelipe)