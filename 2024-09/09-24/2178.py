# 너비우선 탐색(BFS) - standard

import sys

from collections import deque
board = []
visited = []
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def find_road(n, m):
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = 1
    
    while queue:
        y, x = queue.popleft()
        depth = visited[y][x]
        for dy, dx in dir:
            tempY  = y + dy
            tempX = x + dx
            if tempY >= 0 and tempX >= 0 and tempY < n and tempX < m:
                if board[tempY][tempX] == 1 and visited[tempY][tempX] == 0:
                    queue.append([tempY,tempX])
                    visited[tempY][tempX] = depth + 1

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    
    for i in range(n):
        board.append(list(map(int,list(sys.stdin.readline().rstrip()))))
    
    visited = [[0 for _ in range(m)] for _ in range(n)]
    
    result = find_road(n, m)
    print(visited[n-1][m-1])