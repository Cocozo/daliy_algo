#리모컨 - 1107번 골드5
import sys
limitNumber = 15000
sys.setrecursionlimit(limitNumber)

BUTTON = [str(i) for i in range(10)]
CH = 0
MAXDIGIT = 0
current_ch = 100
minimum = 0

def find_minimum(digit):
    global BUTTON
    global MAXDIGIT
    global CH
    global minimum

    if len(digit) == MAXDIGIT:
        return
    for _, num in enumerate(BUTTON) :
        temp_digit = digit + num
        cnt = len(temp_digit) + abs(int(temp_digit) - CH)

        if cnt < minimum :
            minimum = cnt

        find_minimum(temp_digit)


#해당 함수가 메인일 시 실행
if __name__ == "__main__" :
    CH = input()
    MAXDIGIT = len(CH) + 1
    CH = int(CH)
    epoch = int(input())
    if epoch != 0 :
        del_digit = input().split()
        for i in range(epoch) :
            del BUTTON[BUTTON.index(del_digit[i])]

    #주의해야할 점 -> 채널숫자가 100일 경우에도 확인해야함
    minimum = abs(CH - current_ch)
    find_minimum("")
    print(minimum)
