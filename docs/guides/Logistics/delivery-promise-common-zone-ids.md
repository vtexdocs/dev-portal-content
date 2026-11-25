---
title: "Delivery Promise common zone IDs"
slug: "delivery-promise-common-zone-ids"
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

Use the zone ID in your request, not its name or postal code range. If one ID has multiple postal code ranges, all ranges are shown in the same table row.

This reference includes:

- [Country-level zones](#country-level-zones) for all supported countries and territories.
- More specific zones for [Australia](#australia), [Brazil](#brazil), [Mexico](#mexico), and the [United States](#united-states).

> ℹ️ If you need more granular zones for another country, open a ticket with [VTEX Support](https://support.vtex.com/hc/en-us/requests) and ask the product team to evaluate your request.

## Country-level zones

| **Zone ID** | **Zone name** | **Country code** | **Postal code range** |
| :--- | :--- | :--- | :--- |
| `ABW_COUNTRY` | Heel het land | ABW | 00000–99999 |
| `AFG_COUNTRY` | تمام کشور | AFG | 1001–9999 |
| `AGO_COUNTRY` | Todo o país | AGO | 00000–99999 |
| `AIA_COUNTRY` | Entire country | AIA | 00000–99999 |
| `ALB_COUNTRY` | E gjithë vendi | ALB | 1001–9999 |
| `AND_COUNTRY` | Tot el país | AND | AD100–AD700 |
| `ARE_COUNTRY` | الدولة بأكملها | ARE | 00000–99999 |
| `ARG_COUNTRY` | Todo el país | ARG | 1000–9999 |
| `ARM_COUNTRY` | Ամբողջ երկիրը | ARM | 0001–4299 |
| `ASM_COUNTRY` | Entire country | ASM | 96799–96799 |
| `ATG_COUNTRY` | Entire country | ATG | 00000–99999 |
| `AUS_COUNTRY` | Entire country | AUS | 0200–9999 |
| `AUT_COUNTRY` | Gesamtes Land | AUT | 1000–9999 |
| `AZE_COUNTRY` | Bütün ölkə | AZE | 0000–9999 |
| `BDI_COUNTRY` | Tout le pays | BDI | 00000–99999 |
| `BEL_COUNTRY` | Het hele land | BEL | 1000–9992 |
| `BEN_COUNTRY` | Tout le pays | BEN | 00000–99999 |
| `BES_COUNTRY` | Entire country | BES | 00000–99999 |
| `BFA_COUNTRY` | Tout le pays | BFA | 00000–99999 |
| `BGD_COUNTRY` | সমগ্র দেশ | BGD | 1000–9499 |
| `BGR_COUNTRY` | Цялата страна | BGR | 1000–9999 |
| `BHR_COUNTRY` | جميع أنحاء البلاد | BHR | 00000–1216 |
| `BHS_COUNTRY` | Entire country | BHS | 00000–99999 |
| `BIH_COUNTRY` | Cijela zemlja | BIH | 71000–89000 |
| `BLM_COUNTRY` | Tout le pays | BLM | 97133–97133 |
| `BLR_COUNTRY` | Уся краіна | BLR | 210000–247000 |
| `BLZ_COUNTRY` | Entire country | BLZ | 00000–99999 |
| `BMU_COUNTRY` | Entire country | BMU | CR01–PG06 |
| `BOL_COUNTRY` | Todo el país | BOL | 00000–99999 |
| `BRA_COUNTRY` | Todo o país | BRA | 01000000–99999999 |
| `BRB_COUNTRY` | Entire country | BRB | BB11000–BB15000 |
| `BRN_COUNTRY` | Seluruh negara | BRN | BA1111–BE3921 |
| `BTN_COUNTRY` | Entire country | BTN | 00000–99999 |
| `BWA_COUNTRY` | Entire country | BWA | 00000–99999 |
| `CAF_COUNTRY` | Tout le pays | CAF | 00000–99999 |
| `CAN_COUNTRY` | Entire country | CAN | A0A0A0–Y9Z9Z9 |
| `CCK_COUNTRY` | Entire country | CCK | 6799–6799 |
| `CHE_COUNTRY` | Gesamtes Land | CHE | 1000–9999 |
| `CHL_COUNTRY` | Todo el país | CHL | 1000000–9999999 |
| `CHN_COUNTRY` | 全国 | CHN | 100000–999999 |
| `CIV_COUNTRY` | Tout le pays | CIV | 00000–99999 |
| `CMR_COUNTRY` | Tout le pays | CMR | 00000–99999 |
| `COD_COUNTRY` | Tout le pays | COD | 00000–99999 |
| `COG_COUNTRY` | Tout le pays | COG | 00000–99999 |
| `COK_COUNTRY` | Entire country | COK | 00000–99999 |
| `COL_COUNTRY` | Todo el país | COL | 00000000–99999999 |
| `COM_COUNTRY` | Tout le pays | COM | 00000–99999 |
| `CPV_COUNTRY` | Todo o país | CPV | 1000–9999 |
| `CRI_COUNTRY` | Todo el país | CRI | 10101–70903 |
| `CUB_COUNTRY` | Todo el país | CUB | 10000–99999 |
| `CUW_COUNTRY` | Heel het eiland | CUW | 00000–99999 |
| `CXR_COUNTRY` | Entire country | CXR | 6798–6798 |
| `CYM_COUNTRY` | Entire country | CYM | KY1-1100–KY3-1301 |
| `CYP_COUNTRY` | Ολόκληρη η χώρα | CYP | 1000–8799 |
| `CZE_COUNTRY` | Celá země | CZE | 10000–79999 |
| `DEU_COUNTRY` | Gesamtes Land | DEU | 1067–99998 |
| `DJI_COUNTRY` | Tout le pays | DJI | 00000–99999 |
| `DMA_COUNTRY` | Entire country | DMA | 00000–99999 |
| `DNK_COUNTRY` | Hele landet | DNK | 0800–9990 |
| `DOM_COUNTRY` | Todo el país | DOM | 10001–59000 |
| `DZA_COUNTRY` | كل البلاد | DZA | 01000–59000 |
| `ECU_COUNTRY` | Todo el país | ECU | 010101–999999 |
| `EGY_COUNTRY` | جميع أنحاء البلاد | EGY | 11511–99999 |
| `ERI_COUNTRY` | Entire country | ERI | 00000–99999 |
| `ESH_COUNTRY` | كل البلاد | ESH | 00000–99999 |
| `ESP_COUNTRY` | Todo el país | ESP | 01001–52080 |
| `EST_COUNTRY` | Kogu riik | EST | 10111–99999 |
| `ETH_COUNTRY` | ሙሉ ሃገር | ETH | 1000–9999 |
| `FIN_COUNTRY` | Koko maa | FIN | 00001–99999 |
| `FJI_COUNTRY` | Entire country | FJI | 00000–99999 |
| `FLK_COUNTRY` | Entire country | FLK | FIQQ1ZZ–FIQQ1ZZ |
| `FRA_COUNTRY` | Tout le pays | FRA | 01000–98890 |
| `FRO_COUNTRY` | Alt landið | FRO | 100–999 |
| `FSM_COUNTRY` | Entire country | FSM | 96941–96944 |
| `GAB_COUNTRY` | Tout le pays | GAB | 00000–99999 |
| `GBR_COUNTRY` | Entire country | GBR | 00000000–ZZZZZZZZ |
| `GEO_COUNTRY` | მთელი ქვეყანა | GEO | 0001–9999 |
| `GGY_COUNTRY` | Entire country | GGY | GY11AA–GY99ZZ |
| `GHA_COUNTRY` | Entire country | GHA | 00000–99999 |
| `GIB_COUNTRY` | Entire country | GIB | GX111AA–GX111AA |
| `GIN_COUNTRY` | Tout le pays | GIN | 00000–99999 |
| `GLP_COUNTRY` | Tout le pays | GLP | 97100–97190 |
| `GMB_COUNTRY` | Entire country | GMB | 00000–99999 |
| `GNB_COUNTRY` | Todo o país | GNB | 00000–99999 |
| `GNQ_COUNTRY` | Todo el país | GNQ | 00000–99999 |
| `GRC_COUNTRY` | Ολόκληρη η χώρα | GRC | 10000–85700 |
| `GRD_COUNTRY` | Entire country | GRD | 00000–99999 |
| `GRL_COUNTRY` | Hele landet | GRL | 3900–3999 |
| `GTM_COUNTRY` | Todo el país | GTM | 00000000–ZZZZZZZZ |
| `GUF_COUNTRY` | Tout le pays | GUF | 97300–97390 |
| `GUM_COUNTRY` | Entire country | GUM | 96910–96932 |
| `GUY_COUNTRY` | Entire country | GUY | 00000–99999 |
| `HKG_COUNTRY` | 全境 | HKG | 00000–99999 |
| `HND_COUNTRY` | Todo el país | HND | 01101–99999 |
| `HRV_COUNTRY` | Cijela zemlja | HRV | 10000–53999 |
| `HTI_COUNTRY` | Tout le pays | HTI | 01–99 |
| `HUN_COUNTRY` | Az egész ország | HUN | 1000–9999 |
| `IDN_COUNTRY` | Seluruh negara | IDN | 10000–99999 |
| `IMN_COUNTRY` | Entire country | IMN | IM11AA–IM99ZZ |
| `IND_COUNTRY` | पूरा देश | IND | 100000–999999 |
| `IRL_COUNTRY` | An tír ar fad | IRL | A000000–Y999Y99 |
| `IRN_COUNTRY` | کل کشور | IRN | 1111111111–9999999999 |
| `IRQ_COUNTRY` | جميع أنحاء البلاد | IRQ | 10000–72055 |
| `ISL_COUNTRY` | Allt landið | ISL | 101–999 |
| `ISR_COUNTRY` | כל הארץ | ISR | 0100000–9999999 |
| `ITA_COUNTRY` | Tutto il paese | ITA | 118–99049 |
| `JAM_COUNTRY` | Entire country | JAM | 00000000–ZZZZZZZZ |
| `JEY_COUNTRY` | Entire country | JEY | JE10AA–JE49ZZ |
| `JOR_COUNTRY` | جميع أنحاء البلاد | JOR | 11110–77770 |
| `JPN_COUNTRY` | 全国 | JPN | 0000001–9999999 |
| `KAZ_COUNTRY` | Бүкіл ел | KAZ | 010000–999999 |
| `KEN_COUNTRY` | Nchi nzima | KEN | 00100–80116 |
| `KGZ_COUNTRY` | Бүт өлкө | KGZ | 720000–999000 |
| `KHM_COUNTRY` | ទូទាំងប្រទេស | KHM | 00001–25000 |
| `KIR_COUNTRY` | Entire country | KIR | 00000–99999 |
| `KNA_COUNTRY` | Entire country | KNA | 00000–99999 |
| `KOR_COUNTRY` | 전국 | KOR | 01000–63999 |
| `KWT_COUNTRY` | جميع أنحاء البلاد | KWT | 00000–99999 |
| `LAO_COUNTRY` | ທົ່ວປະເທດ | LAO | 01000–99000 |
| `LBN_COUNTRY` | جميع أنحاء البلاد | LBN | 10010000–99999999 |
| `LBR_COUNTRY` | Entire country | LBR | 00000–99999 |
| `LBY_COUNTRY` | جميع أنحاء البلاد | LBY | 01000–99999 |
| `LCA_COUNTRY` | Entire country | LCA | 00000–99999 |
| `LIE_COUNTRY` | Gesamtes Land | LIE | 9485–9498 |
| `LKA_COUNTRY` | සමස්ත රට | LKA | 00100–99950 |
| `LSO_COUNTRY` | Naha yohle | LSO | 100–999 |
| `LTU_COUNTRY` | Visa šalis | LTU | 1001–99069 |
| `LUX_COUNTRY` | Dat ganzt Land | LUX | 1000–9999 |
| `LVA_COUNTRY` | Visa valsts | LVA | 00001001–5555 |
| `MAC_COUNTRY` | 全境 | MAC | 00000–99999 |
| `MAF_COUNTRY` | Tout le pays | MAF | 97150–97150 |
| `MAR_COUNTRY` | جميع أنحاء البلاد | MAR | 10000–93000 |
| `MCO_COUNTRY` | Tout le pays | MCO | 98000–98099 |
| `MDA_COUNTRY` | Toată țara | MDA | 0001–9999 |
| `MDG_COUNTRY` | Ny firenena manontolo | MDG | 101–699 |
| `MDV_COUNTRY` | Entire country | MDV | 00000–99999 |
| `MEX_COUNTRY` | Todo el país | MEX | 01000–99998 |
| `MHL_COUNTRY` | Entire country | MHL | 96960–96970 |
| `MKD_COUNTRY` | Цела земја | MKD | 1000–9999 |
| `MLI_COUNTRY` | Tout le pays | MLI | 00000–99999 |
| `MLT_COUNTRY` | Il-pajjiż kollu | MLT | 00000000–ZZZZZZZZ |
| `MMR_COUNTRY` | တစ်နိုင်ငံလုံး | MMR | 01001–99999 |
| `MNE_COUNTRY` | Cijela zemlja | MNE | 81000–85000 |
| `MNG_COUNTRY` | Бүх улс | MNG | 000000–999999 |
| `MNP_COUNTRY` | Entire country | MNP | 96950–96950 |
| `MOZ_COUNTRY` | Todo o país | MOZ | 1000–9999 |
| `MRT_COUNTRY` | جميع أنحاء البلاد | MRT | 00000–99999 |
| `MSR_COUNTRY` | Entire country | MSR | MSR1110–MSR1350 |
| `MTQ_COUNTRY` | Tout le pays | MTQ | 97200–97290 |
| `MUS_COUNTRY` | Entire country | MUS | 00000–99999 |
| `MWI_COUNTRY` | Dziko lonse | MWI | 00000–99999 |
| `MYS_COUNTRY` | Seluruh negara | MYS | 01000–98009 |
| `MYT_COUNTRY` | Tout le pays | MYT | 97600–97680 |
| `NAM_COUNTRY` | Entire country | NAM | 00000–99999 |
| `NCL_COUNTRY` | Tout le pays | NCL | 98800–98890 |
| `NER_COUNTRY` | Tout le pays | NER | 00000–99999 |
| `NFK_COUNTRY` | Entire country | NFK | 2899–2899 |
| `NGA_COUNTRY` | Entire country | NGA | 100001–999999 |
| `NIC_COUNTRY` | Todo el país | NIC | 00000–99999 |
| `NIU_COUNTRY` | Entire country | NIU | 00000–99999 |
| `NLD_COUNTRY` | Het hele land | NLD | 00000000–ZZZZZZZZ |
| `NOR_COUNTRY` | Hele landet | NOR | 1–9991 |
| `NPL_COUNTRY` | सम्पूर्ण देश | NPL | 01001–97032 |
| `NRU_COUNTRY` | Entire country | NRU | 00000–99999 |
| `NZL_COUNTRY` | Entire country | NZL | 0110–9893 |
| `OMN_COUNTRY` | جميع أنحاء البلاد | OMN | 100–853 |
| `PAK_COUNTRY` | پورا ملک | PAK | 10000–97000 |
| `PAN_COUNTRY` | Todo el país | PAN | 01000–8999 |
| `PER_COUNTRY` | Todo el país | PER | 01000–25999 |
| `PHL_COUNTRY` | Buong bansa | PHL | 0000–9999 |
| `PLW_COUNTRY` | Entire country | PLW | 96940–96940 |
| `PNG_COUNTRY` | Entire country | PNG | 100–675 |
| `POL_COUNTRY` | Cały kraj | POL | 00001–99999 |
| `PRI_COUNTRY` | Todo el país | PRI | 00600–988 |
| `PRY_COUNTRY` | Todo el país | PRY | 0000–9999 |
| `PSE_COUNTRY` | جميع أنحاء البلاد | PSE | 00000–99999 |
| `PRT_COUNTRY` | Todo o país | PRT | 1000000–9999999 |
| `PYF_COUNTRY` | Tout le pays | PYF | 98700–98798 |
| `QAT_COUNTRY` | جميع أنحاء البلاد | QAT | 00000–99999 |
| `REU_COUNTRY` | Tout le pays | REU | 97400–97490 |
| `ROU_COUNTRY` | Toată țara | ROU | 010000–999999 |
| `RUS_COUNTRY` | Вся страна | RUS | 100000–999999 |
| `RWA_COUNTRY` | Igihugu cyose | RWA | 00000–99999 |
| `SAU_COUNTRY` | جميع أنحاء البلاد | SAU | 11000–96500 |
| `SDN_COUNTRY` | جميع أنحاء البلاد | SDN | 11000–99999 |
| `SEN_COUNTRY` | Tout le pays | SEN | 10000–99999 |
| `SGP_COUNTRY` | Entire country | SGP | 018900–828938 |
| `SHN_COUNTRY` | Entire country | SHN | ASCN1ZZ–TDCU1ZZ |
| `SJM_COUNTRY` | Hele landet | SJM | 8099–9171 |
| `SLB_COUNTRY` | Entire country | SLB | 00000–99999 |
| `SLE_COUNTRY` | Entire country | SLE | 00000–99999 |
| `SLV_COUNTRY` | Todo el país | SLV | 01001–1101 |
| `SMR_COUNTRY` | Tutto il paese | SMR | 47890–47899 |
| `SOM_COUNTRY` | Waddanka oo dhan | SOM | 00000–99999 |
| `SPM_COUNTRY` | Tout le pays | SPM | 97500–97500 |
| `SRB_COUNTRY` | Цела земља | SRB | 10000–39999 |
| `SSD_COUNTRY` | Entire country | SSD | 00000–99999 |
| `STP_COUNTRY` | Todo o país | STP | 00000–99999 |
| `SUR_COUNTRY` | Heel het land | SUR | 00000–99999 |
| `SVK_COUNTRY` | Celá krajina | SVK | 01001–99999 |
| `SVN_COUNTRY` | Celotna država | SVN | 1000–9999 |
| `SWE_COUNTRY` | Hela landet | SWE | 10005–98499 |
| `SWZ_COUNTRY` | Lonkhe live | SWZ | H100–S399 |
| `SXM_COUNTRY` | Heel het eiland | SXM | 00000–99999 |
| `SYC_COUNTRY` | Entire country | SYC | 00000–99999 |
| `SYR_COUNTRY` | جميع أنحاء البلاد | SYR | 00000–99999 |
| `TCA_COUNTRY` | Entire country | TCA | TKCA1ZZ–TKCA1ZZ |
| `TCD_COUNTRY` | Tout le pays | TCD | 00000–99999 |
| `TGO_COUNTRY` | Tout le pays | TGO | 00000–99999 |
| `THA_COUNTRY` | ทั่วประเทศ | THA | 10000–99999 |
| `TJK_COUNTRY` | Тамоми кишвар | TJK | 700000–799000 |
| `TKM_COUNTRY` | Tutuş ýurt | TKM | 740000–745000 |
| `TLS_COUNTRY` | Todo o país | TLS | 00000–99999 |
| `TON_COUNTRY` | Fonua kotoa | TON | 00000–99999 |
| `TTO_COUNTRY` | Entire country | TTO | 00000–99999 |
| `TUN_COUNTRY` | جميع أنحاء البلاد | TUN | 1000–9160 |
| `TUR_COUNTRY` | Tüm ülke | TUR | 01000–81999 |
| `TUV_COUNTRY` | Entire country | TUV | 00000–99999 |
| `TWN_COUNTRY` | 全國 | TWN | 10000–99999 |
| `TZA_COUNTRY` | Nchi nzima | TZA | 00000–99999 |
| `UGA_COUNTRY` | Entire country | UGA | 00000–99999 |
| `UKR_COUNTRY` | Вся країна | UKR | 01000–99999 |
| `UMI_COUNTRY` | Entire country | UMI | 00000–99999 |
| `URY_COUNTRY` | Todo el país | URY | 11000–97000 |
| `USA_COUNTRY` | Entire country | USA | 00501–99950 |
| `UZB_COUNTRY` | Butun mamlakat | UZB | 100000–999000 |
| `VAT_COUNTRY` | Tutto il paese | VAT | 00120–120 |
| `VCT_COUNTRY` | Entire country | VCT | VC0100–VC0490 |
| `VEN_COUNTRY` | Todo el país | VEN | 1000–9999 |
| `VGB_COUNTRY` | Entire country | VGB | VG1100–VG1160 |
| `VIR_COUNTRY` | Entire country | VIR | 00801–851 |
| `VNM_COUNTRY` | Toàn quốc | VNM | 100000–999999 |
| `VUT_COUNTRY` | Entire country | VUT | 00000–99999 |
| `WLF_COUNTRY` | Tout le pays | WLF | 98600–98600 |
| `WSM_COUNTRY` | Atunu'u uma | WSM | 00000–99999 |
| `XKX_COUNTRY` | E gjithë vendi | XKX | 10000–60000 |
| `YEM_COUNTRY` | جميع أنحاء البلاد | YEM | 00000–99999 |
| `ZAF_COUNTRY` | Entire country | ZAF | 0001–9992 |
| `ZMB_COUNTRY` | Entire country | ZMB | 10001–70001 |
| `ZWE_COUNTRY` | Entire country | ZWE | 00000–99999 |

## Australia

| **Zone ID** | **Zone name** | **Postal code range** |
| :--- | :--- | :--- |
| `AUS_DIVISION_MAINLAND` | Mainland | 200–9999 |
| `AUS_STATE_NSW` | New South Wales | 2000–2599<br>2619–2899<br>2921–2999 |
| `AUS_STATE_VIC` | Victoria | 3000–3999<br>8000–8999 |
| `AUS_STATE_QLD` | Queensland | 4000–4999<br>9000–9999 |
| `AUS_STATE_SA` | South Australia | 5000–5799<br>5800–5999 |
| `AUS_STATE_WA` | Western Australia | 6000–6797<br>6800–6999 |
| `AUS_STATE_TAS` | Tasmania | 7000–7799<br>7800–7999 |
| `AUS_TERRITORY_ACT` | Australian Capital Territory | 200–299<br>2600–2618<br>2900–2920 |
| `AUS_TERRITORY_NT` | Northern Territory | 800–899<br>900–999 |
| `AUS_DIVISION_EXTERNAL_TERRITORIES` | External Territories | 2899–7151 |
| `AUS_TERRITORY_NORFOLK_ISLAND` | Norfolk Island | 2899–2899 |
| `AUS_TERRITORY_CHRISTMAS_ISLAND` | Christmas Island | 6798–6798 |
| `AUS_TERRITORY_COCOS_KEELING_ISLANDS` | Cocos (Keeling) Islands | 6799–6799 |
| `AUS_TERRITORY_HEARD_MACDONALD_ISLANDS` | Heard & McDonald Islands | 7151–7151 |

## Brazil

| **Zone ID** | **Zone name** | **Postal code range** |
| :--- | :--- | :--- |
| `BRA_REGION_SUDESTE` | Sudeste | 01000-000–39999-999 |
| `BRA_STATE_SP` | São Paulo — Estado | 01000-000–19999-999 |
| `BRA_SUBSTATE_SP_CAPITAL` | São Paulo — Capital | 01000-000–05999-999<br>08000-000–08499-999 |
| `BRA_SUBSTATE_SP_REG_METROPOLITANA` | São Paulo — Região Metropolitana | 01000-000–09999-999 |
| `BRA_SUBSTATE_SP_LITORAL` | São Paulo — Litoral | 11000-000–11999-999 |
| `BRA_SUBSTATE_SP_INTERIOR` | São Paulo — Interior | 12000-000–19999-999 |
| `BRA_STATE_RJ` | Rio de Janeiro — Estado | 20000-000–28999-999 |
| `BRA_SUBSTATE_RJ_CAPITAL` | Rio de Janeiro — Capital | 20000-000–23799-999 |
| `BRA_SUBSTATE_RJ_REG_METROPOLITANA` | Rio de Janeiro — Região Metropolitana | 20000-000–26599-999 |
| `BRA_SUBSTATE_RJ_INTERIOR` | Rio de Janeiro — Interior | 26601-000–28999-999 |
| `BRA_STATE_ES` | Espírito Santo — Estado | 29000-000–29999-999 |
| `BRA_SUBSTATE_ES_CAPITAL` | Espírito Santo — Capital | 29000-000–29099-999 |
| `BRA_SUBSTATE_ES_INTERIOR` | Espírito Santo — Interior | 29100-000–29999-999 |
| `BRA_STATE_MG` | Minas Gerais — Estado | 30000-000–39999-999 |
| `BRA_SUBSTATE_MG_CAPITAL` | Minas Gerais — Capital | 30000-000–31999-999 |
| `BRA_SUBSTATE_MG_REG_METROPOLITANA` | Minas Gerais — Região Metropolitana | 30000-000–34999-999 |
| `BRA_SUBSTATE_MG_INTERIOR` | Minas Gerais — Interior | 35000-000–39999-999 |
| `BRA_REGION_NORDESTE` | Nordeste | 40000-000–65999-999 |
| `BRA_STATE_BA` | Bahia — Estado | 40000-000–48999-999 |
| `BRA_SUBSTATE_BA_CAPITAL` | Bahia — Capital | 40000-000–41999-999 |
| `BRA_SUBSTATE_BA_REG_METROPOLITANA` | Bahia — Região Metropolitana | 40000-000–44470-999 |
| `BRA_SUBSTATE_BA_INTERIOR` | Bahia — Interior | 44471-000–48999-999 |
| `BRA_STATE_SE` | Sergipe — Estado | 49000-000–49999-999 |
| `BRA_SUBSTATE_SE_CAPITAL` | Sergipe — Capital | 49000-000–49099-999 |
| `BRA_SUBSTATE_SE_INTERIOR` | Sergipe — Interior | 49100-000–49999-999 |
| `BRA_STATE_PE` | Pernambuco — Estado | 50000-000–56999-999 |
| `BRA_SUBSTATE_PE_CAPITAL` | Pernambuco — Capital | 50000-000–52999-999 |
| `BRA_SUBSTATE_PE_REG_METROPOLITANA` | Pernambuco — Região Metropolitana | 50000-000–54999-999 |
| `BRA_SUBSTATE_PE_INTERIOR` | Pernambuco — Interior | 55000-000–56999-999 |
| `BRA_STATE_AL` | Alagoas — Estado | 57000-000–57999-999 |
| `BRA_SUBSTATE_AL_CAPITAL` | Alagoas — Capital | 57000-000–57099-999 |
| `BRA_SUBSTATE_AL_INTERIOR` | Alagoas — Interior | 57100-000–57999-999 |
| `BRA_STATE_PB` | Paraíba — Estado | 58000-000–58999-999 |
| `BRA_SUBSTATE_PB_CAPITAL` | Paraíba — Capital | 58000-000–58099-999 |
| `BRA_SUBSTATE_PB_INTERIOR` | Paraíba — Interior | 58100-000–58999-999 |
| `BRA_STATE_RN` | Rio Grande do Norte — Estado | 59000-000–59999-999 |
| `BRA_SUBSTATE_RN_CAPITAL` | Rio Grande do Norte — Capital | 59000-000–59099-999 |
| `BRA_SUBSTATE_RN_INTERIOR` | Rio Grande do Norte — Interior | 59100-000–59999-999 |
| `BRA_STATE_CE` | Ceará — Estado | 60000-000–63999-999 |
| `BRA_SUBSTATE_CE_CAPITAL` | Ceará — Capital | 60000-000–60999-999 |
| `BRA_SUBSTATE_CE_REG_METROPOLITANA` | Ceará — Região Metropolitana | 60000-000–61909-999 |
| `BRA_SUBSTATE_CE_INTERIOR` | Ceará — Interior | 61910-000–63999-999 |
| `BRA_STATE_PI` | Piauí — Estado | 64000-000–64999-999 |
| `BRA_SUBSTATE_PI_CAPITAL` | Piauí — Capital | 64000-000–64099-999 |
| `BRA_SUBSTATE_PI_INTERIOR` | Piauí — Interior | 64100-000–64999-999 |
| `BRA_STATE_MA` | Maranhão — Estado | 65000-000–65999-999 |
| `BRA_SUBSTATE_MA_CAPITAL` | Maranhão — Capital | 65000-000–65099-999 |
| `BRA_SUBSTATE_MA_INTERIOR` | Maranhão — Interior | 65100-000–65999-999 |
| `BRA_REGION_NORTE` | Norte | 66000-000–69999-999<br>76800-000–77999-999 |
| `BRA_STATE_PA` | Pará — Estado | 66000-000–68899-999 |
| `BRA_SUBSTATE_PA_CAPITAL` | Pará — Capital | 66000-000–66999-999 |
| `BRA_SUBSTATE_PA_REG_METROPOLITANA` | Pará — Região Metropolitana | 66000-000–67999-999 |
| `BRA_SUBSTATE_PA_INTERIOR` | Pará — Interior | 68000-000–68899-999 |
| `BRA_STATE_AP` | Amapá — Estado | 68900-000–68999-999 |
| `BRA_SUBSTATE_AP_CAPITAL` | Amapá — Capital | 68900-000–68914-999 |
| `BRA_SUBSTATE_AP_INTERIOR` | Amapá — Interior | 68915-000–68999-999 |
| `BRA_STATE_AM` | Amazonas — Estado | 69000-000–69299-999 |
| `BRA_SUBSTATE_AM_CAPITAL` | Amazonas — Capital | 69000-000–69099-999 |
| `BRA_SUBSTATE_AM_INTERIOR` | Amazonas — Interior | 69100-000–69299-999 |
| `BRA_STATE_RR` | Roraima — Estado | 69300-000–69389-999 |
| `BRA_SUBSTATE_RR_CAPITAL` | Roraima — Capital | 69300-000–69300-999 |
| `BRA_SUBSTATE_RR_INTERIOR` | Roraima — Interior | 69340-000–69389-999 |
| `BRA_STATE_AC` | Acre — Estado | 69900-000–69999-999 |
| `BRA_SUBSTATE_AC_CAPITAL` | Acre — Capital | 69900-000–69920-999 |
| `BRA_SUBSTATE_AC_INTERIOR` | Acre — Interior | 69921-000–69999-999 |
| `BRA_REGION_CENTRO_OESTE` | Centro-Oeste | 70000-000–76799-999<br>78000-000–79999-999 |
| `BRA_STATE_DF` | Distrito Federal — Estado | 70000-000–72799-999<br>73000-000–73699-999 |
| `BRA_SUBSTATE_DF_CAPITAL` | Distrito Federal — Brasília | 70000-000–70999-999 |
| `BRA_SUBSTATE_DF_INTERIOR` | Distrito Federal — Cidades Satélite | 71000-000–72799-999<br>73000-000–73699-999 |
| `BRA_STATE_GO` | Goiás — Estado | 72800-000–72999-999<br>73700-000–76799-999 |
| `BRA_SUBSTATE_GO_CAPITAL` | Goiás — Capital | 72800-000–72999-999<br>73700-000–74894-999 |
| `BRA_SUBSTATE_GO_INTERIOR` | Goiás — Interior | 74895-000–76799-999 |
| `BRA_STATE_RO` | Rondônia — Estado | 76800-000–76999-999 |
| `BRA_SUBSTATE_RO_CAPITAL` | Rondônia — Capital | 76800-000–76834-999 |
| `BRA_SUBSTATE_RO_INTERIOR` | Rondônia — Interior | 76835-000–76999-999 |
| `BRA_STATE_TO` | Tocantins — Estado | 77000-000–77995-999 |
| `BRA_SUBSTATE_TO_CAPITAL` | Tocantins — Capital | 77000-000–77270-999 |
| `BRA_SUBSTATE_TO_INTERIOR` | Tocantins — Interior | 77300-000–77995-999 |
| `BRA_STATE_MT` | Mato Grosso — Estado | 78000-000–78899-999 |
| `BRA_SUBSTATE_MT_CAPITAL` | Mato Grosso — Capital | 78000-000–78109-999 |
| `BRA_SUBSTATE_MT_INTERIOR` | Mato Grosso — Interior | 78110-000–78899-999 |
| `BRA_STATE_MS` | Mato Grosso do Sul — Estado | 79000-000–79999-999 |
| `BRA_SUBSTATE_MS_CAPITAL` | Mato Grosso do Sul — Capital | 79000-000–79129-999 |
| `BRA_SUBSTATE_MS_INTERIOR` | Mato Grosso do Sul — Interior | 79130-000–79999-999 |
| `BRA_REGION_SUL` | Sul | 80000-000–99999-999 |
| `BRA_STATE_PR` | Paraná — Estado | 80000-000–87999-999 |
| `BRA_SUBSTATE_PR_CAPITAL` | Paraná — Capital | 80000-000–82999-999 |
| `BRA_SUBSTATE_PR_REG_METROPOLITANA` | Paraná — Região Metropolitana | 80000-000–83800-999 |
| `BRA_SUBSTATE_PR_INTERIOR` | Paraná — Interior | 83801-000–87999-999 |
| `BRA_STATE_SC` | Santa Catarina — Estado | 88000-000–89999-999 |
| `BRA_SUBSTATE_SC_CAPITAL` | Santa Catarina — Capital | 88000-000–88100-999 |
| `BRA_SUBSTATE_SC_REG_METROPOLITANA` | Santa Catarina — Região Metropolitana | 88000-000–88469-999 |
| `BRA_SUBSTATE_SC_INTERIOR` | Santa Catarina — Interior | 88470-000–89999-999 |
| `BRA_STATE_RS` | Rio Grande do Sul — Estado | 90000-000–99999-999 |
| `BRA_SUBSTATE_RS_CAPITAL` | Rio Grande do Sul — Capital | 90000-000–91999-999 |
| `BRA_SUBSTATE_RS_REG_METROPOLITANA` | Rio Grande do Sul — Região Metropolitana | 90000-000–94900-999 |
| `BRA_SUBSTATE_RS_INTERIOR` | Rio Grande do Sul — Interior | 94901-000–99999-999 |

## Mexico

| **Zone ID** | **Zone name** | **Postal code range** |
| :--- | :--- | :--- |
| `MEX_STATE_CDMX` | Ciudad de México | 1000–16900 |
| `MEX_CDMX_ALVARO_OBREGON` | Álvaro Obregón — CDMX | 1000–1904 |
| `MEX_CDMX_AZCAPOTZALCO` | Azcapotzalco — CDMX | 2000–2990 |
| `MEX_CDMX_BENITO_JUAREZ` | Benito Juárez — CDMX | 3000–3940 |
| `MEX_CDMX_COYOACAN` | Coyoacán — CDMX | 4000–4980 |
| `MEX_CDMX_CUAJIMALPA_DE_MORELOS` | Cuajimalpa de Morelos — CDMX | 5000–5790 |
| `MEX_CDMX_CUAUHTEMOC` | Cuauhtémoc — CDMX | 6000–6920 |
| `MEX_CDMX_GUSTAVO_A_MADERO` | Gustavo A. Madero — CDMX | 7000–7990 |
| `MEX_CDMX_IZTACALCO` | Iztacalco — CDMX | 8000–8930 |
| `MEX_CDMX_IZTAPALAPA` | Iztapalapa — CDMX | 9000–9970 |
| `MEX_CDMX_LA_MAGDALENA_CONTRERAS` | La Magdalena Contreras — CDMX | 10800–10926 |
| `MEX_CDMX_MIGUEL_HIDALGO` | Miguel Hidalgo — CDMX | 11000–11950 |
| `MEX_CDMX_MILPA_ALTA` | Milpa Alta — CDMX | 12000–12950 |
| `MEX_CDMX_TLAHUAC` | Tláhuac — CDMX | 13000–13700 |
| `MEX_CDMX_TLALPAN` | Tlalpan — CDMX | 14000–14900 |
| `MEX_CDMX_VENUSTIANO_CARRANZA` | Venustiano Carranza — CDMX | 15000–15990 |
| `MEX_CDMX_XOCHIMILCO` | Xochimilco — CDMX | 16000–16900 |
| `MEX_STATE_AGUASCALIENTES` | Aguascalientes | 20000–20997 |
| `MEX_STATE_BAJA` | Baja California | 21000–22997 |
| `MEX_STATE_BAJA_SUR` | Baja California Sur | 23000–23997 |
| `MEX_STATE_CAMPECHE` | Campeche | 24000–24940 |
| `MEX_STATE_COAHUILA` | Coahuila de Zaragoza | 25000–27997 |
| `MEX_STATE_COLIMA` | Colima | 28000–28989 |
| `MEX_STATE_CHIAPAS` | Chiapas | 29000–30997 |
| `MEX_STATE_CHIHUAHUA` | Chihuahua | 31000–33997 |
| `MEX_STATE_DURANGO` | Durango | 34000–35987 |
| `MEX_STATE_GUANAJUATO` | Guanajuato | 36000–36210 |
| `MEX_STATE_GUERRERO` | Guerrero | 39000–41998 |
| `MEX_STATE_HIDALGO` | Hidalgo | 42000–43998 |
| `MEX_STATE_JALISCO` | Jalisco | 44100–49996 |
| `MEX_STATE_MEXICO` | México (Edomex) | 50000–57950 |
| `MEX_MEX_TOLUCA` | Toluca — MEX | 50000–50295 |
| `MEX_MEX_HUIXQUILUCAN` | huixquilucan — MEX | 52760–52799 |
| `MEX_MEX_ATIZAPAN DE ZARAGOZA` | Atizapán de zaragoza — MEX | 52900–52998 |
| `MEX_MEX_NAUCALPAN` | Naucalpan — MEX | 53000–53970 |
| `MEX_MEX_TLALNEPANTLA` | Tlalnepantla — MEX | 54000–54198 |
| `MEX_MEX_CUAUTITLAN` | Cuautitlán — MEX | 54700–54879 |
| `MEX_MEX_ECATEPEC` | Ecatepec — MEX | 55000–55549 |
| `MEX_MEX_TEXCOCO` | Texcoco — MEX | 56100–56268 |
| `MEX_MEX_CHIMALHUACAN` | Chimalhuacán — MEX | 56330–56366 |
| `MEX_MEX_IXTAPALUCA` | Ixtapaluca — MEX | 56530–56599 |
| `MEX_MEX_NEZAHUALCOYOTL` | Nezahualcóyotl — MEX | 57000–57950 |
| `MEX_STATE_MICHOACAN` | Michoacán de Ocampo | 58000–61998 |
| `MEX_STATE_MORELOS` | Morelos | 62000–62996 |
| `MEX_STATE_NAYARIT` | Nayarit | 63000–63173 |
| `MEX_STATE_NUEVO` | Nuevo León | 64000–65534 |
| `MEX_STATE_OAXACA` | Oaxaca | 68000–71998 |
| `MEX_STATE_PUEBLA` | Puebla | 72000–72124 |
| `MEX_STATE_QUERETARO` | Querétaro | 76000–76110 |
| `MEX_STATE_QUINTANA` | Quintana Roo | 77000–77250 |
| `MEX_STATE_SAN` | San Luis Potosí | 78000–78143 |
| `MEX_STATE_SINALOA` | Sinaloa | 80000–82996 |
| `MEX_STATE_SONORA` | Sonora | 83000–85994 |
| `MEX_STATE_TABASCO` | Tabasco | 86000–86998 |
| `MEX_STATE_TAMAULIPAS` | Tamaulipas | 87000–87049 |
| `MEX_STATE_TLAXCALA` | Tlaxcala | 90000–90180 |
| `MEX_STATE_VERACRUZ` | Veracruz de Ignacio de la Llave | 91000–96998 |
| `MEX_STATE_YUCATAN` | Yucatán | 97000–97990 |
| `MEX_STATE_ZACATECAS` | Zacatecas | 98000–99998 |

## United States

| **Zone ID** | **Zone name** | **Postal code range** |
| :--- | :--- | :--- |
| `USA_DIVISION_NEW_ENGLAND` | New England | 01001–05907 |
| `USA_DIVISION_MIDDLE_ATLANTIC` | Middle Atlantic | 07001–19640 |
| `USA_DIVISION_EAST_NORTH_CENTRAL` | East North Central | 43001–62999 |
| `USA_DIVISION_WEST_NORTH_CENTRAL` | West North Central | 50001–69367 |
| `USA_DIVISION_SOUTH_ATLANTIC` | South Atlantic | 19701–34997 |
| `USA_DIVISION_EAST_SOUTH_CENTRAL` | East South Central | 35004–42788 |
| `USA_DIVISION_WEST_SOUTH_CENTRAL` | West South Central | 70001–88589 |
| `USA_DIVISION_MOUNTAIN` | Mountain | 59001–89883 |
| `USA_DIVISION_PACIFIC` | Pacific | 90001–99950 |
| `USA_STATE_ME` | Maine | 03901–04992 |
| `USA_STATE_NH` | New Hampshire | 03031–03897 |
| `USA_STATE_VT` | Vermont | 05001–05499<br>05545–05907 |
| `USA_STATE_MA` | Massachusetts | 01001–02791<br>05501–05544 |
| `USA_STATE_RI` | Rhode Island | 02801–02940 |
| `USA_STATE_CT` | Connecticut | 06001–06389<br>06401–06928 |
| `USA_STATE_NY` | New York | 10001–14975 |
| `USA_STATE_NJ` | New Jersey | 07001–08989 |
| `USA_STATE_PA` | Pennsylvania | 15001–19640 |
| `USA_STATE_OH` | Ohio | 43001–45999 |
| `USA_STATE_IN` | Indiana | 46001–47997 |
| `USA_STATE_IL` | Illinois | 60001–62999 |
| `USA_STATE_MI` | Michigan | 48001–49971 |
| `USA_STATE_WI` | Wisconsin | 53001–54990 |
| `USA_STATE_MN` | Minnesota | 55001–56763 |
| `USA_STATE_IA` | Iowa | 50001–52809 |
| `USA_STATE_MO` | Missouri | 63001–65899 |
| `USA_STATE_ND` | North Dakota | 58001–58856 |
| `USA_STATE_SD` | South Dakota | 57001–57799 |
| `USA_STATE_NE` | Nebraska | 68001–68118<br>68122–69367 |
| `USA_STATE_KS` | Kansas | 66002–67954 |
| `USA_STATE_DE` | Delaware | 19701–19980 |
| `USA_STATE_MD` | Maryland | 20601–20734<br>20759–20797<br>20812–21930 |
| `USA_STATE_DC` | District of Columbia | 20001–20039<br>20042–20599<br>20799–20799 |
| `USA_STATE_VA` | Virginia | 20040–20041<br>22001–24658 |
| `USA_STATE_WV` | West Virginia | 24701–26886 |
| `USA_STATE_NC` | North Carolina | 27006–28909 |
| `USA_STATE_SC` | South Carolina | 29001–29948 |
| `USA_STATE_GA` | Georgia | 30001–31999 |
| `USA_STATE_FL` | Florida | 32004–34997 |
| `USA_STATE_KY` | Kentucky | 40003–42788 |
| `USA_STATE_TN` | Tennessee | 37010–38589 |
| `USA_STATE_AL` | Alabama | 35004–36925 |
| `USA_STATE_MS` | Mississippi | 38601–39776 |
| `USA_STATE_AR` | Arkansas | 71601–72959 |
| `USA_STATE_LA` | Louisiana | 70001–71497 |
| `USA_STATE_OK` | Oklahoma | 73001–73300<br>73302–74966 |
| `USA_STATE_TX` | Texas | 73301–73301<br>75001–75501<br>75503–79999<br>88510–88589 |
| `USA_STATE_MT` | Montana | 59001–59937 |
| `USA_STATE_ID` | Idaho | 83201–83876 |
| `USA_STATE_WY` | Wyoming | 82001–83120 |
| `USA_STATE_CO` | Colorado | 80001–81658 |
| `USA_STATE_NM` | New Mexico | 87001–88441 |
| `USA_STATE_AZ` | Arizona | 85001–86556 |
| `USA_STATE_UT` | Utah | 84001–84784 |
| `USA_STATE_NV` | Nevada | 88901–89883 |
| `USA_STATE_WA` | Washington | 98001–99403 |
| `USA_STATE_OR` | Oregon | 97001–97920 |
| `USA_STATE_CA` | California | 90001–96162 |
| `USA_STATE_AK` | Alaska | 99501–99950 |
| `USA_STATE_HI` | Hawaii | 96701–96898 |
