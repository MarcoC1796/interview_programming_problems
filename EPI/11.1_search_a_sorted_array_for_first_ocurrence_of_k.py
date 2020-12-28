# Problem: Write a method that takes a sorted array and a key and returns the index of the fisrt occurrence of that key
#          in the array. Return -1 fi the key does not appear in the array.

# EPI Judge: search_first_key.py
def search_first_of_k(A, k):
    index = -1
    L, U = 0, len(A) - 1
    while L <= U:
        M = L + (U - L) // 2
        if A[M] >= k:
            U = M - 1
            if A[M] == k:
                index = M
        else:
            L = M + 1
    return index

if __name__ == "__main__":
    A = [i for i in range(0,20,3)]
    K = [i for i in range(0,20)]
    print(A)
    for k in K:
        print(k,':',search_first_of_k(A, k))