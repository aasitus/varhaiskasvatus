# %%

import pandas as pd
import geopandas as gpd
import numpy as np
import requests
import json
import io
import os

# Setup data: get daycare data and GeoJSON data, merge them and save as a GeoJSON file
# in the 'data' directory.

def run():

    # Download data from Statistics Finland's API

    pxweb_api_url = "https://pxdata.stat.fi:443/PxWeb/api/v1/fi/StatFin/vaka/statfin_vaka_pxt_14jt.px"
    pxweb_query = """{
    "query": [
        {
        "code": "Vuosi",
        "selection": {
            "filter": "item",
            "values": [
            "2022"
            ]
        }
        },
        {
        "code": "Alue",
        "selection": {
            "filter": "item",
            "values": [
            "SSS",
            "KU020",
            "KU005",
            "KU009",
            "KU010",
            "KU016",
            "KU018",
            "KU019",
            "KU046",
            "KU047",
            "KU049",
            "KU050",
            "KU051",
            "KU052",
            "KU061",
            "KU069",
            "KU071",
            "KU072",
            "KU074",
            "KU075",
            "KU077",
            "KU078",
            "KU079",
            "KU081",
            "KU082",
            "KU086",
            "KU111",
            "KU090",
            "KU091",
            "KU097",
            "KU098",
            "KU102",
            "KU103",
            "KU105",
            "KU106",
            "KU108",
            "KU109",
            "KU139",
            "KU140",
            "KU142",
            "KU143",
            "KU145",
            "KU146",
            "KU153",
            "KU148",
            "KU149",
            "KU151",
            "KU152",
            "KU165",
            "KU167",
            "KU169",
            "KU171",
            "KU172",
            "KU176",
            "KU177",
            "KU178",
            "KU179",
            "KU181",
            "KU182",
            "KU186",
            "KU202",
            "KU204",
            "KU205",
            "KU208",
            "KU211",
            "KU213",
            "KU214",
            "KU216",
            "KU217",
            "KU218",
            "KU224",
            "KU226",
            "KU230",
            "KU231",
            "KU232",
            "KU233",
            "KU235",
            "KU236",
            "KU239",
            "KU240",
            "KU320",
            "KU241",
            "KU322",
            "KU244",
            "KU245",
            "KU249",
            "KU250",
            "KU256",
            "KU257",
            "KU260",
            "KU261",
            "KU263",
            "KU265",
            "KU271",
            "KU272",
            "KU273",
            "KU275",
            "KU276",
            "KU280",
            "KU284",
            "KU285",
            "KU286",
            "KU287",
            "KU288",
            "KU290",
            "KU291",
            "KU297",
            "KU300",
            "KU301",
            "KU304",
            "KU305",
            "KU312",
            "KU316",
            "KU317",
            "KU398",
            "KU399",
            "KU400",
            "KU407",
            "KU402",
            "KU403",
            "KU405",
            "KU408",
            "KU410",
            "KU416",
            "KU418",
            "KU420",
            "KU421",
            "KU422",
            "KU423",
            "KU425",
            "KU426",
            "KU444",
            "KU430",
            "KU433",
            "KU434",
            "KU435",
            "KU436",
            "KU440",
            "KU441",
            "KU475",
            "KU480",
            "KU481",
            "KU483",
            "KU484",
            "KU489",
            "KU491",
            "KU494",
            "KU495",
            "KU498",
            "KU499",
            "KU500",
            "KU503",
            "KU504",
            "KU505",
            "KU508",
            "KU507",
            "KU529",
            "KU531",
            "KU535",
            "KU536",
            "KU538",
            "KU541",
            "KU543",
            "KU545",
            "KU560",
            "KU561",
            "KU562",
            "KU563",
            "KU564",
            "KU309",
            "KU576",
            "KU577",
            "KU578",
            "KU445",
            "KU580",
            "KU581",
            "KU599",
            "KU583",
            "KU854",
            "KU584",
            "KU588",
            "KU592",
            "KU593",
            "KU595",
            "KU598",
            "KU601",
            "KU604",
            "KU607",
            "KU608",
            "KU609",
            "KU611",
            "KU638",
            "KU614",
            "KU615",
            "KU616",
            "KU619",
            "KU620",
            "KU623",
            "KU624",
            "KU625",
            "KU626",
            "KU630",
            "KU631",
            "KU635",
            "KU636",
            "KU678",
            "KU710",
            "KU680",
            "KU681",
            "KU683",
            "KU684",
            "KU686",
            "KU687",
            "KU689",
            "KU691",
            "KU694",
            "KU697",
            "KU698",
            "KU700",
            "KU702",
            "KU704",
            "KU707",
            "KU729",
            "KU732",
            "KU734",
            "KU790",
            "KU738",
            "KU739",
            "KU740",
            "KU742",
            "KU743",
            "KU746",
            "KU747",
            "KU748",
            "KU791",
            "KU749",
            "KU751",
            "KU753",
            "KU755",
            "KU758",
            "KU759",
            "KU761",
            "KU762",
            "KU765",
            "KU768",
            "KU777",
            "KU778",
            "KU781",
            "KU783",
            "KU831",
            "KU832",
            "KU833",
            "KU834",
            "KU837",
            "KU844",
            "KU845",
            "KU846",
            "KU848",
            "KU849",
            "KU850",
            "KU851",
            "KU853",
            "KU857",
            "KU858",
            "KU859",
            "KU886",
            "KU887",
            "KU889",
            "KU890",
            "KU892",
            "KU893",
            "KU895",
            "KU785",
            "KU905",
            "KU908",
            "KU092",
            "KU915",
            "KU918",
            "KU921",
            "KU922",
            "KU924",
            "KU925",
            "KU927",
            "KU931",
            "KU934",
            "KU935",
            "KU936",
            "KU946",
            "KU976",
            "KU977",
            "KU980",
            "KU981",
            "KU989",
            "KU992"
            ]
        }
        },
        {
        "code": "Ikä",
        "selection": {
            "filter": "item",
            "values": [
            "SSS",
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7"
            ]
        }
        },
        {
        "code": "Tiedot",
        "selection": {
            "filter": "item",
            "values": [
            "vaka_lapsi_lkm",
            "vko"
            ]
        }
        }
    ],
    "response": {
        "format": "csv"
    }
    }"""

    response_one = requests.post(pxweb_api_url, json=json.loads(pxweb_query))

    # For each municipality, count the total number of children and the number of foreign language children
    # in early childhood education between the ages of 0 and 7, and the share of the latter as a percentage 
    # of the former. Then turn this into a pandas DataFrame and rename the variables to be a bit more wieldy.
    #
    # Let's use "early childhood education" as a stand-in for daycare. I think theoretically only kids
    # between 0-6 are eligible for daycare, but in some cases there are kids in the age group 7 or above.
    # We can fix this later if we need to.

    daycare_df = pd.read_csv(io.StringIO(response_one.text)).drop(columns='Vuosi')
    daycare_df = daycare_df.rename(columns={
        'Alue': 'area',
        'Ikä': 'age',
        'Varhaiskasvatukseen osallistuneet lapset': 'children',
        'Vieraskieliset varhaiskasvatukseen osallistuneet lapset': 'foreign_language_children'
    })
    daycare_df_grouped = daycare_df.groupby('area').agg({
        'children': 'sum',
        'foreign_language_children': 'sum'
    }).reset_index()
    daycare_df_grouped['foreign_language_share'] = daycare_df_grouped.apply(
        lambda x: x['foreign_language_children'] / x['children'] * 100 if x['children'] != 0 else np.nan,
        axis=1
    )
    daycare_df_grouped['foreign_language_share'] = daycare_df_grouped['foreign_language_share'].round(1)

    # Download data from Statistics Finland's other API. This one returns GeoJSON, which is then used
    # to build a GeoDataFrame. Finally, merge the daycare data with the GeoDataFrame and write the whole
    # thing into a GeoJSON file that we can use with the Leaflet library.

    response_two = requests.get("https://geo.stat.fi/geoserver/wfs?service=WFS&version=2.0.0&request=GetFeature&typeName=vaestoalue:kunta_vaki2021&outputFormat=json")
    gdf = gpd.read_file(response_two.text)
    gdf = gdf.to_crs(epsg=4326).merge(daycare_df_grouped, left_on='nimi', right_on='area')
    gdf = gdf[['nimi', 'vaesto', 'children', 'foreign_language_children', 'foreign_language_share', 'geometry']]
    gdf = gdf.rename(columns={'nimi': 'area', 'vaesto': 'population'})

    # Create the 'data' directory if it doesn't exist and save the GeoJSON file there.
    os.makedirs('demo/public/data', exist_ok=True)
    gdf.to_file('demo/public/data/daycare_data.geojson', driver='GeoJSON')

if __name__ == '__main__':
    run()


