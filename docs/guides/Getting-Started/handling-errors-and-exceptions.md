---
title: "Handling errors and exceptions"
slug: "handling-errors-and-exceptions"
createdAt: "2023-01-28T23:12:53.108Z"
updatedAt: "2023-11-28T13:19:52.868Z"
hidden: false
excerpt: "Learn how to handle errors and exceptions in VTEX API Core Commerce APIs to build resilient applications."
---

Handling errors and exceptions is essential for building resilient applications that can effectively navigate temporary restrictions from VTEX Core Commerce API's rate limits. Exception handling and error recovery mechanisms help your store respond gracefully to rate limit exceeded errors without impacting user interactions. They also minimize unnecessary retries and resource wastage by introducing appropriate wait times and contributing to responsible resource management.

To implement effective error handling in rate-limiting scenarios, consider the [VTEX API response status codes](https://developers.vtex.com/docs/guides/api-response-codes) article and prioritize the best practices outlined in this article, with a specific emphasis on the code families of 3xx (Redirection), 4xx (Client Errors), and 5xx (Server Errors).

## Handle 3xx errors

HTTP status codes in the 3xx range are used for redirection purposes, usually demanding the user agent to take additional actions to fulfill the request.

| Error code              | Error handling strategies                                                                                    |
|-------------------------|------------------------------------------------------------------------------------------------------------|
| `308 Permanent Redirect`  | <ul><li>Update the URL or endpoint used in the request to the new provided location.</li><li>Ensure the redirection is valid and current at the time of the request.</li><li>Confirm if the redirection is genuinely permanent rather than temporary.</li><li>Update your bookmarks, links, or references to reflect the new resource location.</li></ul> |

## Handle 4xx errors

HTTP status codes in the 4xx range denote client errors, typically originating from issues on the client side.

| Error code             | Error handling strategies                                                                                                                                                                      |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `400 Bad Request`        | <ul><li>Refer to [API Reference](https://developers.vtex.com/docs/api-reference) for the expected request format.</li><li>Review the request parameters.</li><li>Validate the request structure and syntax.</li><li>Ensure all required parameters are included.</li></ul> |
| 401 Unauthorized       | <ul><li>Verify the authentication method used. Refer to [Authentication](https://developers.vtex.com/docs/guides/authentication) for more information.</li><li>Ensure that authentication tokens or API keys are correctly passed in the request headers.</li><li>Re-authenticate with valid credentials.</li></ul> |
| `403 Forbidden`          | <ul><li>Ensure you have the appropriate [roles](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc?&utm_source=autocomplete) to perform the desired action.</li><li>Check the expiration or validity of your access credentials.</li></ul> |
| `404 Not Found`          | <ul><li>Refer to [API Reference](https://developers.vtex.com/docs/api-reference) for correct endpoint naming.</li><li>Double-check the URL or endpoint for accuracy.</li><li>Confirm if the resource has been moved or deleted.</li><li>Check the [VTEX status page](https://status.vtex.com/) for real-time outages and incident reports. If the issue persists, reach out to [VTEX Support](https://help.vtex.com/support).</li></ul> |
| `405 Method Not Allowed` | <ul><li>Ensure the request method matches the allowed methods for the resource. Refer to [VTEX API Reference](https://developers.vtex.com/docs/api-reference) for supported methods.</li><li>Check for spelling errors in the method used.</li></ul> |
| `429 Too Many Requests` | <ul><li>Reduce the frequency of requests by optimizing code to limit unnecessary API calls or batch requests when possible.</li><li>Implement an [exponential backoff strategy](https://developers.vtex.com/docs/guides/best-practices-for-avoiding-rate-limit-errors) to gradually increase the delay between retries after receiving a 429 error.</li><li>Monitor your API request patterns closely to identify any areas that may be triggering rate limits frequently and adjust accordingly.</li><<li>Consider implementing a queue system to better manage and distribute requests over time.</li><li>In case of persistent rate limit issues, consider reaching out to [VTEX Support](https://help.vtex.com/support) for further assistance or clarification.</li></ul> |

## Handle 5xx errors

HTTP status codes in the 5xx range indicate server errors, revealing issues on the server side that hinder request fulfillment. Effective error handling in this category is essential for maintaining a reliable application.

| Error code                 | Error handling strategies                                                                                                                                                                                                                          |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `500 Internal Server Error`  | <ul><li>Check if the issue is on your end or the server's.</li><li>If possible, test the same request on different tools to confirm the issue.</li><li>Check the [VTEX status page](https://status.vtex.com/) for real-time outages and incident reports.</li><li>Retry the request after some time, as the error might be temporary.</li><li>If the issue persists, reach out to [VTEX Support](https://help.vtex.com/support).</li></ul> |
| `503 Service Unavailable`    | <ul><li>Retry the request after some time, as the error might be temporary.</li><li>Check the [VTEX status page](https://status.vtex.com/) for real-time outages and incident reports.</li><li>If the issue persists, reach out to [VTEX Support](https://help.vtex.com/support).</li></ul> |
| `504 Gateway Timeout`        | <ul><li>Check for potential network connectivity problems on your end.</li><li>Investigate if the request payload size or complexity might be causing the timeout.</li><li>Check the [VTEX status page](https://status.vtex.com/) for real-time outages and incident reports. If the issue persists, reach out to [VTEX Support](https://help.vtex.com/support).</li><li>Consider [implementing retry mechanisms or backoff strategies](https://en.wikipedia.org/wiki/Exponential_backoff) to manage timeouts effectively.</li></ul> |
