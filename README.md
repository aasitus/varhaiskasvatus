# Foreign-language children in Finnish early childhood education

A simple interactive map that shows the proportion of kids who are not native speakers of Finnish, Swedish or Sami for Finland's municipalities. Uses data from Statistics Finland that's available [here](https://pxdata.stat.fi/PxWeb/pxweb/fi/StatFin/StatFin__vaka/statfin_vaka_pxt_14jt.px/) and [here](https://stat.fi/org/avoindata/paikkatietoaineistot.html).

Uses Python, Pandas and Geopandas to wrangle the data. The map can be visualized either as a Streamlit app available in st_app.py, or with Vite under demo/. In both cases, uses Leaflet to create the map.

## Instructions

1. Setup project:

```sh
npm create vite@latest demo . -- --template vanilla
cd demo
npm install
npm install leaflet
```

2. Setup a Python virtualenvironment, if you want to.

3. Install Python dependencies:

```sh
cd ..
pip install -r requirements.txt
```

4. Run data.py to setup the data:

```sh
python get_data.py
```

5. To see the demo, use either:

```sh
cd demo
npm run dev
```

or (in the root directory):

```sh
streamlit run st_app.py
```
