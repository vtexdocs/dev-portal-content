---
title: "Webstore (OAuth 2.0)"
slug: "login-integration-guide-webstore-oauth2"
hidden: false
createdAt: "2020-06-30T20:23:48.041Z"
updatedAt: "2022-09-23T14:35:03.422Z"
---
VTEX stores are capable of identifying returning clients by requesting that they provide login information. That way, logged-in clients can access their previous purchases and the store can present personalized content based on a client's profile data.

By default, our platform stores users' information in our secure servers, but sometimes it is useful to integrate external identity providers to the authentication process. The framework described in this guide will allow the VTEX platform to connect pre-existing user bases in private servers and is the same protocol used to allow clients to use their Google accounts to login to a 3rd party application.

In this guide you can learn about:
- [OAuth2 and VTEX](#oauth2)
- [How to setup or edit a custom OAuth user login option](#custom-oauth)

## OAuth2

The OAuth2 specification defines a framework that enables applications (__Service Providers__) to ask anyone requesting access to protected data for user authentication without having to interact with their private credentials. It achieves that by interacting with a trusted partner (**identity provider**) that handles user identification, validates their credentials, and returns to the application the data it needs to safely proceed.
You can learn more about the __OAuth2 Authorization Framework__ by reading its [specification document](https://tools.ietf.org/html/rfc6749).

See an example of VTEX's custom OAuth2 authentication flow:
[block:html]
{
  "html": "<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" version=\"1.1\" width=\"621px\" height=\"1121px\" viewBox=\"-0.5 -0.5 621 1121\" content=\"&lt;mxfile host=&quot;app.diagrams.net&quot; modified=&quot;2022-05-20T18:42:13.502Z&quot; agent=&quot;5.0 (Windows)&quot; etag=&quot;8PIBHoj6r_baYqwvr8hD&quot; version=&quot;18.0.7&quot; type=&quot;google&quot;&gt;&lt;diagram id=&quot;6OU5vCIepMFv2dG8NEjW&quot; name=&quot;Page-1&quot;&gt;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&lt;/diagram&gt;&lt;/mxfile&gt;\"><defs/><g><ellipse cx=\"10\" cy=\"5\" rx=\"5\" ry=\"5\" fill=\"rgb(255, 255, 255)\" stroke=\"rgb(0, 0, 0)\" pointer-events=\"all\"/><path d=\"M 10 10 L 10 26.67 M 10 13.33 L 0 13.33 M 10 13.33 L 20 13.33 M 10 26.67 L 0 40 M 10 26.67 L 20 40\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" pointer-events=\"all\"/><path d=\"M 10 40 L 10 1120\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" stroke-dasharray=\"3 3\" pointer-events=\"all\"/><rect x=\"240\" y=\"0\" width=\"100\" height=\"40\" fill=\"rgb(255, 255, 255)\" stroke=\"rgb(0, 0, 0)\" pointer-events=\"all\"/><path d=\"M 290 40 L 290 1120\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" stroke-dasharray=\"3 3\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe center; justify-content: unsafe center; width: 98px; height: 1px; padding-top: 20px; margin-left: 241px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: center;\" data-drawio-colors=\"color: rgb(0, 0, 0); \"><div style=\"display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;\">VTEX ID</div></div></div></foreignObject><text x=\"290\" y=\"24\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"12px\" text-anchor=\"middle\">VTEX ID</text></switch></g><rect x=\"285\" y=\"160\" width=\"10\" height=\"50\" fill=\"rgb(255, 255, 255)\" stroke=\"rgb(0, 0, 0)\" pointer-events=\"all\"/><rect x=\"285\" y=\"80\" width=\"10\" height=\"50\" fill=\"rgb(255, 255, 255)\" stroke=\"rgb(0, 0, 0)\" pointer-events=\"all\"/><rect x=\"285\" y=\"540\" width=\"10\" height=\"450\" fill=\"rgb(255, 255, 255)\" stroke=\"rgb(0, 0, 0)\" pointer-events=\"all\"/><rect x=\"285\" y=\"1040\" width=\"10\" height=\"50\" fill=\"rgb(255, 255, 255)\" stroke=\"rgb(0, 0, 0)\" pointer-events=\"all\"/><rect x=\"520\" y=\"0\" width=\"100\" height=\"40\" fill=\"rgb(255, 255, 255)\" stroke=\"rgb(0, 0, 0)\" pointer-events=\"all\"/><path d=\"M 570 40 L 570 1120\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" stroke-dasharray=\"3 3\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe center; justify-content: unsafe center; width: 98px; height: 1px; padding-top: 20px; margin-left: 521px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: center;\" data-drawio-colors=\"color: rgb(0, 0, 0); \"><div style=\"display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;\">Custom Identity Provider</div></div></div></foreignObject><text x=\"570\" y=\"24\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"12px\" text-anchor=\"middle\">Custom Identity...</text></switch></g><rect x=\"565\" y=\"300\" width=\"10\" height=\"170\" fill=\"rgb(255, 255, 255)\" stroke=\"rgb(0, 0, 0)\" pointer-events=\"all\"/><rect x=\"565\" y=\"820\" width=\"10\" height=\"90\" fill=\"rgb(255, 255, 255)\" stroke=\"rgb(0, 0, 0)\" pointer-events=\"all\"/><path d=\"M 10 80 L 276.68 80\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" pointer-events=\"stroke\"/><path d=\"M 283.68 80 L 276.68 83.5 L 276.68 76.5 Z\" fill=\"rgb(0, 0, 0)\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe flex-end; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 77px; margin-left: 147px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: center;\" data-drawio-colors=\"color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); \"><div style=\"display: inline-block; font-size: 11px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;\">Request secure content</div></div></div></foreignObject><text x=\"147\" y=\"77\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"11px\" text-anchor=\"middle\">Request secure...</text></switch></g><path d=\"M 285.2 120 L 160 120 Q 150 120 140 120 L 11.74 120\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" stroke-dasharray=\"3 3\" pointer-events=\"stroke\"/><path d=\"M 19.62 115.5 L 10.62 120 L 19.62 124.5\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe flex-end; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 117px; margin-left: 147px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: center;\" data-drawio-colors=\"color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); \"><div style=\"display: inline-block; font-size: 11px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;\">Identity Provider List</div></div></div></foreignObject><text x=\"147\" y=\"117\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"11px\" text-anchor=\"middle\">Identity Provider List</text></switch></g><path d=\"M 10 160 L 277.48 160.49\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" pointer-events=\"stroke\"/><path d=\"M 284.48 160.5 L 277.48 163.99 L 277.49 156.99 Z\" fill=\"rgb(0, 0, 0)\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe flex-end; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 157px; margin-left: 148px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: center;\" data-drawio-colors=\"color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); \"><div style=\"display: inline-block; font-size: 11px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;\">Select Custom Identity Provider</div></div></div></foreignObject><text x=\"148\" y=\"157\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"11px\" text-anchor=\"middle\">Select Custom I...</text></switch></g><path d=\"M 285.23 199.4 L 160.68 199.96 Q 150.68 200 140.68 200 L 12.24 200\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" stroke-dasharray=\"3 3\" pointer-events=\"stroke\"/><path d=\"M 20.12 195.5 L 11.12 200 L 20.12 204.5\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe flex-end; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 197px; margin-left: 147px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: center;\" data-drawio-colors=\"color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); \"><div style=\"display: inline-block; font-size: 11px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;\">Redirect to Custom Idp getAuthorizationCode endpoint</div></div></div></foreignObject><text x=\"147\" y=\"197\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"11px\" text-anchor=\"middle\">Redirect to Custom Idp getAuthorizationCode endpoint</text></switch></g><rect x=\"90\" y=\"310\" width=\"120\" height=\"65\" fill=\"rgb(255, 255, 255)\" stroke=\"rgb(0, 0, 0)\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe flex-start; justify-content: unsafe flex-start; width: 122px; height: 65px; padding-top: 310px; margin-left: 90px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: left; width: 120px; height: 65px; overflow: hidden;\" data-drawio-colors=\"color: rgb(0, 0, 0); \"><div style=\"display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; width: 100%; height: 100%; white-space: nowrap;\"><div style=\"box-sizing: border-box ; width: 100% ; background: #e4e4e4 ; padding: 2px\"><font color=\"#000000\">Query parameters</font></div><table style=\"width: 100% ; font-size: 1em\" cellspacing=\"0\" cellpadding=\"2\"><tbody style=\"line-height: 80%\"><tr><td><table style=\"font-size: 1em ; width: 120px\" cellspacing=\"0\" cellpadding=\"2\"><tbody style=\"line-height: 9.6px\"><tr><td><span style=\"font-size: 11px ; text-align: center\">redirect_uri</span><br style=\"font-size: 11px ; text-align: center\" /></td></tr><tr><td style=\"line-height: 12px\"><span style=\"font-size: 11px ; text-align: center\">state</span></td></tr></tbody></table></td></tr></tbody></table></div></div></div></foreignObject><text x=\"90\" y=\"322\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"12px\">Query parameters...</text></switch></g><path d=\"M 9.5 300.68 L 555.88 300.68\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" pointer-events=\"stroke\"/><path d=\"M 562.88 300.68 L 555.88 304.18 L 555.88 297.18 Z\" fill=\"rgb(0, 0, 0)\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe flex-end; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 298px; margin-left: 150px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: center;\" data-drawio-colors=\"color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); \"><div style=\"display: inline-block; font-size: 11px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;\"><a href=\"https://developers.vtex.com/vtex-rest-api/docs/login-integration-guide-webstore-oauth2#authorization-request\">Custom IdP's getAuthorizationCode endpoint</a></div></div></div></foreignObject><text x=\"150\" y=\"298\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"11px\" text-anchor=\"middle\">Custom IdP's ge...</text></switch></g><rect x=\"90\" y=\"210\" width=\"120\" height=\"65\" fill=\"rgb(255, 255, 255)\" stroke=\"rgb(0, 0, 0)\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe flex-start; justify-content: unsafe flex-start; width: 122px; height: 65px; padding-top: 210px; margin-left: 90px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: left; width: 120px; height: 65px; overflow: hidden;\" data-drawio-colors=\"color: rgb(0, 0, 0); \"><div style=\"display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; width: 100%; height: 100%; white-space: nowrap;\"><div style=\"box-sizing: border-box ; width: 100% ; background: #e4e4e4 ; padding: 2px\"><font color=\"#000000\">Query parameters</font></div><table style=\"width: 100% ; font-size: 1em\" cellspacing=\"0\" cellpadding=\"2\"><tbody style=\"line-height: 80%\"><tr><td><table style=\"font-size: 1em ; width: 120px\" cellspacing=\"0\" cellpadding=\"2\"><tbody style=\"line-height: 9.6px\"><tr><td><span style=\"font-size: 11px ; text-align: center\">redirect_uri</span><br style=\"font-size: 11px ; text-align: center\" /></td></tr><tr><td style=\"line-height: 12px\"><span style=\"font-size: 11px ; text-align: center\">state</span></td></tr></tbody></table></td></tr><tr><td style=\"line-height: 100%\"><table style=\"font-size: 1em ; width: 120px\" cellspacing=\"0\" cellpadding=\"2\"><tbody style=\"line-height: 9.6px\"><tr></tr></tbody></table><br /></td></tr></tbody></table></div></div></div></foreignObject><text x=\"90\" y=\"222\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"12px\">Query parameters...</text></switch></g><path d=\"M 565.33 380.07 L 540 380.02 Q 530 380 520 380 L 11.74 380\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" stroke-dasharray=\"3 3\" pointer-events=\"stroke\"/><path d=\"M 19.62 375.5 L 10.62 380 L 19.62 384.5\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe flex-end; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 377px; margin-left: 426px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: center;\" data-drawio-colors=\"color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); \"><div style=\"display: inline-block; font-size: 11px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;\">Present Login Page / Request Credentials</div></div></div></foreignObject><text x=\"426\" y=\"377\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"11px\" text-anchor=\"middle\">Present Login Page / Request Credentials</text></switch></g><path d=\"M 10 420 L 557.38 421.69\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" pointer-events=\"stroke\"/><path d=\"M 564.38 421.72 L 557.37 425.19 L 557.39 418.19 Z\" fill=\"rgb(0, 0, 0)\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe flex-end; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 417px; margin-left: 149px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: center;\" data-drawio-colors=\"color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); \"><div style=\"display: inline-block; font-size: 11px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;\">Send Valid Credentials</div></div></div></foreignObject><text x=\"149\" y=\"417\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"11px\" text-anchor=\"middle\">Send Valid Cred...</text></switch></g><path d=\"M 565 459.63 L 540.25 459.89 Q 530.25 460 520.25 460 L 11.99 460\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" stroke-dasharray=\"3 3\" pointer-events=\"stroke\"/><path d=\"M 19.87 455.5 L 10.87 460 L 19.87 464.5\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe flex-end; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 457px; margin-left: 426px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: center;\" data-drawio-colors=\"color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); \"><div style=\"display: inline-block; font-size: 11px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;\"><a href=\"javascript:void(0);\">Redirect to VTEX ID's authorizationCode endpoint</a></div></div></div></foreignObject><text x=\"426\" y=\"457\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"11px\" text-anchor=\"middle\">Redirect to VTEX ID's authorizationCode endpoint</text></switch></g><rect x=\"370\" y=\"470\" width=\"120\" height=\"65\" fill=\"rgb(255, 255, 255)\" stroke=\"rgb(0, 0, 0)\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe flex-start; justify-content: unsafe flex-start; width: 122px; height: 65px; padding-top: 470px; margin-left: 370px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: left; width: 120px; height: 65px; overflow: hidden;\" data-drawio-colors=\"color: rgb(0, 0, 0); \"><div style=\"display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; width: 100%; height: 100%; white-space: nowrap;\"><div style=\"box-sizing: border-box ; width: 100% ; background: #e4e4e4 ; padding: 2px\"><font color=\"#000000\">Query parameters</font></div><table style=\"width: 100% ; font-size: 1em\" cellspacing=\"0\" cellpadding=\"2\"><tbody><tr><td><span style=\"font-size: 11px ; text-align: center\">code<br />state</span></td></tr><tr><td><br /></td></tr></tbody></table></div></div></div></foreignObject><text x=\"370\" y=\"482\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"12px\">Query parameters...</text></switch></g><path d=\"M 12.2 540 L 276.21 540.44\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" pointer-events=\"stroke\"/><path d=\"M 283.21 540.45 L 276.21 543.94 L 276.22 536.94 Z\" fill=\"rgb(0, 0, 0)\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe flex-end; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 537px; margin-left: 148px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: center;\" data-drawio-colors=\"color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); \"><div style=\"display: inline-block; font-size: 11px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;\">VTEX ID's authorizationCode endpoint</div></div></div></foreignObject><text x=\"148\" y=\"537\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"11px\" text-anchor=\"middle\">VTEX ID's autho...</text></switch></g><rect x=\"90\" y=\"550\" width=\"120\" height=\"65\" fill=\"rgb(255, 255, 255)\" stroke=\"rgb(0, 0, 0)\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe flex-start; justify-content: unsafe flex-start; width: 122px; height: 65px; padding-top: 550px; margin-left: 90px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: left; width: 120px; height: 65px; overflow: hidden;\" data-drawio-colors=\"color: rgb(0, 0, 0); \"><div style=\"display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; width: 100%; height: 100%; white-space: nowrap;\"><div style=\"box-sizing: border-box ; width: 100% ; background: #e4e4e4 ; padding: 2px\"><font color=\"#000000\">Query parameters</font></div><table style=\"width: 100% ; font-size: 1em\" cellspacing=\"0\" cellpadding=\"2\"><tbody><tr><td><span style=\"font-size: 11px ; text-align: center\">code<br />state</span></td></tr><tr><td><br /></td></tr></tbody></table></div></div></div></foreignObject><text x=\"90\" y=\"562\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"12px\">Query parameters...</text></switch></g><path d=\"M 295 619.65 L 556.88 620.1\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" pointer-events=\"stroke\"/><path d=\"M 563.88 620.11 L 556.88 623.6 L 556.89 616.6 Z\" fill=\"rgb(0, 0, 0)\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe flex-end; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 617px; margin-left: 430px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: center;\" data-drawio-colors=\"color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); \"><div style=\"display: inline-block; font-size: 11px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;\"><a href=\"https://developers.vtex.com/vtex-rest-api/docs/login-integration-guide-webstore-oauth2#access-token-exchange\">/POST to Custom IdP's getAccessToken endpoint</a></div></div></div></foreignObject><text x=\"430\" y=\"617\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"11px\" text-anchor=\"middle\">/POST to Custom...</text></switch></g><rect x=\"370\" y=\"630\" width=\"120\" height=\"65\" fill=\"rgb(255, 255, 255)\" stroke=\"rgb(0, 0, 0)\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe flex-start; justify-content: unsafe flex-start; width: 122px; height: 65px; padding-top: 630px; margin-left: 370px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: left; width: 120px; height: 65px; overflow: hidden;\" data-drawio-colors=\"color: rgb(0, 0, 0); \"><div style=\"display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; width: 100%; height: 100%; white-space: nowrap;\"><div style=\"box-sizing: border-box ; width: 100% ; background: #e4e4e4 ; padding: 2px\"><font color=\"#000000\">Body parameters</font></div><table style=\"width: 100% ; font-size: 1em\" cellspacing=\"0\" cellpadding=\"1\"><tbody><tr><td><span style=\"font-size: 11px ; text-align: center ; line-height: 70%\">code<br />client_id<br />client_secret</span></td></tr><tr><td><br /></td></tr></tbody></table></div></div></div></foreignObject><text x=\"370\" y=\"642\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"12px\">Body parameters...</text></switch></g><path d=\"M 565 719.99 L 442.44 720 Q 432.44 720 422.44 720 L 297.24 720\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" stroke-dasharray=\"3 3\" pointer-events=\"stroke\"/><path d=\"M 305.12 715.5 L 296.12 720 L 305.12 724.5\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe flex-end; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 717px; margin-left: 430px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: center;\" data-drawio-colors=\"color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); \"><div style=\"display: inline-block; font-size: 11px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;\">Response</div></div></div></foreignObject><text x=\"430\" y=\"717\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"11px\" text-anchor=\"middle\">Response</text></switch></g><rect x=\"370\" y=\"730\" width=\"120\" height=\"65\" fill=\"rgb(255, 255, 255)\" stroke=\"rgb(0, 0, 0)\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe flex-start; justify-content: unsafe flex-start; width: 122px; height: 65px; padding-top: 730px; margin-left: 370px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: left; width: 120px; height: 65px; overflow: hidden;\" data-drawio-colors=\"color: rgb(0, 0, 0); \"><div style=\"display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; width: 100%; height: 100%; white-space: nowrap;\"><div style=\"box-sizing: border-box ; width: 100% ; background: #e4e4e4 ; padding: 2px\"><font color=\"#000000\">Body parameters</font></div><table style=\"width: 100% ; font-size: 1em\" cellspacing=\"0\" cellpadding=\"1\"><tbody><tr><td><span style=\"font-size: 11px ; text-align: center ; line-height: 70%\">access_token<br />expires_in</span></td></tr><tr><td><br /></td></tr></tbody></table></div></div></div></foreignObject><text x=\"370\" y=\"742\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"12px\">Body parameters...</text></switch></g><path d=\"M 295 820.35 L 556.88 820.45\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" pointer-events=\"stroke\"/><path d=\"M 563.88 820.45 L 556.88 823.95 L 556.88 816.95 Z\" fill=\"rgb(0, 0, 0)\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe flex-end; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 817px; margin-left: 430px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: center;\" data-drawio-colors=\"color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); \"><div style=\"display: inline-block; font-size: 11px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;\"><a href=\"https://developers.vtex.com/vtex-rest-api/docs/login-integration-guide-webstore-oauth2#user-information-exchange\">/GET to Custom IdP's getUserInfo endpoint</a></div></div></div></foreignObject><text x=\"430\" y=\"817\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"11px\" text-anchor=\"middle\">/GET to Custom...</text></switch></g><rect x=\"370\" y=\"830\" width=\"160\" height=\"40\" fill=\"rgb(255, 255, 255)\" stroke=\"rgb(0, 0, 0)\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe flex-start; justify-content: unsafe flex-start; width: 162px; height: 40px; padding-top: 830px; margin-left: 370px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: left; width: 160px; height: 40px; overflow: hidden;\" data-drawio-colors=\"color: rgb(0, 0, 0); \"><div style=\"display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; width: 100%; height: 100%; white-space: nowrap;\"><div style=\"box-sizing: border-box ; width: 100% ; background: #e4e4e4 ; padding: 2px\"><font color=\"#000000\">Header or query parameter<br /></font></div><table style=\"width: 100% ; font-size: 1em\" cellspacing=\"0\" cellpadding=\"1\"><tbody><tr><td><span style=\"font-size: 11px ; text-align: center ; line-height: 70%\">access_token<br /><br /></span></td></tr><tr><td><br /></td></tr></tbody></table></div></div></div></foreignObject><text x=\"370\" y=\"842\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"12px\">Header or query parameter...</text></switch></g><path d=\"M 565 900.01 L 442.44 900 Q 432.44 900 422.44 899.97 L 297.24 899.56\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" stroke-dasharray=\"3 3\" pointer-events=\"stroke\"/><path d=\"M 305.13 895.08 L 296.12 899.55 L 305.1 904.08\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe flex-end; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 897px; margin-left: 430px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: center;\" data-drawio-colors=\"color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); \"><div style=\"display: inline-block; font-size: 11px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;\">Response</div></div></div></foreignObject><text x=\"430\" y=\"897\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"11px\" text-anchor=\"middle\">Response</text></switch></g><rect x=\"370\" y=\"910\" width=\"120\" height=\"75\" fill=\"rgb(255, 255, 255)\" stroke=\"rgb(0, 0, 0)\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe flex-start; justify-content: unsafe flex-start; width: 122px; height: 75px; padding-top: 910px; margin-left: 370px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: left; width: 120px; height: 75px; overflow: hidden;\" data-drawio-colors=\"color: rgb(0, 0, 0); \"><div style=\"display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; width: 100%; height: 100%; white-space: nowrap;\"><div style=\"box-sizing: border-box ; width: 100% ; background: #e4e4e4 ; padding: 2px\"><font color=\"#000000\">Body parameters</font></div><table style=\"width: 100% ; font-size: 1em\" cellspacing=\"0\" cellpadding=\"1\"><tbody><tr><td><span style=\"font-size: 11px ; text-align: center ; line-height: 70%\">userId<br />email<br />name</span></td></tr></tbody></table></div></div></div></foreignObject><text x=\"370\" y=\"922\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"12px\">Body parameters...</text></switch></g><path d=\"M 285 980.1 L 162.44 980.01 Q 152.44 980 142.44 980 L 14.6 980\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" stroke-dasharray=\"3 3\" pointer-events=\"stroke\"/><path d=\"M 22.49 975.5 L 13.49 980 L 22.49 984.5\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe flex-end; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 977px; margin-left: 149px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: center;\" data-drawio-colors=\"color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); \"><div style=\"display: inline-block; font-size: 11px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;\">setCookie with VTEX ID's token</div></div></div></foreignObject><text x=\"149\" y=\"977\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"11px\" text-anchor=\"middle\">setCookie with VTEX ID's token</text></switch></g><rect x=\"55\" y=\"980\" width=\"190\" height=\"20\" fill=\"none\" stroke=\"none\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 990px; margin-left: 150px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: center;\" data-drawio-colors=\"color: rgb(0, 0, 0); \"><div style=\"display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: nowrap;\"><span style=\"font-size: 11px\">and redirect (302) to finish endpoint</span></div></div></div></foreignObject><text x=\"150\" y=\"994\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"12px\" text-anchor=\"middle\">and redirect (302) to finish en...</text></switch></g><rect x=\"565\" y=\"620\" width=\"10\" height=\"110\" fill=\"rgb(255, 255, 255)\" stroke=\"rgb(0, 0, 0)\" pointer-events=\"all\"/><path d=\"M 10 1040 L 274.01 1040.44\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" pointer-events=\"stroke\"/><path d=\"M 281.01 1040.45 L 274.01 1043.94 L 274.02 1036.94 Z\" fill=\"rgb(0, 0, 0)\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe flex-end; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 1037px; margin-left: 146px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: center;\" data-drawio-colors=\"color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); \"><div style=\"display: inline-block; font-size: 11px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;\">VTEX ID's oauth/finish endpoint</div></div></div></foreignObject><text x=\"146\" y=\"1037\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"11px\" text-anchor=\"middle\">VTEX ID's oauth...</text></switch></g><path d=\"M 282.63 1080.1 L 160.07 1080.01 Q 150.07 1080 140.07 1080 L 12.23 1080\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" stroke-dasharray=\"3 3\" pointer-events=\"stroke\"/><path d=\"M 20.12 1075.5 L 11.12 1080 L 20.12 1084.5\" fill=\"none\" stroke=\"rgb(0, 0, 0)\" stroke-miterlimit=\"10\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe flex-end; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 1077px; margin-left: 147px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: center;\" data-drawio-colors=\"color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); \"><div style=\"display: inline-block; font-size: 11px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;\">Redirect to secure content (redirect_uri)</div></div></div></foreignObject><text x=\"147\" y=\"1077\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"11px\" text-anchor=\"middle\">Redirect to secure content (redirect_uri)</text></switch></g><rect x=\"20\" y=\"5\" width=\"50\" height=\"30\" fill=\"none\" stroke=\"none\" pointer-events=\"all\"/><g transform=\"translate(-0.5 -0.5)\"><switch><foreignObject style=\"overflow: visible; text-align: left;\" pointer-events=\"none\" width=\"100%\" height=\"100%\" requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"><div xmlns=\"http://www.w3.org/1999/xhtml\" style=\"display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 20px; margin-left: 45px;\"><div style=\"box-sizing: border-box; font-size: 0px; text-align: center;\" data-drawio-colors=\"color: rgb(0, 0, 0); \"><div style=\"display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: nowrap;\"><div>User</div><div>Agent</div></div></div></div></foreignObject><text x=\"45\" y=\"24\" fill=\"rgb(0, 0, 0)\" font-family=\"Helvetica\" font-size=\"12px\" text-anchor=\"middle\">User...</text></switch></g></g><switch><g requiredFeatures=\"http://www.w3.org/TR/SVG11/feature#Extensibility\"/><a transform=\"translate(0,-5)\" xlink:href=\"https://www.diagrams.net/doc/faq/svg-export-text-problems\" target=\"_blank\"><text text-anchor=\"middle\" font-size=\"10px\" x=\"50%\" y=\"100%\">Text is not SVG - cannot display</text></a></switch></svg>"
}
[/block]
### User Agent

User Agent in this context represents the user's browser. The user interacts with its browser manually, but it's the application that sends the requests to any server, follows redirects and renders pages to the user.

### Redirects

All server communications in the context of this guide happen via the HTTPS protocol. One of the features of this protocol is responding to a request by redirecting the User Agent to a different URI. When the browser receives a redirect response, it proceeds to the specified URI instantly. For example, when a user tries to access protected areas of a store it can be redirected to a login page.

### VTEX ID

**VTEX ID** is the service used for identifying users on our platform. Usually, applications talk to it so they can obtain the token required to access protected information.

### Relevant requests

There are some steps of the OAuth2 authentication process which are worth noting and going into more detail.
[block:callout]
{
  "type": "info",
  "title": "",
  "body": "Note that some of the variable names for the requests mentioned below are customizable when implementing a Custom OAuth option. You can adapt them according to the specification of your identity provider."
}
[/block]
#### Authorization request

When an unauthenticated user requests access to protected resources in a store, VTEX ID will start the authentication process by generating a unique identifier for this authentication session, storing the URI of the requested resource for this session, and redirecting the **User Agent** to this endpoint with the following query variables:
-  `Client ID`: Identification of the client
- `state`: the state containing the unique identifier
-  `redirect_uri`: will always be `https://vtexid.vtex.com.br/VtexIdAuthSiteKnockout/ReceiveAuthorizationCode.ashx`.

At this endpoint, it is expected that the user will be presented with a way to send their credentials or redirected to an endpoint that presents it. This is usually a form requesting a username and password. It is also common practice to check for cookies that indicate that the user is already logged in.

Once the **Identity Provider** has safely identified the user, it should generate an authorization code with more than 64 characters, store it so it can be used later to identify this session, and redirect the **User Agent** to the `authorizationCode` endpoint with the code in a query variable named `code`. The `state` variable will also be forwarded as received. The **identity provider** can also pass a query string parameter `error` to inform occasional errors on its side.

#### Authorization code callback request

The **User Agent** should be redirected to this endpoint after the **Identity Provider** has successfully checked its user's credentials. Two parameters will be retrieved from the query variables by VTEX ID: `code` and `state`.
- `code`: single use code that should expire after a few minutes, as indicated by the [RFC specification](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.2). In case of multiple attempts to use this code, the credentials must be revoked.
- `state`: used to identify the authentication session, which is important to detect [replay attacks](https://en.wikipedia.org/wiki/Replay_attack). And the `code` variable will be used so VTEX ID can get the **Access Token** by using the **Access Token Exchange**endpoint.

#### Access token exchange

This is a simple endpoint that expects a `POST` request with three parameters in its body:

- `client_id`
- `client_secret`
- `code`
- `redirect_uri` (`https://vtexid.vtex.com.br/VtexIdAuthSiteKnockout/ReceiveAuthorizationCode.ashx`)

The values of `client_id` and `client_secret` are stored in VTEX ID when the **Identity Provider** is configured and should be used by this endpoint as credentials that guarantee that only VTEX ID and other well-known clients can have access.
VTEX ID expects 2 parameters in the response body:
- `access_token`: the credential that VTEX ID needs to use in the [Get user information exchange](#get-user-information).
- `expires_in`: the time, in seconds, before the token expires.

#### Get user information

This endpoint should only allow requests with valid `access_token` credentials, which can be used to identify the user, and return the following user information in the request body:
- `userId` (required)
- `email` (required)
- `name`

A user's `email` is the key used to uniquely identify each VTEX user. This is the information VTEX ID needs in order to finish the authentication process.

## Custom OAuth 

In addition to the default options to use [Google and Facebook as identity providers](https://help.vtex.com/en/tutorial/configuring-login-with-facebook-and-google--tutorials_513#) for your store, VTEX allows you to implement a custom OAuth connection, in case you have another **identity provider** that you wish to make available for your customers.

You should understand all the expected behavior for the **Identity Provider** endpoints. But it is not necessarily a good idea to implement the server from scratch. Many certified OAuth2 libraries exist and you should [take a look at them](https://oauth.net/code/) before writing your own code. Any lack of verification or mistreated steps can pose a serious security risk for your store and your customers.

### Integration

You can implement a custom OAuth option by going to your Admin panel and providing some information about the communication between VTEX and your **identity provider** as shown on the relevant requests described above.

[block:callout]
{
  "type": "warning",
  "body": "Each VTEX store may have up to one custom OAuth implementation, which will be active for all store names in that account."
}
[/block]
See the table to learn what information you must configure for each request. And below you can learn more details about each of the configuration steps.

| **Request**                                                                 | **From**                     | **To**                       | **Fields to configure**                                                                                                                                                                                                        |
|-----------------------------------------------------------------------------|------------------------------|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Authorization request](#4.-configure-authorization-code-requests)          | VTEX                         | Custom **identity provider** | <p>- **URL**</p><p>- Custom parameters (optional)</p>                                                                                                                                                                                       |
| [Authorization callback request](#4.-configure-authorization-code-requests) | Custom **identity provider** | VTEX                         | - Authorization code key                                                                                                                                                                                                       |
| [Access token exchange](#5.-configure-access-token-exchange)                | VTEX                         | Custom **identity provider** | <p>**Request:**</p><p>- **URL**</p><p>- Content-Type</p><p>- Authorization code key</p><p>- Custom parameters (optional)</p><p>**Response:**</p><p>- Access token key</p><p>- Token duration key</p>                                                                           |
| [User information exchange](#6.-configure-user-information-exchange)        | VTEX                         | Custom **identity provider** |<p>**Request:**</p><p>- **URL**</p><p>- Where to send access token (Bearer token or query string)</p><p>- Access token key (if sent on query string)</p><p>- Custom parameters (optional)</p>  <p>**Response:**</p><p>- User email key</p><p>- User ID key</p><p>- User name key</p>   |

[block:callout]
{
  "type": "warning",
  "body": "Note that many of the field values indicated in the table are dinamically generated or come from the **identity provider**. Because of this, you must define only the key under which this information will be sent to VTEX, so the platform knows how to properly handle each piece of information. Examples of this include the _authorization code key_, _token duration key_ and _user email key_."
}
[/block]
#### Configuration steps

In order to configure this process, follow the steps below:

1. Go to the **Admin panel** > **Account settings** > **Authentication**.
2. In the **Webstore** tab, click `SET UP` in the **My Custom OAuth** section

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5f26fac-1.PNG",
        "1.PNG",
        909,
        529,
        "#fafafb"
      ],
      "caption": "Authentication settings screen with options: Access Key, Password, Facebook, Google and My Custom OAuth."
    }
  ]
}
[/block]
3. [Set provider details](#3.-set-provider-details)
4. [Configure authorization code requests](#4.-configure-authorization-code-requests)
5. [Configure access token exchange request](#5.-configure-access-token-exchange)
6. [Configure get user information request](#6.-configure-user-information-exchange)

[block:callout]
{
  "type": "info",
  "body": "When performing these steps, you will be able to preview the configuration outcome in the respective **Request Preview** and **Expected Response Preview** sections. We recommend you check them thoroughly when integrating."
}
[/block]
#### 3. Set provider details

When you start the custom OAuth setup, you must fill in the following information:
- **Identity provider’s** name
- **client ID** key (`client_id`)
- **client ID** value
- **client secret** key (`client_secret`)
- **client secret** value

[block:callout]
{
  "type": "danger",
  "body": "These keys are the names under which VTEX should send or expect to receive the information value when communicating with the identity provider. They must be `client_id` and `client_secret` respectively."
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b538997-identity_feedback_oauth.PNG",
        "identity feedback oauth.PNG",
        978,
        630,
        "#000000"
      ],
      "caption": "Provider details section, in the custom OAuth set up interface with the options described in the tutorial."
    }
  ]
}
[/block]
Click `NEXT`.


#### 4. Configure authorization code requests

In this step, you must first provide the authorization request **URL**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/cd0d53e-3.PNG",
        "3.PNG",
        685,
        554,
        "#f8f9f9"
      ],
      "caption": "Authorization code section, in the custom OAuth set up interface with the options described in the tutorial."
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "If you wish, you can also add [custom parameters](#custom-parameters) to this request."
}
[/block]
Then, scroll down to the **Callback Request Information** section and fill in the **Key** under which the authorization code will be sent by the **identity provider** to VTEX.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8e76cb3-4.PNG",
        "4.PNG",
        884,
        557,
        "#f8f9f9"
      ],
      "caption": "Scrolling further down in the authorization code section, in the custom OAuth set up interface with the options described in the tutorial."
    }
  ]
}
[/block]
Click `NEXT`.

#### 5. Configure access token exchange

In order to configure the **access token** exchange request, provide:
- The request **URL**
- **Authorization code key,** under which VTEX should send the authorization code to the identity provider.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0968553-5.PNG",
        "5.PNG",
        883,
        865,
        "#f8f9f9"
      ],
      "caption": "Access token exchange section, in the custom OAuth set up interface with the options described in the tutorial."
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "If you wish, you can also add [custom parameters](#custom-parameters) to this request."
}
[/block]
Then, you may scroll down to the **Response Information** section and inform the **Keys** under which VTEX should expect to receive user information:
- **Access token key**
- **Token duration key**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/56a36a4-6.PNG",
        "6.PNG",
        876,
        511,
        "#f9fafb"
      ],
      "caption": "Scrolling further down in the Access token exchange section, in the custom OAuth set up interface with the options described in the tutorial."
    }
  ]
}
[/block]
Click `NEXT`.

