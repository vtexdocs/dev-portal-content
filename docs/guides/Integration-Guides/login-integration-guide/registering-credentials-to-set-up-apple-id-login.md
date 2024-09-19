---
title: "Registering credentials to set up Apple ID login"
slug: "registering-credentials-to-set-up-apple-id-login"
hidden: false
createdAt: "2023-09-05T17:34:17Z"
updatedAt: "2023-09-05T17:34:17Z"
---

> ⚠️ This feature is in closed beta, meaning only specific customers can access it now. If you want to implement it in the future, please contact [our support](https://support.vtex.com/hc/pt-br/).

To allow users to [sign in to your store with their Apple ID](https://developer.apple.com/sign-in-with-apple/get-started/), you must create valid Apple credentials before [setting up this type of authentication through the VTEX Admin](https://help.vtex.com/en/tutorial/configuring-sign-in-with-apple-id-beta--5qprgEmHYfPTghnYwm0KrV). This guide describes all the necessary steps to get these credentials:

- [Before you begin](#before-you-begin)
- [Instructions](#instructions)
  - [Step 1: Creating an App ID](#step-1-creating-an-app-id)
  - [Step 2: Creating a Services ID](#step-2-creating-a-services-id)
  - [Step 3: Creating a private Key ID and p8 Certificate](#step-3-creating-a-private-key-id-and-p8-certificate)
  - [Step 4: Configuring the Apple ID login in the VTEX Admin](#step-4-configuring-the-apple-id-login-in-the-vtex-admin)

After following these steps to register Apple credentials, you must complete the configuration of Apple ID login in the VTEX Admin, as explained in [Configuring Sign in with Apple ID](https://help.vtex.com/en/tutorial/configuring-sign-in-with-apple-id-beta--5qprgEmHYfPTghnYwm0KrV).

> ℹ️ Read [Apple's documentation](https://developer.apple.com/help/account/configure-app-capabilities/create-a-sign-in-with-apple-private-key) for more information about the required credentials.

## Before you begin

You must have an [Apple ID](https://support.apple.com/apple-id) and be a member of the [Apple Developer Program](https://developer.apple.com/programs/) to follow the instructions presented in this guide.

## Instructions

### Step 1: Creating an App ID

Begin by following the instructions below to enable the Sign in with Apple service on an iOS, tvOS, watchOS, or macOS App ID and classifying it as the primary App ID. Read [Apple’s documentation](https://developer.apple.com/help/account/configure-app-capabilities/about-sign-in-with-apple) on this step for more information.

1. Sign in to the [Apple Developer Portal](https://idmsa.apple.com/IDMSWebAuth/signin?appIdKey=891bd3417a7776362562d2197f89480a8547b108fd934911bcbea0110d07f757&path=%2Faccount%2F&rv=1).
2. Click **Certificates, Identifiers & Profiles**, as shown below.

   ![apple-credentials-1](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/apple-credentials-1-6-11.png)

3. From the sidebar, click **Identifiers**, then click the blue add `+` icon.

   ![apple-credentials-2](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/apple-credentials-2-7.png)

4. Choose **App IDs** and click `Continue`:

   ![apple-credentials-3](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/apple-credentials-3.png)

5. Complete the fields to register the App ID:

   - **Platform**: Select the app platform. You can choose between **iOS, tvOS, watchOS,** or **macOS**.
   - **Description**: Write an internal description for the app. Don’t use special characters such as `@`, `&`, `*`, `'`, `"`.
   - **App ID Prefix:** Non-editable field corresponding to your Apple Developer Team ID, which acts as a prefix to your App ID. Copy this Team ID and save it somewhere, as you will use it to configure the Apple ID login in the VTEX Admin later on. You can also find this Team ID on the [Apple Developer Portal](https://developer.apple.com/) top bar anytime you are logged in.
   - **Bundle ID**: Choose between creating an **Explicit** App ID, used for a single app, or a **Wildcard**, used for a set of apps. Check [Apple’s documentation about App IDs](https://developer.apple.com/help/glossary/app-id/) for more details.

      Then, define the Bundle ID, which works as your app’s unique identifier. It needs to be a uniform type identifier (UTI) string containing only alphanumeric characters (`A-Z`, `a-z`, `0-9`), hyphens (`-`), and/or periods (`.`). The string should be in reverse-DNS format, such as `com.domainname.appname`. Bundle IDs are case-sensitive.

   ![apple-credentials-4](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/apple-credentials-4.png)

6. Scroll down through the list of capabilities and check the box next to **Sign In with Apple**.

   ![apple-credentials-5](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/apple-credentials-5.png)

7. Click `Continue`, review the completed information, then click `Register`.

The App ID created is the combination of the **App ID Prefix** (Team ID) and the **Bundle ID**. For example, `5PD8XQY9EW.com.mystore`.

### Step 2: Creating a Services ID

Next, to enable Sign in with Apple for each website, you must register a Services ID, verify your domain, and associate it to an app. The Services ID identifies the particular instance of your app and serves as the [OAuth client_id](https://www.oauth.com/oauth2-servers/client-registration/client-id-secret/).

1. In the Apple Developer Portal, click **Certificates, Identifiers & Profiles**, as shown below.

   ![apple-credentials-6](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/apple-credentials-1-6-11.png)

2. From the sidebar, click **Identifiers**, then click the blue add `+` icon.

   ![apple-credentials-7](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/apple-credentials-2-7.png)

3. Choose **Services IDs**, as shown below, and click `Continue`.

   ![apple-credentials-8](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/apple-credentials-8.png)

4. Complete the fields to register the Services ID:

   - **Description:** Write the name of the app the user will see during the login flow. Don’t use special characters such as `@`, `&`, `*`, `'`, `"`.
   - **Identifier:** Write the identifier which will be used as the OAuth `client_id`. The string should be in reverse-DNS format, such as `com.domainname.appname.client`. Don’t include asterisks (`*`).

   ![apple-credentials-9](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/apple-credentials-9.png)

5. Check the **Sign In with Apple** checkbox.
6. Click `Configure` next to **Sign In with Apple**.
7. Define the domain your app is running on and the redirect URLs used during the OAuth flow:

   - **Primary App ID:** Make sure your associated App ID is chosen in this field. If this is the first App ID you’ve created that uses Sign In with Apple, it will probably already be selected.
   - **Web Domain:** Enter the domain name where your app will run.
   - **Return URLs:** Enter the redirect URL for your app.

   > ⚠️ You have to use a real domain here, as Apple doesn't allow localhost URLs in this step. Entering an IP address will result in failure later in the process.

   ![apple-credentials-10](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/apple-credentials-10.png)

8. Click `Save`, then `Continue` and `Register` to complete this step.

Now, you have an App ID, and you have created a Services ID which serves as your OAuth `client_id`. The **Identifier** you entered for your Services ID is your OAuth `client_id`. In the given example, this Identifier is `com.mystore.client`.

### Step 3: Creating a private Key ID and p8 Certificate

In this step, you must create and download a private key with Sign in with Apple enabled and associate it with a primary App ID. Then, you need to retrieve the Key ID. The Key ID will later be used by VTEX to generate an [OAuth client secret](https://www.oauth.com/oauth2-servers/client-registration/client-id-secret/) during setup in the VTEX Admin. Follow the steps below:

1. On the Apple Developer Portal, click **Certificates, Identifiers & Profiles**, as shown below.

   ![apple-credentials-11](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/apple-credentials-1-6-11.png)

2. From the sidebar, click **Keys**, then click the blue add `+` icon to register a new key.
3. Give your key a name, and check the **Sign In with Apple** checkbox.

   ![apple-credentials-12](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/apple-credentials-12.png)

4. Click the `Configure` button next to **Sign In with Apple** and select the primary App ID you created earlier, as shown below.

   ![apple-credentials-13](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/apple-credentials-13.png)

5. Click `Save`. Apple will generate a new private key for you and let you download it only once as a **p8 certificate**, which is a text file ending in `.p8`.

   > ⚠️ Make sure you save this file. You won’t be able to get it back again later, and you will need to upload this file when configuring login with Apple ID afterwards through the VTEX Admin.

   ![apple-credentials-14](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/apple-credentials-14.png)

6. Return and view the key information to find your **Key ID**. In the example below, the Key ID is `FGTOPLJDP`.

   ![apple-credentials-15](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/apple-credentials-15.png)

### Step 4: Configuring the Apple ID login in the VTEX Admin

After creating the required credentials, make sure you save them to set up the login with Apple ID through the VTEX Admin. You will need the following information:

| **Credential** | **Description** | **Where to find it** |
|---|---|---|
| **Key ID** | Private key identifier which will be used by VTEX to generate the [OAuth client secret](https://www.oauth.com/oauth2-servers/client-registration/client-id-secret/).  | Obtained in [Creating a private Key ID and p8 Certificate](#step-3-creating-a-private-key-id-and-p8-certificate). |
| **Team ID** | Identifier of your team on the [Apple Developer Portal](https://developer.apple.com/). | Obtained in step 5 of [Creating an App ID](#step-1-creating-an-app-id) or on the [Apple Developer Portal](https://developer.apple.com/), in the top bar, once you are logged in. |
| **Service ID** | Services identifier, to be used as the [OAuth `client_id`](https://www.oauth.com/oauth2-servers/client-registration/client-id-secret/). | Obtained in Creating a Services ID. |
| **p8 Certificate** | Private key saved in a text file ending in `.p8`, generated only once by Apple. | Obtained in [Creating a private Key ID and p8 certificate](#step-3-creating-a-private-key-id-and-p8-certificate). |

Once you have saved the credentials, access the VTEX Admin to complete the configuration of the Apple ID login. Follow the steps described in [Configuring Sign in with Apple ID](https://help.vtex.com/en/tutorial/configuring-sign-in-with-apple-id-beta--5qprgEmHYfPTghnYwm0KrV) to continue.
