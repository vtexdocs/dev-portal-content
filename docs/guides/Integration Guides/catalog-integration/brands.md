---
title: "Brands"
slug: "brands"
hidden: false
createdAt: "2021-12-14T13:34:54.585Z"
updatedAt: "2022-02-03T20:09:00.695Z"
---
Brands are product attributes, just like `Description` and `Name` are also considered to be product attributes or product properties. Products must have an associated  brand.

Brand is a default facet in the search navigation bar.

To learn more see [Brand on our Help Center](https://help.vtex.com/en/tutorial/what-is-a-brand--QU07yhHoaWcEYseEucOQW)

[block:callout]
{
  "type": "warning",
  "title": "Limitation",
  "body": "Products can be associated with only one brand."
}
[/block]

[block:callout]
{
  "type": "danger",
  "title": "Watch out for these pitfalls",
  "body": "- Active Brand\n    - Don't forget to activate brands otherwise products will not be indexed and thereafter will not be displayed on the website. \n- Brands with space characters at the end\n    - Pay attention to empty spaces at the end of the brand name. VTEX understands that as a new brand causing duplication."
}
[/block]

## Data Model

<table>
  <tr>
   <td><strong>Field</strong>
   </td>
   <td><strong>Description</strong>
   </td>
   <td><strong>Required</strong>
   </td>
   <td><strong>Format</strong>
   </td>
   <td><strong>Default</strong>
   </td>
  </tr>
  <tr>
   <td>Name
   </td>
   <td>Brand's Name
   </td>
   <td>Yes
   </td>
   <td>String (150)
   </td>
   <td>-
   </td>
  </tr>
  <tr>
   <td>Text
   </td>
   <td>Brand's Meta Tag Description
   </td>
   <td>No
   </td>
   <td>Integer
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>Keywords
   </td>
   <td>Store Framework - Deprecated
<p>
Classic CMS - Alternative search terms that will lead to the specific brand. The user can find the desired brand even when misspelling it. Used especially when words are of foreign origin and have a distinct spelling that is transcribed into a generic one, or when small spelling mistakes occur.
   </td>
   <td>No
   </td>
   <td>String
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>SiteTitle
   </td>
   <td>Brand's Page Title (SEO)
   </td>
   <td>No
   </td>
   <td>String
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>Active
   </td>
   <td>Flag to activate/deactivate brand
   </td>
   <td>No
   </td>
   <td>Boolean (true/false)
   </td>
   <td>false
   </td>
  </tr>
  <tr>
   <td>MenuHome
   </td>
   <td>Store Framework - Deprecated
<p>
Classic CMS - Brand appears in the Department Menu control (&lt;vtex.cmc:departmentNavigator/>)
   </td>
   <td>No
   </td>
   <td>-
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>AdWordsRemarketingCode
   </td>
   <td>Deprecated
   </td>
   <td>No
   </td>
   <td>-
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>LomadeeCampaignCode
   </td>
   <td>Deprecated
   </td>
   <td>No
   </td>
   <td>-
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>Score
   </td>
   <td>Store Framework Deprecated
<p>
Classic CMS - Value used to set the priority on the search result page.  <a href="https://help.vtex.com/tutorial/como-funciona-o-campo-score--1BUZC0mBYEEIUgeQYAKcae">More Details</a>
   </td>
   <td>No
   </td>
   <td>Integer
   </td>
   <td>null
   </td>
  </tr>
</table>

## API integration
To create a new brand use the [Create brand API endpoint](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-brand).


Body:
```json
{
    "Name": "Adidas",
    "Text": "Welcome to adidas. Shop for adidas shoes, clothing and view new collections for adidas Originals, running, football, soccer, training and much more.",
    "Keywords": "Adidas, Originals",
    "SiteTitle": "Adidas",
    "Active": true,
    "MenuHome": false,
    "Score": null
}
```

Response:
```json
{
    "Id": 12121219,
    "Name": "Adidas",
    "Text": "Welcome to adidas. Shop for adidas shoes, clothing and view new collections for adidas Originals, running, football, soccer, training and much more.",
    "Keywords": "Adidas, Originals",
    "SiteTitle": "Adidas",
    "Active": true,
    "MenuHome": false,
    "AdWordsRemarketingCode": null,
    "LomadeeCampaignCode": null,
    "Score": null,
    "LinkId": null
}
```