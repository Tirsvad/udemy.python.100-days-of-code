import pandas

phonetic_dict = {row.letter: row.code for (index, row) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}
print([phonetic_dict[letter.upper()] for letter in input("Enter a word: ") if letter.isalpha()])
