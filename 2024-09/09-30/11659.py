import sys

accs = []
nums = []
if __name__ == "__main__" :
    n, m = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    accs = [0 for i in range(n+1)]
    
    acc = 0
    for i in range(n):
        acc += nums[i]
        accs[i+1] = acc
    
    for _ in range(m):
        i, j = map(int, sys.stdin.readline().split())
        print(accs[j] - accs[i-1])