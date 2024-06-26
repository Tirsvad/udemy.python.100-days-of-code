from constants import TITLE
from morse_code import MorseCode

loop = True
while loop:
    print(TITLE)
    c = input("Press E for encode\n"
              "Press D for decode\n"
              "?")

    if c.upper() == "E":
        msg = input("Write message to encode:\n")
        msg_encoded = MorseCode.encode(msg)
        print(msg_encoded)
        loop = False
    elif c.upper() == "D":
        msg = input("Write message to decode:\n")
        msg_encoded = MorseCode.decode(msg)
        print(msg_encoded)
        loop = False
