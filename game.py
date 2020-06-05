import random
import sys
import click
from tabulate import tabulate

def initial_board():
    board = [[0 for i in range(4)] for j in range(4)]
    return board

def empty_board(board):
    empty = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                empty.append([i,j])
    return empty

def select_random(empty):
    return random.choice(empty)

def game_over(empty):
    if empty == []:
        return True
    else:
        return False

def put_2_4():
    if random.uniform(0,1) <= 0.7:
        return 2
    else:
        return 4

def arrow_keys():
    #print("waiting for ur move")
    c = click.getchar()
    key = 0
    if c == '\x1b[A':
        key = 1  #up key
    elif c == '\x1b[B':
        key = 2 #down key
    elif c == '\x1b[C':
        key = 3 #right key
    elif c == '\x1b[D':
        key = 4 #left key
    return key

def remove_empty(board, key):
    if key == 1:
        for i in range(4):
            column = []
            for j in range(4):
                if board[j][i] != 0:
                    column.append(board[j][i])
                board[j][i] = 0
            for j in range(len(column)):
                board[j][i] = column[j]
    elif key == 2:
        for i in range(4):
            column = []
            for j in range(3, -1, -1):
                if board[j][i] != 0:
                    column.append(board[j][i])
                board[j][i] = 0
            for j in range(len(column)):
                board[3-j][i] = column[j] 
    elif key == 3:
        for i in range(4):
            row = []
            for j in range(3, -1, -1):
                if board[i][j] != 0:
                    row.append(board[i][j])
                board[i][j] = 0
            for j in range(len(row)):
                board[i][3-j] = row[j]
    elif key == 4:
        for i in range(4):
            row = []
            for j in range(4):
                if board[i][j] != 0:
                    row.append(board[i][j])
                board[i][j] = 0
            for j in range(len(row)):
                board[i][j] = row[j]
    return board

def move(board):
    key = arrow_keys()
    board = remove_empty(board, key)
    for i in range(4):
        for j in range(3):
            if key == 1:
                if board[j][i] == board[j+1][i]:
                    board[j][i] += board[j+1][i]
                    board[j+1][i] = 0
            elif key == 2:
                if board[3-j][i] == board[2-j][i]:
                    board[3-j][i] += board[2-j][i]
                    board[2-j][i] = 0
            elif key == 3:
                if board[i][3-j] == board[i][2-j]:
                    board[i][3-j] += board[i][2-j]
                    board[i][2-j] = 0
            elif key == 4:
                if board[i][j] == board[i][j+1]:
                    board[i][j] += board[i][j+1]
                    board[i][j+1] = 0
    board = remove_empty(board, key)
    return board



def game(board, empty):  
    while(not(game_over(empty))):
        rand = select_random(empty)
        number = put_2_4()
        board[rand[0]][rand[1]] = number
        print(tabulate(board))
        sys.stdout.write("\033[F") 
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[F")
        board = move(board)  
        empty = empty_board(board)
    print("game over")

def start():
    board = initial_board()
    empty = empty_board(board)
    rand1 = select_random(empty)
    number1 = put_2_4()
    board[rand1[0]][rand1[1]] = number1
    empty = empty_board(board)    
    game(board, empty)



start()
