---
title: Uploading files to Master Data
slug: 'uploading-files-to-master-data'
excerpt: 'Learn how to upload files to Master Data v1.'
hidden: false
---

This step-by-step guide will teach you how to upload files to Master Data v1.

## Step by step

### Step 1 - Creating a new data entity

1. Access the DynamicStorage at `https://{account}.ds.vtexcrm.com.br`.
   - _Remember to replace the value between curly braces according to your scenario._
2. Click **Data Entities** in the top bar.
3. Click **Add New**.
4. In the **Acronym** field, enter a two-letter acronym for the data entity you are creating.
5. In **Name**, enter the name of the data entity that will store the PDF file (e.g., _Files_, _PDFs_).
6. Go to the **Fields** tab. In the **Name** field, enter a new name for the field that will store the PDF file in lowercase letters (e.g., _filename_).
7. In **Display Name**, enter the data entity name chosen in Step 5, but with uppercase in the first letter (e.g., _Files_, _Pdf_).
8. In the **Type** dropdown menu, select **File**.
9. Click the "engine icon" ![Engine icon](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Master-Data/v1-guides/engine-icon.png) on the right side of the **Type** field.
10. Under the **General settings** section, select the **Make readable without credential** checkbox.
11. On **Custom field type settings**, select the **Max size per file** according to your scenario. This sets the maximum file size that can be uploaded to this field.
12. Click **Save**.

<video src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Master-Data/v1-guides/creating-a-new-data-entity.mp4" controls autoplay></video>

### Step 2 - Publishing and indexing the data entity

1. On the **Data Entities** tab, find the data entity you created in the previous step and click the "blue disk" button ![Save icon](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Master-Data/v1-guides/save-icon.png) on the left side of the line to publish the entity.
2. Click **Ok** to continue.
3. Click the "four arrows" ![Arrows icon](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Master-Data/v1-guides/arrows-icon.png) icon to reindex the data entity.

> ⚠️ Wait for the data entity to be fully indexed. This action may take anywhere from 30 minutes to 1 hour. During this time, do not make any changes to the data entity or its fields. Note that there is currently no interface to monitor the progress of indexation. Instead, you can periodically check the status of the entity.

<video src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Master-Data/v1-guides/publishing-and-indexing.mp4" controls autoplay></video>

### Step 3 - Creating a Master Data form

1. After waiting the required time, access the Master Data module at `https://{account}.vtexcrm.com.br`.
    - _Remember to replace the value between curly braces according to your scenario._
2. Click the **Advanced settings** tab.
3. Click **Formulários**.
3. Click **Novo** to create a new form.
4. In the **Nome** field, enter the name of the _formulário_, which should be the same as the data entity name.
6. In **Entidade de Dados**, select the data entity you previously created.
7. In the **Campos de Listagem** tab, select the **Id do Registro** and the data entity you previously created.
8. Change to the **Schemas de Layout** tab.
9. Click the **Incluir nova seção** button to add a new section to the form.
10. In the **Nome** field, enter a name for the section.
11. Select the data entity previously created from the column **Campos disponíveis**. Then, drag and drop it into the column **Campos da coluna 1**.
12. Click **Save**.

<video src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Master-Data/v1-guides/creating-a-master-data-form.mp4" controls autoplay></video>

### Step 4 - Uploding the file

Access the Master Data module at `https://{account}.vtexcrm.com.br`. By now, when accessing that URL, you should see a new tab with the name of the form you just created. If that's not the case, reload the page.

    - _Remember to replace the value in the curly brackets according to your scenario._

![Form](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Master-Data/v1-guides/form.png)

1. Click the tab with the name of your new form.
2. Click **Novo**.
3. Click the **Upload a File** button. Choose your file and click **Open**.
4. After the upload, click **Save**.

<video src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Master-Data/v1-guides/uploading-a-file.mp4" controls autoplay></video>

### Step 5 - Accessing the file

1. Click the tab with the name of your new form.
2. Copy the **Id do Registro** value and save it on a notepad. The **Id do Registro** value has the following pattern: `{acronym}-XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX`.
3. Access the file's public URL. Notice that the file's URL has the following pattern: `https://{account}.vtexcommercestable.com.br/api/dataentities/{acronym}/documents/{idWithouthAcronym}/{fieldName}/attachments/{file}`, where:
    - `acronym` - Two-letter acronym that identifies the data structure
    - `idWithouthAcronym` - Id of the document, without the acronym, i.e., the `XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX` from the **Id do Registro** value.
    - `fieldName` - Name of the field created in step 6 of **Step 1 - Creating a new data entity**.
    - `file` - Name of the file followed by its extension (e.g., `myfile.pdf`).
