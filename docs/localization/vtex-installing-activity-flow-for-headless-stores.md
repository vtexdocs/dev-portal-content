---
title: "Installing Activity Flow for Headless stores"
slug: "vtex-installing-activity-flow-for-headless-stores"
excerpt: "Learn how to install Activity Flow in your Headless store."
hidden: false
createdAt: "2025-10-23T13:37:06.246Z"
---

In this guide, you'll learn how to install and configure the [Activity Flow](LINK) script in your Headless store.

This setup allows Activity Flow to capture real user interactions and send them to VTEX for analysis, enabling insights into performance, engagement, and shopper behavior.

## Intructions

### Step 1 - Adding the Activity Flow script asynchronously

Activity Flow relies on a client-side script to collect navigation data. 

To ensure that it doesn’t delay page rendering, you must load the script asynchronously.

1. Open your headless storefront project. 
2. Inside the `<head>` tag of each page you want to monitor, add the following snippet:

```js
<script>
     (function(v,t,e,x,a,f,s){

f=v.vtexaf=v.vtexaf||function(){(f.q=f.q||[]).push(arguments)};
          f.l=+new Date;s=t.createElement(e);s.async=!0;
          s.src=x;a=t.getElementsByTagName(e)[0];
          a.parentNode.insertBefore(s,a)

})(window,document,'script','https://activity-flow.vtex.com/af/af.js');
</script>
```

### Step 2 - Defining default parameters

Next, configure your store’s identification parameters.

These settings allow Activity Flow to recognize which account, environment, and workspace the events belong to.

1. Add a new script in the `<head>` tag, right after the Activity Flow script, with the following structure:

```js
<script>
window.vtexafenv = {
   account: '<ACCOUNT NAME>',
   env: '<ENVIRONMENT TYPE>',
   workspace: '<WORKSPACE TYPE>'
};
</script>
```

- `account` (required): Name of your VTEX account.
- `env` (optional): Environment type. For example, `prod` or `test`.
- `workspace` (optional): The workspace name, useful for A/B testing or distinguishing between environments.

>ℹ️ Replace the values between the curly brackets with your account, environment, and workspace names.

### Step 3 - (Optional) Merging scripts

You can combine both the script loader and the parameter definition into a single script block. Add the following code to the <head> tag:

```js
<script>
     (function(v,t,e,x,a,f,s){

f=v.vtexaf=v.vtexaf||function(){(f.q=f.q||[]).push(arguments)};
          f.l=+new Date;s=t.createElement(e);s.async=!0;
          s.src=x;a=t.getElementsByTagName(e)[0];
          a.parentNode.insertBefore(s,a)

})(window,document,'script','https://activity-flow.vtex.com/af/af.js');
window.vtexafenv = {
   account: '<ACCOUNT NAME>',
   env: '<ENVIRONMENT TYPE>',
   workspace: '<WORKSPACE TYPE>'
};
</script>
```

### Step 4 - Check the script

To validate if the script is installed in your store, follow the steps below:

1. Open the page where you set up the script.
2. Open the **DevTools** and go to **Network** tab.
3. Search for `af.js` and click it.
4. In the **Header** tab, confirm if the **Request URL** is `https://activity-flow.vtex.com/af/af.js`.
5. Check in the console if there are errors. You can also trigger a monitorable action to see events.

![dev_tools_af](https://vtexhelp.vtexassets.com/assets/docs/src/dev_tools_af___1d5b729dddb7926ba5678e8a1a1541e2.png)

If the `af.js` file doesn't appear in the Network tab, confirm that the snippet is in the `<head>` of the page and that there are no script blockers. If the setup is correct and the problem persists, open a ticket with [VTEX Support](https://help.vtex.com/en/support).
