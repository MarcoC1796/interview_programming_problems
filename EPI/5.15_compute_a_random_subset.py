# Problem: Write a program that takes as input a positive integer n and a size k <= n, and returns a size-k subset of
#          {0,1,2,...,n-1}. The subset should be represented as an array. All subsets should bee equally likely and, in 
#          addition, all permutations of elements of the array should be equally likely. You may assume you have a function
#          which takes as input a nonnegative integer t and returns an integer in the set {0,1,t-1} with
#          uniform probability.
from random import randint

# EPI Judge: random_subset.py
def random_subset(n, k):
    visited_indexes = dict()
    subset = []
    for i in range(k):
        rand_index = randint(i, n - 1)
        if rand_index in visited_indexes:
            subset.append(visited_indexes[rand_index])
        else:
            subset.append(rand_index)

        if i in visited_indexes:
            visited_indexes[rand_index] = visited_indexes[i]
            del visited_indexes[i]
        else:
            visited_indexes[rand_index] = i

    return subset

if __name__ == "__main__":
    print(random_subset(10,3))
        