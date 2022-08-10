---
title: "Admin (SAML 2.0)"
slug: "login-integration-guide-admin-saml2"
hidden: false
createdAt: "2020-06-30T20:24:49.386Z"
updatedAt: "2021-12-27T13:51:40.662Z"
---
User management is a native feature of the VTEX platform. Store administrators can not only manage the users that can log in to the admin panel, but also specify the screens they can see and the operations they are allowed to perform using [roles](https://help.vtex.com/tutorial/access-profiles--7HKK5Uau2H6wxE1rH5oRbc). This granular control allows stores to adopt [best practices](https://developers.onelogin.com/saml/best-practices-and-faqs) in terms of security and compliance.

There is often the need, however, to enable or enforce the use of credentials from a central authentication system used by the organization. This guide provides the basic information you need to integrate such an authentication system to the Admin panel for a Single Sign-On (SSO) experience.
[block:callout]
{
  "type": "warning",
  "body": "If you need to use an external identity provider to login to your Admin panel, it must adhere to the SAML 2.0 protocol. We do not currently support other authentication protocols for this scope.",
  "title": "SAML 2.0 is required for Admin login integration"
}
[/block]
## SAML

Security Assertion Markup Language (SAML) is a standard for exchanging authentication and authorization data between domains. SAML 2.0 is an XML-based protocol that enables web-based cross-domain Web Browser Single Sign-On (SSO). It uses secure, digitally signed tokens and encrypted messages to pass data between trusted parties. SAML 2.0 is an open standard, a product of the OASIS Security Services Technical Committee, and is supported by major vendors in the industry. [You can learn more about SAML here](https://github.com/jch/saml).

## SAML Authentication Flow
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d1220f4-SAML.drawio.png",
        "SAML.drawio.png",
        621,
        521,
        "#f7f7f7"
      ]
    }
  ]
}
[/block]
## SAML Roles

### Identity Provider (IdP)

An **Identity Provider** is a system that creates, maintains, and manages identity information for principals (users, services, or systems) and provides principal authentication to other Service Providers (applications) within a federation or distributed network. 

An IdP is a trusted third party that can be relied upon when users and servers are establishing a dialog that must be authenticated. The IdP sends an attribute assertion containing trusted information about the user to the SP. *A user's password is never sent to a SP.*

### Service Provider (SP)

A **Service Provider** is an application server that communicates with an IdP to determine if a user has authenticated and obtain information about the user. The information obtained from the IdP may be used to make authorization decisions.
[block:callout]
{
  "type": "info",
  "title": "",
  "body": "In the context of this guide, the external authentication system is the **Identity Provider** and the VTEX platform for identifying users on our platform, VTEX ID, is the **Service Provider**."
}
[/block]
## SAML Assertions

