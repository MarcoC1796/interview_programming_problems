# Probelm: write a program which takes as input a string and returns the snakestring of s.

# EPI Judge: snake_string.py
def snake_string(s):
    sinusoidal_s = []
    def construct_s(start, stop, step):
        for i in range(start, stop, step):
            sinusoidal_s.append(s[i])

    construct_s(1, len(s), 4)
    construct_s(0, len(s), 2)
    construct_s(3, len(s), 4)

    return ''.join(sinusoidal_s)

if __name__ == "__main__":
    s = "Hello World!"
    print(snake_string(s))