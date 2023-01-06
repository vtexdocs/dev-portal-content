---
title: "Installing B2B Easy Set Up"
slug: "installing-b2b-easy-set-up"
hidden: false
createdAt: "2021-07-28T20:53:10.893Z"
updatedAt: "2022-07-19T17:44:04.867Z"
---

B2B Easy Set Up is an app that helps you quickly get your store configured for B2B ecommerce.

## Installation

1. Download and install the [VTEX IO CLI](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-installation-and-command-reference).
2. [Log in to your account](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-2-basicsetuptodevelopinvtexio#step-1---logging-in-to-your-vtex-account) with `vtex login {accountName}`.
3. [Create a new workspace](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-2-basicsetuptodevelopinvtexio#step-2---creating-your-own-workspace) with `vtex use easysetupworkspace`.
4. [Install the app on your store](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-installing-an-app) with `vtex install vtex.easy-setup`.
  
[block:callout]
{
  "type": "danger",
  "body": "We strongly advise that you **do not run Easy Setup on a production environment**. It will make **irreversible changes** and may delete some previous configurations on your store.",
}
[/block]
  
## Store configuration

Now that the Easy Setup app is installed in your store, proceed to operate the app on the Admin.

1. Open your Admin panel and navigate to **Store Settings** > **Easy Setup**.

2. On the right side of the screen, select which resources you want to apply on your store. If you want to configure all the options, select **All Resources**.

[block:callout]
{
  "type": "warning",
  "body": "If you are using the [B2B Suite](https://developers.vtex.com/docs/guides/vtex-b2b-suite) solution, you must not select the **Organizations** resource. Otherwise this will alter the user profile Master Data schema and prevent the B2B Suite apps from creating users.",
}
[/block]


3. Click on the `Start Easy Setup` button.
   ![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/installing-b2b-easy-set-up-0.PNG)

4. Click on the `I Understand` button that will appear in the **Are you sure you want to proceed?** dialog.

[block:callout]
{
  "type": "danger",
  "body": "Once you click `I Understand`, this step is irreversible.",
}
[/block]

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/installing-b2b-easy-set-up-1.PNG)

Wait a few seconds for the setup to complete.

When the configuration is complete, you will receive a positive feedback on the screen.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/installing-b2b-easy-set-up-2.PNG)

[block:callout]
{
  "type": "info",
  "body": "If you get an error message for some of the resources, try again this time only selecting the troublesome resources. If the error persists, [contact support](https://support.vtex.com/hc/en-us/requests)."
}
[/block]

