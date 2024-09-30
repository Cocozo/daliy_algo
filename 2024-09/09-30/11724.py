import sys
from collections import deque

visited = []
linked = []

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    linked = [[] for i in range(n+1)]
    visited = [0 for i in range(n+1)]
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        linked[a].append(b)
        linked[b].append(a)
    
    c_c = 0
    for i in range(1, n+1):
        if visited[i] == 0:
            c_c += 1
            visited[i] = 1
            queue = deque([i])
            while queue:
                node = queue.popleft()
                for j in linked[node]:
                    if visited[j] == 0:
                        queue.append(j)
                        visited[j] = 1
    
    print(c_c)