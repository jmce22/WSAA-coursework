# The task for this assignment was to print out the current temperature and wind direction at my location
# to my console by using an API from a weather website.
# I saved the data from the API as a json file on my machine called weatherdump.py, extracted the 
# desired information from this json file and printed it out to my console. 

import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=54.05&longitude=-6.44&current=temperature_2m,wind_direction_10m"
response = requests.get(url)

data = response.json()

# I used the below code to write the json file out into my assignments folder 
# so I could read it more easily. I commented it out as I don't need to
# write it each time this code is ran.
# with open ("weatherdump.json", "w") as fp:   
#    json.dump(data, fp)

current_temp = data["current"]["temperature_2m"]
current_temp_units = data["current_units"]["temperature_2m"]

current_wind_direction = data["current"]["wind_direction_10m"]
current_wind_direction_units = data["current_units"]["wind_direction_10m"]

# temperature is measured in degrees celsius and wind direction is measured in angular degrees
print(current_temp, current_temp_units)
print(current_wind_direction, current_wind_direction_units)
