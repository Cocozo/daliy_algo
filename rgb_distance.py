#RGB거리 - 실버1 1149
import sys
limitNumber = 15000
sys.setrecursionlimit(limitNumber)

#지켜야할 규칙
#1번 집의 색은 2번 집의 색과 같지 않아야 한다.
#N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
#i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

values = []
minimum = []
EPOCH = 0
def find_minimum(n, prev_sel, acc):
    if n == EPOCH :
        return acc
    for i in range(3):
        if n != 0 and prev_sel == i :
            continue
        
        temp = acc+values[n][i]

        if temp < minimum[n]:
            minimum[n] = temp
    return temp 


if __name__ == "__main__":
    EPOCH = int(input())
    #RGB 리스트 만들기
    minimum = [10000001] * EPOCH

    for _ in range(EPOCH) :
        R,G,B = map(int, input().split())
        values.append([R, G, B])

    print(find_minimum(0, 0, 0))