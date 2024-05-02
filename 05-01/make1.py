#1로 나누기 - 1463번 실버2
import sys
limitNumber = 1000000
sys.setrecursionlimit(limitNumber)

cnt = 0

save = [0 for i in range(1000001)]

if __name__ == '__main__' :
    num = int(input())

    for i in range(2, num+1):
        save[i] = save[i-1] + 1
        if i % 2 == 0:
            save[i] = min(save[i], save[i//2] + 1)
        if i % 3 == 0:
            save[i] = min(save[i], save[i//3] + 1)
    print(save[num])
