---
title: "Running A/B tests"
slug: "vtex-io-documentation-running-native-ab-testing"
hidden: false
createdAt: "2020-06-03T16:02:44.475Z"
updatedAt: "2022-12-13T20:17:44.109Z"
category: "App Development"
seeAlso:
 - "/docs/guides/vtexarg-abtester"
---

In this guide, learn how to manage an A/B test, covering steps from running the test to concluding the test.

A/B testing involves comparing traffic between two store workspaces and helps you determine which one performs better in terms of user engagement and conversions.
To execute an A/B test, you can use the VTEX IO CLI or the [A/B Tester Admin app](https://developers.vtex.com/docs/guides/vtexarg-abtester).

## Before you start

Ensure you have the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference) installed on your machine.

## Running A/B tests via the Admin

The A/B Tester app allows you to run A/B tests via Admin. To use the app, follow these steps:

1. Open the terminal and log in to the desired account. *Remember to replace the values between curly brackets according to your account name.*

    ```bash
    vtex login {accountName}
    ```

2. Install the A/B Tester app in the `master` workspace to enable A/B testing on your store website by running:

    ```sh
    vtex use master
    vtex install vtex.ab-tester
    ```

3. Type `y` to confirm that you want to install the app in the `master` workspace.

4. Install the **A/B Tester Admin app** in the `master` workspace by running the following:

    ```sh
    vtex install vtexarg.abtester
    ```
  
