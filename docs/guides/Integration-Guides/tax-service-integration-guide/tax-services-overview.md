---
title: "Overview"
slug: "tax-services-overview"
hidden: false
createdAt: "2020-09-01T16:28:25.618Z"
updatedAt: "2021-02-24T13:24:53.349Z"
---
Selling products online is subject to various types of taxes that can differ based on factors such as inventory location, shipping addresses, and, of course, the nature of the product. For certain stores, particularly those operating in a B2B model, tax calculations can become intricate, necessitating the use of an external tax calculation provider.

In such scenarios, it is feasible to establish an integration that enables a store to transmit checkout information to an external tax calculation API. Subsequently, the external API should provide the necessary tax details and values applicable to the purchase.

![Tax Service diagram](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/overview-tax-service.png)

## Implementation

Access the [specification](https://developers.vtex.com/docs/guides/tax-services-specification) and [recipe](https://developers.vtex.com/docs/guides/tax-services-recipe) to learn more about Tax Service integration and how to implement it.

```html
{
  "html": "<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css\" integrity=\"sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm\" crossorigin=\"anonymous\">\n<script src=\"https://code.jquery.com/jquery-3.2.1.slim.min.js\" integrity=\"sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN\" crossorigin=\"anonymous\"></script>\n<script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js\" integrity=\"sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q\" crossorigin=\"anonymous\"></script>\n<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js\" integrity=\"sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl\" crossorigin=\"anonymous\"></script>\n\n\n<a href=\"tax-service-integration-guide\"<button type=\"button\" class=\"btn btn-outline-secondary\">Back</button></a>\n\n<style></style>"
}
```
