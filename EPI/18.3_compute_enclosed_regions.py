# Problem: Let A ve a 2D array whose entries are either W or B. Write a program that takes A,
#          and replaces all Ws that cannot reach the boundary with B.
from collections import deque

# EPI Judge: matrix_enclosed_regions.py
def fill_surrounded_regions(board):
    q = deque()
    m, n = len(board), len(board[0])

    for row in range(m):
        q.append((row, 0))
        q.append((row, n - 1))

    for col in range(1, n - 1):
        q.append((0, col))
        q.append((m - 1, col))

    while q:
        row, col = q.popleft()
        if 0 <= row < m and 0 <= col < n and board[row][col] == 'W':
            board[row][col] = 'V'
            neighbours = [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)]
            for rowN, colN in neighbours:
                q.append((rowN, colN))

    for row in range(m):
        for col in range(n):
            if board[row][col] == 'V':
                board[row][col] = 'W'
            else:
                board[row][col] = 'B'

    return board


if __name__ == "__main__":
    board = [['W', 'W', 'W', 'B', 'W', 'W', 'B', 'W', 'W', 'W', 'B', 'B', 'B', 'W', 'W'], 
            ['B', 'B', 'W', 'W', 'B', 'W', 'W', 'W', 'B', 'W', 'W', 'B', 'W', 'W', 'B'], 
            ['W', 'B', 'W', 'B', 'W', 'W', 'B', 'W', 'B', 'B', 'B', 'W', 'B', 'W', 'B'], 
            ['W', 'B', 'B', 'B', 'B', 'B', 'W', 'W', 'W', 'W', 'W', 'B', 'W', 'W', 'B'], 
            ['W', 'B', 'B', 'W', 'W', 'W', 'W', 'W', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
            ['B', 'W', 'B', 'W', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'W', 'W', 'B', 'B'], 
            ['B', 'W', 'B', 'B', 'B', 'W', 'B', 'W', 'W', 'B', 'B', 'W', 'W', 'W', 'W'], 
            ['B', 'W', 'W', 'W', 'W', 'W', 'B', 'B', 'W', 'W', 'B', 'B', 'W', 'B', 'W'], 
            ['B', 'W', 'B', 'B', 'B', 'W', 'W', 'W', 'W', 'B', 'W', 'W', 'B', 'B', 'B'], 
            ['W', 'B', 'W', 'B', 'W', 'W', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'W'], 
            ['B', 'B', 'B', 'W', 'B', 'W', 'W', 'B', 'B', 'W', 'B', 'B', 'B', 'W', 'B'], 
            ['W', 'W', 'W', 'B', 'B', 'B', 'W', 'W', 'W', 'W', 'B', 'W', 'W', 'B', 'B'], 
            ['W', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'B', 'B', 'B', 'B'], 
            ['B', 'W', 'W', 'W', 'W', 'B', 'W', 'W', 'B', 'W', 'B', 'W', 'W', 'W', 'B'], 
            ['B', 'B', 'W', 'B', 'W', 'B', 'B', 'W', 'B', 'B', 'B', 'W', 'W', 'B', 'W'], 
            ['W', 'B', 'W', 'W', 'B', 'W', 'W', 'W', 'B', 'W', 'B', 'B', 'B', 'W', 'W'], 
            ['B', 'B', 'W', 'W', 'W', 'W', 'B', 'W', 'W', 'W', 'B', 'W', 'W', 'B', 'B'], 
            ['W', 'W', 'W', 'W', 'B', 'B', 'B', 'W', 'B', 'B', 'W', 'W', 'W', 'B', 'W'], 
            ['W', 'B', 'W', 'W', 'W', 'W', 'B', 'W', 'W', 'B', 'W', 'W', 'W', 'B', 'B'], 
            ['B', 'W', 'W', 'B', 'W', 'W', 'W', 'W', 'B', 'W', 'B', 'W', 'W', 'W', 'W'], 
            ['W', 'W', 'B', 'W', 'B', 'B', 'W', 'W', 'W', 'W', 'B', 'W', 'B', 'W', 'W']]
            
    for row in board:
        print(row)
    board = fill_surrounded_regions(board)
    print()
    for row in board:
        print(row)