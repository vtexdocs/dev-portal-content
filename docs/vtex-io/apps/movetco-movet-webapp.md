---
title: "Movet WebApp"
slug: "movetco-movet-webapp"
excerpt: "movetco.movet-webapp@0.0.3"
hidden: true
createdAt: "2022-07-08T22:21:17.495Z"
updatedAt: "2022-07-09T02:30:47.298Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

### Storybook

We use [Storybook](https://storybook.js.org/) environment to help us build and test our components in real time. Run the command below to see the stories in http://localhost:6006/ :

```shell
yarn storybook
```

If you want to change or add stories, take a look at this [guide](https://github.com/vtex/styleguide/blob/master/.github/CONTRIBUTING.md#storybook-organization) before.

## Testing

### Developing new tests

To add tests to a component, just add a test file with the `.test.tsx` extension next to the component implementation.

Example:

```shell
react/components/origami/
├── origami.tsx
└── origami.test.tsx
```

We use [VTEX Test Tools](https://github.com/vtex/test-tools) to test our components.

### Running tests

To run the test use:

```shell
yarn test
```

You can also pass the `--watch` flag:

```shell
yarn test --watch
```

<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->