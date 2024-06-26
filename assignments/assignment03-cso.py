# The task for this assignment was to write a program that retrieves the dataset for 
# the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json"

import requests
import json

# Using RESTful API from available options
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

def getAll():
    response = requests.get(url)
    return response.json()
# .json ensures data in response is received in json format and that we can handle it as a dictionary in python

if __name__ == "__main__":
    with open ("cso.json", "wt") as fp:
        print(json.dumps(getAll()), file = fp)

# this code allows us to write the data from the API into a file called cso.json.
# the with statement ensures the file is closed after it is written

# Note: use Shift + Alt + F when viewing the outputted json file to format it in a more readible manner