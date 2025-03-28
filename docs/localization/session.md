---
title: "Session"
---

The Session module manages the state of session-related information in the customer's browser, including currency, channel, localization, and customer data. It ensures session validation and synchronization with the shopping cart, providing a consistent and up-to-date shopping experience.

## Session object structure

You can see details of the session data managed by the module below.

### Session

| **Field**    | **Type** | **Description**                                               |
| ------------ | -------- | ------------------------------------------------------------- |
| `addressType` | `string`  | Specifies the type of address associated with the session. Possible values are: `shipping` (delivery addresses), `billing` (payment addresses), or `null` if not specified. |
| `b2b` | `object` | Contains B2B information. See [B2B] for more details.  |
| `channel`    | `string`   | Indicates the sales channel associated with the session.                                   |
| `country`    | `string`   | Indicates the country associated with the session in a three-letter ISO code (example: `USA`).          |
| `currency`   | `object`   | Contains currency details for the session. See [Currency](#currency) for more information.            |
| `geoCoordinates` | `object`  | Contains geographical coordinates for the user session. See [GeoCoordinates](#geocoordinates) for details. |
| `locale`     | `string`   | Indicates the locale of the session, including language and region (example: "en-US").    |
| `person`     | `object`   | Contains information about the customer. See [Person] for details. |
| `postalCode` | `string`   | Indicates the postal code associated with the session.   |

#### `b2b`

| **Field** | **Type** | **Description**                           |
| --------- | -------- | ----------------------------------------- |
| `customerID`    | String   | Identifies the buyer organization the customer belongs to. |

#### `geoCoordinates`

| **Field** | **Type** | **Description**                           |
| --------- | -------- | ----------------------------------------- |
| `latitude`    | `number`   | Indicates the latitude coordinate of the geographical location. |
| `symbol`  | `number`   | Indicates the longitude coordinate of the geographical location.              |

#### `currency`

| **Field** | **Type** | **Description**                           |
| --------- | -------- | ----------------------------------------- |
| `code`    | String   | Indicates the currency code in three-letter ISO format (example: `USD`). |
| `symbol`  | String   | Indicates the symbol associated with the currency (example: `$`).              |

#### `person`

| **Field**    | **Type** | **Description**                                         |
| ------------ | -------- | ------------------------------------------------------- |
| `id`         | String   | Provides the customer identifier, if available in the ecommerce platform. |
| `email`      | String   | Stores the email address provided by the customer.                  |
| `givenName`  | String   | Contains the customer’s first name.                                     |
| `familyName` | String   | Contains the customer’s last name.                                   |

<CH.Scrollycoding>

## Import

The Session module exports a `createSessionStore` function and `Session` type, which you can import like this:

<CH.Code>

```ts
import { createSessionStore } from '@faststore/sdk'
import type { Session } from '@faststore/sdk'
```

</CH.Code>

---

## Usage

The following example demonstrates how to manage a session using `createSessionStore`.
The `createSessionStore` function initializes a session store with the provided default session and an optional validation function.
The `validateSession` function sends the current session data to the [FastStore API](https://developers.vtex.com/docs/guides/faststore/faststore-api-overview) for validation and returns the validated session.

<CH.Code>

```ts

import { gql } from '@faststore/graphql-utils'
import { createSessionStore } from '@faststore/sdk'
import { useMemo } from 'react'
import type { Session } from '@faststore/sdk'

import storeConfig from 'store.config'

import { cartStore } from '../cart'
import { request } from '../graphql/request'
import { createValidationStore, useStore } from '../useStore'
import type {
  ValidateSessionMutation,
  ValidateSessionMutationVariables,
} from '../../../@generated/graphql/index'

export const mutation = gql`
  mutation ValidateSession($session: IStoreSession!, $search: String!) {
    validateSession(session: $session, search: $search) {
      locale
      channel
      country
      postalCode
      currency {
        code
        symbol
      }
      person {
        id
        email
        givenName
        familyName
      }
    }
  }
`

export const validateSession = async (session: Session) => {
  const data = await request<
    ValidateSessionMutation,
    ValidateSessionMutationVariables
  >(mutation, { session, search: window.location.search })

  return data.validateSession
}

const [validationStore, onValidate] = createValidationStore(validateSession)

const defaultStore = createSessionStore(storeConfig.session, onValidate)

export const sessionStore = {
  ...defaultStore,
  set: (val: Session) => {
    defaultStore.set(val)

    // Trigger cart revalidation when session changes
    cartStore.set(cartStore.read())
  },
}

export const useSession = () => {
  const session = useStore(sessionStore)
  const isValidating = useStore(validationStore)

  return useMemo(
    () => ({
      ...session,
      isValidating,
    }),
    [isValidating, session]
  )
}
```

</CH.Code>

</CH.Scrollycoding>
