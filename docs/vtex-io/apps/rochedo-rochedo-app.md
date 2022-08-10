---
title: "Rochedo Store"
slug: "rochedo-rochedo-app"
excerpt: "rochedo.rochedo-app@1.0.2"
hidden: true
createdAt: "2022-07-13T14:06:49.727Z"
updatedAt: "2022-07-13T14:06:49.727Z"
---
Rochedo Store Project working with GitFlow to manage branches and SASS to compile CSS files.

## Configuration

### First steps
- Clone this repository
- Run ```git flow init``` (accepting defaults branch names from GitFlow)
- Run ```npm install``` or ```yarn``` on the root folder to install dependencies
- Run ```npm install -g sass``` or ```yarn global add sass```

- The **react/** and **react/components/** *.css* files are in **react/styles/** and **react/styles/components/** respectively as *.scss*.
- The **styles/css/** *.css* files are in **styles/scss/** as *.scss*

#### Watching SCSS files
- After installing all dependencies and installing sass globally, run ```npm run sass``` or ```yarn sass``` to watch your changes.