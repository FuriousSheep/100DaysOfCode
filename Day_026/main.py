# EXO 1 ### LIST COMPREHENSION

# PATH = "/home/ioannis/Bureau/PythonCourses/Day_026/"

# with open(PATH + "file1") as file1:
#     data1 = [int(number.strip('\n')) for number in file1.readlines()]
# with open(PATH + "file2") as file2:
#     data2 = [int(number.strip('\n')) for number in file2.readlines()]

# result = [number for number in data1 if number in data2]
# print(result)

# EXO 2 ### DICTIONARY COMPREHENSION 1

# from random import randint
# names = ["Alexa", "Benjamin", "Carol", "David", "Elena", "Francis"]

# students_score = {name: randint(0, 100) for name in names}
# print(students_score)

# students_passed = {
#     key: value
#     for (key, value)
#     in students_score.items()
#     if value > 60
# }
# print(students_passed)

# EXO 3 ### DICTIONNARY COMPREHENSION 2

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# result = {word: len(word) for word in sentence.split(" ")}

# print(result)

### EXO 4 ###

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }


# def fahranheit(temp):
#     return (9/5 * temp + 32)


# weather_f = {key: fahranheit(value) for (key, value) in weather_c.items()}
# print(weather_f)

# EXO 4 ### ITERATION THROUGH A PANDAS DATAFRAME

# import pandas
# students_dict = {
#     "student": ["Angela", "Benjamin", "Carol"],
#     "score": [89, 72, 63]
# }
# students = pandas.DataFrame(students_dict)
# print(students)
# for (index, row) in students.iterrows():
#     if row.student == "Angela":
#         print(row.score)
