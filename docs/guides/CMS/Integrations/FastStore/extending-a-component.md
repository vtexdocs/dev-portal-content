---
title: "Creating a new section in the CMS"
hidden: false  
slug: "cms-extending-a-component"  
createdAt: "2026-02-19T12:50:00.813Z"  
updatedAt: "2026-04-30T11:48:00.813Z"  
---

> ⚠️ This guide applies only to stores using the [CMS](https://developers.vtex.com/docs/guides/cms-for-faststore-storefronts) with FastStore versions 3 or 4. For stores using Headless CMS, please refer to [this guide](https://developers.vtex.com/docs/guides/faststore/developing-and-overriding-components-creating-a-new-section).

To reuse an existing layout or behavior (such as a banner, hero, or product shelf), you can extend a component and adapt it to your store brand or business rules without rewriting everything from scratch. By extending rather than creating components from scratch, you maintain visual and technical consistency and reduce maintenance.

In this guide, you'll learn how to extend the **CallToAction** section in your FastStore project.

![call-to-action](https://vtexhelp.vtexassets.com/assets/docs/src/call-to-cation___e74ef106c68c9e8d1e99edb2e9840d7b.png)

> ℹ️ A **section** is a type of component that contains other components and acts as a dynamic container in page layouts. For more details, see [Understanding Components and Sections](https://developers.vtex.com/docs/guides/understanding-components-and-sections).

## Before you begin

<Steps>
### Install the CMS

Before extending a component, make sure the [CMS](https://developers.vtex.com/docs/guides/cms-for-faststore-storefronts) is enabled in your VTEX account. The CMS provides the Admin interface to configure and publish the **CallToAction** section you build in this guide.

> ⚠️ The CMS is currently available for stores running Faststore v3 and [FastStore v4](https://developers.vtex.com/docs/guides/faststore/developer-tools-updating-the-cli-package-version). If your store uses the [Headless CMS (legacy)](https://developers.vtex.com/docs/guides/faststore/headless-cms-overview), see the [Upgrading from Headless CMS (legacy) to CMS](https://developers.vtex.com/docs/guides/upgrading-from-headless-cms-legacy-to-cms-overview) track first.

### Install the Content plugin

After installing the CMS into your store account, install the Content plugin on your machine. For more information, see the [Content plugin](https://developers.vtex.com/docs/guides/content-plugin) guide.
</Steps>

## Instructions

### Step 1 - Creating the component

1. Open your store project in a code editor.
2. In the folder `src/components`, create the `CallToAction.tsx` file.
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
   
      CallToAction.$componentKey = 'CallToAction';
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
    vtex content generate-schema cms/faststore/components cms/faststore/pages -o cms/faststore/schema.json
    ```

8. Open the `schema.json` file and check if the section was added to the section list. It should look similar to this:

    ```json
    …  
    {  
        "$ref": "#/components/CallToAction"  
    }  
    …  
    ```

### Step 2 - Verify the component locally

Before syncing your changes with the CMS, run the storefront locally to confirm your new component compiles without errors. This catches typos, missing imports, and invalid schemas before you sync with the CMS.

1. In the project root, start the FastStore development server:

    ```bash
    yarn dev
    ```

2. Open the development server in your browser and check the terminal output for compilation errors related to `CallToAction`.

> ℹ️ The section won't render visually yet because it hasn't been added to any page in the CMS. This is done in [Step 4](#step-4---add-the-component-to-the-cms). At this point, you're only verifying that the development server starts and that your component code, schema, and registration are valid.

If the development server starts successfully and reports no compilation errors, you're ready to sync your changes with the CMS.

### Step 3 - Sync the changes with the CMS

Push the changes to sync with the CMS. Before doing it, make sure you're logged in to your VTEX account by running in the terminal the `vtex login {accountName}` command. Change the `{accountName}` to your store account, for example, `vtex login mystore`.

Push the schema generated to the CMS to reflect in the Admin. To do this, run the following command:

```shell
vtex content upload-schema -s faststore cms/faststore/schema.json
```

> ℹ️ The `-s {storeId}` parameter (in this case, `faststore`) specifies the store ID directly, so you won't be prompted to enter it when running the command.

### Step 4 - Add the component to the CMS

1. In the Admin, open **Storefront > Content**, and click an Entry, such as **Home**, to check whether the component was added.

   ![call-to-action-admin](https://vtexhelp.vtexassets.com/assets/docs/src/call-to-cation-admin___39afe92cbcd5c59606b7fa1db4ceb492.png)

2. Add the component and complete its fields.
3. Click `Save`.
4. With the FastStore development server still running from [Step 2](#step-2---verify-the-component-locally), refresh to preview the **CallToAction** section rendered with the values you just configured.