SAML 2.0 uses assertions (packages) to pass information between the SP and the IdP. These packages contain information about a user (subject) and are written using the XML markup language. Although the standard specification defines [three types of subject-related assertion statements](http://saml.xml.org/assertions), VTEX only supports the **Authentication Assertion** type. We recommend the reading of [this document](https://github.com/jch/saml) to get a better understanding of the SAML protocol.
[block:callout]
{
  "type": "info",
  "body": "An **Authentication Assertion** states that a user was authenticated by an external service at a particular time and is often used to enable web browser SSO.",
  "title": ""
}
[/block]
## Required information

When attempting to access your admin panel, unauthenticated users will be shown a list of login options. To get your external identity provider to show up as an option in this list, you will need to provide the information described in this section when activating the integration.

### Metadata

An XML file used to describe your _Identity Provider_ in a way that allows our servers to redirect users to it and securely identify assertions made by it. It usually contains information like the SSO and Logout URLs as well as the certificate used by the IdP to sign the assertions, such as the following example:
[block:code]
{
  "codes": [
    {
      "code": "<?xml version=\"1.0\"?>\n<md:EntityDescriptor entityID=\"https://idp.example.org/SAML2\" validUntil=\"2013-03-22T23:00:00Z\" \n    xmlns:md=\"urn:oasis:names:tc:SAML:2.0:metadata\" \n    xmlns:saml=\"urn:oasis:names:tc:SAML:2.0:assertion\" \n    xmlns:ds=\"http://www.w3.org/2000/09/xmldsig#\">\n    <md:IDPSSODescriptor protocolSupportEnumeration=\"urn:oasis:names:tc:SAML:2.0:protocol\" WantAuthnRequestsSigned=\"false\">\n        <md:KeyDescriptor use=\"signing\">\n            <ds:KeyInfo xmlns:ds=\"http://www.w3.org/2000/09/xmldsig#\">\n                <ds:X509Data>\n                    <ds:X509Certificate>...</ds:X509Certificate>\n                </ds:X509Data>\n            </ds:KeyInfo>\n        </md:KeyDescriptor>\n        <md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</md:NameIDFormat>\n        <md:SingleSignOnService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect\" Location=\"https://idp.example.org/SAML2/SSO/Redirect\"/>\n        <md:SingleSignOnService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST\" Location=\"https://idp.example.org/SAML2/SSO/POST\"/>\n    </md:IDPSSODescriptor>\n    <md:Organization>\n        <md:OrganizationName xml:lang=\"en\">Some Non-profit Organization of New York</md:OrganizationName>\n        <md:OrganizationDisplayName xml:lang=\"en\">Some Non-profit Organization</md:OrganizationDisplayName>\n        <md:OrganizationURL xml:lang=\"en\">https://www.example.org/</md:OrganizationURL>\n    </md:Organization>\n    <md:ContactPerson contactType=\"technical\">\n        <md:SurName>SAML Technical Support</md:SurName>\n        <md:EmailAddress>mailto:saml-support@example.org</md:EmailAddress>\n    </md:ContactPerson>\n</md:EntityDescriptor>",
      "language": "xml"
    }
  ]
}
[/block]
The authentication system your organization is using should be capable of generating this file for you. [You can learn more about SAML 2.0 Metadata here](http://docs.oasis-open.org/security/saml/v2.0/saml-metadata-2.0-os.pdf).

### Provider Name

Name displayed to unauthenticated users in the list of login options.

### SSO Service Endpoint

URL of your SAML Identity provider - users will be redirected to this address.
[block:callout]
{
  "type": "danger",
  "body": "Note that this URL must be HTTPS."
}
[/block]
### Allowed Email Hosts

List of hosts (the portion after the `@` symbol in an email address) allowed for authentication.
[block:callout]
{
  "type": "info",
  "body": "When a SAML Authentication Assertion is received by our platform, the email provided by the user is checked against the list of **Allowed Email Hosts**. Only emails with hosts listed here are allowed.",
  "title": ""
}
[/block]
## IdP Configuration

Your Identity Provider should be configured to use the following Assertion Consumer Service (ACS) URL:

>`https://vtexid.vtex.com.br/api/vtexid/pub/saml/{{accountName}}/idps/{{accountName}}-saml/sso`

It also should send the authenticated user's email in the **Name Identifier** (`saml:NameID`) variable. The response will be cryptographically signed with the certificate described in the IdP's [Metadata](#metadata) file.
[block:callout]
{
  "type": "info",
  "body": "The account name is your business identification on VTEX system. It's the one you use inside the URL that gives access to your admin: `accountName`.myvtex.com"
}
[/block]
## Activating the integration

When you are done with the [IdP Configuration](#idp-configuration) step, you can request that a new SAML identity provider be set up in your account by sending the [Required Information](#required-information) to our team through a [support ticket](https://help-tickets.vtex.com/en/support). 

Once your provider is enabled, you should see the [Provider Name](#provider-name) listed when attempting to login to your admin panel. Clicking on the corresponding option will redirect you to the [SSO Service Endpoint](#sso-service-endpoint) you provided.