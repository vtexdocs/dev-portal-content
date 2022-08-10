---
title: "My Authentication"
slug: "ui-customization-my-authentication"
hidden: false
createdAt: "2021-07-07T16:54:00.920Z"
updatedAt: "2021-07-07T17:35:14.452Z"
---
This guide shows the steps to change the appearance of the Authentication tab in My Account using CSS.
[block:callout]
{
  "type": "warning",
  "body": "This guide is for stores that do not use VTEX IO, making the customization through CMS. If your store is a VTEX IO store, check the [My Authentication Customization Guide using IO](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-my-authentication) article."
}
[/block]
To customize the appearance of My Authentication components, first you have to create your own CSS file with the desired customization settings. Below you can find the list of CSS handles and a CSS file example.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9e8300e-image6.png",
        "image6.png",
        637,
        187,
        "#262725"
      ],
      "caption": "My Authentication CSS code Portal"
    }
  ]
}
[/block]
| CSS Handles                         |
| ----------------------------------- |
| `vtex_my-authentication_box_container`                     |
| `vtex_my-authentication_box_header`                        |
| `vtex_my-authentication_box_headerSeparator`               |
| `vtex_my-authentication_box_content`                       |
| `vtex_my-authentication_box_footer`                        |
| `vtex_my-authentication_errorAlert_container`              |
| `vtex_my-authentication_warnAlert_container`               |
| `vtex_my-authentication_authenticationScreen_container`    |
| `vtex_my-authentication_authenticationScreen_passBox`      |
| `vtex_my-authentication_newPassInput_container`            |
| `vtex_my-authentication_passValidation_container`          |
| `vtex_my-authentication_passValidation_title`              |
| `vtex_my-authentication_passValidation_content`            |
| `vtex_my-authentication_passValidation_minLengthNumber`    |
| `vtex_my-authentication_passValidation_minLength`          |
| `vtex_my-authentication_passValidation_number`             |
| `vtex_my-authentication_passValidation_lowerUpper`         |
| `vtex_my-authentication_passValidation_lower`              |
| `vtex_my-authentication_passValidation_upper`              |
| `vtex_my-authentication_passValidation_iconSuccess`        |
| `vtex_my-authentication_passValidation_iconFailure`        |
| `vtex_my-authentication_savePassButton_container`          |
| `vtex_my-authentication_skeletonEditPassword_content`      |
| `vtex_my-authentication_skeletonEditPassword_button`       |
| `vtex_my-authentication_currPassInput_container`           |
| `vtex_my-authentication_createPassword_text`               |
| `vtex_my-authentication_codeInput_container`               |
| `vtex_my-authentication_resendCodeButton_container`        |
| `vtex_my-authentication_maskedPassword_title`              |
| `vtex_my-authentication_maskedPassword_content`            |
| `vtex_my-authentication_loginSessionsBox_title`            |
| `vtex_my-authentication_loginSessionsBox_content`          |
| `vtex_my-authentication_skeletonLoginSessions_content`     |
| `vtex_my-authentication_skeletonLoginSessions_button`      |
| `vtex_my-authentication_loginSessionsScreen_container`     |
| `vtex_my-authentication_loginSessions_skeleton`            |
| `vtex_my-authentication_loginSessions_error`               |
| `vtex_my-authentication_loginSessions_list`                |
| `vtex_my-authentication_loginSessions_box`                 |
| `vtex_my-authentication_skeletonLoginSessionsScreen_title` |
| `vtex_my-authentication_skeletonLoginSessionsScreen_text1` |
| `vtex_my-authentication_skeletonLoginSessionsScreen_text2` |
| `vtex_my-authentication_loginSession_currSession`          |
| `vtex_my-authentication_loginSession_currSessionIcon`      |
| `vtex_my-authentication_loginSession_currSessionText`      |
| `vtex_my-authentication_loginSession_device`               |
| `vtex_my-authentication_loginSession_lastAccess`           |
| `vtex_my-authentication_loginSession_originDetails`        |
| `vtex_my-authentication_loginSession_fullAddress`          |
| `vtex_my-authentication_loginSession_firstAccess`          |

Then go to the Admin of your store and do the following steps:

1. In the Admin left panel, go to the **STORE SETUP** section.
2. Click on **CMS**.
3. Click on **Layout**. You can also get here from the link `{accountName}.myvtex.com/admin/a/` replacing `{accountName}` for the name of your account.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9d1249e-image5.png",
        "image5.png",
        342,
        239,
        "#fcfafb"
      ],
      "caption": "Admin menu Layout"
    }
  ]
}
[/block]
4. In the **Front-end CMS** left panel, navigate to **CMS** > **Files Manager** > **.css**.
5. In the **Files Manager** tab, click on the **Add** button.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/dd4552a-image7.png",
        "image7.png",
        1417,
        786,
        "#eff1f3"
      ],
      "caption": "CMS File Manager CSS"
    }
  ]
}
[/block]
6. In the **Files Maintenance** tab, click on the `Localizar` button.
7. A window with a file explorer will open. Choose the CSS file you created.
8. Click on the `Salvar arquivo` button. This will upload your CSS file to the CMS of the store.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bbd4d04-image8.png",
        "image8.png",
        715,
        278,
        "#e6ecf1"
      ],
      "caption": "Add CSS file CMS"
    }
  ]
}
[/block]
9. In the **Front-end CMS** left panel, navigate to **CMS** > **HTML Templates** > **Account**.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/209dec7-image2.png",
        "image2.png",
        303,
        143,
        "#f3f6f9"
      ],
      "caption": "CMS HTML Template Account"
    }
  ]
}
[/block]
10. In the right panel will appear the My Account HTML template. Inside the `<head>` section, insert the tag `<link href="https://{accountName}.vteximg.com.br/arquivos/{cssFile}" rel="stylesheet"></link>`, replacing `{accountName}` for the account name of your store and `{cssFile}` for the name of the CSS file you uploaded.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/beec809-image3.png",
        "image3.png",
        952,
        145,
        "#f5f7f6"
      ],
      "caption": "My Authentication HTML code"
    }
  ]
}
[/block]
11. A popup window will show up. In the last field type **yes**.
12. Click on the `Update Item` button.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1d1158d-image4.png",
        "image4.png",
        508,
        463,
        "#edf2f6"
      ],
      "caption": "CMS Update HMTL template"
    }
  ]
}
[/block]
13. A new popup window will appear. If there are no errors, the HTML template will be saved. Then click on **Ok**.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3a354f4-image1.png",
        "image1.png",
        633,
        184,
        "#deeaf3"
      ],
      "caption": "CMS template successfully saved"
    }
  ]
}
[/block]
After updating the HTML template, you should see the changes in the Authentication tab of your store.