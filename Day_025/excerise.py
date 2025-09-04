import csv

"""
with open(r"100-Day-Python-Bootcamp-Course\Day_025\weather_data.csv","r") as file:
    data = csv.reader(file)
    temperature = []
    for row in data:
        if row[1] == 'temp':
            continue
        temp = int(row[1])
        temperature.append(temp)
    print(temperature)
"""

import pandas

data = pandas.read_csv(r"100-Day-Python-Bootcamp-Course\Day_025\weather_data.csv")
print(data,"\n")
print(data["temp"])
temperature = []
for i in data["temp"]:
    temperature.append(i)

print(temperature)