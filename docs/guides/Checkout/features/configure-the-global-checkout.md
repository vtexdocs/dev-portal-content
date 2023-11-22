---
title: "Configure the Global Checkout"
slug: "configure-the-global-checkout"
hidden: false
createdAt: "2022-07-22T17:22:58.265Z"
updatedAt: "2022-10-20T17:37:14.332Z"
---

Global Checkout is a setting in your store that allows you to sell to many different countries regardless of the country of origin of your VTEX account.

For a complete Global Checkout experience, it is also important that your store be displayed in other languages. For more information about these settings, visit the article about [displaying store in another language](https://help.vtex.com/en/tutorial/displaying-the-store-in-another-language).

## New document and phone fields

To display document and phone typing options different from those used by the store country, follow the steps below:

1. On the Admin menu, access **Checkout**.
2. Click on the `blue gear` on the website you want to edit.
3. Select the **Code** tab.
4. On **Files**, click on `checkout6-custom.css`.
5. Add the code below.

  ```css
  /*Displays the option to enter a foreign document*/
  .document-box { display: block; }

  /*Displays the option to enter an international phone*/
  .phone-box { display: block; }
  ```

6. Click on `Save`.
   ![Document and Phone field](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/configure-the-global-checkout-0.png)

After saving this configuration, two new buttons will be shown in your Checkout:

- "I don't have CPF."
- "I don't have a Brazilian phone."

## New delivery and invoice addresses

### Deliveries

To allow deliveries to a new country (for example, you want to deliver products to a customer located in England), the following actions must be performed:

1. [Create a new carrier](https://help.vtex.com/en/tutorial/registering-a-carrier/).
2. For the new carrier, create a shipping worksheet with the column “Country”.

> ℹ️ The value of the column “Country” must be the 3-digit ISO code of the countries (e.g., for England, you will use the “GBR” value). To check the codes, we recommend the website `https://countrycode.org/`.

After defining the delivery settings for the countries intended, a new field will be shown on your checkout's delivery form, allowing the user to choose the desired international delivery option.

### Invoices

By unchecking the **My invoice address is the same as the delivery** box on the Checkout page, the user can enter a new invoice address among the available countries for delivery. However, nothing prevents this user from having an international credit card from other countries not available in your store.

To allow billing for a credit card whose invoice address is in another country, you must make on your store page a country select field appear on **Invoice Address**.

Also, if you want the option to display all countries in the Invoice Address field, you must enable it in your store layout (CSS) using the code below:

```css
/*Show all countries*/
.CountrySelector--all-countries { display: block; }

/*Hide delivery countries*/
.CountrySelector { display: none; }
```
