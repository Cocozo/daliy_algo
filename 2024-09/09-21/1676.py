import sys
MAX = 500

sum_1 = 0
sum_2 = 0
if __name__ == "__main__" :
    x = int(sys.stdin.readline().rstrip())
    for i in range(1,x+1):
        while i % 5 == 0:
            sum_1 += 1
            i = i // 5
        while i % 2 == 0:
            sum_2 += 1
            i = i // 2
        
    if sum_1 >= sum_2 :
        print(sum_2)
    else:
        print(sum_1)