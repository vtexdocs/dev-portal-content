---
title: "AB Tester"
slug: "vtexarg-abtester"
excerpt: "vtexarg.abtester@1.0.12"
hidden: false
createdAt: "2021-10-21T15:14:07.237Z"
updatedAt: "2022-07-21T17:37:37.156Z"
---

The A/B Tester app allows you to list, start and finish A/B tests via the VTEX Admin.

![A/B Tester Settings](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtexarg-abtester-0.png)

In the following, you'll learn how to install and use the A/B Tester app.

---

## Configuration

Take the following steps to install the AB Tester app on your VTEX Admin.

1. Open the terminal and use the [VTEX IO CLI](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-installation-and-command-reference) to log in to the desired VTEX account.
2. Install the A/B Tester app in the `master` workspace to enable A/B testing on your store website by running:

    ```sh
    vtex use master
    vtex install vtex.ab-tester
    ```

3. Install the **A/B Tester Admin app** in the `master` workspace:

   ```sh
   vtex install vtexarg.abtester
   ```

## Usage

After installing the AB Tester app, you'll be able to:

- Create A/B tests.
- Compare A/B test results.
- Finish an A/B test.

### Creating an A/B test

In the following step by step, you will learn how to set up a new A/B test. Notice that, before proceeding any further, you must already have a [production workspace](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-creating-a-production-workspace) containing the changes you want to evaluate.

1. Access the VTEX Admin.
2. Go to **Others > AB Tester**.
3. Click on **Create new AB test**.
4. Fill out the presented fields as in the following:
   - **Workspace Name -** Enter the name of the production workspace containing the changes you want to examine via the A/B test.
   - **Traffic Proportion -** Enter the desired traffic proportion to be destined for the **master** workspace during the first hours of the A/B test. This value must be any whole number between 0 and 10000. For example, to set 90% of the traffic to the master workspace, enter 9000.
   - **Amount of Time -** Enter the amount of time (in hours) during which the specified **Traffic Proportion** will be maintained. After this period, the traffic proportions of the test will be automatically updated by the A/B testing system. Enter `0` if you prefer the A/B testing system to take care of your website traffic distribution from the start.
     > ℹ️ The A/B testing automatically balances traffic every 3 minutes according to the conversion or revenue rates.
   - **Test Type -** Enter what the A/B test must evaluate: revenue or conversion.
5. Click on **Save**.

Once you save your changes, the A/B test will start immediately, splitting your website traffic according to your preferences.

### Comparing results

After creating your A/B test, the **AB Tester** app will provide a table containing some metrics that will help you evaluate and interpret the test status. This table contains the following information:

- **Conversion** - Conversion rate percentage that each workspace presented during the test.
- **Conversion (last 24hrs)** - Conversion rate percentage that each workspace presented during the test's last 24 hours.
- **N. of Sessions** - Total number of sessions of each workspace since the beginning of the test.
- **N. of Sessions (last 24hrs)** - Number of sessions for each workspace during the test's last 24 hours.

### Finishing an A/B Test

Although automatic, an A/B test will not end by itself. Take the following steps to terminate an A/B test:

1. Access the VTEX Admin.
2. Go to **Others > AB Tester** and scroll the horizontal bar until you see a Kebab menu.
3. Click on the Kebab menu and click on **Finish A/B Test**.

---

## Related Resources

- [Running native A/B tests](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-running-native-ab-testing)