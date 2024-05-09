import pandas

phonetic_data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in phonetic_data.iterrows()}

loop = True
while loop:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only letters is valid")
    else:
        loop = False
        print(output_list)