#### 6. Configure user information exchange

Now you must provide information regarding the user information exchange:
- Request **URL**
- **Where to send Access Token.** It is sent as a bearer token by default. Use the toggle if you wish to change it to **Send on query string**.

Check the **Request Preview** section to make sure it matches the format expected by the **identity provider.** Also, note that if you toggle **Send on query string,** you can edit the access token key under which VTEX will send it to the **identity provider.**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9ba2436-7.PNG",
        "7.PNG",
        877,
        665,
        "#f8f8f9"
      ],
      "caption": "Get user info section, in the custom OAuth set up interface with the options described in the tutorial."
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "title": "",
  "body": "If you wish, you can also add [custom parameters](#custom-parameters) to this request."
}
[/block]
Scroll down to the **Response Information** section, and provide the **Keys** under which VTEX should expect to receive user information:
- **User e-mail key**
- **User ID key**
- **User name key**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/31ad171-8.PNG",
        "8.PNG",
        882,
        524,
        "#f9fafa"
      ],
      "caption": "Scrolling further down in the Get user info section, in the custom OAuth set up interface with the options described in the tutorial."
    }
  ]
}
[/block]
To finalize your Custom OAuth configuration, click `FINISH`.

#### Custom parameters

For each of the [relevant requests](#relevant-requests) that are sent by VTEX to the **identity provider**, you can configure custom parameters with static values. To do this, follow these steps:


1. Click `+ NEW PARAMETER`.
2. Fill in the custom parameter **Key**.
3. Inform the custom parameter **Value**.

### Edit custom OAuth

After you set your custom OAuth option up, you can edit it by following the same steps described below for [implementation](#configuration-steps).

[block:callout]
{
  "type": "danger",
  "body": "If your implementation was initially set up via [VTEX support](https://help.vtex.com/en/support) instead of the process described above, you must be extra careful when editing it via the Admin panel. Incorrect edits may cause your custom OAuth to stop working. We recommend you check the previews thoroughly and make sure they match what is expected by the **identity provider.**"
}
[/block]