import sys
from collections import deque

snake = [0 for _ in range(101)]
ladder = [0 for _ in range(101)]

visited = [-1 for i in range(101)]

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    
    for i in range(n):
        a, b = map(int, sys.stdin.readline().split())
        ladder[a] = b
    
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        snake[a] = b
    
    queue = deque([1])
    visited[1] = 0
    visit = 0
    while queue:
        position = queue.popleft()
        visit = visited[position]
        
        if position == 100:
            print(visited[position])
            break
        
        for dice in range(1, 7):
            temp = position + dice
                    
            if  temp <= 100 and visited[temp] == -1:                    
                
                if ladder[temp] != 0:
                    temp = ladder[temp]
                elif snake[temp] != 0:
                    temp = snake[temp]
                
                if visited[temp] == -1:
                    queue.append(temp)
                    visited[temp] = visit + 1