#잃어버린 괄호 - 1541번 - 실버2
import sys
from collections import deque
maximun_recursion = 1000000
sys.setrecursionlimit(maximun_recursion)

# 마이너스 기호를 만나면 다음 마이너스 기호가 나올때까지 괄호
if __name__ == "__main__":
    e = input()

    left = 0
    right = 0
    enable = False
    parse = ""
    for index, i in enumerate(e):

        if i == '-':
            if enable:
                right = right + int(parse)
            else:
                left = left + int(parse)
                enable = True
            parse = ''
        elif i == '+':
            if enable:
                right = right + int(parse)
            else:
                left = left + int(parse)
            parse = ''
        else:
            parse = parse + i

        if index == len(e)-1:
            if enable:
                right = right + int(parse)
            else:
                left = left + int(parse)

    print(left - right)
