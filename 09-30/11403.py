import sys
from collections import deque

graph = []
connected = []
if __name__ == "__main__" :
    n = int(sys.stdin.readline().rstrip())
    
    graph = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        k = list(map(int, sys.stdin.readline().split()))
        for j in range(len(k)):
            if k[j] == 1:
                graph[i][j] = 1
    
    for i in range(n):
        visited = [0 for i in range(n)]
        queue = deque([i])
        while queue:
            node = queue.popleft()
            for j in range(n):
                if graph[node][j] == 1 and visited[j] == 0:
                    queue.append(j)
                    visited[j] = 1
        connected.append(visited)

    for i in range(n):
        print(" ".join(list(map(str, connected[i]))))