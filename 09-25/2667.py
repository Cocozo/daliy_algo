import sys;
from collections import deque

board = []
visited = []
n = 0

dir = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0]
]

def count_estate(i, j):
    queue = deque()
    queue.append([i, j])
    cnt = 1
    while queue:
        y, x = queue.popleft()
        estate_num = visited[y][x]
        for dy, dx in dir:
            tempY = y + dy
            tempX = x + dx
            if tempY >= 0 and tempX >= 0 and tempY < n and tempX < n:
                if visited[tempY][tempX] == 0 and board[tempY][tempX] == 1:
                    visited[tempY][tempX] = estate_num
                    queue.append([tempY, tempX])
                    cnt += 1
                    
    return cnt
            
            
if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    visited = [[0 for _ in range(n)] for _ in range(n)]
    
    for _ in range(n):
        board.append(list(map(int, list(sys.stdin.readline().rstrip()))))
    
    estate = []
    estate_num = 1
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = estate_num
                estate.append(count_estate(i, j))# bfs 알고리즘
                estate_num += 1
    
    estate.sort()
    print(len(estate))
    for i in estate:
        print(i)