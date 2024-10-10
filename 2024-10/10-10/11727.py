import sys

dp = [0] * 10001
dp[1] = 1
dp[2] = 3

def create_dp(n):
    if dp[n] != 0:
        return dp[n]
    
    dp[n] = create_dp(n-1) + create_dp(n-2) * 2
    
    return dp[n]

if __name__ == "__main__" :
    n = int(sys.stdin.readline().rstrip())

    print(create_dp(n) % 10007)