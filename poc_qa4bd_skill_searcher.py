import requests
import json
from pprint import pprint
from fuzzywuzzy import fuzz, process
import pandas as pd


url =  "https://1928d475-a603-4e22-89a2-dbcdbaca4b1e.mock.pstmn.io"
path = "/skillsearcher/profiles"
session = requests.Session()
#body_response = session.get("{}{}".format(url, path)).text
#data_bio = json.loads(body_response)
#location_api = data["location"]
data_kimble = pd.read_csv("mockData.csv")
data_kimble = data_kimble.set_index('name')
profile = data_kimble['Miguel']
print(profile)