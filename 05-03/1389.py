#케빈 베이컨의 6단계 법칙 - 1389번 - 실버1
import sys
from collections import deque
maximun_recursion = 1000000
sys.setrecursionlimit(maximun_recursion)
MAX = 101

relation = [[0 for i in range(MAX)] for i in range(MAX)]
level = [0 for i in range(MAX)]
visited = [0 for i in range(MAX)]
num = 0

def compute_relation(target):
    q = deque([target])
    visited[target] = 1
    rel_sum = 0
    while q:
        temp = q.popleft()
        for j in range(1, num+1):
            if relation[temp][j] == 1 and visited[j] == 0:
                #레벨에 따른 가중치 추가해야함
                level[j] = level[temp] + 1
                visited[j] = 1
                rel_sum += level[j]
                q.append(j)
    return rel_sum

if __name__ == '__main__':
    num, epoch = map(int, input().split())

    for i in range(epoch):
        a, b = map(int, input().split())
        relation[a][b] = 1
        relation[b][a] = 1
    min_num = 0
    min_rel = -1
    for i in range(1, num+1):
        level = [1 for i in range(MAX)]
        visited = [0 for i in range(MAX)]
        col = compute_relation(i)
        if col < min_rel or min_rel == -1:
            min_rel = col
            min_num = i

    print(min_num)
