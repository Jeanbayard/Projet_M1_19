import folium
import requests
import pandas as pd

max_lati = 49.238
min_lati = 49.13
max_longi = -0.255
min_longi = -0.465

carte_de_france = 'https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png'
attribution = '&copy; OpenStreetMap France | &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>' \
              ' contributors'
m = folium.Map((49.1872, -0.3632), tiles=carte_de_france, attr=attribution, max_bounds=True, zoom_start=13,
               control_scale=True, zoom_control=False, min_lat=min_lati, max_lat=max_lati, min_lon=min_longi,
               max_lon=max_longi)


hopitaux = folium.FeatureGroup("Hopitaux au Caen").add_to(m)
folium.Marker(
    location=[49.205219, -0.357564],
    tooltip="Clique sur moi !",
    popup="CHU Caen Normadie",
).add_to(hopitaux)
folium.Marker(
    location=[49.203800, -0.353964],
    tooltip="Clique sur moi !",
    popup="Centre François Baclesse",
).add_to(hopitaux)
folium.Marker(
    location=[49.188911, -0.346212],
    tooltip="Clique sur moi !",
    popup="CHR Georges Clémenceau",
).add_to(hopitaux)
folium.Marker(
    location=[49.168171, -0.345710],
    tooltip="Clique sur moi !",
    popup="Maternité Polyclinique du Parc",
).add_to(hopitaux)
folium.Marker(
    location=[49.177364, -0.378199],
    tooltip="Clique sur moi !",
    popup="EPSM CAEN",
).add_to(hopitaux)
folium.Marker(
    location=[49.185257, -0.367124],
    tooltip="Clique sur moi !",
    popup="Clinique de La Miséricorde",
).add_to(hopitaux)
folium.Marker(
    location=[49.198387, -0.381535],
    tooltip="Clique sur moi !",
    popup="Hôpital Privé Saint Martin",
).add_to(hopitaux)


pompier = folium.FeatureGroup("Pompiers à Caen").add_to(m)
folium.Marker(
    location=[49.176754, -0.400672],
    tooltip="Clique sur moi !",
    popup="Pompiers",
).add_to(pompier)
folium.Marker(
    location=[49.208839, -0.374225],
    tooltip="Clique sur moi !",
    popup="Service Départemental D'incendie Et De Secours Du Calvados",
).add_to(pompier)
folium.Marker(
    location=[49.147568, -0.334210],
    tooltip="Clique sur moi !",
    popup="Pompiers",
).add_to(pompier)


police = folium.FeatureGroup("Police à Caen").add_to(m)
folium.Marker(
    location=[49.186733, -0.378578],
    tooltip="Clique sur moi !",
    popup="Commissariat de Police",
).add_to(police)
folium.Marker(
    location=[49.167320, -0.349170],
    tooltip="Clique sur moi !",
    popup="Commissariat de Police de Caen",
).add_to(police)
folium.Marker(
    location=[49.179070, -0.360427],
    tooltip="Clique sur moi !",
    popup="Police Nationale",
).add_to(police)
folium.Marker(
    location=[49.165325, -0.344946],
    tooltip="Clique sur moi !",
    popup="Gendarmerie Nationale",
).add_to(police)
folium.Marker(
    location=[49.175613, -0.322431],
    tooltip="Clique sur moi !",
    popup="Police Municipale",
).add_to(police)
folium.Marker(
    location=[49.176754, -0.400672],
    tooltip="Clique sur moi !",
    popup="police",
).add_to(police)
folium.Marker(
    location=[49.166912, -0.324888],
    tooltip="Clique sur moi !",
    popup="Bureau de Police Nationale",
).add_to(police)
folium.Marker(
    location=[49.204811, -0.329610],
    tooltip="Clique sur moi !",
    popup="Bureau de Police d'Hérouville Saint-Clair",
).add_to(police)

groupe_line = folium.FeatureGroup("Groupe des lignes", show=False).add_to(m)
line_in_Caen = [(max_lati, min_longi),
                (max_lati, max_longi),
                (min_lati, max_longi),
                (min_lati, min_longi),
                (max_lati, min_longi)]
folium.PolyLine(line_in_Caen, tooltip="Coast").add_to(groupe_line)

geojson_data = requests.get(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/world_countries.json").json()
folium.GeoJson(geojson_data, name="Carte découpé", show=False).add_to(m)

state_geo = requests.get(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json").json()
state_data = pd.read_csv(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_unemployment_oct_2012.csv")

folium.Choropleth(
    geo_data=state_geo,
    name="Etats des Etats-Unis",
    data=state_data,
    columns=["State", "Unemployment"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.5,
    line_opacity=0.3,
    legend_name="Unemployment rate (%)",
    show=False
).add_to(m)

folium.LayerControl().add_to(m)

m.save("index.html")
