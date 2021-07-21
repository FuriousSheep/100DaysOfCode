PATH = "/home/ioannis/Bureau/PythonCourses/Day_026/"

with open(PATH + "file1") as file1:
    data1 = [int(number.strip('\n')) for number in file1.readlines()]
with open(PATH + "file2") as file2:
    data2 = [int(number.strip('\n')) for number in file2.readlines()]

result = [number for number in data1 if number in data2]
print(result)
