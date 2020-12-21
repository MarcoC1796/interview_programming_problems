# Problem: write a program that takes as arguments s 2D array and a 1D array, 
#          and checks whether the 1D array ocurrs in the 2D array.
#          We say that a 1D array ocurrs in a 2D array if it is possible to start from some entry in the 2D array
#          and traverse asjacent entries in the order specifiec by de 1D array till all entries in the 1D array have
#          been visited.

def is_pattern_contained_in_grid(grid, pattern):
    
    def get_adyacent(row, col):
        return [(row+1, col),(row-1, col),(row, col+1),(row, col-1)]

    def is_in_grid(row, col):
        return (0<=row<len(grid)) and (0<=col<len(grid[0]))

    def traverse_grid(curr_pattern_element, row, col):
        if curr_pattern_element == len(pattern):
            return True
        if is_in_grid(row, col):
            if (row, col, curr_pattern_element) not in visited_entires_with_pattern and\
                                                grid[row][col] == pattern[curr_pattern_element]:
                adyacents = get_adyacent(row, col)
                for adyacent in adyacents:
                    next_pattern_element = curr_pattern_element + 1
                    if traverse_grid(next_pattern_element, *adyacent):
                        return True

            visited_entires_with_pattern.add((row, col, curr_pattern_element))
        return False

    visited_entires_with_pattern = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if traverse_grid(0, row, col):
                return True

    return False

if __name__ == "__main__":
    grid = [[8, 11, 10, 16], 
            [9, 3, 10, 9], 
            [8, 25, 16, 16]]
    pattern = [8, 11, 10, 10, 16, 25]
    print(is_pattern_contained_in_grid(grid, pattern))

    grid = [[34]]
    pattern = [34]
    print(is_pattern_contained_in_grid(grid, pattern))