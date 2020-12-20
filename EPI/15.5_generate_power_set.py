# Problem: Write a function that takes as input a set and returns its power set
# input: [1,2,3]
# output: [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]

def generate_power_set(input_set):
    '''
    INPUT: 
        input_set: List[int], set of elements represented as a list
    OUTPUT:
        power_ser: List[List[int]], power set of input_set 
    '''
    # recursive rule: we compute all sets with curr_element and all sets withoud curr_element
    def generate_sets(curr_element, curr_set):
        if curr_element == len(input_set):
            power_set.append(curr_set[:])
        else:
            # with curr_element
            generate_sets(curr_element + 1, curr_set)
            # without curr_element
            curr_set = curr_set + [input_set[curr_element]]
            generate_sets(curr_element + 1, curr_set)

    power_set = []
    generate_sets(0, [])
    return power_set

if __name__ == "__main__":
    tests = [[1,2,3], [1,2,3,4,5,6]]
    for test in tests:
        print(generate_power_set(test))