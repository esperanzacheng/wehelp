# import urllib
import urllib.request as request
import json
import csv
import pandas as pd

# store the link as src
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data = pd.read_json(response)

alist = data["result"]["results"]

with open("data.csv", "w", encoding="utf-8", newline="") as file:
    for attraction in alist:
        if int(attraction["xpostDate"][0:4]) >= 2015:
            file.write(attraction["stitle"]+",")
            file.write(attraction["address"][5:8]+",")
            file.write(attraction["longitude"]+",")
            file.write(attraction["latitude"]+",")
            file.write(attraction["file"].split("jpg")[0]+"jpg"+"\n")