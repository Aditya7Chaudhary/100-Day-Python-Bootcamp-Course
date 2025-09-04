import pandas

data = pandas.read_csv(r"100-Day-Python-Bootcamp-Course\Day_025\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colours = data["Primary Fur Color"]

l = {}
for i in colours:
    if i not in l.keys():
        l[i] = 1
    l[i] += 1

dict = {}
color = []
count = []
for i in l:
    color.append(i)
    count.append(l[i])
color.pop(0)
count.pop(0)
dict["color"] = color
dict["count"] = count

df = pandas.DataFrame(dict)
print(df)
df.to_csv("100-Day-Python-Bootcamp-Course\Day_025\Colour-count")