import pandas as pd

nato_data_frame = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}
name = input("Type a name: ")

for letter in name.upper():
    print( f"{letter} : {phonetic_dict[letter]}")