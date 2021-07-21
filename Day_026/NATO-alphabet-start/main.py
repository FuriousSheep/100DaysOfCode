import pandas

PATH = "/home/ioannis/Bureau/PythonCourses/Day_026/NATO-alphabet-start/"

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_dataframe = pandas.read_csv(PATH + "nato_phonetic_alphabet.csv")

nato_dictionnary = {
    row.letter: row.code
    for(index, row)
    in nato_dataframe.iterrows()
}
print(nato_dictionnary)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input = input("Enter a word so I may spell it!")

spelled_word = [nato_dictionnary[letter.upper()] for letter in input]

print(spelled_word)
