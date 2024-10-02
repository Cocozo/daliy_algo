import sys
from collections import deque

board = []
visited = []

dir = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0]
]

if __name__ == "__main__" :
    n, m = map(int, sys.stdin.readline().split())
    
    start = []
    visited = [[0 for i in range(m)] for i in range(n)]
    board = [[] for i in range(n)]
    for i in range(n):
        k = list(sys.stdin.readline().rstrip())
        for j in range(m):
            if k[j] == "I":
                start = [i, j]
                visited[i][j] = 1
            board[i].append(k[j])
    
    queue = deque()
    queue.append(start)
    meet = 0
    while queue:
        y, x = queue.popleft()
        
        for dy, dx in dir:
            temp_y = y + dy
            temp_x = x + dx
            
            if temp_y >= 0 and temp_x >= 0 and temp_x < m and temp_y < n:
                if visited[temp_y][temp_x] == 0 and board[temp_y][temp_x] != "X":
                    queue.append([temp_y, temp_x])
                    visited[temp_y][temp_x] = 1
                    if board[temp_y][temp_x] == "P":
                        meet += 1
    
    if meet != 0:
        print(meet)
    else:
        print("TT")