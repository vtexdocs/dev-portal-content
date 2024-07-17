---
title: "Adding a contact form to a landing page"
slug: "adding-a-contact-form-to-a-landing-page"
hidden: false
createdAt: "2024-07-17T18:10:15.623Z"
updatedAt: ""
---

This guide illustrates how to handle data from a Contact Us form and send it to a third-party API. To this end, we will create a Contact Us page with a Contact form.

> ℹ️ For detailed instructions on API extensions, refer to [API extensions](https://developers.vtex.com/docs/guides/faststore/api-extensions-overview) guide.

## Context

- You want to create a Contact Us page so shoppers can contact your store.
- You want to add a form so shoppers can send their requests or feedback.
- To handle the data submissions from this contact form, you need to [extend FastStore API with third-party API schemas](https://developers.vtex.com/docs/guides/faststore/api-extensions-extending-api-schema#extending-faststore-api-with-third-party-api-schemas) to handle the form data submission.

## implementation

### Create the GraphQL files

First, you need to set up the necessary GraphQL files to handle data submissions.

1. In your store repository, go to the `src` folder, if you don’t have one already, create a new `graphql` folder.
2. Inside `graphql`, create the `thirdParty` folder.
3. In the `thirdParty` folder, create two other subfolders:

   - `resolvers`
   - `typeDefs`

4. Create an `index.ts` file inside the `resolvers` folder to set up the base structure for your resolver functions.

  > ℹ️ For further details on code implementation, see the [`thirdParty`](https://github.com/vtex-sites/playground.store/tree/main/src/graphql/thirdParty) folder available in the [playground.store](https://github.com/vtex-sites/playground.store) repository.

<CH.Scrollycoding>

### Define the types

Next, define the GraphQL types for your contact form.

1. Create a `contactForm.graphql` file in the `thirdParty` folder. This file will contain type definitions for your GraphQL schema.
2. In the `graphql/thirdParty/resolvers` folder, create a `contactForm.ts` file to handle the resolver logic for your contact form.
3. In the `graphql/thirdParty/typeDefs` folder, create a `contactForm.graphql` file and add the following schema definitions.

  <CH.Code rows={7} show={["contactForm.graphql"]}>

  ```graphql contactForm.graphql
  type ContactFormResponse {
    message: String!
  }

  input ContactFormInput {
    name: String!
    email: String!
    subject: String!
    message: String!
  }

  type Mutation {
    submitContactForm(input: ContactFormInput!): ContactFormResponse
  }
  ```

  </CH.Code>

     - `ContactFormResponse`: Defines the structure of the response from the API, with a mandatory message field.
      - `ContactFormInput`: Specifies the input fields required for the contact form.
      - `Mutation`: Declares a mutation for submitting the contact form data.

---

### Create the resolvers

Now, let's create the resolver function to process the form submission.

In the `contactForm.ts` file, add the following code. This file imports the `contactFormResolver` and combines it with other potential resolvers into a single object.

<CH.Code rows={7} show={["contactForm.ts"]}>

```ts contactForm.ts mark=10,12
type SubmitContactFormData = {
  input: {
    name: string;
    email: string;
    subject?: string;
    message: string;
  };
};

const contactFormResolver = {
  Mutation: {
    submitContactForm: async (_: never, data: SubmitContactFormData) => {
      const { input } = data;

      try {
        const response = await fetch(
          "https://playground.vtexcommercestable.com.br/api/dataentities/ContactForm/documents?_schema=contactForm",
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(input),
          }
        );

        if (!response.ok) {
          throw new Error("Error while sending the message");
        }

        return { message: "Your message was sent successfully!" };
      } catch (error) {
        return { message: error };
      }
    },
  },
};

export default contactFormResolver;
```

</CH.Code>

---

#### Consolidating the resolvers

In the `graphql/thirdParty/resolvers` folder, create an `index.ts` file to consolidate the resolvers:

<CH.Code rows={7} show={["index.ts"]}>

```ts index.ts
import contactFormResolver from "./contactForm";

const resolvers = {
  ...contactFormResolver,
};

export default resolvers;
```

</CH.Code>

---

### Creating the new section

Create a new section to receive the Contact Form data.

1. In the `src/components` folder, create the `ContactForm` folder.

2. In `ContactForm` folder, create the following files:

   - `ContactForm.tsx`: The main component file.
   - `contant-form.module.scss`: The stylesheet for the component.

3. Add the following code to the `ContactForm.tsx`.

  <CH.Code rows={7} show={["ContactForm.tsx"]}>

  ```tsx ContactForm.tsx
  import { useCallback, useState } from "react";
  import { gql } from "@faststore/core/api";
  import { useLazyQuery_unstable as useLazyQuery } from "@faststore/core/experimental";

  import {
    InputField as UIInputField,
    Button as UIButton,
    TextArea as UITextArea,
  } from "@faststore/ui";

  import styles from "./contact-form.module.scss";

  export const mutation = gql(`
        mutation SubmitContactForm($data: ContactFormInput!) {
          submitContactForm(input: $data) {
            message
          }
        }
      `);

  export const ContactForm = () => {
    const [submitContactForm, { data, error }] = useLazyQuery(mutation, {
      data: { name: "", email: "", subject: "", message: "" },
    });

    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [subject, setSubject] = useState("");
    const [message, setMessage] = useState("");

    const onSubmit = useCallback(
      (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();

        const formValues = {
          name,
          email,
          subject,
          message,
        };

        submitContactForm({ data: formValues });

        if (error) {
          console.error(error);
        }

        if (data) {
          setName("");
          setEmail("");
          setSubject("");
          setMessage("");
        }
      },
      [submitContactForm]
    );

    return (
      <section className={styles.contactForm}>
        <div>
          <h2>Contact Us</h2>
          <p>
            Need to get in touch with us? Please fill out the form, we'll get in
            touch with you soon.
          </p>
        </div>
        <form onSubmit={onSubmit}>
          <UIInputField
            id="name"
            label="Name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
          <UIInputField
            id="email"
            label="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <UIInputField
            id="subject"
            label="Subject"
            value={subject}
            onChange={(e) => setSubject(e.target.value)}
          />
          <UITextArea
            id="message"
            placeholder="Write here your message."
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />
          <UIButton type="submit" variant="primary">
            Send
          </UIButton>
        </form>
      </section>
    );
  };

  export default ContactForm;
  ```

  </CH.Code>

     - This component renders a contact form with name, email, subject, and message fields.
      - The `onSubmit` function handles form submission, sends the data to the server, and clears the form fields upon success.

---

### Creating the stylesheet for the section

In the `contact-form.module.scss` file, add the following code. The stylesheet applies specific styles to the Contact Form component, including layout and spacing adjustments.

<CH.Code rows={7} show={["contact-form.module.scss"]}>

```scss contact-form.module.scss
.contactForm {
  @import "@faststore/ui/src/components/atoms/Button/styles.scss";
  @import "@faststore/ui/src/components/atoms/Input/styles.scss";
  @import "@faststore/ui/src/components/molecules/InputField/styles.scss";

  @include layout-content;

  display: grid;
  grid-template-columns: 1fr 1fr;
  column-gap: var(--fs-spacing-2);

  > div,
  form {
    margin: var(--fs-spacing-6) 0 var(--fs-spacing-3);
  }

  > div {
    p {
      width: 80%;
    }
  }

  h2 {
    font-family: var(--fs-text-face-title);
    font-size: var(--fs-text-size-title-page);
    margin: var(--fs-spacing-6) 0 var(--fs-spacing-3);
  }

  [data-fs-input-field] {
    margin: var(--fs-spacing-3) 0;
  }

  [data-fs-textarea] {
    width: 100%;
    margin-bottom: var(--fs-spacing-4);
    padding: var(--fs-spacing-2) var(--fs-spacing-2) 0;
    height: 150px;
  }

  [data-fs-button] {
    min-width: 250px;
    margin: auto;
  }
}
```

</CH.Code>

> ℹ️ For further details on code implementation, see the [ContactForm](https://github.com/vtex-sites/playground.store/tree/main/src/components/ContactForm) folder available in the [playground.store](https://github.com/vtex-sites/playground.store) repository.
---

### Synchronizing the changes with the Headless CMS

Add the section to the Headless CMS by following the instructions available in [syncing components with the Headless CMS](https://developers.vtex.com/docs/guides/faststore/overrides-syncing-components-with-the-headless-cms).
The following schema was used as an example:

<CH.Code rows={7} show={["sections.json"]}>

```json sections.json
[
  {
    "name": "ContactForm",
    "schema": {
      "title": "ContactForm",
      "description": "Adds a contact form",
      "type": "object",
      "properties": {}
    }
  }
]
```

</CH.Code>

> ℹ️ For further details on code implementation, see the `sections.json` file available in the playground.store repository.
</CH.Scrollycoding>

### Creating a new landing page

Let’s create a new landing page for the Contact Us page to add the new Contact form section. For this part, we will follow the [Creating a new page tutorial](https://help.vtex.com/en/tutorial/managing-pages--3DO6rBhZ1p3zndnFu5BgRt#creating-a-new-page).

1. Go to the VTEX Admin and access Storefront > Headless CMS.
2. Click `Create document` and select `Landing Page`.
3. In the `Sections` tab, click add (`+`) and choose the `ContactForm` section.
4. Go to the `Settings` tab and add the following path in the **Path** field: `/contact-us.`
5. Click `Save`.

## Results

Once you have [set your development mode](https://developers.vtex.com/docs/guides/building-sections/overrides/sending-components-to-the-headless-cms#previewing-changes-in-the-development-mode) to see the changes locally, access the `https://localhost:3000/contact-us` and you will see the new landing page with the Contact us form. Below, you can check a storefront example:

![contact-form-component](https://vtexhelp.vtexassets.com/assets/docs/src/api-extension-example-one___ceffcf6726b7316bbe61eaf4c013e069.png)
