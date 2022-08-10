---
title: "Macromex Scala"
slug: "macromex-scala"
excerpt: "macromex.scala@0.0.122"
hidden: true
createdAt: "2022-07-05T08:28:32.874Z"
updatedAt: "2022-08-09T14:57:48.505Z"
---
## Installation & Setup

#### Installation
- Run the following command on VTEX toolbelt:

> vtex install macromex.scala@0.x

#### Setup
1. Go to `Admin > Apps > My Apps > Macromex Scala > Settings`
2. Fill up the fields with your tokens and keys and press `Save`
3. **TODO ce sunt aceste campuri si de ce este nevoie de ele? ex CategoryId, email alerts**


## Behind the scenes

#### Masterdata Entities & Schemas  

This app uses several Masterdata entities & schemas

* For clients information
    * Entity: **MacromexClient**
    * Schema: **macromex_client_v1**
    
```
{
  "properties": {
    "code": {"type": "string"},
    "name": {"type": "string"},
    "tax_registration_number": {"type": "string"},
    "company_registration_number": {"type": "string"},
    "bank_account": {"type": "string"},
    "price_list": {"type": "string"},
    "doc_layout": {"type": "string"},
    "language_code": {"type": "string"},
    "organization_id": {"type": "string"}
  },
  "v-default-fields": ["name", "code", "id"],
  "required": ["name", "code"],
  "v-indexed": ["name", "code", "organization_id"],
  "v-security": {
    "allowGetAll": true,
    "publicRead": ["id", "name", "code", "organization_id"],
    "publicWrite": ["name"],
    "publicFilter": ["name", "code", "organization_id", "id"]
  }
}
```    

*  For client addresses
    * Entity: **MacromexClientAddress**
    * Schema: **macromex_address_v1**
    
```
{
  "properties": {
    "client_id": {"type": "string"},
    "code": {"type": "string"},
    "address": {"type": "string"},
    "zipcode": {"type": "string"},
    "delivery_address_code": {"type": "string"},
    "delivery_address_name": {"type": "string"},
    "delivery_address": {"type": "string"},
    "delivery_zipcode": {"type": "string"},
    "delivery_days": {"type": "string"}
  },
  "v-default-fields": ["address", "code", "id"],
  "required": ["address", "code"],
  "v-indexed": ["address", "code", "delivery_address_code"],
  "v-security": {
    "allowGetAll": true,
    "publicRead": ["id", "address", "code", "delivery_days", "delivery_address_code"],
    "publicWrite": ["address"],
    "publicFilter": ["address", "code", "id", "delivery_address_code"]
  }
}
```

* For orders
    * Entity: **MacromexOrder**
    * Schema: **macromex_order_v1**
    
```
{
  "properties": {
    "order_number": {"type": "string"},
    "eva_no": {"type": "string"},
    "delivery_date": {"type": "string"},
    "delivery_note": {"type": "string"},
    "invoice_no": {"type": "string"},
    "truck": {"type": "string"},
    "driver_name": {"type": "string"},
    "driver_phone": {"type": "string"},
    "planned_delivery_time": {"type": "string"},
    "picked": {"type": "string"},
    "loaded": {"type": "string"},
    "delivered": {"type": "string"},
    "delivery_time": {"type": "string"},
    "stock_code": {"type": "string"},
    "qty_ordered": {"type": "string"},
    "qty_alloc": {"type": "string"},
    "qty_deliv": {"type": "string"}
  },
  "v-default-fields": ["order_number", "id"],
  "required": ["order_number"],
  "v-indexed": ["order_number", "qty_alloc","stock_code"],
  "v-security": {
    "allowGetAll": true,
    "publicRead": ["id", "order_number"],
    "publicWrite": ["order_number"],
    "publicFilter": ["order_number", "id"]
  }
}
```    