5. Type `y` to confirm the installation.
6. Now, access the VTEX Admin and go to **Extensions Hub > Installed Apps > AB Tester**.
7. Refer to the [A/B Tester Admin app documentation](https://developers.vtex.com/docs/guides/vtexarg-abtester#usage) to create A/B tests, compare and finish tests.

## Running A/B tests via the VTEX IO CLI

### Step 1 - Enabling A/B testing

1. Open the terminal and log in to the desired account. *Remember to replace the values between curly brackets according to your account name.*
  
    ```sh
    vtex login {accountName}
    ```

2. [Create and switch to a Production workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-production-workspace) by running the following command:

    ```sh
    vtex use {workspaceName} --production
    ```

3. Perform the changes you want to test in the production workspace you are using. For example, install or edit an app.

    > ⚠️ If your store uses the [Checkout UI Custom](https://developers.vtex.com/docs/guides/vtex-checkout-ui-custom-v0) app, you must first publish its configurations on your new production workspace. Otherwise, you might experience undesired consequences, such as losing the Checkout custom Javascript code and styles.

4. Switch to the `master` workspace.

    ```sh
    vtex use master
    ```

5. Install the VTEX A/B tester app in the `master` workspace to enable A/B testing on your store website by running:

    ```bash
    vtex install vtex.ab-tester
    ```

    > ℹ️ You can run `vtex ls` to make sure that you have successfully installed `vtex.ab-tester` in the `master` workspace.

6. Run the following command in the `master` workspace.

    ```sh
    vtex workspace abtest start
    ```

    ![ab-testing-start-step1](https://vtexhelp.vtexassets.com/assets/docs/src/abtest-start___5c87b822a4829a1b74a8318510b00c4e.png)

7. Select the production workspace you want to use for comparison with the `master` and agree to proceed.

### Step 2 - Configuring the traffic and time

By agreeing to proceed with the test, you will need to answer the two following questions:

1. `What's the proportion of traffic initially directed to the master workspace?`

      You must answer this question with any whole number between 0 and 10000. For example, if you answer `9000`, you'll set 90% of the traffic to the `master` workspace.

      > ℹ️ To promote the changes from your production workspace in the safest way possible, we strongly recommend that you leave 90% of traffic dedicated to the `master` and the other 10% to the production workspace being tested.

2. `What's the amount of time respecting the restriction?`

    This is the amount of time (in hours) during which the traffic proportion stated in the previous question remains constant. After this period, the A/B testing system automatically balances the traffic proportions, sending more traffic to the best-performing workspace. There are two possible answers to this question:

| **Option** | **Description**                                                                                                                                                                                                                                                                                                                                                                            |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Answer `0` to automatically proceed with the A/B test.** | In this case, VTEX IO will automatically split your website traffic between workspaces, routing 50% of your store's traffic to the `master` and the other 50% to the production workspace being tested. Following that, the platform will automatically balance traffic every three minutes based on the conversion rates. This means that traffic will be gradually routed from the workspace with the lowest conversion rate to the workspace with the highest conversion rate. It's important to note that the test does not end on its own. We also suggest that you evaluate the test results on a daily basis. |
| **Answer with the number of hours you want to keep constant the proportion of traffic previously specified.** | During peak operational periods, it's critical for the test to extract as much data as possible. At the same time, the test shouldn't overextend and end up being harmful to users who are navigating the workspace with the poorest performance.                                                                                                                                                                                     |

  > ℹ️ You can run many A/B tests simultaneously by comparing two or more workspaces to the `master` individually. However, if you opt to set up the traffic manually, the A/B test will distribute the traffic evenly among all production workspaces being A/B tested. For example, suppose you started an A/B test between workspace A and `master`, routing 90% of traffic to the former and 10% to the latter. If you run a new A/B test between workspace B and the `master`, each production workspace, A and B, will only receive 5% of the store's traffic.

### Step 3 - Interpreting the test results

Any time during the A/B test, you can monitor the live results by executing the following command:

```sh
vtex workspace abtest status
```

![ab-testing-status-step3](https://vtexhelp.vtexassets.com/assets/docs/src/abtest-status___8ae7f35a70f9979b7294a5ba8b007c42.png)

You can still update the workspaces used in the A/B test if necessary. However, note that the fewer changes you make to these workspaces, the more accurate your results will be.

Before completing your A/B test, it is important to understand the comparative and final results of the two workspaces. The following presents the metrics available for both results:

#### Comparative results

| Metric                        | Description                                                                                           |
|------------------------------|-------------------------------------------------------------------------------------------------------|
| **Conversion**               | Conversion rate percentage exhibited by each workspace during the test.                            |
| **Expected Loss**            | Anticipated percentage of conversion loss for the store if the lower conversion rate workspace is selected as the winner (based on **Conversion** results). |
| **N. of Sessions**           | Total number of sessions for each workspace since the beginning of the test.                        |
| **N. of Sessions (last 24hrs)** | Number of sessions for each workspace in the past 24 hours during the test.                           |

#### Final results

| **Metric**                   | **Description**                                                                                                                                                                              |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Start Date**                  | Date and time for the beginning of the test.                                                                                                                                                |
| **Running Time**                | Test duration.                                                                                                                                                                               |
| **Probability B beats A**        | Probability, in percentage points, that the production workspace is better for your store than the current `master` workspace. This calculation is based on session and completed sales counts. If this metric is greater than 10%, the production workspace can become the winner. |
| **Winner**                      | Workspace you selected as the winner.                                                                                                                                                        |

> ⚠️ The main results of the A/B test are aimed at scenarios where the platform automatically directed store traffic. While you can and should use A/B tests even if you manually direct the traffic, bear in mind that the numbers behind each result reflect an automatic segmentation according to each workspace experience.

#### Validating the winner workspace

The best way to validate your A/B test workspace winner is to set a maximum conversion loss value according to your store operation size.

For example, you can set a maximum conversion loss of `0,0001%` when starting your test. Then, when either workspace achieves an `Expect Loss` result greater than `0,0001%`, you should end the test and declare a winner.

### Step 4 - Finishing the A/B test

If your test has already reached the time frame you have manually set for it, or if you have already detected a winner during [Step 3](#step-3---interpreting-the-test-results), run the following command in `master` to finish the test.

```sh
vtex workspace abtest finish
```

> ⚠️ If you have manually set a predefined time frame to run your A/B test, it's important that you pay attention to the test during this entire period. Although the platform automatically redistributes traffic according to how each workspace is behaving after the set time frame, overseeing the test is fundamental to its success.

Running the command will display a list of all workspaces being tested by the `vtex.ab-tester` app in the `master` environment. Choose the workspace that you intend to conclude. For example:

![ab-testing-finish-step4](https://vtexhelp.vtexassets.com/assets/docs/src/abtest-end___2940fdcba7933cab4d828ba9e7a34d72.png)

Now that you finish the A/B test, follow the next step to promote the workspace to `master``.

### Step 5 - Promoting the production workspace to master

Note that in the [Step 4](#step-4---finishing-the-ab-test) you only ended the test on the selected workspace. It did not promote any workspace to `master`. Follow these steps below to promote the production workspace to `master`.

1. Change to the production workspace to be promoted. *Remember to replace the values between curly brackets according to your workspace name.*

    > ℹ️ You must be logged in to your VTEX account.

    ```bash
    vtex use {workspaceName}
    ```

2. Promote the workspace being used.

    ```bash
    vtex workspace promote
    ```

Now, all your changes made in production are available in the master workspace.
