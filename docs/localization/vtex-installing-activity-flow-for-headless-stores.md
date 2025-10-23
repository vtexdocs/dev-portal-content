---
title: "Installing Activity Flow for Headless stores"
slug: "vtex-installing-activity-flow-for-headless-stores"
excerpt: "Learn how to install Activity Flow in your Headless store."
hidden: false
createdAt: "2025-10-23T13:37:06.246Z"
---

In this guide, you'll learn how to install and configure the Activity Flow script in your Headless store.

## Before you begin

## Intructions

### Step 1 - Adding the Activity Flow script asynchronously

To reduce the impact on page load times, install the Activity Flow script asynchronously. Add the following code snippet inside the <head> tag of every HTML page you want to monitor:

```javascript
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

To distinguish the origin of events, define the script parameters. Add a new script in the <head> tag, after the Activity Flow script, with the following structure:

```javascript
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

```javascript
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
