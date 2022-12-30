---
title: "Get Segment"
slug: "getsegment"
hidden: false
createdAt: "2019-12-20T00:49:56.335Z"
updatedAt: "2019-12-20T01:16:19.360Z"
---
You can add certain public fields in the querystring and the system will attempt to fulfill it. Values such as cultureInfo and utm are overwriteable, just keep in mind such changes will not be reflected in the client's session.

If you wish to change the value on the session (and thus be reflected on the segment without special querystrings), then use the PATCH request to session.