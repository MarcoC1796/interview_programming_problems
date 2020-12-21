# Problem: Implement a Sudoku solver with all the usual contraints (see 5.17).

def solve_sudoku(partial_assignment):
    column_set_values = {i: set() for i in range(9)}
    row_set_values = {i: set() for i in range(9)}
    cell_set_values = {(i, j): set() for i in range(3) for j in range(3)}

    def test_validity(val, row, col):
        return not (val in column_set_values[col] or val in row_set_values[row] or val in cell_set_values[(row // 3, col // 3)])

    def set_value(val, row, col):
        column_set_values[col].add(val)
        row_set_values[row].add(val)
        cell_set_values[(row // 3, col // 3)].add(val)

    def remove_value(val, row, col):
        column_set_values[col].remove(val)
        row_set_values[row].remove(val)
        cell_set_values[(row // 3, col // 3)].remove(val)

    def get_next_entry(row, col):
        next_col = (col + 1) % 9
        next_row = row
        if next_col == 0:
            next_row = row + 1
        return next_row, next_col

    def initialize_sets():
        for row in range(9):
            for col in range(9):
                val = partial_assignment[row][col]
                if val != 0:
                    set_value(val, row, col)

    def set_next_entry(row, col):
        if row == 9:
            return True
        next_row, next_col = get_next_entry(row, col)
        if partial_assignment[row][col] == 0:
            for val in range(1, 10):
                if test_validity(val, row, col):
                    partial_assignment[row][col] = val
                    set_value(val, row, col)
                    if set_next_entry(next_row, next_col):
                        return True
                    partial_assignment[row][col] = 0
                    remove_value(val, row, col)
            return False

        return set_next_entry(next_row, next_col)

    initialize_sets()
    return set_next_entry(0, 0)

if __name__ == "__main__":
    partial_assignment = [[0, 3, 2, 0, 0, 0, 8, 0, 4], 
                          [8, 0, 0, 2, 0, 0, 0, 7, 0], 
                          [0, 1, 7, 0, 0, 5, 9, 0, 6], 
                          [5, 8, 0, 0, 2, 0, 0, 3, 0], 
                          [0, 0, 6, 0, 4, 0, 7, 0, 0], 
                          [0, 0, 4, 9, 1, 3, 0, 6, 0], 
                          [0, 0, 0, 7, 3, 0, 2, 0, 0], 
                          [0, 5, 9, 0, 0, 0, 0, 0, 1], 
                          [1, 0, 0, 8, 0, 9, 0, 0, 0]]
    solve_sudoku(partial_assignment)
    for row in partial_assignment:
        print(row)      
                
                    
