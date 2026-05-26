---
title: "ClientProfileData type"
slug: "clientprofiledata-type"
hidden: false
createdAt: "2026-05-26T00:00:00.000Z"
---

The `ClientProfileData` type represents the structure of the data returned for a client. Its signature and the types used follow this contract:

```typescript
type ClientProfileData = {
  email: string | null;
  document: string | null;
  phone: string | null;
};
```