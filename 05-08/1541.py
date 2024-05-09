#나는야 포켓몬 마스터 이다솜 - 1541번 - 실버2
import sys
di = dict()

m, n = map(int, sys.stdin.readline().split())

for i in range(1, m+1):
    temp = sys.stdin.readline().rstrip()
    di[temp] = str(i)
    di[str(i)] = temp

for i in range(n):
    print(di[sys.stdin.readline().rstrip()])
