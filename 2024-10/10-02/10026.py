import sys
from collections import deque


board = []
visited = []
visited2 = []
area = []
n = 0
dir = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0]
]

def find_area(position, target):
    queue = deque()
    queue.append(position)
    
    while queue:
        y, x = queue.popleft()
        
        for dy, dx in dir:
            temp_y = y + dy
            temp_x = x + dx
            
            if temp_y >= 0 and temp_x >= 0 and temp_x < n and temp_y < n:
                if visited[temp_y][temp_x] == 0 and board[temp_y][temp_x] in target:
                    queue.append([temp_y, temp_x])
                    visited[temp_y][temp_x] = 1
                    
        

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    
    visited = [[0 for i in range(n)] for i in range(n)]
    result = []
    area = 0
    for _ in range(n):
        board.append(list(sys.stdin.readline().rstrip()))
    for i in range(len(board)):
        for j in range(len(board[i])):
            if visited[i][j] == 0:
                visited[i][j] = 1
                find_area([i, j], [board[i][j]])
                area += 1
                pass
            
    result.append(str(area))
    visited = [[0 for i in range(n)] for i in range(n)]
    area = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if visited[i][j] == 0:
                visited[i][j] = 1
                if board[i][j] in ["R", "G"]:
                    find_area([i, j], ["R", "G"])
                else:
                    find_area([i, j], [board[i][j]])
                area += 1
                pass

    result.append(str(area))
    
    print(" ".join(result))