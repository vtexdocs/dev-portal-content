---
title: "Extending a component"  
hidden: false  
slug: "cms-extending-a-component"  
createdAt: "2026-02-19T12:50:00.813Z"  
updatedAt: "2026-04-30T11:48:00.813Z"  
---

> ⚠️ This guide is valid only for [FastStore stores running v4](https://developers.vtex.com/docs/guides/faststore/developer-tools-updating-the-cli-package-version) or higher and using the [CMS](https://developers.vtex.com/docs/guides/cms-for-faststore-storefronts). For stores using a FastStore version below v4, refer to [this guide](https://developers.vtex.com/docs/guides/faststore/developing-and-overriding-components-creating-a-new-section).

To reuse an existing layout or behavior (such as a banner, hero, or product shelf), you can extend a component and adapt it to your store brand or business rules without rewriting everything from scratch. By extending rather than creating components from scratch, you maintain visual and technical consistency and reduce maintenance.

In this guide, you will learn how to extend the **CallToAction** section in your FastStore project.

![call-to-action](https://vtexhelp.vtexassets.com/assets/docs/src/call-to-cation___e74ef106c68c9e8d1e99edb2e9840d7b.png)

> ℹ️ In FastStore and CMS, a **section** is a type of component that contains other components and acts as a dynamic container in page layouts. For more details, see [Understanding Components and Sections](https://developers.vtex.com/docs/guides/understanding-components-and-sections).

## Before you begin

### Install the CMS

Before extending a component, make sure the [CMS](https://developers.vtex.com/docs/guides/cms-for-faststore-storefronts) is enabled in your VTEX account. The CMS provides the Admin interface to configure and publish the **CallToAction** section you build in this guide.

To check whether the CMS is available in your account, log in to your VTEX Admin and go to **Storefront > Content**.

- If the **Content** option appears, the CMS is already enabled and you can proceed to the [next section](#install-the-content-plugin).
- If the **Content** option is not available, [open a ticket with VTEX Support](https://help.vtex.com/en/support) requesting the CMS to be enabled in your account.

> ⚠️ The CMS is currently available for stores running [FastStore v4](https://developers.vtex.com/docs/guides/faststore/developer-tools-updating-the-cli-package-version) or higher. If your store uses the [Headless CMS (legacy)](https://developers.vtex.com/docs/guides/faststore/headless-cms-overview), refer to the [Upgrading from Headless CMS (legacy) to CMS](https://developers.vtex.com/docs/guides/upgrading-from-headless-cms-legacy-to-cms-overview) track first.

### Install the Content plugin

After installing the CMS into your store account, install the Content plugin on your machine. For more information, see the [Content plugin](https://developers.vtex.com/docs/guides/content-plugin) guide.

## Instructions

### Step 1 - Creating the component

1. Open your store project in a code editor.  
2. In the folder `src/components`, create the file `CallToAction.tsx`.  
3. Add the following code to the `CallToAction.tsx` file:  

   ```tsx  
   import React from "react";  

   export interface CallToActionProps {  
     title: string;  
     link: {  
       text: string;  
       url: string;  
     };  
   }  
     
   export default function CallToAction(props: CallToActionProps) {  
     return (  
       <section>  
         <h2>{props.title}</h2>  
         <a href={props.link.url}>{props.link.text}</a>  
       </section>  
     );  
   }  
   ```

4. Export the `CallToAction` component in the `index.tsx` file.  

   ```tsx  
   …  
   import CallToAction from './CallToAction'  
     
   export default {  
       …  
       CallToAction  
   }  
   ```

5. Create the file for the component that will be a section. In `cms/faststore/components`, create the `cms_component__CallToAction.jsonc` file.  
6. In the `cms_component__CallToAction.jsonc` file, add the following:  

   ```jsonc  
   {  
     "$extends": [  
       "#/$defs/base-component"  
     ],  
     "$componentKey": "CallToAction",  
     "$componentTitle": "Call To Action",  
     "title": "Call To Action",  
     "description": "Get your 20% off on the first purchase!",  
     "type": "object",  
     "required": [  
       "title",  
       "link"  
     ],  
     "properties": {  
       "title": {  
         "title": "Title",  
         "type": "string"  
       },  
       "link": {  
         "title": "Link Path",  
         "type": "object",  
         "required": [  
           "text",  
           "url"  
         ],  
         "properties": {  
           "text": {  
             "title": "Text",  
             "type": "string"  
           },  
           "url": {  
             "title": "URL",  
             "type": "string"  
           }  
         }  
       }  
     }  
   }  
   ```

7. Generate the final schema to add the new section. To do this, run the following command in a terminal:

    ```bash  
    vtex content generate-schema cms/faststore/components cms/faststore/pages -o cms/faststore/schema.json -b vtex.faststore  
    ```

8. Open the `schema.json` file and check if the section was added to the section list. It will probably be like that:

    ```json  
    …  
    {  
        "$ref": "#/components/CallToAction"  
    }  
    …  
    ```

### Step 2 - Verify the component locally

Before syncing your changes with the CMS, run the storefront locally to confirm your new component compiles without errors. This catches typos, missing imports, and invalid schemas before involving the CMS.

1. In the project root, start the FastStore development server:

    ```bash
    yarn dev
    ```

2. Open the development server in your browser and check the terminal output for compilation errors related to `CallToAction`.

> ℹ️ The section will not render visually yet because it has not been added to any page in the CMS, which is done in [Step 4](#step-4---add-the-component-to-the-cms). At this point, you are only verifying that the dev server starts and that your component code, schema, and registration are valid.

If the dev server starts successfully and reports no compilation errors, you are ready to sync your changes with the CMS.

### Step 3 - Sync the changes with the CMS

Push the changes to sync with the CMS. Before doing it, make sure you are logged in to your VTEX account by running in the terminal the `vtex login {accountName}` command. Change the `{accountName}` to your store account, for example, `vtex login mystore`.

Push the schema generated to the CMS to reflect in the Admin. To do this, run the following command:

```shell
vtex content upload-schema cms/faststore/schema.json
```

### Step 4 - Add the component to the CMS

1. Go to the Admin, open **Storefront > Content**, and click a Content-Type, such as **Home**, to check whether the component was added.

    ![call-to-action-admin](https://vtexhelp.vtexassets.com/assets/docs/src/call-to-cation-admin___39afe92cbcd5c59606b7fa1db4ceb492.png)

2. Add the component and fill in its fields.  
3. Click `Save`.
4. With the FastStore development server still running from [Step 2](#step-2---verify-the-component-locally), refresh the server to preview the **CallToAction** section rendered with the values you just configured.
