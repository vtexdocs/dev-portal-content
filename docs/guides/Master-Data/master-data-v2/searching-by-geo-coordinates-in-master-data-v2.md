---
title: "Searching by geocoordinates in Master Data v2"
slug: "searching-by-geo-coordinates-in-master-data-v2"
hidden: false
createdAt: "2022-08-03T15:05:51.107Z"
updatedAt: "2022-08-03T17:45:21.243Z"
---
To enable search by geocoordinates in Master Data v2, your JSON schema must contain an object with the properties `latitude` and `longitude`:
```json
{
"properties": {
    	"{{yourFieldName}}": {
    		"type": "object",
		"properties": {
    			"latitude": { "type": "number" },
			"longitude": { "type": "number" }
		},
		"additionalProperties": false
	}
    }
}
```    
    
Also, it must be configured as indexed:
```json
{
 "v-indexed": [ "{{yourFieldName}}" ]
}
```
    
## Saving documents

To save a document that can later be searched by geocoordinates, it must contain the object value configured as geocoordinates:

```json
{
  "{{yourFieldName}}": {
    "latitude": {{value}},
    "longitude": {{value}}
  }
}
```
   
## Filtering

To filter documents that contain a location nearby a given geocoordinate (measured in km), add a filter as a query parameter in this format:
``` 
{{yourFieldName}}={{latitudeValue}},{{longitudeValue}},{{integer}}km
 ```

See an example:
```
address.location=-23.01227,-43.46163,25km
```
 
## Ordering search results by distance
 
To order documents by distance from a given geocoordinate, use the `_sort` query parameter with this format:
``` 
 _sort={{yourFieldName}} {{asc/desc}} {{latitudeValue}},{{longitudeValue}} km
 ```

See an example
```
 _sort=address.location asc -23.01227,-43.46163 km
```
  
When Master Data order results by distance from a geocoordinate field a new field is available: `_sort`. This field could be added in `_fields` parameter to retrieve the distance between the geocoordinate in the sort query.


## Real complete example

JSON Schema:
```json
    {
		"properties": {
			"name": {
				"type": "string"
			},
			"isActive": {
				"type": "boolean"
			},
			"address": {
				"type": "object",
				"properties": {
					"state": {
						"type": "string"
					},
					"location": {
						"type": [
							"null",
							"object"
						],
						"properties": {
							"latitude": {
								"type": "number"
							},
							"longitude": {
								"type": "number"
							}
						},
						"additionalProperties": false
					}
				}
			}
		},
		"v-indexed": [
			"name",
			"isActive",
			"address"
		],
		"v-default-fields": [
			"id",
			"name",
			"address",
			"_sort"
		]
	}
```

Query:
```
    /search?address.location=-23.01227,-43.46163,100km&_schema=v1&_sort=address.location asc -23.01227,-43.46163 km&_fields=id,_sort
```
    
Result:
```
    [
    	{
    		"id": "AME",
    		"_sort": [
    			0
    		]
    	},
    	{
    		"id": "BAR",
    		"_sort": [
    			10.71936198115181
    		]
    	},
    	{
    		"id": "BAN",
    		"_sort": [
    			14.87184710662879
    		]
    	},
    	{
    		"id": "BRX",
    		"_sort": [
    			27.607623540300178
    		]
    	}
    ]
```