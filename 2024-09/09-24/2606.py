import sys
from collections import deque

network = []
visited = []
if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    network = [[0 for i in range(n+1)] for i in range(n+1)]
    visited = [0 for i in range(n+1)]
    conn = int(sys.stdin.readline().rstrip())
    for _ in range(conn):
        x1, x2 = map(int, sys.stdin.readline().split())
        network[x1][x2] = 1
        network[x2][x1] = 1
    queue = deque()
    queue.append(1)
    visited[1] = 1
    result = 0
    while queue:
        node = queue.popleft()
        for i in range(n+1):
            if network[node][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                result += 1
    print(result)