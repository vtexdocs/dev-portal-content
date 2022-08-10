---
title: "API Documentation"
slug: "caehealthcareqa-pvt-dplcheck-cae-api-docs"
excerpt: "caehealthcareqa.pvt-dplcheck-cae@3.0.4"
hidden: true
createdAt: "2022-08-05T17:38:23.379Z"
updatedAt: "2022-08-09T21:55:38.056Z"
---
## DPL

### - **(GET) User details**

<details>
<summary> <i> This api returns the user details and its export control status</i> </summary>
<pre>

```curl
- https://{{account}}.myvtex.com/v1/user/data
```

### Response example

```json
{
  "lastName": "test",
  "firstName": "dplstatus7"
}
```

</pre>
</details>

### - **(POST) process orders**

<details>
<summary> <i> This api process all orders on the export control order queue/i> </summary>
<pre>

```curl
- https://{{account}}.myvtex.com/v1/orders/process
```

```
Headers:

'x-vtex-api-appkey': "some-app-key"
'x-vtex-api-apptoken': "SOMEAPPTOKEN"
```

### Response example

```json
{
  "onHoldOrders": [],
  "cancelAndRefundOrders": [],
  "approvedOrders": [],
  "withoutActionOrders": [
    {
      "orderID": "11718814232124-01",
      "dateStamp": "2021-10-27T12:23:59.713Z",
      "userEmail": "test@test.com",
      "investigationEmailSent": false,
      "oldEmailSent": false,
      "status": 0,
      "id": "c10e8af8-3720-11ec-82ac-026c0d7011f9"
    }
  ]
}
```

</pre>
</details>

</pre>
</details>

## Test Users

```
DPL Export Compliance Status
1	dplstatus5@guerrillamail.net	6db1fd04-e637-4566-ae7e-203aa232fc47	0
2	dplstatus6@guerrillamail.net	6b559a9c-5241-41c3-98dd-4bfc5665b638	1
3	dplstatus7@guerrillamail.net	4e7dc1d2-3f56-4e64-81cc-31245e8ff91f	2
4	dplstatus8@guerrillamail.net	8de8c682-02c5-438e-9c5f-cf742efba8f3	3
5	dplstatus9@guerrillamail.net	0bbba986-b832-4deb-b012-979f4f9fcd06	4
6	dplstatus10@guerrillamail.net	1a9b54a8-b291-49a0-8af1-982182e0bbff	5
7	dplstatus11@guerrillamail.net	f70cb02b-9047-4f5c-bc43-2dc64fd6ca2f	2
```