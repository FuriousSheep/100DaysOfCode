import csv
from os import truncate
import pandas

ROUTE = "/home/ioannis/Bureau/PythonCourses/Day_025/"

# with open(ROUTE + "weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# data = pandas.read_csv(ROUTE + "weather_data.csv")
# print(data)
# sum = sum(data["temp"])
# average = round(sum/len(data["temp"]), 2)
# max = data["temp"].max()
# print(max)

# day = data[data.day == "Monday"]
# print(int(day.temp) * 9/5 + 32)

data = pandas.read_csv(
    ROUTE + "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

furs = data.groupby("Primary Fur Color")['Unique Squirrel ID'].count()
print(furs)

furs.to_csv("squirrel_furs.csv")
