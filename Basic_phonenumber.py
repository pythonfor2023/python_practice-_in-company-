

# import phonenumbers as ph             #ctrl+k+c
# import folium as fp
# import target  as number

from geopy.geocoders import Nominatim
import time
from pprint import pprint

# instantiate a new Nominatim client
app = Nominatim(user_agent="tutorial")

# get location raw data
location = app.geocode("Karnataka, Banglore").raw
# print raw data
pprint(location)







