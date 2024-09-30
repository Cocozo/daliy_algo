import sys

logs = []

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    logs = list(map(int, sys.stdin.readline().split()))
    
    logs.sort()
    logs.reverse()
    
    low = 0
    high = logs[0]
    res = 0
    while low <= high:
        mid = (low + high) // 2
        sum = 0
        for i in logs:
            sum += max(0, i - mid)
        
        if sum >= m:
            low = mid + 1
            res = mid
        else:
            high = mid -1
    
    print(res)