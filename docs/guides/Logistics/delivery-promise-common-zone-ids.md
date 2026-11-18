---
title: "Delivery Promise common zone IDs"
slug: "delivery-promise-common-zones"
hidden: true
createdAt: "2026-11-18T00:00:00.000Z"
updatedAt: "2026-11-18T00:00:00.000Z"
excerpt: "Find the common zone IDs accepted by the Delivery Promise Notification API."
seeAlso:
 - "/docs/api-reference/delivery-promise-notification-api"
 - "/docs/guides/delivery-promise"
---

[Delivery Promise](https://developers.vtex.com/docs/guides/delivery-promise) allows shoppers to see products that are available for their location. For an external seller's products, the marketplace needs to know both the available quantity and where each delivery promise applies. External sellers provide this information through the [Delivery Promise Notification API](https://developers.vtex.com/docs/api-reference/delivery-promise-notification-api).

A common zone represents a geographic delivery area and groups one or more postal code ranges under a zone ID. In a delivery promise, the `deliveryZoneIds` field specifies the zones where the product can be delivered with the corresponding availability and delivery method.

Send one or more of the IDs listed below in `deliveryZoneIds` when calling either of these endpoints:

- [Update external product availability](https://developers.vtex.com/docs/api-reference/delivery-promise-notification-api#put-/api/delivery-promises/external-sellers/-sellerId-/products)
- [Update delivery promises for an external seller's item](https://developers.vtex.com/docs/api-reference/delivery-promise-notification-api#patch-/api/delivery-promises/external-sellers/-sellerId-/items/-itemId-)

The following tables list the common zones documented for Brazil and the United States. Select the zone that represents the product's delivery coverage. Use the zone ID in your request, not its name or postal code range. If one ID has multiple postal code ranges, all ranges are shown in the same table row.

## Brazil

| **Zone ID** | **Zone name** | **Postal code range** |
| :--- | :--- | :--- |
| `BRA_COUNTRY` | Todo o país | 01000-000–99999-999 |
| `BRA_REGION_NORTE` | Norte | 66000-000–69999-999<br>76800-000–77999-999 |
| `BRA_REGION_CENTRO_OESTE` | Centro-Oeste | 70000-000–76799-999<br>78000-000–79999-999 |
| `BRA_REGION_NORDESTE` | Nordeste | 40000-000–65999-999 |
| `BRA_REGION_SUDESTE` | Sudeste | 01000-000–39999-999 |
| `BRA_REGION_SUL` | Sul | 80000-000–99999-999 |
| `BRA_SUBSTATE_DF_CAPITAL` | Distrito Federal \| Brasília | 70000-000–70999-999 |
| `BRA_SUBSTATE_DF_INTERIOR` | Distrito Federal \| Cidades Satélite | 71000-000–72799-999<br>73000-000–73699-999 |
| `BRA_SUBSTATE_GO_CAPITAL` | Goiás \| Capital | 72800-000–72999-999<br>73700-000–74894-999 |
| `BRA_SUBSTATE_GO_INTERIOR` | Goiás \| Interior | 74895-000–76799-999 |
| `BRA_SUBSTATE_MT_CAPITAL` | Mato Grosso \| Capital | 78000-000–78109-999 |
| `BRA_SUBSTATE_MT_INTERIOR` | Mato Grosso \| Interior | 78110-000–78899-999 |
| `BRA_SUBSTATE_MS_CAPITAL` | Mato Grosso do Sul \| Capital | 79000-000–79129-999 |
| `BRA_SUBSTATE_MS_INTERIOR` | Mato Grosso do Sul \| Interior | 79130-000–79999-999 |
| `BRA_SUBSTATE_BA_CAPITAL` | Bahia \| Capital | 40000-000–41999-999 |
| `BRA_SUBSTATE_BA_REG_METROPOLITANA` | Bahia \| Região Metropolitana | 40000-000–44470-999 |
| `BRA_SUBSTATE_BA_INTERIOR` | Bahia \| Interior | 44471-000–48999-999 |
| `BRA_SUBSTATE_SE_CAPITAL` | Sergipe \| Capital | 49000-000–49099-999 |
| `BRA_SUBSTATE_SE_INTERIOR` | Sergipe \| Interior | 49100-000–49999-999 |
| `BRA_SUBSTATE_PE_CAPITAL` | Pernambuco \| Capital | 50000-000–52999-999 |
| `BRA_SUBSTATE_PE_REG_METROPOLITANA` | Pernambuco \| Região Metropolitana | 50000-000–54999-999 |
| `BRA_SUBSTATE_PE_INTERIOR` | Pernambuco \| Interior | 55000-000–56999-999 |
| `BRA_SUBSTATE_AL_CAPITAL` | Alagoas \| Capital | 57000-000–57099-999 |
| `BRA_SUBSTATE_AL_INTERIOR` | Alagoas \| Interior | 57100-000–57999-999 |
| `BRA_SUBSTATE_PB_CAPITAL` | Paraíba \| Capital | 58000-000–58099-999 |
| `BRA_SUBSTATE_PB_INTERIOR` | Paraíba \| Interior | 58100-000–58999-999 |
| `BRA_SUBSTATE_RN_CAPITAL` | Rio Grande do Norte \| Capital | 59000-000–59099-999 |
| `BRA_SUBSTATE_RN_INTERIOR` | Rio Grande do Norte \| Interior | 59100-000–59999-999 |
| `BRA_SUBSTATE_CE_CAPITAL` | Ceará \| Capital | 60000-000–60999-999 |
| `BRA_SUBSTATE_CE_REG_METROPOLITANA` | Ceará \| Região Metropolitana | 60000-000–61909-999 |
| `BRA_SUBSTATE_CE_INTERIOR` | Ceará \| Interior | 61910-000–63999-999 |
| `BRA_SUBSTATE_PI_CAPITAL` | Piauí \| Capital | 64000-000–64099-999 |
| `BRA_SUBSTATE_PI_INTERIOR` | Piauí \| Interior | 64100-000–64999-999 |
| `BRA_SUBSTATE_MA_CAPITAL` | Maranhão \| Capital | 65000-000–65099-999 |
| `BRA_SUBSTATE_MA_INTERIOR` | Maranhão \| Interior | 65100-000–65999-999 |
| `BRA_SUBSTATE_PA_CAPITAL` | Pará \| Capital | 66000-000–66999-999 |
| `BRA_SUBSTATE_PA_REG_METROPOLITANA` | Pará \| Região Metropolitana | 66000-000–67999-999 |
| `BRA_SUBSTATE_PA_INTERIOR` | Pará \| Interior | 68000-000–68899-999 |
| `BRA_SUBSTATE_AP_CAPITAL` | Amapá \| Capital | 68900-000–68914-999 |
| `BRA_SUBSTATE_AP_INTERIOR` | Amapá \| Interior | 68915-000–68999-999 |
| `BRA_SUBSTATE_AM_CAPITAL` | Amazonas \| Capital | 69000-000–69099-999 |
| `BRA_SUBSTATE_AM_INTERIOR` | Amazonas \| Interior | 69100-000–69299-999 |
| `BRA_SUBSTATE_RR_CAPITAL` | Roraima \| Capital | 69300-000–69300-999 |
| `BRA_SUBSTATE_RR_INTERIOR` | Roraima \| Interior | 69340-000–69389-999 |
| `BRA_SUBSTATE_AC_CAPITAL` | Acre \| Capital | 69900-000–69920-999 |
| `BRA_SUBSTATE_AC_INTERIOR` | Acre \| Interior | 69921-000–69999-999 |
| `BRA_SUBSTATE_TO_CAPITAL` | Tocantins \| Capital | 77000-000–77270-999 |
| `BRA_SUBSTATE_TO_INTERIOR` | Tocantins \| Interior | 77300-000–77995-999 |
| `BRA_SUBSTATE_RO_CAPITAL` | Rondônia \| Capital | 76800-000–76834-999 |
| `BRA_SUBSTATE_RO_INTERIOR` | Rondônia \| Interior | 76835-000–76999-999 |
| `BRA_SUBSTATE_SP_CAPITAL` | São Paulo \| Capital | 01000-000–05999-999<br>08000-000–08499-999 |
| `BRA_SUBSTATE_SP_REG_METROPOLITANA` | São Paulo \| Região Metropolitana | 01000-000–09999-999 |
| `BRA_SUBSTATE_SP_LITORAL` | São Paulo \| Litoral | 11000-000–11999-999 |
| `BRA_SUBSTATE_SP_INTERIOR` | São Paulo \| Interior | 12000-000–19999-999 |
| `BRA_SUBSTATE_RJ_CAPITAL` | Rio de Janeiro \| Capital | 20000-000–23799-999 |
| `BRA_SUBSTATE_RJ_REG_METROPOLITANA` | Rio de Janeiro \| Região Metropolitana | 20000-000–26599-999 |
| `BRA_SUBSTATE_RJ_INTERIOR` | Rio de Janeiro \| Interior | 26601-000–28999-999 |
| `BRA_SUBSTATE_ES_CAPITAL` | Espírito Santo \| Capital | 29000-000–29099-999 |
| `BRA_SUBSTATE_ES_INTERIOR` | Espírito Santo \| Interior | 29100-000–29999-999 |
| `BRA_SUBSTATE_MG_CAPITAL` | Minas Gerais \| Capital | 30000-000–31999-999 |
| `BRA_SUBSTATE_MG_REG_METROPOLITANA` | Minas Gerais \| Região Metropolitana | 30000-000–34999-999 |
| `BRA_SUBSTATE_MG_INTERIOR` | Minas Gerais \| Interior | 35000-000–39999-999 |
| `BRA_SUBSTATE_PR_CAPITAL` | Paraná \| Capital | 80000-000–82999-999 |
| `BRA_SUBSTATE_PR_REG_METROPOLITANA` | Paraná \| Região Metropolitana | 80000-000–83800-999 |
| `BRA_SUBSTATE_PR_INTERIOR` | Paraná \| Interior | 83801-000–87999-999 |
| `BRA_SUBSTATE_SC_CAPITAL` | Santa Catarina \| Capital | 88000-000–88100-999 |
| `BRA_SUBSTATE_SC_REG_METROPOLITANA` | Santa Catarina \| Região Metropolitana | 88000-000–88469-999 |
| `BRA_SUBSTATE_SC_INTERIOR` | Santa Catarina \| Interior | 88470-000–89999-999 |
| `BRA_SUBSTATE_RS_CAPITAL` | Rio Grande do Sul \| Capital | 90000-000–91999-999 |
| `BRA_SUBSTATE_RS_REG_METROPOLITANA` | Rio Grande do Sul \| Região Metropolitana | 90000-000–94900-999 |
| `BRA_SUBSTATE_RS_INTERIOR` | Rio Grande do Sul \| Interior | 94901-000–99999-999 |

## United States

| **Zone ID** | **Zone name** | **Postal code range** |
| :--- | :--- | :--- |
| `USA_COUNTRY` | Entire Country | 00501–99950 |
| `USA_DIVISION_NEW_ENGLAND` | New England | 01001–05907 |
| `USA_STATE_CT` | Connecticut | 06001–06389<br>06401–06928 |
| `USA_STATE_ME` | Maine | 03901–04992 |
| `USA_STATE_MA` | Massachusetts | 01001–02791<br>05501–05544 |
| `USA_STATE_NH` | New Hampshire | 03031–03897 |
| `USA_STATE_RI` | Rhode Island | 02801–02940 |
| `USA_STATE_VT` | Vermont | 05001–05499<br>05545–05907 |
| `USA_DIVISION_MIDDLE_ATLANTIC` | Middle Atlantic | 07001–19640 |
| `USA_STATE_NJ` | New Jersey | 07001–08989 |
| `USA_STATE_NY` | New York | 10001–14975 |
| `USA_STATE_PA` | Pennsylvania | 15001–19640 |
| `USA_DIVISION_EAST_NORTH_CENTRAL` | East North Central | 43001–62999 |
| `USA_STATE_IL` | Illinois | 60001–62999 |
| `USA_STATE_IN` | Indiana | 46001–47997 |
| `USA_STATE_MI` | Michigan | 48001–49971 |
| `USA_STATE_OH` | Ohio | 43001–45999 |
| `USA_STATE_WI` | Wisconsin | 53001–54990 |
| `USA_DIVISION_WEST_NORTH_CENTRAL` | West North Central | 50001–69367 |
| `USA_STATE_IA` | Iowa | 50001–52809 |
| `USA_STATE_KS` | Kansas | 66002–67954 |
| `USA_STATE_MN` | Minnesota | 55001–56763 |
| `USA_STATE_MO` | Missouri | 63001–65899 |
| `USA_STATE_NE` | Nebraska | 68001–68118<br>68122–69367 |
| `USA_STATE_ND` | North Dakota | 58001–58856 |
| `USA_STATE_SD` | South Dakota | 57001–57799 |
| `USA_DIVISION_SOUTH_ATLANTIC` | South Atlantic | 19701–34997 |
| `USA_STATE_DE` | Delaware | 19701–19980 |
| `USA_STATE_FL` | Florida | 32004–34997 |
| `USA_STATE_GA` | Georgia | 30001–31999 |
| `USA_STATE_MD` | Maryland | 20601–20734<br>20759–20797<br>20812–21930 |
| `USA_STATE_NC` | North Carolina | 27006–28909 |
| `USA_STATE_SC` | South Carolina | 29001–29948 |
| `USA_STATE_VA` | Virginia | 20040–20041<br>22001–24658 |
| `USA_STATE_WV` | West Virginia | 24701–26886 |
| `USA_STATE_DC` | District of Columbia | 20001–20039<br>20042–20599<br>20799–20799 |
| `USA_DIVISION_EAST_SOUTH_CENTRAL` | East South Central | 35004–42788 |
| `USA_STATE_AL` | Alabama | 35004–36925 |
| `USA_STATE_KY` | Kentucky | 40003–42788 |
| `USA_STATE_MS` | Mississippi | 38601–39776 |
| `USA_STATE_TN` | Tennessee | 37010–38589 |
| `USA_DIVISION_WEST_SOUTH_CENTRAL` | West South Central | 70001–88589 |
| `USA_STATE_AR` | Arkansas | 71601–72959 |
| `USA_STATE_LA` | Louisiana | 70001–71497 |
| `USA_STATE_OK` | Oklahoma | 73001–73300<br>73302–74966 |
| `USA_STATE_TX` | Texas | 73301–73301<br>75001–75501<br>75503–79999<br>88510–88589 |
| `USA_DIVISION_MOUNTAIN` | Mountain | 59001–89883 |
| `USA_STATE_AZ` | Arizona | 85001–86556 |
| `USA_STATE_CO` | Colorado | 80001–81658 |
| `USA_STATE_ID` | Idaho | 83201–83876 |
| `USA_STATE_MT` | Montana | 59001–59937 |
| `USA_STATE_NV` | Nevada | 88901–89883 |
| `USA_STATE_NM` | New Mexico | 87001–88441 |
| `USA_STATE_UT` | Utah | 84001–84784 |
| `USA_STATE_WY` | Wyoming | 82001–83120 |
| `USA_DIVISION_PACIFIC` | Pacific | 90001–99950 |
| `USA_STATE_AK` | Alaska | 99501–99950 |
| `USA_STATE_CA` | California | 90001–96162 |
| `USA_STATE_HI` | Hawaii | 96701–96898 |
| `USA_STATE_OR` | Oregon | 97001–97920 |
| `USA_STATE_WA` | Washington | 98001–99403 |
