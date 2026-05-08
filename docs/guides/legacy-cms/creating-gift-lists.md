---
title: "Creating gift lists"
slug: "creating-gift-lists"
hidden: false
createdAt: "2022-09-08T14:23:40.396Z"
updatedAt: "2022-09-08T14:23:40.396Z"
---
This feature lets you create a shopping list in the online store, which can be associated with an event such as a wedding, bridal shower, birthday, baby shower or simply a wish list. For this to work properly, your agency or the team responsible for the frontend must create the appropriate templates on the Portal module.

The types of list to be created, and their special features, are chosen by the storekeeper from the platform, as explained in the article [How to create a type of list](http://help.vtex.com/en/tutorial/creating-a-type-of-list).

Each different list created will have its own uses, but the key objective is for consumers to add the products they want to buy, and to be able to do so by logging in to their account with the store.

Lists can also be for others to view products and buy them, to give as presents to the owner of the list. This is the case with wedding lists, bridal showers, baby showers and birthday lists.

## Create link to access the lists section in your store

To create the html element that gives the customer access to the lists in your store's Home, you must include the code below in your template:

```html
<a href=“/giftlist”>Listas</a>
```

The `/giftlist` route acts as the Home of the lists for each client. In the `new-Giftlist` template found in the CMS of your store, we have already included the `<vtex.cmc: GiftListSearchV2/>` control inside the `<body>` element on your template. This control renders the search lists created by your clients.

Inside the `new-GiftList` template, there is a subtemplate with the name`new-GiftList-Sidebar-nav`. This subtemplate contains the code snippet below and can be found in the `Sub Templates` section within `HTML Templates` in your CMS:

```html
<ul class="nav nav-list bs-docs-sidenav giftlist-sidenav">
    <li><a href="/giftlist/"><i class="icon-chevron-right"></i> Buscar uma Lista</a></li>
    <li><a href="/giftlist/create/"><i class="icon-chevron-right"></i> Criar nova Lista</a></li>
    <li><a href="/giftlist/manage/"><i class="icon-chevron-right"></i> Gerenciar minhas Listas</a></li>
</ul>
```

This code renders a list with __three links__:

1. __Search a List__: This link takes the customer to the `/giflist` route, where the searches are performed by the lists.
2. __Create New List__: This link takes the customer to the `/giftlist/create` route, where the customer creates their lists. In the next steps, we'll explain how list creation is done.
3. __Manage My Lists__: This link takes the customer to the `/giftlist/manage` route, where the customer can manage their lists. In the next steps, we'll explain how list management is done.

## Find a List

To find a list on the site, click on the link “My List” and complete one of the filter fields, as shown below. This page can vary, depending on how the site is customized, and can, for instance, be limited simply to the fields “Name”, “Sobrenome” and “Data do Evento”.

- __Tipo de lista:__ Selection of type of list according to the registration made by the store owner on the platform, as explained in the article [How to create a type of list](http://help.vtex.com/en/tutorial/creating-a-type-of-list). This field is the only one which, if completed, requires another field to be completed as well, since your site will contain lists of a number of consumers, and if “type of list” returned all the results, a client would have access to your other clients’ lists;
- __Código da lista:__ Code provided when you create a list. This field can only be used to filter a list;
- __Nome:__ First name, defined by the owner of the list. Guests or any users searching for a list will normally use the owner’s first name. This field can be used on its own, to filter lists with the first name of the owner, but if the owner has more than one list, they will all be shown;
- __Sobrenome:__ Last name, defined by the owner of the list. This field can be used on its own, to filter lists in the last name of the owner, but if the owner has more than one list, they will all be shown. If used jointly with the first name and type of list fields, a more specific result will be shown;
- __Local do evento:__ Address where the event will be held. This field can be used on its own to filter lists relating to the address given, but since it can be written in a number of different ways, it is recommended to use it jointly with other fields, to get a more specific result;
- __Data do evento:__ Date when the event will take place. Like the other fields, it may be that there are other lists with events taking place on the same day. If this field is used as a filter on its own, it may return other lists in addition to the one sought.

## Create a new list

To create a  new list on the site, click on the link “My List” (which normally has the path /giftlist), click on “Create new list”, complete the fields, as below, mark the option “Li e estou de acordo com o regulamento” and save. The user must have a register in the store and must log on, because the user will be the owner of the list and by being logged on will associate the list with the user. When you create a list on your site, it is saved on the platform in the E-Commerce module in Relatórios &gt; Listas &gt; Todas as Listas. Below are details of each field in the form for creating a list:

## Create a list

- __Tipo de lista__:Types of list registered by the store owner on the platform.
- __Nome da lista__:The name of the list is defined by the user when it is created. It depends a lot on the type of list chosen, but normally it is the user’s own name, since it is often used for events like weddings, birthdays, bridal showers and baby showers.

- __URL da lista:__ The link to be used to publicize your list. In this field, just insert the final part of the list address, after the last slash. The default is `http://www.sualoja.com.br/list` + the value you enter in this field.
- __Quem pode ver esta lista?:__ The options for who can see this list vary according to the store owner’s configurations. If it is configured for “_Criador da lista decide_”, you can decide between the options “_somente os participantes desta Lista_” and “_qualquer pessoa_” (only list participants, or anyone). Only the first option will appear if the list visibility is defined as “_Privada_” (Private), and only the second if it is defined as “_Pública_” (Public). The “_Criador da lista decide_” option is important for the user, for example in a wedding gift list, since the couple will want to restrict access to themselves only, while they are choosing the products and managing the list, and open the list for anyone to have access when it is complete.
- __Upload de imagem:__ This field lets an image to be used to represent the event or personalize the list, such as a photo of the bride and groom, for example.
- __Mensagem:__ Allows the list owner to leave a message for the guests if so desired. There is a limit of 1000 characters (including letters, numbers, spaces and punctuation).

## Members

- First name
- Last name
- Email address

_To add a new participant, click on the link “incluir participante”. The limit on the number of members included in a list depends on the configuration when the type of list was created. However we recommend that the number be limited to two, since the greater the number of members administering the list, the more likely it is that it will be incorrectly used._

## Delivery address

- Postal code (CEP)
- Street name
- Number
- Unit
- Bairro
- Cidade
- Estado
- Endereço comercial
- Quem receberá

_If the user is already registered in the store, the address will appear automatically, but they will have the option to modify the address or register a new address and use this new one. For this, there are links “Modify selected address” and “Deliver to another address”, respectively._

## Regulations

Regulations are defined according to the need of each store to regulate use of the list and indicate how it works on its site. It appears as a read-only text field with a vertical scroll bar. The text to be shown here must be registered in text configuration in admin. For this, follow these steps:

- Access the __Catalog__ module
- Go to Configurações and click on __Textos__
- Click on __Selecione o ID do texto a Editar__
- Look for __GifListThermsText__
- Type the text in the field below the selection field, and save

_For this information to appear in the Regulamento field each time a client creates a list, your agency or frontend customization team must use the control `<vtex.cmc:GiftListFormV2 />` inside of `<body>` element on your template._

## Manage my Lists

To manage your list, you must be logged on to the site, access the link “Minha Lista” (which normally has the pathway `/giftlist`), click on “Gerenciar minhas Listas” and then select one of the following actions for the list.

### Visualize

This will give you a macro view of your list, with the information entered when it was created and the products it contains. It will also have links to open the list, i.e. to make it public, if it has been configured as private; to edit and manage it, as explained below; and it may also have a summary of how many products you included and how many have been purchased . There may be other functions, such as buying all the products in the list or printing the list, but this will depend on how the frontend was customized.

### Manage

This is very similar to the previous action, but can also add more units of the products selected, or exclude them from the list

### Edit

Here the user has the same view as when creating the list. The intention is that the owner of the list can amend any configuration made at the outset.

### Exclude

This will delete the list. On clicking, a popup will appear to confirm the request.

## Inserting products in a list

After creating a list, you can add products by browsing the site and clicking on the button “Adicionar produtos às suas Listas”. This button’s function depends on the use of the control `&lt;vtex.cmc:GiftListInsertSkuV2 /&gt;` inside your product template page.

_There is a limit to the number of associations of __300__ SKUs per list._

##### **Special features of a List – Gift Card**

Items purchased from your list will generate a credit that will accrue on a voucher automatically generated at the time the list is created. This voucher will work as a form of payment, so that the list owner redeems on purchases on the site any items they wish.

Learn more about the form of payment worth in the article [Gift Card](https://help.vtex.com/en/tutorial/gift-card--tutorials_995). Remembering that the types of lists available for site creation should be pre-built on the platform by the retailer.

__Important Note:__ Stores that are marketplace (sell sellers products, other partners in your store) are not eligible to use List Voucher.
