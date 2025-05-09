---
title: "Extending My Account"
---

In this guide, you'll learn how to extend the **My Account** page by creating new pages or adding new sections to the default pages.

Check if the [default My Account pages](https://developers.vtex.com/docs/guides/faststore/my-account-overview#default-my-account-pages) meet your needs. If not, you can [create a new page](#creating-new-pages) or [add a new section](#adding-new-sections) to better fit your requirements. These extensions allow you to customize the My Account experience without changing the default structure.

## Creating new pages

To create a new page for **My Account**, follow these steps:

1. Open your FastStore project using the code editor of your choice.
2. Open the `src` folder.
3. Create a folder named `pages` and, within it, create another folder named `account`, or open it if it already exists.
4. In the `src/pages/account` folder, create a `.tsx` file for your new **My Account** page. Take the following example:
	
    ```js src/pages/account/page-test.tsx
    export default function PageTest() {
    return (
        <div>
        <h1>Hello team</h1>
        </div>
    );
    }
    ```

Next, you must enable this new page as a valid route:

1. Create the `myAccount` folder in the `src` directory, or open it if it already exists.
2. In the `src/myAccount` folder, create a file named `navigation.ts`.
3. In the `src/myAccount/navigation.ts` file, import the `getMyAccountRoutes` function from `@faststore/core` and set the new route as in the following example:

    ```ts src/myAccount/navigation.ts mark=[5:7]
    import { getMyAccountRoutes } from "@faststore/core";

    export default getMyAccountRoutes({
    routes: [
        {
        route: "/account/page-test",
        title: "Page test",
        },
    ],
    });
    ```

Once you finish these steps, the new page will appear as an option in the **My Account** menu.

![page-test-my-account](https://vtexhelp.vtexassets.com/assets/docs/src/new-page___e41daa56a05a4783e974a6c7cec08d59.png)

## Adding new sections

To add a new section to a [default My Account page](https://developers.vtex.com/docs/guides/faststore/my-account-overview#default-my-account-pages), follow these steps:

1. Open your FastStore project using the code editor of your choice.
2. Open the `src/myAccount/extensions/{pageName}` folder, where `pageName` is one of the default My Account pages. Example: `src/myAccount/extensions/orders/`
3. In the `src/myAccount/extensions/{pageName}` folder, create two files: `before.tsx` and `after.tsx`. Use the `before.tsx` file to add a section before the existing content of the default page, and use `after.tsx` to insert a section after the existing content.

For example, to add a section after the order details page, you would implement the following:
	
```js src/myAccount/extensions/orders/[id]/after.tsx
function After() {
  return <div>After the default sections, this section is shown :)</div>
}

export default After
```

>ℹ️ Every default page can have `before.tsx` and `after.tsx` extension sections.

Based on the example given, the new section will be placed after the current content on the order details page:

![new-section-my-account](https://vtexhelp.vtexassets.com/assets/docs/src/new-section___1ff45ac89fb0c8629c705bdc6b5deb36.png)
