
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
file_invited_names = "./Input/Names/invited_names.txt"
file_starting_letter = "./Input/Letters/starting_letter.txt"
with open(file_starting_letter) as file:
    letter = file.read()
with open(file_invited_names) as names:
    for name in names.readlines():
        name = name.strip()
        new_letter = letter.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
            file.write(new_letter)
