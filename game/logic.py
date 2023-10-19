import random

board_size = 15
board = [[1 for _ in range(board_size)] for _ in range(board_size)]

def move_pointees():
    moves = [(0,1), (1,0), (0,-1), (-1,0)]
    new_board = [[0 for _ in range(board_size)] for _ in range(board_size)]
    
    for i in range(board_size):
        for j in range(board_size):
            move = random.choice(moves)
            new_i, new_j = i + move[0], j + move[1]
            if 0 <= new_i < board_size and 0 <= new_j < board_size:
                new_board[new_i][new_j] += board[i][j]
            else:
                new_board[i][j] += board[i][j]
                
    return new_board


