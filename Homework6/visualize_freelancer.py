import folium
import pandas as pd

new_york_city_map = folium.Map(location=[40.7128,74.0059])
new_york_city_map.save('osm.html')


