import pandas

PATH = "/home/ioannis/Bureau/PythonCourses/Day_026/NATO-alphabet-start/"

nato_dataframe = pandas.read_csv(PATH + "nato_phonetic_alphabet.csv")

nato_dictionnary = {
    row.letter: row.code
    for(index, row)
    in nato_dataframe.iterrows()
}

input = input("Enter a word so I may spell it!")

spelled_word = [nato_dictionnary[letter.upper()] for letter in input]

print(spelled_word)
