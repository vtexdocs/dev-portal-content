---
title: "Facets Category and  Specification"
slug: "facetscategoryandspecification"
hidden: false
createdAt: "2019-12-30T03:21:07.203Z"
updatedAt: "2020-01-02T15:35:21.517Z"
---
Facets can be obtained with a combination between categories and specifications, followed by the mapping of the content type, in that case the first is a category and the second is a specification, represented by the letter c and specificationFilter_ID ?map=c,specificationFilter_ID.
  
~~~~  
Ex.: Supose we need shoes with the color blue.  
The specification color has the id 123 inside the system.
The search will be like:   
/api/catalog_system/pub/facets/search/shoes/blue?map=c,specificationFilter_123  
The result will list the number of ocurrencies for each following filter option.  
~~~~  
~~~~  
Ex2.: Filter with categories and brands  
/api/catalog_system/pub/facets/search/higiene/shampoo/loreal?map=c,c,b  
Where the path means  higiene(categorie c), shampoo(subcategorie c) and loreal(brand b)  
So the mapping represents the type of each level as ?map=c,c,b  
~~~~