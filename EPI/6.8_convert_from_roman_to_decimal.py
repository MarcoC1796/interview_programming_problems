# Problem: Write a program which takes as input a valid Roman number string s and returns the
#          integer it corresponds to.

# EPI Judge: roman_to_integer.py
def roman_to_integer(s):
    symbols = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    number = 0
    i = 0
    while i < len(s):
        if i + 1 < len(s) and symbols[s[i]] < symbols[s[i+1]]:
            number += symbols[s[i + 1]] - symbols[s[i]]
            i += 2
        else:
            number += symbols[s[i]]
            i += 1
    return number

if __name__ == "__main__":
    strings = ['XXXXXIIIIIIIII', 'LVIIII', 'LIX', 'IXX', 'IVV']
    for string in strings:
        print(roman_to_integer(string))