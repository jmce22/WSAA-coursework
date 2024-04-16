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

print(current_temp, current_temp_units)
print(current_wind_direction, current_wind_direction_units)
