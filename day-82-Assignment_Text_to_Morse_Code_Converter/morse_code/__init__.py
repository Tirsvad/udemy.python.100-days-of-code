from .constants import *


class MorseCode:

    @staticmethod
    def encode(msg: str) -> str:
        msg_encoded = [MORSE_CODE[letter.upper()] for letter in msg]
        return " ".join(msg_encoded)

    @staticmethod
    def decode(msg: str) -> str:
        msg_split = msg.split(" ")
        msg_decoded = ""
        for code in msg_split:
            if code == "":
                msg_decoded += " "
            else:
                for key, value in MORSE_CODE.items():
                    if code == value:
                        msg_decoded += key
        return msg_decoded
