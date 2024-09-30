import sys
from collections import deque

board = []
grows = []

dir = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0]
]

if __name__ == "__main__":
    m, n = map(int, sys.stdin.readline().split())
    
    start = []
    
    grows = [[0 for i in range(m)] for i in range(n)]
    board = [[0 for i in range(m)] for i in range(n)]
    for i in range(n):
        k = list(map(int, sys.stdin.readline().split()))
        for j in range(len(k)):
            board[i][j] = k[j]
            if k[j] == 1:
                start.append([i, j])
    
    queue = deque(start)    
    grow = 0
    while queue:
        y, x = queue.popleft()
        grow = grows[y][x]
        for dy, dx in dir:
            temp_y = y + dy
            temp_x = x + dx
            if temp_x >= 0 and temp_y >= 0 and temp_y < n and temp_x < m :
                if board[temp_y][temp_x] == 0:
                    queue.append([temp_y, temp_x])
                    board[temp_y][temp_x] = 1
                    grows[temp_y][temp_x] = grow + 1
    
    check_ungrown = False
    for i in board:
        if 0 in i:
            check_ungrown = True
            break
    
    if check_ungrown:
        print(-1)
    else:
        print(grow)
        