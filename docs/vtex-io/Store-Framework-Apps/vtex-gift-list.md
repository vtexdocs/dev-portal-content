---
title: "Gift List"
slug: "vtex-gift-list"
hidden: false
createdAt: "2022-07-08T07:17:48.371Z"
updatedAt: "2022-10-27T19:47:24.537Z"
---
A gift list is a list of products that a shopper creates and sends to guests (other shoppers) asking them to buy the products. This can be useful for events like birthdays, weddings, and baby showers. When a guest buys one or more products from the list, virtual credit is generated that can be converted into a [gift card](https://developers.vtex.com/vtex-rest-api/docs/gift-card-integration-guide). The list’s creator has a wallet with information about the generated credit and the gift card. Then, the creator of the list can use the gift card to purchase the desired items.

The Gift List app allows you to create an environment that contains gift lists. In this environment, shoppers can create gift lists, send them to guests, manage credit on their wallets, and see their bank statements. This app makes an Admin interface available where the shopkeeper can manage the progress of the lists, with information like the number of lists created, track information from multiple customers, and how much money was generated from the gift lists among other essential measures.
[block:callout]
{
  "type": "info",
  "body": "The gift cards used in gift lists are VTEX native ones. Gift cards from external providers are not supported by the app."
}
[/block]
## Getting started

The Gift List app must run in an environment separate from the main store. So first you need to create a subaccount inside the main account. You can check the instructions in the [How to create a multistore / multidomain](https://help.vtex.com/en/tutorial/creating-multi-store-multi-domain--tutorials_510) article.

After creating the subaccount, it is necessary to [open a ticket to the VTEX support team](https://help.vtex.com/en/tutorial/opening-tickets-to-vtex-support--16yOEqpO32UQYygSmMSSAM) requesting the installation of the `vtex.edition-store@5.x` app at the new subaccount. See the [Edition App](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app) article for more information.

Another requirement is to create an application key on your subaccount to configure the order hook. You can check the instructions in the [Application Keys](https://help.vtex.com/en/tutorial/application-keys--2iffYzlvvz4BDMr6WGUtet#generating-app-keys-in-your-account) article. You also need to add a role to the application key with access to the **Feed v3 and Hook Admin** resource. You can check the instructions to create and manage roles in the [Roles](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) article.
[block:callout]
{
  "type": "info",
  "body": "Remember to save the app key and the app token for further configuration steps."
}
[/block]
## Setup

To set up Gift List in your store, follow these steps:

1. Install the Gift List app. You can do this by going to the [List app page](https://apps.vtex.com/vtex-list/p) and acquiring the app in the subaccount created previously.
2. Access your subaccount Admin.
3. Access the **Gift List App Settings** menu. The conversion of the values ​​received from the gifts will be sent to a Gift Voucher that can be used in your official store. But for that, we have to configure it. When accessing the previously specified menu, the following screen will be displayed:
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-gift-list-0.png)
4. In the **Account Setting** tab, click on the **Main account name field** and choose the account which is the official store where the generated gift cards will be used.
5. Click on the `SAVE` button.
6. Go to the **Advanced Settings** tab.
7. Use the app key and the app token created previously in the **VTEX App Key** and **VTEX App Token** fields respectively for the order hook. This application key must have no hook registered to it.
8. Click on the `SAVE` button.
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-gift-list-1.png)
9. In the left panel of the Admin, go to **Search** > **Integration Configuration**. Here you will configure the [Intelligent Search](https://help.vtex.com/tracks/vtex-intelligent-search) so that your entire store catalog is indexed in the subaccount.
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-gift-list-2.png)
Click on the `START INTEGRATION` button and wait until all the integration is completed successfully as shown in the image below.
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-gift-list-3.png)
After these steps, the app is configured and the gift lists are available in the store for the shoppers.

## Components

Below is a list of all the components in our app:
[block:html]
{
  "html": "<style>\n    .flexcontainer {\n        display: flex;\n        flex-wrap: wrap;\n        padding-top: 1rem;\n        padding-bottom: 2rem;\n        justify-content: space-between;\n    }\n\n    .flexcontainer-card {\n        display: flex;\n        flex-direction: column;\n        justify-content: space-between;\n        align-items: flex-start;\n        width: 22rem;\n        margin: 0.5rem;\n        line-height: 1.8;\n    }\n    .see-more {\n        color: rgb(247, 25, 99);\n        text-decoration: none !important;\n    }\n\n    .see-more::after {\n        content: url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='30' height='14' viewBox='0 -8 59 14' fill='none'><path d='M0 7H57' stroke='rgb(247, 25, 99)'></path><path d='M49 1L57.5 7L49 13' stroke='rgb(247, 25, 99)'></path></svg>\");\n        display: inline-block;\n        margin-left: 6px;\n        text-decoration: none !important;\n    }\n\n    .see-more:hover:after {\n        content: url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='30' height='14' viewBox='0 -8 59 14' fill='none'><path d='M0 7H57' stroke='rgb(181, 16, 71)'></path><path d='M49 1L57.5 7L49 13' stroke='rgb(181, 16, 71)'></path></svg>\");\n        margin-left: 8px;\n    }\n\n    .see-more:hover {\n        color: rgb(181, 16, 71);\n    }\n    .app-description{\n        font-size: 16px;\n    }\n</style>\n\n<div class=\"flexcontainer\">\n    <div class=\"flexcontainer-card\">\n        <article >\n            <div>\n                <h3>Add To Cart Button</h3>\n                <div>\n                    Displays a button that allows users to add products in the Minicart from a guest page if the quantity purchased has not yet reached the limit.\n                </div>\n            </div><a href=\"https://developers.vtex.com/docs/guides/vtex-list-listaddtocartbutton\" class=\"see-more\">See more</a>\n            <hr></article>\n    </div>\n\n\t\t<div class=\"flexcontainer-card\">\n        <article >\n            <div>\n                <h3>Add to List Button</h3>\n                <div>\n                    Displays a button that allows owners of the list to add products and remove products inside their list.\n                </div>\n            </div><a href=\"https://developers.vtex.com/docs/guides/vtex-list-addtolistbutton\" class=\"see-more\">See more</a>\n            <hr></article>\n    </div>\n\n\t\t<div class=\"flexcontainer-card\">\n        <article >\n            <div>\n                <h3>Auth Condition</h3>\n                <div>\n                    Performs validation that the user is logged in to render different layouts.\n                </div>\n            </div><a href=\"https://developers.vtex.com/docs/guides/vtex-list-authcondition\" class=\"see-more\">See more</a>\n            <hr></article>\n    </div>\n\n\t\t<div class=\"flexcontainer-card\">\n        <article >\n            <div>\n                <h3>Add New Item</h3>\n                <div>\n                    Displays a button to direct the list owner to the search page for adding new items to their list.\n                </div>\n            </div><a href=\"https://developers.vtex.com/docs/guides/vtex-list-addnewitem\" class=\"see-more\">See more</a>\n            <hr></article>\n    </div>\n\n\t\t<div class=\"flexcontainer-card\">\n        <article >\n            <div>\n                <h3>Breadcrumbs</h3>\n                <div>\n                    Displays the path to the user's navigation list. \n                </div>\n            </div><a href=\"https://developers.vtex.com/docs/guides/vtex-list-breadcrumbs\" class=\"see-more\">See more</a>\n            <hr></article>\n    </div>\n\n\t\t<div class=\"flexcontainer-card\">\n        <article >\n            <div>\n                <h3>List Modal</h3>\n                <div>\n                    Displays a modal for editing or creating lists.\n                </div>\n            </div><a href=\"https://developers.vtex.com/docs/guides/vtex-list-listmodal\" class=\"see-more\">See more</a>\n            <hr></article>\n    </div>\n\n\t\t<div class=\"flexcontainer-card\">\n        <article >\n            <div>\n                <h3>Gallery List Items</h3>\n                <div>\n                    Displays the gallery with the products contained in a list.\n                </div>\n            </div><a href=\"https://developers.vtex.com/docs/guides/vtex-list-gallerylistitems\" class=\"see-more\">See more</a>\n            <hr></article>\n    </div>\n\n\t\t<div class=\"flexcontainer-card\">\n        <article >\n            <div>\n                <h3>Gifted Button</h3>\n                <div>\n                    Displays the counter of purchases that have already been made for a product within the list.\n                </div>\n            </div><a href=\"https://developers.vtex.com/docs/guides/vtex-list-giftedbutton\" class=\"see-more\">See more</a>\n            <hr></article>\n    </div>\n\n\t\t<div class=\"flexcontainer-card\">\n        <article >\n            <div>\n                <h3>Go Back To List</h3>\n                <div>\n                    Allows the user to return to the list.\n                </div>\n            </div><a href=\"https://developers.vtex.com/docs/guides/vtex-list-gobacktolist\" class=\"see-more\">See more</a>\n            <hr></article>\n    </div>\n\n\t\t<div class=\"flexcontainer-card\">\n        <article >\n            <div>\n                <h3>List Info</h3>\n                <div>\n                    Is made up of three blocks (<code>list-info.name</code>, <code>list-info.event-date</code> and <code>list-info.owner</code>) and each one represents a type of information associated with the list, which are the name of the list, date of the event and name of the owner of the list respectively.\n                </div>\n            </div><a href=\"https://developers.vtex.com/docs/guides/vtex-list-listinfo\" class=\"see-more\">See more</a>\n            <hr></article>\n    </div>\n\n\t\t<div class=\"flexcontainer-card\">\n        <article >\n            <div>\n                <h3>Product Modal</h3>\n                <div>\n                    Displays a modal with detailed information (such as size and color) about the product the costumer wants to add to the lists they own.\n                </div>\n            </div><a href=\"https://developers.vtex.com/docs/guides/vtex-list-productmodal\" class=\"see-more\">See more</a>\n            <hr></article>\n    </div>\n\n\t\t<div class=\"flexcontainer-card\">\n        <article >\n            <div>\n                <h3>Autocomplete Result List</h3>\n                <div>\n                    Represents the autocomplete from the search bar. \n                </div>\n            </div><a href=\"https://developers.vtex.com/docs/guides/vtex-store-components-autocompleteresults\" class=\"see-more\">See more</a>\n            <hr></article>\n    </div>\n\n\t<div class=\"flexcontainer-card\">\n        <article >\n            <div>\n                <h3>Quantity Selector</h3>\n                <div>\n                    Is made up of three blocks (<code>quantity-selector-minicart</code>, <code>quantity-selector-shelf-guest</code> and <code>quantity-selector-shelf-owner-list</code>) and each of them represents a quantity selector for different contexts which are use in mini-cart, guest shelf, list owner shelf and selection modal on search page.\n                </div>\n            </div><a href=\"https://developers.vtex.com/docs/guides/vtex-list-quantity-selector-2\" class=\"see-more\">See more</a>\n            <hr></article>\n    </div>\n\n\t\t<div class=\"flexcontainer-card\">\n        <article >\n            <div>\n                <h3>Search List</h3>\n                <div>\n                    Displays a search box for public lists according to the name of the owner of the list or the name of the list.\n                </div>\n            </div><a href=\"https://developers.vtex.com/docs/guides/vtex-list-searchlist\" class=\"see-more\">See more</a>\n            <hr></article>\n    </div>\n\n\t\t<div class=\"flexcontainer-card\">\n        <article >\n            <div>\n                <h3>Store Wallet List</h3>\n                <div>\n                    Renders the virtual wallet that contains the user's credit and gift card information.\n                </div>\n            </div><a href=\"https://developers.vtex.com/docs/guides/vtex-list-storewalletlist\" class=\"see-more\">See more</a>\n            <hr></article>\n    </div>\n\n\t\t<div class=\"flexcontainer-card\">\n        <article >\n            <div>\n                <h3>Share List</h3>\n                <div>\n                    Displays a button to automatically copy the URL to send the list to guests.\n                </div>\n            </div><a href=\"https://developers.vtex.com/docs/guides/vtex-list-sharelist\" class=\"see-more\">See more</a>\n            <hr></article>\n    </div>\n\n\t\t<div class=\"flexcontainer-card\">\n        <article >\n            <div>\n                <h3>Users List</h3>\n                <div>\n                    Displays the lists the user has with their names and privacy information. It has as title and a subtitle and a link button to generate new lists.\n                </div>\n            </div><a href=\"https://developers.vtex.com/docs/guides/vtex-list-userlists\" class=\"see-more\">See more</a>\n            <hr></article>\n    </div>\n\n\t\t<div class=\"flexcontainer-card\">\n        <article >\n            <div>\n                <h3>Wrappers</h3>\n                <div>\n                    Are used to call the context Provider for other components and they are made of three blocks (<code>wner-list-wrapper</code> , <code>guest-list-wrapper</code> and <code>user-lists-wrapper</code>) and each one represents a context, which are owners, guests and users respectively.\n                </div>\n            </div><a href=\"https://developers.vtex.com/docs/guides/vtex-gift-list-wrappers\" class=\"see-more\">See more</a>\n            <hr></article>\n    </div>\n\n\t\t<div class=\"flexcontainer-card\">\n        <article >\n            <div>\n                <h3>List Items Order By</h3>\n                <div>\n                    Allows the user to sort the items of an list. The options for ordering are alphabetically or addition date.\n                </div>\n            </div><a href=\"https://developers.vtex.com/docs/guides/vtex-gift-list-listitemsorderby\" class=\"see-more\">See more</a>\n            <hr></article>\n    </div>\n\n</div>"
}
[/block]
## Optional settings (recommended)

### Trade Policy

To better control the functioning of the gift list, we strongly recommend creating a new trade policy. There are 3 main reasons why trade policy helps you to manage gift lists:

1. Stock control: There are two different moments of purchase on gift flow. The first occurs when guests realize a purchase related to the list. The second occurs when the list owner realizes a purchase, using the credits received by the guests on the first purchase.  
   Because of this flow, two items can be removed for the same gift, generating an imbalance in stock control. Attentive to this problem, we suggest one stock to be used only for gift list purchases. For this matter, is mandatory an exclusive trade policy for linking stock with the store catalog.
2. Specific assortment: You could want to define a specific assortment of items to be added to clients' lists. For this purpose, you will need a separate trade policy.
3. Different prices: Another common situation is to define a specific price table for items sold by gift list. A new trade policy helps you to enable this particular price table.

To create a new trade policy, please fill out this [form](https://docs.google.com/forms/d/e/1FAIpQLSe9qCGB_KM_xsV5e9uNe06JE8tMZrWcv6EuHUOmqTiM8oRW7w/viewform). If you want more information about commercial policies, check the [Creating a trade policy](https://help.vtex.com/en/tutorial/creating-a-trade-policy--563tbcL0TYKEKeOY4IAgAE) article on our Help Center.

### Ready-made theme

It is possible to use a ready-made theme with these components or even use this theme and then change it to meet your needs better. If you want to use the mentioned theme, you can access it on the [List Theme repository](https://github.com/vtex-apps/list-theme) or install it directly using the command:

```bash
vtex install vtex.list-theme@3.x
```

After the theme is created, it will be necessary to enter the **Site Editor** in the Admin to add which category the list owner will be redirected to when adding a product to your list, as can be seen below:
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-gift-list-4.png)
### Checkout

We recommend using the checkout created by us for the gift list, as it will allow some personalized features to be added, such as the possibility of sending personalized emails from a guest to the person to be gifted. To use it, just install it with the following command:

```bash
vtex install vtex.list-checkout@0.x
```

If you continue with this alternative, you will also need to install the `checkout-ui-custom` app if you want to edit the previous checkout. The steps to use this application can be found in the [Checkout UI Custom](https://developers.vtex.com/docs/guides/vtex-checkout-ui-custom-v0) article.

With the checkout apps installed, you can enable the message field. To do this, just access the Checkout UI Custom interface via Admin and upload the following snippet in the CSS tab and publish the changes.

```css
.note { display: block; }
```
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/vtex-io/Store%20Framework%20Apps/1c3174c-image5.png",
        "image5.png",
        1999,
        1032,
        "#000000"
      ]
    }
  ]
}
[/block]
### Email for gift purchase

