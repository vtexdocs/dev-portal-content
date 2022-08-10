---
title: "My Account - StoreV2 version"
slug: "modeloramanow-my-account"
excerpt: "modeloramanow.my-account@1.2.9"
hidden: true
createdAt: "2022-07-06T01:46:45.563Z"
updatedAt: "2022-07-27T17:08:11.513Z"
---
> Notice: React: 3.x | Store: 0.x

[Portal](https://github.com/vtex-apps/my-account/tree/master 'Portal version')

## Intro

MyAccount is a canonical app built in all VTEX stores. This app serves as a hub of apps, meaning that it is the entry point for all apps that want to be available for the store's customers.

The app is responsible for handling customer's personal data such as: profile info, passwords, addresses, orders and credit cards. Orders and credit cards are responsibilities of other two apps that come per default with the MyAccount, respectively, these apps are: `vtex.my-orders-app` and `vtex.my-cards`.

## Features

This app provides a few extension points in order to allow apps to customize stores' experience as needed.

### Adding a new page to My Account

First, make sure you have the store-builder as a dependency in you `manifest.json`:

```diff
    "builders": {
      "messages": "1.x",
      "react": "3.x",
+     "store": "0.x"
    },
```

Now, create the file `store/interfaces.json` and define some interfaces:

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

The names `my-app-link`, `my-app-page`, `MyAppLink` and `MyAppPage` may be whatever it makes more sense for you app.

Lastly, create a `store/plugins.json` file like so:

```json
{
  "my-account-menu > my-account-link": "my-account-link.my-app-link",
  "my-account-pages > my-account-page": "my-account-page.my-app-page"
}
```

#### Creating a `my-account-page` component

Now create a new file in the root of the "react" folder with the name "MyAppPage.js".

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

In this example you will have two new pages `/account/#/support` and `/account/#/points`, rendering the UserSupport and UserPoints components respectively.

#### Creating a `my-account-link` component

This component will receive a prop called `render`. You **must** call it with an array of objects with the properties `name` and `path`. This will create the link given the `name` and the `path` provided.

Example of an MyAppLink implementation:

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

### Defining the default home page of My Account

After [creating a new page](#adding-a-new-page-to-my-acccount), you can define the default path that will be rendered when the user opens the URL `/account/`.

1. Open the Site Editor admin (`/admin/cms/site-editor`).
2. Navigate to the My Account page
3. Click on the "My Account - Home" extension point on the Site Editor's menu
4. Fill the field "My Account's default path" to the new path

Following the previous examples, we could fill it with "/points", to open the UserPoints page.

### Display personal info

Inside the Profile page, right above the `edit` button, there is another extension point. This one is intended for stores that collect custom data from their customers (such as their hair color or their pet's name). This extension point allows your component to display such information without breaking the page layout.

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

## Author

Gustavo Silva (@akafts) during a Winter Internship of 2018 at VTEX :)

Ft: Felipe Sales (@salesfelipe)