import folium
import pandas as pd


freelancer_data = pd.read_csv('freelancers.csv')


map_1 = folium.Map(location=[29.7604,-95.3698], zoom_start=4)

for index, row in freelancer_data.iterrows():
    folium.Marker([row['latitude'], row['longitude']], popup=row['name'] + ", " +
                     "Rating: " + str(row['rating']) + ", " +
                     "Review Count: " + str(row['review_count']),
                      icon = folium.Icon(icon='cloud')).add_to(map_1)



map_1.save('freelance.html')
    

