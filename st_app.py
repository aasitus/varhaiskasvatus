import geopandas as gpd
import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("Vieraskieliset lapset varhaiskasvatuksessa")

st.write("Klikkaa kuntaa nähdäksesi tarkempia tietoja.")

# Read data and initialize the Folium map

gdf = gpd.read_file('demo/public/data/daycare_data.geojson')
m = folium.Map(location=[65.5, 26], zoom_start=4.5, tiles=None)

# The map will show a popup with some extra information when a user
# clicks on a municipality. 

# Declare some fields and aliases for the popup.
popup_fields = [
    "area",
    "population",
    "children",
    "foreign_language_children",
    "foreign_language_share"
]
aliases=[
        "Kunta",
        "Väkiluku",
        "Lapsia varhaiskasvatuksessa",
        "Vieraskielisiä lapsia varhaiskasvatuksessa",
        "Vieraskielisten lasten osuus (prosenttia)"
]

# Create the popup
popup = folium.GeoJsonPopup(
    fields=popup_fields,
    aliases=aliases,
    localize=True,
    labels=True,
    style="background-color: white; color: black; font-family: arial; font-size: 12px; padding: 10px;"
)

# Create the choropleth itself. Let's color the municipality based on the
# share of foreign language children in early childhood education.
choropleth = folium.Choropleth(
    geo_data=gdf,
    name='choropleth',
    data=gdf,
    columns=['area', 'foreign_language_share'],
    key_on='feature.properties.area',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Vieraskielisten lasten osuus (prosenttia)'
).add_to(m)

# Add the popup to the choropleth
choropleth.geojson.add_child(popup)

# Show the name of the municipality when hovering over a municipality
folium.GeoJsonTooltip(fields=["area"], aliases=["Kunta"]).add_to(choropleth.geojson)

# Finally, use st_folium to display the map in the Streamlit app
st.data = st_folium(m, width=700)
