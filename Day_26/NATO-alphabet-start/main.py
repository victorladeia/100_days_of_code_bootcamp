import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

letter_dic = {row.letter: row.code for (index, row) in df.iterrows()}

name = input("Enter a name: ")

code_list = [letter_dic[letter.upper()] for letter in name]

print(code_list)



#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

