---
title:"FastStore Analyzer"
---

FastStore Analyzer provides a secure and controlled environment for implementing extension points, ensuring that custom code and third-party extensions don't affect the host application's performance, security, or integrity.

To inspect your project’s code, the Analyzer navigates through each node of your code and captures all function calls made during execution. Once the analysis is complete, it applies predefined rules to detect violations or warning based on established security and performance standards.

## Analyzer rules

The Analyzer works by applying the following rules:

| Available rules                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DOM API access restrictions       | Prevents unauthorized access to specific DOM APIs (example: `document`, `window`, `localStorage`) that could potentially lead to security vulnerabilities or interfere with the normal operation of the web application.<br><br>By restricting access to these APIs, the Analyzer ensures your code remains compliant with security best practices and minimizes risks related to direct manipulation of the Document Object Model (DOM).                            |
| [CSS containment analysis]        | Traverses through the PostCSS Abstract Syntax Tree (AST) to detect the use of problematic selectors that can compromise the styling integrity of your application, such as `:root`, `:host`, and `:host-context`.<br><br>These selectors can lead to global style leakage, impacting the look and feel of the entire application instead of being contained within a specific module or component. The Analyzer enforces proper containment practices to ensure that each module's styles don't interfere with those of others. |
| Third-party script loading detection | Prevents the loading of third-party scripts, such as `importScripts`, `eval`, and `new Function`.<br><br>By disallowing these methods of script loading, the Analyzer helps protect your application against vulnerabilities caused by executing arbitrary code or using insecure loading patterns.                                                                                                                                        |
| Core element modification detection | Prevents any modification to essential core elements of the HTML document, such as `body`, `html`, and `head`.<br><br>Ensuring these elements remain unmodified avoids unintended side effects and supports a stable and predictable environment for the application.                                                                                                                                                                                    |

## Guides in this section

<Flex>
  <WhatsNextCard
    title="Implementing FastStore Analyzer"
    description="Learn how to implement FastStore Analyzer in your store."
    linkTo="https://developers.vtex.com/docs/guides/faststore/faststore-analyzer-implementation"
    linkTitle="See more"
  />
  <WhatsNextCard
    title="CSS Analysis"
    description="Discover how FastStore Analyzer blocks unsafe CSS and auto-fixes non-compliant styles."
    linkTo="https://developers.vtex.com/docs/guides/faststore/faststore-analyzer-css-analysis"
    linkTitle="See more"
  />
</Flex>
