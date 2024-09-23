import sys


arr = []
time = []

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    for i in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        arr.append(temp)
    
    arr.sort(key=lambda time: (time[1], time[0]))
    
    prev_end = 0
    result = 0

    for i in arr:
        if result == 0:
            prev_end = i[1]
            result += 1
            continue
            
        if prev_end <= i[0]:
            prev_end = i[1]
            result += 1
    
    print(result)