# Problem: Write a program that takes two arrays representing integers, and returns and integer representing their
#          product. For example, since 193707721 x -761838257287 = -147574952589676412927 the function should return:
#          <-1,4,7,5,7,4,9,5,2,5,8,9,6,7,6,4,1,2,9,2,7>

# EPI Judge: int_as_array_multiply.py
def multiply(num1, num2):
    negative = 1
    if num1[0] * num2[0] < 0:
        negative = -1
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])

    len1 = len(num1)
    len2 = len(num2)

    multiplication = [0] * (len1 + len2)
    for index1 in reversed(range(len1)):
        for index2 in reversed(range(len2)):
            curr_mult = num1[index1] * num2[index2]
            curr_number = multiplication[index1 + index2 + 1] + curr_mult
            # len1 + len2 = len(multiplication) - 1
            multiplication[index1 + index2 + 1] = curr_number % 10
            multiplication[index1 + index2] += curr_number // 10
    i = 0
    while i < len(multiplication) and multiplication[i] == 0:
        i += 1

    multiplication = multiplication[i:] if i < len(multiplication) else [0]
    multiplication[0] = negative * multiplication[0]
    return multiplication

if __name__ == "__main__":
    num1 = [1,9,3,7,0,7,7,2,1]
    num2 = [-7,6,1,8,3,8,2,5,7,2,8,7]
    assert multiply(num1, num2) == [-1,4,7,5,7,3,9,5,2,5,8,9,6,7,6,4,1,2,9,2,7]
    num1 = [0]
    num2 = [0]
    assert multiply(num1, num2) == [0]
    num1 = [0]
    num2 = [1]
    assert multiply(num1, num2) == [0]
    num1 = [224342]
    num2 = [0]
    assert multiply(num1, num2) == [0]
    num1 = [-1, 3, 1, 4, 1, 2]
    num2 = [1, 3, 1, 3, 3, 3, 2]
    assert multiply(num1, num2) == [-1, 7, 2, 5, 8, 7, 5, 8, 4, 7, 8, 4]
    num1 = [-1,9,3,7,0,7,7,2,1]
    num2 = [-7,6,1,8,3,8,2,5,7,2,8,7]
    assert multiply(num1, num2) == [1,4,7,5,7,3,9,5,2,5,8,9,6,7,6,4,1,2,9,2,7]

        