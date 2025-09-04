import csv

with open(r"100-Day-Python-Bootcamp-Course\Day_025\weather_data.csv","r") as file:
    data = csv.reader(file)
    temperature = []
    for row in data:
        print(row)