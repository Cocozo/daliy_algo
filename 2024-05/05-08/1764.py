#듣보잡 - 1764번 - 실버4
import sys
di = dict()

m, n = map(int, sys.stdin.readline().split())

for i in range(m):
    temp = sys.stdin.readline().rstrip()
    di[temp] = temp

result = []
for i in range(n):
    temp = sys.stdin.readline().rstrip()
    if temp in di:
        result.append(temp)

result.sort()
print(len(result))
for i in result:
    print(i)
    