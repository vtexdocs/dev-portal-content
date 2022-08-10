---
title: "Motorola Registration"
slug: "motorolaus-motorola-registration"
excerpt: "motorolaus.motorola-registration@0.3.3"
hidden: true
createdAt: "2022-07-05T14:55:26.984Z"
updatedAt: "2022-07-06T01:14:32.856Z"
---
Motorola Registration is a collection of components that is used to connect with Sales Force CRM.


- [Motorola Registration](#motorola-registration)
  - [Usage](#usage)
  - [Components](#components)
  - [Creating a new component](#creating-a-new-component)
    - [Project structure](#project-structure)
  - [Developing Process](#developing-process)
  - [Contributing](#contributing)

## Usage

The Registration collection uses the  `node` builder. Please refer to our [Builder](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-builders) documentation to learn more about the `node` builder. 

To use this app, you must import it as dependency of your project in the `manifest.json` file.

```json
  "dependencies": {
    "{{vendor}}.motorola-registration": "0.x"
  }
```

Then, you can start adding components to your store theme app.

> ⚠️ Warning
>
> **Please, try to use the code standarts:** Typescript, SCSS, React Hooks and Function Based Components

## Components

- [Newsletter](https://developers.vtex.com/vtex-developer-docs/docs/vtex-registration-availabilitysubscriber)


## Creating a new component

To start your development, create a new folder on react/components. That's where your source code will be stored. Also create a new tsx file on /react, this file should be used to expose your component, like:

### Project structure

Inside your `react/components/<component_name>` you should have:

- index.tsx
- README.md
- [Optional] components/
- [Optional] constants/
- [Optional] utils/
- [Optional] queries/
- [Optional] mutations/
- [Optional] styles.scss

Next, inside of `react/` folder you need to export your component, such as:

```tsx
import CustomComponent from './components/CustomComponent/index'

export default CustomComponent
```

Next, inside of `react/styles/` folder you need to create a SCSS file with the same stucture as your component and write your component styles. E.g:  Check the `CustomComponent` exemple

Also, all dependencies needed should be inserted inside the react/package.json.

## Developing Process

When developing new features you can install this app in your local theme and run `vtex link` logged in to your account. E.g: Inside this project run `vtex login motorolaglobalsandbox` , `vtex use {{YOUR_WORKSPACE}}` , `yarn sass` and  `vtex link`

## Contributing

If you want to create new components or contribute if an existing one you can develop locally and open a Merge Request.