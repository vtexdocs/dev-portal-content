---
title: "Aramis Store"
slug: "aramisnova-aramis-app"
excerpt: "aramisnova.aramis-app@4.0.103"
hidden: true
createdAt: "2022-07-04T19:24:59.760Z"
updatedAt: "2022-08-09T18:25:14.663Z"
---
## Start development

### GIT
**Important:** All branches needs to be created from `master` branch. Never merge `homolog` branch on `master` branch.

Follow the steps bellow to work with correct git flow for this project.

- Create your branch from `master` branch.
- The name of your branch needs to have one of the following prefixes (feature/... or bugfix/... or hotfix/...).
- Work with the best commit messages according to the [recommended structure](https://teamwork.corebiz.com.br/spaces/tribo-de-devs/page/12718-commit-structure).
- After finish your development, open a PR to `homolog` branch and send it to QA validation.
- After QA approval, open a PR to `master` branch.
- After merge your branch in `master` branch, delete your branch.

### First steps
- Clone this repository
- Run ```npm install``` or ```yarn``` on the root folder to install dependencies
- Run ```npm install -g sass``` or ```yarn global add sass```

- The **react/** and **react/components/** *.css* files are in **react/styles/** and **react/styles/components/** respectively as *.scss*.
- The **styles/css/** *.css* files are in **styles/scss/** as *.scss*

#### Watching SCSS files
- After installing all dependencies and installing sass globally, run ```npm run sass``` or ```yarn sass``` to watch your changes.