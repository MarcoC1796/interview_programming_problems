# Problem: Write a program which takes text for an anonymous letter and text for a magazine and determines if it is
#          possible to write the anonynous letter using the magazine. The anonymous letter can be written as
#          using the magazine if for each character in the anonymous letter, the number of times it appears in the 
#          anonymous letter is no more than the number of times it appears in the magazine.
from collections import Counter

# EPI Judge: is_anonymous_letter_constructible.py
def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # Pythonic solution:
    #   letter = Counter(letter_text)
    #   magazine = Counter(magazine_text)
    #   return not (letter - magazine)
    letter_count = {}
    for char in letter_text:
        letter_count[char] = letter_count.get(char, 0) + 1

    for char in magazine_text:
        if char in letter_count:
            letter_count[char] -= 1
            if letter_count[char] == 0:
                del letter_count[char]
                if letter_count == {}:
                    return True

    return letter_count == {}

if __name__ == "__main__":
    letter = 'ncmynhdiycyijdzengtbzfkhykckxdaflmfncruyxkgbzbtlmqdjketkwoufpexcuhgpynwakgcfifujrvjmjkyuzhictuwhporekrvfctianhvnvwpseqndqypgevngaytzorngiujusksuddrqklrwoodvwlmducvurrvyltpgcauxhvrgqpqifmfsxjeldvoetxnaliyijoluyy'
    magazine = 'epzqrbcueuzjlfmtkvsrjilgbsoorawwtkgqdglowdknpstolbygncjqqcgibjhdvayjjxysctygaeykmlqxabgtxnsfcbtetsvtjomzravwhxizmcbqrycfvptgyqawkxiqhbfgkqsksxeckavxyofevzjwibsgvmskwvmwgoerqyyfxxredqvzlrrypaxmlcqkwvsjybqwigzuukfkzlfcmyohfxcjclqifefuyvrzmruuejtbiesaulimopegmyxvmvklqvvwqbdzuehsayyzbbkeyfosflktoxpautirjpgbjvzeeqhjgjnsfuyvaecklplfxsqrieqkfsqqealqnvcxfugtxrreqnxgugcmcyruvlvfthbeqratgmhdhcnnybjxkldhapywhidrcotfvjuwuxcnqrmt'
    print(is_letter_constructible_from_magazine(letter, magazine))
    letter = ""
    magazine = ""
    print(is_letter_constructible_from_magazine(letter, magazine))