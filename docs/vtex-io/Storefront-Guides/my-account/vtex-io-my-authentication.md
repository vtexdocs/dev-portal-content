---
title: "Styling the My Authentication app"
slug: "vtex-io-my-authentication"
hidden: true
createdAt: "2021-07-07T17:20:23.510Z"
updatedAt: "2021-11-29T13:42:22.029Z"
---
This guide shows the steps to change the appearance of the Authentication tab in My Account using CSS.
[block:callout]
{
  "type": "warning",
  "body": "This guide is for stores that use VTEX IO, making the customization through IO apps. If your store is not a VTEX IO store, check the [My Authentication Customization Guide using CMS](https://developers.vtex.com/vtex-rest-api/docs/ui-customization-my-authentication) article."
}
[/block]
General instructions for customization of IO apps using CSS handles can be found in the article [Using CSS Handles for store customization](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization). Below are specific instructions to customize the My Authentication components in the store theme.

1. Open the code of the theme app of your store. As an example, the boilerplate code of the VTEX store-theme app can be found [here](https://github.com/vtex-apps/store-theme).
2. Navigate to the `styles\css` folder.
3. Insert or create the css file for My Authentication customization. This file should have the name `vtex.my-authentication.css`.
4. In the css file, insert the code to customize the appearance of the components. The list of CSS handles is found below.
![My Authentication CSS code IO](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-my-authentication-0.png)
5. In the root folder of the code of the app, open the `manifest.json` file.
6. Inside `"dependencies"`, insert the property `"vtex.my-authentication": "1.x"`.
![My Authentication dependency](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-my-authentication-1.png)
7. In a terminal, navigate to the root folder of the code of the app.
8. Run the command `vtex link`. After running this command, the theme app should be updated and the visual components should be as defined in the CSS file.

Below is the list of CSS handles for each UI component in My Authentication.

| CSS Handles                         |
| ----------------------------------- |
| `box_container`                     |
| `box_header`                        |
| `box_headerSeparator`               |
| `box_content`                       |
| `box_footer`                        |
| `errorAlert_container`              |
| `warnAlert_container`               |
| `authenticationScreen_container`    |
| `authenticationScreen_passBox`      |
| `newPassInput_container`            |
| `passValidation_container`          |
| `passValidation_title`              |
| `passValidation_content`            |
| `passValidation_minLengthNumber`    |
| `passValidation_minLength`          |
| `passValidation_number`             |
| `passValidation_lowerUpper`         |
| `passValidation_lower`              |
| `passValidation_upper`              |
| `passValidation_iconSuccess`        |
| `passValidation_iconFailure`        |
| `savePassButton_container`          |
| `skeletonEditPassword_content`      |
| `skeletonEditPassword_button`       |
| `currPassInput_container`           |
| `createPassword_text`               |
| `codeInput_container`               |
| `resendCodeButton_container`        |
| `maskedPassword_title`              |
| `maskedPassword_content`            |
| `loginSessionsBox_title`            |
| `loginSessionsBox_content`          |
| `skeletonLoginSessions_content`     |
| `skeletonLoginSessions_button`      |
| `loginSessionsScreen_container`     |
| `loginSessions_skeleton`            |
| `loginSessions_error`               |
| `loginSessions_list`                |
| `loginSessions_box`                 |
| `skeletonLoginSessionsScreen_title` |
| `skeletonLoginSessionsScreen_text1` |
| `skeletonLoginSessionsScreen_text2` |
| `loginSession_currSession`          |
| `loginSession_currSessionIcon`      |
| `loginSession_currSessionText`      |
| `loginSession_device`               |
| `loginSession_lastAccess`           |
| `loginSession_originDetails`        |
| `loginSession_fullAddress`          |
| `loginSession_firstAccess`          |