import sys


dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

def find_tri(n):
    if dp[n] != 0:
        return dp[n]

    dp[n] = find_tri(n-1) + find_tri(n-5)
    
    return dp[n]


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    
    for _ in range(n):
        k = int(sys.stdin.readline().rstrip())
        print(find_tri(k))

# 6, 5, 1
# 7, 6, 2
# 8, 7, 3