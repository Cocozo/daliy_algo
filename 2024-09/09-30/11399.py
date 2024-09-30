import sys

if __name__ == "__main__" :
    n = int(sys.stdin.readline().rstrip())
    l = list(map(int, sys.stdin.readline().split()))
    l.sort()
    
    sum = 0
    acc = 0
    for i in l:
        acc += i
        sum += acc
        
    print(sum)