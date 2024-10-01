import sys

n, m = map(int, sys.stdin.readline().split())

dic = {}

for _ in range(n):
    key, val = map(str, sys.stdin.readline().split())
    dic[key] = val

for _ in range(m):
    key = sys.stdin.readline().rstrip()
    print(dic[key])