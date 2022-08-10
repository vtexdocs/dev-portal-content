---
title: "VTEX IO Start template"
slug: "mxmotoqa-motorola-components"
excerpt: "mxmotoqa.motorola-components@0.1.16"
hidden: true
createdAt: "2022-07-05T07:32:25.675Z"
updatedAt: "2022-08-09T14:54:48.766Z"
---
Access the VTEX IO [basic setup guide](https://vtex.io/docs/getting-started/build-stores-with-store-framework/2) and follow all the given steps.

# Git

- Este repositório usa o [GitFlow](https://danielkummer.github.io/git-flow-cheatsheet/index.html) como apoio ao fluxo de criação de branches.

#### Branches structure:

    `master` - production branch
    `develop` - development branch
    `feature/***` - new features
    `hotfix/***` - should only be created in case of high impact bugs in production and that should be fixed quickly

# Coding

Follow good code practices to keep your code clean and healthy. And whenever possible, work with native VTEX components.

- Avoid Class Components, use functional components with hooks.
- Keep your components small.
- Avoid global styles.

## Pull request validation

The PR's must be validated by a teammate and before being dipped into the homolog branch, the following points must be observed:

- Every PR must have at least one approval.
- Every PR needs to follow the Pull request template, if not, it will be automatically disapproved. The PR template is displayed to the user at the time of opening it.

## The acceptance criteria for the approval of a PR are:

- Semantic
- Good practices
- No alerts, consoles or debuggers
- Ensure readable code
- Validation of problem resolution (best approach)
- Layout validation

## SASS

- Run `npm install -g sass` or `yarn global add sass`
- Run SASS `npm run sass` ot `yarn sass`
- The **react/** and **react/components/** _.css_ files are in **react/styles/** and **react/styles/components/** respectively as _.scss_.
- The **styles/css/** _.css_ files are in **styles/scss/** as _.scss_

# Useful Commands

Log in to the VTEX environment\
`$ vtex login {accountName}`

Lists all workspaces\
`$ vtex workspace list`

Create a workspace\
`$ vtex workspace create {workspaceName}`

Delete a workspace\
`$ vtex workspace delete {workspaceName}`

Delete and recreate the workspace (use when you are having compilation problems)\
`$ vtex workspace reset {workspaceName}`

Use an existing workspace\
`$ vtex workspace use {workspaceName}`

Link in the workspace (local component)\
`$ vtex link`

Unlink the local component from the workspace\
`$ vtex unlink vendor.app-name@0.x`

Opens a tab in the linked workspace browser\
`$ vtex browse`

View current status (account, email, workspace)\
`$ vtex whoami`

# Useful links

- [Vtex CLI installation](https://vtex.io/docs/recipes/development/vtex-io-cli-installation-and-command-reference/)

- [Vtex CoreBiz Training](https://www.youtube.com/watch?v=nH16vQvD0Mg) (You must be logged in to the company email)

- [Component training](https://lab.github.com/vtex-trainings/store-framework)

- [Vtex Documentation](https://developers.vtex.com/docs)

- [Vtex support components](https://github.com/vtex-apps)