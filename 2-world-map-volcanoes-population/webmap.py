# folium is used for creating interactive maps - write python code and create HTML CSS and JS
import folium

# create a map object and pass in coordinates Map(location=[(-90 to 90),(-180 to 180)])
map = folium.Map(location=[38, -100], zoom_start=6)

# saves the map in the html file that is passed in as a parameter - this HTML file is generated for you
map.save("Map.html")