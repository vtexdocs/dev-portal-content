---
title: "Critical CSS"
slug: "vtex-render-server-criticalcss"
excerpt: "vtex.render-server@8.165.3"
hidden: true
createdAt: "2022-07-18T14:28:11.407Z"
updatedAt: "2022-07-18T14:28:11.407Z"
---
The content which a user first sees when opening a web page is known as above-the-fold. Besides, since this part of the page must be loaded quickly for a better user experience, it can also be referred to as critical. **Critical CSS is the minimum blocks of CSS code needed to first display the critical content of the page.**

## Requirements

For Critical CSS to work, the following conditions must be true:

1. The page is server-side rendered successfully
2. CSS Concatenation is enabled
3. Critical CSS is enabled to at least one of the following pages:
    - Home
    - Search
    - Product
    - Custom

> ℹ️ Even after it is enabled and all the requirements are met, pages rendered on development workspaces will **not** contain Critical CSS, since the CSS definitions for pages of this type of environment are constantly changing.


> 🔧 If you want to debug Critical CSS on development workspaces, make sure all the requirements are met and add the `__debugConcatenatedCSS` and `__debugCriticalCSS` query strings to the URL.


## How Critical CSS works on render-server?

> **TL;DR** render-server tries to load previously extracted Critical CSS. If it doesn't exist, only the regular styles (concatenated) with no Critical CSS are returned. If it exists, it returns the Critical CSS along with the (async loaded) concatenated CSS.
> 
> In both cases, after the SSR is complete, it compares the result of the SSR with the Critical CSS from the cache. If the Critical CSS doesn't exist yet, or there was an error, or there's any mismatching or missing classes, a new Critical CSS extraction happens and it's saved to the cache to be used next time.

First, it's important to understand that the first user to access a page will never receive Critical CSS in its response. That happens because the Critical CSS extraction happens after the SSR occurs, so if the page was never rendered until then, there is no Critical CSS to load.

Critical CSS also varies by viewport and the theme's app version. So even if one user has previously accessed a page and the Critical CSS is already extracted, subsequent users that access that page on different devices or after an update will **not** receive that same Critical CSS, as it may vary according to the screen dimensions or it may have been changed during app updates. In those cases, the Critical CSS is extracted again and it's stored considering the parameters mentioned above (read steps 3 and 4).

The processes that happen at each step of the Critical CSS inclusion and extraction will be detailed in the sections below.

### Step 1 - Loading previously extracted Critical CSS

During the rendering pipeline, on the `pages` middleware, the StylesProcessor is created. This object is mainly used to deal with Critical CSS and CSS Concatenation. After it detects Critical CSS is enabled, it fetches previously extracted Critical CSS from VBase.

The Critical CSS is not used right away. Since fetching it takes some time, this process starts here, but the resulting content is only used a few steps later. It may also not exist yet, but render-server doesn't deal with that here.

> ℹ️ To see how the Critical CSS is stored, take a look at the end of step 4.

### Step 2 - Loading Critical CSS state

Before streaming the `<head>` content to the browser on the last middleware of the rendering pipeline (`render`), render-server assembles all the style data the page requires.

The `getServerStyles` method is called. If Critical CSS is enabled, it starts loading the Critical CSS state. This state assembles into an object all the relevant information of the data loaded from VBase regarding Critical CSS.

This state also contains the status of the Critical CSS. This status represents 
if the loaded Critical CSS is `missing` (there was no file to load from VBase), if there was an error during a previous extraction (`error`), if the theme app has been updated or if its overrides or fonts have changed (`mismatching:theme`), if the base styles have changed (`mismatching:styles`), or if it matches the current style and font definitions (`matching`).

If Critical CSS isn't enabled or if its status is `missing` or `error`, it returns the regular styles (concatenated or not) right away.

In case it mismatches or matches the current style and font definitions, the critical state along with all the HTML CSS tags for critical and non-critical styles and fonts are returned. The non-critical CSS will all be `preload`ed, which means that, in this context, they'll be loaded asynchronously and will not block the rendering of the page, speeding up the page.