* For invoices    
    * Entity: **MacromexInvoice**
    * Schema: **macromex_invoice_v1**
    
 ```
{
  "properties": {
    "order_number": { "type": "string" },
    "code": { "type": "string" },
    "invoice_date": {  "type": "string" },
    "data": { "type": "string" }
  },
  "v-default-fields": ["order_number", "id", "code", "invoice_date", "data"],
  "required": ["order_number"],
  "v-indexed": ["order_number", "code", "invoice_date"],
  "v-security": {
    "allowGetAll": true,
    "publicRead": ["id", "order_number", "code", "invoice_date"],
    "publicWrite": ["order_number", "code", "invoice_date"],
    "publicFilter": ["order_number", "id", "code", "invoice_date"]
  }
}
 ``` 
  
* For financial information
    * Entity: **ScalaFinancial**
    * Schema: **financial**
    
```
 {
   "properties": {
     "code": { "type": "string" },
     "credit_limit": { "type": "string" },
     "balance": { "type": "string" },
     "ordered_not_shipped": { "type": "string" },
     "shipped_not_invoiced": { "type": "string" },
     "delivery_block": { "type": "string" },
     "auto_deliv_block": { "type": "string" },
     "blocked": { "type": "string" }
   },
   "v-default-fields": ["id", "code", "credit_limit", "balance", "ordered_not_shipped", "shipped_not_invoiced", "delivery_block", "auto_deliv_block", "blocked" ],
   "required": [ "code" ],
   "v-indexed": [ "code" ],
   "v-security": {
     "allowGetAll": true,
     "publicRead": [ "id", "code", "credit_limit", "balance", "ordered_not_shipped", "shipped_not_invoiced", "delivery_block", "auto_deliv_block", "blocked" ],
     "publicWrite": [ "id", "code", "credit_limit", "balance", "ordered_not_shipped", "shipped_not_invoiced", "delivery_block", "auto_deliv_block", "blocked" ],
     "publicFilter": [ "id", "code", "credit_limit", "balance", "ordered_not_shipped", "shipped_not_invoiced", "delivery_block", "auto_deliv_block", "blocked" ]
   }
 }
  ```  

* For organization (from vtex.organizations app)
    * Entity: **BusinessOrganization**
    * Schema: **business-organization-schema-v1**
> More information can be found here: https://github.com/vtex-apps/organizations

#### Base url: https://{{vendor}}.myvtex.com/no-cache

|  #  |        Route        | Method | Description |
| --- | ------------------- | ------ | ----------- |
| 1   | /products-sync      |  POST  | Used for product synchronizations. |
| 2   | /clients-sync       |  POST  | Used for clients synchronizations. |
| 3   | /create-order       |  POST  | This route is used as order-hook. For each order created, VTEX calls this route with the order data. This creates an XML that it sends to Scala.  |
| 4   | /orders-sync        |  POST  | Used for orders synchronizations.|
| 5   | /invoices-sync      |  POST  | Used for invoices synchronizations.|
| 6   | /financial-sync     |  POST  | Used for financial data synchronizations.|
| 7   | /price-lists-sync   |  POST  | Used for price lists synchronizations.|
| 8   | /client-prices-sync |  POST  | Used for client prices synchronizations.|


### VTEX - Scala Syncs:
-	Clients & Addresses
-	Financial Data
-	Orders
-	Invoices
-	Products
-	Price lists
-	Client price lists
-	Send Orders


Files with all the necessary information are retrieved via the API from the OUT folder.
**TODO add node-scala-ftp mention here and mention IN folder from the ftp**

### 1. Clients & Addresses (marketplace) 
Pentru fiecare client preluat:
**TODO maybe replace with this?** Foreach customer entry in the csv file:  
- It is checked if his organization exists:  
    - If exists: the data is updated with new information.
    - If it doesn't exists: a new organization is created.  
- Check if the client has an account  **TODO ce cont este creat? ai spus mai sus pentru fiecare client preluat.. Din Scala se preiau organizatii, cum verifici si creezi cont pentru ele?**
    - If it does: its account is updated with the information taken at that time.  
    - If not: An account is automatically created  
- Check if the address exists for that client  
    - If exists: the data is updated with their information.  
    - IF it doesn't exists: a new address is created.  

### 2. Financial data (marketplace)  
Financial data includes credit accounts and information on whether or not a customer is blocked.  
The first time it is checked if the financial information exists or not in the master data.  
- If it exists, the information is updated
- If it does not exist, enter the data.

