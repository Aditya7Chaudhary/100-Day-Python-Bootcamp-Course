student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    print(key,value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    print(row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato_data_frame = pandas.read_csv(r"100-Day-Python-Bootcamp-Course\Day_026\NATO-alphabet-start\nato_phonetic_alphabet.csv")
letters = nato_data_frame.letter
code = nato_data_frame.code

dictionary = {letters[i]:code[i] for i in range(len(letters))} 


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def phonetic_code_words(word):
    alpha = [letter.upper() for letter in word]
    for i in range(len(alpha)):
        alpha[i] = dictionary[alpha[i]]
    print(alpha)

phonetic_code_words("Aditya")