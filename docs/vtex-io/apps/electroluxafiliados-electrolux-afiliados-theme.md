---
title: "Electrolux Theme"
slug: "electroluxafiliados-electrolux-afiliados-theme"
excerpt: "electroluxafiliados.electrolux-afiliados-theme@0.3.2"
hidden: true
createdAt: "2022-07-25T20:04:45.173Z"
updatedAt: "2022-07-25T22:12:59.830Z"
---
### Plugin dependencies (VSCode extensions) 🚀

**Required**

- [Eslint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)
- [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
- [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)

**Optional**

- Color Pair Colorizer
- Indent-rainbow
- Tabnine

### VTEX IO Commands

- ✅ _vtex login electroluxcoqa_ - Login to the project
- ✅ _vtex whoami_ - Check login and workspace
- ✅ _vtex use {{WorkspaceName}}_ - Login in workspace

### Versions (Recommended)

- Node - 14.15.x
- Npm - 7.8.x

### Necessary Knowledge

- VTEX IO
- React and Typescript
- CSS and SASS
- GraphQL

### VScode configuration

```
{
  "editor.formatOnSave": false,
  "[jsonc]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[css]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[scss]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[javascript]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  }
}
```