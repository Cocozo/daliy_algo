#피보나치 0,1 의 호출횟수 확인
import sys
limitNumber = 15000
sys.setrecursionlimit(limitNumber)

CALL1 = 0
CALL0 = 0
MAX = 41
save1 = [0] * MAX
save0 = [0] * MAX

def fibo(n) :
    global CALL1
    global CALL0
    if n == 0 :
        CALL0 = CALL0 + 1
    elif n == 1 :
        CALL1 = CALL1 + 1
    else :
        if save0[n] != 0 and save1[n] != 0 :
            CALL0 = CALL0 + save0[n]
            CALL1 = CALL1 + save1[n]
        else :
            fibo(n-1)
            fibo(n-2)
            save1[n] = CALL1
            save0[n] = CALL0




if __name__ == "__main__" :
    numbers = []
    save0[0] = 1
    save1[1] = 1
    epoch = int(input())
    for _ in range(epoch) :
        numbers.append(int(input()))
    for i in range(epoch) :
        CALL0 = 0
        CALL1 = 0
        fibo(numbers[i])
        print(f"{CALL0} {CALL1}")
