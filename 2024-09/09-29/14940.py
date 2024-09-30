import sys
from collections import deque

board = []
visited = []

dir = [[0, 1], [1, 0], [0 , -1], [-1, 0]]

if __name__ == "__main__" :
    n, m = map(int, sys.stdin.readline().split())
    
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    board = [[] for _ in range(n)]
    start = []
    for i in range(n):
        k =list(map(int, sys.stdin.readline().split()))
        for j in range(len(k)):
            board[i].append(k[j])
            if k[j] == 0:
                visited[i][j] = 0
            if k[j] == 2:
                visited[i][j] = 0
                start = [i, j]
    
    queue = deque()
    queue.append(start)
    while queue:
        y, x = queue.popleft()
        distance = visited[y][x]
        
        for dy, dx in dir:
            tempY = y + dy
            tempX = x + dx
            if tempX >= 0 and tempY >= 0 and tempY < n and tempX < m:
                if visited[tempY][tempX] == -1 and board[tempY][tempX] == 1:
                    queue.append([tempY, tempX])
                    visited[tempY][tempX] = distance + 1
    
    for i in visited:
        print(" ".join(list(map(str, i))))