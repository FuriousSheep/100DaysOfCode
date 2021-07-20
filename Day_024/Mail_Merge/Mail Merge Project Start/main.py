# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

DIRECTORY_ADDRESS = "/home/ioannis/Bureau/PythonCourses/Day_024/Mail_Merge/Mail Merge Project Start/"


def get_names():
    with open(DIRECTORY_ADDRESS + "/Input/Names/invited_names.txt") as file:
        names = file.readlines()
    return names


def map(list, fun):
    mapped_list = []
    for e in list:
        mapped_list.append(fun(e))
    return mapped_list


def strip_newline(str):
    return str.strip("\n")


def make_letters(names):
    with open(DIRECTORY_ADDRESS + "Input/Letters/starting_letter.txt") as file:
        template = file.read()
    for name in names:
        content = template.replace("[name]", name)
        with open(DIRECTORY_ADDRESS + f"/Output/ReadyToSend/{name}", "w") as file:
            file.write(content)


names = get_names()
print(names)
names = map(names, strip_newline)
print(names)
make_letters(names)
