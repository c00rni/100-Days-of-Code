#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

base_letter = ""
with open("Input/Letters/starting_letter.txt", "r") as base_letter_file:
    base_letter = str(base_letter_file.read())

with open("Input/Names/invited_names.txt", "r") as names_file:
    for name in names_file:
        name = name.strip()
        with open(f'Output/ReadyToSend/{name}.txt', mode='w', encoding='utf-8') as new_letter_file:
            new_letter_file.write(base_letter.replace("[name]", name))