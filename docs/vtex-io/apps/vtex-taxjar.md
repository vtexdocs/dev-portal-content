---
title: "TaxJar"
slug: "vtex-taxjar"
excerpt: "vtex.taxjar@0.6.2"
hidden: true
createdAt: "2022-07-26T20:00:23.925Z"
updatedAt: "2022-07-26T21:33:01.624Z"
---
The TaxJar app uses the TaxJar API to calculate taxes.  Optionally, invoiced orders will be recorded in TaxJar for reporting.

## Configuration

### Step 1 - Create API Token in TaxJar

- [Sign up for TaxJar](https://partners.taxjar.com/English)
- [How do I get a TaxJar sales tax API token?](https://support.taxjar.com/article/160-how-do-i-get-a-taxjar-sales-tax-api-token)

### Step 2 - Install the TaxJar app

Using your terminal, log in to the desired VTEX account and run the following command:
`vtex install vtex.taxjar`

### Step 3 - Defining the app settings
![image](https://user-images.githubusercontent.com/47258865/118002998-2b2db400-b316-11eb-9f09-13df44be8086.png)
1. Enter the API Token.
2. Choose optional settings
- **Production Mode** - The entered API Token is a Live token.
- **Enable TaxJar inb checkout** - Request tax calculations.
- **Post completed transactions to TaxJar** - Record invoiced orders in TaxJar
- **Post marketplace transactions to TaxJar** - Record invoiced marketplace orders in TaxJar
3. Save Settings.
4. Test Connection.

### Step 4 - Adding customer exemptions

1. Fill in all fields, making sure that the email used is a valid VTEX account.
2. Currently, the application supports up to three exempt US states for a user.

### Notes

- Pickup points are used to determine nexus addresses.  Must be tagged with 'TaxJar'
![image](https://user-images.githubusercontent.com/47258865/119150454-759ce800-ba1c-11eb-84cb-d1386380e3ca.png)
- Product tax codes are entered in Catalog -> Products and SKUs -> Tax Code.
- An order transaction is created in TaxJar when an order is invoiced.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!