### Step 3 - Extracting Critical CSS

The process of extracting the Critical CSS is always asynchronous, so it never blocks the SSR. That's why the first user to access a page will never receive Critical CSS: it only happens after the page is server-side rendered.

The extraction of the Critical CSS also happens on the `render` middleware of the rendering pipeline. The method `extractCritical` is called and it starts by evaluating class mismatches.

Classes mismatches are only considered on product pages. Due to the variation present on this kind of page, even if it uses the same template, the CSS classes present on the HTML document for one product in relation to another can be drastically different.

(Case 0) If class mismatches should not be considered or if the Critical CSS state status is `missing` or `error`, the CSS classes saved as the `cssClasses` property are the ones used when rendering the page that just got requested. This property is only used in future extractions where the next condition is true.

If class mismatches should be considered and the status was different from `missing` and `error`, there are three possible cases:

1. No class was used for rendering. For some reason, the SSR didn't return any valid class that was used when rendering the page. If that's the case, the data of the current Critical CSS state is used for extracting it again (`cssClasses` and `appendableCritical`).

2. There was no `cssClasses` value on the current CSS Critical state. In this case, the classes mismatched, since there were rendered classes, but none of them was present on the current CSS Critical state. The status is updated to `mismatching:classes` and the CSS classes that were used when rendering the page that just got requested are defined as the `cssClasses` property, while `appendableCritical` property continues to be equal to the current Critical CSS value present on the CSS Critical state. Both will be used to extract it again.

3. There were classes used for rendering and there was `cssClasses` value on the current CSS Critical state. A set composed of the two collections of classes is created. This set of classes is used as the `cssClasses` property and the `appendableCritical` property continues to be equal to the current Critical CSS value present on the CSS Critical state. The status will be changed to `mismatching:classes` only if this new set of classes contains more classes than the previous `cssClasses` value on the CSS Critical state.


In short:
- Case 1 tries to refine the extraction of currently existing critical if the rendered page somehow doesn't contain any classes. 
- Case 2 is very rare, and it acts as a way to extract Critical CSS even when, on case 0 (on a previous render), the rendered page didn't contain any classes (similar to case 1), but the extraction still happened.
- Case 3 updates the `cssClasses` in case there were any missing classes that should have been included previously. That might happen due to the variations mentioned earlier.

Even after this process, it's not always that the Critical CSS is actually extracted. It may skip extracting if it has already been extracted a few minutes earlier.

It skips the extraction if the previous extraction was generated up to 6 hours earlier when the status is `matching`, and only up to 10 minutes if the status is `error` or `mismatching:styles`. If the status is `mismatching:classes`, `mismatching:theme` or `missing`, the extraction happens immediately. 

If the extraction should happen, all the HTML of the page rendered on the server, the styles, and previous Critical CSS information are sent to a `vtex.critical-css-extractor` app's service. This service is responsible for emulating a browser (using puppeteer) and rendering this page again. After it does that, it extracts only the CSS classes being used by the visible HTML elements (considering the viewport). If there's any previous Critical CSS information, it merges it with the resulting Critical CSS and returns the merged Critical CSS back to render-server. 

If there was render-server receives no extracted Critical CSS and the previous Critical CSS state status was different from `missing`, it doesn't save this extraction.

### Step 4 - Saving Critical CSS

If everything went ok, the newly extracted Critical CSS is saved to VBase along with the style references, page HTML, an updated date identifying when it was generated and the CSS classes obtained when evaluating class mismatches (`cssClasses`).

The path to the JSON file has the following structure (the same is used to load previous attempts on Step 1):
`attempt/{app_name_with_version_and_name_of_critical_template}_width={screen_width}_height={screen_height}.json`

Example:
`attempt/tokstoksponsorio_store_theme_0_39_0_store_product_width=1920_height=1280.json`

After the file is saved, the process of generating Critical CSS ends.