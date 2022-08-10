---
title: "Metatools ticket request"
slug: "metatools-ticket-requests"
excerpt: "metatools.ticket-requests@1.0.6"
hidden: true
createdAt: "2022-07-29T07:30:32.238Z"
updatedAt: "2022-07-29T07:30:32.238Z"
---
Metatools ticket request

### Installation && Configuration

1. Use the vtex toolbelt to install.
 ```
 ``vtex install metatools.ticket-requests@0.x``
 ```

2. Import the ``metatools.ticket-requests`` app to your theme's dependencies in the ``manifest.json``
```
"dependencies": {
    ....
    "ticket-requests" : "0.x"
}
```
3. Navigate to ``admin/apps/metatools.ticket-requests@1.0.3/setup/`` and add your ``VTEX`` ``App Key`` and ``App Token`` data.

4. Navigate to ``admin/tickets/settings`` and add your company data

| Field name | What it does |
| ---------- | ------------ |
| ``Metatools email address`` | The email address to send notifications copies to |
| ``Company name`` [^1] | Your company name |
| ``Fiscal code`` [^1] | Your company fiscal code |
| `` Reg.No.`` [^1] | Your company registration number |
| ``Address`` [^1] | Your company headoffice address |

[^1]: The Company data is only used inside the B2B withdrawal form

<br>

### Usage
<br>
1. B2B Registration requests

Add the ``registration-b2b-request`` block to your desired page
```
...
"flex-layout.row#my-request": {
  "children": [
    "registration-b2b-request"
  ]
}
...
```

2. B2B/B2C contact requests

Add the ``b2c-contact-form`` block to your desired page
```
...
"flex-layout.row#my-request ": {
  "children": [
    "b2c-contact-form"
  ]
}
...
```

2. B2B withdrawal requests

Add the ``withdrawal-b2b-request`` block to your desired page
```
...
"flex-layout.row#my-request ": {
  "children": [
    "withdrawal-b2b-request"
  ]
}
...
```
<br>

### Email templates
<br>

There are 4 message center email template you need to configure inside your admin section: ``admin-ticket-response-template-en`` [^2], ``b2b-registration-request-en`` [^2], ``b2c-contact-form-en`` [^2] and ``b2b-withdrawal-request-en`` [^2].

[^2]: The `en` ending on each template is the binding language code. It needs to be changed accordingly for each of your marketplaces bindings.

The data send to the template contains:
| Property | Value |
| -------- | ----- |
| ``id`` | The ticket id |
| ``state`` | The state of the ticket |
| ``clientId`` | The id of the client that opened the ticket (if available) |
| ``subject`` | The subject of the email |
| ``receiverEmail`` | The email of the recipient |
| ``type`` | The type of the ticket (Contact, Open Account etc...) |
| ``message`` | The response mesage from the admin interface |
| ``firstName`` | The first name of the person who opened the ticket (if available) |
| ``lastName`` | The last name of the person who opened the ticket (if available) |
| ``companyName`` | The company name of the person who opened the ticket (if available) |
| ``phone`` | The phone number of the person who opened the ticket (if available) |

<br>

### How it works
<br>

- The client sends a request from one of the 3 forms shown above. 
- The admin receives the the message and can respond and change the state of the ticket from the admin interface (``admin/tickets/requests``)
- The user receives email notification and can track the state of the tickets inside his account section.