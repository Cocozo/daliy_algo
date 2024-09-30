import sys
from collections import deque

MAX = 100001
a, b = map(int, input().split())
visited = [0 for k in range(MAX)]
q = deque([(a, 0)])
visited[a] = 1
while True:
    temp, dimention = q.popleft()
    if temp == b:
        print(dimention)
        break
    else:
        nodes = [temp + 1, temp - 1, temp * 2]
        for i in nodes:
            if i >= 0 and i < MAX and visited[i] == 0:
                q.append((i, dimention + 1))
                visited[i] = 1