If you want to send the emails that are triggered with the checkout above, you must create a new template in the admin, in the **Message Center** -> **Templates** page. The name of the template must be `new-list-order` and the recipient `{{ownerListEmail}}`.
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-gift-list-5.png)
An optional HTML code for the email template can be found [here](https://drive.google.com/file/d/1ZkI--JZn25PyG4FssoqqPi6a33075skO/view?usp=sharing).

### Login integration with the main account

Another recommendation is to unify the login of the main account with the subaccount. With this, you can provide a unified navigation experience, since a login into the subaccount will also be a login into the main account and vice versa. You can check the instructions for this configuration in the [Unifying login for different accounts](https://developers.vtex.com/vtex-rest-api/docs/unifying-login-for-different-accounts) article, using the main account as the **primary account** and the subaccount as the **secondary account**.

## Store owner interface

There is also an interface available for the shopkeeper to follow the metrics obtained by the list application. You can access it on the Admin by going to the **Store owner interface** menu. In this interface, you will see on the first screen all the users that contain a gift list, with their respective amounts of lists, the value they have already earned in gifts, the value converted into gift vouchers, and whether or not there is already an active list at the moment, respectively. You can also search for emails.
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-gift-list-6.png)
If you want to have more information about a specific user, just click on the arrow next to the user's name, which will redirect you to a second screen. On this new screen, you can find information from each list of this user, including the name of the list, the value gained in the list, the date of the event, and if the event has already occurred or not. 

There is also a totalizer with the number of lists, the amount invoiced on the lists, and the converted amount. It is worth adding that if a search is performed or a filter is used, the number of lists ​​and purchased values will be updated according to the result. The search can be done by the list title and the available filters are the status of the lists and the date of creation of the list. Finally, if you want to see the list in question, you can click on the <i class="fa fa-eye"></i> button and you will be redirected to the list in question in the guest view.
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-gift-list-7.png)