### 2.1 Credit accounts  
The information about the organization is taken over and it is checked if there is a credit account for it.  
- If it does not exist, the respective account is created and all users are added as additional holders. **TODO mentioneaza ca nu functioneaza adaugarea de additional holders, iar la prima creare de astfel de cont, nu cred ca avem ce account holders sa adaugam**
- If it exists, the credit limit and the available credit are updated and it is checked if all the clients from the platform are additional holders. If there is an account that is not an additional holder, it is added. 

### 2.2 Block Client
We take over the isBlocked field and check all the users in the respective organization. If that field differs, it is updated with the received information.
**TODO Bazat pe ce informatie din csv modificam acest camp? unde este campul?**

### 3. Orders (seller)
We check for each order to see if it exists in the master data.  **TODO WIP**
- If it doesn't exists: a new order is created
- If it exists: We update the information in the order

### 3.1 We check the quantities and products that are sent. If there are differences between the data in the file and those in the initial order, the initial order is canceled and a new order is created with the new information.

### 4. Invoices (seller)
We enter the invoices in the master date and send a notification to VTEX with the invoice number, value, products, date of issue and its url. The invoice URL is generated by us in the form (https://mercadi.ro/get-invoice/?oid = .... Or https://bocado.ro/get-invoice/?oid = .... ) and the invoice is displayed by the invoicing application.

### 5. Products (seller)

We check if the products exist in the platform.
- If exists
    - We update stocks
    - We update the specifications
    - We send notification to each marketplace to update the specifications and the unitMultiplier
- If it doesn't exists, we create a new product
    - We process the categories and enter them if necessary
    - We create the product and the SKU
    - We save stocks and specifications
    - We send notification to marketplaces for specifications

### 6. Price Lists (marketplace)

- We update or add product price information, depending on the “priceTableId” which is used in point 7 to display different prices depending on the customer.
- We update sales policy in seller (00: mcxtt, 05: mcxhoreca)

### 7. Client price lists (marketplace)
We update price information for customers

### 8. When a new order is placed in VTEX, the application creates an XML with the order data and sends it to the SCALA that saves it in FTP, in the IN folder. 

This does not apply to the orders in point 3.1.


## Other applications:

- macromex.clients
- macromex.customer-credit-checkout
- macromex.front-organizations
- macromex.invoicing
- macromex.my-deliveries
- macromex.pixels
- macromex.price-details
- macromex.registration

### macromex.clients

This app is installed on both marketplaces.
The application displays the clients section in admin.
From this area you can:
- See all the organizations
- Users in the organizations
- Addresses.
- Addresses can be assigned to users.
- Users roles and statuses can be updated

> Required settings:
> * This application doesn't need any settings.

  
### macromex.customer-credit-checkout  

This app creates the following route `/customercredit-checkout/check-user`
This application is used on checkout to verify financial information about the customer, if there are outstanding payments or if the user is blocked.
The `Place order` button is hidden and a warning message is displayed

> Required settings:
> - Seller name
> - Seller app key
> - Seller app token
> - Marketplace app key
> - Marketplace app token

### macromex.front-organizations  

This app displays the `My organization` page in `My account` section.
From this page:
- new users can be added to the organization or they can be deleted from the organization.
- Users' permissions and status can be changed
- Addresses can be assigned to users
- Addresses can be deleted from users

> Required settings:
> - Marketplaces app key
> - Marketplaces app token


### macromex.invoicing

This app displays the `My invoices` page in `My account` section.  
On this page you can see all the information about the invoices

> Required settings:
> - Seller name
> - Seller app key
> - Seller app token


### macromex.my-deliveries

This app displays the `My deliveries` page in `My account` section.  
On this page you can see all the information about the deliveries

> Required settings:
> - Seller name
> - Seller app key
> - Seller app token


###macromex.price-details


This application is used on the product page to display prices per kg, quantities per box and subtotal

> Required settings:
> * This application doesn't need any settings.

### macromex.registration

This application generates the path `/create-account` and is used to create accounts.

> Required settings:
> - Seller name
> - Seller app key
> - Seller app token
> - Marketplaces app key
> - Marketplaces app token
> - Email addresses for notifications