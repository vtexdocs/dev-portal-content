---
title: "API response status codes"
slug: "api-response-codes"
createdAt: "2023-01-28T23:12:53.108Z"
updatedAt: "2023-11-28T13:19:52.868Z"
hidden: false
excerpt: "Understand the outcome of your interactions with VTEX Core Commerce APIs by delving deeper into HTTP status codes."
---

Every interaction with [VTEX Core Commerce APIs](https://developers.vtex.com/docs/api-reference) returns an HTTP status code that indicates whether the request succeeded, failed, or demands particular actions for subsequent actions.

| Status code            | Description                                                                                                                                                                |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `200 OK`                 | The request was successfully processed by VTEX.                                                                                                                           |
| `201 Created`            | The request has been fulfilled, and a new resource has been created. This response is typically sent after POST requests and some PUT requests.                           |
| `202 Accepted`           | The request has been received, but the processing has not been completed yet.                                                                                             |
| `204 No Content`         | The request was processed successfully by the VTEX server, but there is no content to return.                                                                                         |
| `205 Reset Content`      | The VTEX server has accepted the request but will not return any content. The client must reset the document from which the original request was sent.                        |
| `400 Bad Request` | The VTEX server could not decode the request body, generally due to malformed syntax or an incorrect `Content-Type` header.|
| `401 Unauthorized` |  The caller was not authorized to perform the request due to missing or incorrect authentication credentials. Refer to [Authentication](https://developers.vtex.com/docs/guides/authentication) for more information. |
| `403 Forbidden` | The request is valid, but the VTEX server refuses to process the request. Ensure you have the appropriate [roles](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc?&utm_source=autocomplete) to perform the desired action.|
| `404 Not Found` | The requested resource cannot be located. Refer to [VTEX API Reference](https://developers.vtex.com/docs/api-reference) for correct endpoint naming. |
| `405 Method Not Allowed` | The HTTP method used to access the endpoint is incorrect. Refer to [VTEX API Reference](https://developers.vtex.com/docs/api-reference) for more information on the supported methods.           |
| `429 Too Many Requests`   | The application exceeded request rate limits. |
| `500 Internal Server Error` | An internal server error has occurred. Please verify the headers of the HTTP request. If the request is directed to an external server, check with the provider. For VTEX-related issues, visit the [VTEX status page](https://status.vtex.com/) for real-time outages and incident reports. If the issue persists, contact [VTEX Support](https://help.vtex.com/support) for assistance. |
| `502 Bad Gateway`          | The VTEX server acting as a gateway or proxy received an invalid response from the upstream server. Please try again later.                                                    |
| `503 Service Unavailable`  | The VTEX server is temporarily unavailable. Check the [VTEX status page](https://status.vtex.com/) for real-time outages and incident reports. Try again later, or if the issue persists, reach out to [VTEX Support](https://help.vtex.com/support). |
| `504 Gateway Timeout`      | The VTEX server acting as a gateway or proxy timed out while attempting to complete the request. Please try again later, or if the issue persists, reach out to [VTEX Support](https://help.vtex.com/support).                                                        |
