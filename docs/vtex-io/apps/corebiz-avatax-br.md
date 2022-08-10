---
title: "Avatax-BR"
slug: "corebiz-avatax-br"
excerpt: "corebiz.avatax-br@1.0.1"
hidden: true
createdAt: "2022-07-20T17:59:44.485Z"
updatedAt: "2022-08-09T17:33:44.008Z"
---
This app enables tax calculations using AvaTax-Brazil V3 api services from Avalara.

> This app requires external subscription to Avalara.

The Avatax-BR conector is an app which connects to VTEX Tax Hub allowing Avalara to calculate taxes in various B2B (or B2C) scenarios. 

This app is only compatible with Brazil stores.

#### Installation

You can install this app through VTEX App Store or by command-line using `VTEX Toolbelt`:

```
vtex install vtex.avatax-br@2.x
```

After installation, this app requires additional configurations in your store account, which will be described as following. **Don't worry**: The app will only be activated through a on/off switch in the Avatax Br admin page.

#### Initial Setup

The following steps must be followed:
- MasterData configuration (AS, AE, AL and CL entities)
- Establishment configuration through the admin app
- SKU Integration (must be custom-built)
- Client registration form (must be custom-built)

#### MasterData Configuration

First, go to MasterData on the Admin sidebar, and click on the "Advanced Settings" button. In the configurations panel, click on "Data structures". There you'll be able to edit and create MasterData structures. For this app, you need to create three new entities: AS (skus), AE (establishments) and AL (logs), and edit an existent one CL (clients).

