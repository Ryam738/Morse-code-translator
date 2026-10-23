from constants import MORSE_CODE
import os, sys

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def read_regular(text: str):
    morsed = ""
    for char in text:
        if char.upper() not in MORSE_CODE:
            raise Exception(f"character {char.upper()} not supported")
        morsed += ' '
        morsed += MORSE_CODE[char.upper()]
    return morsed

def read_morse(text: str):
    regular = ""
    rev_MORSE_CODE = {}
    for key, value in MORSE_CODE.items():
        rev_MORSE_CODE[value] = key
    split_text = text.split(' ')
    for m_char in split_text:
        if m_char == '':
            continue
        if m_char not in rev_MORSE_CODE:
            raise Exception("character(s) not found")
        regular += rev_MORSE_CODE[m_char]
    return regular

def main():
    while True:
        clear_screen()
        type = input("translate regular or morse code?\n")
        if type != 'regular' and type != 'morse code':
            continue
        break
    clear_screen()
    text = input('please type or paste text below\n')
    if type == 'regular':
        clear_screen()
        print(read_regular(text))
    else:
        clear_screen()
        print(read_morse(text))
    sys.exit()

main()
