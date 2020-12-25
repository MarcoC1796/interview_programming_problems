# Problem: write a prgram that takes an integer and determines if that integer's representation as a decimal string
#          is a palindrome:

import math

# EPI Judge: is_number_palindromic.py
def is_palindrome_number(x):
    if x <= 0:
        return x == 0

        # digits is a number 10 ^ n = x  ==>  n = floor(log10(x)) + 1
    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10 ** (num_digits - 1)

    for _ in range(num_digits // 2):
        msd = x // msd_mask
        lsd = x % 10
        if msd != lsd:
            return False
        # removing msd
        x = x % msd_mask
        # removing lsd
        x = x // 10
        num_digits -= 2
        msd_mask = 10 ** (num_digits - 1)

    return True

if __name__ == "__main__":
    tests = [0,1,7,11,121,333,2147447412,-1,12,100,2147483647]
    for x in tests:
        print(is_palindrome_number(x), end=" ")