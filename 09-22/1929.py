import sys

def make_board(n):
    board = [0, 0]
    for i in range(n-1):
        board.append(1)
    return board

if __name__ == "__main__":
    m, n = map(int, sys.stdin.readline().split())
    board = make_board(n)
    
    for i in range(n+1):
        if board[i] == 1:
            # board[i] = 1
            for j in range(i * 2, n+1, i):
                board[j] = 0
    
    for i in range(n+1):
        if i >= m and board[i] == 1:
            print(i)