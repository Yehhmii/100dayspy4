# with open("./Weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv
# with open("Weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas
# pandas has two datatype -DataFrame and Series-
# data = pandas.read_csv("Weather_data.csv")
# print(type(data)) --- has a type of dataframe
# print(type(data["temp"]))  --- has a type od series

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# To find the average or mean of our series
# Method A
# total = 0
# for num in temp_list:
#     total += num
# Method B
# total = sum(temp_list)
# average = total / len(temp_list)
# print(average)
# Method C
# print(data["temp"].mean())

# ==To find the maximum value==
# print(data["temp"].max())

# ==Get Data in columns==
# print(data["condition"])
# print(data.condition)

# ==Get Data in row==
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# print(monday_temp)
# monday_temp_in_F = monday_temp * 9/5 + 32
# print(monday_temp_in_F)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# our_data_frame = pandas.DataFrame(data_dict)
# our_data_frame.to_csv("new_data.csv")
