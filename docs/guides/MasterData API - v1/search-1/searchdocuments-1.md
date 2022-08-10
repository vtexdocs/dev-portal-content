---
title: "Search documents"
slug: "searchdocuments-1"
hidden: false
createdAt: "2019-12-18T22:14:53.633Z"
updatedAt: "2019-12-18T23:28:26.140Z"
---
### Headers

| Name |  |
| -------- | -------- |
| Content-Type | application/json |
| Accept | application/vnd.vtex.ds.v10+json |
| x-vtex-api-appKey | App Key |
| x-vtex-api-appToken | App Token |
| REST-Range | Defines the collection of documents to be returned. A range within the collection limited by 100 documents per query. |

**WARNING**: Never use ```x-vtex-api-appKey``` and ```x-vtex-api-appToken``` headers in javascript files that will be added to stores, in order to not expose them.


### Querystring

| Attribute | What it does |
| -------- | -------- |
| _fields | Fields that will be returned by document |
| _where | Specification of filters |
| _keyword | Search in all fields marked as searchable |
| _sort | Sort order |

### How to fill the querystring attributes

1. _fields: Use the field names separated by commas. Ex. ```_fields=email,firstName,document```.
2. _where: See the query examples below to learn how to use filters.
3. _keyword: Enter the value you want to query. Use quotes for a partial query. Ex. ```_keyword=Maria``` or ```_keyword=*Maria*```
4. _sort: Use ```ASC``` value to sort ascending or ```DESC``` value to sort descending. Ex. ```_sort=firstName ASC```.
5. If you want to fetch all fields use the ```_all``` parameter in the list of response fields. Ex: ```_fields=_all```


### Query Examples:


#### Simple filter

```
/dataentities/CL/search?email=my@email.com
```

#### Complex filter

```
/dataentities/CL/search?_where=(firstName=Jon OR lastName=Smith) OR (createdIn between 2001-01-01 AND 2016-01-01)
```

#### Filter by range

##### Date Range

```
/dataentities/CL/search?_where=createdIn between 2001-01-01 AND 2016-01-01
```

##### Range numeric fields

```
/dataentities/CL/search?_where=age between 18 AND 25
```

#### Partial filter

```
/dataentities/CL/search?firstName=*Maria*
```

#### Filter for null values

```
/dataentities/CL/search?_where=firstName is null
```

#### Filter for non-null values

```
/dataentities/CL/search?_where=firstName is not null
```

#### Filter for difference
```
/dataentities/CL/search?_where=firstName<>maria
```

#### Filter greater than or less than
```
/dataentities/CL/search?_where=number>5
/dataentities/CL/search?_where=date<2001-01-01
```