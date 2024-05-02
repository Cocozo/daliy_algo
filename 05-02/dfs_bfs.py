#DFS와 BFS - 1260번 실버2
import sys
from collections import deque
limitNumber = 1000000
sys.setrecursionlimit(limitNumber)

MAX = 1001
edge_num = 0
edges = [[0 for i in range(MAX)] for i in range(MAX)]
visited = [0 for i in range(MAX)]

bfs_num = []
dfs_num = []

def dfs(edge):
    visited[edge] = 1
    print(edge, end=" ")
    for i in range(1, edge_num+1):
        if edges[edge][i] == 1 and visited[i] == 0:
            dfs(i)

def bfs(edge):
    q = deque([edge])
    visited[edge] = 1
    while q:
        s = q.popleft()
        print(s, end=" ")
        for i in range(1, edge_num+1):
            if edges[s][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = 1

if __name__ == "__main__" :
    edge_num, lines, start_line = map(int, input().split())

    for _ in range(lines):
        start, end = map(int, input().split())
        edges[start][end] = 1
        edges[end][start] = 1


    dfs(start_line)
    visited = [0 for i in range(MAX)]
    print()
    bfs(start_line)
