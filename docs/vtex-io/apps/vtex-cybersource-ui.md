---
title: "Cybersource IO"
slug: "vtex-cybersource-ui"
excerpt: "vtex.cybersource-ui@0.2.0"
hidden: true
createdAt: "2022-08-05T19:12:31.899Z"
updatedAt: "2022-08-09T21:25:05.824Z"
---
This app uses Cybersource REST API to process Payments, Risk Management, and Taxes

## Configuration

1. [Install](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-installing-an-app) `vtex.cybersource` and `vtex.cybersource-ui` in the desired account.

2. In Cybersource EBC, generate authentication keys.
	- Payment Configuration -> Key Management -> Generate Key
	- Choose `REST - Shared Secret` and Generate Key

3. In VTEX Admin, Transactions -> Cybersource, enter key values.
	![image](https://user-images.githubusercontent.com/47258865/178300211-3d3eadf2-6f44-4db4-95dd-76fae2bfebc4.png)

4. Transactions -> Payments -> Settings
	- Select Gateway Affiliations and click the green plus
	- Select Cybersource (Ensure the url is `/admin/pci-gateway/#/affiliations/vtex-cybersource-v1/`)
	- Application Key & Application Token are not used.
	- Payment capture sets when the Payments system attempts to caoture funds.  Capture Setting of Immediate Capture will Authorize and Capture in a single call.
	- Merchant Id, Merchant Key, and Shared Secret Key settings on Gateway will override the settings on the main app settings page.
	![image](https://user-images.githubusercontent.com/47258865/178299999-a27149a6-f937-4602-96ed-d232d8795095.png)

5. Payment Conditions
	- Add New Payment using Gateway

Device Fingerprint
Add the following code to Checkout UI Custom and replace {{ORG_ID}} and {{MERCHANT_ID}} with the appropriate values.
```
function addsDeviceFingerPrint() {
  if (!window.vtex) return;
  if (window.vtex.deviceFingerprint) return;
  $.ajax({
    type: 'get',
    async: true,
    url: rootPath() + '/api/sessions?items=*'
  }).then(function(response) {
    var ORG_ID = "{{ORG_ID}}";
    var MERCHANT_ID = "{{MERCHANT_ID}}";
    console.log('session', response);
    window.vtex.deviceFingerprint = response.id;
    var sessionId = response.id || "CYBERSOURCE";
    var script = document.createElement("script");
    script.type = "text/javascript";
    script.src = `https://h.online-metrix.net/fp/tags.js?org_id=${ORG_ID}&session_id=${MERCHANT_ID}${sessionId}`;
    document.head.appendChild(script);
    var noScript = document.createElement("noscript");
    var iframe = document.createElement("iframe");
    iframe.style = "width: 100px; height: 100px; border: 0; position: absolute; top: -5000px;";
    iframe.src = `https://h.online-metrix.net/fp/tags?org_id=${ORG_ID}&session_id=${MERCHANT_ID}${sessionId}`;
    noScript.appendChild(iframe);
    document.body.appendChild(noScript);
  })
}
```

# Cyber Source UI

### Merchant Defined Fields
- In the Merchant Defined Fields Tab, users can define custom fields.
- The text input follows these rules
    1. Any values outside of **{{}}** these curly brackets will be taken at direct value
    2. Any values between the **{{}}** must be in the following format `Reference Word|Modification Word|Values`
        1. All reference words can be found in the `Show All Referencable Words` dropdown
            1. Reference words can be left blank if `Modification Word` and `Values` are present
            2. Reference word is case sensitive
        2. Modification Words are either `Pad` or `date`
        3. If using `Pad`, the `Values` must be either in the format of a `number` or `desired length:fill character`
            1. `fill character` must be a single value. For example, `9:x` will result in a desired length of 9, and filling empty spaces with x 
        4. If using `date`, the `Values` must be in the format of `dd/MM/yyyy` or any combination of it.
            1. `M` for month must be capitalized. This format can be scrambled to your liking, such as `yyyy/MM` or `yyyy` or `dd/yyyy/MM`
    3. Every new line is a new Merchant Defined Field
- Examples

| Input  | Is it Valid? | Reason |
| ------------- | ------------- | ------------- |
| {{MiniCart.Buyer.LastName}},{{MiniCart.Buyer.FirstName}}  | Valid  | Reference words are valid |
| 26940{{\|date\|yy}  | Invalid  | Missing second closing bracket |
| 26940{{\|date\|yy}}  | Valid  | Valid |
| currency{{notaword}}  | Invalid  | Invalid reference word |

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!