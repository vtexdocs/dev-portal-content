---
title: "Wordpress Integration"
slug: "vtex-wordpress-integration"
excerpt: "vtex.wordpress-integration@2.22.0"
hidden: false
createdAt: "2020-06-03T15:19:10.536Z"
updatedAt: "2022-12-15T16:50:19.073Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->

The Wordpress Integration app provides a way to bring in blog data from the Wordpress API and create a blog homepage, category pages, and blog post pages on your store, using your existing store header, footer, and styling.

## Configuration

### Step 1 - Installing the Wordpress Integration app

Using your terminal and [VTEX IO Toolbelt](https://vtex.io/docs/recipes/development/vtex-io-cli-installation-and-command-reference/#command-reference), log in to the VTEX account you are working on and [install](https://vtex.io/docs/recipes/store/installing-an-app) the `vtex.wordpress-integration@2.x` app.

### Step 2 - Defining the app settings

In your VTEX account's admin, perform the following actions:

1. Access the **Apps** section and then **My Apps**.
2. Select the **Wordpress Integration** app box and open the Settings section.
3. If your VTEX store uses multiple bindings, enable the **configuration by binding** option to configure the app settings specific to each binding.
4. Enter your **Wordpress URL**. This should be the domain where the Wordpress API endpoint is hosted and Wordpress is administered.
5. If your Wordpress installation's API is hosted under a path other than `wp-json/wp/v2/`, enter the path in the **Wordpress API path** field. For example, if the `posts` endpoint looks like `https://example.wordpress.com/index.php?rest_route=/wp/v2/posts`, enter `index.php?rest_route=/wp/v2/` here. If unsure, leave the field blank.
6. Enter the **Title tag for block homepage** which will determine the title tag for the Wordpress portions of your store.
7. Enter the **Store blog home path** which is used to include Wordpress posts in the sitemap and be indexed by search engines. For example, the path to your store's blog is www.my-store.com/blog, you would enter 'blog'.
8. Select the filters that you want to show, this filters will appear as part of the pagination in both search posts and all posts views, you can filter by category, tag, and/or date.
9. Save your changes.

⚠️ If you have a security plugin installed on your WordPress installation (such as WordFence), ensure it is not blocking requests to `/users` or `/?author=N` queries.

ℹ️ _The settings option `Create Sitemap Entries` will likely not need to be modified. This setting tells the app to create the initial sitemap entries. Once this is done, the app programmatically updates this setting to prevent duplicate sitemap entires._

### Step 3 - Creating the blog pages

It is time to create the store pages that will host the blog content. Before performing the following actions, make sure you already are logged into the desired VTEX account and working on a [Developer workspace](https://vtex.io/docs/recipes/development/creating-a-development-workspace/).

1. Open your Store Theme app in your code editor.
2. Add the `wordpress-integration` app as a `peerDependency` in your theme's `manifest.json` file:

```diff
 "peerDependencies": {
+  "vtex.wordpress-integration": "2.x"
 }
```

3. In the `store/routes.json` file, create paths for the blog's new pages as shown below:

```json
"store.blog-home": {
	"path": "/blog"
},
"store.blog-category": {
	"path": "/blog/category/:categoryslug_id"
},
"store.blog-post": {
	"path": "/blog/post/:slug_id"
},
"store.blog-search-result": {
	"path": "/blog/search/:term_id"
}
```

ℹ️ _You may change `blog` in each route to another string of your choosing._

| Blog page                  | Description                                                                                                                             |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `store.blog-home`          | The homepage of your blog. This can also be extended (i.e. `store.blog-home#custom`) to create additional custom blog pages, if needed. |
| `store.blog-category`      | A listing of blog posts belonging to a particular category, derived from a category slug in the page route.                             |
| `store.blog-post`          | A detail view of a single blog post, derived from a post slug in the page route.                                                        |
| `store.blog-search-result` | A listing of blog posts matching a search query, derived from a search term in the page route.                                          |

If you wish to display WordPress **pages** on your store site in addition to **posts**, you can add a route like the one shown below:

```json
"store.custom#blog-page": {
	"path": "/blog/page/:slug"
}
```

In addition to that, you can optionally add `:page` parameters for URL-controlled pagination. For example:

```json
"store.blog-home": {
	"path": "/blog(/page/:page)"
},
"store.blog-category": {
	"path": "/blog/category/:categoryslug_id(/page/:page)"
},
"store.blog-search-result": {
	"path": "/blog/search/:term_id(/page/:page)"
},
```

If the `:page` parameter is not provided, pagination can alternatively be controlled by query string, such as `/blog/category/example-category?page=2` .

### Step 4 - Declaring the pages' blocks

Once the routes are set up, you may populate each blog page with blocks.

The Wordpress Integration app provides the following blocks for your use:

| Block name                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `blog-all-posts.wordpress-all-posts`                       | Paginated list of all blog posts, starting with the most recent. Recommended to be placed on `store.blog-home` page.                                                                                                                                                                                                                                                                                                                                                                                                            |
| `blog-category-list.wordpress-category-list`               | Paginated list of blog posts from a specific category. This must be placed on the `store.blog-category` page, as the category slug is provided by the parameter in the page route.                                                                                                                                                                                                                                                                                                                                              |
| `blog-post-details.wordpress-post-details`                 | Shows the details for a single blog post. This must be placed on the `store.blog-post` page, as the post slug is provided by the parameter in the page route.                                                                                                                                                                                                                                                                                                                                                                   |
| `blog-page-details.wordpress-page-details`                 | Shows the details for a single blog page. This must be placed on a customized `store.blog-home#page` page to render the contents via the slug passed through the route parameter.                                                                                                                                                                                                                                                                                                                                               |
| `blog-latest-posts-preview.wordpress-latest-posts-preview` | Shows teasers for the most recent 3-5 posts (default is 3).                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `blog-category-preview.wordpress-category-preview`         | Shows teasers for the most recent 3-5 posts from a specific category (default is 3). The category ID must be provided as a prop.                                                                                                                                                                                                                                                                                                                                                                                                |
| `blog-search.wordpress-search`                             | Search box that shoppers can use to search blog articles. When submitted, the shopper is redirected to the `store.blog-search-list` page.                                                                                                                                                                                                                                                                                                                                                                                       |
| `blog-search-list.wordpress-search-list`                   | Paginated list of blog post search results. This must be placed on the `store.blog-search` page, as the search terms are provided by the parameter in the page route.                                                                                                                                                                                                                                                                                                                                                           |
| `search-blog-articles-preview.wordpress`                   | Shows teasers for the most recent 3-5 posts in the store search results page with a link to the `store.blog-search-list` page. This can only be placed on the main `store.search-result` template and uses the same search query as the product search component on that page.                                                                                                                                                                                                                                                  |
| `search-blog-articles-list.wordpress`                      | An alternative to the `search-blog-articles-preview.wordpress` block, but instead this block shows a _complete_ paginated list of posts in the search results page. It automatically uses the same search query as the product search component on that page.                                                                                                                                                                                                                                                                   |
| `blog-related-products.wordpress-related-products`         | A specialized wrapper for a product shelf that can be placed on the `store.blog-post` page. It must be a child of the `blog-post-details.wordpress-post-details` block. This allows you to tag Wordpress posts with product reference codes, and the products in question will then be displayed in the shelf. The tags must be in the format `prod-[reference code]`. For example, if your product had a reference code of `VTEX01`, the tag should be `prod-VTEX01`. This block must have `product-summary.shelf` as a child. |
| `blog-post-container.wordpress`                            | A context component that provides data for an individual blog post to its child blocks. This must be placed on the `store.blog-post` page.                                                                                                                                                                                                                                                                                                                                                                                      |
| `blog-post-navigation.wordpress`                           | A component that renders "Previous Article" and "Next Article" buttons. Must be placed as a child of a `blog-post-container.wordpress` block.                                                                                                                                                                                                                                                                                                                                                                                   |
| `blog-related-posts.wordpress-related-posts`               | Similar to the above, but the reverse: this is a block intended to be placed in the theme's `store.product` page template which will show teasers for 3-5 blog posts (3 by default) that are tagged with the reference code of the product being viewed.                                                                                                                                                                                                                                                                        |
| `blog-breadcrumb.wordpress-breadcrumb`                     | A breadcrumb component intended to be placed at the top of each blog page.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `blog-search-list.wordpress-category-related-posts`        | A block that can be used to display the title and body of one or more posts on a store category or department page. Use case: SEO text for your store's departments. By default, when placed on a store category or department page, the block will attempt to display a WordPress post tagged `category-{id}`, where `{id}` is the numeric ID of your VTEX store department.                                                                                                                                                   |

#### `blog-all-posts.wordpress-all-posts` props

| Prop Name      | Type            | Description                                                                                                                                                                                                                                                                                                                                                | Default value   |
| -------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `mediaSize`    | `MediaSizeEnum` | WordPress media image size that should be used in the blog's preview blocks.                                                                                                                                                                                                                                                                               | `full`          |
| `ampLinks`     | `boolean`       | Whether the links from each blog post should point to the external blog AMP (Accelrated Mobile Page) in a new tab (`true`) or not (`false`). Only valid for AMPs generated using the [WordPress AMP plugin](https://wordpress.org/plugins/amp/).                                                                                                           | `false`         |
| `ampUrlFormat` | `string`        | URL structure for AMP links. `ampPathSuffix` appends `/amp` to the end of the external blog post URL. `ampQuery` appends `?amp` and `ampQueryValue` appends `?amp=1`. <br></br> For example, possible URLs are https://www.wordpressblog.com/blog-post/amp, https://www.wordpressblog.com/blog-post?amp, or https://www.wordpressblog.com/blog-post?amp=1. | `ampPathSuffix` |

#### `blog-category-list.wordpress-category-list` props

| Prop Name      | Type            | Description                                                                                                                                                                                                                                                                                                                                                | Default value   |
| -------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `mediaSize`    | `MediaSizeEnum` | WordPress media image size that should be used in the blog's preview blocks.                                                                                                                                                                                                                                                                               | `full`          |
| `ampLinks`     | `boolean`       | Whether the links from each blog post should point to the external blog AMP (Accelrated Mobile Page) in a new tab (`true`) or not (`false`). Only valid for AMPs generated using the [WordPress AMP plugin](https://wordpress.org/plugins/amp/).                                                                                                           | `false`         |
| `ampUrlFormat` | `string`        | URL structure for AMP links. `ampPathSuffix` appends `/amp` to the end of the external blog post URL. `ampQuery` appends `?amp` and `ampQueryValue` appends `?amp=1`. <br></br> For example, possible URLs are https://www.wordpressblog.com/blog-post/amp, https://www.wordpressblog.com/blog-post?amp, or https://www.wordpressblog.com/blog-post?amp=1. | `ampPathSuffix` |

#### `blog-latest-posts-preview.wordpress-latest-posts-preview` props

| Prop Name           | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                                  | Default value   |
| ------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| `title`             | `string`        | Title to be displayed above the block.                                                                                                                                                                                                                                                                                                                                                                       | `null`          |
| `numberOfPosts`     | `number`        | The number of posts to be displayed.                                                                                                                                                                                                                                                                                                                                                                         | `3`             |
| `tags`              | `array`         | Array of tag IDs allowed. When this property is included, only posts that contain all the listed tags will be displayed.                                                                                                                                                                                                                                                                                     | `undefined`     |
| `excludeTags`       | `array`         | Array of tag IDs to be excluded. Posts containing any of the excluded tags will not be displayed.                                                                                                                                                                                                                                                                                                            | `undefined`     |
| `excludeCategories` | `array`         | Array of category IDs to be excluded. Posts containing any of the excluded categories will not be displayed.                                                                                                                                                                                                                                                                                                 | `undefined`     |
| `useTextOverlays`   | `boolean`       | Whether each blog post data (title, category, etc) should be overlaid on the post's featured image (`true`) or not (`false`). If `false`, date of publication and category are shown above the image, title and excerpts are shown below it.                                                                                                                                                                 | `false`         |
| `showCategories`    | `boolean`       | Whether the post category should be shown (`true`) or not (`false`).                                                                                                                                                                                                                                                                                                                                         | `true`          |
| `showDates`         | `boolean`       | Whether the date of publication should be shown (`true`) or not (`false`).                                                                                                                                                                                                                                                                                                                                   | `true`          |
| `showAuthors`       | `boolean`       | Whether the post author should be shown (`true`) or not (`false`).                                                                                                                                                                                                                                                                                                                                           | `false`         |
| `showExcerpts`      | `boolean`       | Whether the post excerpts should be shown (`true`) or not (`false`).                                                                                                                                                                                                                                                                                                                                         | `false`         |
| `mediaSize`         | `MediaSizeEnum` | WordPress media image size that should be used in the blog's preview blocks.                                                                                                                                                                                                                                                                                                                                 | `full`          |
| `absoluteLinks`     | `boolean`       | Whether the links from each blog post should point to the external blog in a new tab (`true`) or not (`false`).                                                                                                                                                                                                                                                                                              | `false`         |
| `ampLinks`          | `boolean`       | Whether the links from each blog post should point to the external blog AMP (Accelrated Mobile Page) in a new tab (`true`) or not (`false`). <br></br> Only valid for AMPs generated using the [WordPress AMP plugin](https://wordpress.org/plugins/amp/). If `true` but AMP is not enabled for a particular post and `absoluteLinks` is enabled, then the the external blog post link will be used instead. | `false`         |
| `ampUrlFormat`      | `string`        | URL structure for AMP links. `ampPathSuffix` appends `/amp` to the end of the external blog post URL. `ampQuery` appends `?amp` and `ampQueryValue` appends `?amp=1`. <br></br> For example, possible URLs are https://www.wordpressblog.com/blog-post/amp, https://www.wordpressblog.com/blog-post?amp, or https://www.wordpressblog.com/blog-post?amp=1.                                                   | `ampPathSuffix` |

#### `blog-category-preview.wordpress-category-preview` props

| Prop Name          | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                                  | Default value            |
| ------------------ | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------ |
| `category`         | `number`        | The numeric ID of the category in the WordPress system.                                                                                                                                                                                                                                                                                                                                                      | `0`                      |
| `title`            | `string`        | Title to be displayed above the component.                                                                                                                                                                                                                                                                                                                                                                   | `null`                   |
| `description`      | `string`        | Subheader to be displayed below the component's title.                                                                                                                                                                                                                                                                                                                                                       | `null`                   |
| `customLinkText`   | `string`        | Text to be displayed as a link to the `store.blog-category` page (according to the given category).                                                                                                                                                                                                                                                                                                          | `All [category] Posts >` |
| `customLinkTarget` | `string`        | If you would like the aforementioned link to direct the user somewhere other than the `store.blog-category` page, you may enter a different target using this prop.                                                                                                                                                                                                                                          | `undefined`              |
| `numberOfPosts`    | `number`        | Number of posts to be displayed.                                                                                                                                                                                                                                                                                                                                                                             | `3`                      |
| `useTextOverlays`  | `boolean`       | Whether each blog post data (title, category, etc) should be overlaid on the post's featured image (`true`) or not (`false`). If `false`, date of publication and category are shown above the image, title and summary are shown below it.                                                                                                                                                                  | `false`                  |
| `showDates`        | `boolean`       | Whether the date of publication should be shown (`true`) or not (`false`).                                                                                                                                                                                                                                                                                                                                   | `true`                   |
| `showAuthors`      | `boolean`       | Whether the post author should be shown (`true`) or not (`false`).                                                                                                                                                                                                                                                                                                                                           | `false`                  |
| `showExcerpts`     | `boolean`       | Whether the post excerpts should be shown (`true`) or not (`false`).                                                                                                                                                                                                                                                                                                                                         | `false`                  |
| `mediaSize`        | `MediaSizeEnum` | WordPress media image size that should be used in the blog's preview blocks.                                                                                                                                                                                                                                                                                                                                 | `full`                   |
| `absoluteLinks`    | `boolean`       | Whether the links from each blog post should point to the external blog in a new tab (`true`) or not (`false`).                                                                                                                                                                                                                                                                                              | `false`                  |
| `showPostButton`   | `boolean`       | Displays a button that allows the user to link directly to WP post (`true`) or not (`false`).                                                                                                                                                                                                                                                                                                                | `false`                  |
| `ampLinks`         | `boolean`       | Whether the links from each blog post should point to the external blog AMP (Accelrated Mobile Page) in a new tab (`true`) or not (`false`). <br></br> Only valid for AMPs generated using the [WordPress AMP plugin](https://wordpress.org/plugins/amp/). If `true` but AMP is not enabled for a particular post and `absoluteLinks` is enabled, then the the external blog post link will be used instead. | `false`                  |
| `ampUrlFormat`     | `string`        | URL structure for AMP links. `ampPathSuffix` appends `/amp` to the end of the external blog post URL. `ampQuery` appends `?amp` and `ampQueryValue` appends `?amp=1`. <br></br> For example, possible URLs are https://www.wordpressblog.com/blog-post/amp, https://www.wordpressblog.com/blog-post?amp, or https://www.wordpressblog.com/blog-post?amp=1.                                                   | `ampPathSuffix`          |

#### `blog-search.wordpress-search` props

| Prop Name     | Type     | Description                    | Default value        |
| ------------- | -------- | ------------------------------ | -------------------- |
| `placeholder` | `string` | Component's input placeholder. | `Search articles...` |

#### `blog-search-list.wordpress-search-list` props

| Prop Name      | Type            | Description                                                                                                                                                                                                                                                                                                                                                | Default value   |
| -------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `mediaSize`    | `MediaSizeEnum` | WordPress media image size that should be used in the blog's preview blocks.                                                                                                                                                                                                                                                                               | `full`          |
| `ampLinks`     | `boolean`       | Whether the links from each blog post should point to the external blog AMP (Accelrated Mobile Page) in a new tab (`true`) or not (`false`). Only valid for AMPs generated using the [WordPress AMP plugin](https://wordpress.org/plugins/amp/).                                                                                                           | `false`         |
| `ampUrlFormat` | `string`        | URL structure for AMP links. `ampPathSuffix` appends `/amp` to the end of the external blog post URL. `ampQuery` appends `?amp` and `ampQueryValue` appends `?amp=1`. <br></br> For example, possible URLs are https://www.wordpressblog.com/blog-post/amp, https://www.wordpressblog.com/blog-post?amp, or https://www.wordpressblog.com/blog-post?amp=1. | `ampPathSuffix` |

#### `search-blog-articles-preview.wordpress` props

| Prop Name         | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                                  | Default value   |
| ----------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| `numberOfPosts`   | `number`        | The number of posts to be displayed.                                                                                                                                                                                                                                                                                                                                                                         | `3`             |
| `useTextOverlays` | `boolean`       | Whether each blog post data (title, category, etc) should be overlaid on the post's featured image (`true`) or not (`false`). If `false`, date of publication and category are shown above the image, title and excerpts are shown below it.                                                                                                                                                                 | `false`         |
| `showCategories`  | `boolean`       | Whether the post category should be shown (`true`) or not (`false`).                                                                                                                                                                                                                                                                                                                                         | `true`          |
| `showDates`       | `boolean`       | Whether the date of publication should be shown (`true`) or not (`false`).                                                                                                                                                                                                                                                                                                                                   | `true`          |
| `showAuthors`     | `boolean`       | Whether the post author should be shown (`true`) or not (`false`).                                                                                                                                                                                                                                                                                                                                           | `false`         |
| `showExcerpts`    | `boolean`       | Whether the post excerpts should be shown (`true`) or not (`false`).                                                                                                                                                                                                                                                                                                                                         | `false`         |
| `mediaSize`       | `MediaSizeEnum` | WordPress media image size that should be used in the blog's preview blocks.                                                                                                                                                                                                                                                                                                                                 | `full`          |
| `absoluteLinks`   | `boolean`       | Whether the links from each blog post should point to the external blog in a new tab (`true`) or not (`false`).                                                                                                                                                                                                                                                                                              | `false`         |
| `ampLinks`        | `boolean`       | Whether the links from each blog post should point to the external blog AMP (Accelrated Mobile Page) in a new tab (`true`) or not (`false`). <br></br> Only valid for AMPs generated using the [WordPress AMP plugin](https://wordpress.org/plugins/amp/). If `true` but AMP is not enabled for a particular post and `absoluteLinks` is enabled, then the the external blog post link will be used instead. | `false`         |
| `ampUrlFormat`    | `string`        | URL structure for AMP links. `ampPathSuffix` appends `/amp` to the end of the external blog post URL. `ampQuery` appends `?amp` and `ampQueryValue` appends `?amp=1`. <br></br> For example, possible URLs are https://www.wordpressblog.com/blog-post/amp, https://www.wordpressblog.com/blog-post?amp, or https://www.wordpressblog.com/blog-post?amp=1.                                                   | `ampPathSuffix` |

#### `blog-related-posts.wordpress-related-posts` props

| Prop Name         | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                                  | Default value   |
| ----------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| `title`           | `string`        | Title to be displayed above the component.                                                                                                                                                                                                                                                                                                                                                                   | `null`          |
| `numberOfPosts`   | `number`        | The number of posts to be displayed.                                                                                                                                                                                                                                                                                                                                                                         | `3`             |
| `useTextOverlays` | `boolean`       | Whether each blog post data (title, category, etc) should be overlaid on the post's featured image (`true`) or not (`false`). If `false`, date of publication and category are shown above the image, title and excerpts are shown below it.                                                                                                                                                                 | `false`         |
| `showCategories`  | `boolean`       | Whether the post category should be shown (`true`) or not (`false`).                                                                                                                                                                                                                                                                                                                                         | `true`          |
| `showDates`       | `boolean`       | Whether the date of publication should be shown (`true`) or not (`false`).                                                                                                                                                                                                                                                                                                                                   | `true`          |
| `showAuthors`     | `boolean`       | Whether the post author should be shown (`true`) or not (`false`).                                                                                                                                                                                                                                                                                                                                           | `false`         |
| `showExcerpts`    | `boolean`       | Whether the post excerpts should be shown (`true`) or not (`false`).                                                                                                                                                                                                                                                                                                                                         | `false`         |
| `mediaSize`       | `MediaSizeEnum` | WordPress media image size that should be used in the blog's preview blocks.                                                                                                                                                                                                                                                                                                                                 | `full`          |
| `absoluteLinks`   | `boolean`       | Whether the links from each blog post should point to the external blog in a new tab (`true`) or not (`false`).                                                                                                                                                                                                                                                                                              | `false`         |
| `ampLinks`        | `boolean`       | Whether the links from each blog post should point to the external blog AMP (Accelrated Mobile Page) in a new tab (`true`) or not (`false`). <br></br> Only valid for AMPs generated using the [WordPress AMP plugin](https://wordpress.org/plugins/amp/). If `true` but AMP is not enabled for a particular post and `absoluteLinks` is enabled, then the the external blog post link will be used instead. | `false`         |
| `ampUrlFormat`    | `string`        | URL structure for AMP links. `ampPathSuffix` appends `/amp` to the end of the external blog post URL. `ampQuery` appends `?amp` and `ampQueryValue` appends `?amp=1`. <br></br> For example, possible URLs are https://www.wordpressblog.com/blog-post/amp, https://www.wordpressblog.com/blog-post?amp, or https://www.wordpressblog.com/blog-post?amp=1.                                                   | `ampPathSuffix` |

#### `blog-search-list.wordpress-category-related-posts` props

| Prop Name            | Description                                                                                                                                                                    | Type                                 | Default value  |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------ | -------------- |
| `categoryIdentifier` | You may manually specify the ID to be used in the WordPress tag. For example, if you set this prop to "test", the block will look for a WordPress post tagged "category-test". | String                               | (empty string) |
| `numberOfPosts`      | `number`                                                                                                                                                                       | The number of posts to be displayed. | `3`            |

#### `MediaSizeEnum` Possible Values

| Enum Name      | Enum Value     | Description                                                   |
| -------------- | -------------- | ------------------------------------------------------------- |
| `Thumbnail`    | `thumbnail`    | Uses the WordPress Media Settings `Thumbnail size` values.    |
| `Medium`       | `medium`       | Uses the WordPress Media Settings `Medium size` values.       |
| `Medium Large` | `medium_large` | Uses the WordPress Media Settings `Medium Large size` values. |
| `Large`        | `large`        | Uses the WordPress Media Settings `Large size` values.        |
| `Full`         | `full`         | Uses the original image size values.                          |

### Paginated List Customization

Blocks that use a paginated list accept some common props that allow customization of the paginated list behavior.

These blocks include:

- `blog-all-posts.wordpress-all-posts`
- `blog-category-list.wordpress-category-list`
- `blog-search-list.wordpress-search-list`
- `search-blog-articles-list.wordpress`

| Prop Name      | Description                                            | Type   | Default value |
| -------------- | ------------------------------------------------------ | ------ | ------------- |
| `postsPerPage` | Number of posts to be displayed in the paginated list. | Number | `10`          |

## Advanced configuration

### Multiple WordPress installations

Starting with version 1.6.0 of this app, blog content from **multiple WordPress installations** is supported.

To accomplish this, a `customdomainslug` parameter must be added to your blog routes, and your WordPress blocks must be updated with various props.

ℹ️ _This configuration is not required if you only wish to display blog content from a single WordPress domain._

#### Step 1 - Adding the `customdomainslug` parameter

It is time to create the store pages that will host the blog content. Before performing the following actions, make sure you already are logged into the desired VTEX account and working on a [Developer workspace](https://vtex.io/docs/recipes/development/creating-a-development-workspace/).

1. In the `store/routes.json` file, add the `customdomainslug` parameter to the paths for the blog's new pages. For example:

```json
"store.blog-home": {
	"path": "/blog"
},
"store.blog-category": {
	"path": "/:customdomainslug/category/:categoryslug_id"
},
"store.blog-post": {
	"path": "/:customdomainslug/post/:slug_id"
},
"store.blog-search-result": {
	"path": "/:customdomainslug/search/:term_id"
},
"store.custom#blog-page": {
	"path": "/:customdomainslug/page/:slug_id"
}
```

⚠️ **\*Note that the blog homepage should continue to use a specific path**. It can be `blog` as in the example, or a different string of your choice. All other routes should use the `:customdomainslug` dynamic parameter.\*

#### Step 2 - Updating the blocks' props

In order to support multiple WordPress installations, you will need to update the theme block's list of props.

First, add the `customDomains` prop to blocks that use the URL params to load blog data. Namely, they are:

- `blog-category-list.wordpress-category-list`
- `blog-post-details.wordpress-post-details`
- `blog-post-details.wordpress-page-details`
- `blog-search-list.wordpress-search-list`
- `blog-breadcrumb.wordpress-breadcrumb`

The value of the `customDomains` prop should be a JSON list of domain "slugs" and the domain that each slug represents. The first entry should be your "default" slug and domain.

For example, if you wanted URLs with the slug `blog` to load content from `http://www.blog.com/` and URLs with the slug `other-blog` to load content from `http://www.otherblog.com/`, you would give each block a prop like this:

```json
{
  "props": {
    "customDomains": "{ \"blog\":\"http://www.blog.com/\",\"other-blog\":\"http://www.otherblog.com/\" }"
  }
}
```

ℹ️ _Make sure to follow the format of the example value, including the brackets and escaped double quotes._

Blocks that do not use URL params should be given a different set of props, namely `customDomainSlug` and `customDomain`. These blocks are:

- `blog-all-posts.wordpress-all-posts`
- `blog-latest-posts-preview.wordpress-latest-posts-preview`
- `blog-category-preview.wordpress-category-preview`
- `blog-search.wordpress-search`
- `search-blog-articles-preview.wordpress`
- `search-blog-articles-list.wordpress`
- `blog-related-posts.wordpress-related-posts`
- `blog-search-list.wordpress-category-related-posts`

`customDomainSlug` must be provided for _all_ blocks when using multiple WordPress installations. `customDomain`, in turn, only needs to be provided for blocks that are _not_ using the default WordPress domain from the app settings.

Continuing the example from above, any block that shows content from the "default" WordPress domain should receive the `customDomainSlug` prop with a value of `blog`. Blocks that show content from the secondary WordPress domain should receive a `customDomainSlug` prop with a value of `other-blog` and a `customDomain` prop with a value of `http://www.other-blog.com/` also. For example:

```json
"store.blog-home": {
    "blocks": [
      "blog-search.wordpress-search",
      "blog-latest-posts-preview.wordpress-latest-posts-preview",
      "blog-category-preview.wordpress-category-preview#test",
      "blog-all-posts.wordpress-all-posts"
    ]
  },
  "blog-search.wordpress-search": {
    "props": {
      "customDomainSlug": "blog"
    }
  },
  "blog-latest-posts-preview.wordpress-latest-posts-preview": {
    "props": {
      "title": "Latest Posts",
      "useTextOverlays": true,
      "customDomainSlug": "blog"
    }
  },
  "blog-category-preview.wordpress-category-preview#test": {
    "props": {
      "category": 5,
      "description": "Description of category",
      "useTextOverlays": false,
      "customDomain": "http://www.otherblog.com/",
      "customDomainSlug": "other-blog"
    }
  },
  "blog-all-posts.wordpress-all-posts": {
    "props": {
      "customDomainSlug": "blog"
    }
  },
```

ℹ️ _Make sure to follow the format of the example value, including the brackets and escaped double quotes._

### Adding Subcategories to blog URLs

To have subcategories included in your blog URLs (`/blog/category/subcategory`), you will need to update your store's `routes.json`, as well as the theme's blocks that display category-related URLs.

Add an additional category route including the `:categoryslug` and `:subcategoryslug_id` parameter:

```json
"store.blog-category": {
	"path": "/blog/category/:categoryslug_id"
},
"store.blog-category#subcategory": {
	"path": "/blog/category/:categoryslug/:subcategoryslug_id"
},
```

Declare the subcategory block:

```json
"store.blog-category#subcategory": {
  "blocks": [
      "blog-category-list.wordpress-category-list"
  ]
},
```

Add the prop `subcategoryUrls` with a value of `true` to the blocks below:

- 'blog-all-posts.wordpress-all-posts'
- `blog-breadcrumb.wordpress-breadcrumb`
- 'blog-category-list.wordpress-category-list'
- 'blog-category-preview.wordpress-category-preview'
- 'blog-latest-posts-preview.wordpress-latest-posts-preview'
- `blog-post-details.wordpress-post-details`
- 'blog-related-products.wordpress-related-products'
- 'search-blog-articles-list.wordpress'
- 'search-blog-articles-preview.wordpress'

For example:

```json
"blog-all-posts.wordpress-all-posts": {
  "props": {
    "subcategoryUrls": true
  }
},
```

## WordPress Plugins Support

### Yoast SEO

The [Yoast SEO plugin](https://yoast.com/wordpress/plugins/seo/) provides meta tags and structured data for your WordPress content. If your WordPress installation has this plugin, the app will include this data on your posts or pages.

### AMP (Accelerated Mobile Pages)

The [AMP plugin](https://wordpress.org/plugins/amp/) lets you build AMP pages in your WordPress site. If your WordPress installation has this plugin, and your blog posts are AMP enabled, then the app will allow you to redirect visitors to the AMP version of your blog posts.

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles                            |
| -------------------------------------- |
| `breadcrumbContainer`                  |
| `breadcrumbHomeLink`                   |
| `breadcrumbLink`                       |
| `breadcrumbSeparator`                  |
| `breadcrumbCurrentPage`                |
| `categoryBlockContainer`               |
| `categoryBlockTitle`                   |
| `categoryBlockDescription`             |
| `categoryBlockFlex`                    |
| `categoryBlockFlexItem`                |
| `categoryBlockLink`                    |
| `categorySelectContainer`              |
| `dateSelectContainer`                  |
| `dateSelectInnerContainer`             |
| `dateRangeInputsContainer`             |
| `dateInputContainer`                   |
| `dateFilterButtonsContainer`           |
| `filtersContainer`                     |
| `latestPostsBlockContainer`            |
| `latestPostsBlockTitle`                |
| `latestPostsBlockFlex`                 |
| `latestPostsBlockFlexFirstColumnItem`  |
| `latestPostsBlockFlexSecondColumn`     |
| `latestPostsBlockFlexSecondColumnItem` |
| `latestPostsBlockFlexItem`             |
| `listTitle`                            |
| `listContainer`                        |
| `listFlex`                             |
| `listFlexItem`                         |
| `paginationComponent`                  |
| `postFlex`                             |
| `postContainer`                        |
| `postTitle`                            |
| `postMeta`                             |
| `postMetaDate`                         |
| `postMetaAuthor`                       |
| `postMetaCategory`                     |
| `postFeaturedImage`                    |
| `postFeaturedImageContainer`           |
| `postBody`                             |
| `postCategoryLink`                     |
| `postChildrenContainer`                |
| `postNavigationContainer`              |
| `postNavigationFlex`                   |
| `postNavigationFlexItem`               |
| `postNavigationLink`                   |
| `relatedPostsBlockContainer`           |
| `relatedPostsBlockTitle`               |
| `relatedPostsBlockFlex`                |
| `relatedPostsBlockFlexItem`            |
| `searchBlockContainer`                 |
| `searchListTitle`                      |
| `searchListContainer`                  |
| `searchListFlex`                       |
| `searchListFlexItem`                   |
| `searchResultBlockContainer`           |
| `searchResultBlockTitle`               |
| `searchResultBlockFlex`                |
| `searchResultBlockFlexItem`            |
| `searchResultBlockLink`                |
| `tagSelectContainer`                   |
| `teaserAuthor`                         |
| `teaserCategoryLink`                   |
| `teaserContainer`                      |
| `teaserDate`                           |
| `teaserGradientOverlay`                |
| `teaserHeader`                         |
| `teaserImageContainer`                 |
| `teaserImage`                          |
| `teaserBody`                           |
| `teaserSeparator`                      |
| `teaserTextOverlay`                    |
| `teaserTextOverlayTitle`               |
| `teaserTextOverlayMeta`                |
| `teaserTitle`                          |
| `teaserTitleLink`                      |
| `wordpressContentLink`                 |
| `wordpressRelatedProducts`             |

<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

<!-- DOCS-IGNORE:end -->