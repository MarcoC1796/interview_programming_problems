# Problem: implement an integer to string conversion function, and a string to integer conversion function.

def int_to_string(integer):
    if integer == 0:
        return "0"

    negative = ""
    if integer < 0:
        negative = "-"
        integer = -integer

    string = []
    while integer != 0:
        char = integer % 10
        string.append(chr(ord("0") + char))
        integer = integer // 10

    return negative + ''.join(reversed(string))

def string_to_int(string):
    digits = {chr(ord("0") + i): i for i in range(10)}
    negative = False
    if string[0] == '-':
        negative = True
        string = string[1:]
    elif string[0] == '+':
        string = string[1:]

    integer = 0
    for char in string:
        integer = integer * 10 + digits[char]
    return -integer if negative else integer

if __name__ == "__main__":
    integer = 4176473
    string = "+4176473"
    print(int_to_string(integer))
    print(string_to_int(string))
