import sys

MAX = 50

board = [0 for i in range(MAX)]

def check_redraw(y, x):
    letter = ''
    change = 0
    for i in range(y):
        checksum = 0
        for j in range(x):
            if i == 0 and j == 0:
                letter = board[i][j]
            elif i == 0 :
                if board[i][j] == letter:
                change += 1

if __name__ == "__main__" :
    n, m = map(int, sys.stdin.readline().split())
    for i in range(n):
        board[i] = sys.stdin.readline().rstrip()

    min = 0
    for i in range(m-8+1):
        for j in range(n-8+1):
            temp = check_redraw(i, j)
            if min > temp:
                min = temp
    
    print(min)