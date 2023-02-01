---
title: "Enable the Observation field in the order screen"
slug: "enable-the-remarks-field-in-the-order-screen"
hidden: false
createdAt: "2021-08-11T19:48:00.546Z"
updatedAt: "2022-02-24T20:35:52.440Z"
---

The inStore app allows the use of an **Observation** field, where it's possible to store additional information regarding the order.

The data entered in this field is sent via API to the Order Management System. They populate the `openTextField` field, which can be retrieved later either in the Admin or through an [Orders API](https://developers.vtex.com/docs/api-reference/orders-api#overview) call.

A common example of using the **Observation** field is the case where the store wants to receive an identification number from the sales associate who made the sale, such as the **[sales associate code](https://developers.vtex.com/vtex-rest-api/docs/sales-associate-code)**. In this case, the sales associate has to enter this number in the **Observation** field whenever closing an order.

The **Observation** field is enabled by editing the `checkout-instore-custom.js` file. Check out the [How to customize inStore](https://developers.vtex.com/vtex-rest-api/docs/how-to-customize-instore) guide for further information on how to access this file.

## Edit the `checkout-instore-custom.js` file

To enable the **Observation** field, you must set the following properties inside the `window.LOCALE_MESSAGES` object in the `checkout-instore-custom.js` file. In the **UI display** column below, you can see where the information you set is rendered in the inStore UI. You can click on each image to enlarge it.
[block:parameters]
{
"data": {
"0-0": "`cartObservation`",
"1-0": "`cartObservationTitle`",
"2-0": "`observationNote`",
"h-2": "Description",
"2-2": "Description of the field that will appear to the sales associate.",
"0-2": "Title of the button that will appear in the cart to open the **Observation** field.",
"1-2": "Title of the modal that will appear when the sales associate opens the **Observation** field.",
"h-1": "Type",
"0-1": "string",
"1-1": "string",
"2-1": "string",
"h-0": "Name",
"0-3": "![cartObservation](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/enable-the-remarks-field-in-the-order-screen-0.png)",
"1-3": "![cartObservationTitle](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/enable-the-remarks-field-in-the-order-screen-1.png)",
"2-3": "![observationNote](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/enable-the-remarks-field-in-the-order-screen-2.png)",
"h-3": "UI display"
},
"cols": 4,
"rows": 3
}
[/block]

This information must be added to the code as shown in the example below.

[block:code]
{
  "codes": [
    {
      "code": "window.LOCALE_MESSAGES = {\n  locale: \"en\",\n  messages: {\n    en: {\n      cartObservation: \"Observation\",\n      cartObservationTitle: \"Observation\",\n      observationNote: \"Observation note\"\n    }\n  }\n};",
      "language": "javascript"
    }
  ]
}
[/block]

> ❗ Do not remove any of the other properties present in the `window.INSTORE_CONFIG` object, to avoid breaking other functionalities.

If it's necessary to apply some validation logic or mask to the data entered in this field, you can include in the `checkout-instore-custom.js` file a function that listens to the `note.visible` event, which is triggered when the modal is open, and then develop your logic.
[block:code]
{
  "codes": [
    {
      "code": "document.addEventListener (\n  \"note.visible\",\n  function () {\n    // add mask logic, validation, etc.\n    // example: to capture the “textarea” element of the Observation field, you can use the following code:\n    // var note = document.getElementById('note')\n  },\n  false\n);",
      "language": "javascript"
    }
  ]
}
[/block]
If you need something more advanced, like making a specific request based on the data entered, it is possible to listen to the `note.change` event, which is emitted whenever the button to save the data is pressed.
[block:code]
{
  "codes": [
    {
      "code": "document.addEventListener (\n  \"note.change\",\n  function (inputData) {\n    // add the logic that uses the data\n    // the content of the field is the value of \"inputData\"\n  },\n  false\n);",
      "language": "javascript"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "After making changes in the code, make sure you press the `Save` button."
}
[/block]