Check out the [Resources](https://developers.vtex.com/vtex-developer-docs/docs/installing-b2b-easy-set-up#resources) section below for details on the sample data used by the app in the initial setup.

## Resources

### Users

This resource creates some users with `priceTables` data.

<details>
  <summary>View Sample Data</summary>
  <hr/>
  <ul>
    <li>Email: <code>john@email.com</code></li>
    <ul>
      <li>PriceTable: platinum</li>
    </ul>
    <br />
    <li>Email: <code>steven@email.com</code></li>
    <ul>
      <li>PriceTable: gold</li>
    </ul>
    <br />
    <li>Email: <code>chris@email.com</code></li>
    <ul>
      <li>PriceTable: silver</li>
    </ul>
  </ul>
  <hr/>
</details>

### Brands

This resource creates one brand.

<details>
  <summary>View Sample Data</summary>
  <hr/>
  <ul>
    <li>Name: Brand (9280)</li>
  </ul>
  <hr/>
</details>

### Categories

This resource creates seven categories.

<details>
  <summary>View Sample Data</summary>
  <hr/>
  <ul>
    <li>Name: Apparel (9281)</li>
    <li>Name: Food and beverage (9282)</li>
    <li>Name: Sporting (9283)</li>
    <li>Name: Agribusiness (9284)</li>
    <li>Name: Home Appliance (9285)</li>
    <li>Name: Computer & Software (9286)</li>
    <li>Name: Power tools (9287)</li>
  </ul>
  <hr/>
</details>

### Collections

This resource creates a collection with all products.

<details>
  <summary>View Sample Data</summary>
  <hr/>
  <ul>
    <li>Name: All</li>
    <li>Type: Inclusive</li>
    <li>BrandId: 9280 (Brand)</li>
  </ul>
  <hr/>
</details>

### Fields

This resource creates a group with two fields containing a variety of field values for two specifics categories.

<details>
  <summary>View Sample Data</summary>
  <hr />
  <ul>
    <li>Group: Specifications</li>
    <br />
    <li>Category: Apparel (9281)</li>
    <ul>
      <li>Field: Clothes Size</li>
      <li>Field Values: S, M, L and XL</li>
    </ul>
    <br />
    <li>Category: Sporting (9283)</li>
    <ul>
      <li>Field: Shoes Size</li>
      <li>Field Values: 8, 8.5, 9, 9.5 and 10</li>
    </ul>
  </ul>
  <hr />
</details>

### Products

This resource creates an assortment of products and SKUs and sets their specifications, images and attachments (related to customizations and subscriptions).

<details>
  <hr />
  <summary>View Sample Data</summary>
  <ul>
    <details>
      <summary>Category: Apparel (9281)</summary>
      <ul>
        <li>Product Name: adidas Men's Performance Polo - Blast Blue (880001)</li>
        <ul>
          <li>SKU Name: S (880010)</li>
          <li>SKU Name: M (880011)</li>
          <li>SKU Name: L (880012)</li>
          <li>SKU Name: XL (880013)</li>
        </ul>
        <br />
        <li>Product Name: adidas Men's Performance Polo - Green Night (880002)</li>
        <ul>
          <li>SKU Name: S (880020)</li>
          <li>SKU Name: M (880021)</li>
          <li>SKU Name: L (880022)</li>
          <li>SKU Name: XL (880023)</li>
        </ul>
        <br />
        <li>Product Name: adidas Women's Microdot Polo - Night Indigo (880003)</li>
        <ul>
          <li>SKU Name: S (880030)</li>
          <li>SKU Name: M (880031)</li>
          <li>SKU Name: L (880032)</li>
          <li>SKU Name: XL (880033)</li>
        </ul>
        <br />
        <li>Product Name: adidas Women's Microdot Polo - True Pink (880004)</li>
        <ul>
          <li>SKU Name: S (880040)</li>
          <li>SKU Name: M (880041)</li>
          <li>SKU Name: L (880042)</li>
          <li>SKU Name: XL (880043)</li>
        </ul>
      </ul>
    </details>
    <details>
      <summary>Category: Food and beverage (9282)</summary>
      <ul>
        <li>Product Name: Yellow Onions (10 lbs.) (880026)</li>
        <ul>
          <li>SKU Name: _same name_ (880260)</li>
        </ul>
        <br />
        <li>Product Name: Cauliflower Fresh (880027)</li>
        <ul>
          <li>SKU Name: _same name_ (880270)</li>
        </ul>
        <br />
        <li>Product Name: Asparagus Green Conventional (880028)</li>
        <ul>
          <li>SKU Name: _same name_ (880280)</li>
        </ul>
        <br />
        <li>Product Name: Fresh Hass Avocadoes (880029)</li>
        <ul>
          <li>SKU Name: _same name_ (880290)</li>
        </ul>
        <br />
        <li>Product Name: Fresh Coconuts (880030)</li>
        <ul>
          <li>SKU Name: _same name_ (880300)</li>
        </ul>
        <br />
        <li>Product Name: Whole Watermelon Mini Fresh (880031)</li>
        <ul>
          <li>SKU Name: _same name_ (880310)</li>
        </ul>
        <br />
        <li>Product Name: Navel Oranges Grown Large Fresh (880032)</li>
        <ul>
          <li>SKU Name: _same name_ (880320)</li>
        </ul>
        <br />
        <li>Product Name: Navel Oranges Grown Large Fresh, Pack of 10 (880039)</li>
        <ul>
          <li>SKU Kit: _same name_ (880390)</li>
          <li>SKU Components: 10un of Navel Oranges Grown Large Fresh</li>
        </ul>
    </details>
    <details>
      <summary>Category: Sporting (9283)</summary>
      <ul>
        <li>Product Name: Nike Men's Roshe G Spikeless Golf Shoes (880005)</li>
        <ul>
          <li>SKU Name: 8 (880050)</li>
          <li>SKU Name: 8.5 (880051)</li>
          <li>SKU Name: 9 (880052)</li>
          <li>SKU Name: 9.5 (880053)</li>
          <li>SKU Name: 10 (880054)</li>
        </ul>
        <br />
        <li>Product Name: Nike Men's Air Max 1 G Spikeless Golf Shoes (880006)</li>
        <ul>
          <li>SKU Name: 8 (880060)</li>
          <li>SKU Name: 8.5 (880061)</li>
          <li>SKU Name: 9 (880062)</li>
          <li>SKU Name: 9.5 (880063)</li>
          <li>SKU Name: 10 (880064)</li>
        </ul>
        <br />
        <li>Product Name: Nike Air Max 270 G Spikeless Golf Shoes (880007)</li>
        <ul>
          <li>SKU Name: 8 (880070)</li>
          <li>SKU Name: 8.5 (880071)</li>
          <li>SKU Name: 9 (880072)</li>
          <li>SKU Name: 9.5 (880073)</li>
          <li>SKU Name: 10 (880074)</li>
        </ul>
        <br />
        <li>Product Name: Skechers Women's Go Golf Drive 4 Dogs At Play Spikeless Golf Shoes (880008)</li>
        <ul>
          <li>SKU Name: 8 (880080)</li>
          <li>SKU Name: 8.5 (880081)</li>
          <li>SKU Name: 9 (880082)</li>
          <li>SKU Name: 9.5 (880083)</li>
          <li>SKU Name: 10 (880084)</li>
        </ul>
    </details>
    <details>
      <summary>Category: Agribusiness (9284)</summary>
      <ul>
        <li>Product Name: 2020 APACHE AS1040 (880033)</li>
        <ul>
          <li>SKU Name: _same name_ (880330)</li>
        </ul>
        <br />
        <li>Product Name: 2 POST CANOPY (880034)</li>
        <ul>
          <li>SKU Name: _same name_ (880340)</li>
        </ul>
        <br />
        <li>Product Name: 2020 AMACSA PH390 (880035)</li>
        <ul>
          <li>SKU Name: _same name_ (880350)</li>
        </ul>
        <br />
        <li>Product Name: Faceplate Combine Snout (880036)</li>
        <ul>
          <li>SKU Name: _same name_ (880360)</li>
        </ul>
        <br />
        <li>Product Name: 2016 MK MARTIN ENT MKGB788 Blades/Box Scraper (880037)</li>
        <ul>
          <li>SKU Name: _same name_ (880370)</li>
        </ul>
        <br />
        <li>Product Name: 1998 JOHN DEERE 8400T (880038)</li>
        <ul>
          <li>SKU Name: _same name_ (880380)</li>
        </ul>
    </details>
    <details>
      <summary>Category: Home Appliance (9285)</summary>
      <ul>
        <li>Product Name: Weber 45010001 Spirit II E-310 3-Burner Liquid Propane Grill, Black (880021)</li>
        <ul>
          <li>SKU Name: _same name_ (880210)
        </ul>
        <br />
        <li>Product Name: iRobot Roomba 675 Robot Vacuum-Wi-Fi Connectivity, Works with Alexa, Good for Pet Hair,
          Carpets, Hard Floors, Self-Charging (880022)</li>
        <ul>
          <li>SKU Name: _same name_ (880220)</li>
        </ul>
        <br />
        <li>Product Name: ALROCKET Dehumidifier 35oz(1000ml) Small Dehumidifier for 2100 Cubic Feet (260 sq ft) Portable
          and Compact Ultra Quiet (880023)</li>
        <ul>
          <li>SKU Name: _same name_ (880230)</li>
        </ul>
        <br />
        <li>Product Name: McCulloch MC1375 Canister Steam Cleaner with 20 Accessories (880024)</li>
        <ul>
          <li>SKU Name: _same name_ (880240)</li>
        </ul>
        <br />
        <li>Product Name: Cuisinart GR-4N 5-in-1 Griddler (880025)</li>
        <ul>
          <li>SKU Name: _same name_ (880250)</li>
        </ul>
    </details>
    <details>
      <summary>Category: Computer & Software (9286)</summary>
      <ul>
        <li>Product Name: Acer Aspire Z24-890-UA91 AIO Desktop - Windows 10 (880015)</li>
        <ul>
          <li>SKU Name: _same name_ (880150)</li>
        </ul>
        <br />
        <li>Product Name: Lenovo IdeaCentre AIO 3 - Windows 10 (880016)</li>
        <ul>
          <li>SKU Name: _same name_ (880160)</li>
        </ul>
        <br />
        <li>Product Name: Acer Aspire TC-885-UA92 Desktop - Windows 10 (880017)</li>
        <ul>
          <li>SKU Name: _same name_ (880170)</li>
        </ul>
        <br />
        <li>Product Name: CYBERPOWERPC Gamer Xtreme VR Gaming PC - Windows 10 (880018)</li>
        <ul>
          <li>SKU Name: _same name_ (880180)</li>
        </ul>
        <br />
        <li>Product Name: Acer Aspire 5 Slim Laptop - Windows 10 (880019)</li>
        <ul>
          <li>SKU Name: _same name_ (880190)</li>
        </ul>
        <br />
        <li>Product Name: Jumper EZbook X3 Windows 10 Laptop (880020)</li>
        <ul>
          <li>SKU Name: _same name_ (880200)</li>
        </ul>
        <br />
        <li>Product Name: Acer Aspire z24 890 + Acer Aspire ATC 885 (880040)</li>
        <ul>
          <li>SKU Kit: _same name_ (880400)</li>
        </ul>
        <li>SkuComponents:</li>
        <ul>
          <li>1un of Acer Aspire Z24-890-UA91 AIO Desktop - Windows 10 (880015)</li>
          <li>1un of Acer Aspire TC-885-UA92 Desktop - Windows 10 (880017)</li>
        </ul>
    </details>
    <details>
      <summary>Category: Power tools (9287)</summary>
      <ul>
        <li>Product Name: BLACK+DECKER 20V MAX Drill & Home Tool Kit, 68 Piece (LDX120PK),Black/Orange (880009)</li>
        <ul>
          <li>SKU Name: _same name_ (880090)</li>
        </ul>
        <br />
        <li>Product Name: BLACK+DECKER 20V MAX Cordless Drill / Driver with 30-Piece Accessories (LD120VA) (880010)</li>
        <ul>
          <li>SKU Name: _same name_ (880100)</li>
        </ul>
        <br />
        <li>Product Name: BLACK+DECKER 20V Max Cordless Chainsaw, 10-Inch, Tool Only (LCS1020B) (880011)</li>
        <ul>
          <li>SKU Name: _same name_ (880110)</li>
        </ul>
        <br />
        <li>Product Name: BLACK+DECKER 20V MAX Cordless Drill Combo Kit, 2-Tool (BD2KITCDDI),Black/Orange Impact Combo
          Kit (880012)</li>
        <ul>
          <li>SKU Name: _same name_ (880120)</li>
        </ul>
        <br />
        <li>Product Name: BLACK+DECKER 20V MAX 5-1/2-Inch Cordless Circular Saw, Tool Only (BDCCS20B) (880013)</li>
        <ul>
          <li>SKU Name: _same name_ (880130)</li>
        </ul>
        <br />
        <li>Product Name: BLACK+DECKER 20V MAX 5-1/2-Inch Cordless Circular Saw (BDCCS20C) (880014)</li>
        <ul>
          <li>SKU Name: _same name_ (880140)</li>
        </ul>
    </details>
  </ul>
  </ul>
  <hr />
</details>

#### Attachments

##### Customization

<details><hr/>
  <summary>View Sample Data</summary>
    <ul>
    <li>Name: T-Shirt Customization (T-Shirt Name - 15 characters)</li>
    <li>Products: adidas Men's Performance Polo - Blast Blue (880001)</li>
    </ul>
<hr/></details>

##### Subscriptions

It is mandatory to [follow these additional steps](https://help.vtex.com/tutorial/como-configurar-assinatura-v2--1FA9dfE7vJqxBna9Nft5Sj#2-how-to-install-the-subscription-app) if you want to enable subscriptions.

<details><hr/>
  <summary>View Sample Data</summary>
    <ul>
    <li>Name: Subscription</li>
    <li>Products: All from category Food and beverage (9282)</li>
    </ul>
<hr/></details>

### Prices

This resource sets sample prices and price tables.

#### Most products

<details><hr/>
  <summary>View Sample Data</summary>
    <ul>
      <li>ListPrice: 30.00</li>
      <li>BasePrice: between 50.00 and 2000.00</li>
      <li>Markup: 0%</li>
    </ul>
    <hr/></details>

#### Quantity prices

<details>
  <summary>View Sample Data</summary>
    <ul>
      <li>Product Name: BLACK+DECKER 20V MAX Cordless Drill / Driver with 30-Piece Accessories (LD120VA) (880100)</li>
      <li>ListPrice: null</li>
      <li>BasePrice: 100.00</li>
      <li>FixedPrices:</li><ul>
      <li>Minimum Quantity: 1</li>
      <li>Value: 100.00</li>
      <li>Minimum Quantity: 10</li>
      <li>Value: 90.00</li>
      <li>Minimum Quantity: 50</li>
      <li>Value: 80.00</li>
      <li>Minimum Quantity: 100</li>
      <li>Value: 70.00</li></ul>
    </ul>
</details>

#### Price Tables

<details><hr/>
  <summary>View Sample Data</summary>
    <ul>
      <li>Name: silver</li>
      <ul>
        <li>Percentual Modifier: -5%</li>
      </ul>
      <br/>
      <li>Name: gold</li>
      <ul>
        <li>Percentual Modifier: -10%</li>
      </ul>
      <br/>
      <li>Name: platinum</li>
      <ul>
        <li>Percentual Modifier: -15%</li>
      </ul>
    </ul>
    <hr/></details>

### Payments

This resource sets 3 affiliations (Promissory, Test and CreditControlV2), the custom payment Promissories and the payment condition using them, the VISA credit card condition and the Customer Credit condition.

<details><hr/>
  <summary>View Sample Data</summary>
    <ul>
      <li>Affiliation: Promissory</li>
      <ul>
        <li>Custom Payment: Promissory (201)</li>
        <li>Payment Condition: Promissory</li>
      </ul>
      <br/>
      <li>Affiliation: Test</li>
      <ul>
        <li>Payment Condition: VISA (credit card)</li>
      </ul>
      <br/>
      <li>Affiliation: CreditControlV2</li>
      <ul>
        <li>Payment Conditions:</li>
        <li>15 days (0% interest)</li>
        <li>30 days (0% interest)</li>
        <li>15 and 30 days (1% interest)</li>
        <li>15, 30 and 45 days (1.5% interest)</li>
      </ul>
    </ul>
<hr/></details>

### Benefits

This resource sets a Progressive Discount promotion.

<details><hr/>
  <summary>View Sample Data</summary>
    <ul>
      <li>Name: Progressive Discount</li>
      <li>Conditions:</li>
      <li>Start: 2010-01-01</li>
      <li>End: 2070-01-01</li>
      <li>Collection: All</li>
      <li>Benefit:</li>
      <ul>
        <li>Quantity: 5</li>
        <li>Discount: 5%</li>
        <li>Quantity: 10</li>
        <li>Discount: 15%</li>
        <li>Quantity: 15</li>
        <li>Discount: 25%</li>
        <li>Quantity: 20</li>
        <li>Discount: 35%</li>
      </ul>
    </ul>
    <hr/></details>

### Taxes

This resource sets VAT and ICMS taxes.

<details><hr/>
  <summary>View Sample Data</summary>
    <ul>
      <li>Name: VAT</li><ul>
      <li>Condition:</li>
      <li>Start: 2010-01-01</li>
      <li>End: 2070-01-01</li>
      <li>Category: Agribusiness (9284)</li>
      <li>Tax: 5%</li></ul>
      <br/>
      <li>Name: ICMS</li><ul>
      <li>Condition:</li>
      <li>Start: 2010-01-01</li>
      <li>End: 2070-01-01</li>
      <li>Category: Agribusiness (9284)</li>
      <li>Tax: 12%</li></ul>
    </ul>
    <hr/></details>

### Logistics

This resource updates the **Logistics** module using sample docks, warehouse and carrier.

<details>
  <hr />
  <summary>View Sample Data</summary>
  <ul>
    <li>Freight Values:</li>
    <ul>
      <li>Country: BRA</li>
      <li>ZipCodeStart: 0</li>
      <li>ZipCodeEnd: 9999999</li>
      <li>Country: USA</li>
      <li>ZipCodeStart: 0</li>
      <li>ZipCodeEnd: 99999999</li>
    </ul>
    <br />
    <li>Docks:</li>
    <ul>
      <li>Name: Doca Principal (1)</li>
      <ul>
        <li>Country: BRA</li>
      </ul>
      <li>Name: Main Dock (2)</li>
      <ul>
        <li>Country: USA</li>
      </ul>
    </ul>
    <br />
    <li>Warehouse:</li>
    <ul>
      <li>Name: Estoque (1_1)</li>
      <li>Docks:</li>
      <ul>
        <li>Doca Principal (1)</li>
        <li>Main Dock (2)</li>
      </ul>
    </ul>
    <hr />
</details>

### Organizations

This resource creates Master Data schemas that are necessary to set up **Roles and Permissions** in your store's Admin, as described in [this guide](https://developers.vtex.com/vtex-developer-docs/docs/installing-the-b2b-store-theme#create-master-data-schemas).
