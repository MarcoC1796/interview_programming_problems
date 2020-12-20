# Problem: How would you compute the parity of a very large number of 64-bit words?

def parity(x):
    shift = 32
    while shift > 0:
        x = x >> shift ^ x
        shift = shift // 2
    return x & 0x1

if __name__ == "__main__":
    from random import randint
    for i in range(10):
        current_value = ""
        real_value = 0
        for j in range(64):
            bit = randint(0,1)
            real_value += bit
            current_value = current_value + str(bit)
            
        test = parity(int(current_value,2))
        print(current_value, real_value % 2, test)