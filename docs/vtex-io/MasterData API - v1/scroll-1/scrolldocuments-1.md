---
title: "Scroll documents"
slug: "scrolldocuments-1"
hidden: false
createdAt: "2019-12-18T22:14:53.633Z"
updatedAt: "2019-12-18T23:27:20.718Z"
---
Use all the features of ```search``` API to perform filters.

In the first request the ```X-VTEX-MD-TOKEN``` token will be obtained in the header. This token must be passed to the next request in the querystring ```_token``` parameter.

**ATTENTION:** To inform the quantity of documents per request use the querystring parameter ```_size```.

After the token is obtained it is no longer necessary to send the filter or document size per page parameters. You only need to resend the token until the document collection is empty.

### First request example:
```
/dataentities/CL/scroll?isCluster=true&_size=250&_fields=email,firstName
```

After the first request retrieve the token in the header ```X-VTEX-MD-TOKEN``` and make the next requests.

### Example of subsequent requests:
```
/dataentities/CL/scroll?_token=tokenvalueexample
```