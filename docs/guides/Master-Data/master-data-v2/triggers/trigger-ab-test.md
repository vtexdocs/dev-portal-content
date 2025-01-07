---
title: "A/B testing Master Data v2 trigger actions"
slug: "trigger-ab-test"
hidden: false
createdAt: "2022-07-28T22:16:57.620Z"
updatedAt: "2022-11-16T23:48:57.663Z"
---
The [Master Data v2 trigger](https://developers.vtex.com/vtex-rest-api/docs/setting-up-triggers-in-master-data-v2) configuration has an optional property called `weight`.

It is a field that accepts integers between zero and 100. This number is a percentage value of distribution between triggers.

This allows you to perform comparative experiments with different actions for the same Master Data trigger.
[block:callout]
{
  "type": "warning",
  "body": "This feature works only if you have at least two actions with value in the `weight` property."
}
[/block]

Example 1: A/B Test between two triggers with 50% of the load.

```json
    {
    	"properties": { ... },
    	"v-triggers": [
    		{
    			"name": "scenario-1",
    			"weight": 50,
          ...
    		},
    		{
    			"name": "scenario-2",
    			"weight": 50,
          ...
    		}
    	]
    }
```

Example 2: A/B Test between four triggers with different weights.
```json
    {
    	"properties": { ... },
    	"v-triggers": [
    		{
    			"name": "scenario-1",
    			"weight": 40,
          ...
    		},
    		{
    			"name": "scenario-2",
    			"weight": 30,
          ...
    		},
    		{
    			"name": "scenario-3",
    			"weight": 20,
          ...
    		},
    		{
    			"name": "scenario-4",
    			"weight": 10,
          ...
    		}
    	]
    }
```