![](https://user-images.githubusercontent.com/1629129/125787544-95a06cfc-e6f3-4697-8c07-8bf589bdf891.png)

##### 1 - Avatax SKUs
Contains relevant product data required by Avalara.
**Acronym**: AS
**Name**: Avatax SKUs

| Name    | Display Name | Data Type    | Nullable | Searchable | Filterable |
|---------|----------|---------|---------|----------|-----------|
| skuId   | SKU ID   | Integer | Yes     | Yes      | Yes       |
| skuInfo | SKU Info | Text    | Yes     |          |           |
|         |          |         |         |          |           |

**skuId**: The id of the SKU in VTEX.
**skuInfo**: A string in JSON format which should contain all needed properties to perform tax calculation. These properties will be described in a later topic (SKU integration)

![](https://user-images.githubusercontent.com/1629129/125787730-39825489-97ae-414b-80f7-c7303c5d7119.png)

##### 2 - Avatax Establishments
To Avalara, the establishments represent the source (dock) of the products being sold. There should be as many establishments as there are docks.

**Acronym**: AE
**Name**: Avatax Establishments

| Name           	| Display Name             	| Data Type        	| Nullable 	| Searchable 	| Filterable 	|
|----------------	|----------------------	|-------------	|---------	|----------	|-----------	|
| activitySector 	| Activity Sector   	| Text        	| Yes     	|          	|           	|
| city           	| City               	| Varchar 750 	| Yes     	|          	|           	|
| cnpj           	| CNPJ                 	| CPF / CNPJ  	| Yes     	|          	|           	|
| complement     	| Complement          	| Text        	| Yes     	|          	|           	|
| dockId         	| Dock Id           	| Varchar 100 	| Yes     	| Yes      	| Yes       	|
| dockName       	| Dock Name         	| Text        	| Yes     	|          	|           	|
| entityType     	| Entity Type     	| Text        	| Yes     	|          	|           	|
| icmsTaxPayer   	| Is ICMS Tax Payer  	| Boolean     	| Yes     	|          	|           	|
| pCredSN        	| ICMS Tax Rate     	| Integer     	| Yes     	|          	|           	|
| phone          	| Phone Number             	| Phone   	| Yes     	|          	|           	|
| neighborhood   	| Neighborhood               	| Varchar 750 	| Yes     	|          	|           	|
| state          	| State               	| Varchar 100 	| Yes     	|          	|           	|
| stateTaxId     	| State Tax Id   	| Text        	| Yes     	|          	|           	|
| street         	| Street           	| Varchar 750 	| Yes     	|          	|           	|
| streetNumber   	| Street Number               	| Integer     	| Yes     	|          	|           	|
| suframa        	| Suframa              	| Text        	| Yes     	|          	|           	|
| taxRegime      	| Tax Regime 	| Text        	| Yes     	|          	|           	|
| zipCode        	| Postal Code        	| CEP         	| Yes     	|          	|           	|

**activitySector**: The company's activity sector.
**city**: City where the establishment is located.
**cnpj**: Corporate document of the establishment.
**complement**: Complement of the establishment's address.
**dockId**: Id of the VTEX dock.
**dockName**: Name of the VTEX dock.
**entityType**: Entity Type (Company, Individual, Government, etc)
**icmsTaxPayer**: Defines if the entity is an ICMS taxpayer.
**pCredSN**: Rate for calculating the use of ICMS credit.
**neighborhood**: Neighborhood of the establishment's address.
**state**: State of the establishment's address.
**stateTaxId**: State registration of the company, if it is an ICMS tax payer.
**street**: Street address of the establishment.
**streetNumber**: Address number of the establishment.
**suframa**: Suframa number ("Superintendencia da Zona Franca de Manaus").
**taxRegime**: Company's tax regime (simplified, real profit, estimated profit, and so on).
**zipCode**: Postal code of the establishment's address.

##### 3 - Avatax Logs
Every tax calculation is saved in this entity for later queries.
**Acronym**: AL
**Name**: Avatax Logs

| Name              	| Display Name                     	| Data Type        	| Nullable 	| Searchable 	| Filterable 	|
|-------------------	|------------------------------	|-------------	|---------	|----------	|-----------	|
| avalaraReturn     	| Avalara Response             	| Text        	| Sim     	|          	|           	|
| client            	| Client                      	| Text        	| Sim     	|          	|           	|
| email             	| Client Email     	| Varchar 100 	| Sim     	|          	|           	|
| establishment     	| Establishment              	| Text        	| Sim     	|          	|           	|
| freightSimulation 	| Freight Simulation           	| Currency    	| Sim     	|          	|           	|
| orderId           	| Checkout/Order ID        	| Varchar 100 	| Sim     	| Sim      	| Sim       	|
| payLoad           	| Avalara Request                   	| Text        	| Sim     	|          	|           	|
| type              	| Log Type 	| Text        	| Sim     	|          	|           	|

**avalaraReturn**: The response from Avalara's APIs.
**client**: Object containing client data.
**email**: The email of the client.
**establishment**: Object containing establishment data.
**freightSimulation**: Freight simulation value total.
**orderId**: Unique session id for the checkout step, or orderId in case the purchase has been completed.
**payLoad**: The request sent to Avalara's APIs.
**type**: PDP/Checkout. Specifies where exactly the calculation process was called. PDP means the "productTax" endpoint, checkout means it was called on the checkout steps.

##### Client Entity Changes
The following fields must be added to the client (CL) entity:

| Name           	| Display Name             	| Data Type        	| Nullable 	| Searchable 	| Filterable 	|
|----------------	|----------------------	|-------------	|---------	|----------	|-----------	|
| activitySector 	| Activity Sector   	| Text        	| Sim     	|          	|           	|
| entityType     	| Entity Type     	| Text        	| Sim     	|          	|           	|
| icmsTaxPayer   	| Is ICMS Tax Payer 	| Boolean     	| Sim     	|          	|           	|
| pCredSN        	| ICMS Tax Rate     	| Integer     	| Sim     	|          	|           	|
| stateTaxId     	| State Tax Id   	| Varchar 750 	| Sim     	|          	|           	|
| taxRegime      	| Tax Regime 	| Text        	| Sim     	|          	|           	|
| useType        	| Use Type          	| Varchar 100 	| Sim     	|          	|           	|
| usagePurpose   	| Usage Purpose     	| Varchar 100 	| Sim     	|          	|           	|

**activitySector**: The entity's activity sector. Allowed values:
> **armedForces**
> **auctioneer**
> **audiovisualIndustry**
> **bondedWarehouse**
> **broadcastingIndustry**
> **construction**
> **coops**
> **distributor**
> **distributionCenter**
> **electricityDistributor**
> **energyGeneration**
> **extractor**
> **farmCoop**
> **filmIndustry**
> **finalConsumer**
> **fuelDistributor**
> **generalWarehouse**
> **importer**
> **industry**
> **itaipubiNacional**
> **maritimeService**
> **mealSupplier**
> **nonProfitEntity**
> **pharmaDistributor**
> **publicAgency**
> **religiousEstablishment**
> **retail**
> **ruralProducer**
> **securityPublicAgency**
> **service**
> **stockWarehouse**
> **telco**
> **transporter**
> **waterDistributor**
> **wholesale**

**entityType**: Entity type. Allowed values:
> **business**
> **individual**
> **federalGovernment**
> **stateGovernment**
> **cityGovernment**
> **foreign**
> **mixedCapital**
> **coops**

**icmsTaxPayer**: true if the entity is an ICMS tax payer.
**pCredSN**: ICMS tax rate.
**stateTaxId**: State tax id. Mandatory is the entity is an ICMS tax payer.

**taxRegime**: The entity's tax regime. Allowed values:
> **realProfit**
> **estimatedProfit**
> **simplified**
> **simplifiedOverGrossthreshold**
> **simplifiedEntrepeneur**
> **individual**

**useType**: Type of "use" for which the customer's purchases are intended. Allowed values:
> **use or consumption**
> **resale**
> **agricultural production**
> **production**
> **fixed assets**

**usagePurpose**: Optional free text which describes the useType field in detail.

#### Application Configuration
After configuring MasterData, access the application through the VTEX Admin menu and click on *Others -> Avatax Br*:

On the main tab we have the application's settings area, where you can turn the connector on/off and enable the sandbox environment (that makes so the app requests reach Avalara's sandbox servers instead of production).

You also need to fill in the **clientId** and **clientSecret** parameters. Those are provided by Avalara (or generated through their platform). After filling them in, click on  "Verify Ping" to ensure the connection is operational.

![](https://user-images.githubusercontent.com/1629129/125787878-dcb9379a-8a24-40e6-bf56-0162685f3bbb.png)

#### Establishment Configuration

You can see that there are two stock related tabs: "Add stock" and "Current stocks". The configuration of stocks, which are equivalent to the establishment at Avalara (represented by the entity AE of MasterData), is one of the necessary steps for the adequate operation of the connector. To get started, go to the second tab, "Add Stock" and register all the establishments.

Keep in mind that the connector works only for docks that have an associated establishment, so make sure that the establishments are properly registered.

![](https://user-images.githubusercontent.com/1629129/125788018-0d0bb86e-5e9f-43b2-be37-ea953abc9c24.png)

#### Sku Integration

In addition to the establishments, SKUs need to be properly entered in MasterData, based on information coming from the ERP. The sku structure contains two fields, skuId which corresponds to the SKU ID in VTEX, and skuInfo, which contains the additional data we send during tax calculation. The skuInfo field is a text field which must be in a JSON format, respecting the following structure:

**itemCode**: Code of the item in the ERP. *Type: string*.
**itemDescriptor.taxCode**: Auxiliary code for determining the legal basis of the item, registered in Avalara's system, used mainly to promote disambiguation in some cases of conflicts between tax rules. *Type: string*.
**itemDescriptor.hsCode**: NCM (Mercosul Common Nomenclature) code of the product. *Type: string.*
**itemDescriptor.ex**: Tax exception code, linked to IPI. *Type: string*.
**itemDescriptor.cean**: Item bar code (EAN). *Type: string*.
**itemDescriptor.source**: Code which defines the origin of the item. *Type: string*. Allowed values:
> **0**: Domestic goods, except those treated in codes 3,4,5 and 8.
> **1**: Foreign goods imported directly by the seller, except those treated in code 6.
> **2**: Foreign goods acquired in the domestic market (within Brazil), except those treated in code 7.
> **3**: Domestic goods with imported content above 40% and of value less than or equal to 70%.
> **4**: Domestic goods produced following "standard basic processes", as established by legislation (standard basic processes are designed to separate simple assembly from manufacturing processes) 
> **5**: Domestic goods with imported content less than or equal to 40%.
> **6**: Foreign goods imported directly by the seller without national equivalent as listed by Comex and natural gas.
> **7**: Foreign goods purchased in the domestic market (within Brazil) without national equivalent as listed by Comex and natural gas.
> **8**: National goods with imported content above 70%.
itemDescriptor.

**productType**: Fiscal type of the product according to SPED table. *Type: string*. Allowed values:
> **FOR PRODUCT**: Finished product
> **FOR MERCHANDISE**: Goods for resale
> **SERVICE**: Services
> **FEEDSTOCK**: Raw materials
> **FIXED ASSETS**: Fixed Assets
> **PACKAGING**: Packaging
> **PRODUCT IN PROCESS**: Product in process
> **SUBPRODUCT**: By-product
> **INTERMEDIATE PRODUCT**: Intermediate product
> **MATERIAL FOR USAGE AND CONSUMPTION**: Material for Use and Consumption
> **OTHER INPUTS**: Other inputs
> **NO RESTRICTION**: Other

**itemDescriptor.manufacturerEquivalent**: Item is a commodity, but will be considered as a product. *Type: boolean*.

**JSON Example**:
```
{
    "itemCode": "12345",
    "itemDescriptor": {
        "taxCode": "",
        "hsCode": "85171231"
        "ex": "",
        "cest": "2105301"
        "cean": "",
        "source": "4", "source": "4",
        "productType": "FOR MERCHANDISE",
        "manufacturerEquivalent": true
    }
}
```

This json **must** be converted to text and inserted from an integration between ERP and VTEX MasterData. It is worth noting that the skuInfo is a **string** and not an object, so all its content must be enclosed in quotes ("").

Below is an example of a request (cURL) to insert a sku:
```
curl --location --request POST 'http://{{account}}.myvtex.com/api/dataentities/AS/documents' \
--header 'Content-Type: application/json' \
--data-raw '{
    "skuId": 1,
    "skuInfo": "{\"itemCode\":\"12345\",\"itemDescriptor\":{\"taxCode\":\"\",\"hsCode\":\"85171231\",\"ex\":\"\",\"cest\":\"2105301\",\"cean\":\"\",\"source\":\"4\",\"productType\":\"FOR MERCHANDISE\",\"manufacturerEquivalent\":true}}"
}'
```

Since these are private entities, it is also necessary to have authorization to add this information to MasterData, so authorization parameters must be placed in the header:

**VtexIdclientAutCookie**: To obtain this value you must open the Developer Tools on your browser, on the Applications tab, while inside the VTEX Admin. Then look for Cookie values and copy the value of the VtexIdclientAutCookie cookie value.

**AppKey/AppToken**: To get the AppKey and AppToken, log into the admin and go to the "Account Management" tab and then click on "Account". You can see all registered tokens in the security area. You can create one by clicking on "Generate appKey and appToken", then fill in the request information and click on "Generate new tokens".

#### Using Avatax BR
After finishing the setup and activating the connector your store will be able to calculate and display taxes and fees through Avalara. 

In summary, the steps for configuring and using the connector are:
* MasterData Structure
* Application Settings
* Customer Master Data Customization
* Establishment registration
* SKU Integration
* Connector activation through the Settings screen

To see everything working just enter your store, login and add the product to the cart. When you enter the cart, the taxes calculated by Avalara will automatically appear and the final amount will be calculated with the addition of taxes. Each operation during the checkout process, from the cart to the checkout, such as change of address, change of quantity and inclusion / removal of products, causes a new calculation and the information is automatically updated. 

![](https://user-images.githubusercontent.com/1629129/125788192-7fd8fa6e-584f-448f-839f-d5dc02d0b7da.png)

#### Viewing the Logs
You can view all tax and fee calculations performed by the connector through the Logs tab.

In this table you can view all the calculations performed and their city/state of origin and destination, and included/highlighted taxes. The "Refresh" button reloads the logs, and you can filter the view of the columns and display more or fewer rows through the table buttons.

![](https://user-images.githubusercontent.com/1629129/125788247-0b1b4826-5d47-445c-8032-f14ecebaad88.png)

If you want to view the entire contents of a calculation, simply click the icon in the "Details" column.

Besides being able to analyze Avalara's answer in full, it is also possible to download just the request object (for further simulations and/or questions with Avalara).

![](https://user-images.githubusercontent.com/1629129/125788312-325b2edd-4b78-4aae-8783-295a35dc5809.png)

The logs screen also allows you to export the log files and filter by order number, to investigate which tax calculation was performed for a specific purchase.