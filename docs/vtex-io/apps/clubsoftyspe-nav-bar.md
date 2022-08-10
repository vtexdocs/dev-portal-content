---
title: "Menu Nav-Bar"
slug: "clubsoftyspe-nav-bar"
excerpt: "clubsoftyspe.nav-bar@0.0.9"
hidden: true
createdAt: "2022-07-04T23:04:03.284Z"
updatedAt: "2022-07-04T23:04:03.284Z"
---
Lets you render a menu by means of an arrangement of objects.

## Aplica Install 

1. Clone the repository and change the name and vendor in the manifest file, such as:
```
{
vendor: "account name"
name: "name of your application"
}
```

2. Login to your vtex account:
```
vtex login <account name>
```

3. Check that you don't have another application installed with the same name with this command:
```
vtex ls
```

4. Select your workspace and use this command:
```
vtex link
```

## Block 


1. Add the following line as a dependency in your project in the manifest-json file:
```
"<name-account>.custom-nav-bar: "0.x" "
```

2. Where you use this application add the following block, such as:
```
  "flex-layout.col#custom-nav-bar": {
    "children": ["custom-nav-bar"],
    "props": {
    }
  },
    "custom-nav-bar": {
    "props": {
      "items": [
        {
          "id_item": 1,
          "name": "RETORNABLES",
          "icon": "",
          "sub_items": {
            "sub_title": [
              {
                "items_nav": [
                  {
                    
                    
                  {
                ]
              }
            ],
            "typeButton":"button",
            "customPixelEventId": ""
          }
        }
      ]
    }
}
```

### `block-1` props

| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `items`      | `Array`         | `Items de la nav bar`| `undefinded`        |
| `typeButton` |`String`         |`Nav bar button type` | `empty` |
|`customPixelEventId`| `string`  |`Event to activate the modal` | `empty` |



## Modus Operandi *(not mandatory)*


Page navigation menu through an object that is received through props and has the ability to listen for events in Google Tag Manager.

## Important

- Dynamic Yield works automatically by taking the name of the menu and triggering the 'navbarCategoryClicked' event for menu and submenus.

## Customization

| CSS Handles |
| ----------- | 
| `containerNav` | 
| `containerUl` | 
| `containerSubItems` | 
| `titleAction` | 
| `titleAction:hover` |
| `containerSubItemsHiden` | 
| `containerSubItemsShow` | 
| `liSubItem:first-child` | 
| `icon` |
| `item` | 
| `containerTitle` | 
| `containerItemList` | 
| `ulContainer` |
| `liSubItem` |
| `liSubItem:first-child .li` |
| `test:first-child` |
| `itemLinkX` |
| `itemLink:hover` |
| `titleMenu`|

## Archive Styles
Add a file in your styles folder with the following name:
```
"account-name.name-app"
```

```
/* --- Styles --- */
  .containerNav {
    display: flex;
    width: 100%;
    height: 47px;
    align-items: center;
    justify-content: center;
    background-color: black;
  }
  
  .containerUl {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    width: 85%;
    height: 47px;
    font-size: 12px;
    background-color: black;
  }
  
  .containerSubItems {
    height: 47px;  
  }
  
  .titleAction{
    color: white;
    text-decoration: none;
    font-size: 12px;
  }

  .titleAction:hover {
    text-decoration: none;
    border-bottom: 4px solid red;
    border-top-width: 2;
  }
  
  .containerSubItemsHiden {
    display: none;
  }
  
  .containerSubItemsShow {
    position: absolute;
    transition: 0.8s;
    width: 100%;
    z-index: 99;
    left: 0px;
    top: 79px;
    background: url(/arquivos/navbar-retornable.jpg) 100% 100% no-repeat white;
    cursor: default;
    padding: 0px 0px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
  }
  
  .liSubItem:first-child {
    width: 300px;
    height: 22px;
    margin: 0px -15px 10px;
    border-bottom: 1px solid gray;
    border-top-width: 1;
    padding: -5px;
  }
  
  .icon {
    width: 17px;
    height: 16px;
    position: relative;
    right: 8px;
    top: 3px;
  }
  
  .item {
    margin: 10px;
    white-space: pre;
    text-align: center;
    justify-items: center;
  }

  .containerTitle {
    width: 100%;
    height: 35px;
    margin-left: 25px;
    display: flex;
    align-items: center;
    justify-content: flex-end;
  }

  .containerItemList {
    width: 25%;
    display: flex;
    justify-content:  flex-start;
  }
  
  .containerItemList:first-child{
    width: 25%;
    margin: 0px 0px;
  } 
   
  .ulContainer{
    width: 100%;
  }
   
   .liSubItem{
    width: 250px;
    color: gray;
    list-style: none;
    margin: 0px -15px 10px;
  }
  
  .liSubItem:first-child .li{
    color: black;
  }
  
  .test:first-child{
    color: black;
  }
  
  .itemLink{
    text-decoration: none;
    font-size: 12px;
    margin: 10px 0 0 0;
    color: gray;
  }
  
  .itemLink:hover{
    text-decoration: none;
    color: red;
    font-size: 14px;
  }

  
  .titleMenu{
    color: black;
    font-size: 14px;
    font-weight: bold;
    font-family: gothamboldregular;
    cursor: default;
  } 

  <!-- Styles for tablet -->
  @media screen and (max-width: 1085px) and (min-width: 1024px) {
  .containerNav {
    display: flex;
    width: 90%;
    height: 47px;
    align-items: center;
    justify-content: center;
    position: relative;
    right: 45px;
    background-color: black;
  }

    
  .containerUl {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    width: 100%;
    height: 47px;
    font-size: 11px;
    white-space: pre;
    background-color: grey;
  }
  
  .title_nav {
    width: 100%;
    height: max-content;
    color: #ffffff;
    text-decoration: none;
    font-size: 8px;
    white-space: pre;
  }

  
}
```

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

---- Luis Martínez ----

- Fabián Toro ( Dinamic Yield implementation )